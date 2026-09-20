# Shinobi Master v2

Fresh, distilled restart (2026-09-20) of the Shinobi Master design project. The old workspace (`C:\Claude`, `docs/`, wireframes, archived Godot port) is frozen and referenced from `sources/`.

- Agents and humans: start at `AGENTS.md`.
- Layout:

```
AGENTS.md        canon rules, reading order, per-agent notes
CLAUDE.md        pointer to AGENTS.md
design/          modular living GDD (one doc per system) + decisions.md
data/            game data as JSON (abilities, characters, wounds, conditions)
demo/            Godot 4.x 1v1 duel demo (the MVP)
proposals/       non-canon input from ChatGPT / agents / owner brainstorms
sources/         frozen transcripts + pointers to the old workspace
```

## First-time setup (owner, once)

```
cd C:\Claude\shinobi-v2
git init
git add .
git commit -m "v2 skeleton"
```
