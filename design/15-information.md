# 15 — Information: knowledge, insight, surfaces

**Scope:** MVP (model, tiers, in-scene surfaces) · TARGET/FUTURE (channels, groups) · **Status:** DECIDED D5.8, D5.10; defaults PROPOSED · **Updated:** 2026-09-20

## Purpose
One system governs what any actor knows about any fact, and where the player sees it. Insight (in-fight) and Knowledge (carried) are two channels of it.

## Player experience goal
You see the world through your character's eyes. An unknown technique is a shock the first time, a pattern the second, a page in your bestiary once you've beaten it. Learning your enemies is how you grow.

## Rules / Data

### Facts
Every fact has three independent properties:

| Axis | Values |
|---|---|
| Exists in world state | true / false |
| Known by | set of knowers, each at a tier |
| Surface | never · in-scene (HUD, log) · separate screen (sheet, bestiary, journal) · both |

Engine-only facts (AI intent, unspent hidden Insight, seeds) are `surface: never`.

### Tiers
| Tier | Reached by | Player sees |
|---|---|---|
| unknown | — | outcome only, as a **magnitude band** ("a little / a lot / massively") |
| witnessed | seen once | outcome + "an unidentified technique" |
| identified | seen twice, or family known | name, family, rough costs; on the opponent's known-list next fight |
| studied | won the fight · reveal (scene-only) · taught · bestiary source | full card: costs, tags, triggers, variance band |
| legend (FUTURE) | decay of a *remembered* mark | true in outline, details drifted; sharpened by study |

**Families** are the unit of learning: knowing a family lifts every technique in it one tier faster.

### Channels
| Channel | Scope | Cost | Tag |
|---|---|---|---|
| Witnessing | this scene, sticks | free; **gated by scene conditions** (smoke, dark = not witnessed) | MVP |
| Insight reveal | this scene only | Insight | MVP |
| Winning | sticks | — | MVP |
| Teaching / inheritance | sticks, family-level | campaign | TARGET |
| Bestiary factions, books, spies | sticks | campaign currency | FUTURE |

### Insight (unchanged from v1, D2.6, D2.14, D3.2)
Per-character hidden meter, starts 0 each scene, built by reads/probes/feints/absorbing hits (× Wits), cap Wits/2. Spent partially: (1) effective-initiative shift N/2; (2) reveal (jumps a fact one tier for this scene). Drains to ~25% when an armed reaction fires. Usable at any selection or impact moment.

### Knowers
- Characters (MVP). Knowledge is **character-owned**: dies with them, inheritable (PROPOSED default; alt: player meta-progression).
- NPCs learn the player symmetrically (PROPOSED default yes).
- Groups (TARGET/FUTURE): teams pool; cultures/factions/orders absorb (member → group), spread (group → member by rank/trust), diffuse (group ↔ group by relations, secrets with a half-life), lose. Knowledge-purpose groups absorb fast. See `50-world-systems.md`.

### Surfaces
- **Opponent panel is a query:** "what does *this* actor know about *that* one?" Same code renders the AI's view of the player.
- In-scene: bands, chips, declared-but-unidentified actions, "reaction armed" indicator, unknown-ability count.
- Separate screen: character sheet (own), bestiary/journal (others), at the tier known.

## Dependencies
- Reads from: `14-scenes-conditions` (witness gating), `12-reactions-passives` (reveal → reaction precision), `50-world-systems` (group knowers)
- Writes to: `31-ui` (bands, bestiary screen), `20-campaign` (progression)

## Open questions
1. Character-owned vs player-owned knowledge (Open #9).
2. NPC symmetry (Open #9).
3. Cultures as knowers vs identification modifiers (Open #10).
4. Does the opponent **team sheet** (combos) obey tiers? Proposed yes.
5. Reveal-spend feeding next round's reaction precision (D3.2 follow-on) — experiment once playable.

## Status table
| Item | Status | Scope | Source |
|---|---|---|---|
| Fact × knower-tier × surface model | DECIDED | MVP | D5.10 |
| Tiers unknown→studied; bands for unknown | DECIDED | MVP | D5.8, D5.10 |
| Witness / reveal / win channels | DECIDED | MVP | D5.10 |
| Insight rules | DECIDED (confirm in play) | MVP | D2.6, D2.14, D3.2 |
| Teaching, inheritance, factions, groups | DECIDED direction | TARGET/FUTURE | D5.10 |
| Character-owned, NPC-symmetric | PROPOSED | MVP | — |
