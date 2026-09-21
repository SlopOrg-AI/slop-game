# Board — River Nomads settlement (exploration)

**Date:** 2026-09-20 · **Status:** PROPOSED, not accepted · **Scope:** FUTURE (world/location; not MVP)
**Cluster:** none — owner-directed one-off, not a Direction-defined cluster (`40-production.md` §2 step 1 skipped)
**Prompt source:** owner, this session. Rewritten to prose per the house prompt style; anti-goals moved out of the positive into the negative.

Raw frames are gitignored (D5.28). Committed: `_contact-sheet.png`, the four prompt/negative files, this file.

**One sheet per board, by accident of wording.** `.gitignore` and hook check C both match the literal
name `_contact-sheet.png`, so the per-variant sheets this board also produced
(`_contact-sheet-v3-fast.png` and friends) stay local and cannot be committed under any flag. The
committed sheet is therefore one frame per variant plus both 20-step frames. Whether D5.28 meant
"one sheet" or "sheets" is a rule question for Chief of Staff — not something to fix by widening
the check.

## What ran

| Variant | Prompt | Frames | Mode | Settings |
|---|---|---|---|---|
| v1 | `prompt.txt` + `negative.txt` | `prompt-fast-s2026092[0-3]` | 8-step Lightning | euler/simple, cfg 1.0, 1664×928, shift 3.1 |
| v2 | `v2.txt` + `negative-v2.txt` | `v2-fast-s2026092[0-3]` | same | same |
| v3 | `v3.txt` + `negative-v3.txt` | `v3-fast-s2026092[0-3]` | same | same |
| v3 final | `v3.txt` + `negative-v3.txt` | `v3-full-s2026092[0-1]` | 20 steps | euler/simple, cfg 4.0, 1664×928, shift 3.1 |

Seeds 20260920–23, identical across variants, so the only changed term is the prompt.
Settings from `tools/workflows/build_workflows.py`; run by `tools/gen_board.py`, sheets by `tools/contact_sheet.py`.

**Deviation from the shipped graphs:** 1664×928 (16:9) not 1328² — an official Qwen-Image bucket,
chosen because the subject is a settlement stretched linearly along a river. Noted rather than assumed.

## Critique — against `01-pillars.md`, by annotator axis

Axes are the annotator's tags (`tools/annotate/README.md`): line · palette · shading · silhouette · proportion · composition · framing · texture.

| Axis | v1 | v2 | v3 | Named row it answers to |
|---|---|---|---|---|
| palette | **holds** — muted indigo/ochre, one accent per figure | **drifts warm** — peach/tan dominant, indigo lost | **holds**, strongest of the three | owner brief; Ukiyo-e row (D5.16) |
| silhouette | featureless blobs — silhouette by absence, not design | **lost** — faces, hair, costume detail | **holds** — flat black standees, one accent each | Paper Mario row; pillar 4 |
| line | no cut edge at all | **over** — die-cut *sticker* outline around whole clusters | woodblock keyline, no cut edge | style card `2026-09-20-smoketest/style-card.md` |
| shading | flat, correct | flat, correct | flat, correct | style card |
| texture | grain overlay present | grain present | clean | style card ("smooth and uniform, lacking grain") |
| composition | one-point perspective, dock to vanishing point | same | same, but low water-level camera — the most Hiroshige-like | Ukiyo-e row |
| framing | 4/4 seeds near-identical | 4/4 near-identical | 4/4 near-identical | — |

**v3 at 20 steps / cfg 4.0 is a different picture, not a cleaner one.**
`_contact-sheet-v3-full.png` vs `_contact-sheet-v3-fast.png`, same prompt, same seeds:

| Axis | 8-step Lightning @ cfg 1.0 | 20-step @ cfg 4.0 |
|---|---|---|
| register | flat vector with a woodblock keyline | a genuine woodblock print — paper tone, ink bleed, aerial mist |
| silhouette | hard black standees, one accent each | softer silhouettes, depth-faded rear figures; **accent-per-figure mostly lost** (one red bundle) |
| texture | clean | **print grain throughout** — against the style card's "smooth and uniform, lacking grain" |
| the salvaged tech | boombox-shaped | one battered grey deck with a wire antenna — **the best anachronism-ceiling read on the board** |
| seal stamp | present in 3/4 | absent in 2/2 |

The two passes each win half the brief: Lightning holds the flat-graphic half (**Paper Mario** row),
20-step holds the Ukiyo-e half (**D5.16** row). Neither holds both. Treat that as a real result, not
a tuning gap — the brief asks one image to be flat cut paper *and* an atmospheric print.

### Rejections against a named row

1. **Paper construction is missing in all fourteen round-1 frames.** No layered sheets, no per-shape edge, no
   drop shadow between layers. v2's white outline was the model giving a sticker, not a cut-out.
   Fails the **Paper Mario** row ("cut-out material, layered flat sets, paper-doll pose/costume-layer
   construction", D5.19) and pillar 4. This is the board's main failure and it did not move under
   three prompt rewrites.
2. **A red seal stamp appears bottom-right in three v3 frames.** Direct hit on the anti-goal
   "No Japanese calligraphy motifs" (`01-pillars.md`). `japanese calligraphy, text, watermark` was
   in the negative and did not remove it.
3. **The cassette deck renders as a 1980s boombox** in v1/v2 and as a recognizable deck in v3.
   The **Naruto** row's anachronism ceiling is "vaguely recognizable"; pillar 5's anti-pillar is
   "recognizable modern/future tech". `boombox, stereo speakers` in the v3 negative did not remove it.
4. **Cogs and gears appeared on the dock in v1 seed 20260923** — steampunk creep, an explicit
   anti-goal. Adding them to the v2/v3 negative did clear it.

### What holds and is worth keeping

- Backdrop grammar: layered mist over water, hills as flat colour bands. Reads as the Ukiyo-e row
  wants and needs no further prompting.
- Silhouette-first crowd with one saturated accent per figure (v3). This is the closest thing on
  disk to a standee crowd, and it came from naming *"flat paper standees read as silhouettes first,
  dark simple shapes with almost no interior detail"* explicitly.
- The place reads: dock-as-street, nets, woven cargo, strung lanterns, boats as dwellings.

## Finding that outlives this board

Three prompt rewrites moved palette, silhouette and camera, and moved **paper construction not at
all** — the model gives flat vector or a sticker outline, never layered paper. Prompt text alone
looks insufficient for the material half of the art direction. Two paths already named in
`proposals/2026-09-20-local-imagegen-handoff.md` §8:

- open #3 — multi-image conditioning: feed a style reference alongside the prompt (`image1`/`image2`).
  Untested, and this is the case it exists for.
- `qwen-flat-color-v2` LoRA (§9) — flat colour, trained without lineart; partial fit.

Both are Content/Tech work, not a prompt fix. Recommending neither here — flagging that the next
attempt at cut-paper should not be another prompt rewrite.

## Next actions
1. Art lead: accept / return this board. Closest single frame to the brief's mood is
   `v3-full-s20260920`; closest to its *construction* is `v3-fast-s20260921`. Neither is both. Nothing here is canon; "River Nomads" has no faction doc
   (`grep` finds it only in the `01-pillars.md` Noir row).
2. If cut-paper is wanted from this pipeline, test the style-reference path (handoff §8 #3) before
   spending more prompt iterations.
3. Nothing in `design/` changes off this board.

---

# Round 2 — style reference instead of style adjectives

**Implements** the proposed change from the Next actions above and closes handoff open thread #3
(`proposals/2026-09-20-local-imagegen-handoff.md` §8): `TextEncodeQwenImageEditPlus` takes
image1/image2/image3 and nothing in this repo had ever passed more than one. Run by
`tools/gen_styled.py` on Qwen-Image-Edit-2509. Every reference goes through
`ImageScaleToTotalPixels` at 1.0 MP so the inputs share a pixel budget, per the documented tip.

**Style reference:** `2026-09-20-smoketest/qwen-smoketest_00001_.png` — the project's own cut-paper
figure, the image the style card was distilled from. Nothing new was downloaded or trained.

| Mode | Inputs | Prompt | Frames |
|---|---|---|---|
| `styleref` | style ref only, fresh latent at 1664×928 | `v4.txt` | `v4-styleref-fast-s2026092[01]`, `v4-styleref-full-s2026092[01]` |
| `restyle` | style ref + the best round-1 frame as image2 | `v5.txt` | `v5-restyle-fast-s2026092[01]` |

## Result: the style reference moved what three prompt rewrites could not

| Axis | round 1, prompt only | round 2, `styleref` | |
|---|---|---|---|
| composition | one-point perspective in 14/14 frames | **flat parallel layers, side on, no vanishing point** | fixed |
| line | no cut edge, or a sticker halo | **a true white cut edge on the boat and dock** | mostly fixed |
| silhouette | held in v3 | holds — standees with one accent each | held |
| palette | muted indigo/ochre | **drifts warm** — the reference's off-white ground bleeds into the sky | regressed |
| shading | flat | flat | held |
| paper layering | absent | **partial at 8 steps** — foreground gets a cut edge, water and sky stay flat vector | see below |

### At 20 steps / cfg 4.0 it stops being partial

`v4-styleref-full-s20260920` and `-s20260921` are **actual layered cut paper**: paper grain in every
shape, real drop shadows between layers, cut edges throughout, and in s20260920 the paper board the
whole scene is mounted on, casting its own shadow. Figures are paper standees. Hills are flat paper
bands. This is the **Paper Mario** row (cut-out material, layered flat sets, D5.19) and pillar 4's
terrain-table → diorama → cut-out grammar, produced rather than described — and s20260920 lands on
`AGENTS.md`'s own comp, "Paper Mario cut-outs on a wargame table", without being asked for it.

The 8-step Lightning LoRA is the wrong tool for this one. Round 1 found the two step counts split
the brief between them; with a style reference they do not — 20 steps wins outright, and cheaply
(57–75 s a frame, warm).

Still wrong in both 20-step frames: the palette is warm tan, not muted indigo/ochre, and the
one-saturated-accent-per-figure rule is gone — every standee is the same dark grey. Both are
palette, and both are what the style reference overrode.

Round 1's conclusion was that cut-paper "did not move under prompting". It moves under a reference
image. That is the finding: the construction half of the art direction is carried by an image input,
not by adjectives — which is what `01-pillars.md` implies anyway, since the Paper Mario row names a
*material*, and materials are shown, not described.

## `restyle` mode is not the one to use

Feeding the round-1 frame as image2 preserved its composition exactly and then wrapped every element
in the same **sticker halo** the v2 prompt produced — an outline around a cluster, not a cut edge on
a shape. It also came back at **1368×760 instead of 1664×928**: the 1.0 MP budget on the content
reference sets the output size. Same failure the handoff records for full-image edits, reached by a
different route. Both seeds are near-identical, so the content reference also flattens seed variety.

Use `styleref` (one reference, fresh latent) for new work. `restyle` earns its place only when an
existing composition must be kept, and then the output is smaller than the input.

## Carried over unfixed from round 1

- The cassette deck still renders as a recognizable 1980s object — now a bare cassette tape lying in
  the boat. Anachronism ceiling (Naruto row) and pillar 5 both still say "vaguely recognizable", and
  four negative-prompt terms have not shifted it. Next lever is an image reference for the prop, not
  more words.
- Palette control got *worse* with a style reference, because the reference carries a palette as
  well as a construction. Separating them — construction from image, palette from prompt — is the
  next experiment, and the obvious version is a second reference that is a palette swatch.

## Next actions (round 2)
1. Art lead: this is the first board on disk that answers the Paper Mario row. Accept
   `v4-styleref-full-s20260920` as the **construction** reference for the cut-paper register even if
   the palette is returned — the two are now separable levers.
2. Palette is the open lever. Next experiment is a second reference carrying palette only
   (a swatch or a round-1 frame), construction from the smoketest figure, palette from image2.
   One run, four frames.
3. The cluster this unblocks is `cutouts-m1` (Kaede, Genzo × 2 poses each,
   `leads/direction/art.md`), which is MVP and has been waiting on exactly this. A character
   reference plus the style reference is the same two-image call, now known to work.
4. Do not use 8-step Lightning for a cut-paper board. 20 steps at cfg 4.0, ~60 s a frame.
5. Nothing in `design/` changes off this board. River Nomads still has no faction doc.
