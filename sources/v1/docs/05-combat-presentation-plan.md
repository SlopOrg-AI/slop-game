> **PARKED 2026-09-20 — NOT CANON.** This doc surfaced only on disk, never synced to the project, and its decisions (D3.1p–D3.8p) were numbered as a competing "session 3" against the real, project-canonical D3.1–D3.4 in `combat-scene-decisions.md`. The Godot port it plans against is archived (D4.1). Some of its source material (`00-art-lore-steer.md`, `02-vision-board.md`, `04-art-direction.md`) is unrecoverable — see `combat-scene-decisions.md` D4.3. Kept for reference only; do not build against this without re-confirming direction, especially D3.6p (multi-actor combat), which is unconfirmed as real owner direction.

# 05 — Combat Presentation & UI Rework

**Status:** WORKING · options open where marked
**Updated:** 2026-09-19 (session 3)

> Decomposition of the work needed to move the Godot combat screen from the ported
> wireframe layout to the directed-camera / staged-diorama vision. Source material:
> `00-art-lore-steer.md`, `02-vision-board.md`, `04-art-direction.md` (art-branch
> agent output, read 2026-09-19). Decisions recorded in `combat-scene-decisions.md`
> as D3.1–D3.6. Combat rules are unchanged by this document.

---

## 1. Why this document exists

The Godot port reached Phase 2 of `Godot\shinobi-master\CLAUDE.md`: a working
1v1 duel playable with the mouse, built as a faithful port of wireframe
**layout A** (`combat-1v1-v3/v4`). That layout is now superseded.

The art-branch documents explicitly list what layout A *is* under their **Avoid**
heading (`04` §7): large permanent drawers, full-screen card-browser
presentation, large side panels open during normal selection. The port is correct
against its brief and wrong against the current vision. That is a spec change, not
a defect — but **`CLAUDE.md` Phase 2 is now stale and must be rewritten before
anyone builds against it again.**

The engine is unaffected. `duel/engine/*` is headless, signal-driven and pinned by
`tests/golden-seed7-policyA.txt`. That is what makes this rework affordable.

---

## 2. Settled direction (session 3)

| # | Decision | Consequence |
|---|---|---|
| D3.1 | 3D camera in 3D space; fighters are 2D cutouts; terrain/buildings simplified and representational | Scene root becomes `Node3D`, not `Control` |
| D3.2 | **Palette stays "ink over paper."** The noir / late-Victorian / industrial revision in `02`/`00` is deferred, not adopted | No UI art churn now; `Ink.gd` values stand |
| D3.3 | Tabletop-wargaming language applies to **props** — terrain features, decor, buildings, clutter. It does **not** apply to UI/UX | Resolves the apparent conflict with "no board-game view" |
| D3.4 | Exception-based disclosure: a normal sunny day draws no attention; a flood is signposted | Conditions render by deviation from baseline, not always |
| D3.5 | **"A thunk."** Every click moves the camera with purpose to the next pose, with a corresponding UI change | Requires a Director layer (§5) |
| D3.6 | Combat must scale to many-vs-many — see `06-multi-actor-combat.md` | Shapes the UI *now*, even though the engine is still 1v1 |

### Deliberately deferred
- Noir/industrial palette revision (D3.2).
- Real art. Grey-box and silhouette placeholders until the Director proves timing.
- The `02` §13 "north-star screenshot" paragraph describes Japanese village
  architecture, which the same document's correction section drops. **The
  correction wins; that paragraph is stale** and will mislead an art agent
  reading it cold.

---

## 3. What survives the rework

| Layer | Fate |
|---|---|
| `duel/engine/*`, `DataStore` | **Untouched.** Golden test stays green throughout — that is the proof this is cosmetic. |
| `tests/run_golden.gd` | Untouched. Never sees the UI. |
| `Ink.gd` palette + factories | Kept (D3.2). Style factories survive; some widgets do not. |
| `Log`, `InitiativeBar` | Reworked, not replaced — both are already thin strips. |
| `Hand`, `AbilityCard`, `BudgetStrip`, `SidePanel`, stats drawer | **Deleted.** Replaced by radial + tooltip + compact reserves. |
| `CineStrip` | **Deleted.** Replaced by the real 3D stage. |
| `DuelScreen` (root `Control`) | **Replaced** by `Node3D` stage root + `CanvasLayer`. |
| `tests/run_ui_smoke.gd` | Rewritten against the new controls. Keep the pattern: drive real widgets, never the engine directly. |

Roughly 60% of the Phase 2 UI goes. The correctness-critical part does not.

---

## 4. Approach options — how to execute the rework

> **RESOLVED (session 3, D3.8):** new scene alongside · UI written against a list of
> actors · hybrid placement · thunk on every click including DECLARE. The options
> below are kept as the reasoning behind that choice.

### 4a. Axis 1 — replacement strategy

**Option 1 — Parallel stage scene (greenfield, switch when ready)**
New `res://duel/stage/DuelStage.tscn` (`Node3D` + `CanvasLayer`) built alongside
the existing `DuelScreen.tscn`. Both drive the same `Duel`. `run/main_scene` flips
when the new scene reaches parity; the old screen is then deleted.
- **For:** never a broken build; the old screen stays a live oracle for "what
  should this value be?"; `run_ui_smoke.gd` keeps passing against it while the new
  stage is half-built; both can run side by side for comparison.
- **Against:** two UIs compiling; some duplicated signal wiring; requires the
  discipline to actually delete the old one.
- **Risk:** low. **Effort:** medium.

**Option 2 — In-place strangler**
Keep `DuelScreen` as a `Control` root; swap components one at a time
(`CineStrip` → `SubViewportContainer` holding the 3D stage, `Hand` → radial, …).
- **For:** continuously playable; small diffs; no duplicated wiring.
- **Against:** 3D ends up inside a SubViewport — an extra render target, awkward
  fullscreen camera work, fiddlier 3D input picking. The structure/values refactor
  (§5, B4) would happen inside a codebase still shaped by the old
  rebuild-everything model.
- **Risk:** medium, accumulating. **Effort:** medium-high overall.

**Option 3 — Engine first, then build the UI once**
Do many-vs-many (`06`) before touching the UI.
- **For:** target selection, initiative display and the radial all change shape
  under N actors; doing it first avoids building them twice.
- **Against:** long stretch with nothing visible; and the engine change is
  **blocked on an unmade design decision** — a single shared ±50 bar cannot
  represent three teams (`06` §3). Also the golden test only covers 1v1, so a
  large engine change lands with weaker coverage than it appears.
- **Risk:** medium-high. **Effort:** high.

**Option 4 — Roster façade now, engine later**
Add a thin N-actor façade over the current `Duel` before any UI work:
`duel.actors`, `duel.team_of(a)`, `duel.allies_of(a)`, `duel.enemies_of(a)`,
`duel.player_team`. Today it returns two actors on two teams. **The new UI is
written against the façade and never says `you`/`opp`.** The engine grows into
real many-vs-many on its own track, behind the same names.
- **For:** UI and engine proceed in parallel; the UI is built once; the façade is
  a small, behaviour-free change with a hard regression net (the golden log must
  stay byte-identical).
- **Against:** abstraction slightly ahead of need; the façade must be honest about
  what it cannot yet express (initiative, `06` §3).
- **Risk:** low. **Effort:** small now; avoids a large rebuild later.

**Recommendation: Option 1 + Option 4.** They compose. Build the façade first
(days, not weeks, and provable by the golden test), then build a parallel stage
scene against it.

### 4b. Axis 2 — where the UI lives

**Option W — All screen-space.** Everything on a `CanvasLayer` over the 3D view.
Most readable, easiest to test — but fights `04` §8's "actions appear around the
active actor".

**Option X — Hybrid.** *Recommended.*
- **Stage-anchored (3D):** things belonging to an actor — the ability radial
  around the active fighter, target reticles, the "reaction armed" marker, wound
  and damage callouts.
- **Screen-space (`CanvasLayer`):** things belonging to the player — initiative
  strip, action queue, phase controls, log.

**Option Y — Fully diegetic.** Initiative as a physical turn track on the table
edge, queue as cards laid on the table. Strong tabletop read — but **D3.3 says the
wargaming language belongs to the props, not the UI.** Rejected on that basis.

### 4c. Axis 3 — fidelity sequencing

**Grey-box first** (recommended, and cheap now that D3.2 defers palette work):
prove camera timing with blocks and silhouettes; commission art only once the
Director's beats feel right. The alternative — art first — risks producing assets
timed to choreography that then changes.

---

## 5. Workstreams

Parallelisable. The dependency notes are the important part.

### WS-A — The stage (3D space, cutouts, representational props)
*No dependencies.*
- **A1** Scene restructure: `Node3D` root, `CanvasLayer` UI, `Camera3D` rig. Keep
  the project rule — scene files stay stubs, the tree is built in `_ready()`.
- **A2** Cutout actor: billboarded quad on a visible base. Pose = texture swap.
- **A3** Prop kit (D3.3): flat-shaded low-poly ground plate plus a
  bridge / wall / crate / lantern vocabulary. Representational, not modelled.
- **A4** Wargaming look-dev: key light, soft contact shadow onto the table,
  tilt-shift depth of field, desaturation with depth. *The base discs and the
  tilt-shift carry most of the "miniatures" read.*
- **A5** Staging marks: named `Marker3D`s (attacker, defender, centre, flank) that
  shot profiles aim at, so no camera work hardcodes a position.

### WS-B — The Director ("a thunk") — **critical path**
*Everything visual depends on this.*
- **B1 Beat queue.** The engine resolves a step synchronously and emits several
  `log_line`s. The Director captures them into an ordered beat list and plays them
  back on a clock. **This is the core architectural addition; none of the
  cinematic work functions without it.** The art documents describe states and
  moods but never this transport layer.
- **B2 Beat types** — `stage`, `cut`, `pose`, `impact`, `consequence`, `settle` —
  each with duration and camera intent, so timing is data rather than code.
- **B3 Camera rig:** named marks → `Tween` on the `Camera3D` transform. A thunk is
  a short ease-out move (~200ms) plus a settle; hit-stop on impact; a hard cut
  where the shot profile asks for one.
- **B4 Rework `state_changed`.** Today every emission rebuilds every component
  wholesale (the port mirrored the JS `innerHTML` model). That destroys any
  in-flight tween. Components must separate **structure** (built once) from
  **values** (updated in place). **Prerequisite, not polish** — and the largest
  refactor of existing Phase 2 code.
- **B5** Redefine controls: `Step` = one beat; `Play all` = auto-advance the queue
  on the clock, not 40 instant iterations.
- **B6** Motion-comfort setting (`04` §14): reduce or disable camera movement.
  Cheap now, expensive to retrofit.

### WS-C — UI reconfiguration
*Depends on B4. Shape depends on the Axis-1 choice and on `06`.*
- **C1 Exception-based conditions (D3.4).** The data already supports this:
  every condition carries a `baseline`, and `conditions.json` carries
  `tipping_threshold: 4`. Rule: at baseline → **render nothing**; off baseline →
  small chip; `|v − baseline| ≥ 4` → signposted, with a matching change on the
  stage. Today the strip always draws all six and ghosts the inactive ones — the
  exact noise D3.4 objects to. In the current scene this collapses six readouts to
  two: `weather +3` (prominent, approaching tipping) and `footing −1` (minor);
  `light`, `noise`, `alert`, `time_of_day` disappear entirely.
- **C2** Radial / fan selector — root ring Body/Mind/Spirit/Reaction, second ring
  the loaded techniques. Two levels maximum; collapses after every confirm (that
  collapse is what makes each selection a discrete thunk). Feeds the existing
  `Duel.on_card_click()`; no engine change.
- **C3** Contextual tooltip replacing the card face: name, cost, initiative
  consequence, primary effect, 2–4 tags, lock reason. `Derive.status()` already
  returns the lock reason as `why`.
- **C4** Thin persistent layer only: initiative strip, compact reserves, action
  queue, phase/confirm.
- **C5** Initiative projection (`04` §10a): ghost marker plus connector for the
  projected position while a technique is focused. `InitiativeBar` already draws a
  ghost pip for pending insight; this extends the same idea to hover.
- **C6** Insight as an inspection *state*: selector recedes, opponents become
  directly selectable on the stage.

### WS-D — Presentation data
*Schema depends on B2.*
- **D1** `res://data/shots.json` — `shot_id → {camera_profile, attacker_mark,
  defender_mark, pose_sequence, timing, fx}`. **Gameplay JSON untouched**
  (`04` §16), so the golden test keeps guarding it.
- **D2** Reconcile vocabularies. The ability data uses **12** shot ids —
  `strike_close`, `finisher`, `lunge`, `brace`, `approach`, `observe`, `feint`,
  `glare`, `cast_ranged`, `sidestep`, `throw`, `block`. `04` §3 proposes **10**
  different profile names (`establish`, `close_attacker`, `side_melee`,
  `low_heavy`, `rush`, `reaction_reverse`, …). **Map, do not rename** — the
  ability data stays as authored and `shots.json` translates.
- **D3** Pose families (`04` §6): 6–8 families, not 17 bespoke sets.
- **D4** Reaction signature. A perfect counter should be the loudest recurring
  audiovisual event in the game (`04` §11). The engine already emits a distinct
  `"negated · initiative reverses …"` line for the Director to key a
  screen-direction reversal off.

### WS-E — Art assets
*Blocked on A4 look-dev.* Placeholder-first per §4c.

### WS-F — Keeping it honest
- **F1** `run_golden.gd` green at every commit.
- **F2** Rewrite `run_ui_smoke.gd` once C2 lands.
- **F3** New headless Director test: assert a beat queue drains and lands on the
  expected camera mark. No rendering required.

---

## 6. Sequencing

Build the thunk before the stage. The stage is the appealing part; the Director is
the part that can fail.

| Phase | Contents | Done when |
|---|---|---|
| **2R.0** | Choose Axis 1/2/3; rewrite `CLAUDE.md` Phase 2; roster façade if Option 4 | Golden still byte-identical after the façade |
| **2R.1** | A1, A2 (grey), A5, B1–B3, B5 | **One ability resolves as a directed beat:** camera thunks to a mark, cutout swaps pose, impact lands, camera settles. Ugly is acceptable. |
| **2R.2** | B4, C4, C1 | Tweens survive a `state_changed`; conditions signpost by exception |
| **2R.3** | C2, C3, C5 | Duel playable via radial; hand and drawers deleted |
| **2R.4** | D1, D2, D3 | All 12 shot ids drive distinct camera behaviour, from data |
| **2R.5** | A3, A4, E | Reads as tabletop wargaming in a screenshot |
| **2R.6** | D4, C6, B6 | Perfect counter unmistakable; Insight is a state; motion toggle exists |

---

## 7. Main-branch handoff

**Decisions proposed**
- `CLAUDE.md` Phase 2 is superseded and needs rewriting before further UI work.
- Presentation data lives in its own `shots.json`; gameplay schema untouched.
- The Director (beat queue) is a new architectural layer, not a UI component.

**Existing design affected**
- `01-design-bible.md` §11 Presentation — "static pose images swapped per shot
  type" understates the target; the Director and shot library belong there.
- `00-project-steer.md` §5 MVP boundary — cutaway stage description.

**Questions requiring project-owner decision**
- ~~Axis 1/2/3~~ — **answered, D3.8.** The camera thunks during DECLARE too, which
  widens WS-B: the Director needs selection beats as well as resolution beats.
- **Open, new:** how a world-anchored radial behaves while the camera is moving
  (settle-then-open, or screen-lock while open). Falls out of D3.8 items 3 + 4.
- Initiative model under many-vs-many — see `06-multi-actor-combat.md` §3.

**Safe to prototype without decision**
- Grey-box stage, cutout billboards, base discs, tilt-shift look-dev.
- Beat queue and camera rig against the current 1v1 engine.
- Exception-based condition rendering (C1) — pure data read, no rule change.
