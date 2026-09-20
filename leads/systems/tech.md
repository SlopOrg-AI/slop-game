# Tech — lead brief (under Systems) · agent: **Claude Code**

Reports to: Systems · Agent surface: Claude Code (only) · Updated: 2026-09-20

## Charter
All technical execution. Builds what Systems specifies and Direction/Content hand over: the Godot 4.x / GDScript duel demo that loads Systems' schema data-driven (the code never names Strength or Stamina — D5.12), the validator, golden tests, local tools, git and Claude Code configuration. Any lead that needs code written hands the task to Tech; Tech does not decide *what* the game is, only *how it runs*.

**Bound to Claude Code.** Tech sessions run in Claude Code in `C:\Claude\shinobi-v2` (`CLAUDE.md` loads the guard rails). Cowork, Codex, ChatGPT and the local LLM do not act as Tech; they write a task to `proposals/` or `inbox/` tagged `[tech]` and Claude Code picks it up.

## Owns
- `demo/` (not created yet — gate in `demo/README.md`)
- `data/validate.py` (to write) — enforces Systems' validator rules against `SCHEMA.md`
- Golden tests; the archived v1 engine at `C:\Claude\Godot\shinobi-master` as *reference only* (ideas, not code, unless a D-number says otherwise)
- `.claude/` (agent pointers, settings, hooks), `.gitattributes`, `.gitignore`, git hooks; git remote when the owner wants one; `tools/claude-agents/` seed
- `tools/` code (`annotate/` — Content owns its *use*)
- Asset/data loading contract: where accepted assets live, how JSON is loaded
- Explaining Godot concepts to the owner when they become relevant, not before (AGENTS §5)

## Does NOT own
- Rules or vocabulary → Systems · which assets/data exist → Content · screen look → Art; screens are disposable, components persist (D5.2) · milestones/sequence → Admin · git *execution* (staging, commit messages, tags) → Admin; Tech owns the *tooling* (hooks, `.gitignore`, `.claude/`)

## Reads first
`CLAUDE.md` → `AGENTS.md` → `00-steer.md` §4 (engine constraints D5.12) → `leads/systems.md` → `data/SCHEMA.md` (when it exists) → `demo/README.md` → `proposals/2026-09-20-session-6-handoff.md` §6 E

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | Godot from the start; basic screens are part of prototyping; every screen change reacts to a play session or a selected board | D5.2 | DECIDED |
| — | schema v3 before M1, with refinement | handoff §1 (owner answer) | DECIDED (not D-logged) |
| — | "we need a tech lead, that should be claude code" | Cowork 2026-09-20 | DECIDED (this brief) |
| — | "claude code agents can make these commits on my behalf" | chat 2026-09-20 | DECIDED — Claude Code commits, as **Admin** (D5.27); Tech owns the tooling |
| — | local image-gen as part of the design-iteration pipeline; get Qwen running locally | chat 2026-09-20 | DONE — see handoff |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Godot project | not started — gated on 10–14 distilled + schema v3 | MVP | demo/README |
| Validator | not written | MVP | handoff §6 D |
| `.claude/agents/` pointers | **DONE** — 8 leads copied in, `engine`→`tech` rename applied; copies gitignored, `tools/claude-agents/` is source of truth | — | leads/README |
| Local image-gen pipeline | **DONE, verified** — ComfyUI v0.36.0 + Qwen-Image / Qwen-Image-Edit-2509 on the 5090 | — | `proposals/2026-09-20-local-imagegen-handoff.md` |
| `tools/workflows/build_workflows.py` | **DONE** — generates all 4 Qwen graphs; edit this, not the JSON | — | this session |
| `tools/annotate/` (server, UI, `regional_edit.py`) | **DONE, verified** — Content owns its use | — | `tools/annotate/README.md` |
| Style distiller (Qwen3-VL 8B) | **DONE** — one card produced, Art has not accepted it | — | handoff §4 |
| Git | 7 commits on `main`, local only, clean tree. Tech commits on the owner's behalf. | — | chat 2026-09-20 |
| `.claude/settings.json` guard rails (deny edits to `sources/**`, `design/decisions.md` without approval) | PROPOSED — not written | — | this session |
| Pre-commit hook: `decisions.md` diff requires a D-number in the message | PROPOSED — not written | — | this session |
| `.gitattributes` / `.gitignore` | present; art-binary policy **DECIDED D5.28** — contact sheets + selected boards only, raw gens ignored. `.gitignore` updated 2026-09-20; existing history left alone | — | D5.28 |
| Godot version | OPEN — pin 4.7 (archive) or latest 4.x | MVP | successor-review §4 #5 |

## Next actions
1. ~~Copy `tools/claude-agents/*` → `.claude/agents/`~~ **done**. Remaining: propose
   `.claude/settings.json` + pre-commit hook in `proposals/`. Gate cleared (structure committed `9ea9650`).
2. ~~Resolve open #3 — art binaries~~ **decided D5.28**; `.gitignore` now ignores raw
   generations under `proposals/art/**` and keeps `_contact-sheet.png` plus anything under
   an `accepted/` folder. Remaining: tell Content where accepted assets live (open #2).
   Gate: none.
3. Write `data/validate.py` alongside `SCHEMA.md` (same commit as schema v3). Gate: `SCHEMA.md` drafted.
4. Headless engine first, data-driven sheets/pools/tags/materials from commit 1; golden test rewritten for v2 rules; then loadout → duel → table-view stub, one commit per screen, owner plays before the next. Gate: action 3 + Systems action 3.

Pipeline follow-ups (low priority, none blocking M1; detail in the handoff §8):
8-step Lightning untested on the *edit* graph · `euler` vs `euler_ancestral` A/B unresolved (n=1) ·
multi-image conditioning wired but unused — it is the path to Kaede/Genzo × 2 poses ·
Qwen-Image-Edit 2511 reported better at character consistency (21 GB).

## Open questions
1. Godot version pin.
2. Accepted-asset location for Content.
3. ~~Art binaries: LFS, ignore, or keep small set~~ — closed by **D5.28**.

## Escalates to
Systems for any rule ambiguity found while coding — never resolve it in code. Owner for scope.
