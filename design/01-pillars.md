# 01 — Pillars (one-pager)

**Scope:** all · **Status:** DECIDED (D5.3–D5.5, D5.16–D5.21) except where marked (D5.22 is a flagged reference, not a decision) · **Updated:** 2026-09-20

## Purpose
The test every design, art, and scope question is held against. If a proposal serves no pillar, it is out.

## Pillars

| # | Pillar | What it means in play | Anti-pillar (what it rules out) |
|---|---|---|---|
| 1 | **Reading beats rolling** | Information is a resource. Insight, hidden reactions, revealed queues. The fight is won by understanding the opponent. | Variance that decides fights. Hidden math with no tells. |
| 2 | **Commitment is exposure** | Big moves resolve first and are the most counterable. Overextending creates the reversal. | Safe optimal lines. Damage races. |
| 3 | **Bodies, not bars** | No HP. Wounds are anatomical, named, and change what you can do. | Health pools, generic "damage." |
| 4 | **One table, one world** | Terrain map → diorama → cut-out; only the camera changes scale. One render style across every layer. | Separate visual languages per screen. Theater/puppets. |
| 5 | **A living, anachronistic world** | Regions carry their own era and place markers; factions and NPCs act while you travel. | A single global tech era. Steampunk. Recognizable modern/future tech. |
| 6 | **One systemic foundation** | Duel, infiltration, siege, city, culture — one scene runner, one actor model at every scale, one condition system. Scenes nest. | Bespoke minigames per encounter type. Separate character sim and holdings sim. |
| 7 | **Scope discipline** | 1v1 duel first; everything else is designed, tagged, and waits. | Building TARGET/FUTURE before MVP is human-played. |
| 8 | **Knowledge is power** | What your character *knows* — techniques, families, creatures, cities — is progression, tradeable, inheritable, and gated by what they've witnessed. | Omniscient player. Static bestiary unlocked by menu. |

## Player fantasy (one line)
Feel the opponent out, spot the tell, spring the trap — then grow from a nobody into the one the village looks to.

## Influence allocation — each influence owns a job and is barred from others (D5.5)

| Influence | Owns | Does NOT own |
|---|---|---|
| NITRO GEN OMEGA | camera cuts, plan → watch rhythm, animatic-style held-frame staging (D5.18) | art style; theater/puppet framing (Bunraku considered, rejected — pillar 4 anti-pillar + anti-goals) |
| Tabletop wargaming | terrain table, diorama staging, grouped-standee mass units, table-view camera | rules (no grid, no measuring) |
| Paper Mario | cut-out material, layered flat sets, paper-doll pose/costume-layer construction (D5.19) | tone, theater, puppets |
| UI as animate paper (D5.17) | UI reads as physical paper — folding, fluttering, z-depth as interaction feedback (panels sliding like sheets, edges catching light, paper-grain/shadow) | combat camera/animation grammar (NITRO GEN OMEGA); tabletop language in UI (D3.3 still holds — props only) |
| Naruto | action readability, shonen progression arc, **anachronism ceiling** (powerlines, CRTs, Y2K — vaguely recognizable) | world, costume, name |
| Meiji Restoration | uneven industrialization, old/new social friction, imported tech in traditional settings | a global era |
| Ghibli / Nausicaä | ecology, handmade tech, settlements adapted to environment | every faction's costume |
| Cowboy Bebop | drifter fashion, worn tech, negative space, adult tone | world history |
| Noir · caballero / frontier | per-region flavor (River Nomads first) | global base |
| Ukiyo-e (Japanese woodblock prints) (D5.16) | atmospheric overworld backdrop: mountains, roads, rice terraces, mist, seasonal light | character costume or color rules (Naruto row) |
| Cassette cyber-funk | props, media, signal culture | HUD, palette |
| Historical shinobi | what the profession is: recon, deception, sabotage | costume shorthand (headbands, vests) |
| Zero Company / XCOM | radial selector + direct targeting as *starting point* | grid |
| Mount & Blade | 3D relief pathing, living-map travel | combat |
| Crusader Kings 3 | characters/traits/bonds generate history; dynasty legacy | map-painting |
| The Bazaar | build tempo, loadout-as-deck feel | economy |
| **Magic: the Gathering** | ability kinds (activated / triggered / static), cost + color identity (body/mind/spirit), keywords as tags, templated rules text, deckbuilding curve | hand/draw/library, life totals |
| **Blades in the Dark** | scale (log₂ headcount) and tier, effect bands, crew sheet as group actor, faction tier/hold/status, clocks | position/effect adjudication (no GM) |
| **City of Mist** | tiered status tags, story tags minted by play, burn-a-tag, narrative + mechanical in one token | free-text tags without an ontology |
| Witcher | bestiary schools, knowledge as trade | monster-hunter framing |
| ASOIAF | political texture, "20 good men" scale logic, named-but-mortal, institutions with agendas | magic system, despair |
| The Black Company (D5.20) | grunt's-eye view of war — the mercenary company (not king or wizard) as the narrative unit; chronicle-keeping (the Annals) as an in-fiction institutional duty; magic played as a terrifying, opaque force rather than an explained system | political texture / institutions-with-agendas (ASOIAF's); world-memory system (Dwarf Fortress Legends, below); costume |
| Elric of Melniboné | power with a price, doomed-champion arc, decadent empires as ruin layer | costume |
| Fafhrd & Gray Mouser | two-person party as default unit, city sword-and-sorcery, banter | world scale |
| Discworld | cities and institutions as characters, guilds/orders with personality | comedy as tone |
| Dwarf Fortress (Legends) | the world remembers everything; marks | opacity |
| Malazan Book of the Fallen (D5.21, D5.22) | ascension — mortals becoming legend/godhood through remembered deeds, as narrative precedent for the marks/legacy system (D5.13); soldiers' dark humor and camaraderie under grim stakes; **flagged riff reference (not yet a decision, D5.22)** for a future magic/spirit-resource design pass — warrens as concept/patron-tied power paths, visible strain/cost on overreach, uneven mastery | the marks/legacy mechanic itself (still D5.13/Dwarf Fortress Legends); ability-kind chassis and color identity (still Magic: the Gathering's); tag ontology (still City of Mist's); world scale (TARGET/FUTURE flavor only, not MVP) |
| RimWorld | storyteller as pacing Director (FUTURE) | colony sim |

## Design stance (D5.15)
**Simulationist chassis, narrativist tags.** The owner's TTRPG literacy is the design's source and its main risk: tabletop reaches for a new subsystem per fiction and lets a GM adjudicate; a video game punishes subsystem count and has no GM. Replacements for the GM, in order: tags as rules (one ontology, matched by family), magnitude bands instead of exact numbers, exception-based display, authored content via families + agents, human play before any tuning, and — FUTURE — a pacing Director. Pillar 6 is the enforcement: one engine, actors at every scale.

## Anti-goals (explicit)
- No tactical grid. No HP bars. No real-time action combat.
- No recognizable modern/future tech above the Y2K ceiling; nothing with a real-world brand shape.
- No Japanese calligraphy motifs. No Naruto costume shorthand. No steampunk, top hats, gothic architecture.
- No theater framing (curtains, puppets, storybook narrator).
- No system built before the duel is human-played.

## Dependencies
- Reads from: `decisions.md` (D2.11 variance, D4.5 multi-actor, D5.3–D5.5)
- Writes to: every other design doc (as the test)

## Open questions
1. Title (Open #7 in `00-steer.md`).
2. Whether "Bodies, not bars" extends to mental/spiritual wounds in the same UI language — confirm at M2.
3. **Magic/spirit-resource system has no dedicated doc yet** (folded into ability design in `10-combat-loop.md`/`12-reactions-passives.md` for now). Malazan Book of the Fallen (D5.22) is flagged as riff reference for whenever that gets its own design pass — not decided, just earmarked so it isn't lost.

## Status table
| Item | Status | Scope | Source |
|---|---|---|---|
| Pillars 1–3, 6 | DECIDED | MVP | bible §1, D2.x |
| Pillar 4 presentation grammar | DECIDED | MVP (M2) | D5.3 |
| Pillar 5 world/era rule | DECIDED | TARGET | D5.4 |
| Influence allocation | DECIDED | all | D5.5, D5.16–D5.21 |
