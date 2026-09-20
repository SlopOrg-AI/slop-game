# STATUS — one board

Maintained by **Admin** (`leads/admin.md`) — sole writer (D5.27). Every lead writes its row in its own brief; Admin transcribes. Detail lives in each lead brief; this page answers only: **phase · blocked on · next · when**.

**Phase:** pre-production → Godot 1v1 duel demo (M1). No human has played a duel yet.
**Next free numbers:** D-number **D5.29** (D5.24 still unlogged — being resolved with C20/C13) · C-ref **C23**.
**Git:** `main`, local only, clean tree (a commit count here rots the moment the board is committed). Admin (Claude Code) executes git on the owner's behalf, staging by path — never `git add -A`, two surfaces are live. Tech owns the tooling (hooks, `.gitignore`).

## Board

| Lead | Phase | Blocked on | Next action | Updated |
|---|---|---|---|---|
| Admin | structure DECIDED (D5.27); C21 + C22 registers landed in `AGENTS.md` §5 | — | `40-production.md` first half, on the owner's go | 2026-09-20 |
| Systems | C1→D5.25, C3→D5.26 logged; coherence pass done — the 20 C-refs distil to **9 statements**, with **7 clashes + 4 readings** open | owner present | **A first** (armed-ability economy: D5.25 removed the cap, D5.9 makes `hold` optional — live canon with a hole), then B + C20 + C13 as one exchange → `11-initiative.md` | 2026-09-20 |
| ↳ Content | v1-schema data on disk; no accepted board | schema v3 · accepted style card | hold; then Kaede/Genzo × 2 poses | 2026-09-20 |
| ↳ Tech | image-gen pipeline + `tools/` shipped and verified; art-binary policy landed (D5.28); Godot still gated | schema v3 for `validate.py` | propose `.claude/settings.json` + pre-commit hook | 2026-09-20 |
| Direction / Art | table decided; 30/31 stubs | — | distill `31-ui.md` component list | 2026-09-20 |
| Direction / Level | spatial model PROPOSED | C13 promotion · §5 #2 | `arena-m1` cluster | 2026-09-20 |
| Direction / Scenario | nothing authored | — | playtest protocol | 2026-09-20 |
| Marketing | scope undefined | owner | define scope in `inbox/` | 2026-09-20 |

Systems' input document for the walk: `proposals/2026-09-20-c-coherence.md` (§2 the clashes, §4 its own suggested order).

## Critical path to M1 — `PROPOSED (Admin, 2026-09-20)`
Systems promotions → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

Owner: tag this `CONFIRMED (owner, date)` to settle it. Any change re-opens it as PROPOSED (D5.27).

## Conflicts (cross-lead, owner resolves)
| # | Between | Issue | Status |
|---|---|---|---|
| 1 | Systems ↔ 00-steer | D5.24 cited in `11`/`14`/`00` §6, not in `decisions.md` | OPEN — owner: resolve with C20/C13 next session, not log-or-strip |
| 2 | Systems ↔ data | `00-steer` §4 "+ reaction" slot vs D5.9 default A vs C1 | **RESOLVED — D5.25.** Docs updated; `characters.json → slots.reaction` and `rules.json → reactions.max_armed` are dead fields, deleted in the schema-v3 migration (logged in `data/README.md`) |
| 3 | Tech ↔ Admin | art binaries in git (~10 MB PNGs committed) | **RESOLVED — D5.28.** `.gitignore` now keeps contact sheets + `accepted/` only; history untouched. Residue: which committed smoketest PNGs are keepers (Art/Content) |
| 4 | Admin ↔ Cowork | two surfaces regenerating `STATUS.md` | **RESOLVED — D5.27.** Single-writer rules in `leads/README.md`; Cowork removing its `STATUS.md` Project mirror |

## Housekeeping owed
- `decisions.md` `Acts on it` value **"Production"** now names a retired lead — Systems' call whether to rename it (`Process`?); existing rows are history and stay
- Which of the committed `proposals/art/2026-09-20-smoketest/` PNGs are keepers; the rest can be untracked (Art/Content, then Tech)
- `design/40-production.md` — empty stub (Admin owns it). Gated: M1/M2 milestone content depends on the C-ref promotions; the tool-split and image-gen-loop halves could be written now
- D1–D4 not compressed into `decisions.md`
- `rules.json` `_note`s cite v1 open-question numbers; `insight.reveal_timing` references the removed Arm step
- **Project mirror re-sync owed (owner action):** `AGENTS.md` — §6 lead-table row and the single-writer sentence; `01-pillars.md` — rows 7/8 reordered. `00-steer.md` unchanged. Re-upload those two files to the Claude.ai Project and the mirror is level again
