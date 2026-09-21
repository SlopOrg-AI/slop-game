# Proposal — agent-experience review (fresh-agent read of the repo)

**Produced by:** Cowork session, 2026-09-20, owner-requested — no lead hat. **Targets:** `AGENTS.md`, `leads/`, `design/40-production.md`, `tools/`, `STATUS.md` housekeeping. **Proposes:** eight fixes, seven mechanical, one owner pick already pending. **Supersedes:** nothing. **Status:** `PROPOSED`.

Method: read as a new agent would — `CLAUDE.md` → `AGENTS.md` → `00-steer` → every lead brief → folder READMEs → `decisions.md` → git log; then two integrity scans (backticked paths vs disk; every `D#.#` cited vs the log).

---

## 1. Verdict

The structure is better than most production repos. A cold agent can find the canon, learn what it may write, and know who decides — in about 20 KB of reading. The risks are not structural; they are **decay and non-enforcement**. Five of the ten findings below are the same failure: a rule that exists only as prose, in a repo that renamed two roles and deleted three files in one day.

Do not add process. Every fix below is a script, a sweep, or an owner one-liner already written.

## 2. Working — keep as is

| # | What | Why it matters to an agent |
|---|---|---|
| 1 | One entry point, enforced reading order, "do not load every doc" (`AGENTS.md` §2) | The single biggest driver of agent quality. Most repos have no answer to "what do I read?" |
| 2 | `decisions.md` as arbiter; later D wins; **doc-vs-log conflict resolves to the log** (rule 2) | A falsifiable conflict rule. An agent can resolve a contradiction without asking |
| 3 | Write permissions stated per folder *and* per surface (rules 5, 7; `AGENTS.md` §4) | Removes the most common agent failure: helpful edits to files it shouldn't touch |
| 4 | Rule 4 — never self-attribute a decision to the owner | Directly targets the confabulation mode that ruins design repos |
| 5 | `Acts on it` column in `decisions.md` | Makes a 29 KB log skimmable by role. Unusual and correct |
| 6 | Briefs carry **Does NOT own** and **Escalates to** | The half of role definition everyone omits, and the half that prevents scope creep |
| 7 | `data/README.md` "Known drift" + "migration is not a silent edit" | Pre-empts an agent tidying six fields and breaking the schema-v3 plan |
| 8 | Two registers (C21/C22), `.gitattributes` LF pin, `tools/workflows/build_workflows.py` as generator-not-artifact | Three quiet decisions that each remove a recurring class of noise |

## 3. Friction — ranked by cost to a fresh agent

| # | Finding | Evidence | Cost |
|---|---|---|---|
| **F1** | **Retired-role residue contradicts a logged decision.** `Admin` was retired by D5.29; `STATUS.md` custody was split by D5.38 | `40-production.md` §1 tool-split row and **§3 record-discipline row ("`STATUS.md` has one writer: Admin")** — a *rule statement* now wrong · `inbox/README.md` triage protocol · `tools/claude-agents/README.md` ("two hats: admin… tech") · `leads/marketing.md`, `leads/systems.md`, `leads/systems/content.md` Does-NOT-own rows | An agent reading `40-production` §3 follows a superseded rule and is *correct* to, until it reaches the log. Rule 2 says fix the doc; nothing finds it |
| **F2** | **`design/` is mostly stubs; canon lives in `decisions.md` + `proposals/`** | `10`, `13`, `20`, `21`, `30`, `31` are ~300 B. `00-steer` §5 doc map promises content that isn't on disk; `02-ontology.md` is cited by `decisions.md` rows and is absent from the map | "Read the one system doc you're touching" yields 336 bytes. The agent then reconstructs the rule from a 29 KB log and a 26 KB proposal — the exact cost the reading order was built to avoid |
| **F3** | **Guard rails proposed, nothing installed** | `proposals/2026-09-20-guard-rails.md` §6 — four hooks + two permission rules, backed by four incidents from one day. `.claude/settings.json` does not exist; `tools/hooks/` does not exist | Nothing but discipline stops an agent editing `sources/**` or `decisions.md`. Two of the four logged incidents are ones a fresh agent repeats by default |
| **F4** | **Board lags reality by a session** (author/keeper split, D5.38) | `STATUS.md` Housekeeping still lists the three `admin.md` tombstones; `leads/systems/tech.md` §For Chief of Staff says all three are deleted and asks for the strike | The board is what every agent reads first for "what's next". D5.38 is the right rule; it needs a reconciliation *step*, not just a channel |
| **F5** | **`.claude/agents/` is gitignored and hand-copied** | `.gitignore` last block; `tools/claude-agents/README.md` copy command. 7 pointer files, no `chief-of-staff` (correct — Cowork-only), but `leads/systems/tech.md` says "8 leads copied in" | A new clone — **the Mac** — has no subagents until the owner runs a copy. Drift between the two folders is silent. The files are 700 B pointers with no secrets; there is no reason to ignore them |
| **F6** | **No reference-integrity check** | Scan found `D5.24` cited as canon in **6 files** — `00-steer` §6, `11-initiative.md` (status table asserts DECIDED), `14-scenes-conditions.md`, `STATUS.md`, `leads/systems.md`, `leads/direction/level.md` — and absent from the log. Also dangling: `12-reactions-insight.md`, `02-art-direction.md`, three `admin.md` paths | Already tracked as conflict #1, but it was found by a human. After `engine`→`tech`, `admin` retired, one doc deleted and one renumbered, the next dangling path costs an agent a fabricated section |
| **F7** | **Two proposals are load-bearing required reading** | `leads/systems.md` and `leads/systems/tech.md` both list `…-session-6-handoff.md` (26 KB) under Reads first; `…-ontology-draft.md` likewise. `proposals/` is defined as non-canon | A non-canon file that every session must read is a second canon, exempt from rule 2 |
| **F8** | **No `SCHEMA.md`, no validator; `data/` carries six documented drifts** | `data/README.md`; `data/validate.py` "to write"; schema v3 gates Godot, the validator, and Content's next board | The single largest unblock in the repo. Correctly sequenced — worth naming as *the* critical path item rather than one row of it |
| **F9** | **One disk, no remote, canon cites PC-only files** | `leads/systems/tech.md` §Machines — "Blocking: no git remote exists"; "Deadline: the text behind D1–D4 and the v1 bible live only on the PC disk and are cited by canon" | Survivable for the game; fatal for agent experience if the Mac holds the only clone — the Project mirror is 3 files of ~40, so a Chief of Staff without disk access is blind |
| **F10** | **A gate no agent can evaluate** | `demo/README.md` gate = "`00-steer` and the 10–14 system docs marked distilled"; `40-production.md` open #3 says "distilled" is undefined. `AGENTS.md` §2 says 10–**15** | Every "may I start Godot?" question is unanswerable by rule, so it escalates |

## 4. Recommendations

| # | Do | Who | Cost |
|---|---|---|---|
| **R1** | **Answer `guard-rails` §6.** Tech's read (all four checks + both permission rules) is the right default; A and B have same-day evidence | owner | one line |
| **R2** | `tools/check_refs.py` — resolve every backticked path, every `D#.#` against the log, and flag retired lead names. Wire into `pre-commit` beside checks A–D | Tech | ~30 lines; catches F1, F6, and the next rename |
| **R3** | Un-ignore `.claude/agents/`; delete the copy step and `tools/claude-agents/`. Fix the 8-vs-7 count | Tech | 10 min; closes F5 |
| **R4** | Sweep the retired-role residue listed in F1. `40-production` §3 is the urgent one — it states a rule D5.38 superseded | Tech (mechanical housekeeping, D5.29) | 20 min |
| **R5** | **Define "distilled"** — no STUB marker, or no OPEN rows at MVP scope. It gates Godot, so it is not a Production footnote | Systems, via the queue | one queue item |
| **R6** | Add to session close: Tech's §For Chief of Staff is read and struck by Chief of Staff before the next board write | Chief of Staff | a line in `leads/README.md` §Running a lead session |
| **R7** | Distil `session-6-handoff` and `ontology-draft` into `02-ontology.md` when it is written, then drop both from every Reads-first list | Systems | rides with F8 |
| **R8** | Git remote (private) **before** the Mac move; rescue the PC-only text cited by D1–D4 in the same session | owner + Tech | `…-two-machine-migration.md` §1–§2 |

## 5. What not to do

- **Do not add rules.** The process-to-content ratio is already high for a solo hobby project: `leads/` + `STATUS.md` + `AGENTS.md` ≈ 45 KB of governance over ~35 KB of written design, six of twelve system docs still stubs. Every finding above is decay or non-enforcement of a rule that already exists.
- **Do not fix `data/` piecemeal.** `data/README.md` is right; leave the six drifts until schema v3.
- **Do not let the queue grow past five.** It is the one place the owner is the bottleneck, and it is currently well-shaped.
