#!/usr/bin/env python3
"""Tile a board folder into the one PNG that is allowed into git (D5.28).

    python tools/contact_sheet.py 2026-09-20-river-nomads

Writes proposals/art/<topic>/_contact-sheet.png with every frame labelled by
filename, so critique can name a frame and the raw PNG behind it stays local.
"""
from __future__ import annotations

import argparse
import math
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
    args = ap.parse_args()

    folder = ART / args.topic
    frames = sorted(p for p in folder.glob("*.png") if p.name != "_contact-sheet.png")
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

    out = folder / "_contact-sheet.png"
    sheet.save(out)
    print(f"{out}  {sheet.width}x{sheet.height}  {len(thumbs)} frames")


if __name__ == "__main__":
    main()
