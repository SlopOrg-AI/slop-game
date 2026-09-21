# STATUS — 2026-09-21

Phase: pre-production → Godot 1v1 duel demo (**M1**). Human duels played: **0**.

One page, by budget. Detail lives in `status/<role>.md`; this board carries only what the owner must decide, one block per role, and the critical path. An **ask** is a row in the asker's own block naming another role — every role reads this board at session start, so nothing can be missed by not knowing it exists. The asker deletes its row when the ask is met.

## For the owner — rule on these (≤ 5)

**Q1 · Three settings you have ruled but that are not applied. An agent can do none of them.**
Ruled **A** on 2026-09-21. Until they are set, the repository does not behave the way the
documents now say it does. (a) `required_approving_review_count: 1` · (b)
`require_code_owner_review: true` — both at
<https://github.com/SlopOrg-AI/slop-game/settings/rules>, and both need **admin**, which the
machine account deliberately does not have · (c) grant the token **Workflows: Read and write**
at <https://github.com/settings/personal-access-tokens> as `sloporgAI`, which re-triggers org
approval. *Blocks:* (a) and (b) block any true claim that review is enforced — **it is not
today, `required_approving_review_count` is still 0**. (c) blocks the Godot check and every
future rail. *Then verify:* whether code-owner review does anything with the count at 0 is
still unverified; set both together and check rather than assume.

**Q2 · The three exposure findings, deferred.** `sloporgAI`'s real Gmail is permanently in
public history (`a6d5625`) and is that identity's password-recovery path · neither account has
two-factor authentication · the merge classifier is not a control. Detail and fixes:
`proposals/2026-09-21-machine-account-exposure.md`. *Blocks:* nothing. The email setting is
worth doing first — every merge by that account republishes the address until it is on.

**Q3 · What should Builder do next?** **A** the Godot check — the original objective, blocked
on Q1(c) · **B** the governance rule sketched on 2026-09-21: the owner rules game decisions
(tags S, A, C), roles decide their own mechanism (P, E), and no role may widen what it is
allowed to decide. Needs the owner's own wording to log · **C** the archive pass on `leads/`,
`inbox/`, `bridge/`, held on `A260921.9`. **Recommendation: B, then A** — B is what stops this
queue re-forming every session. *Blocks:* Builder.

## Designer — no live session

**state** · Seat unclaimed. No Designer session has run under the clean-slate framework.
**next** · `status/designer.md` is the queue. **C23** is the oldest item, owed since 2026-09-20.
**asks** · none.

## Builder — `builder-260921-c` live

**state** · Host configuration done and demonstrated (`D260921.3-P`). Standup tidy in progress. Full state: `status/builder.md`.
**next** · Sessions-register template into `PROTOCOL.md`, then the `leads/` · `inbox/` · `bridge/` archive pass.
**not finished** · **The archive pass is held** on two things, both of which it would destroy: the nine unpromoted local refs (`A260921.9`), and the `leads/`-only pointer to C23. Implementation review §5 — check what points *only* at what is being archived.
**asks** ·

- `A260921.10 → owner` · **Three exposure findings, deferred by you to "later".** The machine account's real Gmail is in public history permanently (`a6d5625`) and it is that identity's recovery path · neither account has 2FA · the merge classifier refused twice and allowed four times today with no review present, so it is not a control and review here is currently a convention. Detail and fixes: `proposals/2026-09-21-machine-account-exposure.md`. *Blocks:* nothing — but any claim that review is enforced is untrue until `required_approving_review_count` is 1.
- `A260921.9 → designer` · **Do `sys.7` and `sys.8` still mean anything?** Nine refs were recorded in briefs and never promoted to D-numbers: `cos.2`–`cos.7`, `sys.7`, `sys.8`, `tech.1`. `D260921.1-P` retired local refs and made the `cos.*` process rows background, so those are likely moot — the two `sys.*` may be live game rules. *Blocks:* archiving `leads/`. Detail: `status/designer.md` #7.
- `A260921.5 → owner` · The doorbell has never run **and cannot**: its step 5 pushes to `main`, which is gated with no bypass actors. **Parked by the owner, 2026-09-21** — reworking it to open a pull request is the fix when it is wanted.

## Steward — claim stale

**state** · `steward-260921-a` claimed 03:09, last seen 03:09 — past the 3-hour rule (`PROTOCOL.md` §2.1), so presumed dead and takeable. Full state: `status/steward.md`.
**asks** · `A260921.1 → builder` — run the §11 migration checklist. **In progress**: charters, clones, `PROTOCOL.md` and this collapse are done; the archive pass is held above.

## Critical path to M1 — `CONFIRMED (owner, 2026-09-20)`

Q1 + Q2 rulings → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

Carried unchanged, because the owner confirmed this wording. Two notes, neither a rewrite: *Scenario* and *Content* are no longer roles (`D260921.1-P` makes them tasks a role launches), and **Godot testing was parked by the owner on 2026-09-21**, which moves the engine step rightward.
