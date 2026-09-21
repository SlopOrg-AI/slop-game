> **CONFIRMED 2026-09-20 (D4.5).** This doc surfaced only on disk, unsynced to the Project, and its central claim was flagged unconfirmed on discovery — see `combat-scene-decisions.md` D4.3. Owner has since confirmed directly: N-vs-M combat, teams of three default, up to 3×3 allied, **is real direction.** Un-parked. Status below stands as written.
>
> **Still true and unchanged by that confirmation:** this is TARGET, not MVP — the MVP stays one 1v1 duel (`00-project-steer.md` §5, S1.§0). The engine audit in §2 below refers to the Godot port, which is archived (D4.1) — a future Godot attempt needs to redo that audit against whatever code exists then. §3's initiative-model question is still open and is the actual next design task here.

# 06 — Multi-Actor Combat (many vs many)

**Status:** CANON DIRECTION (owner, session 3) · mechanism OPEN
**Updated:** 2026-09-19 (session 3)

> Combat must scale beyond the 1v1 duel. Recorded as D3.6. This document states
> the requirement, audits what the current engine assumes, and lays out the design
> questions that must be answered before the engine can grow. It does **not**
> decide them — several are combat-design calls (`01-design-bible.md`), not
> implementation details.

---

## 1. The requirement

From the project owner:

> The engine needs to be flexible to many vs many. Teams of three normally, and
> even three teams of three operating as allies, against many.

Read as three capabilities, in increasing order of difficulty:

| Level | Shape | Notes |
|---|---|---|
| **M1** | 1 v 1 | Current. Golden-tested. |
| **M2** | N v N, two sides | Teams of three is the expected default |
| **M3** | Multiple teams, alliance-aware | Three teams of three as allies vs a larger force; "team" and "side" stop being the same thing |

M3 is the one that breaks assumptions. It means an actor's *team* (who they train,
travel and take orders with) is distinct from their *side* in this scene (who they
are currently fighting alongside), and alliances are a scene property.

---

## 2. What the current engine assumes

Audited 2026-09-19 against the Phase 1 port.

**Good news: the assumption is concentrated.** Occurrences of `you` / `opp` /
`other()`:

| File | Count | Comment |
|---|---|---|
| `Duel.gd` | 63 | The state machine — all of it |
| `AI.gd` | 1 | `arm()` reading the single opponent's queue |
| `Resolver.gd` | 0 | Already actor-agnostic: `deal_damage(duel, att, def, …)` |
| `Derive.gd` | 0 | Already actor-agnostic: `derive(a)`, `budget(a)`, `status(duel, a, …)` |
| `Actor.gd`, `Rng.gd`, `JsNum.gd` | 0 | Unaffected |

`Resolver` and `Derive` — the damage pipeline and the rules reads, i.e. the parts
most expensive to get wrong — already take explicit attacker/defender arguments
and carry no notion of sides. **The whole 1v1 assumption lives in `Duel.gd`.**
That is much better than it could have been.

### The specific baked-in assumptions

1. `var you: Actor` / `var opp: Actor` — two named slots, not a roster.
2. `other(a)` returns *the* opponent. Every damage, reaction and AI call routes
   through it. Under M2/M3 this must become `enemies_of(a) -> Array[Actor]` and
   every call site must then **choose**.
3. `init_v: float` — a **single shared scalar**, read as `+` for you and `−` for
   them (`init_for(a)`). See §3: this cannot represent three sides.
4. `build_order()` interleaves exactly two ranked lists (leader[i], follower[i]).
   Needs an N-way rule.
5. `check_end()` iterates `[you, opp]` and sets a single loser. Needs per-actor
   defeat, per-team defeat, and scene win conditions over sides.
6. Reactions: `def.armed` fires against whoever attacks. The trigger matching
   itself is target-agnostic and probably survives unchanged — worth confirming.
7. **Abilities carry no target field.** `abilities.json` mentions `target` only
   twice, both as `amplify.on: "target"` (an amplification scope, not a chosen
   victim). Damage currently always lands on `other(att)`.

### Consequence: targeting becomes a real system

This is the largest design gap, not merely the largest refactor. Under M2/M3 the
player must choose *who* each queued action hits, which adds a step to DECLARE,
changes the ability schema, changes the AI, and changes the UI. It is the reason
`05-combat-presentation-plan.md` §4a recommends building the UI against an N-actor
façade now rather than building it twice.

---

## 3. The hard question — initiative under many-vs-many

**A single shared −50…+50 bar cannot represent three sides.** Bible §4 defines
initiative as one tug-of-war between two poles, and both reach (§4 Job 1) and the
dominant/desperate zones (Job 2) are read off an actor's signed position on it.
With three or more mutually hostile groups there is no single axis.

This blocks the engine work. Three candidate models, none yet chosen:

**Model A — per-actor initiative.** Each actor holds their own scalar. Reach and
zones read from it directly; ability deltas move the actor's own value and
optionally push others'.
- *For:* simplest to reason about; scales to any count; reach/zones keep working.
- *Against:* loses the tug-of-war — the bar stops being a shared object that one
  side wins. That is a core identity of the combat design (bible §4, D2.12).

**Model B — per-side bar.** One bar per hostile side, measured against the field.
- *For:* preserves the tug-of-war feel within a side.
- *Against:* "the field" needs defining; awkward when alliances shift mid-scene
  (M3); unclear what an actor's personal reach reads from.

**Model C — pairwise engagement bars.** A bar exists per engaged pair.
- *For:* most faithful to the duel fiction; reach is naturally per-opponent.
- *Against:* combinatorial; hard to display; unclear how a third party
  intervening in a pair's bar works.

**Recommendation: none yet — this is an owner/design decision, not an engineering
one.** Model A is the cheapest to implement and the most damaging to the existing
design identity, which is exactly the kind of trade that should not be made by
default.

---

## 4. Other open design questions

1. **Team vs side.** Is alliance a fixed scene property, or can it change
   mid-fight (betrayal is very much in this game's emotional target)?
2. **Trick-taking order across N sides.** D2.13 ranks each side's queue by
   requirement sum and interleaves two lists. What is the N-way rule, and who
   leads?
3. **Action budget.** Unchanged per actor (D2.7), but does a team share anything?
4. **Reactions.** One armed per actor still, or per team? Can an ally's reaction
   fire in defence of a teammate? (This is a strong fantasy and worth considering.)
5. **Insight.** Per actor (D2.6). Is it readable by allies? Does an ally's read
   help you?
6. **Win/fail conditions.** Per side, per team, or per actor? Bible §8.6 lists
   courage break / incapacitation / surrender / kill for one opponent.
7. **AI.** One policy per actor, or a team-level coordinator choosing targets and
   focus-fire? Focus-fire is the obvious emergent behaviour and may need damping.
8. **Scene scale.** Does the stage (`05` WS-A) need to compose 9+ cutouts
   readably? This feeds the camera and staging-mark design directly.

---

## 5. The regression net

**`tests/golden-seed7-policyA.txt` is the safety line for this work.** Any
many-vs-many refactor must keep reproducing the seed-7 1v1 log byte-identical:
153 lines, empty diff. A 1v1 scene is just the N=2, two-sides case, so if the
generalisation is correct the golden output cannot move.

Its coverage limit should be stated plainly: **the golden test proves the 1v1 path
still works; it proves nothing about N>2.** New scenario fixtures will be needed —
at minimum a 3v3 and a 3×3-allied-vs-many log — generated once the initiative
model (§3) is settled and then frozen the same way.

---

## 6. Sequencing note

This work is **not** a prerequisite for the presentation rework, provided the UI is
written against the roster façade described in `05` §4a Option 4. The façade
(`duel.actors`, `team_of`, `allies_of`, `enemies_of`, `player_team`) can be added
to the current 1v1 engine with no behaviour change — proven by the golden test —
letting the UI and the engine generalisation proceed in parallel.

Doing the engine first (option 3 in `05`) is blocked on §3, which has no answer
yet.

---

## 7. Main-branch handoff

**Decisions proposed**
- Many-vs-many is a design target, not a future nicety (owner, D3.6).
- Targeting becomes an explicit system: ability schema, DECLARE step, AI and UI.
- The golden test is retained as the 1v1 regression net through the refactor.

**Existing design affected**
- `01-design-bible.md` §4 Initiative — the single shared bar is 1v1-only.
- §6 Round structure — trick-taking order is defined for two sides.
- §7 Reactions — "one armed" is per actor; ally interaction undefined.
- §8.6 Win/fail — defined against a single opponent.
- §9.2 Ability schema — no target field exists.
- `00-project-steer.md` §5 MVP boundary — "one 1v1 duel" remains the MVP; this
  document describes what comes after, and what not to paint into a corner.

**Canon dependencies**
- Spacing remains abstract; no tactical grid (`00-art-lore-steer` §9b).
- Insight remains hidden and per actor (D2.6).
- Initiative remains persistent and tactically central (D2.12) — which is exactly
  what makes §3 hard.

**Questions requiring project-owner decision**
- §3 initiative model. **Blocking.**
- §4.1 whether alliances can change mid-scene.
- §4.4 whether reactions can defend an ally.

**Safe to build without decision**
- The roster façade over the existing 1v1 engine (§6).
- UI written against that façade (`05` §4a Option 4).
