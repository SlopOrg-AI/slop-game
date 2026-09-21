# Chief of Staff handoff — Cowork session `a5`, 2026-09-21

**Produced by:** Chief of Staff assistant, Cowork session `a5` · **For:** the Chief of Staff successor (`cos-lead`), Tech, owner · **Status:** **FINAL** — closed 2026-09-21 after incorporating Tech's channel. §§7–10 were added in the closing pass and supersede anything earlier that disagrees.

> **Two Chief of Staff assistant sessions ran concurrently tonight and the owner requested a handover from each. This is one of two.** Read both; do not merge by overwriting. This session wrote four paths and no others: `leads/chief-of-staff.md` (its own brief, every write guarded against the on-disk timestamp), this file, `proposals/2026-09-21-uncommitted-work-check.md` and `proposals/2026-09-21-permissions-and-inbox.md` — each named with the session tag or a unique topic precisely so it cannot collide with the other session's work. No other lead's file was touched.

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

**Read, in this order, and stop:** `leads/chief-of-staff.md` (your brief, including `## For Tech`) → `leads/systems/tech.md` §For Chief of Staff → this file and the other session's handover → `STATUS.md`. *(Order corrected in the closing pass: Tech's channel is now first in the brief's own §Reads first, because nothing pointed at it and it went unread for five hours.)* Nothing else unless a question turns on it. You are the most expensive surface in the project; reading the folder is how that cost stops being worth paying.

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

---

## 7. Closing pass — what changed after §§1–6 were written

Tech's channel moved fast in the last hour. All of this is verified by Tech, not claimed here:

- **`cos.5` is implemented and verified.** `python tools/watch.py --report` lists unrecorded work, split into *declared* and *unclaimed*, and commits nothing. Detection restored, guessing still retired.
- **On its first run it caught a flaw in Tech's own watcher** — the requesting brief was being committed *after* its request was cleared, which would have put a lead's edits under Tech's name. Fixed: the request is stripped before committing, and the brief lands in its own commit tagged to its author.
- **The declare-to-commit path worked end to end** (`f05f9a0`, three paths, tagged `cos`). First time tonight a lead got work into the record without Tech carrying it by hand.
- **Relayed authorization — the owner ruled Chief of Staff may carry it.** Tech's refusal of `cos.5` is withdrawn. **Four things still go to the owner in person:** irreversible or outward-facing acts (remotes, force-push, history rewrites, deletions) · Tech's own permissions and guard rails · canon (`CLAUDE.md`, `AGENTS.md`) · anything contradicting what the owner told Tech directly. Everything else Chief of Staff carries as the owner's word.
- **Item 6 of Tech's queue is withdrawn** — the commit-attribution hook is installed and verified on the owner's direct word.
- **Tech has read `proposals/2026-09-21-permissions-and-inbox.md` and has no objection**, correctly noting it is policy rather than mechanism and therefore not Tech's to rule on. It prefers this framing of the `inbox/` contradiction to its own.
- **Tech's channel is now the first line of this brief's §Reads first.** That single missing line is why five hours of Tech's channel went unread. It was the highest-value edit available to this seat.
- **One file in the tree is still unclaimed:** `proposals/2026-09-21-cos-handover-a.md`, from the other concurrent session. Session `a5` cannot declare another session's work. Session `a` names it, or the owner does, or it sits there uncommitted.

## 8. What this session did NOT finish

No log will tell you any of this, which is the one half of a handover nobody else can write.

| Owed | State |
|---|---|
| **Ratify the seven promoted rows** (`D5.45`–`D5.51`) | **Zero of seven done.** Not started, not partially done |
| `cos.2`, `cos.3` | Recorded, **not promoted** |
| `cos.4`, `cos.5` | Recorded, not promoted. `cos.5` was implemented ahead of its promotion — correct under the ruling, but it means the record and the log disagree until Tech promotes |
| **`C23` to Systems** | **Still owed, two days running.** Owner feedback on the three-deck draw that triage could not deliver because delivering it required writing into another lead's brief |
| Critical path | Still `PROPOSED`. The owner reprompted it — *"too brief, how is user to know without easy reference"* — and the re-presentation was never written |
| Triage text in `leads/README.md` | Not fixed. Resolution is decided (hand over, never cross-write); only the text is stale |
| `sessions/cos.md` | **Never claimed.** Deliberate with two sessions live — either claim would have been false — but the register holds no record of tonight at all |
| `STATUS.md` | **This session never read it.** Everything said about the board came from the briefs and Tech's channel. Flagged because that is exactly how a confident wrong claim gets made later |

## 9. Proposed opening prompt for the successor

Owner's to take, edit or ignore. It front-loads the two things that cost the most last night — an unclaimed seat and an unread channel — and it closes the session properly, which no prompt here has done before.

```
Act as Chief of Staff. You are a lead.

1. Claim your seat first: create sessions/cos.md by hand — the template in
   sessions/README.md is the whole specification. If a claim is already there
   naming a different session, stop and ask me before writing anything.

2. Read, in this order, and stop:
   leads/chief-of-staff.md (your brief)
   leads/systems/tech.md  §For Chief of Staff  (Tech's channel to you — it holds
     ~30 items and a handover addressed to you; it went unread for five hours
     last night because nothing pointed at it)
   proposals/2026-09-21-cos-handoff-a5.md  and  proposals/2026-09-21-cos-handover-a.md
     (two predecessor sessions ran concurrently; read both)
   STATUS.md
   Nothing else unless a question turns on it.

3. Before writing to any file: read it from disk in the same session, and never
   write back a copy you read minutes ago. Three of your predecessor's writes
   were silently overwritten that way last night.

4. First four acts, in order — do not start anything new until these are done:
   a. Ratify the seven promoted rows D5.45–D5.51 against what I actually ruled,
      then write the board rows. Zero of seven are done.
   b. Deliver C23 to Systems. It has been owed for two days.
   c. Put the three rulings in proposals/2026-09-21-permissions-and-inbox.md in
      front of me, framed as options with your recommendation.
   d. Fix the triage text in leads/README.md — triage hands over, never writes
      into another lead's brief.

5. You have no git. To get anything into the record, put a ## Commit me block in
   your own brief naming the paths. Work sitting on disk is not in the record —
   that is how two handovers written for you nearly went unseen.

6. You may carry my authorization to Tech and Tech acts on it. Four exceptions
   come to me in person; they are listed in Tech's channel.

7. Do not build. The freeze stands: no new governance mechanism until a human has
   played a duel, except to repair something that failed silently. What actually
   blocks the game is design/02-ontology.md, which does not exist. If you find
   yourself proposing a new file, register or tier, the answer is a line in a
   brief that already exists.

8. At session close: update your brief, delete sessions/cos.md to release the
   seat, and leave a handover at proposals/<date>-cos-handoff-<session>.md saying
   what you did not finish.
```

## 10. One judgement to carry forward

The owner asked whether getting the agent setup right early pays off in cascading benefits. It does — but last night is a clean natural experiment on *which* structure pays, and the answer is narrower than the question:

- **Every mechanism that paid for itself was written after a failure that had already happened.** The session register (two Tech sessions collided) · the declare-to-commit block (an hour of untracked work) · the unclaimed-work report (a handover invisible to the surface that records things) · the guard rails (each refused something real, including four of Tech's own commits).
- **Every mechanism that cost was written in anticipation of one.** Two-tier numbering, party-tagged identifiers, agent namespaces and a promotion flow were locked before the documents they govern existed, and blinded three guard rails within the hour.

So the rule to carry: **build in response to a failure that actually happened, not one you can imagine.** And bound the next pass — one more iteration on the setup, then the next session is judged on whether `design/02-ontology.md` exists, because 31 of 50 decisions so far are about how we work and zero duels have been played.
