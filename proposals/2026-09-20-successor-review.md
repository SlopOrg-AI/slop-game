# Proposal — successor review & next steps (v2)

**Produced by:** Claude (Cowork), 2026-09-20 · **Targets:** `00-steer.md` §3 priorities, `40-production.md` (stub) · **Proposes:** a sequenced work plan for the next ~4 sessions + 5 owner decisions · **Supersedes:** nothing (no D-numbers claimed). Status: `PROPOSED`.

---

## 1. State of v2 (read from disk, 2026-09-20)

| Area | State |
|---|---|
| Canon rules, steer, pillars | Done. AGENTS / 00 / 01 coherent; Project mirror in sync (byte-identical). |
| Decisions log | D5.1–D5.15 logged. **D1–D4 not compressed in** — still only in `C:\Claude\docs\combat-scene-decisions.md`. |
| System docs | **5 of 14 written** (00, 01, 12, 15, 50). **Stubs:** 10, 11, 13, 14 (all MVP), 20, 21, 30, 31, 40. |
| Data | v1 schema copied to `data/`. Drift vs D5.9 / D5.12 / D5.14 documented, not migrated. |
| Demo | Not started. Gate in `demo/README.md`: docs 10–14 distilled first. |
| Git | **Not initialised** (no `.git` in `shinobi-v2/`). "Disk is canon, git is the record" has no record yet. |
| Stale file | `design/12-reactions-insight.md` — a delete marker; still present. |

**Critical path to M1:** distill 10 → 11 → 13 → 14 (+ D1–D4 compression) → schema v3 → Godot project. Nothing else blocks the demo.

## 2. Inconsistencies found

1. **Reaction slot.** `00-steer.md` §4 IN: "Loadout screen (typed slots: body/mind/spirit **+ reaction**)". D5.9 / Open #3 default A: *no* dedicated reaction slot. `characters.json` has `slots.reaction: 1`; `rules.json` has `reactions.max_armed: 1`. Three sources, two answers. Needs one D-number.
2. **Insight reveal timing.** `rules.json` `insight.reveal_timing: "OPEN #1 — arm_declared | resolve_interrupt"` — the Arm step no longer exists (D5.8). The open needs restating as "during Plan vs at impact" or closing (D2.14 already says "any selection or impact moment").
3. **Open-question numbering.** `rules.json` `_note`s cite v1 numbers (#0, #1, #2, #4); `00-steer.md` §6 renumbered. Harmless until someone follows the wrong pointer.
4. **Persistence of un-fired reactions** — `12-reactions-passives.md` says "v1 rule stands"; with `hold` costs now per-ability (D5.9), the blanket `persist_until_fired: true` in `rules.json` is redundant or contradictory. Resolve in the schema bump.
5. **Pillar numbering** in `01-pillars.md`: row 8 precedes row 7. Cosmetic; fix when touched.
6. **Unplayed core loop.** Priorities say "a human plays 10 duels" but the only playable thing is `wireframes/combat-1v1-v4.html` (v1 rules: Declare→Arm→Resolve, one armed reaction). v2 says "no HTML rebuild" (D5.2) but does not say whether the *existing* HTML should be played meanwhile. It costs nothing to open.

## 3. Proposed sequence

### Session A — housekeeping (≈30 min, owner + agent)
- `git init` + commit "v2 skeleton" in `shinobi-v2/` (README §First-time setup). Everything after this is diff-able.
- Delete `12-reactions-insight.md`.
- Log **D5.16**: reaction slot answer (decision 2 below). Fix `00-steer.md` §4 to match.
- Log **D5.17**: restate/close reveal-timing open; renumber `rules.json` `_note`s to `00-steer` §6.
- Optional, zero-cost: owner plays `combat-1v1-v4.html` 3–5 rounds. Purpose is *feel* (does reading the opponent happen at all?), not tuning — it runs v1 rules. Write one paragraph to `proposals/YYYY-MM-DD-first-human-play.md`.

### Session B — distill the MVP combat docs (agent drafts, owner reacts, one doc per pass)
Order by dependency: **10 combat loop → 11 initiative → 13 damage/wounds → 14 scenes/conditions.** Sources: v1 bible §§3–10, D2.x, D3.1–D3.4, findings-02. Each doc: template sections, tables, numbers pointed at `data/*.json`, status table with D-numbers. While drafting 10, compress D1–D4 into `decisions.md` as the promised table (one line each; supersessions kept). Then `40-production.md` (tool split, M1/M2 definitions moved out of `00-steer`, image-gen loop) and `31-ui.md` (the **component library list** D5.2 depends on — initiative strip, queue row, armed-slot, wound sheet, log, radial stub, standee, diorama tile). 20/21/30 stay stubs until after M1 except what the art loop needs from 30.

### Session C — schema v3 (one D-number, one commit)
- `abilities.json`: `kind ∈ {activated, reaction, sustained, decaying, one-off}`, `hold`/`upkeep` cost objects; drop `shot` ids or keep as `_shot`.
- `states.json`: tiered `family:name` tags, tier 1–5, decay per round (D5.14).
- `characters.json`: `scale`, `kind`; slots per D5.16.
- `rules.json`: remove `reactions.max_armed` if Option A; keep D3.1–D3.4 as *applied* values (they're pending play — flag with `_pending_play: true` rather than leaving unapplied).
- Add `data/SCHEMA.md` (field reference) so the Godot loader has a contract. Small: 17 abilities, 8 states, 2 characters.

### Session D+ — Godot M1 (agent builds, owner plays)
1. **Headless engine first** (`demo/duel/engine/`), GDScript, reads `../data`. Reuse *ideas* from the archived `duel/engine/*`; where rules are unchanged, diff against `tests/golden-seed7-policyA.txt`. Where D5.8/D5.9/D5.14 changed rules, the golden test is expected to break — write a new one.
2. Engine constraints baked in from commit 1: `Actor{scale, kind, stats-from-data}`, `Scene{scale, parent, children}`, data-driven selectable-actor list, tiered tags (D5.12, D5.14). Cheap now, expensive later.
3. Screens, in order: loadout → duel (queue, armed slot, initiative bar, wound list, log) → table-view stub. Plain Godot Control nodes, "ink over paper" placeholder. Each screen composed from `31-ui` components.
4. AI: scripted, with "was I countered last round?" memory (findings-02 F5).
5. **Exit:** owner plays 10 duels; findings → `proposals/`; opens #1–#4 answered or re-gated.
Godot concepts explained as they come up (scene tree, Control vs Node2D, autoloads, Resources vs JSON) — not before.

### Parallel track — art/UI loop (owner-run)
Image gen → `proposals/art/YYYY-MM-DD-<topic>/` → agent critique against `01-pillars` influence table + anti-goals → selected board decomposed into `31-ui` components. First target: two character cut-outs (Kaede, Genzo) in 2 poses each; second: one diorama tile. Feeds M1 restyle, not M1 scope.

## 4. Decisions needed from the owner
1. **Play the v4 HTML now?** Yes (cheap feel-check on v1 rules) / No (wait for Godot M1, avoid anchoring on v1 loop).
2. **Reaction slot for MVP.** A: typed slots hold any kind, reserves limit concurrency (D5.9 default) · B: keep `+ reaction` slot as in `00-steer` / `characters.json` · C: hard cap on armed count.
3. **Schema v3 before M1 engine, or M1 on v2 schema then migrate?** Before is cheaper (port once); after gets a playable duel sooner but replays the v1 model.
4. **Who edits `design/` during distillation?** Agent writes directly on owner instruction in-session (fast) · agent writes to `proposals/`, owner promotes (safer, slower).
5. **Godot version** — pin 4.7 (archive used it) or latest 4.x stable.

## 5. Risks I'd watch
- **Distillation drift**: re-deriving 10–14 from a 300-line bible invites re-designing. Rule: copy the decided rule, cite the D-number, put anything new under Open questions.
- **Agent scope creep in Godot** (v1 failure mode). Guard already in D5.2: every screen change reacts to a play session or a selected board. Add: one commit per screen, owner plays before the next.
- **Data before docs**: don't let schema v3 encode rules that 10–14 haven't written down.
