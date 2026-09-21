# Chief of Staff — lead brief · agent: Cowork

Reports to: owner · Directs: nothing (organizes every lead) · Updated: 2026-09-21

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
`STATUS.md` → `inbox/` (untriaged) → the one proposal under discussion. `AGENTS.md`/`00-steer` only when a question turns on them.
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

### Items, in order — what Tech works next

1. `PROTOCOL.md` + retire `tools/sweep.py` + pointer lines in `AGENTS.md` §6 and `CLAUDE.md` (proceed; approved above).
2. Close or explicitly accept the undeclared-work gap from question 3, in `PROTOCOL.md`.
3. Promote `cos.4`.
4. Put the numbering question to the owner with my position attached.
5. Leave `proposals/2026-09-20-initiative-and-earmarks.md` unarchived — four rows (`D5.46`/`D5.47`/`D5.50`/`D5.51`) still point at text that lives only there.
6. `Surface:` trailer hook — keep waiting for the owner's word in a Tech session; do not install on a relay.

Where one is blocked, say so in this channel and move on.

## Pending — local refs awaiting promotion (D5.44-EP)
| Local ref | Decision, one line | Ruled | Promoted |
|---|---|---|---|
| `cos.2` | **Framework freeze (Q7)** — a lead that thinks a rule is wrong logs the concern in its own `Open questions` and works on under the rule; only the owner reopens it. Scope: `leads/README.md`, `AGENTS.md` §§1–6, `-P`/`-EP` rows. Written to `leads/README.md` §Framework freeze | 2026-09-20 | — |
| `cos.3` | **Minimize (C28)** — manage project bloat at all times, reduce governance overhead, no new governance file without deleting one. Written to `AGENTS.md` §5 | 2026-09-20 | — |
| `cos.4` | **Inter-agent traffic** — Tech owns the mechanism, Chief of Staff the policy. Agents communicate peer to peer; Chief of Staff is an interested party that steers, adjudicates between leads and escalates to the owner, **never a relay or a gate**. Chief of Staff tracks execution — ruled / executing / stalled / who owes the next move — as tracking, not a new queue | 2026-09-21 | — |

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | "status.md is owned by chief of staff. housekeeping may make sense for tech" · "I think of you as chief of staff - organizing the project" | chat 2026-09-20 | DECIDED in chat — D5.29 to log (Tech) |
| — | "outline roles of named agents and propose means to adjudicate for me" → "implement" | chat 2026-09-20 | IMPLEMENTED — `leads/README.md` §Roles, §Adjudication; `STATUS.md` §Decisions |
| **C29** `[cos]` | "I want you to be my quick, what's new what's latest and priority considerations" → mode of Chief of Staff, on demand only | chat 2026-09-20 | IMPLEMENTED — §Standing brief. No D-number; owner may log one. |
| **C30** `[cos]` | on a chat closing line: "this bit is not user friendly" — agent-facing shorthand in a user-facing reply | chat 2026-09-20 | IMPLEMENTED — §Standing brief, closing-line rule. Extends C21/C22. |
| **C31** `[cos]` | on Tech's mechanism/policy split: "correct" · "cos should [handle] interagent traffic, execution, adjudication and escalation" · on execution: "I don't want things running out of control" | chat 2026-09-21 | IMPLEMENTED — §Owns, §For Tech. `cos.4` pending promotion. |

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
0. **Ratify the seven promoted rows** — `D5.45-P`, `D5.46-ES`, `D5.47-AES`, `D5.48-ACPS`, `D5.49-EPS`, `D5.50-CES`, `D5.51-CES` (`leads/systems/tech.md` §For Chief of Staff). Read each row, confirm it states what the owner ruled, write the board rows. Gate: none.
1. **Chase the seven unreferenced rulings** (`STATUS.md` §Pending promotion) — Systems owes five, Tech one, Chief of Staff two. None holds a local ref; each is a `D5.24` in the making. Gate: none.
2. **Q7 freeze → `leads/README.md`** — gated on D5.39, which has landed and verified. Gate: none.
3. **C28 standing rule (minimize) → one line in `AGENTS.md` §5** with the freeze; Tech transcribes. Gate: freeze in force.
4. **Cite the tests in templates** — C26 (vision §1 + `01-pillars` together) and C27 (distilled = against `02-ontology` + `data/SCHEMA.md`, synthesised, no STUB, no MVP OPEN row) in cluster and proposal templates. Gate: none.
5. Refill the queue from Waiting: **coherence clashes C–F first**, then pillar strains, Godot version pin, agent-experience R1–R8. Gate: none; queue is empty.
6. Re-check `00-steer` §1 clause 1 against D5.34/D5.35 (card battler now has a mechanism). Gate: next session.

Handoff: `proposals/2026-09-20-cos-handoff.md`.

## Open questions
1. Queue size 5 — right for hobby cadence? Adjust after two rounds.
2. Does the decisions queue itself survive the three-step chain (D5.42 cl.3), or is it one hop too many? Revisit after one round under the new rule.

## Escalates to
Owner, always.
