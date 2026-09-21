# 40 — Production (tools, process, milestones)

**Scope:** MVP · **Status:** mixed — process DECIDED, milestones PENDING (see §5) · **Last decision:** D5.28 · **Updated:** 2026-09-20

## Purpose
How the project is built: which tool does which job, how art gets from a prompt to a screen, and what each milestone has to contain before it counts as done. This doc is **downstream of design** — it records the process that serves the decisions in `decisions.md` and the system docs. It decides nothing about the game.

## Player experience goal
None. Production has no player-facing surface; the template row is kept so the doc reads like its siblings. The nearest thing to a goal: nothing in here should ever be the reason a design question gets answered a particular way.

## Rules / Data

### 1. Tool split

| Job | Tool | Lives in | Run by |
|---|---|---|---|
| Game runtime | Godot 4.x, GDScript | `demo/` (not created — gate below) | Tech |
| Game numbers | JSON | `data/*.json` | Content authors, Tech loads |
| Data validation | `data/validate.py` (not written; ships with schema v3) | `data/` | Tech |
| Image generation | ComfyUI + Qwen-Image / Qwen-Image-Edit-2509, local RTX 5090 | graphs mirrored to `proposals/art/*.workflow.json` so prompts are diffable | Tech runs, Art directs |
| Style distillation | Qwen3-VL 8B, `style-distiller` graph | style cards beside the board | Art |
| Board critique | `tools/annotate/server.py` → `<image>.annotations.json` | `proposals/art/` | Art |
| Region re-roll | `tools/annotate/regional_edit.py` | same | Tech |
| Workflow build | `tools/workflows/build_workflows.py` | `tools/` | Tech |
| The record and the board | `STATUS.md` (**authored** by Chief of Staff, **kept and committed** by Tech — D5.38), `leads/`, triage | repo root | Chief of Staff · Tech |
| Git, hooks, the commit sweep | commits, `tools/hooks/`, `tools/sweep.py`, `.claude/` | repo root | Tech (D5.29, D5.39) |

Agent surfaces and what each may write: `AGENTS.md` §4. Settings, weights and the two install traps: `proposals/2026-09-20-local-imagegen-handoff.md` — not restated here.

### 2. The art loop (process)

1. **Direction** defines a cluster — a coherent set of things the game needs drawn (`leads/direction/`).
2. **Generate** locally into `proposals/art/YYYY-MM-DD-<topic>/`. Raw generations stay local; only contact sheets and accepted boards are committed (**D5.28**).
3. **Annotate** — critique pinned to coordinates, not prose about the whole image.
4. **Critique against `01-pillars.md`** — the influence table, including what each influence does *not* own. A board that drifts is rejected against a named row, not a mood.
5. **Owner selects.** A selected board moves to an `accepted/` folder (see open #2) and becomes canon for its cluster.
6. **Decompose** the selected board into UI components → `31-ui.md`. Screens are disposable, components persist (**D5.2**).
7. **Restyle** the demo screens from the component list. Never from an agent's plan — only from a selected board or a human play session (`00-steer.md` §2).

Steps 1–5 run in parallel with engine work and block nothing. Steps 6–7 wait on `31-ui.md`.

### 3. Record discipline

| Rule | Where | Source |
|---|---|---|
| A design point is decided only with a D-number | `design/decisions.md` | `AGENTS.md` §1.2 |
| A lead's brief has one writer: that lead. `STATUS.md` has one **author** (Chief of Staff) and one **keeper** (Tech) | `leads/`, `STATUS.md` | D5.27 → D5.29 → D5.38 |
| Guard rails refuse a malformed commit; the sweep commits other surfaces' work by path, never by content | `tools/hooks/`, `tools/sweep.py` | D5.39 |
| One commit per doc/decision batch; message = what changed + D-numbers; staged by path, never `git add -A` | git | D5.27 |
| Milestone tags on the commit that closes a milestone (`m1-playable`) | git | this doc |
| Two registers: compress for agents, plain words for the owner | everywhere | C21, C22 (`AGENTS.md` §5) |

### 4. Demo gate

The Godot project is not created until `00-steer.md` and the 10–15 system docs are marked distilled (`demo/README.md`). **"Distilled" is defined by C27 (`sys.4`) — see open #3, now closed.**

### 5. Milestones — PENDING

**M1 and M2 are stated in `00-steer.md` §3 and are not restated here.** They move into this doc, in full, when the combat docs they bound are distilled — because a milestone is a promise about content, and the content is still being decided:

| Milestone | Blocked by | What it needs before it can be written here |
|---|---|---|
| M1 — playable duel | conflicts A, B and the C-ref promotions (`proposals/2026-09-20-c-coherence.md` §2, §4) | the ability economy settled (A), `11-initiative.md` written (B + C20 + C13), schema v3, then a done-list the owner can check off |
| M2 — staged duel | M1 played | what "staged" includes, decided after ten duels have been played, not before |

Writing them sooner would be Production deciding design by the back door. The board (`STATUS.md`) carries the live sequence meanwhile, tagged `PROPOSED` until the owner confirms it.

## Dependencies
- Reads from: `00-steer.md` §3–§4 (priorities, MVP boundary) · `decisions.md` (D5.2, D5.27, D5.28) · `demo/README.md` (gate) · `leads/README.md` (who writes what) · `proposals/2026-09-20-local-imagegen-handoff.md` (pipeline detail)
- Writes to: `demo/README.md` (milestones), `31-ui.md` (component list arrives via step 6)

## Open questions
1. **Godot version pin** — 4.7 (archived port's version) or latest 4.x. Tech open #1.
2. **Where accepted assets live.** `.gitignore` currently keeps anything under `proposals/art/**/accepted/`; the long-term home is likely `demo/assets/`. Tech open #2, Content open #1.
3. ~~What "distilled" means as the demo gate.~~ **CLOSED — C27 (`sys.4`), owner 2026-09-20:** written against `02-ontology.md` and `data/SCHEMA.md` (rules in the ontology's vocabulary, numbers pointing at schema fields), **produced by synthesis** across sources, and carrying **no STUB marker and no OPEN row at MVP scope** — all three, not either/or. Production only records it; the gate text lives in `demo/README.md`.
4. Which already-committed smoke-test boards are keepers (D5.28 residue) — Art/Content, then Tech untracks the rest.

## Status table
| Item | Status | Scope | Source |
|---|---|---|---|
| Tool split (§1) | DECIDED | MVP | this doc, local pipeline handoff |
| Art loop (§2) | DECIDED | MVP | `00-steer` §3 #2, D5.2, D5.28 |
| Record discipline (§3) | DECIDED | all | D5.27, C21/C22 |
| Demo gate (§4) | DECIDED; term defined by C27 | MVP | `demo/README.md`, C27 (`sys.4`) |
| M1 / M2 definitions (§5) | PENDING — stay in `00-steer` §3 until combat settles | MVP | `00-steer` §3 |
| Milestone git tags | PROPOSED | MVP | this doc |
