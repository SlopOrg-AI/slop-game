# Shinobi Master v2 — Claude Code entry point

@AGENTS.md

Guard rails Claude Code must hold in every session (short form of AGENTS.md §1, §6):

- Disk is canon. `design/decisions.md` arbitrates; no D-number = not decided. Never log a D-number or self-attribute a decision to the owner without an explicit instruction in this session.
- Write freely only in `proposals/` and `inbox/`. `design/`, `data/`, `demo/` change only on owner instruction in-session. `sources/` is read-only evidence.
- Do not expand the MVP (`design/00-steer.md` §4). Do not create the Godot project until the gate in `demo/README.md` clears.
- Work as a lead: `leads/README.md` → `leads/<lead>.md`. Subagent pointers: `.claude/agents/` (seed from `tools/claude-agents/`). End every session by updating the lead brief and `STATUS.md`.
- Commit small; message = what changed + D-numbers. Owner runs git.
