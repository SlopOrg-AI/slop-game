# STATUS — 2026-09-21

Phase: pre-production → Godot 1v1 duel demo (**M1**). Human duels played: **0**.

One page, by budget. Detail lives in `status/<role>.md`; this board carries only what the owner must decide, one block per role, and the critical path. An **ask** is a row in the asker's own block naming another role — every role reads this board at session start, so nothing can be missed by not knowing it exists. The asker deletes its row when the ask is met.

## For the owner — rule on these (≤ 5)

**Q1 · Nobody can change CI any more.** The machine account's token has no **Workflows**
permission by design, so an agent cannot edit `.github/workflows/`; `D260921.5-P` says you
do not commit. Between them, `guard-rails.yml` is now unwritable by anyone. *Blocks:* the
Godot check when it comes off the back burner, and any future rail that needs a workflow
change. **Options:** grant the token Workflows write (an agent can then rewrite the rails
that police it) · carve out `.github/**` as the one place you do commit · a separate
credential used only for workflow changes. **Recommendation:** the carve-out — it is rare,
deliberate, and keeps the property that agents cannot disarm their own guard rails.

**Q2 · Does a merge commit count as you committing?** GitHub authors merge commits as
whoever clicks merge. Rail F excludes them, treating a merge as a review action rather than
authorship. If you want `chris-egan` out of the history entirely, **agents must do all
merging** — which makes the merge-classifier question load-bearing rather than curiosity.
*Blocks:* nothing today; decides whether Q3 is optional or required.

**Q3 · Raise `required_approving_review_count` to 1?** `D260921.4-P` (a) said prove the lane
once, then decide. The lane is proven: `sloporgAI` opened #8, `rails` went green, and rail F
was shown refusing a deliberate failure in real CI. The risk I flagged earlier — an agent
signing off your work — **disappears** under `D260921.5-P`, because you no longer author
pull requests. `require_code_owner_review` becomes safe for the same reason, which closes
Trap 1. *Needs:* admin; an agent cannot set it.

## Designer — no live session

**state** · Seat unclaimed. No Designer session has run under the clean-slate framework.
**next** · `status/designer.md` is the queue. **C23** is the oldest item, owed since 2026-09-20.
**asks** · none.

## Builder — `builder-260921-c` live

**state** · Host configuration done and demonstrated (`D260921.3-P`). Standup tidy in progress. Full state: `status/builder.md`.
**next** · Sessions-register template into `PROTOCOL.md`, then the `leads/` · `inbox/` · `bridge/` archive pass.
**not finished** · **The archive pass is held** on two things, both of which it would destroy: the nine unpromoted local refs (`A260921.9`), and the `leads/`-only pointer to C23. Implementation review §5 — check what points *only* at what is being archived.
**asks** ·
- `A260921.9 → designer` · **Do `sys.7` and `sys.8` still mean anything?** Nine refs were recorded in briefs and never promoted to D-numbers: `cos.2`–`cos.7`, `sys.7`, `sys.8`, `tech.1`. `D260921.1-P` retired local refs and made the `cos.*` process rows background, so those are likely moot — the two `sys.*` may be live game rules. *Blocks:* archiving `leads/`. Detail: `status/designer.md` #7.
- `A260921.5 → owner` · The doorbell has never run **and cannot**: its step 5 pushes to `main`, which is gated with no bypass actors. **Parked by the owner, 2026-09-21** — reworking it to open a pull request is the fix when it is wanted.

## Steward — claim stale

**state** · `steward-260921-a` claimed 03:09, last seen 03:09 — past the 3-hour rule (`PROTOCOL.md` §2.1), so presumed dead and takeable. Full state: `status/steward.md`.
**asks** · `A260921.1 → builder` — run the §11 migration checklist. **In progress**: charters, clones, `PROTOCOL.md` and this collapse are done; the archive pass is held above.

## Critical path to M1 — `CONFIRMED (owner, 2026-09-20)`

Q1 + Q2 rulings → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

Carried unchanged, because the owner confirmed this wording. Two notes, neither a rewrite: *Scenario* and *Content* are no longer roles (`D260921.1-P` makes them tasks a role launches), and **Godot testing was parked by the owner on 2026-09-21**, which moves the engine step rightward.
