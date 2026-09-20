# 50 — World systems: actors at every scale

**Scope:** FUTURE (design direction) · MVP obligation = engine constraints in §6 only · **Status:** DECIDED direction D5.11–D5.13; mechanisms OPEN · **Updated:** 2026-09-20

## Purpose
One engine, recursively applied. A city, a faction, a dragon, a team, and a shinobi are all actors with the same four stat classes, the same ability kinds, and the same knowledge tiers — at different scales and clocks. This doc holds the direction so the MVP engine doesn't foreclose it.

## Player experience goal
The world is made of the same stuff you are. Beat a champion and their city *learns* you. Secure a gate in a sewer fight and the siege above you turns. Your grandfather's crater is still on the map.

## 1. Scale hierarchy (D5.12)

| Scale | Name | Clock | Named actor | Group actor | Typical scene |
|---|---|---|---|---|---|
| 0 | Duel | round | Shinobi | Band (a handful, "20 good men") | 1v1, skirmish, infiltration beat |
| 1 | Field | watch | Champion | Company (~100s) | battle, ambush, district chase |
| 2 | Siege | day | **Kaiju** (dragon, warlord-as-army, walking ruin) | Host · Settlement | siege, plague, festival, market war |
| 3 | Realm | season | Titan (sleeping god, migrating forest, empire) | Faction / Culture | war, dynasty, ecological shift |
| 4 | Age | generation | Old Builders (legacy only) | Civilization | time skip, succession |

Rules:
- **Actor scale** = the scale at which it fights alone. Group scale = log₂ headcount (Blades in the Dark: 0 ≈ 1–2, 1 ≈ 6, 2 ≈ 12, 3 ≈ 20, 4 ≈ 40…). Scale × tier decides who is a peer.
- Below its scale an actor is a **location** (a kaiju is terrain in a duel: scenes on its back, under the wing, at the eye). Above its scale it is a **member**, folded into a group actor.
- **Minion groups** are group actors with no selectable members; the weak participate by grouping. Roster vs abstract strength: OPEN #11.
- Primary play is scale 0–1: PC + allies (named and/or bands). Higher scales are *entered*, *influenced* (queue a settlement's action as its leader), or *inherited*.

## 2. Nested scenes (D5.12)
- A scene at scale N is a location at scale N−1. Siege of the city ⊃ the city ⊃ sewer, forgotten tunnels, gate.
- Child outcomes propagate up as **conditions** ("gate secured" flips a siege condition); parent conditions propagate down (bible §10.4 generalized). Clocks nest; a parent tick contains many child rounds; parent AI acts concurrently.

## 3. Teams as co-present actors (D5.12)
- In a party scene, **members and the team sheet are both selectable** in planning.
- Team abilities = **combos** with member prerequisites: `requires: {members: [{family: fire, tier: ≥identified}, {family: wind}]}`. Charged to members' reserves *and* team reserves.
- Team reserves: Cohesion / Trust / Signal — built by bonds and fighting together. Team attributes derived (Coordination from bonds + shared family knowledge; leader's Wits/Heart as multipliers). Team wounds: broken formation, mistrust, lost signal.
- Team actions share the trick-taking order; requirement sum = members' sum → big combos resolve first and are most exposed (pillar 2).
- Recursive: a Company sheet holds Band sheets; a Settlement holds institutions. A party of one has no team sheet.

## 4. Settlements as actors (D5.11)

| Class | Character | Settlement (crude) |
|---|---|---|
| Attributes | Strength, Quickness, Wits, Courage, Heart | Population, Infrastructure, Learning, Cohesion, Legitimacy |
| Reserves | Stamina, Focus, Chakra | Workers, Food, Tools/Materials, Wealth, ritual capacity |
| Meters | Insight, Initiative | Intelligence on a rival, Standing vs a rival |
| Guards | Toughness, Grit, Will | Walls, Order, Faith |
| Wounds | torn calf | burned granary, plague, schism |
| Abilities | strike / trap / Keen Eyes | project or edict / response (raise militia when raided) / institution (a bestiary order = sustained passive that absorbs knowledge fast) |
| Loadout | typed slots | active institutions and projects |
| Clock | round | season |

- **City development = learning abilities**, via members, trade, conquest, teaching — same knowledge tiers as characters.
- **Ecology teaches:** environments carry knowledge facts (a bloom, exposed machinery, a migration). Known family + environmental fact → **synthesis** → new technique or settlement ability (bloom + irrigation family → a dead city revives). Cultures diverge because their surroundings taught them differently.
- Metaphor strain to design, not rename: settlement "initiative", "courage break" (collapse?).

## 5. Marks / legacy (D5.13)

| Mark | Modeled as |
|---|---|
| Landscape | permanent condition or terrain feature on the relief table (a crater, a scorched forest, a diverted river) |
| Built | a settlement ability/wound that outlives its maker (a wall, an order) |
| Remembered | a fact whose knower is *the world*, decaying to **legend** tier rather than unknown |
| Inherited | knowledge / traits / bonds to heirs and institutions |
| Named | places, techniques, epithets |

- Significance threshold: only actors above a scale/renown line leave marks.
- Old-builder ruins = this system at maximum age. Marks are gameplay: they change conditions, pathing, abilities, and what can be studied.

## 6. MVP obligation (the only part that touches the demo)
- `Actor {scale, kind: named|group|settlement, stats-from-data}` — stat class and reserve names come from data, never code.
- `Scene {scale, parent, children}` — conditions propagate both ways.
- Planning screen's selectable-actor list is data-driven (N actors, may include a team actor), even though M1 shows one.
- Tags are `family:name`; states are tiered (D5.14). Nothing else here is built before the duel is human-played.

## Dependencies
- Reads from: `10`–`15` (the engine), `21-world-factions` (cultures), `20-campaign`
- Writes to: `20-campaign`, `21-world-factions`, `30-art-direction` (relief table marks)

## Open questions
1. N-vs-M initiative model (Open #5) — now also "team vs team vs kaiju".
2. Minion roster vs abstract (Open #11). 3. Cultures as knowers (Open #10). 4. Settlement analogues of initiative and courage break. 5. Pacing Director (RimWorld storyteller) — where it lives.

## Status table
| Item | Status | Scope | Source |
|---|---|---|---|
| Scale hierarchy, actor kinds, nesting | DECIDED direction | FUTURE | D5.12 |
| Teams as co-present actors, combos | DECIDED direction | TARGET | D5.12 |
| Settlements as actors, ecology teaches | DECIDED direction | FUTURE | D5.11 |
| Marks / legacy | DECIDED direction | FUTURE | D5.13 |
| Engine constraints §6 | DECIDED | MVP | D5.12, D5.14 |
