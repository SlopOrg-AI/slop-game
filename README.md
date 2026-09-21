# Shinobi Master v2

Fresh, distilled restart (2026-09-20) of the Shinobi Master design project. The old workspace is frozen; the parts canon cites were **rescued into `sources/v1/`** (D5.40). What stayed behind, and why, is listed in `sources/v1/README.md`.

- Agents and humans: start at `AGENTS.md`.
- Layout:

```
AGENTS.md        canon rules, reading order, per-agent notes
CLAUDE.md        pointer to AGENTS.md
design/          modular living GDD (one doc per system) + decisions.md
data/            game data as JSON (abilities, characters, wounds, conditions)
demo/            Godot 4.x 1v1 duel demo (the MVP)
proposals/       non-canon input from ChatGPT / agents / owner brainstorms
sources/         frozen transcripts; sources/v1/ = the rescued v1 workspace
tools/           hooks (guard rails), the commit sweep, image-gen tooling
```

## Setting up a clone (any machine)

```
git clone <the private remote> && cd <repo>
git config core.hooksPath tools/hooks
cp tools/claude-agents/*.md .claude/agents/ && rm -f .claude/agents/README.md
```

The second line is not optional: it enables the guard rails (D5.39), which are
tracked in `tools/hooks/` precisely so every clone gets the same ones. On Windows
use `copy tools\claude-agents\*.md .claudegents\` for the third.

**What runs where.** The repo, git, the docs, the data and (when it exists) the
Godot demo work on any machine. **Image generation does not:** ComfyUI, the Qwen
weights and the RTX 5090 are on the PC, so `tools/workflows/build_workflows.py`
and `tools/annotate/regional_edit.py` only work there and say so if run
elsewhere. Raw art boards are deliberately not in the repo (D5.28), so a machine
without the PC sees contact sheets and accepted work only.

A successor arriving on a new machine should read
`proposals/2026-09-20-two-machine-migration.md` section 7 before anything else.
