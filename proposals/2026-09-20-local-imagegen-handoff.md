# Local image-gen pipeline — handoff

**Date:** 2026-09-20 · **Status:** working end to end, settings not yet tuned
**Supersedes:** the "owner-run image gen via ChatGPT / 5090" line in `design/00-steer.md:21`

Art generation now runs locally on the 5090 instead of through ChatGPT. This
document is the context a successor needs to pick it up. Read
`tools/annotate/README.md` for the annotator specifically.

---

## 1. Why local

`proposals/2026-09-20-successor-review.md:58` defines the art loop as
image gen → `proposals/art/YYYY-MM-DD-<topic>/` → agent critique against the
`01-pillars` influence table → selected board decomposed into `31-ui`.

The generation step was the manual, off-machine part. The blocker for
"2 characters × 2 poses each" was **character consistency**: rerolling a prompt
gives a new character every time. Local Qwen-Image-**Edit** solves that —
you generate once and *edit* into new poses, holding identity.

---

## 2. Machine and install

| | |
|---|---|
| GPU | RTX 5090, 32 GB VRAM, driver 616.92, Blackwell sm_120 |
| RAM / CPU | 48 GB · Ryzen 5 3600 (the bottleneck for model loading, not sampling) |
| ComfyUI | `C:\tools\ComfyUI_windows_portable` — v0.36.0 portable |
| Torch | 2.13.0+cu130, CUDA 13.0, capability (12, 0) — works as shipped, no update needed |
| Python | ComfyUI's embedded interpreter at `python_embeded\python.exe`. System Python is 3.10 and is **not** used. |

Models are deliberately **outside** this repo (~62 GB).

Launch ComfyUI with output pointed at the repo:

```
C:\tools\ComfyUI_windows_portable\python_embeded\python.exe -s ^
  C:\tools\ComfyUI_windows_portable\ComfyUI\main.py --windows-standalone-build ^
  --output-directory "C:\Claude\shinobi-v2\proposals\art"
```

Serves on <http://127.0.0.1:8188>.

### Installed weights

| File | Where | Size |
|---|---|---|
| `Qwen_Image-Q8_0.gguf` | `models\diffusion_models` | 20.3 GiB |
| `Qwen-Image-Edit-2509-Q8_0.gguf` | `models\diffusion_models` | 20.3 GiB |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `models\text_encoders` | 8.7 GiB |
| `qwen3vl_8b_fp8_scaled.safetensors` | `models\text_encoders` | 9.9 GiB |
| `qwen_image_vae.safetensors` | `models\vae` | 0.24 GiB |
| `Qwen-Image-Lightning-4steps-V2.0-bf16.safetensors` | `models\loras` | 1.0 GiB |
| `Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors` | `models\loras` | 0.8 GiB |

Custom node: **ComfyUI-GGUF** (city96) + `gguf`, `sentencepiece`, `protobuf`
installed into the embedded Python.

### Two non-obvious facts that will waste your time

1. **GGUF files go in `models\diffusion_models`, not `models\unet`.**
   `ComfyUI-GGUF/nodes.py:32` resolves `unet_gguf` to `diffusion_models` first.
2. **The CLIPLoader `type` for Qwen3-VL is `ideogram4`.** Not a typo — Comfy
   keys loader types by architecture. Qwen-Image itself uses `qwen_image`.

---

## 3. Workflows

Saved in `ComfyUI\user\default\workflows\`, mirrored into
`proposals/art/*.workflow.json` so prompts and settings are diffable in git.
Open them via **Workflows (w)** in ComfyUI's left rail → Browse.

| Workflow | Purpose |
|---|---|
| `qwen-image-t2i` | text → image, 20 steps, 1328² |
| `qwen-image-t2i-fast` | same with Lightning 4-step LoRA |
| `qwen-image-edit` | image + instruction → image, 20 steps |
| `qwen-image-edit-fast` | same with Lightning 4-step LoRA |
| `style-distiller` | image → art-direction text (Qwen3-VL 8B) |

**Litegraph hides all node text below ~60% zoom.** A graph that looks like blank
grey boxes is loaded correctly — just zoom in. This wasted time once already.

---

## 4. Repo tools

### `tools/annotate/server.py` — board annotator

`python tools/annotate/server.py` → <http://127.0.0.1:8189>. Pin or box regions
of any board under `proposals/art/`, tag and note them; saves
`<image>.annotations.json` beside the PNG. Coordinates normalised 0–1.
Tags mirror the axes the style distiller reports on.

### `tools/annotate/regional_edit.py` — annotation → masked edit

```
python tools/annotate/regional_edit.py <board> --list
python tools/annotate/regional_edit.py <board> --id a2 --instruction "..."
```

Regenerates only the annotated region. `SetLatentNoiseMask` confines denoising;
the **full** board still goes in as reference conditioning so the patch stays in
style; `ImageCompositeMasked` restores everything outside the mask exactly.

**Verified:** on the smoke-test board only **5.11% of pixels changed**, and the
changed-pixel bbox `(405,655,904,843)` sat entirely inside the mask-plus-margin
limit `(377,627,931,870)`. Output stayed at native 1328² with no drift.

---

## 5. Verified results

| Run | Time | Note |
|---|---|---|
| t2i cold | 90 s | 21 GB off disk dominates; Ryzen 3600 is the limit |
| t2i warm, 20 steps | 36 s | 1.67 s/it |
| **t2i warm, 8-step Lightning** | **12 s** | 3× faster, cut-paper read holds — use for exploration |
| t2i, 8-step, first run after LoRA swap | 78 s | the LoRA forces a model reload; not the steady-state number |
| full-image edit, 20 steps | 51–119 s | returns ~1024², see pixel drift below |
| regional edit cold / warm | 141 s / 66 s | native 1328², zero drift |
| style distiller | ~90 s | |

Swapping between the plain and Lightning graphs forces a model reload each time,
which costs more than the sampling does. Batch work on one graph before
switching rather than alternating.

Evidence lives in `proposals/art/2026-09-20-smoketest/`.
`style-card.md` there is real distiller output.

---

## 6. Settings — what's set and how confident

Workflows are generated by **`tools/workflows/build_workflows.py`** — edit that
and re-run it rather than hand-editing the JSON. Each setting carries a comment
explaining why it holds the value it does.

| Setting | t2i | edit | Basis |
|---|---|---|---|
| sampler | `euler` | `euler` | official baseline; ComfyUI tutorials and Qwen's own HF discussion |
| scheduler | `simple` | `simple` | same |
| steps | 20 | 20 | "quick render" tier; use 50 for a final board |
| cfg | 4.0 | 4.0 | Qwen-Image model card `true_cfg_scale=4.0`; Segmind's band is 4–5 |
| shift | 3.1 | 3.0 | both are shipped template defaults — the difference is upstream, leave it |
| resolution | 1328² | native | official 1:1; edit runs at the source's own size |
| Lightning (`-fast`) | 8 steps @ cfg 1.0 | 8 steps @ cfg 1.0 | each LoRA is distilled for its own step count; 8-step@8 > 4-step@4. **Verified on t2i: 12 s warm, style holds.** The edit variant is still untested. |

### Sampler/scheduler sweep — actually run

9 combinations, fixed seed/prompt/steps/cfg. Contact sheet:
`proposals/art/2026-09-20-sampler-sweep/_contact-sheet.png` (individual frames
are gitignored).

- **`karras` is broken on this model.** `euler`+`karras` produced a washed-out,
  translucent, incomplete figure. Karras is an EDM sigma schedule for the
  SD1.5/SDXL family; Qwen-Image is rectified flow. Do not use it.
- **`euler_ancestral`+`simple` gave the best cut-paper read** — bolder flat
  shapes, cleaner white cut edge, stronger negative space.
- `simple` / `sgm_uniform` / `beta` with plain `euler` are near-identical.
  `res_multistep` and `dpmpp_2m` land in the same place.
- All ran 36 s; the 93 s on the first is cold load.

**Caveat: n=1 per cell.** Ancestral samplers inject noise, so at the same seed
they produce a *different image*, not a better-sampled one. The karras failure
is structural and will generalise; the ancestral advantage is one lucky draw
until someone runs 4 seeds × {euler, euler_ancestral}. **That test has not
been run.**

### Prompt style

Prompts are now **prose — 1–3 plain sentences, subject front-loaded**, not
comma-separated keyword lists. Qwen-Image reads prompts through a Qwen2.5-VL
encoder rather than CLIP, and every guide asks for sentences; tag soup is the
SDXL idiom and underuses the encoder. Changed on the strength of the
documentation rather than a controlled A/B, which has still not been run.

Do **not** adopt the official magic suffix `", Ultra HD, 4K, cinematic
composition."` — it pushes photographic realism, the opposite of the flat
cut-paper register.

---

## 7. Known issues

**Pixel drift / zoom is a named, documented Qwen-Image-Edit bug.** Full-image
edits shift, zoom, or crop relative to the input — this is why an early edit came
back 1024² with the figure cropped at mid-thigh.

**Do not "fix" it by removing `FluxKontextImageScale`.** That was tried and
measured. Without the node the output keeps its native 1328², but the edit stops
happening — mean absolute difference from the source fell from **20.99** (working
pose change) to **3.48** (effectively a copy). The node snaps the input into a
resolution bucket the model was trained on; outside that bucket the conditioning
collapses into reconstruction. It has been restored.

The real trade-off:

- **Full-image edits** keep `FluxKontextImageScale`, work correctly, and come
  back at ~1024². Upscale afterwards if you need more.
- **When native resolution matters**, use `tools/annotate/regional_edit.py`. The
  masked path forces resampling of the target region, so it edits correctly at
  1328² and measured zero drift. This is also what the published guidance calls
  the drift-free "local editing" pattern.
- Documented fallbacks if drift still bites: pad → resize to 1024 → edit →
  resize back → crop, or the `comfyui-qwen-zoom-fix` custom node.

**Annotation notes must be phrased as fixes, not diagnoses.** A note reading
"sash is too warm" was fed to the model verbatim and it made the sash *warmer* —
it read the description as the target. Re-running with "recolour the sash to the
same cool slate as the tunic" produced the right result. `--instruction`
overrides the note for this reason.

**Never use ancestral samplers with the Lightning LoRAs.** Few-step distilled
models assume a deterministic path; ancestral noise breaks them. The `-fast`
graphs must stay on `euler`.

**`denoise=1.0` can wash texture inside the mask.** ComfyUI issue #10710 reports
euler+simple at denoise 1.0 losing complex background texture in Qwen-Image-Edit
(closed as "not planned"). Harmless on flat cut-paper art; would bite on a
grainier board.

**The style distiller's `PROMPT:` line is a draft, not a paste.** On our test it
called a palette "monochromatic" when there was a clear tan note, and claimed
"subtle gradients" on flatter art. The prose `STYLE:` section is more reliable.

---

## 8. Open threads

1. **4-seed A/B of `euler` vs `euler_ancestral`** to settle whether ancestral is
   genuinely better or was one good sample.
2. **Prose vs keyword-list prompt A/B**, and cfg 2.5 vs 4.0. Four cells, ~5 min.
3. **Multi-image conditioning is wired but unused.**
   `TextEncodeQwenImageEditPlus` takes `image1`/`image2`/`image3`; official
   guidance is 1–3 inputs optimal. Community tip: run each reference through
   `ImageScaleToTotalPixels` so they share a pixel budget — this reportedly
   stabilises composition and style transfer. This is the path to feeding a
   character reference *and* a style reference at once.
4. **8-step Lightning may beat 4-step.** Each LoRA is distilled for its own step
   count; community consensus is 8-step at 8 steps > 4-step at 4 steps. We only
   downloaded the 4-step variants.
5. **Qwen-Image-Edit 2511 exists** and is reported to improve character
   consistency and reduce drift versus 2509 — directly relevant to the
   two-characters-two-poses goal. ComfyUI ships 2511 and 2512 templates. A 21 GB
   download, not a rethink.
6. **Update the docs.** `design/00-steer.md:21` and `design/40-production.md`
   still describe the ChatGPT-based loop.
7. **Q8 GGUF vs fp8** is roughly a wash in the community comparisons — Q8
   slightly faster and lighter on VRAM, fp8 occasionally sharper. Not worth
   revisiting unless VRAM becomes tight.

---

## 9. Sources

- [Qwen-Image model card](https://huggingface.co/Qwen/Qwen-Image) — official cfg/steps/resolutions
- [Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509) — multi-image, 1–3 inputs optimal
- [Qwen-Image-Edit-2511 blog](https://qwen.ai/blog?id=qwen-image-edit-2511) — consistency improvements
- [ComfyUI Qwen-Image-Edit docs](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)
- [ComfyUI issue #10710](https://github.com/comfyanonymous/ComfyUI/issues/10710) — denoise/texture limitation
- [MyAIForce: fixing pixel drift](https://myaiforce.com/fix-pixel-drift-for-qwen-edit/)
- [MyAIForce: QIE deep dive](https://myaiforce.com/qie-2511/) — sampler comparisons
- [Segmind prompt & parameter guide](https://blog.segmind.com/qwen-image-prompt-parameter-guide/)
- [Qwen-Image-Lightning](https://github.com/ModelTC/Qwen-Image-Lightning) · [8-step vs 4-step discussion](https://huggingface.co/lightx2v/Qwen-Image-Lightning/discussions/4)
- [qwen-flat-color-v2 LoRA](https://huggingface.co/motimalu/qwen-flat-color-v2) — flat colour, but trained *without* lineart; partial fit only
- [comfyui-qwen-zoom-fix](https://github.com/akramhusseini/comfyui-qwen-zoom-fix)

**Note on research coverage:** Reddit blocks our crawler, so r/StableDiffusion
and r/comfyui could not be read directly. Community findings above came via
aggregators, HF discussions, and GitHub issues. A successor with Reddit access
should check those subreddits for Qwen-Image-Edit pose/character-consistency
threads specifically.
