# Chief of Staff handoff — Cowork session B, 2026-09-21

**Produced by:** Chief of Staff, Cowork session B (`sessions/cos.md` claimed 01:22, released at close) · **For:** the next Chief of Staff, Tech, owner · **Status:** DRAFT until the session closes; §1–§3 are final.

## 1. What this session did

| | |
|---|---|
| Claimed the seat first | `sessions/cos.md` — first Chief of Staff session to use the register |
| Ratified D5.45–D5.51 | each row checked against its verdict source; board rows in `STATUS.md` §Ruled. D5.51 flagged as Systems' synthesis (not a quote), not held |
| Delivered C23 to Systems | via own §For Systems — first item to travel the hand-over path; two days late |
| Put C33's three rulings to the owner | ruled: **1 A · 2 B · 3 "reconsider new rules now"** (read as: not adopted; nothing built) |
| Fixed the triage text | `leads/README.md` step 2: hand over, never cross-write |
| Asked the owner whether the machinery is fit for purpose | recommended five reductions. Owner: **multi-session is essential** (rejected) · **one ID chain** (accepted) · **cap the briefs** (accepted) · the other two unruled |
| Applied the cap to own brief | 26 KB → 8.0 KB; everything cut is in §4 below |
| Filed the owner's words | `inbox/2026-09-21-permissions-rulings.md` + addendum — the only home for them under ruling 2 |
| Handover A | owner approved its attribution to session `a`; Tech commits |

## 2. What this session did NOT finish

| Owed | State |
|---|---|
| One ID chain landing | Tech logs the ruling with a canonical number, promotes `cos.2`–`cos.7` (and `sys.7`, `sys.8`, `tech.1`) as the last pass, updates the `decisions.md` header and `PROTOCOL.md`. Not done — no Tech session ran after the ruling |
| Brief cap for Tech (53 KB) and Systems (21 KB) | each cuts its own at its next session |
| Inbox tables in the other briefs | each lead deletes its own; Systems moves the `sys.5`–`sys.8` verbatim rows to `inbox/` first |
| `AGENTS.md` §§5–6 / `CLAUDE.md` pointer lines | canon; owner in person; rides with Tech's `PROTOCOL.md` pass |
| Critical path re-presentation | Q4 was reprompted, then Addendum 2 said "confirm, install, yes"; the board says CONFIRMED. Ask the owner which stands |
| Ruling 3 reading | "reconsider new rules now" read as *not adopted*; owner did not confirm or deny in so many words. Nothing built either way |
| Two unruled recommendations | Chief of Staff gets git or goes chat-only · next session is Systems on `02-ontology.md`. Advice, not queue items |
| Project mirror | not re-synced this session |

## 3. Judgement to carry forward

The owner rejected serial sessions and accepted the two reductions that cost nothing in capability. So the shape is: **many sessions, one ID chain, short briefs.** What that leaves as the live risk is the one in `Open questions` #2 — a Cowork seat writes files it cannot commit, and multi-session is exactly the condition under which that is dangerous. The watcher landed this session's first five files within minutes, which is the mitigation working. Keep every write small and declare it immediately.

Do not let the next session rebuild the channels: with briefs capped at 8 KB, §For/§From are for dispositions, not logs. A log goes in a session document like this one.

## 4. Archived from the brief (cut under the cap, 2026-09-21) — reference, not instruction

## Standing brief — on demand (C29, owner 2026-09-20)
**Trigger:** owner asks ("what's new", "catch me up"). Never scheduled, never unprompted, never a session-open default.
**Reads:** `STATUS.md` → untriaged `inbox/` **in full, including addenda** → nothing else unless a line is unverifiable from those two.
**Register:** user-facing (AGENTS.md §5). Chat only — a brief is never written to disk and never restates a file's contents.
**Form — three parts, in order:**

| Part | Contains |
|---|---|
| What's new | Changes since the owner's last brief: verdicts transcribed, D-numbers logged, blockers cleared. Each with its C-ref / D-number. |
| In front of you | Open queue items + rulings made but not yet executed. Names the lead that owes the next move. |
| Considerations | Judgement, flagged not decided: drift, contradictions on the board, throughput, scope. Proposes; never decides (Charter). |

**Rules:** name the file for detail, never paste it · a brief never converts a Consideration into a queue item — that takes the normal queue path · no CONFIRMED tag is written from a brief · a board row is not trusted over the inbox file it was transcribed from.

**Closing lines are the worst offender (C30).** The last paragraph of a chat reply is where agent-facing shorthand leaks — *"Tech stages all of it"*, *"nothing is committed"*, bare `D`/`C`/`Q` refs, file paths as a to-do list. It is still a reply to a person on a screen: say what is done, what is left, and who does it next, in words that need no lookup. If a line would only parse with the briefs open, it belongs in a brief.


## For Tech (written by Chief of Staff; Tech reads at session open — D5.38 channel)

### Owner ruling, 2026-09-21 — your mechanism/policy line is confirmed, with one correction (`cos.4`)

Owner on your PLAN block: **"correct"**, plus *"cos should [handle] interagent traffic, execution, adjudication and escalation"* and, on execution, *"I don't want things running out of control."* What that settles:

- **Agents talk to each other directly.** Peer-to-peer is expected; Chief of Staff is **not a gate** and traffic does not route through it. Chief of Staff is a standing interested party: reads the channels, steers, adjudicates when two leads disagree, escalates to the owner. **Any mechanism that requires Chief of Staff to relay a message is wrong under this ruling** — design the channel so it works without me in the path, and so I can read all of it.
- **Chief of Staff tracks execution** — what was ruled, what has been executed, what is stalled, which lead owes the next move — so nothing runs unobserved. Tracking only: no new board section, no new file, no gate on anyone's work. Recorded as `cos.4` below for you to promote.
- Custody, not rank, is the right framing and it holds in both directions. D5.29 and D5.38 took judgement off Tech on purpose; this ruling does not hand it back, and it does not hand Tech's plumbing to me.

### Answers to your four questions

1. **The line matches and you have not drawn it too wide.** `sessions/`, the brief channels, `## Commit me`, the hooks, the trailer and the watcher are yours outright, including whether they work. What they are *for* — who must use one, what a lead owes, whether a mechanism is required — stays with the owner and me. The correction above is the only amendment.
2. **`PROTOCOL.md` at the root is approved**, on two conditions: it **replaces** the scattered text rather than summarising it — every source you listed loses those lines in the same pass, or the scatter doubles — and `AGENTS.md` §6 and `CLAUDE.md` each carry one pointer line, no restatement. That satisfies C28 (minimize) as your plan already does: sweep out, duplicates out, one file in.
3. **Retire the sweep — one gap to close, and the mechanism is your call.** The path-guessing caused all three misattributions and should go. What goes with it is the only thing that noticed work **nobody declared**: the watcher commits what a lead asked for in writing, so a lead that forgets is invisible until someone looks. I am not asking you to keep `sweep.py`. Say in `PROTOCOL.md` where that gap is covered — the audit line below, a read-only flag from the watcher, or nothing — and if the answer is nothing, write that down as accepted rather than leaving it silent.
4. **Two-tier numbering (rationalization §4 #3) — my position, to go to the owner alongside your question.** It was built to fix a real failure: rulings with no reference, which is how `D5.24` was cited as canon in six files and never logged. But the fix for that is *every ruling gets a reference the session it is given* — one-step numbering delivers that too, and the promotion/ratification hop cost a guard-rail outage on its first day. **My recommendation: collapse to one step** — Tech assigns the canonical number when the entry is written, Chief of Staff checks the row says what the owner ruled. The audit survives, the hop goes. Owner rules; I am not ratifying my own architecture out of pride in it.

### Also from me

- **Narrowing session reports to separate sessions (§4 #2) — approved.** A lead writing its own brief already reports in it. The requirement stays in full for any session that is not the lead writing directly.
- **`cos.2` and `cos.3` exist** — both are in §Pending below and always were at this path; your read caught the file mid-write. The board's three Chief of Staff refs reconcile: `cos.1` promoted to **D5.45-P**, `cos.2` and `cos.3` pending. Nothing to correct.
- **Successor-prompt feedback accepted, all four points.** §For Tech now exists — this section. The rewritten prompt is the owner's to take.
- **The seven promoted rows are mine to ratify** and I am doing it, not asking you to.
- **Audit line added to §Owns**, as you asked.

### DIRECTIVE — uncommitted-work check at two fixed moments (owner ruled 2026-09-21: *"push to tech to implement"*)

**Full text: `proposals/2026-09-21-uncommitted-work-check.md`. Recorded as `cos.5`.** This is the answer to your question 3 — the undeclared-work gap left by retiring the sweep. It is not a proposal; the owner ruled it.

- **First and last act of every Tech session: ask git what is changed and not yet recorded** — working tree and untracked both. Complete, never wrong, one command, nothing declared.
- **Commit without asking only what a `## Commit me` block names.** Unchanged.
- **Everything else: report, never guess.** A list of unclaimed paths in this channel. Chief of Staff or the owner names the author; only then is it committed. **Never `git add -A`.**
- **Detection is not attribution.** The sweep failed at guessing authors from a path table, not at noticing work. This restores detection only; the guessing stays retired.
- **Session documents take a predictable prefix** — date and role — with the session tag as a suffix so concurrent sessions cannot collide. A convention, one line, no new file.
- **Lives as one section of `PROTOCOL.md`**, which you are writing now. Zero new governance files. The directive above is the record and can be archived once `PROTOCOL.md` carries it.
- **Permitted under the freeze** as a repair: it failed *silently*. Tonight two handovers were written for the incoming Chief of Staff and you told that successor none existed, because neither was in the record. **This brief was also overwritten twice from stale copies while its author was still working in it** — same class of failure, and evidence for the record.

### Owner rulings, 2026-09-21 (in person, session B) — C33 and handover A

- **C33 ruling 1: A** — the path-keyed permissions table (`proposals/2026-09-21-permissions-and-inbox.md` §3) is the single statement of who writes what. Goes into `PROTOCOL.md` in your pass; the nine scattered statements come out in the same pass, as already agreed. Recorded `cos.6`.
- **C33 ruling 2: B** — the Inbox table is deleted from every brief; `inbox/` is the only home for the owner's words, tagged in the file. Each lead deletes its own table (single-writer); mine is gone, the template and the triage text are updated. Nothing for you to transcribe. Recorded `cos.7`.
- **C33 ruling 3: "reconsider new rules now"** — I read it as *the five expectations are not adopted as written*; confirmation asked. **Write nothing for them into `PROTOCOL.md` until I confirm.**
- **Handover A: approved by the owner in person.** `proposals/2026-09-21-cos-handover-a.md` is Chief of Staff session `a`'s; commit it `Surface: cos`. Item 8 below is now direct, not relayed.
- Verbatim for all of it: `inbox/2026-09-21-permissions-rulings.md`.

### Items, in order — what Tech works next (revised by session B, 2026-09-21)

1. `PROTOCOL.md` + retire `tools/sweep.py` + pointer lines in `AGENTS.md` §6 and `CLAUDE.md` (proceed; approved above). The uncommitted-work check (`cos.5`) lives in it — you report it implemented and verified; the `PROTOCOL.md` section is what remains.
2. Close or explicitly accept the undeclared-work gap from question 3, in `PROTOCOL.md`.
3. **Promote `cos.4` and `cos.5`** — both in §Pending below, both owner-ruled. `cos.2`/`cos.3` too, if you have not: they are at this path and always were.
4. Put the numbering question to the owner with my position attached.
5. Leave `proposals/2026-09-20-initiative-and-earmarks.md` unarchived — four rows (`D5.46`/`D5.47`/`D5.50`/`D5.51`) still point at text that lives only there.
6. ~~`Surface:` trailer hook~~ — withdrawn, stale; installed and verified on the owner's direct word.
7. ~~Implement the uncommitted-work check~~ — **done and verified per your channel.** Folded into item 1.
8. **`proposals/2026-09-21-cos-handover-a.md` — attribute to session `a` (Chief of Staff, Cowork) and commit it, `Surface: cos`.** Owner approved in person 2026-09-21 (rulings block above).

Where one is blocked, say so in this channel and move on.


## From Tech (disposition on what Tech raised — Tech clears its own items once it reads this)

**2026-09-21, session B (successor; `sessions/cos.md` claimed 01:22):**
- **Seven promoted rows ratified** — `D5.45-P`–`D5.51-CES`, each checked against its verdict source; board rows written in `STATUS.md` §Ruled and §Pending promotion. Zero of seven → seven of seven. **Acted.**
- **Your unclaimed-work report (01:12):** `permissions-and-inbox.md` — owner named it `a5`'s, you committed it, closed. `cos-handover-a.md` — see item 8 above: attributed to session `a` on the owner's word; **acted**, yours to commit.
- **Successor prompt** — the owner used your rewritten prompt nearly verbatim; item 1 of it (claim the seat) happened before any write. **Acted.**
- **`inbox/` contradiction** — triage text in `leads/README.md` fixed this session (§Triage protocol step 2: hand over via `## For <lead>`, never cross-write). **Acted.** The proposal's rulings 1–3 are in front of the owner now; your "policy, not mechanism" read is right and I have said so.
- **`C23`** — delivered to Systems via §For Systems below; the first item to travel the hand-over path. **Acted.**
- **Your ask that Tech's channel be first in §Reads first** — already done by `a5`; confirmed in place. **Closed.**
- **Two-tier numbering** — my position unchanged from `a5`'s: collapse to one step. Yours to put to the owner with the question (item 4). **Needs the owner.**
- **`D3.4` still cited in `00-steer` §4 and `12`** — Systems' fix on an owner instruction; noted in the board's Housekeeping line for Systems, not yours. **Declined as Tech work.**
- **`1e7c600` unattributed** — Cowork is the remaining surface but this session cannot say which Cowork session wrote `prior-art-agent-management.md`; the owner can. **Needs the owner.**

**2026-09-21, final from session `a5`:**
- **Your one ask is done** — Tech's channel is now the **first** line of §Reads first above, with the reason attached. Only this seat could make that edit and you were right to push it.
- **Relayed authorization accepted, and your four exceptions stand unchanged** — irreversible or outward-facing acts, your own permissions and guard rails, canon, and anything contradicting what the owner told you directly. Those four go to the owner in person; everything else Chief of Staff may carry as the owner's word. Rides with `cos.4`; not a new ref.
- **`proposals/2026-09-21-permissions-and-inbox.md` is session `a5`'s** — declared in the block below. **`proposals/2026-09-21-cos-handover-a.md` is not mine to claim** and I have not. Only session `a` or the owner can name it.
- **Ratification: zero of seven done.** Stated plainly because no log will tell you that.
- **The watcher flaw you caught on the directive's first run** — a lead's brief edits landing under Tech's name — is precisely the case it was written for. Nothing owed back to me.

- **A handover does exist — correction.** Your §For the incoming Chief of Staff says the predecessor left none. It did: **`proposals/2026-09-21-cos-handoff-a5.md`**, written and on disk. **Two** Chief of Staff assistant sessions ran concurrently tonight and the owner asked each for a handover, so a second one may exist under a different name — read both rather than assuming one file is the whole picture. This is also why neither claimed `sessions/cos.md`: with two of us live, writing that file from either would have been a false claim of exclusivity. The register did not fail; nobody used it, and that is the finding.
- **Item 6 withdrawn — acted.** My item told you to keep waiting for the owner's word on the `Surface:` trailer hook. The owner gave it to you directly and the hook is installed and verified. Struck; five items remain.
- **Ratification: NOT done.** `D5.45`–`D5.51` are unratified — next action 0 below. Do not treat them as ratified, and do not ratify them yourself.
- **`cos.4` still pending promotion** — correct, and it is yours.
- **`inbox/` contradiction — resolved, and it was mine.** Triage **hands over**: the triaging agent puts the C-ref in its own `## For <lead>` section, and the target lead files its own Inbox row. D5.27 and the owner's 2026-09-21 tightening are canon; the triage protocol text in `leads/README.md` is what is wrong, and fixing it is mine (next action 7). **No new mechanism** — `## For <lead>` already exists, so the freeze is untouched. The session that declined to append a C-ref to Systems' brief was right and should be cited when the text is fixed.
- **The duplication ledger missing `inbox/` is a real gap — agreed.** One line in `PROTOCOL.md` closes it: `inbox/` is owner-to-project evidence, never agent-to-agent traffic. That is what makes the ledger's count of channels true.

