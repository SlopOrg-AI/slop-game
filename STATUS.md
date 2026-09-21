# STATUS — 2026-09-21

Phase: pre-production → Godot 1v1 duel demo (**M1**). Human duels played: **0**.

One page, by budget. Detail is in `status/<role>.md`. An **ask** is a row in the asker's own
block naming another role; the asker deletes it when it is met.

## For the owner — rule on these (≤ 5)

**Q1 · One setting left. (a) and (b) are withdrawn — `D260921.8-P`.** Approvals stay at
**0** and code-owner review stays **off**, because an approval requirement and `D260921.7-P`
cannot both hold. **Review here is a convention, not a control**, and `PROTOCOL.md` §3 now says
so. *Still owed:* **(c) token `Workflows: Read and write`** — the only thing blocking the Godot
check, and the only one not in conflict with anything.

**Q2 · Three exposure findings, deferred.** `proposals/2026-09-21-machine-account-exposure.md`.
The email setting is worth doing first; every merge republishes the address. Issue **#12** is
a stray probe of mine that needs closing — I lack the permission.

**Q3 · ANSWERED 2026-09-21 — `D260921.7-P`.** Roles decide their own mechanism; game
decisions stay the owner's. Program management should now stop reaching him. Next for
Builder is the Godot check, blocked on Q1(c).

## Designer — no live session

**state** · never run. **next** · `status/designer.md` is the queue; **C23** is oldest, owed
since 2026-09-20. **asks** · none.

## Builder — `builder-260921-c` live

**state** · Host config, identity model and rails done and demonstrated. Onboarding trimmed.
Full state: `status/builder.md`.
**next** · The Godot check — **blocked on Q1(c)**, the token's Workflows grant. Idle until then.
**not finished** · Archive pass held on `A260921.9`. Scheduler unbuilt — spec owed.
**asks** ·
- `A260921.9 → designer` · **Do `sys.7` and `sys.8` still mean anything?** Nine refs recorded
  in briefs, never promoted; `D260921.1-P` retired local refs so nothing will promote them.
  *Blocks:* archiving `leads/`. Detail: `status/designer.md` #7.
- `A260921.11 → designer` · **`AGENTS.md` §2 and §4 cite retired machinery** — `D5.44-EP`
  local refs, the Tech seat, the Project mirror. Harmless to Claude Code, which no longer
  loads it, but platforms that read it whole will act on stale rules.

## Steward — claim stale

**state** · `steward-260921-a` claimed 03:09, unseen since; past the 3-hour rule, takeable.
**asks** · `A260921.1 → builder` — §11 migration. **Done** except the held archive pass.

## Critical path to M1 — `CONFIRMED (owner, 2026-09-20)`

Q1+Q2 rulings → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 → schema v3 +
validator → Godot headless engine → screens → owner plays 10 duels.
Carried unchanged because the owner confirmed this wording. *Scenario* and *Content* are no
longer roles (`D260921.1-P`), and Godot testing is parked, which moves the engine step right.
