# Systems — lead brief

Reports to: owner (via Production) · Directs: `systems/content.md`, `systems/engine.md` · Updated: 2026-09-20

## Charter
The game itself: **what exists** (ontology — entities, actor kinds, sheets, pools, tag dictionary, materials, scenes/zones, naming) and **how it resolves** (rules — Plan→Resolve, precedence, momentum, damage→mint, information, chemistry, Push). Scale-generic by pillar 6: campaign and world systems are the same rules at scale 2–4, not a second sim. Arbitrates vocabulary for every other lead; the ontology is Engine's contract.

## Owns
- `design/02-ontology.md` (to create), `data/SCHEMA.md`, `data/tags.json`, `data/materials.json`, sheets/pools definitions
- `design/10–15` (combat/information), `20-campaign`, `50-world-systems`
- `design/decisions.md` edits **on owner instruction only** (rule 4)
- Schema versions (one D-number per bump); the validator's *rules* (Engine writes the script)

## Does NOT own
- Instances (which 17 abilities, Kaede/Genzo, factions, lore) → Content · Godot code → Engine · look/feel, space *aesthetics*, encounter authoring → Direction · milestones → Production

## Reads first
`AGENTS.md` → `00-steer.md` → `01-pillars.md` → `proposals/2026-09-20-session-6-handoff.md` (§2 C-refs, §3 model, §4 corrections) → `…-ontology-draft.md` → `decisions.md` latest → the one doc being touched

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| C1–C20 | see `proposals/2026-09-20-session-6-handoff.md` §2 — owner direction on reactions-as-abilities, RPS precedence, no modes, tag dictionary, materials, damage tags+numbers, narrowed RNG, stars, draws, gold, attributes on sight, range/space, magic traditions, instantiated reserves, sheets, Devotion, Push, provisional terms, nested tug-of-wars | Cowork 2026-09-20 | PROPOSED — walk with owner, promote one at a time → D5.25+ |
| — | D5.24 (engagement-scoped initiative) cited in `11`, `14`, `00-steer` §6 but not in `decisions.md` | handoff §1b | OPEN — log or strip |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| `00`, `01`, `12`, `15`, `50` | written | mixed | D5.x |
| `10`, `11`, `13`, `14`, `20` | STUB | MVP (20: TARGET) | — |
| `02-ontology.md`, `data/SCHEMA.md` | not created | MVP | handoff §6 B |
| `data/*.json` | v1 schema; drift vs D5.9 / D5.12 / D5.14 documented | MVP | data/README |
| `12-reactions-insight.md` | delete marker, still on disk | — | successor-review |
| Reach-on-bar (D2.8/D2.12), trick-taking (D2.13), `00-steer` §4 boundary | UNDER REVIEW pending C-ref promotion | MVP | handoff §1b |

## Next actions
1. With owner: promote/reject C1–C20 → `decisions.md` D5.25+; log or strip D5.24; apply supersessions to `00-steer` §1/§4/§6; delete `12-reactions-insight.md`. Gate: owner in session.
2. `02-ontology.md` + `data/SCHEMA.md`, one section per exchange, PROVISIONAL/LOCKED column on every term (C19). Gate: action 1.
3. Distill `10 → 11 → 13 → 14 → 12 → 15` against the ontology, citing D-numbers or marking PROPOSED; compress D1–D4 during `10`. Gate: action 2.

## Open questions
Handoff §5 #1–#11 (momentum sub-questions, zones in M1, Courage's class, Focus, minting policy, acquisition distribution, Push details, M1 content adds, Lightning Palm, family/role names, carried `00-steer` §6 opens).

## Escalates to
Owner. Rule for the lead: if a v1 rule and an unpromoted C-ref conflict, write the v1 rule and flag the conflict — never silently harmonise.
