# STATUS — 2026-09-21

Phase: pre-production → Godot 1v1 duel demo (**M1**). Human duels played: **0**.

One page, by budget. Detail lives in `status/<role>.md`; this board carries only what the owner must decide, one block per role, and the critical path. An **ask** is a row in the asker's own block naming another role — every role reads this board at session start, so nothing can be missed by not knowing it exists. The asker deletes its row when the ask is met.

## For the owner — rule on these (≤ 5)

**Q1 · Merge [PR #5](https://github.com/SlopOrg-AI/slop-game/pull/5) and [PR #6](https://github.com/SlopOrg-AI/slop-game/pull/6).** Both green and CLEAN. **No agent session can merge them** — Claude Code's own guard rails refuse merge-without-review, which is not a repo setting anyone here can change. *Blocks:* the Builder seat claim reaching `main`; `D260921.4-P` reaching the log. Every future pull request lands the same way.

**Q2 · Create the fine-grained token for `sloporgAI`** — `D260921.4-P` (a). Only the owner can; an agent cannot issue account credentials. *Blocks:* raising `required_approving_review_count` above 0, and any honest claim that independent review is a control rather than a convention. *Known trap:* the org may require two-factor auth before membership activates, and if it requires approval for fine-grained tokens the token authenticates and then 404s on the repo.

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

**state** · `steward-260921-a` claimed 03:09, last seen 03:09 — past the 3-hour rule in `sessions/README.md`, so presumed dead and takeable. Full state: `status/steward.md`.
**asks** · `A260921.1 → builder` — run the §11 migration checklist. **In progress**: charters, clones, `PROTOCOL.md` and this collapse are done; the archive pass is held above.

## Critical path to M1 — `CONFIRMED (owner, 2026-09-20)`

Q1 + Q2 rulings → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

Carried unchanged, because the owner confirmed this wording. Two notes, neither a rewrite: *Scenario* and *Content* are no longer roles (`D260921.1-P` makes them tasks a role launches), and **Godot testing was parked by the owner on 2026-09-21**, which moves the engine step rightward.
