#!/usr/bin/env python3
"""Queue a text-to-image board on the local ComfyUI (Qwen-Image).

One board = one folder under proposals/art/<topic>/ holding prompt.txt,
negative.txt and every frame generated from them, so a board is diffable and
re-runnable from what is on disk.

    python tools/gen_board.py 2026-09-20-river-nomads --mode fast --seeds 4
    python tools/gen_board.py 2026-09-20-river-nomads --mode full --seeds 2

Settings mirror tools/workflows/build_workflows.py; the reasoning for each is
there and in proposals/2026-09-20-local-imagegen-handoff.md section 6. Run all
the seeds of one mode before switching: swapping the Lightning LoRA in or out
forces a full model reload that costs more than the sampling.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ART = (Path(__file__).resolve().parents[1] / "proposals" / "art")
HOST = "http://127.0.0.1:8188"

GGUF = "Qwen_Image-Q8_0.gguf"
CLIP = "qwen_2.5_vl_7b_fp8_scaled.safetensors"
VAE = "qwen_image_vae.safetensors"
LORA = "Qwen-Image-Lightning-8steps-V2.0-bf16.safetensors"

SHIFT = 3.1
FULL_STEPS, FULL_CFG = 20, 4.0   # "quick render" tier; 50 for a final board
FAST_STEPS, FAST_CFG = 8, 1.0    # Lightning 8-step, never with an ancestral sampler
SAMPLER, SCHEDULER = "euler", "simple"  # karras is broken on this flow model

# Official Qwen-Image buckets. Off-bucket sizes degrade composition.
SIZES = {"1:1": (1328, 1328), "16:9": (1664, 928), "9:16": (928, 1664),
         "4:3": (1472, 1140), "3:4": (1140, 1472)}


def graph(pos: str, neg: str, w: int, h: int, seed: int, fast: bool, prefix: str) -> dict:
    steps, cfg = (FAST_STEPS, FAST_CFG) if fast else (FULL_STEPS, FULL_CFG)
    model = ["1", 0]
    g = {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": GGUF}},
        "2": {"class_type": "CLIPLoader",
              "inputs": {"clip_name": CLIP, "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": VAE}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": pos}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"clip": ["2", 0], "text": neg}},
        "8": {"class_type": "EmptySD3LatentImage",
              "inputs": {"width": w, "height": h, "batch_size": 1}},
        "9": {"class_type": "KSampler",
              "inputs": {"model": ["5", 0], "positive": ["6", 0], "negative": ["7", 0],
                         "latent_image": ["8", 0], "seed": seed, "steps": steps,
                         "cfg": cfg, "sampler_name": SAMPLER, "scheduler": SCHEDULER,
                         "denoise": 1.0}},
        "10": {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 0]}},
        "11": {"class_type": "SaveImage",
               "inputs": {"images": ["10", 0], "filename_prefix": prefix}},
    }
    if fast:
        g["12"] = {"class_type": "LoraLoaderModelOnly",
                   "inputs": {"model": ["1", 0], "lora_name": LORA, "strength_model": 1.0}}
        model = ["12", 0]
    g["4"] = {"class_type": "ModelSamplingAuraFlow", "inputs": {"model": model, "shift": SHIFT}}
    g["5"] = {"class_type": "CFGNorm", "inputs": {"model": ["4", 0], "strength": 1.0}}
    return g


def submit(g: dict) -> str:
    req = urllib.request.Request(HOST + "/prompt", data=json.dumps({"prompt": g}).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))["prompt_id"]
    except urllib.error.HTTPError as e:
        sys.exit("ComfyUI rejected the graph: " + e.read().decode()[:900])


def wait(pid: str, timeout: int = 1800) -> list[str]:
    start = time.time()
    while time.time() - start < timeout:
        h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
        if pid in h:
            st = h[pid].get("status", {})
            if st.get("status_str") == "error":
                sys.exit("execution failed: " + json.dumps(st)[:900])
            names = [i["filename"] for n in h[pid].get("outputs", {}).values()
                     for i in n.get("images", [])]
            return names + [f"{time.time() - start:.0f}s"]
        time.sleep(3)
    sys.exit("timed out waiting for ComfyUI")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic", help="board folder under proposals/art/")
    ap.add_argument("--mode", choices=("fast", "full"), default="fast")
    ap.add_argument("--seeds", type=int, default=4)
    ap.add_argument("--seed0", type=int, default=20260920)
    ap.add_argument("--aspect", choices=sorted(SIZES), default="16:9")
    args = ap.parse_args()

    folder = ART / args.topic
    pos = (folder / "prompt.txt").read_text(encoding="utf-8").strip()
    neg = (folder / "negative.txt").read_text(encoding="utf-8").strip()
    w, h = SIZES[args.aspect]
    fast = args.mode == "fast"

    pids = []
    for i in range(args.seeds):
        seed = args.seed0 + i
        prefix = f"{args.topic}/{args.mode}-s{seed}"
        pids.append((seed, submit(graph(pos, neg, w, h, seed, fast, prefix))))
    print(f"queued {len(pids)} x {args.mode} at {w}x{h}", flush=True)
    for seed, pid in pids:
        print(f"  seed {seed}: {' '.join(wait(pid))}", flush=True)


if __name__ == "__main__":
    main()
