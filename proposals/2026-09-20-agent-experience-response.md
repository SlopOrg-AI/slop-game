# Chief of Staff response — agent-experience review (R1–R8)

**Produced by:** Chief of Staff (Cowork), 2026-09-20 · **Answers:** `2026-09-20-agent-experience-review.md` · **Status:** PROPOSED; queue rows in §4 for Tech to transcribe.

## 1. Verdict on the verdict
Correct diagnosis: decay and non-enforcement, not structure. Accept R1–R8 as written. Sequence them (§3); do not run them piecemeal across surfaces.

## 2. Considerations the review under-weights
| # | Consideration | Proposal |
|---|---|---|
| X1 | **Governance is outrunning design** — ≈45 KB process vs ≈35 KB design, six stubs. The framework is one session from becoming the product. | **Framework freeze:** after D5.39 lands, no change to `AGENTS.md`, `leads/`, hooks or the queue format without a queue item. Next three sessions are design/distillation only. |
| X2 | **F2 is the most expensive finding** — "read the doc you're touching" returns 300 bytes and the agent rebuilds the rule from a 29 KB log. | **Stub redirects:** every stub gets one line — *"Current rule: D5.x, D5.y (`decisions.md`); draft model: handoff §3.n"* — generated from the `Acts on it` column. Ten minutes; removes the reconstruction cost until distillation. |
| X3 | **F7 (load-bearing proposals) is a second canon in fact.** | Interim honesty: stamp both files *"REQUIRED READING until `02-ontology.md` exists; rule 2 still applies — the log wins."* Remove the stamp with R7. |
| X4 | **The review is a Cowork product** — the most expensive surface doing a read-only sweep. | Make the fresh-agent read periodic, on Claude Code or Codex: every milestone tag, or every ~15 commits. Output = this table format, ≤1 page. |
| X5 | **R3 half-measure risk.** Un-ignoring `.claude/agents/` is right; `.claude/settings.json` (permissions) should be committed too; `settings.local.json` stays ignored. | Say so in D5.39 so Tech doesn't split the difference. |
| X6 | **F4 lag is structural under D5.38** (author ≠ keeper). R6 handles close; nothing handles open. | Tech transcribes pending rows at **session open** before any work; Chief of Staff confirms at close. Two lines in `leads/README.md`. |
| X7 | **F9/R8 is the only finding with a deadline.** | Remote before the Mac move is not a recommendation; it is the move. Rule it with C24, not D5.39. |

## 3. Sequence (three sessions, all Claude Code except the owner lines)
1. **Owner:** rule D5.39 (guard rails + sweep + X5) and C24 (remote first). One session, two verdicts.
2. **Tech:** R1 → R3 → R4 → R2 → X2 stub redirects → X3 stamps. One commit each.
3. **Systems:** R5 "distilled" definition (queue) → R7 with `02-ontology.md`.
Then the freeze (X1).

## 4. Queue rows (Tech transcribes into `STATUS.md` when slots free; Q6 is urgent enough to displace Q5)
```
Q6 · What does "distilled" mean for a design doc? It gates starting Godot · blocks: demo/README gate, Godot start
  A: no STUB marker and no OPEN row at MVP scope   ← Systems (review R5)
  B: owner signs each doc off by name
Q7 · Freeze the framework after D5.39 — no governance changes without a queue item for three sessions · blocks: nothing; protects design time
  A: freeze   ← Chief of Staff
  B: keep it fluid
```
