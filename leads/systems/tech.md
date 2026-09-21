# Tech — lead brief (under Systems) · agent: **Claude Code**

Reports to: Systems · Agent surface: Claude Code (only) · Updated: 2026-09-20

## Charter
All technical execution. Builds what Systems specifies and Direction/Content hand over: the Godot 4.x / GDScript duel demo that loads Systems' schema data-driven (the code never names Strength or Stamina — D5.12), the validator, golden tests, local tools, git and Claude Code configuration. Any lead that needs code written hands the task to Tech; Tech does not decide *what* the game is, only *how it runs*.

**Bound to Claude Code.** Tech sessions run in Claude Code in `C:\Claude\shinobi-v2` (`CLAUDE.md` loads the guard rails). Cowork, Codex, ChatGPT and the local LLM do not act as Tech; they write a task to `proposals/` or `inbox/` tagged `[tech]` and Claude Code picks it up.

## Owns
- `demo/` (not created yet — gate in `demo/README.md`)
- `data/validate.py` (to write) — enforces Systems' validator rules against `SCHEMA.md`
- Golden tests; the archived v1 engine at `C:\Claude\Godot\shinobi-master` as *reference only* (ideas, not code, unless a D-number says otherwise) — **not rescued, PC disk only** (D5.40)
- `.claude/` (agent pointers, settings, hooks), `.gitattributes`, `.gitignore`, git hooks; git remote when the owner wants one; `tools/claude-agents/` seed
- `tools/` code (`annotate/` — Content owns its *use*), `tools/hooks/` (proposed)
- **Git execution** (D5.29): staging by path — never `git add -A` — commit messages (what changed + D-numbers), milestone tags (`m1-playable`), and committing another surface's work with a message that says whose it is
- **Mechanical housekeeping** (D5.29): stale files, broken cross-references, renames, D-number stamps on items the owner decided. Never a lead's judgement — that goes back to the lead or to Chief of Staff
- **The commit sweep** (D5.39): run `python tools/sweep.py` at session open and close; `--commit --surface <name>` sweeps. Classifies by **path, never content** (`proposals/2026-09-20-commit-sweep.md` §A.1); flags go to §For Chief of Staff below; a hook refusal stops the sweep and nothing is retried
- **Guard rails** (D5.39): `tools/hooks/` + `.claude/settings.json`. Enable per clone with `git config core.hooksPath tools/hooks` — **including the Mac successor's**
- Asset/data loading contract: where accepted assets live, how JSON is loaded
- Explaining Godot concepts to the owner when they become relevant, not before (AGENTS §5)

## Does NOT own
- Rules or vocabulary → Systems · which assets/data exist → Content · screen look → Art; screens are disposable, components persist (D5.2) · triage, sequencing, milestones, conflicts and the decisions queue → Chief of Staff
- **`STATUS.md` judgement**: what a row says, what is blocked, the queue order, the critical path → Chief of Staff **authors** it. Tech holds **custody** (D5.38): types the file, commits it, transcribes without paraphrase — and never re-sequences. Tech's own row still goes in this brief first

## Reads first
`CLAUDE.md` → `AGENTS.md` → `00-steer.md` §4 (engine constraints D5.12) → `leads/systems.md` → `data/SCHEMA.md` (when it exists) → `demo/README.md` → `proposals/2026-09-20-session-6-handoff.md` §6 E

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | Godot from the start; basic screens are part of prototyping; every screen change reacts to a play session or a selected board | D5.2 | DECIDED |
| — | schema v3 before M1, with refinement | handoff §1 (owner answer) | DECIDED (not D-logged) |
| — | "we need a tech lead, that should be claude code" | Cowork 2026-09-20 | DECIDED (this brief) |
| — | "claude code agents can make these commits on my behalf" | chat 2026-09-20 | DECIDED — Claude Code commits **as Tech** (D5.29); it keeps the board but does not author it (D5.38) |
| — | local image-gen as part of the design-iteration pipeline; get Qwen running locally | chat 2026-09-20 | DONE — see handoff |
| — | "admin and tech and production seem to run together… I think of you as chief of staff" · "status.md is owned by chief of staff. housekeeping may make sense for tech" | Cowork chat 2026-09-20 | **DECIDED — D5.29**; logged here on "log it" |

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
| Git | `main`, local only, clean tree. **Tech executes git** (D5.29), staging by path; two surfaces write this repo | — | D5.29 |
| Roles: Chief of Staff (Cowork) + Tech (Claude Code); `admin` retired after eleven commits | DECIDED — **D5.29** | all | this session |
| Repo guard rails — 4 hook checks + `.claude/settings.json` | **DECIDED D5.39 — installed and verified** (each check refused a real attempt, 2026-09-20) | — | `proposals/2026-09-20-guard-rails.md` |
| Commit sweep — `tools/sweep.py` | **DECIDED D5.39 — installed; first run swept 5 files (Cowork)** | — | `proposals/2026-09-20-commit-sweep.md` |
| Hook bug: first version failed **open** on Windows cp1252 | FIXED same session — UTF-8 read, and a check that cannot run now refuses | — | commit `85263f2` |
| Guard rail B caught **real work**, not a test — refused the D5.40 commit while the board still advertised D5.40 | WORKING as designed, 2026-09-20 | — | commit `06fd397` |
| Git remote (C24) | **DONE 2026-09-20 (D5.40)** — pushed to the owner's private `chris-egan/slop-game` and **verified**: a fresh clone from GitHub matches this one commit for commit (48), same tree hash, 132 files, only the no-reply author. The repo no longer exists on one disk | — | `proposals/2026-09-20-two-machine-migration.md` |
| **History rewritten once, before any push** (2026-09-20) | all 39 commits re-authored to the owner's GitHub no-reply address; every hash changed. Safe only because nothing was pushed and no second clone existed. Backup of the pre-rewrite `.git` kept in the session scratchpad until the push verifies | — | owner, chat |
| GitHub CLI | installed 2026-09-20 (`winget`, v2.101.0). Sign-in is the owner's | — | owner, chat |
| Retired-role residue (`admin`) | CLEARED 2026-09-20 across eight live docs; history left alone | — | X-list / board |
| Stub redirects (X2) + required-reading stamps (X3) | DONE — nine stubs, two proposals; redirects regenerate idempotently | — | `proposals/2026-09-20-agent-experience-response.md` |
| `.claude/settings.json` reach | **PARTIAL by construction** — binds Claude Code's Write/Edit tools; a shell edit (`python`, `sed`) is not covered. The hooks are what actually hold | — | this session |
| `.gitattributes` / `.gitignore` | present; art-binary policy **DECIDED D5.28** — contact sheets + selected boards only, raw gens ignored. `.gitignore` updated 2026-09-20; existing history left alone | — | D5.28 |
| Godot version | OPEN — pin 4.7 (archive) or latest 4.x | MVP | successor-review §4 #5 |

## Next actions
1. ~~Guard rails~~ **done, D5.39** — installed, verified check by check, one
   fail-open bug found and fixed. Remaining: enable on every other clone
   (`git config core.hooksPath tools/hooks`) as they appear. Gate: a clone existing.
2. **Housekeeping carried from the board** (D5.29): `rules.json` `_note`s cite v1 open
   numbers and the removed Arm step → needs Systems' word on the replacements;
   `decisions.md` `Acts on it` value "Production" → Systems' call; which committed
   smoketest PNGs are keepers → Art/Content, then Tech untracks the rest; D1–D4
   compression → Systems. Tech executes, each named lead decides. Gate: per item.
3. ~~The remote~~ **done and verified** (D5.40). ~~The v1 rescue~~ **done** — `sources/v1/`.
   Remaining from migration §6: **step 5, the Mac clone** — clone, enable the hooks, re-seed
   `.claude/agents/`, run the annotator once, and report the commit count back. Gate: the Mac.
4. **D1–D4 compression** is now Systems' whenever it wants it — no longer a deadline, because
   `sources/v1/docs/combat-scene-decisions.md` is in the repo. Tech executes, Systems judges.
5. Write `data/validate.py` alongside `SCHEMA.md` (same commit as schema v3). Gate: `SCHEMA.md` drafted.
4. Headless engine first, data-driven sheets/pools/tags/materials from commit 1; golden test rewritten for v2 rules; then loadout → duel → table-view stub, one commit per screen, owner plays before the next. Gate: action 3 + Systems action 3.

Pipeline follow-ups (low priority, none blocking M1; detail in the handoff §8):
8-step Lightning untested on the *edit* graph · `euler` vs `euler_ancestral` A/B unresolved (n=1) ·
multi-image conditioning wired but unused — it is the path to Kaede/Genzo × 2 poses ·
Qwen-Image-Edit 2511 reported better at character consistency (21 GB).

## Machines (2026-09-20, owner: prompting moves to a Mac; the Tech seat continues as a Claude Code successor there)
| Runs where | What |
|---|---|
| Either machine | repo, git, docs, `data/`, Godot (when the gate clears), `tools/annotate/server.py` |
| **PC only** | ComfyUI + Qwen weights on the RTX 5090; `tools/workflows/build_workflows.py`, `tools/annotate/regional_edit.py` — they now read `SHINOBI_COMFY_ROOT` and **fail with one clear sentence** off-machine (step 6) · the 177 MB v1 Godot archive, not rescued |
| **Remote** | `origin` → the owner's private `chris-egan/slop-game`. Pushed and verified 2026-09-20. Every clone runs `git config core.hooksPath tools/hooks` on arrival |
| **Deadline** | ~~the text behind D1–D4 and the v1 bible live only on the PC disk~~ **DONE 2026-09-20** — `sources/v1/` holds all of v1 `docs/` and the v4 wireframe; every stub and the D1–D4 note now cite the in-repo copies |

Successor handoff checklist: that file §7. Board custody after the move: `proposals/2026-09-20-board-custody.md` (Chief of Staff and owner rule).

## Verification record (D5.39, 2026-09-20)
| Check | Attempt made | Result |
|---|---|---|
| A | duplicated the `D5.38` row and committed | refused, named the duplicate |
| B | committed the board while it advertised `D5.39`, already logged | refused, named both numbers |
| C | `git add -f` a raw `.png` under `proposals/art/` | refused, named the file |
| D | added a `D5.40` row, message omitting the number | refused at `commit-msg` |
Every attempt was made against the real repo and reverted; the tree was byte-identical afterwards. The first attempt exposed the fail-open bug above — the reason to verify by attempting rather than by reading the code.

## For Chief of Staff (rows Tech transcribes but does not decide — D5.38)
- **D5.38 landed.** `leads/chief-of-staff.md` §Owns was amended by Tech to match the log (canon rule 2: a doc that disagrees with `decisions.md` is wrong). Re-word it as you like — the brief is yours; the amendment was hygiene, not judgement.
- **D5.39 landed** — guard rails and the sweep are live. Two board consequences, held for the owner's approval before Tech transcribes: the next-free line must move past **D5.39** (check B refuses commits touching `decisions.md` or `STATUS.md` until it does), and the Waiting list entry for guard rails + sweep is now Ruled.
- **Conflict #4's wording is superseded.** It reads "Chief of Staff sole writer, Tech commits"; D5.38 split that into author and keeper.
- **Verdicts round 1 transcribed** (`inbox/2026-09-20-queue-verdicts-1.md`). Two reconciliations Tech did **not** decide: (a) the addendum rules **Q6** while the Board-rows section still lists it reprompted — transcribed as ruled, per the addendum; (b) the file says "Not yet ruled: D5.39", which the owner ruled in chat before the file was written to disk — transcribed as ruled and logged.
- **No CONFIRMED tag was written.** Q4 *was* the confirm-the-critical-path question and came back **reprompted** ("too brief how is user to know without easy reference"). The critical path stays `PROPOSED`. Chief of Staff owes the re-presentation.
- **Board rows owed from the migration work** (handed to the owner for approval first): remote pushed and verified · v1 rescued · the "D1–D4 not compressed" housekeeping line loses its deadline but stays open · Tech's blocker is no longer the owner.
- **History was rewritten once**, before the first push, re-authoring all commits to the owner's no-reply address. Anything quoting a pre-2026-09-20 commit hash is stale; two in this brief were repointed.
- **THERE IS A THIRD SURFACE.** The owner runs a **second Claude Code instance as an art execution agent** against the local Qwen stack; `tools/gen_board.py` and `tools/contact_sheet.py` are its work, not Cowork's. Consequences, none of them Tech's to rule on:
  - **D5.27, D5.38, D5.39 were all written for two surfaces.** "Cowork→`chief-of-staff.md`, everything else flag" in sweep table A.1 has no row for a third writer, and `tools/**` is classified as Tech's own work on the assumption that only Tech writes there.
  - **That surface can run git.** `CLAUDE.md` tells any Claude Code session it is Tech by default, so two sessions would both answer to the same brief and the same board custody. Either it commits its own art work under its own name, or it never commits and Tech sweeps for it — the owner or Chief of Staff decides which, and `CLAUDE.md` needs a sentence either way.
  - **Which lead is it?** Asset production runs sit with Content (`leads/systems/content.md` Owns); the image-gen pipeline as a tool sits with Tech. It currently has no brief and no routing tag.
  - Sweep fixed today: `tools/**` no longer claims Tech authorship, and `--surface` carries a warning that the script cannot tell who wrote a file.
- **Sweep flags, 2026-09-20:** none beyond the line above. `STATUS.md` was classified as custody, not swept — it carries your pending edit and the owner is approving the rows first.
- **Add to your own brief when you next write it** (Tech does not edit it): *"Audit — read `git log` since the last Chief of Staff session and flag anything that should not have landed. After the fact, never a gate: Chief of Staff cannot run git, and a commit is reversible (D5.39)."*
- Housekeeping line "`leads/admin.md`, `tools/claude-agents/admin.md`, `.claude/agents/admin.md` — tombstone/delete with D5.29" is **done**; all three deleted, no dangling pointers. Strike it.
- Tech row: next action is now the **guard-rails** pick (`proposals/2026-09-20-guard-rails.md` §6), then the carried housekeeping. Godot still gated on schema v3.

## Open questions
1. Godot version pin.
2. Accepted-asset location for Content.
3. ~~Art binaries: LFS, ignore, or keep small set~~ — closed by **D5.28**.

## Escalates to
Systems for any rule ambiguity found while coding — never resolve it in code. Owner for scope.
