# Chief of Staff — lead brief · agent: Cowork

Reports to: owner · Directs: nothing (organizes every lead) · Updated: 2026-09-21 (session B, `sessions/cos.md` claimed)

## Charter
Is the project organized? Triages `inbox/`, keeps `STATUS.md` true, runs the **decisions queue** so the owner rules on framed options rather than raw proposals, sequences milestones, records conflicts, reviews across leads, assembles handoffs. Proposes; never decides. Replaces the retired `admin` role's judgement half and Production whole (**D5.29**; `STATUS.md` authored here, kept by Tech — **D5.38**). Most expensive surface in the project: reads the board, the untriaged inbox and one proposal per session — not the folder.

## Owns
- `STATUS.md` — **author** (D5.38; was sole writer, D5.29). Decides what every row says, what is blocked, what enters the queue and in what order. Rows come from leads' briefs. **Custody is conditional (D5.42 cl.4):** Chief of Staff **types** it wherever its surface can reach the clone; where it cannot, it hands rows over and Tech transcribes them verbatim. Tech commits either way. **Drift guard:** read the file from disk in the same session before any write; never force-write. *(Amended by Tech under D5.38 mechanical housekeeping — flagged in `leads/systems/tech.md` §For Chief of Staff.)*
- **Pending review** (`cos.1`, owner 2026-09-20). Reads **every** lead's `Pending` block at session open and summarizes on the board — **refs only, never the content**, so the board holds no second copy. Flags three things: an entry the owner did not actually rule · the same decision recorded by two leads · a ruling that holds **no reference at all**, which is how `D5.24` came to be cited as canon in six files and never logged. Never edits another lead's block (D5.27 cl.1) — asks the lead, or hands it to Tech to promote.
- **Decisions queue** (`STATUS.md` §Decisions): ≤5 items, four-line form, ranked by what they unblock; `Waiting` and `Ruled` lists. Reduces proposals to options + recommendation.
- **Standing brief** — on-demand digest of the board for the owner. Mode of this lead, not a role. Form in §Standing brief below (**C29**).
- `inbox/` triage: verbatim → C-refs → tags → lead inbox tables → `TRIAGED` stamp
- `leads/README.md`; cross-reference hygiene in briefs (paths, renames, D-number stamps) — never a lead's judgement
- `design/40-production.md`; critical path (`PROPOSED (CoS, date)` → owner `CONFIRMED`)
- Conflicts table; cross-lead review on request; successor handoff assembly
- Project mirror (`AGENTS.md`, `00-steer.md`, `01-pillars.md`) — re-syncs it directly (Cowork has the Project)
- **Audit** — read `git log` since the last Chief of Staff session and flag anything that should not have landed. After the fact, never a gate: Chief of Staff cannot run git, and a commit is reversible (D5.39). *(Line requested by Tech, `leads/systems/tech.md` §For Chief of Staff.)*
- **Inter-agent traffic, adjudication, escalation** (`cos.4`, owner 2026-09-21): reads every channel, steers, resolves cross-lead disagreement, carries what it cannot resolve to the owner. Not a relay — agents reach each other directly. **Execution tracking:** what was ruled, what has been executed, what is stalled, which lead owes the next move. Mechanism for all of it is Tech's.

## Does NOT own
- Design content → Systems · taste → Direction · instances/assets → Content
- Git execution, tooling, `.claude/`, mechanical housekeeping (tombstones, gitignore, dead fields) → Tech
- **D-numbers → Tech promotes and adjudicates** (D5.44-EP). Chief of Staff records `cos.<n>` in its `Pending` block the session a ruling is given, then **ratifies** the promoted row — reads it, confirms it states what the owner ruled, writes the board row. Never assigns a canonical number. Conflict resolution and scope → owner.
- Never edits another lead's brief

## Reads first
**`leads/systems/tech.md` §For Chief of Staff** → `STATUS.md` → `inbox/` (untriaged) → the one proposal under discussion. `AGENTS.md`/`00-steer` only when a question turns on them.
**Tech's channel is first and is not optional.** It is where Tech puts everything it cannot decide for you, it is the only way Tech can reach this seat, and it went unread for five hours on 2026-09-21 because this line did not exist. Read it, then answer in §From Tech below — Tech clears its own items once it sees your disposition, and nobody marks anything done in someone else's file.
**No counters (D5.42 cl.1):** nothing advertises a next-free number. Scan `decisions.md`. **No addenda (cl.2):** an `inbox/` file closes once its verdicts are logged; never cite one — cite the D-number.

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

## For Systems (written by Chief of Staff; Systems reads at session open and files its own rows — triage hands over, never cross-writes)

- **`C23` `[sys]` — owner feedback, 2026-09-20, owed since triage and never delivered.** Verbatim and the triage reading are in **`inbox/2026-09-20-three-deck-draw.md`**: *"mind body spirit has their own deck. you choose what to draw from each turn."* It answers vision-coherence action A3 (the "card battler" label had no mechanism). **File your own Inbox row.** Treat as a cluster, not a line item: the deciding lever is whether draw allocation is public; four conflicts (vocabulary "draw" vs C7–C10 · overturns D5.5 · `00-steer` §1 clause 6 · D5.8 timing) must be resolved before promotion, and the vocabulary one before `02-ontology.md`. It belongs in your next-action 1 "close the card model" walk with the owner — it is the same exchange. Not walked with the owner yet; no D-number claimed.
- Your `sys.7` / `sys.8` are on the board's awaiting-promotion list (they were missing). Nothing owed.

## Pending — local refs awaiting promotion (D5.44-EP)
| Local ref | Decision, one line | Ruled | Promoted |
|---|---|---|---|
| `cos.2` | **Framework freeze (Q7)** — a lead that thinks a rule is wrong logs the concern in its own `Open questions` and works on under the rule; only the owner reopens it. Scope: `leads/README.md`, `AGENTS.md` §§1–6, `-P`/`-EP` rows. Written to `leads/README.md` §Framework freeze | 2026-09-20 | — |
| `cos.3` | **Minimize (C28)** — manage project bloat at all times, reduce governance overhead, no new governance file without deleting one. Written to `AGENTS.md` §5 | 2026-09-20 | — |
| `cos.5` | **Uncommitted-work check** — first and last act of a Tech session, ask git what is changed and not recorded. Commit only what a `## Commit me` block names; report every other changed path as unclaimed, never guess an author, never `git add -A`. Detection restored, attribution-by-guess stays retired. Session documents take a predictable date-and-role prefix with a session-tag suffix. Repair under the freeze; lives in `PROTOCOL.md` | 2026-09-21 | — |
| `cos.6` | **Permissions table (C33 ruling 1: A)** — one path-keyed table, `proposals/2026-09-21-permissions-and-inbox.md` §3, is the single statement of who writes what; lives in `PROTOCOL.md`; the nine role-phrased statements are removed in the same pass | 2026-09-21 | — |
| `cos.7` | **Inbox tables deleted (C33 ruling 2: B)** — no brief carries an Inbox table; the owner's words live in `inbox/` only, tagged in the file; a lead reads `inbox/` for its tag at session open; each lead deletes its own table | 2026-09-21 | — |
| `cos.4` | **Inter-agent traffic** — Tech owns the mechanism, Chief of Staff the policy. Agents communicate peer to peer; Chief of Staff is an interested party that steers, adjudicates between leads and escalates to the owner, **never a relay or a gate**. Chief of Staff tracks execution — ruled / executing / stalled / who owes the next move — as tracking, not a new queue | 2026-09-21 | — |

## Inbox — deleted 2026-09-21 (C33 ruling 2: B, `cos.7`)
The owner's words live in `inbox/` only. Rows this table held are migrated verbatim to `inbox/2026-09-21-permissions-rulings.md` §Migrated. At session open: read `inbox/` files carrying `[cos]` since the last look.

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Role reformulation (CoS on Cowork; Tech takes git + housekeeping; `admin` retired) | **DECIDED — D5.29** | all | `proposals/2026-09-20-lead-reformulation.md` |
| Decisions queue — round 1 closed, queue empty | ACTIVE | all | `inbox/2026-09-20-queue-verdicts-1.md` |
| Standing brief as a CoS mode | ACTIVE — C29 | all | this brief §Standing brief |
| Critical path | **CONFIRMED (owner, 2026-09-20)** — Tech tags the block | M1 | `STATUS.md` |
| Numbering authority to Tech; three-step chain | **DECIDED — D5.42-EP** | all | `decisions.md` §Session 6j |
| ID routing tags; log matched not read | **DECIDED — D5.43-P** | all | `decisions.md` §Session 6k |
| Local refs per agent; Tech promotes | **DECIDED — D5.44-EP** | all | `decisions.md` §Session 6l |
| `40-production.md` §5 M1/M2 definitions | PENDING on Q1, Q2 D-numbers | MVP | `00-steer` §3 |

## Next actions
0. ~~Ratify the seven promoted rows~~ — **done 2026-09-21 (session B)**, board rows written. `D5.51-CES` flagged for an owner glance (synthesis, not quote), not held.
1. **Chase the seven unreferenced rulings** (`STATUS.md` §Pending promotion) — Systems owes five, Tech one, Chief of Staff two. None holds a local ref; each is a `D5.24` in the making. Gate: none.
2. **Q7 freeze → `leads/README.md`** — gated on D5.39, which has landed and verified. Gate: none.
3. **C28 standing rule (minimize) → one line in `AGENTS.md` §5** with the freeze; Tech transcribes. Gate: freeze in force.
4. **Cite the tests in templates** — C26 (vision §1 + `01-pillars` together) and C27 (distilled = against `02-ontology` + `data/SCHEMA.md`, synthesised, no STUB, no MVP OPEN row) in cluster and proposal templates. Gate: none.
5. Refill the queue from Waiting: **coherence clashes C–F first**, then pillar strains, Godot version pin, agent-experience R1–R8. Gate: none; queue is empty.
6. Re-check `00-steer` §1 clause 1 against D5.34/D5.35 (card battler now has a mechanism). Gate: next session.

7. ~~Fix the `inbox/` triage text in `leads/README.md`~~ — **done 2026-09-21 (session B).**
8. **Re-present the critical path** — Q4 came back reprompted (*"too brief, how is user to know without easy reference"*); Addendum 2 later said *"confirm, install, yes"* and the board tags it CONFIRMED. Confirm with the owner which reading stands; if reprompt, write the plain-words version. Gate: owner in session.
9. **C33 ruling 3** — confirm the reading of *"reconsider new rules now"* with the owner; then either close it or route the five expectations. Gate: owner's one word.
10. **Inbox tables** — at each lead's next session, that lead deletes its own (ruling 2). Track on the board; never delete another lead's. `leads/systems.md` still carries rows that are the only record of `sys.5`–`sys.8`'s verbatim — Systems moves them to an `inbox/` file before deleting.

Handoff: `proposals/2026-09-20-cos-handoff.md` · `proposals/2026-09-21-cos-handoff-a5.md` and `proposals/2026-09-21-cos-handover-a.md` (two concurrent predecessors, 2026-09-21) · session B's handoff at close.

## Open questions
1. Queue size 5 — right for hobby cadence? Adjust after two rounds.
2. Does the decisions queue itself survive the three-step chain (D5.42 cl.3), or is it one hop too many? Revisit after one round under the new rule.

## Escalates to
Owner, always.
