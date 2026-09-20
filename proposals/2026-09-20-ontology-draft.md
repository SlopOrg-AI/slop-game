# Proposal — ontology draft: attribute hierarchy + naming schema

**Produced by:** Claude (Cowork), 2026-09-20, from the owner's design session of the same day · **Targets:** new `design/02-ontology.md`, `data/SCHEMA.md`, schema v3 · **Status:** `PROPOSED` — every term below is **PROVISIONAL** until a D-number locks it. Nothing here supersedes a decision; it names what the session discussed so 10–14 and the data can cite one vocabulary.

---

## 1. Structural hierarchy (what contains what)

```
World
└─ Scene            {scale, parent, children, conditions[], zones[], actors[]}     — is an Entity, and a Location at scale N−1
   ├─ Zone          {shape, anchors[], edges[]}                                     — authored polygon
   │  ├─ Anchor     {name, tags}                                                    — named point; positions are "zone + anchor | open"
   │  └─ Edge       {to: zone, kind: open|cover|wall|drop, material?}               — an Entity; created/destroyed by chemistry
   ├─ Object        Entity + {material, position, affordances[]}
   └─ Actor         Entity + {scale, kind: named|group|settlement, numbers (§2), abilities[], knowledge}
Entity              {id, name, tags[], states[], tracks{}?, material?}              — base of everything a rule can touch
Fact                {exists, known_by: {knower → tier}, surface}                     — anything the information system tracks
Ability template    {id, name, kind, budget, limits, stars[], descriptors[], reach, cost, effects}
Ability instance    {template, owner, draws{}, stars}                                — a character's *version*; teachable, inheritable
Material            {id, properties[], resistance{}, transitions[], products{}}
Reserve definition  {id, class, max_from{}, refill, fill[]}
```

Rules test **tags only**, never the subclass. A `burnable` actor and a `burnable` screen burn by the same rule.

## 2. Numbers on an actor (the attribute hierarchy)

Ordered from slowest-changing to fastest. Every row carries a **class** (body · mind · spirit) — class is a cross-cutting tag, not a level.

| Level | Name | What it is | Changes on | Class members (provisional) | Visible to others at |
|---|---|---|---|---|---|
| A | **Attributes** | tested capacities, 0–300 (100 competent) | training, wounds (temporary), age | body: Strength, Quickness · mind: Wits · spirit: Heart, Courage | sighted → observed → confirmed → ceiling |
| B | **Reserves** | pools spent to act; **data-defined**, any number of them | every round | *innate* (refill): Stamina (body), Focus (mind), Chakra (spirit) · *filled* (no refill): Blood (body→spirit) · *borrowed*: place, bond | by tell (Blood visible, Focus not) |
| C | **Guards** | flat absorb per damage channel | wounds, states | Toughness (physical), Grit (mental), Will (spiritual) | inferred from confirmed hits |
| D | **Meters** | in-scene per-actor numbers with named zones | every action | Insight (hidden, cap Wits/2) · Momentum (per-actor; replaces shared initiative — **pending owner pick 1/2/3**) | Insight never; Momentum as band |
| E | **Tracks** | accumulated severity per region within a scene | every damage event | head, torso, arms, legs (physical) · mind (mental) · spirit (spiritual) — Open #4 | as bands; wounds by name |
| F | **States** | tiered tags with decay, `name-N` | rules mint / decay | wet-2, burning-1, staggered-1, guarding-2, restrained-3, focused-1, braced-1 | in-scene chips, exception-based |
| G | **Wounds** | named, minted when a track crosses a threshold; carry effects on A–D | thresholds | ~12 authored | by name, once witnessed |
| H | **Knowledge** | facts × tier, carried between scenes | witnessing, reveal, winning, teaching | tiers: unknown → witnessed → identified → studied → (legend) | it *is* visibility |
| I | **Position** | zone + anchor; range to anything is derived | maneuvers | Engaged · Short · Medium · Long · Extreme | always, if sighted |
| J | **Abilities** | instances in typed slots | acquisition, training | draws sum to budget × star fraction | star level as a fact with tiers |

Derivation direction is downward only: attributes feed reserves' maxes and abilities' draws; reserves pay abilities; abilities emit damage events; events move tracks and states; tracks mint wounds; wounds modify attributes. No level reads a level below it except through a minted wound/state — that's the loop, and it's the only loop.

**Design tests:** a new number must name the threshold it feeds; a new tag must name the rule that reads it; a new reserve must name what fills it.

## 3. Draws and budgets (how abilities read the numbers)

- `draws: [{source, key, weight}]` — `source ∈ attribute | reserve | element | scene | object | bond | fact | mark`. M1 uses `attribute` + `element`.
- **Budget:** mono-class full-scale = 1.0. Second class **+.5**. Element **+.25** (source: Heart, provisional). Second *source* (place, bond, fact) counts as a second class.
- **Stars** scale the budget: ★1 .6 → ★5 1.0; stars add descriptors at thresholds; never change the distribution.
- **Limits** on the template; **distribution** on the instance, fixed at acquisition (source: learner's ratio and/or teacher's instance, clamped — owner decision pending). Descriptor ⇔ top weight is a validator rule (`swift` ⇒ Quickness leads).
- **Gold** ⇔ two classes in draws ⇔ two reserves in cost. Flag: Focus-on-everything must be resolved (Focus = mind reserve only, or gold defined by draws alone).
- **Tradition** = draw profile × reserve × tell (sorcery: Heart/Courage → Chakra; wizardry: Wits → Focus; ninjutsu: body+Wits → Stamina+Chakra, hands required; blood: Str-filled Blood). **School** = effect verb (destruction · alteration · illusion · restoration · conjuration · mysticism). Variety = tradition × school.

## 4. Tag families (the descriptor vocabulary)

Format `family:name`. Lowercase, singular, ASCII, `_` inside names. Tier suffix `-N` (1–5) appears only on **state instances**. Matchers match on family or exact tag. Families are closed lists per doc; adding a *family* is a design decision, adding a *name* is authoring.

| Family | Names (initial) | Read by |
|---|---|---|
| `class` | body · mind · spirit | slots, gold rule, reserve colour |
| `channel` | physical · mental · spiritual | guard selection |
| `form` | blunt · crushing · slashing · piercing · grappling | guard bypass, wound selection |
| `element` | fire · water · lightning · wind · earth · cold | chemistry (amplify/clear/mint), element draw |
| `tempo` | swift · heavy | precedence (`swift` precedes `heavy`; `swift` precedes a `guard` state lacking `swift`) — **family name provisional** |
| `intent` | strike · feint · read · intimidate · guard · control · maneuver · counter | reaction triggers, AI, information tells |
| `effect` | stagger · expose · daze · dread · bleed · pin | state minting |
| `state` | wet · burning · chilled · charged · staggered · exposed · focused · braced · guarding · restrained · pinned · drained | chemistry, precedence, display |
| `condition` | light · footing · noise · alert · weather · dust | witness gating, cost mods, cascades |
| `material` | wood · stone · packed_earth · metal · cloth · water · flesh | transitions |
| `property` | burnable · conductive · brittle · fluid · rigid · porous · massive | chemistry (rules test these, not materials) |
| `region` | head · torso · arms · legs · mind · spirit | tracks, wounds |
| `range` | engaged · short · medium · long · extreme | reach rule, maneuvers |
| `edge` | open · cover · wall · drop | range derivation, creation/destruction |
| `kind` | activated · reaction · sustained · decaying · one_off | resolution |
| `source` | attribute · reserve · element · scene · object · bond · fact · mark | draws |
| `tradition` | sorcery · wizardry · ninjutsu · blood · rite · pact | tells, learning families |
| `school` | destruction · alteration · illusion · restoration · conjuration · mysticism | effect verb, bestiary grouping |
| `tier` | unknown · witnessed · identified · studied · legend | information system |
| `scale` | duel · field · siege · realm · age | actor/scene scale |

## 5. Dictionary rule verbs (`data/tags.json`)

Few and fixed; pairs are many. Adding a verb is a design decision.

| Verb | Shape | Example |
|---|---|---|
| `precedes` | tag × tag [unless tag] | swift × heavy · swift × guarding unless swift |
| `amplifies` | tag × tag → ×k | wet × lightning → ×2 |
| `clears` | tag × tag | water × burning |
| `bypasses` | form × guard → fraction | piercing × toughness → .5 |
| `mints` | tag × tag [requires scene tags] → state/object/edge [weight] | fire × burnable → burning-1 · earth × chakra → edge:wall{packed_earth} |
| `gates` | condition × channel | dust-3 × witness → not witnessed |
| `converts` | reserve × reserve → rate | stamina → blood 2:1 · stamina → chakra 2:1 |
| `transitions` | material × threshold → state, products | wood @ fire-3 → charred; @ collapsed → object:rubble + footing:unstable |

Unlisted pairs do nothing. Silence is a valid answer. Minting: deterministic when one candidate; narrow weighted draw among several, surfaced as a band (**owner decision pending**).

## 6. Naming schema (ids, files, instances)

- **IDs:** `snake_case`, singular, ASCII, stable forever. Renames add an `aliases` entry; never reuse an id for a different thing.
- **Display names** are free text in `name`; the id is the contract. Codename-era names are fine in `name`.
- **Instances:** ability instance = `{template, owner, draws, stars}` in the owner's loadout; referenced in logs as `template@owner` (`swift_strike@kaede`). Objects in a scene: `template#n` (`screen#1`).
- **States on an entity:** `state:name-N`. **Wounds:** `wound:name`. **Facts:** `fact:<subject>.<attribute>` (`fact:genzo.strength`, `fact:genzo.iron_guard.stars`).
- **Numbers:** attributes and reserve maxes integers on 0–300 (irregular values, never round-100 in authored data); weights two decimals summing to the budget; tiers 1–5; thresholds integers; bands named in `rules.json` only.
- **Files:** design docs `NN-name.md` (00 steer · 01 pillars · **02 ontology** · 10–15 combat · 20–21 campaign/world · 30–31 presentation · 40 production · 50 world systems). Data: one JSON per noun, plural filename: `abilities · characters · reserves · materials · wounds · states · conditions · scenes · tags · rules`. Every file carries `schema_version` (→ 3 on migration) and a `_doc` line citing the doc that owns it.
- **Cross-file references** are id strings, never nested copies.
- **Lock marker:** every term in `02-ontology.md` has a Status column: `PROVISIONAL` (default) · `LOCKED D#.#`. Docs 10–14 cite the ontology; they do not re-define terms.

## 7. Open, in order of leverage

1. Momentum (per-actor) vs shared bar vs per-action position — owner pick 1/2/3.
2. Courage: spirit (with Heart, under sorcery) or mind — settles three lanes.
3. Focus: mind reserve only, or universal attention budget (decides what "gold" means in cost).
4. Family name for swift/heavy (`tempo` here; alternatives `pace`, `weight`).
5. Acquisition source for instance distribution (learner ratio / teacher / choice).
6. Minting among several candidates: deterministic priority or narrow weighted draw.
7. `restrained` (holding back) and Blood: M1 or TARGET.
8. Lightning Palm: body+spirit gold, or the one tri-class showpiece.
