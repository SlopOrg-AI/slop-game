# STATUS — one board

**Authored by Chief of Staff** (`leads/chief-of-staff.md`, Cowork) — it decides what every row says. **Kept by Tech** (Claude Code): types and commits it, transcribing without paraphrase, never re-sequencing (D5.27 → D5.29 → **D5.38**). Leads write their row in their own brief first. This page answers only: **phase · blocked on · next · what the owner must decide**.

**Phase:** pre-production → Godot 1v1 duel demo (M1). No human has played a duel yet.
**Next free numbers:** D-number **D5.41** · C-ref **C28**. (D5.38 = board custody; **D5.39 = guard rails + sweep**; **D5.40 = private remote, C24 — execution blocked on the owner**. C25 = Q1's earmark mechanic, C26 = vision-as-test, C27 = "distilled".) D5.24 still unlogged — folds into Q2's entry.
**Git:** `main`, local only. Tech (Claude Code) executes git, staging by path — never `git add -A`.

## Decisions — for the owner

Answer in chat or here: `Q1: A` · `Q1: A, but …` · `Q1: reject` · `Q1: defer to <gate>`.

```
Q4 · Confirm the critical path below · blocks: nothing; settles sequence
  REPROMPTED — owner: "too brief how is user to know without easy reference."
  Chief of Staff owes a re-presentation in plain words, with the references.
  Until then the critical path stays PROPOSED — no CONFIRMED tag is written.
```

**Waiting** (queued as slots free): coherence clashes C–F + four readings (`c-coherence` §2–§3) · pillar strains P2a, P3a (`vision-coherence` §3) · Godot version pin · which smoketest PNGs are keepers · **guard rails + commit sweep, as one ruling** (`proposals/2026-09-20-guard-rails.md` §6 + `proposals/2026-09-20-commit-sweep.md` §C → D5.39) · agent-experience review R1–R8 (`proposals/2026-09-20-agent-experience-review.md` §4).
**Ruled** (2026-09-20, `inbox/2026-09-20-queue-verdicts-1.md`):
- **Q1 — A, with the owner's own mechanic** (**C25** `[sys]`): earmarks clear each round; arming earmarks that round; the earmark equals the ability's check number (D5.30). Systems logs, reconciles against D5.31 where they differ, writes into `10`/`12`.
- **Q2 — A**: nested bars (pair · team · fight), distance on the map (C13 + C20 promoted). Systems logs and resolves **D5.24** in the same entry → `11-initiative.md`.
- **Q3 — vision paragraph *and* pillars are together the test** for all work (**C26** `[sys] [cos]`), not pitch-only. Systems corrects `00-steer` §1 against the log; Chief of Staff cites both as the test in templates.
- **Q5 — hold.** Marketing stays dormant and off the queue.
- **Q6 — ruled by the addendum** (**C27**): *distilled* = written against `02-ontology.md` and `data/SCHEMA.md`, produced by synthesis across sources, carrying no STUB marker and no OPEN row at MVP scope. Cited by the `demo/README.md` gate and `40-production.md` open #3.
- **Q7 — A, as the owner reads it**: framework freeze means leads and agents *log* concerns; the owner decides whether to change. Chief of Staff adds it to `leads/README.md`.
- **D5.39 — guard rails, commit sweep, Chief of Staff audit**: ruled in chat and logged; the verdicts file predates it and lists it as unruled.

## Board

| Lead | Phase | Blocked on | Next action | Updated |
|---|---|---|---|---|
| Chief of Staff | reformulation owner-confirmed; queue live | owner verdicts Q1–Q5 | transcribe verdicts; queue next batch | 2026-09-20 |
| Systems | C1→D5.25, C3→D5.26; coherence pass done — 20 C-refs → 9 statements, 7 clashes + 4 readings open | Q1, Q2 | on Q1/Q2 rulings: log D-numbers, write `11-initiative.md` | 2026-09-20 |
| ↳ Content | v1-schema data on disk; no accepted board | schema v3 · accepted style card | hold; then Kaede/Genzo × 2 poses | 2026-09-20 |
| ↳ Tech | image-gen pipeline + `tools/` shipped; art-binary policy landed (D5.28); Godot gated | schema v3 for `validate.py` | **log D5.29, apply `lead-reformulation` §6 renames, take housekeeping list below into own brief**; then `.claude/settings.json` + pre-commit hook proposal | 2026-09-20 |
| Direction / Art | table decided; 30/31 stubs | — | distill `31-ui.md` component list | 2026-09-20 |
| Direction / Level | spatial model PROPOSED | Q2 · §5 #2 | `arena-m1` cluster | 2026-09-20 |
| Direction / Scenario | nothing authored | — | playtest protocol | 2026-09-20 |
| Marketing | scope undefined | Q5 | define scope | 2026-09-20 |

Systems' input for the walk: `proposals/2026-09-20-c-coherence.md` (§2 clashes, §4 order).

## Critical path to M1 — `PROPOSED (Chief of Staff, 2026-09-20)` → Q4
Q1 + Q2 rulings → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

## Conflicts (cross-lead)
| # | Between | Issue | Status |
|---|---|---|---|
| 1 | Systems ↔ 00-steer | D5.24 cited in `11`/`14`/`00` §6, not in `decisions.md` | OPEN — folds into Q2 |
| 2 | Systems ↔ data | "+ reaction" slot | RESOLVED — D5.25; dead fields go in schema-v3 migration |
| 3 | Tech ↔ Chief of Staff | art binaries in git | RESOLVED — D5.28; residue in Waiting |
| 4 | Cowork ↔ Claude Code | two writers of `STATUS.md` | RESOLVED — D5.27/D5.29; Chief of Staff sole writer, Tech commits |

## Housekeeping (Tech owns; listed here until Tech's brief carries it)
- `decisions.md` `Acts on it` value "Production" names a retired lead — Systems' call (`Process`?); rows are history
- `leads/systems/tech.md` — add git execution + housekeeping to Owns; `CLAUDE.md` hat line; `AGENTS.md` §6 already updated
- **Retired-role residue** (`Admin`, D5.29) still stated in live docs: `design/40-production.md` §1 tool-split row and **§3 record-discipline row** (states a rule D5.38 superseded) · `inbox/README.md` triage protocol · `tools/claude-agents/README.md` · Does-NOT-own rows in `leads/marketing.md`, `leads/systems.md`, `leads/systems/content.md`
- **`D5.24` cited as canon in six files** and absent from `decisions.md` — `00-steer` §6, `11-initiative.md` (status table asserts DECIDED), `14-scenes-conditions.md`, `STATUS.md`, `leads/systems.md`, `leads/direction/level.md`. Folds into Q2
- `design/40-production.md` §5 M1/M2 definitions — after Q1/Q2
- D1–D4 not compressed into `decisions.md`
- `rules.json` `_note`s cite v1 open numbers; `insight.reveal_timing` references the removed Arm step
- Project mirror: level as of this write (Chief of Staff re-syncs)
