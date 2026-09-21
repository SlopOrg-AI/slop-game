# Shinobi Master v2 — Claude Code entry point

@AGENTS.md

**Read `PROTOCOL.md` first — it is how we work, in two pages.** Roles, the session contract, the git rule, the decision rule, the budgets, and §Changes: everything about the way we work that changed since your last session.

Three things it says that matter before you touch anything:

- **Claim your role** (`sessions/`). If your role names a live session that is not you, you are not it — ask the owner. On 2026-09-20 two sessions both read a line like this one, both concluded they were Tech, and both wrote the same files for hours.
- **`git config core.hooksPath tools/hooks`** on any fresh clone. Guard rails are per-clone config; a clone without that line has none.
- **`design/decisions.md` is the arbiter.** No agent logs a decision without the owner's words in the same session.

`AGENTS.md` carries the project's canon rules and the game's shape. This file adds nothing to either.
