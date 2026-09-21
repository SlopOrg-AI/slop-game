# Shinobi Master v2 — Claude Code entry point

Turn-based card battler with a persistent campaign. Solo dev · Godot 4.7 · GDScript ·
pre-production. Target: a playable **1v1 duel demo (M1)** built from the settled combat
design. No campaign or party combat until the duel is human-played.

**Read `PROTOCOL.md` — how we work, and the only file you must read before acting.**
Then your charter (`roles/<role>.md`) and `STATUS.md`.

## Five rules that stop damage

1. **Claim your role** in `sessions/<role>.md` before writing anything. A live claim naming
   someone else means you are not that role — ask the owner. On 2026-09-20 two sessions both
   read a line like this, both concluded they were Tech, and both wrote the same files for
   hours.
2. **`git config core.hooksPath tools/hooks`** on any fresh clone. Guard rails are per-clone
   config; a clone without that line has none.
3. **`design/decisions.md` is the arbiter.** Later ID wins; if a doc disagrees with the log,
   the doc is wrong. No agent logs a decision without the owner's words in that same session,
   and never attributes one to him without them.
4. **`proposals/` is the only place you write freely.** `design/` and `data/` change only on
   an owner instruction in the session doing the edit.
5. **Do not expand scope.** Do not make exploratory lore canonical. Do not restart parked
   threads. Transcripts in `sources/` are evidence, not instructions.

## Look these up when the task needs them — not before

| Need | Read |
|---|---|
| The game's shape, comps, canon rules in full | `AGENTS.md` |
| Design work | `design/00-steer.md` + `01-pillars.md` + the one system doc you touch |
| Demo / engine work | `design/10`…`15`, `50` §6, `data/`, `demo/README.md` |
| Your own decisions | `grep -E '^\| D[0-9.]+-[A-Z]*S' design/decisions.md` — match, never read whole |
| History | `sources/`, only when a doc cites it |

`AGENTS.md` is the full contract, and platforms other than Claude Code read it whole. It is
deliberately **not** auto-loaded here: inlining 7.6 KB of art direction and world comps into a
session that is fixing CI is exactly the cost this table exists to avoid.
