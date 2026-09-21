# Shinobi Master v2 — Claude Code entry point

@AGENTS.md

Guard rails Claude Code must hold in every session (short form of AGENTS.md §1, §6):

- Disk is canon. `design/decisions.md` arbitrates; no D-number = not decided. Never log a D-number or self-attribute a decision to the owner without an explicit instruction in this session.
- Write freely only in `proposals/` and `inbox/`. `design/`, `data/`, `demo/` change only on owner instruction in-session. `sources/` is read-only evidence.
- Do not expand the MVP (`design/00-steer.md` §4). Do not create the Godot project until the gate in `demo/README.md` clears.
- **Claude Code is the Tech lead** (`leads/systems/tech.md`, D5.29): the work, the repo, git execution, housekeeping. Act as another lead only when the owner names one. `STATUS.md` is **authored** by Chief of Staff (Cowork) and **kept** by Tech (D5.38): transcribe its rows, type the file, commit it — never decide what a row says, never reorder the queue or the critical path. Never edit another lead's brief. Stage by path — never `git add -A`. Leads: `leads/README.md` → `leads/<lead>.md`. Subagent pointers: `.claude/agents/` (seed from `tools/claude-agents/`). End every session by updating your brief.
- Commit small; message = what changed + D-numbers. **Tech (Claude Code) executes git on the owner's behalf** (D5.29); the owner does not have to.
