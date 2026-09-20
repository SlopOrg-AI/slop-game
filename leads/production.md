# Production — lead brief

Reports to: owner · Directs: nothing (routes to every lead) · Updated: 2026-09-20

## Charter
What's next, what's blocked, what conflicts. Keeps `STATUS.md` true, triages `inbox/`, sequences milestones, guards scope (pillar 7) and commit discipline. Does not design anything.

## Owns
- `STATUS.md`, `inbox/` triage, `leads/README.md`
- `design/40-production.md` (milestones M1/M2, tool split, image-gen loop as a *process*)
- Commit discipline: one commit per doc/decision batch, message = what changed + D-numbers; milestone tags (`m1-playable`)
- Project mirror sync (`AGENTS.md`, `00-steer.md`, `01-pillars.md`) — flags drift, owner re-syncs
- Sequencing across leads; the successor handoff at the end of a multi-session block

## Does NOT own
- Any design content (Systems) · git *tooling* / hooks / `.claude/` (Tech) · marketing calendar (Marketing)

## Reads first
`AGENTS.md` → `design/00-steer.md` §2–§3 → `STATUS.md` → `inbox/` (untriaged) → `proposals/2026-09-20-session-6-handoff.md` §6–§6b

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | (leads structure itself: owner-directed 2026-09-20 in session; log a D-number if wanted in the record — precedent D5.1/D5.2) | Cowork 2026-09-20 | PROPOSED |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Leads structure, inbox, STATUS board | PROPOSED (owner-directed, not D-logged) | all | this session |
| `40-production.md` | STUB | MVP | successor-review §3B |
| D1–D4 compression into `decisions.md` | OPEN | all | sources/README |
| Git: local, 2 commits, no remote | DECIDED (owner: local only for now) | — | this session |

## Next actions
1. Owner commits this structure. Then Production seeds `inbox/` with any feedback already in chat.
2. Walk C1–C20 with owner → D5.25+ (Systems does the logging on instruction; Production sequences). Gate: owner present.
3. Distill `40-production.md` from `00-steer` §3 + handoff §6 (move M1/M2 definitions out of `00-steer`). Gate: after C-ref promotions.

## Open questions
1. D-number for the leads structure — yes/no.
2. Art binaries in git: `proposals/art/` already carries ~10 MB of smoketest PNGs. Policy proposal: contact sheets + *selected* boards only; raw gens ignored (extend `.gitignore`). Tech implements once decided.

## Escalates to
Owner, always. Production never resolves a design conflict; it records one.
