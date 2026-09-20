# Content — sub-lead brief (under Systems)

Reports to: Systems · Directs: nothing · Updated: 2026-09-20

## Charter
What gets **included** in the game: data instances (abilities, characters, wounds, states, conditions, materials, scenes), assets (cut-outs, poses, diorama tiles, standees), animations, effects, text (names, rules text, wound names, log lines). Produces against Direction's clusters and Systems' schema; never invents a rule or a look.

## Owns
- `data/*.json` **instances** (not the schema) — `abilities`, `characters`, `wounds`, `states`, `conditions`, and new `materials`/`scenes` entries once the schema exists
- Asset production runs: `proposals/art/<date>-<topic>/` as *working* area; selected assets to a location Tech specifies (TBD, likely `demo/assets/`)
- The local image-gen pipeline as a *production* tool (`proposals/2026-09-20-local-imagegen-handoff.md`, ComfyUI workflows, `tools/annotate/` usage)
- `design/21-world-factions.md` content (factions, regions, names) — dormant until TARGET
- `sources/lore.md` as evidence for content, never as canon

## Does NOT own
- Schema, tag vocabulary, rules → Systems · what things should look like, which clusters exist → Direction · loaders, asset import → Tech

## Reads first
`AGENTS.md` → `00-steer.md` §4 (MVP IN list) → `leads/systems.md` status → `data/README.md` → `01-pillars.md` anti-goals → the Direction brief for the cluster in hand

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| C8, C12, C14, C17 | stars/training, gold as archetype signposts, magic traditions, Devotion — content-shaped once Systems fixes the schema | handoff §2 | waiting on Systems |
| — | handoff §5 #8: M1 content adds (`restrained`, Blood, Sand Shield fighter, place-sourced technique, `Brace`, one destructible + one creatable object) | handoff §5 | OPEN — owner to pick |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| 17 abilities, 2 fighters, ~12 wounds, 8 states, conditions | on disk, v1 schema | MVP | data/README |
| 17-ability lane table (Brute/Reader/Resolute/Duelist/Zealot/Mystic) | PROPOSED, in chat only — to be written into `12`/data | MVP | handoff §3.3 |
| Character cut-outs (Kaede, Genzo × 2 poses) | first target; smoketests exist, no accepted board | MVP (M1 restyle) | successor-review parallel track |
| Diorama tile | second target | M2 | — |
| Factions / regions / lore | dormant | TARGET/FUTURE | 21, sources |

## Next actions
1. Nothing until schema v3 direction is set — do not migrate JSON silently (data/README rule). Gate: Systems action 1–2.
2. Once Direction/art has an accepted style card: produce Kaede + Genzo, 2 poses each, via Qwen-Image-Edit; annotate; hand to Direction for critique. Gate: accepted style card.
3. Write the lane table into `data/abilities.json` (`_lane` field) when schema v3 lands. Gate: D-number for schema v3.

## Open questions
1. Where accepted assets live (Tech to specify).
2. Which of handoff §5 #8 adds are in M1.

## Escalates to
Systems for vocabulary/rules; Direction for taste; owner via Admin for scope.
