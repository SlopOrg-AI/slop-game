#!/usr/bin/env python3
"""Tile a board folder into the one PNG that is allowed into git (D5.28).

    python tools/contact_sheet.py 2026-09-20-river-nomads

Writes proposals/art/<topic>/_contact-sheet.png with every frame labelled by
filename, so critique can name a frame and the raw PNG behind it stays local.
"""
from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ART = Path(__file__).resolve().parents[1] / "proposals" / "art"
CELL = 640          # long edge of each thumbnail
PAD, LABEL = 12, 26
BG, FG = (28, 28, 30), (235, 235, 235)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("--cols", type=int, default=0, help="0 = square-ish")
    ap.add_argument("--glob", default="*.png", help="which frames to tile")
    ap.add_argument("--files", nargs="*", help="explicit frame names, instead of --glob")
    # D5.28 keeps exactly one PNG per board folder: the ignore rule and hook
    # check C both match the literal name _contact-sheet.png, so a sheet under
    # any other name stays local. Name the one that is meant to be committed.
    ap.add_argument("--out", default="", help="output name (default _contact-sheet.png)")
    args = ap.parse_args()

    folder = ART / args.topic
    if args.files:
        frames = [folder / n for n in args.files]
        missing = [str(f) for f in frames if not f.exists()]
        if missing:
            raise SystemExit("no such frame: " + ", ".join(missing))
    else:
        frames = sorted(p for p in folder.glob(args.glob) if not p.name.startswith("_"))
    if not frames:
        raise SystemExit(f"no frames in {folder}")
    cols = args.cols or math.ceil(math.sqrt(len(frames)))
    rows = math.ceil(len(frames) / cols)

    thumbs = []
    for p in frames:
        im = Image.open(p).convert("RGB")
        im.thumbnail((CELL, CELL), Image.LANCZOS)
        thumbs.append((p.name, im))
    cw = max(im.width for _, im in thumbs)
    ch = max(im.height for _, im in thumbs)

    sheet = Image.new("RGB", (cols * (cw + PAD) + PAD,
                              rows * (ch + LABEL + PAD) + PAD), BG)
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("consola.ttf", 15)
    except OSError:
        font = ImageFont.load_default()
    for i, (name, im) in enumerate(thumbs):
        x = PAD + (i % cols) * (cw + PAD)
        y = PAD + (i // cols) * (ch + LABEL + PAD)
        sheet.paste(im, (x + (cw - im.width) // 2, y))
        draw.text((x + 2, y + ch + 5), name, fill=FG, font=font)

    if args.out:
        out = folder / args.out
    elif args.files or args.glob == "*.png":
        out = folder / "_contact-sheet.png"
    else:
        slug = re.sub(r"[^A-Za-z0-9]+", "-", args.glob.replace(".png", "")).strip("-")
        out = folder / f"_contact-sheet-{slug}.png"
    sheet.save(out)
    print(f"{out}  {sheet.width}x{sheet.height}  {len(thumbs)} frames")


if __name__ == "__main__":
    main()
