# Engine — sub-lead brief (under Systems)

Reports to: Systems · Directs: Claude Code sessions · Updated: 2026-09-20

## Charter
What **runs** it. Godot 4.x / GDScript duel demo that loads Systems' schema data-driven — the code never names Strength or Stamina (D5.12). Also owns the tooling layer: Claude Code direction (`.claude/`), git integration (hooks, `.gitattributes`, `.gitignore`), validator scripts, golden tests, local tools (`tools/`).

## Owns
- `demo/` (not created yet — gate in `demo/README.md`)
- `data/validate.py` (to write) — enforces Systems' validator rules against `SCHEMA.md`
- Golden tests; the archived v1 engine at `C:\Claude\Godot\shinobi-master` as *reference only*
- `.claude/` (agent pointers, settings), `.gitattributes`, `.gitignore`, hooks; git remote when the owner wants one
- `tools/annotate/` code (Content owns its *use*)
- Godot concepts explained to the owner when they become relevant, not before (AGENTS §5)

## Does NOT own
- Rules or vocabulary → Systems · which assets/data exist → Content · screen look → Direction/art; screens are disposable, components persist (D5.2) · milestones/sequence → Production

## Reads first
`AGENTS.md` → `00-steer.md` §4 (engine constraints D5.12) → `leads/systems.md` → `data/SCHEMA.md` (when it exists) → `demo/README.md` → `proposals/2026-09-20-session-6-handoff.md` §6 E

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | Godot from the start, basic screens are part of prototyping; every screen change reacts to a play session or a selected board | D5.2 | DECIDED |
| — | schema v3 before M1, with refinement | handoff §1 (owner answer) | DECIDED (not D-logged) |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Godot project | not started — gated on 10–14 distilled + schema v3 | MVP | demo/README |
| Validator | not written | MVP | handoff §6 D |
| `.claude/agents/` lead pointers | created this session | — | leads/README |
| `.gitattributes` / `.gitignore` | present; art-binary policy pending (Production open #2) | — | — |
| Godot version | OPEN — pin 4.7 (archive) or latest 4.x | MVP | successor-review §4 #5 |

## Next actions
1. Nothing in `demo/` until gate clears. Gate: Systems action 3 + schema v3 D-number.
2. Write `data/validate.py` alongside `SCHEMA.md` (same commit as schema v3). Gate: `SCHEMA.md` drafted.
3. Headless engine first, data-driven sheets/pools/tags/materials from commit 1; golden test rewritten for v2 rules; then loadout → duel → table-view stub, one commit per screen, owner plays before the next. Gate: action 2.

## Open questions
1. Godot version pin.
2. Accepted-asset location for Content.
3. Art binaries: LFS, ignore, or keep small set (with Production).

## Escalates to
Systems for any rule ambiguity found while coding — never resolve it in code.
