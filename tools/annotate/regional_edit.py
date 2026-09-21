"""Turn a saved annotation into a masked Qwen-Image-Edit run.

Reads <image>.annotations.json, renders a mask for one annotation, and asks
ComfyUI to regenerate only that region. Pixels outside the mask are composited
back from the original, so the rest of the board is bit-identical.

    python regional_edit.py 2026-09-20-smoketest/qwen-smoketest_00001_.png --id a2
    python regional_edit.py <board> --list
    python regional_edit.py <board> --id a1 --fast

Requires the ComfyUI server (default http://127.0.0.1:8188) and the models set
up for the qwen-image-edit workflow.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import time
import urllib.request
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = (HERE / ".." / ".." / "proposals" / "art").resolve()
# ComfyUI runs on the PC with the 5090 and nowhere else (D5.40); override with
# SHINOBI_COMFY_ROOT. Checked at import so an off-Windows run says why.
COMFY = Path(os.environ.get("SHINOBI_COMFY_ROOT", r"C:\tools\ComfyUI_windows_portable\ComfyUI"))
if not COMFY.is_dir():
    raise SystemExit(
        "ComfyUI not found at %s.\n"
        "Image generation runs on the PC with the RTX 5090 and nowhere else; this\n"
        "script cannot work from another machine. Set SHINOBI_COMFY_ROOT if it is\n"
        "installed somewhere else on this one." % COMFY
    )
INPUT_DIR = COMFY / "input"
HOST = "http://127.0.0.1:8188"

EDIT_GGUF = "Qwen-Image-Edit-2509-Q8_0.gguf"
EDIT_LORA = "Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors"
CLIP = "qwen_2.5_vl_7b_fp8_scaled.safetensors"
VAE = "qwen_image_vae.safetensors"

# Appended to every instruction: the model holds what you name and drifts on
# what you don't, and here we only ever want a local change.
STYLE_LOCK = ("Keep the existing art style, palette, outline weight, shading and "
              "lighting exactly as they are. Change nothing outside this region.")


def die(msg: str):
    print("error:", msg, file=sys.stderr)
    raise SystemExit(1)


def sidecar_for(img: Path) -> Path:
    return img.with_suffix(img.suffix + ".annotations.json")


def load_annotations(img: Path) -> list[dict]:
    side = sidecar_for(img)
    if not side.exists():
        die(f"no annotations beside {img.name} - annotate it first")
    return json.loads(side.read_text("utf-8")).get("annotations", [])


def render_mask(ann: dict, size: tuple[int, int], pin_frac: float) -> "Image.Image":
    from PIL import Image, ImageDraw
    w, h = size
    m = Image.new("RGB", size, "black")
    d = ImageDraw.Draw(m)
    if ann.get("kind") == "box":
        box = (ann["x"] * w, ann["y"] * h,
               (ann["x"] + ann["w"]) * w, (ann["y"] + ann["h"]) * h)
        d.rectangle(box, fill="white")
    else:
        r = min(w, h) * pin_frac
        cx, cy = ann["x"] * w, ann["y"] * h
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="white")
    return m


def build_graph(src_name: str, mask_name: str, prompt: str, out_prefix: str,
                steps: int, cfg: float, seed: int, grow: int, feather: int,
                fast: bool) -> dict:
    model_src = ["1", 0]
    g: dict = {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": EDIT_GGUF}},
        "2": {"class_type": "CLIPLoader",
              "inputs": {"clip_name": CLIP, "type": "qwen_image"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": VAE}},
        "4": {"class_type": "LoadImage", "inputs": {"image": src_name}},
        "5": {"class_type": "LoadImageMask",
              "inputs": {"image": mask_name, "channel": "red"}},
        "6": {"class_type": "GrowMask",
              "inputs": {"mask": ["5", 0], "expand": grow, "tapered_corners": True}},
        "7": {"class_type": "FeatherMask",
              "inputs": {"mask": ["6", 0], "left": feather, "top": feather,
                         "right": feather, "bottom": feather}},
    }
    if fast:
        g["20"] = {"class_type": "LoraLoaderModelOnly",
                   "inputs": {"model": ["1", 0], "lora_name": EDIT_LORA,
                              "strength_model": 1.0}}
        model_src = ["20", 0]

    g.update({
        "8":  {"class_type": "ModelSamplingAuraFlow",
               "inputs": {"model": model_src, "shift": 3.0}},
        "9":  {"class_type": "CFGNorm",
               "inputs": {"model": ["8", 0], "strength": 1.0}},
        # Full source as reference conditioning -- the model still sees the whole
        # board, which is what keeps the regenerated patch stylistically in step.
        "10": {"class_type": "TextEncodeQwenImageEditPlus",
               "inputs": {"clip": ["2", 0], "vae": ["3", 0], "image1": ["4", 0],
                          "prompt": f"{prompt} {STYLE_LOCK}"}},
        "11": {"class_type": "TextEncodeQwenImageEditPlus",
               "inputs": {"clip": ["2", 0], "vae": ["3", 0], "image1": ["4", 0],
                          "prompt": ""}},
        "12": {"class_type": "VAEEncode",
               "inputs": {"pixels": ["4", 0], "vae": ["3", 0]}},
        # Noise mask confines denoising to the annotated region.
        "13": {"class_type": "SetLatentNoiseMask",
               "inputs": {"samples": ["12", 0], "mask": ["7", 0]}},
        "14": {"class_type": "KSampler",
               "inputs": {"model": ["9", 0], "positive": ["10", 0],
                          "negative": ["11", 0], "latent_image": ["13", 0],
                          "seed": seed, "steps": steps, "cfg": cfg,
                          "sampler_name": "euler", "scheduler": "simple",
                          "denoise": 1.0}},
        "15": {"class_type": "VAEDecode",
               "inputs": {"samples": ["14", 0], "vae": ["3", 0]}},
        # Belt and braces: composite the result back over the original through the
        # same mask, so untouched pixels are guaranteed identical, not merely close.
        "16": {"class_type": "ImageCompositeMasked",
               "inputs": {"destination": ["4", 0], "source": ["15", 0],
                          "x": 0, "y": 0, "resize_source": False,
                          "mask": ["7", 0]}},
        "17": {"class_type": "SaveImage",
               "inputs": {"images": ["16", 0], "filename_prefix": out_prefix}},
    })
    return g


def submit(graph: dict) -> str:
    req = urllib.request.Request(
        HOST + "/prompt", data=json.dumps({"prompt": graph}).encode(),
        headers={"Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))["prompt_id"]
    except urllib.error.HTTPError as e:
        die(f"ComfyUI rejected the graph: {e.read().decode()[:800]}")


def wait(pid: str, timeout: int = 1800) -> list[str]:
    start = time.time()
    while time.time() - start < timeout:
        h = json.load(urllib.request.urlopen(f"{HOST}/history/{pid}"))
        if pid in h:
            entry = h[pid]
            st = entry.get("status", {})
            if st.get("status_str") == "error":
                die("execution failed: " + json.dumps(st)[:800])
            names = [i["filename"] for n in entry.get("outputs", {}).values()
                     for i in n.get("images", [])]
            print(f"  done in {time.time() - start:.1f}s")
            return names
        time.sleep(3)
    die("timed out waiting for ComfyUI")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("board", help="image path relative to proposals/art")
    ap.add_argument("--id", help="annotation id (e.g. a2)")
    ap.add_argument("--list", action="store_true", help="list annotations and exit")
    ap.add_argument("--instruction", help=(
        "use this instead of the annotation's note. Notes are often a diagnosis "
        "('sash is too warm') and the model reads that as the target rather than "
        "the complaint -- pass the fix ('make the sash the same slate as the tunic')"))
    ap.add_argument("--fast", action="store_true",
                    help="4-step Lightning LoRA instead of 20 steps")
    ap.add_argument("--steps", type=int)
    ap.add_argument("--cfg", type=float)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--grow", type=int, default=12, help="dilate mask, px")
    ap.add_argument("--feather", type=int, default=28, help="soften mask edge, px")
    ap.add_argument("--pin-radius", type=float, default=0.09,
                    help="pin mask radius as a fraction of the short side")
    ap.add_argument("--dry-run", action="store_true",
                    help="write the mask and print the graph, submit nothing")
    a = ap.parse_args()

    img = (ART / a.board).resolve()
    try:
        img.relative_to(ART)
    except ValueError:
        die("board must be inside proposals/art")
    if not img.exists():
        die(f"no such board: {img}")

    anns = load_annotations(img)
    if a.list or not a.id:
        print(f"{len(anns)} annotation(s) on {a.board}:")
        for x in anns:
            print(f"  {x['id']:4} [{x.get('tag','-'):11}] {x.get('kind'):4}  "
                  f"{x.get('note','').strip() or '(no note)'}")
        if not a.id:
            print("\npass --id <id> to run a regional edit")
        return

    ann = next((x for x in anns if x["id"] == a.id), None)
    if ann is None:
        die(f"no annotation {a.id} on that board")
    note = (a.instruction or ann.get("note") or "").strip()
    if not note:
        die(f"annotation {a.id} has no note - nothing to instruct the model with")
    if not a.instruction:
        print("note: using the annotation verbatim. If it reads as a diagnosis "
              "rather than a fix, pass --instruction.")

    from PIL import Image
    with Image.open(img) as im:
        size = im.size

    stamp = datetime.now().strftime("%H%M%S")
    src_name = f"regedit-src-{stamp}.png"
    mask_name = f"regedit-mask-{stamp}.png"
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(img, INPUT_DIR / src_name)
    render_mask(ann, size, a.pin_radius).save(INPUT_DIR / mask_name)

    steps = a.steps if a.steps is not None else (4 if a.fast else 20)
    cfg = a.cfg if a.cfg is not None else (1.0 if a.fast else 4.0)
    seed = a.seed or int(time.time()) % 2**31
    out_prefix = f"{Path(a.board).parent.as_posix()}/{img.stem}-{a.id}".lstrip("./")

    print(f"board   {a.board}  {size[0]}x{size[1]}")
    print(f"region  {ann['id']} [{ann.get('tag')}] {ann.get('kind')}")
    print(f"note    {note}")
    print(f"sampler {steps} steps, cfg {cfg}, seed {seed}"
          f"{'  (Lightning 4-step)' if a.fast else ''}")

    graph = build_graph(src_name, mask_name, note, out_prefix,
                        steps, cfg, seed, a.grow, a.feather, a.fast)
    if a.dry_run:
        print(json.dumps(graph, indent=2))
        print(f"\nmask written to {INPUT_DIR / mask_name}")
        return

    print("submitting…")
    for name in wait(submit(graph)):
        print(f"  -> proposals/art/{Path(out_prefix).parent.as_posix()}/{name}")


if __name__ == "__main__":
    main()
