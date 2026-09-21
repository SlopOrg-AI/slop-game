# Combat & Scene Design — Decisions Log

**Updated 2026-09-20 (session 4).** Chronological decision record with rationale. When a decision is reversed, the old entry stays and is marked **SUPERSEDED →** with a pointer. The consolidated current state lives in `01-design-bible.md`; if the two disagree, the later-dated entry here wins and the bible gets corrected.

---

# Session 4 — 2026-09-20

## D4.1 Godot port abandoned; next attempt starts clean
One day into the port (5 commits: scaffold → data move → engine port + golden test → UI layout A → 3D stage/Director/roster façade), owner judged combat design not yet human-validated and the port was already compounding scope without review — see D4.3. `Godot/shinobi-master/` is archived in place (`ARCHIVED.md` inside); git history (5 commits) kept as reference only. **The next Godot attempt does not resume this codebase** — it starts clean once combat is human-playtested and art direction is settled.
*Rationale:* owner call, 2026-09-20.

## D4.2 Simulation-driven tuning paused; human playtest leads
AI-vs-AI auto-play findings (`prototype-findings-01.md`, `prototype-findings-02.md`) and the D3.1–D3.4 tuning fixes they produced are **not discredited** — the reasoning in each still looks sound — but simulation is no longer what drives design priority. Owner will playtest `combat-1v1-v4.html` directly and flag when simulation is useful again. D3.1–D3.4 stay logged as proposed fixes, still unapplied to `design-data`/`res://data`, now pending human play rather than pending a Godot golden-test (that gate no longer exists — D4.1).
*Rationale:* owner judged auto-play-derived tuning a rabbit hole. The actual design thesis (bible §1, "information is a resource") requires a human reading an opponent — an AI policy queuing the first affordable card every round can't exercise that loop.

## D4.3 Divergent doc thread discovered and parked
A second "session 3" existed only on disk (`C:\Claude\docs\`), never synced to this Project: a presentation rework (3D camera, cutout staging, a cinematic Director/beat-queue, exception-based condition UI) and a multi-actor combat expansion (teams of three, up to 3×3 allied teams, logged as **"CANON DIRECTION, owner"**) — recorded in `05-combat-presentation-plan.md`, `06-multi-actor-combat.md`, and a competing **D3.1–D3.8 in the disk copy of this file, same numbers as the real D3.1–D3.4 above, different content.**

Its cited source material — `00-art-lore-steer.md`, `02-vision-board.md`, `04-art-direction.md`, described as "art-branch agent output" — does not exist anywhere in the connected folder. Git history for the Godot repo shows one branch, no worktrees, no commit ever touching those filenames. Treated as unrecoverable.

Relabelled **D3.1p–D3.8p** (see Session 3B below) to stop colliding with the real D3.1–D3.4. Marked **PARKED — not canon.** `duel/engine/*` (the headless engine, golden-tested) is unaffected either way and is preserved with the archived repo (D4.1).

**Open, unresolved by this session:** whether D3.6/D3.6p (many-vs-many as "canon direction") reflects an actual instruction from the owner in a session/window this investigation couldn't see, or is scope self-attributed by an unsupervised run. **Reverted to the original MVP boundary** (party combat = OUT/FUTURE, `00-project-steer.md` §5) pending owner confirmation either way.

## D4.4 Art direction: image-gen replaces HTML-as-visual-spec
The HTML wireframe (`combat-1v1-v4.html`) stays the mechanics testbed (D2.1) — that part worked, it's what surfaced Findings 1–4. What didn't work: treating its DOM as the *visual* spec for Godot (D3.7p). Going forward, visual direction — character/pose art first, then cutaway-shot style, then UI skin — is explored through image generation, owner-run: owner generates, Claude reacts and iterates on prompts against the bible's Reference touchstones. No image-gen tool is connected in this session.
*Rationale:* owner call, 2026-09-20.

## D4.5 Multi-actor combat (N vs M) confirmed as real design direction
Owner confirmed 2026-09-20: yes — 3v3 team combat, and N-vs-M generally, is real intent, not an artifact of an unsupervised run. D3.6p below is **un-parked** and restated as canon design direction: teams of three as the normal shape, multiple allied teams against a larger force as the stretch case (`06-multi-actor-combat.md` §1, now un-parked).

**Confirmed as TARGET, not MVP.** The MVP vertical slice stays one 1v1 duel (S1.§0 — unchanged, still current); multi-actor is what the design builds toward *after*. What was actually wrong in the D3.6p episode was never the content — it's that it landed only on disk, unsynced, mid an unreviewed multi-phase Godot push (D4.1). The content itself checks out.

The hard open question is unaffected and still blocking: **a single shared initiative bar cannot represent three-plus sides** (`06-multi-actor-combat.md` §3 — per-actor / per-side / pairwise bar, none chosen). That's real design work for whenever this is picked up, not implementation detail to defer to an engine session.
*Rationale:* owner confirmation, 2026-09-20.

---

# Session 3B — 2026-09-19 (evening, presentation/scope thread)

> **Status as of 2026-09-20:** this surfaced only on disk, never synced to the Project, numbered as a competing "session 3" against the real D3.1–D3.4 above (see D4.3). The **multi-actor combat requirement (D3.6p) is confirmed and un-parked** — see D4.5. Everything else here — the 3D-camera/cutout/Director presentation rework and the specific Godot UI-execution choices — **stays parked**: it was scoped against the now-archived Godot port (D4.1) and needs redoing against whatever exists whenever art direction and an engine restart both happen. Full text lives in `05-combat-presentation-plan.md` (parked) and `06-multi-actor-combat.md` (un-parked, confirmed) — both added to this Project. Summary table below.

| # | Decision | Status |
|---|---|---|
| D3.1p | Presentation = 3D camera, 2D cutouts, representational props | Parked — Godot-specific, archived with the port |
| D3.2p | Palette stays "ink over paper"; noir revision deferred | Parked |
| D3.3p | "Tabletop wargaming" language applies to props, not UI/UX | Parked |
| D3.4p | Exception-based condition disclosure (baseline → render nothing) | Parked |
| D3.5p | "A thunk" — every click is a directed camera beat | Parked — requires a Director layer that doesn't exist anywhere now |
| D3.6p | Combat scales to many-vs-many, teams of 3, up to 3×3 allied | **Confirmed, un-parked — see D4.5.** Design direction stands; engine/UI work against it is still all ahead |
| D3.7p | Godot Phase 2 (wireframe layout A) declared superseded same day it was built | Moot — Godot archived (D4.1) |
| D3.8p | UI rework approach: parallel stage scene + roster façade + hybrid 3D/screen-space UI + thunk on every click | Parked — Godot-specific |

---

# Session 3 — 2026-09-19 (night)

## D3.1 Damage scales with attacker Strength
Ability damage `amount` (§9.2) is a base value; at resolve it's scaled by `attacker.strength / 100` before the guard subtracts (§8.1). 100 = the "competent professional" anchor (§3.3), so an authored amount is exact at Strength 100. Fixes `prototype-findings-02.md` Finding 1 (Toughness 26 zeroing most hits) without flattening guards — same-tier duels stay balanced (both sides' guard and damage scale with tier), and a weak attacker still can't crack a strong defender's guard (outscaling preserved).
*Rejected: flat guard-baseline nerf — would also let weak attackers chip legendary defenders, undermining the outscaling the user explicitly wants kept.*
**Not yet applied to `design-data/`** — pending human playtest confirmation (D4.2), not a Godot golden-test (D4.1).

## D3.2 Insight capped and drained on reaction fire
Insight caps at `Wits / 2`; when an armed reaction fires (either grade), the holder's Insight drops to ~25% of its pre-fire value. Fixes Finding 2 (uncapped Insight made a 1-predicate reaction perfect every round, pinning the bar) — a cap alone would've just delayed the same problem once hit.
**Follow-on, not built:** reveal-spend feeding directly into next-ARM reaction precision (revealing an opponent's hidden ability lets you arm a narrower, better-grading reaction), so reveal competes with shove/grade-boost as a genuine third use of Insight instead of being mechanically the weakest option. Queued as an experiment once there's a build to test it in — no play data yet.
**Not yet applied to `design-data/`.**

## D3.3 Perfect-counter reversal = ability delta only
Drops the flat +10 from the reversal formula. Example: Shoulder Charge (`initiative: +17`) countered perfectly now reverses the bar by 17, not 27 (delta + 10). Fixes Finding 3 — the flat bonus was double-dipping with the delta and pinning the ±50 bar in one action.
**Not yet applied to `design-data/`.**

## D3.4 Reaction's held reserve excludes itself from refill while armed
Confirms existing bible language (§3.4/§7: "holding a trap is a standing cost") against Finding 4, where the v4 prototype's 100% Focus refill was silently no-selling that cost. Not a new rule — closes a doc/engine gap.
**Open sub-question before this is purely a data fix:** does the *JS reference engine itself* already have the refill-while-armed bug, or would only the Godot port introduce it? Moot for now — no Godot port in flight (D4.1). Resolve when the JS engine is next touched.

## Open after session 3
0. Confirm D2.13 trick-taking interleave — unchanged, open.
2. Wound regions — confirm the six. Unchanged, open.
3. Reaction slots — dedicated vs competing. Unchanged, open.
5. UI number display — raw vs bands. Unchanged, open.
6. Whether Mind needs a tested attribute beyond Wits. Unchanged, open.

~~1. Insight → reaction grade~~ — RESOLVED, see D3.2.
~~4. Guards vs damage calibration~~ — RESOLVED, see D3.1.
**New, resolved this session:** reversal size (D3.3) · reaction refill exclusion (D3.4, pending the JS-engine check above).

**Note (2026-09-20):** all of the above is now gated on human playtest (D4.2), not simulation or a Godot build.

---

# Session 2 — 2026-09-19 (afternoon)

## D2.1 Working method: wireframe → scope → Godot
Iterate HTML wireframes of the 1v1 screen with *holistic* elements (including future systems) until scope is clear; then pull **only MVP-tagged** elements into Godot. Stat/ability design runs concurrently.
*Rationale:* wireframes are cheap and disposable; Godot time is not.

## D2.2 Sim results demoted to historical
The Python sim (`shinobi-prototype/`) and *Prototype Findings #1* are **not canonical**. Its stat model is superseded (D2.3). Its JSON schema shapes remain a useful starting point.
*Rationale:* user judged the sim premature; design was still moving under it.

## D2.3 Stat model v2 — four classes
- **Attributes** (tested, never spent, lowered only by wounds): Strength, Quickness, **Wits, Courage, Heart**.
- **Reserves** (spent, refill per round as % of max): Stamina **40%** (30–50), Focus **100%** unless hindered, Chakra **30%** (25–33).
- **Meters** (start 0, built, tapped): Insight (hidden, per character), Initiative (shared).
- **Guards** (absorb damage by type): Toughness = physical, Grit = mental, Will = spiritual.
- Scale 0–300+ (~100 competent, ~150 elite, 200+ legendary), irregular values via traits. Guards small-scale.
- Plain names kept; flavour lives in ability/wound names.
- **SUPERSEDES** S1.§5 (wits/insight/courage as spend-regen pools; grit=metal soak; stamina as fungible *currency* remains).

## D2.4 Heart added; Will re-purposed
Heart = *what you're willing to give*: gates demeanor stances (berserk, cold resolve) [TARGET], scales emotional commitment amplification. Courage = *what you can take*: break line, offsets back-foot penalty. Will is now the spiritual **guard**, not a pool.

## D2.5 Damage = one channel + a reactive tag stack
Channel (physical / mental / spiritual) picks the guard. Everything else a hit *is* — form (blunt, piercing…), element (fire, water, lightning…), effect (stagger, bleed, burn…), intent (feint, read…) — is a **tag**, and tags overlap. Every tag can be matched by guards, states, conditions, wounds and reactions; effect and element tags impose statuses. Bible §3.2a. *(Revised same day from "elements are amplify tags only".)*

## D2.6 Insight = hidden initiative modifier
Starts at 0 per scene; built by reads/probes/feints/absorbing hits (scaled by Wits). **Spent partially, any amount**: (1) shift *effective* initiative by the amount spent — the reveal that turns the tables; (2) small spends reveal opponent info. Also shifts reaction grade. AI does the same to the player. Early rounds should be Insight-generating.
*Rationale:* "just when they thought they knew, the counter came." Meter, not pool, gives the fight a build → strike rhythm.

## D2.7 Action budget = the reserves
No fixed action count, no tick budget. Every ability costs some mix of Focus/Stamina/Chakra; queue until you can't afford the next. Focus at 100% refill is the de-facto per-round attention budget; hindering Focus is the universal tempo lever.
**SUPERSEDES** S1.§7 `actions_per_round = 2` and ChatGPT's time-cost budget.

## D2.8 Initiative discount dropped
Spending initiative for cost discounts is removed. Reach gate (−2) and zones (Dominant ≥+5, Desperate ≤−5) stay. Insight is the spend mechanism now.
**SUPERSEDES** S1.§6 job 2.

## D2.9 Anatomical injuries in MVP
No HP. Typed damage → guard → severity band → named wound with stat effects. Regions proposed: head, torso, arms, legs, mind, spirit. ~12 wounds authored for MVP.
**SUPERSEDES** S1.§5 percentile threshold damage.

## D2.10 Docs restructured
`00-project-steer.md` (read first) · `01-design-bible.md` (source of truth, MVP/TARGET/FUTURE tags) · this log · `prototype-findings-01.md` (historical) · `source-chatgpt-status-2026-09.md` (provenance).

## D2.11 "No dice" relaxed → bounded, opt-in variance
Player decisions keep primary weight, but some abilities may carry a magnitude band so a lucky hit can tip a threshold (initiative zone, attribute below an ability's `requires` → "dropped guard"). Downside mitigable via Insight/Wits/Courage. Mechanism **OPEN** — see bible §1a for the proposed shape and alternatives.
**SUPERSEDES** the "no dice anywhere" north star (S1 / bible §1).

## D2.12 Initiative on a 100-pt bar
−50 … +50, centred on 0. Reach −10 · Dominant ≥ +25 · Desperate ≤ −25. Ability initiative deltas use the same irregular, roughly-normal principle as attributes (±3–9 ordinary, ±11–15 big, 20+ for reveals/perfect counters). Insight converts at 2:1. **SUPERSEDES** S1.§6 range.

## D2.13 Resolution order = trick-taking by requirement sum [interpretation — confirm]
Each queued ability is ranked by the **sum of its `requires`** (Lightning Palm = Wits 75 + Qck 70 = 145). Each side's highest is its **lead**. The higher lead resolves first; sides then alternate, each playing in descending requirement order. Tie → initiative holder, then Quickness. Consequence: the heaviest commitments resolve first and are the most exposed to armed reactions. Initiative no longer decides order — it decides reach, zones and what Insight can flip.
**SUPERSEDES** "initiative order" in S1.§7 and bible §6. *"Defines order" read as the interleave above — correct if wrong.*

## D2.14 Insight usable at any moment of selection or impact
Commit (partial) during Declare, during Arm, **and as an interrupt before any incoming action lands** — the shift applies before reach, zone and reaction grade are checked. AI gets the same interrupts. **Closes OPEN #1.**

## D2.15 Variance = per-ability band rolled at Resolve (prototype default)
Only abilities with `variance` roll (Lightning Palm 0.8–1.4, Shoulder Charge 0.8–1.3). Log shows the roll. Other mechanisms in §1a remain candidates. **Closes OPEN #0 for now.**

## Open after session 2
0. ~~Variance mechanism~~ → D2.15 (per-ability band; revisit after play).
1. ~~Insight reveal timing~~ → D2.14.
2. Wound regions — confirm the six.
3. Reaction slots — dedicated vs competing.
4. ~~Initiative tie at 0~~ → D2.13 (order no longer initiative-driven; lead-sum tie → initiative holder, then Quickness).
5. UI number display — raw vs bands.
6. Whether Mind needs a tested attribute beyond Wits.
7. **Trick-taking interleave** — confirm D2.13 reading of "defines order".
8. ~~Reaction grade via Insight differential~~ → D3.2, session 3.
9. ~~Guards vs damage calibration~~ → D3.1, session 3.

---

# Session 1 — 2026-09-19 (morning)

## S1.§0 MVP vertical slice
**One 1v1 duel. Nothing else.** Full resource, initiative, reaction, and counter systems. Condition system built, thin data. No location node map, overworld, progression, party.
*Reverses an earlier decision that put Location/Scene/Conditions inside the MVP. The systems are still designed in full — only authored content is cut.* **Still current.**

## S1.§1 Structural tiers
1. Campaign/overworld — 3D worldmap, Mount & Blade travel. 2. Location — Slay-the-Spire node map of Scenes; carries persistent Conditions. 3. Scene — the encounter unit; one runner for every type. **Still current.**

## S1.§2 Scene model
Participants `agent` | `passive`. Objectives composable over `eliminate, survive N, reach, acquire, evade, protect` with AND/OR; separate win/fail clauses. Encounter types: passive-only · 1v1 duel (MVP) · escalating threat. Fail forward; retreat allowed. 1 PC, no party. **Still current.**

## S1.§3 Conditions — two systems
3a Scene conditions (numeric): light, noise, alert, footing, weather, time_of_day; ±1 normal, +4 tipping. 3b Actor states (tags + duration): wet, staggered, exposed, focused. 3c Escalation: tick rates, cascades (weather→footing; noise≥4→alert), scripted beats; clamps; cascade depth ≤2. 3d Abilities declare gate / cost / amplify. **Still current** (MVP authors footing + light).

## S1.§4 Abilities & loadout
One pool tagged for context; loadout pre-scene into typed slots; power axes = slot count × ability quality; ≤50% moveset overlap at high end. **Still current.** Reaction-slot question still open.

## S1.§5 Resources — **SUPERSEDED → D2.3, D2.5, D2.9**
Was: spend/regen stamina, wits, insight, chakra, courage; thresholds strength, quickness; soaks grit (metal), toughness (physical), heart (spirit); percentile threshold damage (~4%/point).

## S1.§6 Initiative
Single bar −10…+10; reach gate −2; zones Dominant ≥+5 (×1.25), Desperate ≤−5 (partial→perfect). **Still current.** Job 2 "spend for discounts" — **SUPERSEDED → D2.8**.

## S1.§7 Round structure
DECLARE (queues visible) → ARM (one hidden reaction) → RESOLVE (initiative order). No dice. **Still current.** `actions_per_round = 2` — **SUPERSEDED → D2.7**. Tie-at-0 rule still open.

## S1.§8 Reactions
Persistent once armed; one at a time; graded by trigger specificity (narrow → perfect, broad → partial; Insight/focused/desperate upgrade); scales with attacker commitment. **Still current.**

## S1.§9 Win conditions
Per scene: kill (rare) · stamina floor · strength/quickness to zero · courage break. **Still current**, restated in bible §8.6 as courage break · incapacitation · surrender · kill.
