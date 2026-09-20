# Board annotator

Pin critique notes to regions of generated art, so feedback is anchored to
coordinates instead of whole-image prose. Feeds the art loop in
`design/00-steer.md` — boards land in `proposals/art/`, get annotated here, and
the annotations are read back when deciding the next edit.

## Run

```
python tools/annotate/server.py
```

Then open <http://127.0.0.1:8189>. Stdlib only — any Python 3.9+, including
ComfyUI's embedded interpreter at
`C:\tools\ComfyUI_windows_portable\python_embeded\python.exe`.

Port 8189 is chosen to stay clear of ComfyUI on 8188; override with `--port`.

## Use

- **Boards** (left) lists every image under `proposals/art/`, newest first, with
  a count of existing notes.
- **Pin** mode: click a spot. **Box** mode: drag a region.
- Type the note, pick a tag, hit **Save** (or `Ctrl+S`).
- `Delete` removes the selected marker when focus isn't in a textarea.

Tags match the axes the style distiller reports on, so critique and distillation
speak the same vocabulary: `line`, `palette`, `shading`, `silhouette`,
`proportion`, `composition`, `framing`, `texture`, `other`.

## Output

Saved beside each image as `<image>.annotations.json`:

```json
{
  "image": "2026-09-20-smoketest/qwen-smoketest_00001_.png",
  "image_size": [1328, 1328],
  "updated": "2026-09-20T21:13:52+00:00",
  "annotations": [
    {
      "id": "a1",
      "tag": "silhouette",
      "note": "Hair silhouette reads mushy - needs a cleaner cut-paper edge",
      "kind": "pin",
      "x": 0.4613, "y": 0.1304
    },
    {
      "id": "a2",
      "tag": "palette",
      "note": "Sash is the one place the palette breaks - too warm against the slate",
      "kind": "box",
      "x": 0.3140, "y": 0.5024, "w": 0.3574, "h": 0.1231
    }
  ]
}
```

Coordinates are **normalised 0–1** against the image's own dimensions, so they
survive resizing, re-export, and being read at a different display scale.
`image_size` records the pixel dimensions they were authored against.

`kind` is `pin` (x, y) or `box` (x, y, w, h), where x/y is the top-left corner.

## Acting on an annotation

`regional_edit.py` turns a saved annotation into a masked Qwen-Image-Edit run —
only the annotated region is regenerated, everything else is composited back
from the original.

```
python tools/annotate/regional_edit.py <board> --list
python tools/annotate/regional_edit.py <board> --id a2
python tools/annotate/regional_edit.py <board> --id a2 --fast
```

The annotation's **note is the instruction**, with a style-lock clause appended
so the model holds palette, outline weight and lighting.

> **Phrase notes as fixes, not diagnoses.** A note like *"sash is too warm"*
> gets read as a description of the target, and the model will happily make it
> warmer. Write *"make the sash the same slate as the tunic"* instead — or leave
> the diagnosis in the annotation for the record and pass the fix at run time
> with `--instruction`.

How it stays local:

- `SetLatentNoiseMask` confines denoising to the mask, so only that latent
  region is resampled.
- The **full** board is still passed as reference conditioning (`image1` on the
  text encoder), which is what keeps the regenerated patch stylistically in step
  with its surroundings.
- `ImageCompositeMasked` composites the result back over the original through
  the same mask, so pixels outside it are identical rather than merely close.

A `pin` annotation becomes a circular mask (`--pin-radius`, default 9% of the
short side); a `box` becomes a rectangle. Both are dilated (`--grow`) and
softened (`--feather`) so the seam doesn't read as a hard edge.

Output lands beside the source as `<stem>-<annotation id>_00001_.png`.
Use `--dry-run` to write the mask and print the graph without executing.

## Notes

- Paths are constrained to `proposals/art/`; traversal outside it is refused.
- The server binds to `127.0.0.1` only.
- There is no auth and no concurrency control — one person, one machine. Two
  browser tabs editing the same board will last-write-wins each other.
