# Chief of Staff handoff — Cowork session `a5`, 2026-09-21

**Produced by:** Chief of Staff assistant, Cowork session `a5` · **For:** the Chief of Staff successor (`cos-lead`), Tech, owner · **Status:** record, not proposal.

> **Two Chief of Staff assistant sessions ran concurrently tonight and the owner requested a handover from each. This is one of two.** Read both; do not merge by overwriting. This session wrote exactly two paths: `leads/chief-of-staff.md` (its own brief, every write guarded against the on-disk timestamp) and this file, whose name carries the session tag precisely so it cannot collide with the other handover. Nothing else was touched.

---

## 1. What this session did

| | |
|---|---|
| Relayed Tech's two new channel blocks to the owner | `leads/systems/tech.md` §For Chief of Staff — the PLAN block and the successor-prompt feedback |
| Took the owner's ruling on inter-agent governance | logged as **C31** in §Inbox, **`cos.4`** in §Pending, written into §Owns |
| Opened the missing `## For Tech` channel section | `leads/chief-of-staff.md` — Tech's feedback point #1 was that it did not exist; it now does |
| Answered Tech's four questions | in that section, with a recommendation on the one that goes to the owner |
| Queued six items for Tech, in order | same section — this is what makes a Tech successor prompt pointing at "§For Tech" valid |
| Added the audit line Tech asked for | §Owns: read `git log` since the last Chief of Staff session, flag what should not have landed, after the fact, never a gate |
| Requested a commit via the watcher | `## Commit me` block in the brief, naming only `leads/chief-of-staff.md` |

**Not done, and owed:** ratifying the seven rows Tech promoted (`D5.45-P`, `D5.46-ES`, `D5.47-AES`, `D5.48-ACPS`, `D5.49-EPS`, `D5.50-CES`, `D5.51-CES`). It is next action 0 in the brief. **Do not skip it** — the whole promotion chain is unfinished until someone confirms each row states what the owner actually ruled.

## 2. The governance model as it stands tonight

Eight things are settled enough to build on. The successor's job is to cement them, not to relitigate them.

1. **Mechanism vs policy.** Tech owns how sessions identify themselves, how surfaces reach each other, how work is committed, checked and attributed. The owner and Chief of Staff own who exists, which roles there are, who answers to whom, what a lead owes, and whether any mechanism is mandatory. Owner: *"correct."*
2. **Custody, not rank** — in both directions. Tech keeps the record, so commit format, hooks, paths and git are Tech's. A rule is Systems', a look is Art's, a sequence is Chief of Staff's, a decision is the owner's. Tech deferring to those is the same principle, not a different one.
3. **Agents talk to each other directly.** Peer to peer is expected. Chief of Staff is **not a gate and not a relay** — it is a standing interested party that reads the channels, steers, adjudicates between leads, and escalates to the owner. *Any mechanism that requires Chief of Staff in the message path is wrong under `cos.4`.*
4. **Chief of Staff tracks execution** — ruled, executing, stalled, who owes the next move — so nothing runs unobserved. Owner: *"I don't want things running out of control."* Tracking, not a new queue, not a gate.
5. **Authority reaches each session on its own.** A peer relaying an owner ruling does not make it that session's authority, and a peer's caution does not outrank a direct owner instruction to that peer. Both can be correct at once; tonight both were.
6. **Attribution is prose, not data.** Three surfaces share one clone and one git identity, so no automated check can tell them apart. `sessions/` answers *who is live*, the proposed `Surface:` trailer answers *who wrote this*. The trailer is still waiting on the owner's word **in a Tech session** — it was refused on a relay, correctly.
7. **The freeze is in force** (Q7): no new governance mechanism until a human has played a duel, except to repair something that refused legitimate work or failed silently. Concerns get logged in a brief, not built.
8. **Minimize** (C28): no new governance file without deleting one.

**The finding underneath all of it:** 50 decisions logged, **31 about how we work**, 19 about the game. 31 proposals. 11 of 14 design docs still stubs. Ontology, schema and demo absent. **Duels played by a human: zero.** The scope rule was applied to the game all night and never once to the machinery around it. Tech wrote that about its own work, which is the right way for it to have surfaced.

## 3. Open for the owner

| # | Question | Where it came from | My position |
|---|---|---|---|
| 1 | **Two-tier decision numbering** — local refs, promotion, ratification — worth its cost at 50 rows with one decider? | rationalization §4 #3 | **Collapse to one step.** It was built to stop rulings going unrecorded; one-step numbering does that too, and the extra hop cost a guard-rail outage on day one. It is my architecture and I am not defending it out of pride |
| 2 | **`Surface:` commit trailer** — adopt as required? | Tech, waiting | Adopt. It is the only thing that survives the move to one clone per surface. Needs your word in a Tech session, not a relay |
| 3 | **`CLAUDE.md` tells every Claude Code session it is Tech** — now false, there is an art execution agent | Tech | Needs one sentence from you. Tech will not edit canon because a peer asked, and it is right not to |
| 4 | **Does the art execution agent commit its own work?** | Tech | Yes — its own name, no guessing. It is why its one commit is attributed correctly where three of Tech's sweeps were not |
| 5 | **One committed image per board folder (D5.28)** — widen the check? | art agent | Rule question for Art and Systems, not Tech. Tech implements whatever is ruled |
| 6 | **Critical path is still `PROPOSED`** — Q4 came back reprompted: *"too brief, how is user to know without easy reference"* | board | Chief of Staff owes the re-presentation. Still owed |
| 7 | **Commit `1e7c600` is unattributed** — the art agent has confirmed it is not theirs | Tech | Cowork is the remaining surface. Someone should say so and a correction commit follows |

## 4. In flight

- **Tech is proceeding now** on: one `PROTOCOL.md` at the root replacing rules currently scattered across nine files, retiring `tools/sweep.py`, and pointer lines in `AGENTS.md` §6 and `CLAUDE.md`. Approved by me on two conditions (it *replaces* rather than summarises; one pointer line each, no restatement).
- **One gap I flagged and Tech owes an answer on:** the watcher only commits what a lead asked for in writing, so a lead that forgets is invisible. The retired sweep was the only thing that noticed undeclared work. Tech closes the gap in `PROTOCOL.md` or writes down that it is accepted.
- **`proposals/2026-09-20-initiative-and-earmarks.md` must not be archived.** Four logged rows (`D5.46`, `D5.47`, `D5.50`, `D5.51`) point at rule text that lives only there.
- **Pending promotion:** `cos.2` (framework freeze), `cos.3` (minimize), `cos.4` (inter-agent traffic).
- **Seven rulings still hold no reference at all** — Systems owes five, Tech one, Chief of Staff two. Each is a `D5.24` in the making.

## 5. Guidance to the Chief of Staff successor

**Read, in this order, and stop:** `STATUS.md` → `leads/chief-of-staff.md` (your brief, including `## For Tech`) → `leads/systems/tech.md` §For Chief of Staff → this file and the other session's handover. Nothing else unless a question turns on it. You are the most expensive surface in the project; reading the folder is how that cost stops being worth paying.

**Claim `sessions/cos.md` before you write anything.** Neither Chief of Staff session tonight claimed it — the register exists precisely because two Tech sessions once spent hours rebuilding each other's work, and tonight two of *us* ran. Creating the file is the claim; finding one already there is the collision, and a collision is a question for the owner, not something to resolve by overwriting.

**You have no shell.** You write into the clone directly and you cannot commit. Ask with a `## Commit me` block in **your own brief** — the block's location is your attribution, so never declare a surface and never ask another lead to type your rows.

**Before any write to a file another surface touches:** read it from disk in the same session, and guard the write against what you read. Never force-write. Tonight's most expensive class of failure was two hands on one file.

**The standing rules that are easiest to break:**

- Never edit another lead's brief. Propose; never decide.
- Board holds refs, never a second copy of the content.
- You do not assign decision numbers. You record a local ref the session a ruling is given, then ratify what Tech promotes.
- Closing lines to the owner are plain English. No bare refs, no file paths offered as a to-do list — if a line only parses with the briefs open, it belongs in a brief (C30).
- Disagree with a rule? Log the concern in your own `Open questions` and work on under it. Only the owner reopens.

**And the one that matters most right now: do not build.** Every instinct this project has rewarded for two days has been to design another mechanism. The freeze is in force, the machinery already outweighs the game it is for, and the correction started with the surface that built the most of it. Bias every call toward subtraction. If you find yourself proposing a new file, a new register or a new tier, the answer is almost certainly a line in an existing brief.

## 6. For `cos-lead`, cementing the protocol

Treat §2 as inputs, not open questions — the owner has ruled on the split, on traffic, and on execution tracking. Tech's four questions are **answered** in `leads/chief-of-staff.md` §For Tech; that section is the current policy statement and `PROTOCOL.md` should be consistent with it, not a second version of it. The genuinely open items are the seven in §3, and of those only #1 changes the shape of the model.

The failure mode to design against is the one this project keeps producing: **a rule written in five places, and a second session rebuilding what already exists because it could not find the first.** One home per rule, one pointer from everywhere else.
