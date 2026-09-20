# STATUS — one board

Maintained by Production (`leads/production.md`). Every lead updates its own row at the end of its session. Detail lives in each lead brief; this page answers only: **phase · blocked on · next · when**.

**Phase:** pre-production → Godot 1v1 duel demo (M1). No human has played a duel yet.
**Next free numbers:** D-number **D5.27** (D5.24 still unlogged — being resolved with C20/C13) · C-ref **C21**.
**Git:** `main`, local only, 8 commits, clean tree. Lead structure + guard rails committed. Tech (Claude Code) commits on the owner's behalf; Production owns commit *process*.

## Board

| Lead | Phase | Blocked on | Next action | Updated |
|---|---|---|---|---|
| Production | structure just set up | owner commit | seed `inbox/`; sequence C1–C20 walk | 2026-09-20 |
| Systems | C1→D5.25, C3→D5.26 logged; `decisions.md` now carries an `Acts on it` column; 15/20 C-refs still open | owner present | momentum + space exchange: D5.24 + C20 + C13 together → D5.27+ and `11-initiative.md` | 2026-09-20 |
| ↳ Content | v1-schema data on disk; no accepted board | schema v3 · accepted style card | hold; then Kaede/Genzo × 2 poses | 2026-09-20 |
| ↳ Tech | image-gen pipeline + `tools/` shipped and verified; Godot still gated | schema v3 for `validate.py` · Production for art-binary policy | propose `.claude/settings.json` + pre-commit hook | 2026-09-20 |
| Direction / Art | table decided; 30/31 stubs | — | distill `31-ui.md` component list | 2026-09-20 |
| Direction / Level | spatial model PROPOSED | C13 promotion · §5 #2 | `arena-m1` cluster | 2026-09-20 |
| Direction / Scenario | nothing authored | — | playtest protocol | 2026-09-20 |
| Marketing | scope undefined | owner | define scope in `inbox/` | 2026-09-20 |

## Critical path to M1
Systems promotions → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

## Conflicts (cross-lead, owner resolves)
| # | Between | Issue | Status |
|---|---|---|---|
| 1 | Systems ↔ 00-steer | D5.24 cited in `11`/`14`/`00` §6, not in `decisions.md` | OPEN — owner: resolve with C20/C13 next session, not log-or-strip |
| 2 | Systems ↔ data | `00-steer` §4 "+ reaction" slot vs D5.9 default A vs C1 | **RESOLVED — D5.25.** Docs updated; `characters.json → slots.reaction` and `rules.json → reactions.max_armed` are dead fields, deleted in the schema-v3 migration (logged in `data/README.md`) |
| 3 | Tech ↔ Production | art binaries in git (~10 MB PNGs committed) | OPEN — policy proposal in `leads/production.md` |

## Housekeeping owed
- `design/12-reactions-insight.md` — delete marker still on disk
- `design/40-production.md` — empty stub
- D1–D4 not compressed into `decisions.md`
- `rules.json` `_note`s cite v1 open-question numbers; `insight.reveal_timing` references the removed Arm step
- `01-pillars.md` row order 8 before 7 (cosmetic)
- Project mirror: re-sync `AGENTS.md` after §6 is added
