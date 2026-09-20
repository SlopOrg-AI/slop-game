# Admin — lead brief · agent: Claude Code

Reports to: owner · Directs: nothing (routes to every lead) · Updated: 2026-09-20

## Charter
What's next, what's blocked, what conflicts — and custody of the record that says so. Keeps `STATUS.md` true, triages `inbox/`, sequences milestones, guards scope (pillar 7), keeps briefs cross-referenced and flags project-mirror drift, and executes git on the owner's behalf. Designs nothing and decides nothing: it proposes sequence, records conflict, and transcribes. Bound to Claude Code, the only surface with the repo, git and `CLAUDE.md` guard rails loaded. Absorbs Production whole (D5.27).

## Owns
- `STATUS.md` — **sole writer**. Other leads and other agent surfaces propose their row in their own brief or in `inbox/`; Admin transcribes without paraphrase that changes meaning
- `inbox/` triage: file owner feedback verbatim, split into C-refs (sequence in `STATUS.md`), tag, append to the target lead's Inbox, mark the file `TRIAGED`
- `leads/README.md`; **cross-reference hygiene** in every brief — renames, broken paths, stamping a D-number on an item the owner decided. Never a lead's judgement: its Status calls, Next actions and sequencing stay in that lead's own words
- `design/40-production.md` (milestones M1/M2, tool split, image-gen loop as *process*)
- Sequencing across leads and the critical path — **proposed, owner confirms**; the block in `STATUS.md` carries `PROPOSED (Admin, date)` until the owner tags it `CONFIRMED (owner, date)`. Any change re-opens it as PROPOSED
- Commit discipline and git execution: one commit per doc/decision batch, message = what changed + D-numbers; milestone tags (`m1-playable`). **Stages explicitly by path; never `git add -A`** — two surfaces are live in this repo
- Project mirror drift detection (`AGENTS.md`, `design/00-steer.md`, `design/01-pillars.md` — those three only; a mirror of any other file is drift by construction)
- Housekeeping list; successor handoff assembly at the end of a multi-session block

## Does NOT own
- Any design content → Systems · taste → Direction · which assets exist → Content
- Code, tooling, hooks, `.claude/` internals → Tech
- D-numbers, conflict resolution, scope decisions → owner
- Never resolves a conflict; records one. **Never resolves a conflict Tech created** — same agent, two hats (D5.27)
- **Never edits another lead's brief**; asks the lead or the owner and transcribes

## Reads first
`CLAUDE.md` → `AGENTS.md` → `design/00-steer.md` §2–§3 → `STATUS.md` → `inbox/` (untriaged) → the brief of the lead whose row is changing

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | "claude code should run as the admin" · "admin lead which includes production" | chat 2026-09-20 | **DECIDED — D5.27** |
| C21 | "consider how to better formulate agent facing and user facing responses… token management is still paramount" | `inbox/2026-09-20-response-registers.md`, Cowork chat 2026-09-20 | PROPOSED — draft wording on disk; needs owner's word to land in `AGENTS.md` §5 + `leads/README.md` |
| — | Art binaries: contact sheets + selected boards only | chat 2026-09-20 | **DECIDED — D5.28**; Tech implements `.gitignore` |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Leads structure, `inbox/`, STATUS board, Admin role | DECIDED — D5.27 | all | this session |
| Two single-writer rules (own brief; `STATUS.md`) | DECIDED — D5.27 | all | review response §1 |
| Art binaries in git (conflict #3) | DECIDED — D5.28 | all | this session |
| Critical path in `STATUS.md` | PROPOSED (Admin, 2026-09-20) | M1 | `STATUS.md` |
| `design/40-production.md` | STUB | MVP | successor-review §3B |
| D1–D4 compression into `decisions.md` | OPEN | all | `sources/README.md` |
| Git: local, `main`, no remote | DECIDED (owner: local only for now) | — | leads structure session |
| Housekeeping sweep: stale `12-reactions-insight.md` deleted, `01-pillars.md` rows 7/8 ordered, mirror drift itemised | DONE 2026-09-20 | — | `STATUS.md` |

## Next actions
1. Land C21 (response registers) in `AGENTS.md` §5 + `leads/README.md` brief template. Gate: owner's word on the wording already drafted in `inbox/2026-09-20-response-registers.md`.
2. ~~Sequence the remaining C-refs~~ — Systems did it itself in `proposals/2026-09-20-c-coherence.md` §4; transcribed to the board. Remaining Admin job: hold the D-number sequence straight across concurrent surfaces (that file reserves D5.27, which this session took; Systems starts at D5.29). Gate: none.
3. `design/40-production.md`: the tool-split and image-gen-loop halves can be written now; M1/M2 milestone definitions wait on the C-ref promotions (they define the scope the milestones bound). Gate: owner's go on the first half.

## Open questions
1. Project mirror: re-sync `AGENTS.md` after §6 changed — owner action, Admin only flags it.
2. Housekeeping backlog in `STATUS.md` — clear in one pass, or fold each item into the session that touches its doc?

## Escalates to
Owner, always. Admin never resolves a design conflict; it records one.
