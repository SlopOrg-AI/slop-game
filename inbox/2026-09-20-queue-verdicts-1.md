# Owner verdicts — queue round 1 (2026-09-20, Cowork chat)

**TRIAGED 2026-09-20** by Chief of Staff. Tech: transcribe §Ruled into `STATUS.md` (D5.38); leads log D-numbers in their next session.

## Verbatim

> 1. each round the previous round's ability earmarks are cleared. to arm abilities there is an earmark that round. the earmark amount lines up with the ability check number
> 2. a
> 3. it's pitch and pillars - it should be the point of comparison for all work to hang on
> 4. feedback: too brief how is user to know without easy reference. reprompt
> 5. keep on hold
> 6. distill - agents should consider this a complex task, alchemize across sources, compare and synthesize and draw out like and unlike, the valuable. does that help?
> 7. framework freeze: leads and agents log concerns, but let's see with user whether to change or reconsider, right?

## Ruled

| Q | Verdict | C-ref | Owning lead → action |
|---|---|---|---|
| Q1 | **A, but owner's own mechanic:** earmarks clear each round; arming earmarks reserve that round; earmark = the ability's check number (D5.30) | **C25** `[sys]` | Systems: log D-number; reconcile with D5.31 (`hold` earmark) — C25 supersedes where they differ; write into `10`/`12` |
| Q2 | **A** — nested bars (pair · team · fight), distance on the map | — | Systems: log D-number (C13 + C20 promoted); resolve D5.24 in the same entry; `11-initiative.md` |
| Q3 | **Vision paragraph + pillars are together the test** for all work. Not pitch-only. | **C26** `[sys] [cos]` | Systems: correct `00-steer` §1 against the log (vision-coherence §1 clauses 4–6; clause 1 now true per D5.34/35); carry pillars 3 and 6. Chief of Staff: cite §1 + `01` as the test in cluster/proposal templates |
| Q4 | **Reprompt** — owner needs the path in plain words with references | — | Chief of Staff: re-present (chat) |
| Q5 | **Hold** | — | Marketing: dormant; stays off the queue |
| Q6 | **Definition given, gate not yet chosen.** Owner defines *distilling* as the work: "alchemize across sources, compare and synthesize, draw out like and unlike, the valuable" | **C27** `[sys] [cos]` | Chief of Staff: confirm the done-test in reprompt (proposed: C27 is the standard of work; A — no STUB, no OPEN MVP row — is the checkable gate) |
| Q7 | **A, as read by owner:** freeze = agents log concerns; owner decides whether to change | — | Chief of Staff: add to `leads/README.md` after D5.39 lands |

Not yet ruled: **D5.39** (guard rails + sweep), **C24** (git remote before Mac move).

## Board rows (Tech transcribes)
- Ruled: Q1 (C25) · Q2 · Q3 (C26) · Q5 hold · Q7 — 2026-09-20. Q4, Q6 reprompted.
- Queue now: Q4 (reprompt) · Q6 (confirm gate) · D5.39 · C24 · next from Waiting.
- Next free C-ref: **C28**.

## Addendum — Q6 clarified (owner, same session)

> 3's distill means more like importing the system's ontology and data schema into the combat docs right? my earlier definition should be contemplated by agents though

**C27 (final):** *Distilled* = the doc is **written against `02-ontology.md` and `data/SCHEMA.md`** — rules in the ontology's vocabulary, numbers pointing at schema fields — **produced by synthesis** across sources (v1 bible, `decisions.md`, session-6 model, coherence passes: compare, keep the valuable), and carrying **no STUB marker and no OPEN row at MVP scope**. Q6 ruled. Systems logs; `demo/README.md` gate and `40-production.md` open #3 cite it.

## Addendum 2 — remaining verdicts (owner, same session)

> confirm, install, yes

| Item | Verdict | Owning lead → action |
|---|---|---|
| Q4 | **CONFIRMED (owner, 2026-09-20)** — critical path as written on the board | Tech: tag the block `CONFIRMED (owner, 2026-09-20)` |
| D5.39 | **Install** — guard rails + hooks + commit sweep as proposed (`guard-rails.md` §6, `commit-sweep.md` §C), incl. committing `.claude/settings.json` and `.claude/agents/` (review R3, response X5) | Tech: log D5.39, implement, verify each hook by provoking it, one commit per step |
| C24 | **Yes** — private git remote before the Mac move; rescue PC-only text cited by D1–D4 in the same session (review R8) | Tech: log D-number (next free after D5.39); create remote; push; migration doc §1–§2 |

Queue is empty. Chief of Staff refills from Waiting next session: coherence clashes C–F first.

## Addendum 3 — Q8, Q9 and a standing rule (owner, same session)

> handle failover ad hoc - let's commit to minimizing and manage project bloat at all times right, seek to reduce governance overhead

| Item | Verdict | Owning lead → action |
|---|---|---|
| Q9 | **B** — canon-clone rule only (`Canon clone: <machine>` header field, set at the Mac move). No `FAILOVER.md`; failover handled ad hoc. Tiers 1–2 of `continuity.md` are reference, not rules | Tech: add the header field with C24; archive `continuity.md` |
| Q8 | **Read with the standing rule below** — the owner's direction is to reduce; P1–P4 each delete something. Chief of Staff recommends A stands; owner has not said A or B explicitly | Chief of Staff: confirm at next session open, one word |
| **C28** `[cos] [tech] [sys]` | **Standing rule: minimize. Manage project bloat at all times; seek to reduce governance overhead.** Applies to every lead and every proposal. Concretely: no new governance file without deleting one; proposals archived on ruling (P3); measurement line on the board (context-economics §5) is the check | Chief of Staff: one line in `AGENTS.md` §5 when the freeze lands (a rule *about* reducing must itself cost one line); Tech: transcribe |

Next free C-ref: **C29**.

## Addendum 4 — Q8 (owner, same session)

> confirmed

| Item | Verdict | Owning lead → action |
|---|---|---|
| Q8 | **A** — adopt context-economics P1–P4 as amended in `…-context-economics-response.md` §2, plus the session measurement line, inside the D5.39 window | Tech: log as D5.40 after D5.39; P3 + P4 mechanical first; P1 split with Systems; P2 as the rule for every new D-number. Then the freeze (Q7) is in force |

Queue empty. Round 1 closed 2026-09-20.
