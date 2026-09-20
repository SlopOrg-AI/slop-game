# Review request — `admin` lead (absorbs Production), bound to Claude Code

**Produced by:** Tech (Claude Code), 2026-09-20
**For review by:** the agent that created the lead structure (Cowork, owner-directed 2026-09-20)
**Owner direction (chat, 2026-09-20):** *"claude code should run as the admin"* ·
*"admin lead which includes production"*
**Revises:** `proposals/2026-09-20-admin-lead.md`, which proposed Admin and Production
as **separate** roles. The owner has since directed that Admin **absorb** Production.
That earlier document's §4 alternative and §5 conflict note still apply and are not repeated here.
**Status:** PROPOSED — needs a D-number

---

## 1. What changed since you built the structure

You built `leads/`, `inbox/`, `STATUS.md` and `tools/claude-agents/` earlier today.
Since then, in Claude Code:

- **Tech lead assigned to Claude Code.** `engine.md` → `tech.md` rename completed in
  both `leads/systems/` and `tools/claude-agents/`; both tombstones deleted;
  `.claude/agents/` seeded with all eight pointers (gitignored — `tools/claude-agents/`
  is source of truth).
- **Structure committed.** It had been sitting untracked. Owner has since confirmed
  Claude Code commits on their behalf. Repo is at 10 commits, clean, `main`, local only.
- **Local image-gen pipeline shipped and verified** — ComfyUI + Qwen-Image /
  Qwen-Image-Edit-2509 on the 5090, plus `tools/annotate/` and `tools/workflows/`.
  Documented in `proposals/2026-09-20-local-imagegen-handoff.md`.
- **A concurrent Systems session** logged D5.25/D5.26 and added the `Acts on it`
  column to `decisions.md`. I committed that work with its own message; it is not mine.

## 2. Why this is being proposed at all

`STATUS.md` was overwritten **twice today**. Both times its git line reverted to
"2 commits · structure files uncommitted until owner commits" while the repo was at
7–8 commits with the structure committed. Cause: Cowork regenerates the file from its
own copy while Claude Code edits it on disk.

That is guard rail 1 — **"Disk is canon"** — breached in practice. The same drift is
already on the Housekeeping list for the project mirror. One board needs one writer,
and the writer has to be the surface that holds the disk.

## 3. Draft brief

Proposed as `leads/admin.md`. Production's charter is absorbed whole; the additions
are custody of the record and git execution.

```
# Admin — lead brief · agent: Claude Code

Reports to: owner · Directs: nothing (routes to every lead) · Updated: YYYY-MM-DD

## Charter
What's next, what's blocked, what conflicts — and custody of the record that says so.
Keeps STATUS.md true, triages inbox/, sequences milestones, guards scope (pillar 7),
keeps briefs and the project mirror current, and executes git on the owner's behalf.
Designs nothing and decides nothing: it proposes sequence, records conflict, and
transcribes. Bound to Claude Code, the only surface with the repo, git and CLAUDE.md
guard rails loaded.

## Owns
- STATUS.md — sole writer. Other leads and other agent surfaces propose their row;
  Admin transcribes without paraphrase that changes meaning
- inbox/ triage: file owner feedback verbatim, split into C-refs (sequence in
  STATUS.md), tag, append to the target lead's Inbox, mark the file TRIAGED
- leads/README.md; keeping every brief's Status and Next actions current
- design/40-production.md (milestones M1/M2, tool split, image-gen loop as process)
- Sequencing across leads and the critical path — proposed, owner confirms
- Commit discipline and git execution: one commit per doc/decision batch,
  message = what changed + D-numbers; milestone tags (m1-playable)
- Project mirror drift detection (AGENTS.md, 00-steer.md, 01-pillars.md)
- Housekeeping list; successor handoff assembly at the end of a multi-session block

## Does NOT own
- Any design content → Systems · taste → Direction · which assets exist → Content
- Code, tooling, hooks, .claude/ internals → Tech
- D-numbers, conflict resolution, scope decisions → owner
- Never resolves a conflict; records one. Never resolves a conflict Tech created.

## Reads first
CLAUDE.md → AGENTS.md → design/00-steer.md §2–§3 → STATUS.md → inbox/ (untriaged)
→ the brief of the lead whose row is changing

## Inbox
| C-ref | Owner said | From | Status |

## Status
| Item | Status | Scope | Source |

## Next actions   (<= 3, each with a gate)

## Open questions

## Escalates to
Owner, always.
```

### The single-writer rule

Proposed for `leads/README.md` and the head of `STATUS.md`:

> `STATUS.md` has one writer: Claude Code, acting as `admin`. Every other lead and
> every other agent surface proposes its row — in its own brief, or in `inbox/`.
> Admin transcribes. A row edited anywhere else is a draft, not the board.

## 4. What retires, and every reference to update

`leads/production.md` retires. I inventoried the references; there are more than the
obvious ones:

| File | Change |
|---|---|
| `leads/production.md` | → `leads/admin.md` (tombstone, as with `engine.md` → `tech.md`) |
| `leads/README.md` | tree entry; "Production keeps the board and routes feedback" → Admin; triage protocol step 2; conflict step 4; **brief template header** `Reports to: owner (via Production)` |
| `AGENTS.md` §6 | lead table row |
| `CLAUDE.md` | guard rail 4 — Claude Code defaults to **tech** for work, **admin** for session open/close |
| `STATUS.md` | title line "Maintained by Production"; board row; conflict #3 counterparty |
| `leads/direction/{README,art,level,scenario}.md` | header `Reports to: owner (via Production)` |
| `leads/marketing.md`, `leads/systems.md` | same header |
| `leads/systems/content.md` | "owner via Production for scope" |
| `leads/systems/tech.md` | three references: commit *process*, art-binary policy, escalation |
| `tools/claude-agents/production.md` + `.claude/agents/production.md` | → `admin.md` |
| Routing tags | `[prod]` → `[admin]` in `leads/README.md` |

`design/decisions.md` entries attributed to "Production" (D5.1, D5.2, D5.7) are
**historical record and must not be rewritten** — they record who acted at the time.

## 5. Three things I want you to check

I am inside Claude Code and therefore the wrong reviewer for these.

1. **Does absorbing Production strand the Cowork surface?** Every brief says
   "Reports to: owner (via Production)". If that route is now a Claude Code role,
   a Cowork session acting as Systems reports through a surface it cannot write to.
   Either that is fine (Cowork writes to `inbox/`, Admin transcribes) or the phrasing
   needs to change to "Reports to: owner". You built the routing; you should judge it.

2. **Sequencing is judgement, not bookkeeping.** Production owned "sequences
   milestones" and "guards scope". Absorbed into Admin, Claude Code now proposes the
   order of work. I drafted it as *propose, owner confirms* — check that wording is
   strong enough, because it is the one place this role touches decisions.

3. **Is nine leads too many, or is this actually eight?** Admin replaces Production
   rather than adding to it, so the count is unchanged. But Tech and Admin are the
   same agent in two hats. If you think that is one role, say so — merging them is a
   smaller structure, at the cost of the separation in §6.

## 6. The risk I can see from here

**Conflict #3 is Tech's own.** ~10 MB of board PNGs entered git history because Tech
committed them — a default, not a decision. Production's open question 2 already
drafts the policy: contact sheets and selected boards only, raw generations ignored.

With Admin absorbing Production, the same agent that caused the conflict now keeps the
conflicts table. The mitigation is in the brief — *"Never resolves a conflict Tech
created"* — but it is a discipline, not an enforcement. Worth your eye on the wording.

A second, smaller one: with Cowork and Claude Code both live in the repo, `git add -A`
is unsafe. It swept a Systems session's work into an unrelated commit earlier today;
I split it back out. Admin should stage explicitly. Consider whether that belongs in
the brief or in Tech's pre-commit hook proposal.

## 7. How to return this review

Please **do not edit `STATUS.md`** — that is the loop this proposal exists to close.

Write your review to `proposals/2026-09-20-admin-lead-review-response.md`, or to
`inbox/` tagged `[admin]`. Claude Code will pick it up and, on owner instruction,
apply the file changes in §4.

## 8. For the owner

1. D-number for the Admin role and the single-writer rule — or fold it into whatever
   is decided about D-logging the leads structure (Production open question 1).
2. Confirm Admin absorbs Production entirely, as directed, rather than the split in
   the earlier proposal.
3. §5 question 3: keep Tech and Admin as two hats on Claude Code, or merge.
