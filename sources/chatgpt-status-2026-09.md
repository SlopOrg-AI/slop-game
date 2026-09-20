> **PROVENANCE ONLY.** ChatGPT's parallel handoff doc, imported 2026-09-19 verbatim. Its content has been merged into `01-design-bible.md`; where it disagreed with project decisions, the bible states the resolution. Do not treat this file as current.

# Indie Game Project — Development Status & Handoff

## Purpose
This document is the persistent handoff for future chats/agents working on the game design, lore bible, technical architecture, production pipeline, and eventual implementation.

## Working Preferences
- User is a first-time game developer.
- Do not assume programming knowledge or familiarity with game-development systems.
- Explain technical concepts/options when they become relevant.
- Prefer open-source tooling; current engine preference is **Godot**.
- Keep responses concise; use bullets and formatting to emphasize structure.
- When ambiguity would materially affect a large task, ask focused Q&A before proceeding.
- Use this Markdown file as persistent project context between chats.
- Avoid prematurely locking architecture or scope.

---

# 1. Project Concept

A sandbox RPG inspired by **shonen battle manga/anime** (example reference: *Naruto*), where the player controls a self-created character in a predesigned world.

The game has three tightly connected layers:

### Overworld
- 3D world map.
- Travel between locations should feel somewhat like *Mount & Blade* strategic-map movement.
- The world should continue to evolve while the player travels.

### Scene / Combat System
- Not conventional real-time action combat.
- Planning should feel turn-based: player selects abilities/actions and sequences the actions for the next round.
- After planning, actions play out in real time / timed resolution segments.
- Presentation should be somewhat abstracted rather than showing continuous character movement/combat.
- Fight presentation should use cut-away shots of characters performing actions, inspired by *NITRO GEN OMEGA*.
- Spacing is abstracted rather than simulated directly.
- A persistent **initiative bar / initiative state** represents who has the advantage to close distance and deal damage versus who is on the back foot.
- Combat should feel closer to a card game / auto-battler in decision structure than an action game.

### Campaign Sandbox
- Player creates one main character initially.
- Ideally the system later supports building a party.
- NPC leaders should use fundamentally similar systems to the player.
- The main distinction between the player character and NPC leaders can be scale: number of subordinates, contacts, missions, etc.
- Factions and NPCs have their own agendas and develop independently.
- NPC behavior should be influenced by personality traits plus cultural/religious beliefs.
- Shonen-style progression: learn techniques, train, build friendships/rivalries, take increasingly difficult missions, gain power/status, and potentially become a leader of a group/village (e.g. eventually becoming the equivalent of a Hokage).

---

# 2. Combat Design — Current Decisions

## Basic Rhythm
1. Observe / learn about opponent.
2. Plan a sequence of actions for the next round.
3. Actions consume time and relevant resources.
4. Prepared actions resolve during a timed execution segment.
5. Conditions and reactions can trigger during resolution.
6. Initiative shifts as actions and scene conditions change.
7. Return to planning.

## Action Sequences
- Player selects a **sequence of actions**, not merely one action.
- Main limitations are:
  - time required by each action;
  - available stamina/focus/resources.
- Defensive actions can remain prepared across turns.

## Defensive / Reactive Mechanics
Defense should evoke a card game's trap/reaction system:
- A defensive or reactive ability can be activated in advance.
- It triggers when a relevant opponent action/contest occurs.
- It can:
  - prevent an incoming effect;
  - mitigate it;
  - counter it;
  - create a reversal/punish opportunity.
- Desired combat feel: an opponent commits heavily to offense, neglects defense, and is punished by a prepared reaction.
- These should create quick, exciting reversals.

## Information / Uncertainty
- Player should know basic information about opponents.
- Exact move sets/resources should remain partly uncertain.
- Example: player may know an opponent has roughly 3–4 strength-based abilities without knowing every detail.
- **Insight** can be spent to reveal more information.
- Fights should encourage combatants to feel each other out before committing to all-or-nothing moves.

## Initiative
- Initiative is a persistent **tug-of-war**, not simply a per-turn initiative roll.
- Initial initiative is determined by character stats and scenario.
- Example: surprise can create a massive initial initiative advantage.
- Actions and changes in the scene continuously alter the initiative value.
- Initiative helps represent who can close distance / deal damage and who is on the back foot.

## Determinism
- Combat should play more like a card game where choosing abilities and sequencing decisions determines the outcome.
- Randomness should not be the primary determinant of victory.

---

# 3. Resources & Attributes

Important distinction: **attributes/thresholds** are not necessarily spent, while some pools are explicitly consumable.

## Current Resources / Characteristics
- **Strength**
  - Threshold / capability stat.
  - Example: enough Strength may be required to use a heavy technique such as “Combat Hammer.”
  - Strength itself is not necessarily consumed when using such a move.
  - Can be reduced by injury.

- **Quickness**
  - Threshold / capability stat.
  - Relevant to physical contests and initiative.
  - Can be reduced by injury.

- **Stamina**
  - Spendable resource.
  - Limits physical exertion/action sequencing.
  - Can be injured/damaged at multiple levels, including reduction of current stamina and stamina regeneration.

- **Focus**
  - Newly added spendable resource alongside Stamina.
  - Used for concentration/mental/technical effort.
  - Recovery should generally be slower/structured than simple constant refill.

- **Wits**
  - Spendable tactical resource.
  - Can generate advantages through positioning, environment, improvisation, etc.
  - Regenerates over time.
  - High-Wits-regeneration characters may convert early initiative into strong tactical positions.

- **Insight**
  - Spendable information/observation resource.
  - Used to reveal more detail about opponents and their abilities.
  - Regenerates over time.

- **Chakra / Spirit / Mana**
  - Spendable supernatural resource.
  - Early techniques should have relatively low requirements.
  - Regeneration should feel somewhat slower than Stamina.
  - Supreme/exceptional ninjutsu, genjutsu, magic, etc. require progression/unlocking.

- **Courage**
  - New character characteristic/system.
  - Primarily affects resistance to fear and ability to discount / resist certain attacks or effects.

## Attribute Scale
- Current thinking is a large numerical scale, approximately **0–300+** rather than 1–100.
- Rough interpretation:
  - ~100 = standard/basic competent range;
  - 64 can still be meaningfully better than basic depending on the relevant baseline/context;
  - 200+ = legendary.
- Exact calibration is **not yet locked**.
- Traits should modify baseline stats and should include both positive and negative modifiers, ideally with irregular values rather than clean round numbers.

## Build Philosophy
Multiple viable archetypes are required:
- Highly specialized “genius” builds (e.g. genjutsu, taijutsu, ninjutsu) should be extremely powerful within their domain.
- All-rounders should remain effective when piloted intelligently and supported by information/strategy.
- Stealth-focused or situational specialists should be capable of succeeding at missions that stronger combat specialists cannot, because they are suited to the particular mission requirements.
- Different regeneration profiles should create meaningful playstyles.

Example:
- High Stamina regeneration: absorb chip damage, conserve/prepare, then unleash a large critical attack.
- High Wits regeneration: seize early tactical advantage and convert it into positioning/tempo.

---

# 4. Injuries / Damage Model

## Core Principle
There is **no single universal HP/condition ladder** defining overall health.

Instead:
- Injuries are described anatomically.
- Each injury impacts the associated game systems.
- A character’s overall combat condition emerges from accumulated wounds and their effects.

## Injury Effects
An injury may affect:
- current resource value;
- maximum/capacity;
- regeneration rate;
- attribute value / threshold;
- access to specific abilities;
- ability effectiveness;
- other logical downstream systems.

Example intent:
- A leg injury can reduce Quickness and/or current Stamina and potentially reduce Stamina regeneration.
- A mental injury could affect Focus/Insight or relevant abilities.

## Severity
- Do **not** impose one universal severity ladder such as “Bruised → Wounded → Critical.”
- Severity is a characteristic of each individual wound/injury.
- Overall injury state is tracked through the collection of wounds and the resulting changes to stats, resource pools, and regeneration.
- Injury names/descriptions should communicate the anatomical damage and severity.

## Death
- Some battle scenes can explicitly be to the death.
- NPCs can permanently die.
- Player can eventually die.
- For the current version, player can save freely and reload an earlier save before death.
- Marriage/children and generational time skips are a future system, not current scope focus.

---

# 5. Scene / Encounter Framework

- Not all scenes are battles.
- Each scene should have a **defined win condition / objective**.
- The same underlying contest/resource framework should power both combat and non-combat scenes.
- Different abilities can be useful depending on the scene.

Possible battle objectives include:
- defeat/kill opponent;
- force surrender;
- reduce Stamina to a threshold;
- reduce Strength or Quickness to zero;
- other scenario-specific objectives.

Non-combat scenes should reuse the same core systems but emphasize different abilities and information.

---

# 6. Techniques / Abilities

## Design
- Techniques are **named, descriptive, evocative abilities**.
- They should have a stable baseline identity.
- Example concept: **Scattershot** fundamentally does lower damage across more targets.
- Modifiers/tags can alter the base behavior and add effects.
- Abilities should generally **outnumber the slots available in a battle**, forcing loadout decisions.

## Tags / Descriptors
Elemental affinity and synergies are desired, but exact tag taxonomy is still early.

Tags should likely describe things such as:
- elemental affinity;
- range;
- execution time;
- target count/area;
- ability family/type;
- special conditions/effects;
- reactive/defensive behavior;
- other descriptive properties.

Some techniques are:
- instant;
- long execution;
- long range;
- contact/touch range;
- etc.

The game should remain fun with straightforward hand-to-hand combat even without elemental complexity.

## Acquisition / Modification
Ability acquisition should feel like a **mix of visual novel and deckbuilder**:
- Undertake missions.
- Perform personal activities / training.
- Interact with patrons, peers, opponents, etc.
- Gain new abilities from these interactions.
- Train to acquire specific techniques.
- Modify techniques.
- Potentially combine techniques.

Relationships and encounters can therefore directly affect both narrative and combat build development.

---

# 7. Character & Campaign Systems

## Player Character
- Player creates a custom protagonist.
- Character identity should include:
  - personality;
  - traits;
  - reputation;
  - relationships;
  - clan/background;
  - beliefs;
  - scars;
  - titles;
  - equipment;
  - other persistent campaign characteristics.

## Traits
- Traits can be innate/background/personality-derived.
- Traits can also be acquired through play.
- Existing traits can be modified/impacted by encounters and bonds.
- Traits contribute to baseline character stats.
- Trait modifiers should be mixed across stats, not simple all-positive buffs.

## Relationships / Bonds
Bonds should potentially affect:
- narrative/events;
- stats and traits;
- technique acquisition/modification;
- combat cooperation;
- other campaign systems.

## Progression
- Player discovers and learns new moves.
- Builds relationships and rivalries.
- Undertakes more difficult missions.
- Gains greater rewards and access.
- Eventually can become leader of a group/village.
- Long-term fantasy includes becoming the equivalent of the **next Hokage**.

## Future Generations
Future vision includes:
- marriage system;
- children;
- time skip;
- player taking control of a next-generation character.

This is explicitly **future scope**, not initial implementation scope.

---

# 8. World Simulation

- Pre-designed world, but highly systemic/emergent campaign.
- Competing factions.
- NPCs have individual agendas.
- Individual personality traits influence behavior.
- Culture and religious tenets influence people/factions.
- NPCs should act while the player is elsewhere.
- NPC leaders ideally use similar character/combat systems to player-controlled characters.
- Difference between player and NPC leaders should largely be scale: followers, contacts, mission requests, organizational reach, etc.

---

# 9. Technical / Production Direction

## Current Preference
- **Godot** as preferred game engine.
- Preference for open-source tools generally.

## Pipeline Topics To Design Later
- Godot project structure.
- Version control / Git.
- Asset folders and naming conventions.
- 2D/3D art workflow.
- Animation workflow.
- VFX.
- Music.
- SFX.
- UI.
- Fonts.
- Import/export formats.
- Asset licensing/attribution.
- Data/configuration architecture.
- Save system.
- Localization, if needed.
- Testing and debugging workflow.
- Build/release process.

Do not make specific tooling/architecture decisions until the game’s presentation and scope are sufficiently defined.

---

# 10. Current Open Questions

These were the next intended design questions when the handoff occurred:

1. **Core attributes:** What is the final permanent attribute list besides Strength, Quickness, Wits, Insight, Courage, and Focus? Should Stamina and Chakra be attributes as well as derived/spendable pools, or only resources?
2. **Descriptor tags:** What exact tag families should exist beyond elemental affinity?
3. **Technique modification:** Are tags inherent to techniques, or can characters acquire/change tags through training/relationships?
4. **Bonds:** Exactly how broadly should relationships affect stats, abilities, combat cooperation, and narrative?
5. **World scale:** One large contiguous 3D world or several regions/villages connected by the overworld?

These questions should be answered before locking the next design layer.

---

# 11. Recommended Next Documentation Sequence

1. Finalize the **character stat/resource model**.
2. Define the **ability/technique data model and tag system**.
3. Define the **initiative + action sequencing system**.
4. Define the **injury model** in enough detail for prototyping.
5. Define the generic **scene/contest framework**.
6. Define the **world/faction/NPC simulation model**.
7. Define **progression, relationships, training, and technique acquisition**.
8. Define the **minimum vertical slice**.
9. Choose the concrete Godot architecture and production tools.
10. Create the implementation repository/project structure.

---

# 12. Important Design North Stars

- **Player decisions should drive outcomes.**
- **Combat should produce reversals and tactical tension, not primarily RNG swings.**
- **Information is a resource.**
- **Preparation matters, but overcommitting should create counterplay.**
- **Character specialization should be powerful without invalidating generalists or situational specialists.**
- **The same systemic foundation should support combat and non-combat scenes.**
- **The world should feel alive independently of the player.**
- **The player’s story should emerge from interacting systems, relationships, missions, rivalries, and progression rather than only from a fixed plot.**
- **Named techniques should feel distinctive even when modified by a shared tag system.**

---

# 13. Handoff Instructions for Future Chat / Agent

Start by reading this file and treating sections 1–8 as the current working design.

Do not treat unresolved items as settled.

When a new design choice affects an existing section:
- identify the dependency;
- ask targeted Q&A when the choice is ambiguous and materially affects architecture/scope;
- update this file with the resulting decision;
- preserve a short decision rationale where useful.

The project is still in **pre-production / design discovery**. No production architecture should be considered final yet.
