"""Generate the Qwen ComfyUI workflows for this project.

Writes UI-format (litegraph) graphs to both ComfyUI's workflow folder and this
repo, so prompts and sampler settings stay diffable in git.

    python tools/workflows/build_workflows.py

Settings and the reason for each are in SETTINGS below. See
proposals/2026-09-20-local-imagegen-handoff.md for the research behind them.
"""
from __future__ import annotations

import json
import os

COMFY_WF = r"C:\tools\ComfyUI_windows_portable\ComfyUI\user\default\workflows"
REPO_WF = r"C:\Claude\shinobi-v2\proposals\art"

# --- settings -------------------------------------------------------------
# cfg 4.0: the Qwen-Image model card uses true_cfg_scale=4.0 and Segmind's guide
#   puts the useful band at 4-5. An earlier 2.5 here was an arbitrary choice.
# steps 20: "quick render" tier per the same guide; 50 for a final board.
# shift 3.1 (t2i) / 3.0 (edit): both are ComfyUI's shipped template defaults.
#   The difference is upstream and deliberate -- do not "harmonise" them.
# euler + simple: the official baseline. A 9-way sweep found karras visibly
#   broken on this flow-matching model and simple/sgm_uniform/beta equivalent.
# Lightning = 8 steps @ cfg 1.0: each Lightning LoRA is distilled for its own
#   step count and 8-step@8 beats 4-step@4. Never pair these with an ancestral
#   sampler -- few-step distilled models assume a deterministic path.
T2I_STEPS, T2I_CFG, T2I_SHIFT = 20, 4.0, 3.1
EDIT_STEPS, EDIT_CFG, EDIT_SHIFT = 20, 4.0, 3.0
FAST_STEPS, FAST_CFG = 8, 1.0
SIZE = 1328  # official 1:1 resolution

LORA_T2I = "Qwen-Image-Lightning-8steps-V2.0-bf16.safetensors"
LORA_EDIT = "Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors"
GGUF_T2I = "Qwen_Image-Q8_0.gguf"
GGUF_EDIT = "Qwen-Image-Edit-2509-Q8_0.gguf"
CLIP = "qwen_2.5_vl_7b_fp8_scaled.safetensors"
VAE = "qwen_image_vae.safetensors"

# Prose, not a keyword list. Qwen-Image reads prompts through a Qwen2.5-VL
# encoder rather than CLIP, and every guide asks for 1-3 plain sentences with
# the subject front-loaded. Comma-separated tag soup is the SDXL idiom and
# underuses the encoder.
T2I_POS = (
    "A full-body cut-paper illustration of a young female ninja, standing in a "
    "three-quarter view with her entire figure visible from head to feet. "
    "She is built from flat layered paper shapes with clean white cut edges and "
    "no gradient shading, in a restrained palette of slate greys and soft putty "
    "tones. She is isolated on a plain off-white background with a soft drop shadow."
)
T2I_NEG = "photographic, 3d render, gradient shading, busy background, text, watermark"

EDIT_POS = (
    "Turn the figure to face left in a full side profile. Keep the same character, "
    "the same flat cut-paper construction and white cut edges, the same slate and "
    "putty palette, and the same framing and scale with the whole figure visible."
)


# --- tiny litegraph builder ----------------------------------------------
def build(spec, wires, wid):
    nodes = {}
    for nid, ntype, pos, size, ins, outs, wv in spec:
        nodes[nid] = {
            "id": nid, "type": ntype, "pos": pos, "size": size, "flags": {},
            "order": nid - 1, "mode": 0,
            "inputs": [{"name": n, "type": t, "link": None} for n, t in ins],
            "outputs": [{"name": n, "type": t, "links": [], "slot_index": i}
                        for i, (n, t) in enumerate(outs)],
            "properties": {"Node name for S&R": ntype},
            "widgets_values": wv,
        }
    links = []
    for i, (src, sslot, dst, iname) in enumerate(wires, start=1):
        slot = next(k for k, inp in enumerate(nodes[dst]["inputs"]) if inp["name"] == iname)
        links.append([i, src, sslot, dst, slot, nodes[src]["outputs"][sslot]["type"]])
        nodes[src]["outputs"][sslot]["links"].append(i)
        nodes[dst]["inputs"][slot]["link"] = i
    return {"id": wid, "revision": 0, "last_node_id": max(nodes),
            "last_link_id": len(links), "nodes": list(nodes.values()),
            "links": links, "groups": [], "config": {}, "extra": {}, "version": 0.4}


def t2i(fast: bool):
    steps, cfg = (FAST_STEPS, FAST_CFG) if fast else (T2I_STEPS, T2I_CFG)
    prefix = "2026-09-20-smoketest/" + ("t2i-fast" if fast else "t2i")
    spec = [
        (1, "UnetLoaderGGUF", [40, 40], [400, 60], [], [("MODEL", "MODEL")], [GGUF_T2I]),
        (2, "CLIPLoader", [40, 260], [400, 110], [], [("CLIP", "CLIP")],
            [CLIP, "qwen_image", "default"]),
        (3, "VAELoader", [40, 410], [400, 60], [], [("VAE", "VAE")], [VAE]),
        (4, "ModelSamplingAuraFlow", [40, 510], [400, 60], [("model", "MODEL")],
            [("MODEL", "MODEL")], [T2I_SHIFT]),
        (5, "CFGNorm", [40, 610], [400, 80], [("model", "MODEL")],
            [("MODEL", "MODEL")], [1.0, False]),
        (6, "CLIPTextEncode", [490, 40], [470, 240], [("clip", "CLIP")],
            [("CONDITIONING", "CONDITIONING")], [T2I_POS]),
        (7, "CLIPTextEncode", [490, 320], [470, 140], [("clip", "CLIP")],
            [("CONDITIONING", "CONDITIONING")], [T2I_NEG]),
        (8, "EmptySD3LatentImage", [490, 500], [470, 110], [],
            [("LATENT", "LATENT")], [SIZE, SIZE, 1]),
        (9, "KSampler", [1010, 40], [340, 270],
            [("model", "MODEL"), ("positive", "CONDITIONING"),
             ("negative", "CONDITIONING"), ("latent_image", "LATENT")],
            [("LATENT", "LATENT")],
            [20260920, "randomize", steps, cfg, "euler", "simple", 1.0]),
        (10, "VAEDecode", [1010, 360], [340, 60],
            [("samples", "LATENT"), ("vae", "VAE")], [("IMAGE", "IMAGE")], []),
        (11, "SaveImage", [1010, 470], [490, 320], [("images", "IMAGE")], [], [prefix]),
    ]
    wires = [(2, 0, 6, "clip"), (2, 0, 7, "clip"), (4, 0, 5, "model"),
             (5, 0, 9, "model"), (6, 0, 9, "positive"), (7, 0, 9, "negative"),
             (8, 0, 9, "latent_image"), (9, 0, 10, "samples"), (3, 0, 10, "vae"),
             (10, 0, 11, "images")]
    if fast:
        spec.insert(1, (12, "LoraLoaderModelOnly", [40, 130], [400, 90],
                        [("model", "MODEL")], [("MODEL", "MODEL")], [LORA_T2I, 1.0]))
        wires += [(1, 0, 12, "model"), (12, 0, 4, "model")]
    else:
        wires += [(1, 0, 4, "model")]
    return build(spec, wires, "qwen-image-t2i-fast" if fast else "qwen-image-t2i")


def edit(fast: bool):
    steps, cfg = (FAST_STEPS, FAST_CFG) if fast else (EDIT_STEPS, EDIT_CFG)
    prefix = "2026-09-20-smoketest/" + ("edit-fast" if fast else "edit")
    # FluxKontextImageScale is REQUIRED, despite being the reason output comes
    # back ~1024 rather than at the source's size. Removing it was tried: the
    # output kept its native 1328 but the edit stopped happening -- mean abs
    # difference from the source fell from 20.99 (working edit) to 3.48
    # (effectively a copy). The node snaps the input into a resolution bucket
    # the model was trained on; outside it, conditioning collapses to
    # reconstruction. Accept the downscale on full-image edits, or use
    # tools/annotate/regional_edit.py when native resolution matters -- the
    # masked path forces resampling and works fine at 1328.
    spec = [
        (1, "UnetLoaderGGUF", [40, 40], [400, 60], [], [("MODEL", "MODEL")], [GGUF_EDIT]),
        (2, "CLIPLoader", [40, 260], [400, 110], [], [("CLIP", "CLIP")],
            [CLIP, "qwen_image", "default"]),
        (3, "VAELoader", [40, 410], [400, 60], [], [("VAE", "VAE")], [VAE]),
        (4, "LoadImage", [40, 510], [400, 380], [],
            [("IMAGE", "IMAGE"), ("MASK", "MASK")], ["kaede-smoketest.png", "image"]),
        (5, "ModelSamplingAuraFlow", [40, 930], [400, 60], [("model", "MODEL")],
            [("MODEL", "MODEL")], [EDIT_SHIFT]),
        (6, "CFGNorm", [40, 1030], [400, 80], [("model", "MODEL")],
            [("MODEL", "MODEL")], [1.0, False]),
        (14, "FluxKontextImageScale", [500, 40], [380, 60], [("image", "IMAGE")],
            [("IMAGE", "IMAGE")], []),
        (7, "TextEncodeQwenImageEditPlus", [500, 140], [470, 250],
            [("clip", "CLIP"), ("vae", "VAE"), ("image1", "IMAGE")],
            [("CONDITIONING", "CONDITIONING")], [EDIT_POS]),
        (8, "TextEncodeQwenImageEditPlus", [500, 430], [470, 150],
            [("clip", "CLIP"), ("vae", "VAE"), ("image1", "IMAGE")],
            [("CONDITIONING", "CONDITIONING")], [""]),
        (9, "VAEEncode", [500, 620], [400, 60],
            [("pixels", "IMAGE"), ("vae", "VAE")], [("LATENT", "LATENT")], []),
        (10, "KSampler", [1010, 40], [340, 270],
            [("model", "MODEL"), ("positive", "CONDITIONING"),
             ("negative", "CONDITIONING"), ("latent_image", "LATENT")],
            [("LATENT", "LATENT")],
            [20260920, "randomize", steps, cfg, "euler", "simple", 1.0]),
        (11, "VAEDecode", [1010, 360], [340, 60],
            [("samples", "LATENT"), ("vae", "VAE")], [("IMAGE", "IMAGE")], []),
        (12, "SaveImage", [1010, 470], [490, 320], [("images", "IMAGE")], [], [prefix]),
    ]
    wires = [(4, 0, 14, "image"), (14, 0, 9, "pixels"), (3, 0, 9, "vae"),
             (14, 0, 7, "image1"), (14, 0, 8, "image1"),
             (2, 0, 7, "clip"), (2, 0, 8, "clip"),
             (3, 0, 7, "vae"), (3, 0, 8, "vae"),
             (5, 0, 6, "model"), (6, 0, 10, "model"),
             (7, 0, 10, "positive"), (8, 0, 10, "negative"),
             (9, 0, 10, "latent_image"), (10, 0, 11, "samples"), (3, 0, 11, "vae"),
             (11, 0, 12, "images")]
    if fast:
        spec.insert(1, (13, "LoraLoaderModelOnly", [40, 130], [400, 90],
                        [("model", "MODEL")], [("MODEL", "MODEL")], [LORA_EDIT, 1.0]))
        wires += [(1, 0, 13, "model"), (13, 0, 5, "model")]
    else:
        wires += [(1, 0, 5, "model")]
    return build(spec, wires, "qwen-image-edit-fast" if fast else "qwen-image-edit")


def main():
    graphs = {
        "qwen-image-t2i": t2i(False),
        "qwen-image-t2i-fast": t2i(True),
        "qwen-image-edit": edit(False),
        "qwen-image-edit-fast": edit(True),
    }
    for name, wf in graphs.items():
        for path in (os.path.join(COMFY_WF, name + ".json"),
                     os.path.join(REPO_WF, name + ".workflow.json")):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(wf, f, indent=2)
        print("wrote", name)


if __name__ == "__main__":
    main()
