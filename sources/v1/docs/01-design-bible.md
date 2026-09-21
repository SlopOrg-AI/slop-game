# 01 — Design Bible

**Single design source of truth. Updated 2026-09-19.**
Every item is tagged: **[MVP]** built in the first Godot slice · **[TARGET]** designed now, built after MVP · **[FUTURE]** vision, not designed in detail · **[OPEN]** undecided.

Sources merged: ChatGPT status doc (Sept 2026), project decisions log, memory of earlier chats. Where sources disagreed, the resolution is stated inline with ⚖️.

---

## 1. North stars

- Player decisions carry primary weight. **Variance is bounded and opt-in** — it creates surprises, it never decides the fight. See §1a. *(Revised 2026-09-19 from "no dice anywhere".)*
- Combat produces **reversals and tactical tension**: preparation matters, overcommitting creates counterplay.
- **Information is a resource.** Reading the opponent is how you turn a fight.
- Specialists are powerful in their domain; generalists and situational specialists stay viable.
- One systemic foundation serves combat *and* non-combat scenes.
- The world lives independently of the player. Story emerges from systems, bonds, rivalries, missions.
- Named techniques feel distinctive even under a shared tag system.

### 1a. Variance model [OPEN — direction set, mechanism undecided]

Intent (user, 2026-09-19): a hit can be *a bit lucky* and tip a threshold — initiative crosses a zone line, a Strength threshold drops and a guard fails — so an ability is removed from the opponent's board. Not guaranteed; the player *chose to gamble* on that upside. Downside exists but can be mitigated.

Proposed shape:
- **Deterministic core.** Costs, gates, reaction grading, wound mapping stay exact. Variance only touches **magnitude** of damage / initiative delta on abilities that declare it.
- **Opt-in per ability.** Ability schema gains `variance: { low, high }` as a multiplier band (e.g. 0.8–1.3). Most abilities `1.0–1.0`. "Gamble" abilities carry a wide band and a **swing tag**; safe abilities carry none.
- **Threshold-driven payoff.** The interesting outcomes are the ones that cross a line: initiative into Dominant, a Strength/Quickness attribute below an ability's `requires` (→ that ability locks = "dropped guard"), a wound band up one step. Variance matters *because* the game is full of thresholds.
- **Mitigation is a skill.** Insight spend can narrow the opponent's band or widen yours; Wits-gated abilities can *reroll* or *floor* a result; Courage floors downside on spiritual damage. Reactions can be tuned to trigger on "high roll" outcomes.
- **Visible odds.** UI shows the band on the ability card and the thresholds a high roll would cross (see wireframe callout on Lightning Palm).
- Alternatives to consider: (a) player-picked "commit" levels instead of RNG (more Heart-flavoured, still deterministic), (b) hidden RNG resolved at Declare (a "sealed" result), (c) deck-draw variance (draw a hand from the loadout each round). Decide after first wireframe pass with variance shown.

---

## 2. Structural tiers

| Tier | What | Tag |
|---|---|---|
| **Campaign / overworld** | 3D world map, Mount & Blade travel; world evolves while you travel | FUTURE |
| **Location** | Slay-the-Spire-style node map of Scenes; carries persistent Conditions; abilities/choices between nodes | TARGET |
| **Scene** | The encounter unit. One runner handles every type: duel, infiltration beat, passive obstacle, social contest | MVP (1v1 duel only) |

---

## 3. Characteristics — the stat model [MVP]

⚖️ Supersedes the sim's pool-heavy model and the Godot mock's physical/mental/spirit notches. Merges ChatGPT's threshold-vs-pool distinction and 0–300 scale.

### 3.1 Four classes

| Class | Verb | Definition | Members |
|---|---|---|---|
| **Attributes** | *tested* | Fixed capability rating. Gate abilities (`requires`). Scale effects. Only **wounds** lower them. Never spent. | Strength, Quickness, Wits, Courage, Heart |
| **Reserves** | *spent* | Pool with a max and a per-round refill. Abilities cost them. | Stamina, Focus, Chakra |
| **Meters** | *built → tapped* | Start at 0 each scene, rise through play, tapped at will. | Insight (per character, hidden) · Initiative (shared, visible) |
| **Guards** | *absorb* | Flat subtraction from incoming damage of one type. Small numbers. | Toughness (physical), Grit (mental), Will (spiritual) |

### 3.2 The stats by group

Damage resolves against **one of three guards** — physical (Toughness), mental (Grit), spiritual (Will) — but what a hit *is* comes from a **stack of tags**, not one type. See §3.2a.

#### 3.2a Damage tags — reactive, overlapping [MVP core, taxonomy grows]

A damage instance carries any number of tags from several families; they all apply and overlap:

| Family | Examples | What they do |
|---|---|---|
| **Channel** (exactly one) | physical · mental · spiritual | Picks the guard that absorbs it and the regions it can wound. |
| **Form** | blunt · piercing · slashing · crushing · grappling | Shapes the **wound** (blunt torso → bruised ribs; piercing torso → punctured lung); interacts with guards (piercing ignores part of Toughness). |
| **Element** | fire · water · lightning · wind · earth · metal | Amplify against states and each other (lightning ×2 vs `wet`; fire dries `wet`; water on `burning` extinguishes); impose their own status. |
| **Effect** | stagger · expose · bleed · burn · chill · daze · dread | The **status** the hit tries to apply; a hit can carry several. |
| **Intent** | feint · read · pressure · finisher | Insight/initiative side-effects; what reactions key on. |

Rules:
- **Every tag can react.** Guards, states, scene conditions, wounds and reactions all match on tags, not on a single type. A reaction "vs piercing" and a reaction "vs lightning" both fire on a *lightning-piercing* needle.
- **Statuses come from tags.** Effect tags apply states on the target (durations in §10.2); element tags apply their element state (`wet`, `burning`, `charged`, `chilled`). States then feed back into amplify/gate/cost rules — this is the combo layer.
- **Order of resolution:** channel guard → form modifier → element amplify vs current states → wound roll-up → statuses applied → intent side-effects.
- Hand-to-hand must stay fun with only channel + form + effect; elements are additive.
- Taxonomy is open-ended; the MVP authors ~5 forms, 3 elements, 6 effects.

| Group | Stat | Class | Refill | What it does |
|---|---|---|---|---|
| **Body** | Strength | Attribute | — | Force. Gates heavy/grappling techniques. Scales physical damage. |
| | Quickness | Attribute | — | Speed/precision. Gates fast techniques. Breaks initiative ties. Scales evasion-type reactions. |
| | Stamina | Reserve | **40%** of max / round (band 30–50) | Fuel for physical action. **Fungible**: can be converted into Chakra, or spent to *brace* Strength/Quickness for a round. |
| | Toughness | Guard | — | Absorbs physical damage. |
| **Mind** | Wits | Attribute | — | Tactical faculty. Gates terrain/improvisation/feint abilities. Scales Insight generated by reading moves. |
| | Focus | Reserve | **100%** / round unless hindered | Concentration. Costed by almost every ability. **Lost sharply** to stagger, pain, genjutsu → your next round shrinks. |
| | Insight | Meter | starts 0 | Your read on the opponent. See §5. |
| | Grit | Guard | — | Absorbs mental damage (genjutsu, pressure, confusion). |
| **Spirit** | Chakra | Reserve | **30%** / round (band 25–33) | Supernatural techniques. |
| | Courage | Attribute + **break line** | — | *What you can take.* Spiritual damage erodes it; at ≤ **25%** the character breaks (defeat unless scene says otherwise). Reduces the back-foot penalty of low initiative. |
| | Heart | Attribute | — | *What you're willing to give.* Gates **demeanor stances** [TARGET] (berserk: +Strength −Focus refill; cold resolve: +Guards, no Heart surge). Scales the amplification when an ability is "committed" with emotion. |
| | Will | Guard | — | Absorbs spiritual damage. |

**Removed:** the sim's *insight/wits/courage as spend-regen pools*; the Godot mock's *Will* pool; *metal* as a damage type.

### 3.3 Scale and calibration

- One numeric scale for Attributes and Reserve maxes: **0–300+**. ~100 competent professional · ~150 elite · 200+ legendary. Guards live on a small scale (~5–40).
- Values are **irregular** (104, 97, 141) — produced by base + trait modifiers, never round numbers.
- Reserve refill is a **percentage of max**, so a bigger pool refills more in absolute terms; wounds and states modify the percentage.
- Ability costs at the ~100 level: light action ≈ 10–15 Stamina + 20–25 Focus; heavy ≈ 25–30 Stamina + 35–45 Focus; jutsu ≈ 20–30 Chakra + 30–40 Focus.

**Reference pair (the "average battle"):**

| | Kaede (generalist) | Genzo the Ox (brute) |
|---|---|---|
| Strength / Quickness | 104 / 97 | 141 / 71 |
| Wits / Courage / Heart | 92 / 94 / 88 | 58 / 117 / 126 |
| Stamina / Focus / Chakra (max) | 110 / 100 / 101 | 138 / 80 / 66 |
| Toughness / Grit / Will | 14 / 9 / 12 | 26 / 11 / 6 |

### 3.4 Action budget [MVP]

⚖️ Replaces the sim's fixed `actions_per_round = 2` and ChatGPT's separate "time cost".

- **No action count and no tick budget.** Each ability costs some combination of Focus / Stamina / Chakra. You queue actions until you cannot afford the next one.
- Focus refilling to 100% makes it the de-facto *attention budget* for the round; Stamina and Chakra are the *endurance* limits across rounds.
- Hindering Focus (stagger, pain, genjutsu) is therefore the universal "you lose tempo" lever.
- **Reactions** cost no queue budget but **reserve** their cost while armed (that reserve is unavailable to actions and does not refill).

---

## 4. Initiative [MVP]

- **Single shared bar, 100 points: −50 … +50, centred on 0**, persists across the whole fight (tug-of-war, never reset). *(D2.12; was −10…+10.)*
- Opening value from scenario (surprise/ambush can start at ±25–30) and Quickness differential.
- Ability deltas follow the same irregular / roughly-normal principle as attributes: ordinary moves ±3–9, movement and big commits ±11–15, perfect counters and Insight reveals can move 20+.
- **Job 1 — reach:** melee abilities require initiative ≥ −10 for the attacker. Below that you are on the back foot: ranged, movement, reads, and defensive plays only.
- **Job 2 — pressure:** zones.

| Zone | Trigger | Effect |
|---|---|---|
| Dominant | ≥ +25 | Physical/spiritual damage ×1.25 |
| Neutral | between | — |
| Desperate | ≤ −25 | Partial reactions upgrade to perfect; Courage reduces further penalties |

- Initiative moves via: ability `initiative` deltas, landing major damage, perfect reactions (reverse), Insight reveal (§5), Heart surges [TARGET].
- ⚖️ The sim's "spend initiative for discounts" is **dropped**. Spending is Insight's job now.
- Initiative no longer decides resolution order (D2.13). Ties in lead-sum → initiative holder, then Quickness.

---

## 5. Insight — the hidden edge [MVP]

- **Per-character hidden meter, starts at 0** each scene. Shifted by scenario (ambusher +, ambushed −), location knowledge, and opening abilities.
- **Built** by reading moves: observe, probe, feint, deliberately absorb a hit, certain reactions. Scaled by Wits. Early rounds naturally become "feeling each other out".
- **Tapped, any amount, not all-or-nothing.** Two uses:
  1. **Turn the tables** — spend N Insight to shift your *effective* initiative by N/2 bar points (`rules.insight.per_initiative_unit`) at the moment it matters. The visible bar shows what both fighters *think* the position is; Insight is the hidden modifier that reveals you were never as cornered as you looked. Spending part keeps the rest hidden for later.
  2. **Reveal** — spend a little to see: opponent's declared action costs, one hidden ability, wound list, current reserve bands.
- Insight also **shifts reaction grade** (partial → perfect) when the holder's Insight exceeds the attacker's.
- Opponents build and tap Insight too — a fighter who looks beaten is still dangerous.
- **Timing (D2.14):** commit at any moment you are selecting abilities *or about to be impacted by one* — Declare, Arm, or as an interrupt before an incoming action resolves. The shift applies before reach, zone and reaction grade are checked.

---

## 6. Round structure [MVP]

1. **DECLARE** — both sides queue actions simultaneously (limited only by reserves). Queues are then **revealed** to each other (costs and names; details subject to Insight).
2. **ARM** — each side may set **one hidden reaction**, knowing what the opponent declared. Optional hidden Insight commitment here [OPEN].
3. **RESOLVE** — **trick-taking order (D2.13):** each queued ability is ranked by the sum of its `requires`; the side with the higher lead goes first, then sides alternate in descending requirement order (tie → initiative holder, then Quickness). Reactions fire on matching triggers; wounds applied; Focus/Stamina/Chakra refill at end of round; scene conditions tick. Initiative governs reach and zones, not order.
4. Return to DECLARE unless a win/fail clause is met.

Information model: **queued actions visible, armed reactions hidden, Insight hidden.** Variance (if adopted, §1a) is rolled at RESOLVE, magnitude only.

---

## 7. Reactions / counters [MVP]

- Card-game trap feel. Armed in advance, triggers on a matching opponent action/contest.
- **One armed at a time.** Persistent across rounds until it fires; its reserved cost stays locked (holding a trap is a standing cost).
- **Graded by trigger specificity, not chance:**
  - Narrow trigger (≥2 predicates, e.g. *melee AND physical*) matching exactly → **perfect**: full negation, attacker's spent reserves lost, initiative reverses.
  - Broad trigger (1 predicate) → **partial**: damage halved.
  - Modifiers: Insight differential +1 grade; `focused` state or Desperate zone +1 grade.
- Effect scales with the attacker's commitment (bigger swing, bigger punish).
- **[OPEN]** Loadout: dedicated reaction slot vs competing with actions. Proposal: one dedicated reaction slot.

---

## 8. Damage and wounds — anatomical, no HP [MVP]

⚖️ Replaces the sim's percentile threshold damage. Implements ChatGPT's anatomical model.

### 8.1 Pipeline
1. Ability deals damage of amount A with a **tag stack** (§3.2a) to a **region**.
2. Subtract the **Guard** matching the channel tag, modified by form (e.g. piercing bypasses part of Toughness) → net N. N ≤ 0 → no wound (effect/element tags may still apply states).
3. Amplifiers apply (element × states, zone, wounds).
4. N maps to a **severity band** for that region → a **named wound** is created.
5. Wound effects apply immediately and persist (for the scene, or longer [TARGET]).

### 8.2 Regions [OPEN — confirm]
Physical: **head, torso, arms, legs**. Mental: **mind**. Spiritual: **spirit** (spiritual damage primarily erodes Courage; severe hits also wound spirit).

### 8.3 Severity bands
Per wound, not a universal ladder. Bands: **minor · moderate · severe · crippling**. Same net damage produces a different wound per region. Wound names communicate anatomy and severity.

### 8.4 Wound effects (any combination)
Attribute reduction · reserve current reduction · reserve max reduction · refill % reduction · ability lock (by tag or id) · ability effectiveness · state application.

Examples (author ~12 for MVP):

| Wound | Region / band | Effects |
|---|---|---|
| Bruised ribs | torso / minor | Stamina −10 now |
| Torn calf | legs / moderate | Quickness −22; Stamina refill −10%; locks `lunge` tag |
| Broken forearm | arms / severe | Strength −35; locks `grapple` tag; `two-handed` abilities locked |
| Rattled | mind / minor | Focus −30 now |
| Concussed | head / moderate | Focus refill 100% → 60%; Wits −15 |
| Shaken | spirit / moderate | Courage −20; Heart −10 |

### 8.5 Overall condition
Emerges from accumulated wounds. No HP bar. UI shows wound list + the stats they've dragged down.

### 8.6 Win / fail conditions (per scene) [MVP]
- **Courage break** — Courage ≤ 25% of max.
- **Incapacitation** — Stamina reaches 0, or Strength/Quickness below the floor needed for any loaded ability.
- **Surrender** — AI/player yields (AI: when projected loss is certain).
- **Kill** — only in scenes flagged lethal.
- Composable objectives for non-duel scenes [TARGET]: eliminate, survive N, reach, acquire, evade, protect; AND/OR; separate win and fail clauses; fail-forward.

---

## 9. Abilities / techniques

### 9.1 Identity [MVP]
Named, evocative, stable baseline identity. Tags describe behaviour; modifiers alter it [TARGET]. Straightforward hand-to-hand must be fun with zero elemental complexity.

### 9.2 Schema [MVP]
```
id, name, group (body|mind|spirit), kind (action|reaction)
tags: [strike, heavy, grapple, lunge, movement, read, feint, genjutsu, fire, water, lightning, metal, ...]
reach: melee | ranged | any
requires: { strength?: n, quickness?: n, wits?: n, courage?: n, heart?: n }
costs: { focus?: n, stamina?: n, chakra?: n }
damage: [ { amount: n, region: head|torso|arms|legs|mind|spirit,
            tags: [channel, form?, element*, effect*, intent*] } ]   # §3.2a — tags overlap
initiative: ±n
insight: +n            # generated on use
applies: [state]       # on target
self_applies: [state]
gates: [ { condition, op, value } ]        # scene-condition legality
cost_mods: [ { condition, reserve, per_point } ]
amplify: [ { state|tag|zone, on: target|self, mult } ]
trigger: { predicates: [...] }             # reactions only
variance: { low: 1.0, high: 1.0 }          # magnitude band, §1a [OPEN]; 1.0–1.0 = deterministic
shot: string                               # cutaway shot type
```

### 9.3 Loadout [MVP]
- One ability **library** per character; **loadout** chosen pre-scene into **typed slots** (body / mind / spirit + reaction). Abilities outnumber slots → deckbuilding moment.
- Two power axes: slot count (raw) and ability quality (sophistication). Movesets overlap ≤ ~50% at the high end.

### 9.4 Tag families [TARGET]
Element · reach · execution (instant/long) · target count/area · family (taijutsu/ninjutsu/genjutsu/…) · reactive trigger family · special conditions. Exact taxonomy grows with content.

### 9.5 Acquisition and modification [TARGET → FUTURE]
Visual-novel × deckbuilder: missions, training, patrons, peers, rivals grant abilities; training modifies tags; combining techniques [FUTURE]. Bonds directly shape build.

---

## 10. Scene conditions and actor states

### 10.1 Scene conditions (numeric tracks) [engine MVP, content thin]
**light, noise, alert, footing, weather, time_of_day.** Baseline + increments; ±1 normal; **+4 tipping threshold**. Each declares tick rate; **cascades** push each other (weather → footing; noise ≥4 → alert); scripted beats per scene. Hard clamps; cascade depth ≤ 2/round. MVP authors **footing** and **light** only.

### 10.2 Actor states (tags with duration) [MVP]
**wet, burning, charged, chilled, staggered, exposed, bleeding, dazed, dreading, focused, braced.** Boolean + round count. Applied by effect and element tags (§3.2a); element states interact (fire clears wet; water clears burning).

### 10.3 Three channels into abilities [MVP]
Every ability may declare **gate** (legality), **cost_mod**, **amplify**. Combos live here (lightning ×2 vs `wet`).

### 10.4 Propagation [TARGET]
Scene → Location is context-dependent (flashlight doesn't raise location light; a warehouse fire does, modestly, if night).

---

## 11. Presentation [MVP thin → TARGET]

- **Cutaway stage:** each ability has a `shot` type; MVP swaps static pose images and prints a log line. TARGET: short pose sequences, camera cuts, VFX.
- **Art:** flat 2D characters/props in a 3D scene (Paper Mario). Poses ideally generated from a 3D model → 2D. Procedural-friendly pipeline.
- **UI direction:** "ink over paper" (from the Godot mock) — keep as the visual hypothesis, validate in wireframes.
- **Opponent panel shows no raw numbers** unless revealed by Insight: bands, chips, declared actions, "reaction armed" indicator, unknown-ability count.

---

## 12. Character and campaign systems [TARGET / FUTURE]

- Player creates a protagonist: personality, traits, reputation, relationships, clan, beliefs, scars, titles, equipment. [TARGET]
- **Traits** modify base stats with mixed, irregular values; innate or acquired; altered by bonds. [TARGET]
- **Bonds** affect narrative, stats/traits, technique acquisition, combat cooperation. [TARGET]
- **Progression:** missions → techniques, bonds, rivalries → status → leadership → Hokage-equivalent. [FUTURE]
- **Death:** scenes can be lethal; NPCs die permanently; player can die; free save/reload for now. [TARGET]
- **Generations:** marriage, children, time skip, play the heir. [FUTURE]

## 13. World simulation [FUTURE]
Pre-designed world, emergent campaign. Factions and NPCs with agendas, personality traits, cultural/religious tenets; act while player is elsewhere. NPC leaders use the same character/combat systems; the difference is scale (followers, contacts, missions).

## 14. Technical direction [MVP]
- Godot 4.7, GDScript, Windows. Repo at `C:\Claude\Godot\shinobi-master`.
- **Data-driven:** abilities, characters, wounds, conditions as JSON; engine reads them. Adding content = adding data.
- UI built in code (hand-edited `.tscn` is fragile); rebuild as scene tree once layout settles.
- Deferred until MVP works: asset pipeline, animation, VFX, music/SFX, save system, localization, build/release.
