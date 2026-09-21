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

1. **Paper construction is missing in all twelve frames.** No layered sheets, no per-shape edge, no
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
