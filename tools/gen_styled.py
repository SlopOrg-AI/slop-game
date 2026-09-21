#!/usr/bin/env python3
"""Style-reference generation on Qwen-Image-Edit-2509 (handoff section 8 #3).

The open thread this closes: `TextEncodeQwenImageEditPlus` takes image1/image2/
image3 and nothing in this repo had ever used more than one. Prompt text alone
would not produce the layered cut-paper construction the art direction asks for
(proposals/art/2026-09-20-river-nomads/board.md), so the reference goes in as an
image instead of as adjectives.

    # new scene, style carried by a reference image
    python tools/gen_styled.py <board> --style <img> --mode fast

    # restyle an existing frame, composition carried by a second reference
    python tools/gen_styled.py <board> --style <img> --content <img> --mode full

<board> is a folder under proposals/art/ holding the instruction as
<prompt>.txt and negative.txt, same convention as tools/gen_board.py.
Reference paths are relative to proposals/art/ or absolute.

Every reference goes through ImageScaleToTotalPixels so the inputs share one
pixel budget -- the documented multi-image tip; unequal budgets are reported to
destabilise composition. Official guidance is 1-3 references, no more.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ART = Path(__file__).resolve().parents[1] / "proposals" / "art"
COMFY = Path(os.environ.get("SHINOBI_COMFY_ROOT", r"C:\tools\ComfyUI_windows_portable\ComfyUI"))
if not COMFY.is_dir():
    raise SystemExit(
        "ComfyUI not found at %s.\nImage generation runs on the PC with the RTX 5090 "
        "and nowhere else. Set SHINOBI_COMFY_ROOT if it is installed elsewhere here." % COMFY)
INPUT_DIR = COMFY / "input"
HOST = "http://127.0.0.1:8188"

GGUF = "Qwen-Image-Edit-2509-Q8_0.gguf"
CLIP = "qwen_2.5_vl_7b_fp8_scaled.safetensors"
VAE = "qwen_image_vae.safetensors"
LORA = "Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors"

SHIFT = 3.0               # the edit template's own default, not the t2i 3.1
FULL_STEPS, FULL_CFG = 20, 4.0
FAST_STEPS, FAST_CFG = 8, 1.0
SAMPLER, SCHEDULER = "euler", "simple"   # never ancestral with a Lightning LoRA
MEGAPIXELS = 1.0          # shared budget across references
SIZES = {"1:1": (1328, 1328), "16:9": (1664, 928), "9:16": (928, 1664),
         "4:3": (1472, 1140), "3:4": (1140, 1472)}


def stage(path: Path, tag: str) -> str:
    """Copy a reference into ComfyUI's input folder under a predictable name."""
    name = f"styleref-{tag}-{path.stem[:40]}{path.suffix}"
    shutil.copyfile(path, INPUT_DIR / name)
    return name


def graph(pos: str, neg: str, refs: list, latent: tuple, seed: int,
          fast: bool, prefix: str) -> dict:
    """refs[0] is the style reference; refs[1:] are content/character references.

    latent is ("empty", w, h) for a new scene, or ("image", node_id) to take the
    output size from an already-scaled reference.
    """
    steps, cfg = (FAST_STEPS, FAST_CFG) if fast else (FULL_STEPS, FULL_CFG)
    g = {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": GGUF}},
        "2": {"class_type": "CLIPLoader",
              "inputs": {"clip_name": CLIP, "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": VAE}},
    }
    enc = {"clip": ["2", 0], "vae": ["3", 0]}
    for i, name in enumerate(refs, start=1):
        load, scale = f"10{i}", f"11{i}"
        g[load] = {"class_type": "LoadImage", "inputs": {"image": name}}
        g[scale] = {"class_type": "ImageScaleToTotalPixels",
                    "inputs": {"image": [load, 0], "upscale_method": "lanczos",
                               "megapixels": MEGAPIXELS, "resolution_steps": 1}}
        enc[f"image{i}"] = [scale, 0]

    g["6"] = {"class_type": "TextEncodeQwenImageEditPlus", "inputs": dict(enc, prompt=pos)}
    g["7"] = {"class_type": "TextEncodeQwenImageEditPlus", "inputs": dict(enc, prompt=neg)}

    if latent[0] == "empty":
        g["8"] = {"class_type": "EmptySD3LatentImage",
                  "inputs": {"width": latent[1], "height": latent[2], "batch_size": 1}}
    else:
        g["8"] = {"class_type": "VAEEncode",
                  "inputs": {"pixels": [latent[1], 0], "vae": ["3", 0]}}

    g["4"] = {"class_type": "ModelSamplingAuraFlow",
              "inputs": {"model": ["12", 0] if fast else ["1", 0], "shift": SHIFT}}
    g["5"] = {"class_type": "CFGNorm", "inputs": {"model": ["4", 0], "strength": 1.0}}
    if fast:
        g["12"] = {"class_type": "LoraLoaderModelOnly",
                   "inputs": {"model": ["1", 0], "lora_name": LORA, "strength_model": 1.0}}
    g["9"] = {"class_type": "KSampler",
              "inputs": {"model": ["5", 0], "positive": ["6", 0], "negative": ["7", 0],
                         "latent_image": ["8", 0], "seed": seed, "steps": steps, "cfg": cfg,
                         "sampler_name": SAMPLER, "scheduler": SCHEDULER, "denoise": 1.0}}
    g["13"] = {"class_type": "VAEDecode", "inputs": {"samples": ["9", 0], "vae": ["3", 0]}}
    g["14"] = {"class_type": "SaveImage",
               "inputs": {"images": ["13", 0], "filename_prefix": prefix}}
    return g


def submit(g: dict) -> str:
    req = urllib.request.Request(HOST + "/prompt", data=json.dumps({"prompt": g}).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))["prompt_id"]
    except urllib.error.HTTPError as e:
        sys.exit("ComfyUI rejected the graph: " + e.read().decode()[:900])


def wait(pid: str, timeout: int = 1800) -> list:
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


def resolve(p: str) -> Path:
    q = Path(p)
    q = q if q.is_absolute() else ART / p
    if not q.exists():
        sys.exit(f"no such reference: {q}")
    return q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("--style", required=True, help="the style reference (image1)")
    ap.add_argument("--content", help="composition/character reference (image2); "
                                      "also sets the output size")
    ap.add_argument("--prompt", default="prompt", help="<name>.txt in the board folder")
    ap.add_argument("--mode", choices=("fast", "full"), default="fast")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--seed0", type=int, default=20260920)
    ap.add_argument("--aspect", choices=sorted(SIZES), default="16:9")
    ap.add_argument("--tag", default="", help="extra label in the output filename")
    args = ap.parse_args()

    folder = ART / args.topic
    pos = (folder / f"{args.prompt}.txt").read_text(encoding="utf-8").strip()
    negf = folder / f"negative-{args.prompt}.txt"
    neg = (negf if negf.exists() else folder / "negative.txt").read_text(encoding="utf-8").strip()

    refs = [stage(resolve(args.style), "style")]
    if args.content:
        refs.append(stage(resolve(args.content), "content"))
        latent = ("image", "112")      # the scaled second reference (node 11<i>, i=2)
    else:
        latent = ("empty",) + SIZES[args.aspect]

    label = args.tag or ("restyle" if args.content else "styleref")
    pids = []
    for i in range(args.seeds):
        seed = args.seed0 + i
        prefix = f"{args.topic}/{args.prompt}-{label}-{args.mode}-s{seed}"
        pids.append((seed, submit(graph(pos, neg, refs, latent, seed, args.mode == "fast", prefix))))
    print(f"queued {len(pids)} x {label}/{args.mode}, {len(refs)} reference(s)", flush=True)
    for seed, pid in pids:
        print(f"  seed {seed}: {' '.join(wait(pid))}", flush=True)


if __name__ == "__main__":
    main()
