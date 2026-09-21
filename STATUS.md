# STATUS — one board

**Authored by Chief of Staff** (`leads/chief-of-staff.md`, Cowork) — it decides what every row says. **Kept by Tech** (Claude Code): types and commits it, transcribing without paraphrase, never re-sequencing (D5.27 → D5.29 → **D5.38**). Leads write their row in their own brief first. This page answers only: **phase · blocked on · next · what the owner must decide**.

**Phase:** pre-production → Godot 1v1 duel demo (M1). No human has played a duel yet.
**Next free numbers:** D-number **D5.39** · C-ref **C25**. (D5.29 logged; D5.30–D5.37 logged by the combat session; D5.38 = board custody. C23 = three decks, C24 = the Mac move.) D5.24 still unlogged — resolves with Q2.
**Git:** `main`, local only. Tech (Claude Code) executes git, staging by path — never `git add -A`.

## Decisions — for the owner

Answer in chat or here: `Q1: A` · `Q1: A, but …` · `Q1: reject` · `Q1: defer to <gate>`.

```
Q1 · Armed abilities: holding a reaction is free, so arming everything every round is the best play · blocks: 10, 12, schema v3
  A: `hold` cost mandatory for reactions/sustained — existing vocabulary, no new mechanic   ← Systems
  B: pay on arm, spent whether or not it fires — arming becomes a bet
Q2 · Initiative: one bar, or nested bars (pair · team · fight) with distance moved off the bar onto the map · blocks: 11, 14, D5.24
  A: nested bars, distance on the map (C13 + C20 as stated)   ← Systems
  B: keep one bar as-is until the demo is played; C13/C20 wait
Q3 · Vision paragraph (00-steer §1): the pitch, or the test everything is held against? · blocks: vision-coherence findings
  A: pitch — pillars are the test; §1 stops being cited as canon   ← Chief of Staff
  B: test — §1 must carry pillars 3 and 6 and be corrected now
Q4 · Confirm the critical path below as written · blocks: nothing; settles sequence
  A: confirm   ← Chief of Staff
  B: amend (say what)
Q5 · Marketing: record from now, or from the first playable demo · blocks: marketing scope
  A: from M1 — nothing showable yet   ← Chief of Staff
  B: from now — design-process devlog
```

**Waiting** (queued as slots free): coherence clashes C–F + four readings (`c-coherence` §2–§3) · pillar strains P2a, P3a (`vision-coherence` §3) · Godot version pin · which smoketest PNGs are keepers.
**Ruled:** —

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
- `leads/admin.md`, `tools/claude-agents/admin.md`, `.claude/agents/admin.md` — tombstone/delete with D5.29
- `leads/systems/tech.md` — add git execution + housekeeping to Owns; `CLAUDE.md` hat line; `AGENTS.md` §6 already updated
- `design/40-production.md` §5 M1/M2 definitions — after Q1/Q2
- D1–D4 not compressed into `decisions.md`
- `rules.json` `_note`s cite v1 open numbers; `insight.reveal_timing` references the removed Arm step
- Project mirror: level as of this write (Chief of Staff re-syncs)
