# Proposal — `admin` lead, bound to Claude Code

**Produced by:** Tech (Claude Code), 2026-09-20, on owner instruction in session
**Targets:** `leads/README.md`, `leads/production.md`, `AGENTS.md` §6, `CLAUDE.md`
**Proposes:** a custodial `admin` role, bound to Claude Code, that becomes the sole
writer of `STATUS.md` and the keeper of repo hygiene
**Would supersede:** Production's ownership of `STATUS.md`, `inbox/` triage mechanics
and `leads/README.md` (sequencing and scope judgement stay with Production)
**Status:** PROPOSED — needs a D-number

---

## 1. The problem, with evidence

`STATUS.md` has been overwritten **twice** in one day. Both times the git line
reverted to "2 commits · structure files uncommitted until owner commits" while
the repo was at 7–8 commits with the structure committed. Cause: Cowork
regenerates the file from its own copy; Claude Code edits it on disk.

That is a direct breach of guard rail 1, **"Disk is canon."** A board with two
writers is not a board — it is two drafts, and the reader cannot tell which is
true. The same drift is already logged for the project mirror
(`AGENTS.md`, `00-steer.md`, `01-pillars.md`) in Production's Housekeeping list.

The structure already solves this shape of problem for Tech work.
`leads/systems/tech.md` states that Cowork, Codex, ChatGPT and the local model
"write a task to `proposals/` or `inbox/` tagged `[tech]` and Claude Code picks
it up." Applying the same rule to the board is one consistent step, not a new
principle.

## 2. What is proposed

An **`admin`** role, bound to Claude Code, holding the *mechanical custody* of the
project record. It is a custodian, not a decision-maker: it transcribes, files,
routes and commits. It never decides what is next, never resolves a conflict and
never logs a D-number.

Crucially this is a **transfer, not a duplication**. Production keeps judgement;
Admin takes the artefacts. Creating Admin *alongside* Production's existing
ownership of `STATUS.md` would reproduce the exact two-writer bug being fixed.

### Splits from Production

| Moves to Admin | Stays with Production |
|---|---|
| `STATUS.md` — **sole writer** | Sequencing across leads; the critical path |
| `inbox/` triage *mechanics* (file verbatim, split into C-refs, tag, route) | Which C-refs are worked, and in what order |
| `leads/README.md`; keeping briefs current | `design/40-production.md` (milestones, tool split) |
| Housekeeping list; mirror **drift detection** | Scope guard (pillar 7); commit *discipline* as policy |
| Git execution; successor handoff assembly | Recording conflicts for the owner to resolve |

### Unchanged

`AGENTS.md` §1 stands in full. Admin never logs a D-number, never self-attributes
a decision to the owner, and writes to `proposals/` unless the owner is in session.
The owner remains the sole decision-maker on D-numbers, conflicts, milestone order
and scope.

## 3. The single-writer rule

Proposed wording for `leads/README.md` and the head of `STATUS.md`:

> `STATUS.md` has one writer: Claude Code, acting as `admin`. Every other lead and
> every other agent surface proposes its row — in its own brief, or in `inbox/`.
> Admin transcribes, without paraphrase that changes meaning. A row edited
> anywhere else is a draft, not the board.

This is what makes the fix structural rather than a convention someone remembers.

## 4. Why not simply bind Production to Claude Code

Considered, and rejected. Production is already scoped as non-deciding
("never resolves a design conflict; it records one"), so binding it to Claude Code
would grant no new authority and would need no new role.

Two reasons against it:

1. **It strands Cowork.** The owner works through chat and Cowork as well as Claude
   Code. Production is the natural surface for owner-facing sequencing
   conversations. Making it Claude Code-only pushes that work somewhere undefined.
2. **It leaves the single-writer rule implicit.** The two-writer bug happened
   precisely because ownership was stated but not bound to a surface. A role whose
   defining property *is* the binding makes the rule enforceable.

If the owner prefers fewer roles, binding Production to Claude Code and adding the
single-writer rule to it achieves most of the benefit. It is the smaller change and
a reasonable alternative.

## 5. Separation of concerns — a live example

**Conflict #3 is Tech's own.** Roughly 10 MB of board PNGs entered git history
because Tech committed them; that was a default, not a decision.

Tech and Admin are the same agent wearing different hats, so the separation is a
discipline rather than a wall. The discipline that matters: Admin **records** the
conflict and Production proposes policy; Tech **implements** whatever the owner
decides. Admin must not quietly close a conflict that Tech created. Production's
open question 2 already drafts the policy — contact sheets and selected boards
only, raw generations ignored — and that is the right shape.

## 6. Draft brief

Ready to drop into `leads/admin.md` if promoted.

```
# Admin — lead brief · agent: Claude Code

Reports to: owner · Directs: nothing (serves every lead) · Updated: YYYY-MM-DD

## Charter
Custody of the project record. Keeps STATUS.md true, triages inbox/ into C-refs,
keeps briefs and leads/README.md current, detects mirror drift, executes git, and
assembles the successor handoff. Decides nothing: transcribes, files, routes,
commits. Bound to Claude Code — the only surface with the repo, git and CLAUDE.md
guard rails loaded.

## Owns
- STATUS.md — sole writer; other leads propose rows, Admin transcribes
- inbox/ triage mechanics: file owner feedback verbatim, split into C-refs
  (continuing the sequence in STATUS.md), tag, append to the target lead's Inbox
- leads/README.md; keeping every brief's Status/Next actions current
- Housekeeping list; mirror drift detection (AGENTS.md, 00-steer.md, 01-pillars.md)
- Git execution on the owner's behalf; commit messages = what changed + D-numbers
- Successor handoff assembly at the end of a multi-session block

## Does NOT own
- What is next, or in what order → Production · any design content → Systems
- Resolving conflicts, D-numbers, scope → owner · code and tooling → Tech
- Taste → Direction

## Reads first
CLAUDE.md → AGENTS.md → STATUS.md → inbox/ (untriaged) → the brief of the lead
whose row is changing

## Inbox
| C-ref | Owner said | From | Status |

## Status
| Item | Status | Scope | Source |

## Next actions   (<= 3, each with a gate)

## Open questions

## Escalates to
Owner, always. Admin never resolves; it records and routes.
```

## 7. Implementation if promoted

1. `leads/admin.md` from the draft above.
2. `leads/production.md` — remove `STATUS.md`, `inbox/` triage and
   `leads/README.md` from **Owns**; add "board maintained by Admin" to Charter.
3. `leads/README.md` — add Admin to the tree and the single-writer rule (§3).
4. `AGENTS.md` §6 — add the Admin row to the lead table.
5. `CLAUDE.md` — amend the fourth guard rail: Claude Code defaults to **tech** for
   work and **admin** for session open/close.
6. `tools/claude-agents/admin.md` pointer, copied to `.claude/agents/`.
7. `STATUS.md` — add the single-writer line under the title; add an Admin row.

Steps 2–5 and 7 touch files outside `proposals/`, so they need the owner in session.

## 8. Risks

- **Role inflation.** Nine leads for a one-person project is a lot. Mitigated by
  Admin owning no discipline and producing no design output — it is a scribe.
- **Same agent, two hats.** Tech and Admin are both Claude Code, so the separation
  is discipline, not enforcement. §5 names the specific failure to watch.
- **Bookkeeping crowding out work.** If a session spends more time on the board
  than on the task, the role is miscalibrated. Admin work belongs at session open
  and close, not throughout.

## 9. What promotion needs

A D-number for the role and the single-writer rule, plus a decision on §4 —
distinct `admin` role, or bind Production to Claude Code instead.

Production's open question 1 ("D-number for the leads structure — yes/no") is
still open; if the structure itself is not being D-logged, this should follow the
same treatment rather than being logged alone.
