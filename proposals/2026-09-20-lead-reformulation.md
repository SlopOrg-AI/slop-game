# Lead reformulation — Chief of Staff, Systems, Direction, Marketing

**Produced by:** Cowork, 2026-09-20, owner in session · **Status:** **PROMOTED D5.29** (2026-09-20) — logged on the owner's "log it"; §6 applied by Tech
**Owner said (verbatim):** *"admin and tech and production seem to run together, systems is good i think … I think of you as chief of staff - organizing the project"* · *"you are most expensive agent with largest context. brief responses in chat are essential. write what will be most helpful to other agents."*

## 1. Clarification: what "Production retired" meant
D5.27 renamed Production → Admin and moved it to Claude Code. Nothing was dropped; the *organizing* job (sequence, milestones, conflicts) and the *custody* job (board, git, housekeeping) were bundled into one role on one surface. The owner's instinct is right: that bundle overlaps Tech (same agent, same repo), and it put the organizing judgement on the surface the owner talks to least.

## 2. Proposed roles (7, was 8)

| Role | Surface | Question it owns | Absorbs |
|---|---|---|---|
| **Chief of Staff** | Cowork | *Is the project organized?* Triage `inbox/` → leads; sequence and milestones (`40-production.md`); conflicts table; cross-lead review; session handoffs; `STATUS.md` content | Production (all) · Admin's triage/board/handoff |
| **Systems** | any | *What is the game?* ontology + rules | unchanged |
| ↳ Content | any | *What's in it?* | unchanged |
| ↳ **Tech** | Claude Code | *What runs it, and is the repo sound?* Godot, validator, tooling, `.claude/`, **git execution**, mechanical housekeeping (tombstones, gitignore, mirror re-sync flags) | Admin's git/tooling/housekeeping |
| **Direction** (art · level · scenario) | any | *What should it be like?* | unchanged |
| **Marketing** | any | *How is it shown?* | unchanged |

Admin ceases to exist as a name. Its judgement half goes to Chief of Staff, its mechanical half to Tech.

## 3. Single-writer rules (kept from D5.27, re-assigned)
- A lead's **brief**: written only by that lead.
- **`STATUS.md`**: written only by Chief of Staff. Rows come from briefs; Chief of Staff transcribes. Tech commits the file but never edits it.
- **Drift guard** (the cause of today's overwrites): Chief of Staff **reads `STATUS.md` from disk in the same session before every write** and never force-writes. Tech's pre-commit hook may later enforce "STATUS.md changed → message starts `Board:`".
- **Git:** Tech executes; owner may; nobody else. Stage by path, never `git add -A`.

## 4. Cost tiers — who does what kind of work
| Surface | Cost | Use for | Don't use for |
|---|---|---|---|
| Cowork (Chief of Staff) | highest — largest context | organizing, judgement, cross-lead review, owner conversation | reading whole docs, distillation, bulk edits |
| Claude Code (Tech; also runs any lead on request) | mid | building, repo work, doc distillation with owner present | owner-facing sequencing |
| Codex / ChatGPT | mid | proposals, research, second opinions | anything outside `proposals/` |
| Local LLM (5090) | lowest | batch text, image pipeline | design decisions |

Chief of Staff sessions read **`STATUS.md` + untriaged `inbox/` + the one proposal under discussion** — not the folder. Leads read their briefs; Chief of Staff reads leads' *rows*.

## 5. Chat register for Chief of Staff (extends AGENTS §5 C21/C22)
- Chat replies to the owner: the decision needed, the reason, the file — three to six lines. Detail goes to disk.
- Spell out shorthand or don't use it. "M1" = the first playable duel demo; "C-ref" = a numbered note of something the owner said; "D-number" = a logged decision.

## 6. If promoted (D5.29) — file changes, Tech applies with owner present
1. `leads/admin.md` → `leads/chief-of-staff.md` (this table + §3–§5 as the brief). Tombstone admin.
2. `leads/systems/tech.md`: add git execution + mechanical housekeeping to Owns.
3. `leads/README.md` tree, routing tags (`[admin]` → `[cos]`), triage step 2 → Chief of Staff, cost-tier table (§4).
4. `AGENTS.md` §6 table row; `CLAUDE.md` guard rail 4: "Claude Code is Tech; it commits `STATUS.md` but does not write it."
5. `STATUS.md` header: "Maintained by Chief of Staff (Cowork)". `tools/claude-agents/admin.md` → tombstone (Chief of Staff has no Claude Code pointer by design).
6. `decisions.md`: `Acts on it` value for process rows → `Process` (Systems' call, already on the housekeeping list).

## 7. Alternative, if the owner prefers Claude Code to hold the board
Keep D5.27 as is; rename Admin → Chief of Staff on Claude Code; Cowork becomes an advisor with no file it owns. Cheaper in tokens, but the organizing conversation then happens on a surface the owner uses for building, and Cowork's reviews have nowhere to land except `proposals/`.
