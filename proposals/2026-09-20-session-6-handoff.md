# Session 6 handoff — 2026-09-20 (Cowork → successor agent)

**Produced by:** Claude (Cowork), end of session · **Status:** `PROPOSED` inbox document. Nothing here is canon until the owner logs D-numbers. **Read this before touching `design/10`–`14`, `data/`, or `demo/`** — the session reconsidered several v1/v2 combat foundations and the stubs must not be distilled from the v1 bible as-is.

Companion files from this session (all `proposals/`, all PROPOSED):
- `2026-09-20-successor-review.md` — state audit + first sequence proposal. **Sequence superseded by §6 below**; audit and inconsistency list still valid.
- `2026-09-20-ontology-draft.md` — attribute hierarchy, tag families, dictionary verbs, naming schema. **§2 (levels A–D) superseded by sheets + pools (§3.2 here)**; the rest stands.

---

## 1. What happened this session

1. Audit of `shinobi-v2/` (see successor-review §1–2). Key facts: 5/14 design docs written, 10–14 are stubs, D1–D4 not compressed, JSON on v1 schema, **git not initialised**, stale `design/12-reactions-insight.md` present, Project mirror in sync.
2. Owner answered the first decision set: **no HTML play** (wait for Godot M1) · **schema v3 before M1, with refinement** · **agent edits `design/` directly in-session** on owner instruction.
3. A long design conversation followed. The owner steered; the agent elaborated. §2 separates the two.

## 1b. Parallel session, same day — reconcile first

A second Cowork session ("Session 6 — inspiration index") wrote to the folder while this one ran. State at handoff time:
- `decisions.md` now has **D5.16–D5.23** (ukiyo-e, UI as animate paper, animatic register, Paper Mario sharpen, Black Company, Malazan, Malazan earmark for a magic/spirit-resource pass, **Rogue Trader as precedent for the initiative bar's threshold move tiers**). `01-pillars.md` updated to match.
- **D5.24 (engagement-scoped initiative; concurrent engagements, scene bleed at end of round) is cited in `11-initiative.md`, `14-scenes-conditions.md` and `00-steer.md` §6 but is NOT logged in `decisions.md`.** By rule 2 it is not yet decided. Owner or that session should log it or strip the citations.
- New on disk: `proposals/2026-09-20-inspiration-index.md`, `proposals/art/2026-09-20-smoketest/` (Qwen image-gen smoke tests, `style-card.md`), ComfyUI workflow JSONs under `proposals/art/`, and `tools/annotate/` (local board annotator, port 8189). **The image-gen loop is running on the 5090** — this handoff's "parallel track" is already live.
- Numbering: this document's candidates are **C1–C19 → next free D-number is D5.25** (D5.24 pending).

Interactions with this session's content:
- **D5.23 (Rogue Trader)** affirms a *single shared* tug-of-war meter with tiered moves at Dominant/Desperate. That is direct precedent for **Push (C18)** — Heroic Acts / Desperate Measures — and it weighs on the momentum decision (§5 #1): the owner's affirmed spirit is a shared meter, so option (1) "keep the bar, pressure only, reach removed" is closer to D5.23 than the agent's lean to (3). Present both; do not pre-decide.
- **D5.22 (Malazan earmark)** is the flagged flavour reference for exactly the traditions/reserves pass in §3.8 — and bars it from silently expanding into the MtG ability-kind chassis or the City of Mist tag ontology. §3.8 respects that (reserves and draws, not new kinds or tag semantics); cite D5.22 when writing it up.
- **D5.24 (engagements)** and the spatial model (§3.1) need reconciling: an engagement is probably a *zone-scoped* momentum track. Write them together in `11`.

## 2. Owner direction this session (candidate decisions — owner to promote or reject)

These are the owner's own statements, paraphrased closely. Each is a candidate **D5.25+** entry. The agent did **not** log them (AGENTS rule 4). C-refs are for citation only.

| Ref | Owner direction | Supersedes / touches |
|---|---|---|
| C1 | **Reactions and passives are ordinary abilities** — chosen in Plan with actives, tapping the same resources. The only difference is *how they resolve*. There is no slot question. | Open #3 (closes as a non-question) · `00-steer` §4 "+ reaction" · `characters.json slots.reaction` · `rules.json reactions.max_armed` |
| C2 | **Rock-paper-scissors-like resolution rather than strict trick-taking.** OD&D lineage (different speeds for magic/ranged) is the design space. Example: a speed attack beats a strength block unless the block has a `swift` tag. | D2.13 (demotes to tiebreak at most) · Open #2, #8 |
| C3 | **No ability "modes."** Abilities are a descriptive action or state; tags are descriptors, not categories. | Agent's mode proposal — rejected |
| C4 | **Tags have a dictionary** of how they combine and interact, setting player expectations. Model: **BotW systemic chemistry** — things combine and interact as expected. Infinite Craft was cited for the *scale* of combinatorics, not the shape. | D5.14, D5.15 (extends) |
| C5 | **Environmental destruction and creation are in the rules; a material datatype is needed.** | D5.11, D5.13 (mechanism) · `30`, `50` |
| C6 | **Damage: descriptive tags AND numeric tracking.** Minting still works — when thresholds are hit a new condition is written to the scene in light of overall scene state, following the dictionary. | `13`, D5.14 |
| C7 | **RNG narrowed, not removed.** Ability damage itself is consistent. **Darkest Dungeon model**: abilities do a % of the character's stat. | D2.11, D2.15, Open #1 (narrows) |
| C8 | **Abilities are generic and trained up; 5-star system.** Stars give scaling effects and tags. The PC only intuits a rough idea of an opponent's skill with an ability. | `15` (new fact type) · progression (TARGET) |
| C9 | **Draws are weighted across attributes** (Swift Strike ≈ Quickness-led, some Strength). "Intuitive and systemic." | D3.1 (replaced by draws) |
| C10 | **Draw budget:** a full-scale ability's draws sum to 1. Gold can exceed 1 (second class ≈ +.5); elements ≈ +.25 baseline. **Distribution is fixed at acquisition**, within template limits (e.g. Swift Strike ≥ half swift): some fighters have SWIFT blows, others swift BLOWS. | `abilities.json`, `characters.json` |
| C11 | **Attributes are readable on sight** (rough), become certain quickly once the foe moves; the insightful learn the ceiling; getting hit confirms — **unless the foe is holding back.** | `15` |
| C12 | **Gold abilities** (two classes: body+mind, body+spirit, mind+spirit) are **archetype signposts**, like gold cards in MtG set drafts. | `01` (MtG allocation), loadout/progression |
| C13 | **Range and initiative: drastic reconsideration — the bar-as-reach jars.** Start from tabletop assumptions: **FFG Star Wars RPG** range bands and scale; actors at *relative* range; **plus anchor points on the map** for relative positioning and sectioning space; **Index Card RPG** for room/map design; **shapes outline a scene space.** Fail-forward / success-with-consequence in the spirit of **Blades in the Dark / PbtA.** | Vision paragraph · D2.8, D2.12 (reach on bar) · Open #5 · `11`, `14`, `30`, `31` |
| C14 | **Magic:** variety in schools and sources defined by draws — *sorcery vs wizardry*; Elder Scrolls schools; ninjutsu has a physical component. **Chakra is one reserve option among many.** Blood magic: Strength fills a Blood reserve that is spent for magic actions. | `12`, `15`, `50`; reserves become data |
| C15 | **Reserves are flexible and instantiated** — Gaara's sand shield is a reserve not all characters have. **Sand is a magic reserve in its own right** (like Blood, magicka, devotion/favor). Gaara's sand *converts* (hardened, tagged). | pools model (§3.2) |
| C16 | **Attributes must adjust** if the actor datatype models people *and* places. | D5.11, D5.12 → sheets (§3.2) |
| C17 | **Devotion:** better as an *attribute to check* plus a *reserve to spend* (agent's "devotion = knowledge" rejected). | traditions table |
| C18 | **Major rework to consider: spend attributes explicitly at critical moments to empower an action** — at the point of despair, or when dominating initiative. | new mechanic ("Push", §3.9); Elric pillar |
| C19 | **All game terms are provisional** until the owner says otherwise. Ontology, schema and hierarchy naming conventions are work to do. | `02-ontology.md` (new doc) |
| C20 | **Multiple tug-of-wars, nested: individual, team, and skirmish level.** (Stated at handoff, after reading D5.23/D5.24.) Resolves §5 #1: the shared meter *spirit* (D5.23) is kept, but there is one meter per level, and levels nest. | Open #5 · D5.12 nesting · D5.24 engagements · `11` |

## 3. The model as it stands (agent synthesis — PROPOSED, provisional names)

### 3.1 Entities and space
- `Entity {id, name, tags[], states[], tracks{}?, material?}` is the base of everything a rule can touch. Rules test **tags only**, never the subclass.
- `Scene {scale, parent, children, conditions[], zones[], actors[], objects[]}`; `Zone {shape, anchors[], edges[]}`; `Anchor {name, tags}`; `Edge {to, kind: open|cover|wall|drop, material?}` — edges are entities, created/destroyed by chemistry.
- **Position** = zone + (anchor | open). **Range is derived, never tracked**: same anchor → Engaged; same zone → Short; adjacent → Medium; two steps → Long; else Extreme; edges modify. **Reach is a descriptor** (`melee` needs Engaged; `ranged` carries a max band) read by one rule. Movement = maneuvers that change band/anchor. Same bands at every scale (FFG planetary-scale precedent).

### 3.2 Sheets and pools (replaces ontology-draft §2 levels A–D)
- **Sheet** = per actor kind, maps universal `class.role` keys to named 0–300 attributes. Roles (placeholders): `body.force`, `body.finesse`, `mind.acuity`, `mind.?` (Open #13), `spirit.will`, `spirit.nerve`. Character: Str, Qck, Wits, —, Heart, Courage. Settlement: Population, Infrastructure, Learning, Order, Legitimacy, Cohesion. Engine addresses roles; abilities and rules are meaningful wherever the role exists.
- **Pool** = `{id, class, roles: reserve|guard|meter, max_from[], refill, fill[], pays_for[], consumed_by[], grants[], tell}`. Every actor instantiates its own list. Stamina/Focus/Chakra are common templates, not the definition. Guards and meters are pool roles.
- `max_from` follows the **fill source**: Chakra ← spirit attributes; Blood ← `body.force`; Sand ← the container object's capacity; Favor ← bond tier; a relic ← `const`.
- Exemplar reserves: Chakra (innate refill, = "magicka"), Blood (filled by Str conversion / own wounds; overdraw mints `drained`), **Sand** (filled from scene `sand` tier and carried supply; **is matter** — spending it transitions the material: `hardened`, `packed`, `coffin` objects, reclaimable), Favor (spent for miracles; Devotion is the *attribute*), Momentum (per-actor, pending), Cohesion (team).

### 3.3 Abilities
- **Template** `{id, name, kind, budget, limits{}, stars[], descriptors[], reach, cost, effects}` · **Instance** `{template, owner, draws{}, stars}` — the character's *version*; teachable, inheritable; log notation `swift_strike@kaede`.
- **Kinds (D5.9, C1):** activated · reaction · sustained · decaying · one-off — kind = *when/how it resolves*, nothing else. Iron Guard becomes a sustained `guarding` state; Steel Nerve/Flicker Step already mint self-states.
- **Draws:** `[{source: attribute|reserve|element|scene|object|bond|fact|mark, key, weight}]`. Magnitude = Σ value × weight (DD model, C7/C9). Budget: mono 1.0; +.5 second class; +.25 element. **Stars scale the budget** (★1 .6 → ★5 1.0) and add descriptors at thresholds; distribution fixed at acquisition within `limits`.
- **Gold** ⇔ two classes in draws ⇔ two reserves in cost; lanes: Brute (body), Reader (mind), Resolute (spirit), Duelist (body+mind, signpost Feint), Zealot (body+spirit, Killing Intent), Mystic (mind+spirit, Water Lash). All 17 current abilities placed (see chat table; to be written into `12`/data).
- **Validator rules:** descriptor ⇔ top weight (`swift` ⇒ Quickness leads); instance draws within limits and sum = budget × star fraction; gold ⇔ two classes ⇔ two reserves.

### 3.3b Momentum — nested tug-of-wars (C20; agent elaboration PROPOSED)
- **One shared meter per level, levels nest:** *individual* (each engaged pair — the duel bar, −50…+50, Dominant/Desperate zones, Push gating) · *team* (per engagement: the side-vs-side pressure of a party fight; D5.24's "engagement" is this level) · *skirmish* (per scene: the whole fight, which way the field is going).
- **Propagation is upward as conditions, downward as modifiers** (D5.12 §2 shape): a pair bar reaching Dominant mints a team-level condition (`pressing-1`); team momentum crossing a zone mints a skirmish condition (`routing-2`); skirmish momentum shifts every child bar's thresholds or zone bonuses. Same numbers→thresholds→minted-name discipline as damage.
- **Reach leaves the bar at every level** (C13): distance is zones/anchors/bands; momentum is only pressure.
- **Open #5 becomes tractable:** N-vs-M is not "one bar for three sides" — pairs have pair bars, sides have a team bar, the scene has one. A third party joining a duel opens a new pair bar and joins (or opens) a team bar. Model pairs as *engagements between actors*; group actors carry one bar per opposing group.
- **M1:** individual level only; the meter datatype and threshold/propagation hooks written so team/skirmish are data, not engine work. Reconcile with D5.24 in `11` (engagement = the team-level container).

### 3.4 Resolution
- Round = **Plan → Resolve** (D5.8). All abilities committed hidden, simultaneously.
- **Precedence from descriptors** (C2): `swift` precedes `heavy`; `swift` precedes a `guard` state lacking `swift`; `reach`/ranged before melee; craft/casting last — as dictionary `precedes` entries. Inside a class: momentum holder first, then requirement sum (D2.13 as tiebreak). Cycles → momentum holder. Passives **onset** at their precedence slot; reactions fire on trigger.
- **Outcome tiers from margin, not dice** (C13 spirit): full / success-with-consequence / fail-forward, decided by precedence won or lost and net vs threshold; consequences are minted tags.

### 3.5 Damage (C6, C7)
- Event `{amount, tags, target entity + region}` → resistance (guard pool or material resistance, modified by dictionary: bypass, amplify) → **two numeric outputs**: *states* (tiered tags, decay) and *tracks* (accumulated per region/material, persistent in scene) → threshold crossed → **mint** named wound / material transition, selected by the tags that pushed it over and the scene state → name carries effects.
- Numbers are magnitude, tags are quality, names are the result. Display: names and bands; raw numbers `surface: never` / hover (Open #12).
- Change vs today: `wounds.json` severity bands become thresholds on accumulating tracks (ten minor hits can become a moderate wound).
- **RNG lives in two places only:** which candidate is minted when several are valid (weighted by scene state, surfaced as a band — or deterministic priority; owner to pick), and opt-in per-ability variance (D2.15). No accuracy/crit/dodge rolls.

### 3.6 Chemistry and materials (C4, C5)
- `data/tags.json` = the dictionary. Verbs (fixed, few): `precedes · amplifies · clears · bypasses · mints · gates · converts · transitions`. Pairs are many; unlisted pairs do nothing. Rules attach to **properties** (`burnable`, `conductive`, `brittle`, `fluid`…), applied to whatever carries them — fighter, wound, footing, screen, settlement.
- `data/materials.json`: `{id, properties[], resistance{}, transitions[] (tiered, named: intact → scorched-1 → burning-2 → charred-3 → collapsed), products{} (collapsed → rubble object + unstable footing + dust condition)}`. Creation recipes are `mints` entries producing objects/edges (`earth` × `chakra` → `edge:wall{packed_earth}`). Destruction is creation of something else.
- Propagation in a duel is scene ↔ actor (conditions/cascades); spatial spread arrives with zones/dioramas, same rules.

### 3.7 Information (D5.10 + C8, C11)
- Attributes are facts with tiers: **sighted** (wide band, Str/Qck only) → **observed** (they move: narrow band) → **confirmed** (hit / be hit: exact *effective* value) → **ceiling** (Insight ≥ threshold or studied: true max).
- Star level of an opponent's ability is a fact: unknown → band ("novice/journeyman/master") → identified → exact at studied.
- **Holding back** = self-state `restrained-N`: caps effective attributes; all observations report effective values; only `ceiling` pierces it; dropping it is the reveal beat. Must cost: reduced effect, blocks `heavy`, drops at a moderate wound; sandbagger may build Insight faster. AI gets it.
- Tells follow reserves and traditions (Blood/Sand visible; Focus not; ninjutsu seals readable).

### 3.8 Traditions and schools (C14, C15, C17)
- **Tradition** = reserve × draw profile × tell × how learned: sorcery (Heart/Courage → Chakra, innate) · wizardry (Wits → Focus, learned; stronger vs studied targets) · ninjutsu (body + Wits → Stamina + Chakra; hands/seals required — gold-rate by definition) · blood (Str-filled Blood) · sand (place-fed material reserve) · rite/place · pact/bond (Devotion attribute + Favor reserve).
- **School** = effect verb (Elder Scrolls): destruction (damage) · alteration (states/materials) · illusion (information attacks) · restoration (track/tier reduction) · conjuration (creation) · mysticism (knowledge/Insight). Variety = tradition × school.
- No source above the Y2K ceiling; cassette cyber-funk stays props.

### 3.9 Push (C18) — placeholder name
- At commit, spend X of an attribute the ability draws on; X × k joins the draw. **Gated by momentum zone:** Desperate ≈ 20% cap (the reversal), Dominant ≈ 10% (the press). Attribute drops *now* for the scene and flows through every weight, pool max and guard; recovers between scenes; below a floor mints a lasting wound. Visible; cannot coexist with `restrained` (reveals ceiling). Blood is the farmable formal version; Push is the universal expensive one.
- `rules.json → push: {zones, rate, recovery_per_scene, floor}`; engine change = one term in the draw sum + a strain entry.

## 4. Corrections the owner made — do not re-propose
- "Ability modes" as an authored category — **rejected** (C3).
- "Slots for reactions" — **a false question** (C1).
- "Consequences are minted, not rolled" — **overstated**; RNG is narrowed, not gone (C7).
- Devotion as knowledge — **rejected** (C17).
- `max_from: Heart` for Sand — **wrong**; Sand is its own reserve, sized by its source/container (C15).
- Initiative bar as reach — **jars**; spatial model per C13.
- Strict trick-taking as primary order — **reconsidered** (C2).

## 5. Open decisions — consolidated, ranked by leverage (owner)
1. ~~Momentum model~~ — **answered by C20:** shared meters, one per level (individual · team · skirmish), nested (§3.3b). Remaining sub-questions: does a pair bar exist per *pair* or per *actor-vs-side*; how team momentum is derived (sum of pair bars vs its own accrual); zone names per level.
2. **Zones/anchors/edges in M1** (2–3 zones, 2 anchors, 3 bands, 1 cover edge) or engine-shape only.
3. **Courage's class** — spirit (`spirit.nerve`, with Heart under sorcery) or mind. Settles lanes and Open #13.
4. **Focus** — mind reserve only, or universal attention budget (decides what "gold" means in cost). Agent leans mind-only.
5. **Minting among several candidates** — deterministic priority vs narrow weighted draw surfaced as a band.
6. **Acquisition source for instance distribution** — learner's attribute ratio / teacher's instance / player choice (agent: a+b, c in a training scene).
7. **Push details** — scene-temporary vs permanent by default; zones-only vs anytime at a worse rate; same attribute only vs cross-class (Courage fuelling a Str blow).
8. **M1 content adds** — `restrained` (holding back) · Blood (one fill action, one Blood technique) · Sand Shield fighter · one place-sourced technique · a `Brace` reaction for block comparison · one destructible + one creatable object. Each is data, not engine; each expands the 17.
9. **Lightning Palm** — body+spirit gold, or the one tri-class showpiece.
10. **Family name** for swift/heavy (`tempo` placeholder) and role names (`force/finesse/acuity/will/nerve` placeholders).
11. Carried from `00-steer` §6: variance mechanism (#1, narrowed by C7), wound regions (#4), selector/targeting (#6), title (#7), stack vs inline (#8, likely absorbed by precedence), knowledge ownership (#9), cultures as knowers (#10), minions (#11), UI numbers (#12), Mind attribute (#13).

## 6. Revised sequence (supersedes successor-review §3)

- **A — housekeeping (owner + agent, short):** `git init` + first commit (owner) · log or strip **D5.24** · delete `12-reactions-insight.md` · owner promotes C1–C19 selectively → `decisions.md` **D5.25+** · fix `00-steer` §1 vision (reach/initiative), §4 (+ reaction), §6 (opens).
- **B — `02-ontology.md` + `data/SCHEMA.md`** from the ontology draft as amended by §3.2 here: hierarchy, sheets, pools, tag families (add `role`, `pool_role`, `tradition`, `school`, `range`, `edge`), verbs, naming, PROVISIONAL/LOCKED column. Small iterations; owner reacts per section.
- **C — distill 10 → 11 → 13 → 14 → 12 → 15** against the ontology, *not* the v1 bible alone (keep the D5.24 lines already in `11`/`14` once logged): 10 (Plan→Resolve, precedence, outcome tiers, Push), 11 (momentum + engagements + space: zones/anchors/bands), 13 (event → tracks/states → mint), 14 (scenes, conditions, objects, materials, chemistry), 12 (kinds, gold, stars, instances), 15 (attribute/star facts, holding back). Compress D1–D4 into `decisions.md` alongside. Then 40 (milestones, tool split, image-gen loop) and 31 (component list).
- **D — schema v3** (one D-number): `abilities` (templates/stars/limits) · `characters` (sheet, pools[], instances) · new `sheets`, `pools`, `materials`, `tags`, `scenes` · `wounds` thresholds on tracks · `states` tiered · `rules` (precedence fallback, push, minting policy) · `SCHEMA.md`. Validator script in `data/`.
- **E — Godot M1:** headless engine first, data-driven sheets/pools/tags/materials from commit 1 (never names Strength or Stamina), golden test rewritten for the v2 rules; then loadout → duel (queue, committed abilities, momentum band, wound list, zone sketch, log) → table-view stub. Exit: owner plays 10 duels; findings → `proposals/`.
- **Parallel:** image-gen loop → `proposals/art/`; critique vs pillars; two cut-outs first.

## 6b. Successor — first three sessions, concretely (owner-endorsed at handoff)

**Session 1 — lock the ground (owner present).**
1. Confirm git is initialised (`git log` shows "v2 skeleton" + a "session 6 proposals" commit). If not, stop and ask the owner to run §8.
2. Walk C1–C20 with the owner in order; for each, log `D5.25+` in `decisions.md` (one line: decision · rationale · supersedes · doc) or mark it REJECTED/DEFERRED in this file. Log or strip D5.24. Do not batch-promote — one at a time, owner says the word.
3. Apply the supersessions the promotions imply: `00-steer` §1 vision (initiative → nested momentum, reach → range bands), §4 boundary (stat model → sheets/pools; "+ reaction" gone; trick-taking → precedence; damage → draws/tracks), §6 opens (close #2, #3, #5, #8 as promoted; add the §5 list here).
4. Delete `12-reactions-insight.md`. Commit: "D5.25–D5.xx: session 6b promotions".

**Session 2 — `02-ontology.md` (agent drafts, owner reacts per section).**
- Source: `…-ontology-draft.md` §1, §3–§7 + this file §3.2 (sheets/pools) + §3.3b (momentum levels). Add tag families `role`, `pool_role`, `tradition`, `school`, `range`, `edge`, `level` (individual|team|skirmish). Status column on every term.
- Then `data/SCHEMA.md` derived from it. Commit each.

**Session 3+ — distill against the ontology, one doc per pass, in this order:** `10` → `11` (momentum levels + D5.24 engagements + space) → `13` → `14` (objects, materials, chemistry) → `12` (kinds, gold, stars, instances; the 17-ability lane table) → `15` (attribute/star facts, holding back). Compress D1–D4 into `decisions.md` during `10`. Then `40`, `31`. Then schema v3 + validator. Then Godot M1 (§6 E).

**Standing rules for the successor:** every distilled rule cites a D-number or is marked PROPOSED; nothing new goes in `design/` without the owner in the session; `proposals/` for everything else; commit per doc; if a v1 rule and a C-ref conflict and the C-ref isn't promoted yet, write the v1 rule and flag the conflict in Open questions — never silently harmonise.

## 7. Notes for the successor agent
- Reading order: `AGENTS.md` → `design/00-steer.md` → **this file** → `proposals/2026-09-20-ontology-draft.md` → `proposals/2026-09-20-successor-review.md` §1–2.
- Everything in §3 is agent synthesis of owner direction. Cite C-refs when writing docs; write `PROPOSED` until the owner logs a D-number. Never self-attribute.
- Owner working style observed this session: reacts to concrete sketches, corrects sharply, prefers one idea per exchange, will overturn earlier v1/v2 decisions when they jar — flag the supersession explicitly rather than silently harmonising.
- Owner is a first-time game dev with strong TTRPG literacy; comps this session: OD&D speeds, FFG SW RPG, ICRPG, Blades in the Dark, PbtA, MtG gold cards, Darkest Dungeon %, Elder Scrolls schools, BotW chemistry, Naruto (Gaara), Elric.
- `device_bash` was unavailable this session; files were written via stage/commit. Git status unknown beyond "no `.git` seen."
