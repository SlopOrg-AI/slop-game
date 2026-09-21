# 12 — Reactions & passives

**Scope:** MVP · **Status:** DECIDED D5.8, D5.9; slots OPEN · **Updated:** 2026-09-20
**STUB — rules below are the v2 direction; v1 grading/cost detail still to be distilled from `C:\Claude\docs\01-design-bible.md` §7, D3.2–D3.4.** Insight moved to `15-information.md`.

> **Current rule:** D5.8, D5.9, D5.25, D5.26, D5.30, D5.31, D5.32, D5.34, D5.35, D5.36 (`design/decisions.md` — the arbiter; this doc is a stub and does not restate them) · **draft model:** `proposals/2026-09-20-session-6-handoff.md` §3.3 · **open clashes:** `proposals/2026-09-20-c-coherence.md` §2

## Purpose
Everything you commit in Plan that is not a queued action: traps, sustained edges, decaying effects, one-shots.

## Player experience goal
You bet on a read. The trap you set against the heavy commit you *think* is coming either springs the reversal or sits there costing you.

## Rules / Data

### Ability kinds (MtG model, D5.9)
| Kind | Fires | Lifetime | Example |
|---|---|---|---|
| Activated | when resolved in order | one resolution | strike, feint |
| Reaction | on trigger match | consumed when fired | Anticipate |
| Sustained passive | continuously | until dropped / wounded out / dispelled | Keen Eyes |
| Decaying passive | continuously | natural decay (N rounds, scene `wind`) or active removal | Smoke Screen |
| One-off | at commit or round boundary | this round | round-start surge |

Costs per ability: `hold: {reserve, amount}` (locked, excluded from refill — D3.4) and/or `upkeep: {reserve, per_round}`. Any kind may use either.

### Commitment (D5.8)
All kinds are committed in **Plan** alongside actives, hidden, simultaneously. No reveal step. Persistence of an un-fired reaction across rounds: v1 rule (persists, cost locked) stands unless play says otherwise.

### Grading (v1, D3.2–D3.3 — confirm in play)
Narrow trigger (≥2 predicates) → perfect: negate, attacker's spent reserves lost, initiative reverses by the countered ability's delta. Broad (1 predicate) → partial: damage halved. +1 grade: holder's Insight > attacker's · `focused` · Desperate zone. Firing drains holder's Insight to ~25%.

### Slots — OPEN #3
A (default): typed body/mind/spirit slots hold any kind; concurrency limited by reserves. B: dedicated passive slot(s). C: hard cap on armed count.

### Resolution order — OPEN #8
Reactions inline in trick-taking order (v1) vs a **stack** (LIFO against the action answered; responses to responses).

## Dependencies
- Reads from: `10-combat-loop` (order), `15-information` (Insight grade bonus), `13-damage-wounds` (tiered states subtract)
- Writes to: `11-initiative` (reversal)

## Open questions
1. Slots (Open #3). 2. Stack vs inline (Open #8). 3. Un-fired reaction persistence — confirm in play. 4. Burn-a-tag / devil's-bargain class (bigger effect, named cost) — PROPOSED, later.

## Status table
| Item | Status | Scope | Source |
|---|---|---|---|
| Kinds + hold/upkeep | DECIDED | MVP | D5.9 |
| Commit in Plan, no reveal | DECIDED | MVP | D5.8 |
| Grading | DECIDED (confirm in play) | MVP | S1.§8, D3.2, D3.3 |
| Slots | OPEN | MVP | — |
