# Review — implementing the clean slate: four risks, one correction

**From:** the owner's Cowork console (the outgoing Chief of Staff assistant, session `a5`) · **To:** Steward and Builder · **On:** `proposals/2026-09-21-clean-slate.md` (APPROVED, D260921.1-P / D260921.2-P) · **Status:** advice, pushed on the owner's instruction (*"push advice to cos"*). Not a proposal, not a queue item, nothing to rule on. Delete it once read.

**Verdict: implement it.** The diagnosis matches what the `a5` session watched fail first-hand, point for point, and the design is genuinely subtractive — one copy of the repo per role removes the *category* of problem that every retired mechanism was working around. What follows is about **how to land it**, not whether.

---

## 0. A correction the record needs

Session `a5` reported to the owner, three times, that another session was overwriting the Chief of Staff brief from a stale copy. **That was wrong.** Tech's evidence (`proposals/2026-09-21-cos-tech-handshake.md` §5, restated on the board): a `git reset --hard HEAD~1` to drop an empty test commit discarded uncommitted work in the shared tree. Not a second author.

The remedy is unchanged — a history operation in one worktree cannot reach another — but the **stated diagnosis in `clean-slate.md` §0.1 should carry the real mechanism**, because the next person reasons from it. "Several agents write one tree" is the condition; "a history operation in a shared tree destroys another agent's uncommitted work" is what actually happened. Write the second one down.

## 1. `design/decisions.md` will now conflict on every concurrent append

Three roles, three worktrees, one append-only file. Simultaneous appends land at the same place and git cannot merge them — **silent loss becomes a blocked merge**, which is better, but it will happen most sessions once more than one role is live, and it lands on whoever pushes second.

| Option | Cost |
|---|---|
| **One row per file** — `decisions/D260921.3-P.md`, the log rendered from the folder by the stop step, exactly as `STATUS.md` is rendered from `status/<role>.md` | One more render; the pattern already exists in this design |
| **Only one role logs** (Steward, or whoever is with the owner) | Zero mechanism; reintroduces the hop that lost C23 for two days |
| Do nothing and resolve conflicts by hand | Every merge conflict is in the one file nobody may rewrite |

**Recommended: one row per file.** It is the same trick the design already chose for the board, applied to the only other file every role writes.

## 2. A ruling the owner gives in chat has no carrier

The console cannot write. The doorbell only wakes when `queue/` holds an unanswered item. So a ruling the owner gives spontaneously — in the console, on his phone, mid-conversation — lives **nowhere** until some session happens to pick it up. That is the exact shape that left C23 undelivered for two days, and D260921.2-P's *"an answer is the instruction wherever he gave it"* makes it worse, not better: the instruction is valid and unrecorded.

**Cheapest fix, no mechanism:** the console's standing output for any ruling is a **paste-ready block** — the verbatim words, the suggested ID, the tag, and the one-line rule — which the owner pastes into the next session or the doorbell thread. Add one line to `claude/CONSOLE.md` §3 making that the console's default, not an offer.

## 3. Do not let the launcher gate the migration

`tools/start` — worktrees, claims, three tabs, standing prompts, a stop step that renders the board, pushes, and reports conflicts — is **the largest single piece of machinery this project has ever built**, and it is being built in the same pass that declares a hard stop on new machinery. If it half-works, nothing starts at all.

- Create the worktrees **by hand, once**. Ten seconds, no code.
- Migrate, verify, stop.
- The launcher is a convenience added **after** the hard stop proves the design works without it — or by a task session, not by the migration.

## 4. Split the migration into four commits

The checklist in §11 is one Builder session doing: worktrees · `PROTOCOL.md` · three charters · board render · queue folder · archive six trees · retire three tools · rewrite `AGENTS.md` and `CLAUDE.md`. **Single big passes by one surface are this project's documented failure mode** — five mechanisms shipped that way last night, two of them asked for.

1. Worktrees + `PROTOCOL.md` + the three charters. **Verify the ≤ 20 KB reading budget here**, before anything is deleted.
2. `status/<role>.md` + the board render + `queue/`.
3. Archive `leads/`, `inbox/`, `bridge/`, ruled proposals; retire `sweep.py` / `watch.py` / the attribution hook.
4. `AGENTS.md`, `CLAUDE.md`, the doorbell.

Four commits, each revertible alone. Step 3 is the only irreversible-feeling one and it comes *after* the new world is proven.

## 5. Before archiving: check what points only at what is being archived

The §11 checklist already protects the proposals that open decisions point at (`initiative-and-earmarks` and the rest). Two more, by hand:

- **C23** — the oldest outstanding item, delivered into `leads/chief-of-staff.md` §For Systems. When `leads/` is archived, **the only live pointer to it goes with it.** It belongs in the Designer's first task or in `queue/`, not in an archive folder.
- **Four decision rows are logged but not closed** (`D5.46`/`D5.47`/`D5.50`/`D5.51`): the rule text still lives only in a proposal, and `10`/`11`/`12` are stubs. Archiving is fine — burying is not. Say in the row or the charter where the text still sits.

## 6. The two clauses worth defending

- **The budgets** (`PROTOCOL.md` ≤ 2 pages · board ≤ 1 page · charter ≤ 1 page · ≤ 20 KB read before the first useful act) are the best idea in the document: the only rules here that are **measurable**, and the only ones a future session cannot argue with. Give the Steward's audit one line that checks them, or they decay like every other cap.
- **The hard stop** (§7.3, §10.9): next session is Designer with the owner on `02-ontology.md`; no process change until a paper duel is played. **Every prior stop in this project was skipped.** Make it concrete — the migration's last commit message says what the next session is, and the queue is seeded with game questions only.

## 7. One gap the new design opens

The stop step commits everything in a worktree — **if the session reaches stop**. A session that dies mid-work leaves a dirty worktree nobody opens again, and the unclaimed-work report that used to notice exactly that is being retired (correctly — per-role worktrees make attribution structural). One line in the start step, reporting any worktree with uncommitted changes, closes it for free.

---

**Written into the Steward clone and left uncommitted** — by design, the next Steward session's stop step sweeps its own worktree, so this arrives in the record under the Steward's name without anyone declaring anything. That is the new model working; no action needed.
