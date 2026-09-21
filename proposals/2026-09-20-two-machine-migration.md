# Proposal — prompting moves to a Mac; the PC disk goes away

**Produced by:** Tech (Claude Code), 2026-09-20 · **Targets:** git remote (none exists), `sources/`, `design/decisions.md`, `demo/README.md`, `leads/systems/tech.md`, `tools/`, `proposals/2026-09-20-guard-rails.md` · **Proposes:** what must happen before the owner prompts from a Mac, what stays on the PC forever, and what it costs · **Status:** `PROPOSED` · C24. **Nothing has been done: no remote created, nothing pushed, no account touched.**

---

## 1. The one blocking fact

The repo has **no remote**. `git remote -v` is empty; 28 MB of history exists on the PC disk and nowhere else. Canon rule 1 says this folder is canon — if the disk holding it is unreachable, there is no canon on the Mac and no v2 project.

Everything else below is consequence or cleanup. This is the blocker.

## 2. What canon cites that is *not* in the repo

`sources/README.md` names the frozen v1 workspace at `C:\Claude\` as evidence. Four things there are cited *by canon*, not merely referenced:

| # | Path (PC only) | Cited by | Consequence on the Mac |
|---|---|---|---|
| 1 | `docs\combat-scene-decisions.md` | `design/decisions.md` line 5 — **the record for D1–D4**, "cited by number from the system docs" | **D1–D4 become unreadable.** Four decisions the design docs cite by number, with no text behind them |
| 2 | `docs\01-design-bible.md` §7 | `design/12-reactions-passives.md` — v1 grading/cost detail "still to be distilled", D3.2–D3.4 | That doc can never be finished |
| 3 | `Godot\shinobi-master\` | `demo/README.md`, `leads/systems/tech.md` — archived v1 engine, reference only; its `data/` is already copied into `data/` | Reference lost. Low cost: ideas only, and the data came across |
| 4 | `wireframes\combat-1v1-v4.html`, `shinobi-prototype\` | `00-steer.md` §2, C23 ("static tableau like html looked like") | The only running artefact of v1 combat. The owner still cites it |

**#1 and #2 are not optional.** Either the text comes into the repo before the move, or D1–D4 and the v1 ability detail are gone. D1–D4 compression has been "housekeeping owed" since session 5; the move converts it from *owed* to *now*.

Cheapest fix for #3/#4: copy the wireframe and the archived Godot project into `sources/v1/` as a frozen snapshot, or accept the loss deliberately and strike the citations. Size is the only argument against — worth measuring before deciding, not assuming.

## 3. What can never move

| Thing | Why | Effect |
|---|---|---|
| ComfyUI + Qwen-Image / Qwen-Image-Edit / Qwen3-VL on the RTX 5090 | tens of GB of weights, CUDA | **All image generation stays on the PC.** A Mac session can direct and critique, not generate |
| `tools/workflows/build_workflows.py`, `tools/annotate/regional_edit.py` | hard-coded `C:\tools\ComfyUI_windows_portable`, `C:\Claude\shinobi-v2\proposals\art` | PC only. Should read those paths from config or an env var, so they fail with a clear message off-Windows instead of a confusing one |
| `tools/annotate/server.py` | stdlib only | Runs anywhere — but only sees boards that are **in the repo** |

**Consequence of D5.28, which was decided when one machine held everything:** raw generations are gitignored, so a Mac session sees only contact sheets and accepted boards. Critiquing a raw board — the step the annotator exists for — becomes a PC-side job, or D5.28 needs an exception for the cluster currently being worked. A decision, not a detail.

## 4. What travels cleanly

- `.gitattributes` already normalises everything to LF. No line-ending surprise on macOS.
- Godot 4.x, Python 3.10+, git: all present or trivially installed on macOS.
- `.claude/agents/` is gitignored and re-seeded from `tools/claude-agents/` — but that folder's README gives Windows `copy` commands. One-line fix: add the `cp` equivalent.
- Docs that say `cd C:\Claude\shinobi-v2` (`README.md`, `tools/claude-agents/README.md`) need a second line, not a rewrite.

## 5. What this does to the guard-rails proposal

It strengthens it and changes one thing.

- **Versioned hooks were already the right call** (`core.hooksPath tools/hooks`, tracked). With more than one clone it stops being a nicety: `.git/hooks` would have to be set up by hand per machine and would drift. Tracked hooks travel with the clone.
- **One command per clone:** `git config core.hooksPath tools/hooks`. Three clones now — PC, Mac, Cowork's — so say it once in `README.md`.
- **Check B gets more valuable.** Two machines and two agent surfaces means more chances for two sessions to read the same next-free D-number. That happened twice tonight on one machine.
- **`.claude/settings.json`** is per-repo and tracked; it travels unchanged.

No change to the four checks themselves.

## 6. Sequence — ordered, because two steps have a hardware deadline

1. **Decide the remote.** A private GitHub repo is the obvious answer; any host reachable from both machines works. **Owner's call and owner's account — Tech will not create one or push to one unasked.**
2. **Rescue the cited v1 material** (§2 #1 and #2 at minimum) into `sources/` while the disk is still there. This is the irreversible-if-skipped step.
3. Compress D1–D4 into `decisions.md` — Systems' judgement, Tech executes. Alternative that preserves the option: copy the v1 file in verbatim as evidence now, compress later.
4. Push. Verify the clone is complete from a second directory **on the PC** before trusting it.
5. Clone on the Mac, install hooks, re-seed `.claude/agents/`, run the annotator once against `proposals/art/` to confirm what should work does.
6. Fix the hard-coded paths in `tools/` to fail loudly off-Windows (§3).
7. Amend the docs in §4 and add a "machines" section to `leads/systems/tech.md`: what runs where.

Steps 2 and 3 are the ones with the deadline attached to the hardware.

## 7. Handoff — what the Mac Tech successor needs

The owner has confirmed the Tech seat continues: a **Claude Code successor on the Mac**. It will inherit the repo and git and **none of this conversation**. Everything it needs must be on disk before the PC goes away. This section is that list; it assumes nothing.

**Read, in order:** `CLAUDE.md` → `AGENTS.md` → `STATUS.md` → `leads/systems/tech.md` → this file → `proposals/2026-09-20-guard-rails.md` → `proposals/2026-09-20-board-custody.md`.

**Set up, once:**

| Step | Command / check | If it fails |
|---|---|---|
| Clone | from the remote the owner chose (§6 #1) | there is no project — stop and ask |
| Hooks | `git config core.hooksPath tools/hooks` — only if guard rails were approved | check whether `tools/hooks/` exists at all before assuming |
| Subagent pointers | `cp tools/claude-agents/*.md .claude/agents/ && rm -f .claude/agents/README.md` (the folder is gitignored; `tools/claude-agents/` is the source of truth) | harmless; pointers are a convenience |
| Python | `python3 --version` ≥ 3.9 for `tools/annotate/server.py` | only the annotator is affected |
| Godot | not until the gate in `demo/README.md` clears | — |

**Know, before being surprised:**

1. **Image generation does not exist on this machine.** ComfyUI, the Qwen weights and the RTX 5090 are on the PC. `tools/workflows/build_workflows.py` and `tools/annotate/regional_edit.py` have Windows paths compiled in and will fail here. That is expected, not broken.
2. **Raw art boards are not in the repo** (D5.28). The annotator will show contact sheets and anything under `accepted/`, and nothing else.
3. **Check `sources/v1/`.** If §2's rescue happened it holds the v1 combat-scene decisions (the text behind D1–D4) and the design bible. **If it is missing, D1–D4 have no text anywhere reachable** — say so plainly when a doc cites them; do not reconstruct them from the system docs that cite them.
4. **Two surfaces still write this repo.** Stage by path, never `git add -A`, and commit another surface's work with a message that says whose it is. There are several examples in the log.
5. `.gitattributes` normalises to LF; a whole-file diff on first checkout would mean that config was lost, not that the files changed.

**Owed to the owner on arrival:** confirm from the Mac that the clone is complete (`git log --oneline | wc -l` against what `STATUS.md` claims), then say so. Until that check runs, the PC disk should not be considered disposable.

## 8. For the owner

1. **Which remote**, and private? Tech does not create accounts or push anywhere without you saying so.
2. **v1 rescue scope:** the two cited documents only (small), or the whole frozen workspace including the wireframe and archived Godot project (bigger — measure first)?
3. **D5.28 exception** for raw boards while the art loop is split across two machines: yes, no, or defer until it bites?
4. Guard rails: unchanged ask — `proposals/2026-09-20-guard-rails.md` §6.
