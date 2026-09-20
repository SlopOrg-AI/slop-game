# Art direction — lead brief

Reports to: owner (via Production); umbrella `direction/README.md` · Directs: clusters → Content · Updated: 2026-09-20

## Charter
Authoritative on how the game **looks**: characters, costume, material (paper cut-out, ink over paper), palette, UI-as-animate-paper, the animatic camera register, the terrain-table → diorama → cut-out grammar. Holds the influence table and anti-goals as the test. Critiques every board; accepts or returns. Does not generate.

## Owns
- `design/30-art-direction.md` (stub → distill), `design/31-ui.md` (component library list D5.2 depends on)
- Style card acceptance (`proposals/art/<date>/style-card.md`) — the reference Content generates against
- Board critique in `tools/annotate/` vocabulary (`line palette shading silhouette proportion composition framing texture`)
- Proposing influence-table rows/edits (owner decides)

## Does NOT own
- Producing assets, running ComfyUI → Content · space layout → Level · what the fight is → Scenario · UI *behaviour*/implementation → Tech · rules → Systems

## Reads first
`AGENTS.md` → `01-pillars.md` (influence table, anti-goals — the whole job) → `00-steer.md` §1, §3 #2 → `decisions.md` D5.3, D5.4, D5.17–D5.19 → `proposals/art/2026-09-20-smoketest/style-card.md` → newest boards in `proposals/art/`

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | UI should feel like paper come to life, bold flat colour | D5.17 | DECIDED |
| — | animatic held-frame staging, not theater/puppets; Bunraku closed | D5.18 | DECIDED |
| — | 3D base model → generated flat 2D pose/costume pieces (paper-doll pipeline) | D5.19 | DECIDED |
| — | Ability selector: radial as starting point, targeting unsolved — resolve through image-gen + critique loop | D5.6 | OPEN → this lead + Tech |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Influence allocation table | DECIDED | all | D5.5, D5.16–D5.23 |
| `30-art-direction.md` | STUB | MVP (M2 for staging) | — |
| `31-ui.md` component list | STUB — M1 needs it | MVP | D5.2 |
| Style card | one smoketest card exists; not accepted | MVP | proposals/art |
| Cluster `cutouts-m1` (Kaede, Genzo × 2 poses) | to define | MVP | successor-review |
| Cluster `diorama-m2` (one tile) | to define | M2 | — |

## Next actions
1. Distill `31-ui.md` as the component library list: initiative/momentum strip, queue row, committed-ability slot, wound sheet, log, radial stub, standee, diorama tile — each with the pillar rows it must read against. Gate: none (Tech needs it for M1).
2. Accept or revise the style card; then write cluster `cutouts-m1` in handoff form. Gate: owner reacts to the card.
3. Distill `30-art-direction.md` from D5.3/D5.4/D5.17–D5.19 + `01` table. Gate: after 1.

## Open questions
1. Selector/targeting (D5.6, `00-steer` §6 #6).
2. UI numbers: raw vs bands (§6 #12) — with Systems' information model.
3. "Bodies, not bars" for mental/spiritual wounds in the same UI language (`01` open #2) — confirm at M2.

## Escalates to
Owner for any influence-table change; Systems when a look implies a rule.
