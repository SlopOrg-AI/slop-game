# 00 — Steer (read first)

**Codename:** Shinobi Master (working title only — see Open #7) · solo dev · PC/Steam · Godot 4.x / GDScript · hobby cadence
**Updated:** 2026-09-20 (v2 restart, D5.1). Design detail: system docs 10–31. Decision history: `decisions.md`.

## 1. Vision (one paragraph)

**This paragraph and `01-pillars.md` are together the test** every design, art and scope question is held against — not a pitch, and neither half alone (C26, `sys.3`; owner 2026-09-20). A proposal must serve the vision **and** a named pillar, or it is out.

Turn-based card battler with a persistent campaign and world state. Create a shinobi, learn techniques, build bonds and rivalries, rise to lead a village. Combat is a duel of **planning and reading**: play cards from a hand, arm hidden reactions — no slot, an earmark each round (D5.25, `sys.1`) — and fight over **nested initiative** tug-of-wars, pair inside team inside fight, while distance is played out on the map (`sys.2`); the fighter who *understands* the opponent turns the tables. Decisions carry the weight: outcomes are deterministic and variance sits in the draw (D5.35). There is no HP — damage is a named, anatomical wound that closes options rather than lowering output. One actor model, one scene runner, one condition system at every scale: the duel, the village and the war are the same rules with the camera moved. Everything is staged on **one table**: a sculpted terrain map for travel, dioramas set down on it for locations, painted cut-out standees inside them for fights — only the camera changes scale. The world is post-post-apocalyptic and deliberately anachronistic: each region carries its own time-and-place markers, from pre-industrial to a vaguely-recognizable Y2K ceiling. Above the duel, a sandbox campaign tracks political and personal ties; an overworld carries you between them.

## 2. Where we are

**Phase: pre-production → Godot 1v1 duel demo.**

- v1 (`C:\Claude`, 2026-09-19/20): three design sessions settled the combat core; an HTML wireframe (`combat-1v1-v4.html`) ran AI-vs-AI; a one-day Godot port was archived for compounding scope before any human played. **No human has played a duel yet.**
- v2 (this folder): distilled restart. Disk is canon, `decisions.md` arbitrates, new decisions start at D5.1.
- **Session 6b (2026-09-20, Cowork design session) — read before any 10–15 distillation, schema or demo work:** the owner reconsidered combat foundations (resolution order, reach/initiative, damage numerics, draws/stars/gold, reserves as instantiated pools, sheets per actor kind, tag chemistry + materials, magic traditions, attribute Push). Owner direction (C1–C20) and the resulting model are PROPOSED in `proposals/2026-09-20-session-6-handoff.md` (+ `…-ontology-draft.md`, `…-successor-review.md`); **partly promoted 2026-09-20: C1 → D5.25, C3 → D5.26; the attribute economy and the card/hand model are D5.30–D5.37; C12/C17/C19 deferred; next free is D5.38** (D5.16–D5.23 are the same-day inspiration-index session; **D5.24 is cited in `11`/`14`/§6 below but not yet in `decisions.md`** — being resolved next alongside C20/C13). Until promoted, treat D2.8/D2.12 (reach on the bar), D2.13 (trick-taking) and the §4 boundary below as under review.
- **D5.2:** Godot from the start, basic screens included. **Screens are disposable; components persist.** A component library models what the image-gen boards show; each selected board is decomposed into components and recomposed as a screen. Guard against the v1 failure mode: every screen change is a reaction to a human play session or a selected board, not to an agent's plan.

## 3. Priorities (in order)

1. **Godot demo M1 — playable duel with basic screens.** Engine + JSON data + loadout screen + duel screen (queue, armed reaction, initiative bar, wound list, log) + table-view stub. Goal: a human plays 10 duels.
2. **Art + UI exploration loop** in parallel (owner-run image gen via ChatGPT / 5090; Claude critiques; `40-production.md`): character/pose cut-outs → diorama/table look → ability selector + targeting. Selected boards go straight into the M1 screens.
3. Resolve the combat opens that human play surfaces (§6 #1–#4).
4. **Godot demo M2 — staged duel.** Table view ↔ cutaway, cut-out standees, selector from #2.
5. Only after 1–4: location/diorama layer, then campaign.

## 4. MVP boundary — "one 1v1 duel in Godot"

**IN**
- Two characters from JSON; player vs scripted AI (AI must remember "was I countered last round?").
- Stat model: 5 attributes · 3 reserves · 2 meters · 3 guards. Scale 0–300, irregular values.
- Round: **Plan → Resolve** (D5.8). Actives and passives committed together, hidden. No reveal; learn by watching. Budget = **attribute checks at resolution (D5.30)**; a failed check locks the card out for the scene (D5.32). Order = trick-taking by requirement sum (D2.13, confirm in play).
- Initiative bar −50…+50, reach −10, Dominant ≥+25, Desperate ≤−25.
- Insight: hidden meter, partial spend as initiative modifier or reveal; cap Wits/2, drained on reaction fire (D3.2, confirm in play).
- Ability kinds (D5.9): activated · reaction · sustained · decaying · one-off; `hold`/`upkeep` costs. **Kind governs only how an ability resolves (D5.25); reactions and passives are ordinary abilities chosen in Plan, no slot, no armed cap.** Reactions graded by trigger specificity; reversal = ability delta only (D3.3); held reserve excluded from refill (D3.4).
- Information model (D5.10) in the engine: fact × knower-tier × surface; tiers advance by witnessing, Insight reveal, winning. Unknown abilities show as magnitude bands. Minimal bestiary screen.
- Damage: tag stack → guard → **tiered states** (D5.14) → severity band → named wound. ~12 wounds. Magnitude from the card's check (D5.30, supersedes D3.1). A wound lowers an attribute, which pushes cards below their checks — **damage closes options rather than reducing output**.
- **Engine constraints (D5.12):** actor {scale, kind, stats-from-data}; scene {scale, parent, children}; selectable-actor list data-driven. M1 shows one character each side; the code never assumes it.
- Win/exit: courage break · incapacitation · surrender · kill · **escape** (D5.33) (scene-flagged).
- ~16 abilities (4 reactions, 3 insight openers). Variance: per-ability band on 2 abilities (D2.15), revisit after play.
- Scene conditions engine; **footing** and **light** authored.
- **Deck construction** screen, three decks by class: body/mind/spirit (D5.35; no reaction slot — D5.25). In play: choose a deck, draw one card per draw step, up to hand size.
- M1 presentation: basic Godot screens + text log, restyled as image-gen boards are selected. M2: pose-swap cut-outs, table view ↔ cutaway.

**OUT** (TARGET / FUTURE — designed, not built)
- Party scenes: named + group actors, **team sheet with combos** (D5.12) — TARGET. Blocking open: initiative model for 3+ sides.
- Location node map + dioramas, overworld terrain table, campaign, factions, NPC sim.
- Knowledge channels beyond witness/reveal/win: teaching, inheritance, bestiary factions, group knowers (D5.10) — TARGET/FUTURE.
- World systems (`50-world-systems.md`, FUTURE): settlements as actors, ecology teaches, nested scales, marks/legacy.
- Technique acquisition, traits, bonds, progression, Heart stances, generations.
- Animation beyond pose swap + cut-out transforms; VFX; music; save system.

## 5. Doc map

| Doc | Role |
|---|---|
| `01-pillars.md` | Pillars, influence allocation, anti-goals |
| `10-combat-loop` `11-initiative` `12-reactions-passives` `13-damage-wounds` `14-scenes-conditions` `15-information` | Combat + information systems (MVP) |
| `20-campaign` `21-world-factions` | Campaign, overworld, world (TARGET/FUTURE) |
| `50-world-systems` | Settlements as actors, ecology, scale hierarchy, nesting, legacy (FUTURE) |
| `30-art-direction` `31-ui` | Presentation grammar, art rules, interface |
| `40-production` | Tool roles, Claude Code pipeline, demo milestones, image-gen loop |
| `decisions.md` | D-log. Later entry wins; docs get corrected |

## 6. Open decisions (highest leverage first)

| # | Question | Status | Doc |
|---|---|---|---|
| 1 | Variance mechanism — **largely answered by D5.35**: variance is in the draw, outcomes stay deterministic. Per-ability band (D2.15) now probably redundant | OPEN (narrowed), gated on play | 10 |
| 2 | D2.13 trick-taking interleave — confirm reading | OPEN, gated on play | 10 |
| 3 | ~~Slots for passives/reactions~~ | **CLOSED — D5.25**: a false question; reactions and passives are ordinary abilities, concurrency limited by cost | 12 |
| 4 | Wound regions — head/torso/arms/legs + mind + spirit | OPEN (confirm) | 13 |
| 5 | Initiative model for N-vs-M — per-actor / per-side / pairwise (actors *within one* engagement; cross-engagement scoping is separate — see D5.24) | OPEN, blocks TARGET | 11 |
| 6 | Ability selector + targeting — radial start; how actives point at targets/teams | OPEN → image-gen loop | 31 |
| 7 | Title — codename only; decide after demo, from world or core verb | OPEN | 00 |
| 8 | Reactions on a **stack** (LIFO vs the action they answer) or inline in trick-taking order | OPEN | 10 |
| 9 | Knowledge ownership: character (inheritable, default) vs player meta-progression; NPC symmetry (default yes) | OPEN, defaults set | 15 |
| 10 | Cultures as knowers, or only organized groups with culture as identification modifier | OPEN | 50 |
| 11 | Minion groups: literal roster (members can be named later) vs abstract strength | OPEN | 50 |
| 12 | UI numbers — raw vs bands (bands now the info-system default for unknowns) | OPEN, low stakes | 31 |
| 13 | Mind's second attribute — Courage went to spirit (D5.36), so mind is Wits alone. Mental-channel damage degrades Wits (reads decay), so this is a gap, not a hole | OPEN | 02, 10 |

## 7. Rules for agents

See `AGENTS.md`. Short form: disk is canon · D-number or it isn't decided · don't self-attribute owner decisions · don't expand MVP · `proposals/` for anything not instructed.
