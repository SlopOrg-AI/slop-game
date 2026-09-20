# Mission / scenario design — lead brief

Reports to: owner (via Production); umbrella `direction/README.md` · Directs: clusters → Content · Updated: 2026-09-20

## Charter
Authoritative on **what happens**: the encounter as staged — which actors, which loadouts, what the opponent does and remembers, win conditions in play, pacing of a fight, and later the mission that puts the player in the scene. Owns the human-play loop's *setup*: the 10 duels the owner must play are ten scenarios, not one. Feeds findings from play back to Systems as evidence.

## Owns
- M1 scenario set: opponent scripts (must remember "was I countered last round?" — findings-02 F5), loadout presets, win-condition flags per scene (courage break · incapacitation · surrender · kill)
- Playtest protocol: what the owner records per duel; findings → `proposals/<date>-play-<n>.md`
- Later: mission/encounter templates at scale 1–2 (TARGET), campaign scenario structure with `20`
- Comps: Blades in the Dark / PbtA fail-forward *as staging feel* (rules side is Systems'), CK3 characters-generate-history (TARGET)

## Does NOT own
- Resolution rules, AI as an engine component's *code* → Systems / Tech · space → Level · look → Art · which abilities exist → Content (Scenario picks from them)

## Reads first
`AGENTS.md` → `00-steer.md` §3 #1, #3, §4 win conditions → `01-pillars.md` pillars 1–2 (reading beats rolling, commitment is exposure — the scenario must make these happen) → `proposals/2026-09-20-session-6-handoff.md` §3.7 (holding back, tells), §5 #8 → `data/characters.json`, `abilities.json`

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| — | no HTML play; wait for Godot M1 | handoff §1 | DECIDED (not D-logged) |
| — | goal: a human plays 10 duels | 00-steer §3 #1 | DECIDED |
| C11 | attributes readable on sight … unless the foe is holding back | handoff §2 | PROPOSED — Systems; scenario uses `restrained` opponents as a staging tool |
| — | M1 content adds candidate list (`restrained`, Blood, Sand Shield fighter, …) | handoff §5 #8 | OPEN — Scenario recommends which make the 10 duels *teach* something |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| Opponent AI with counter-memory | DECIDED (behaviour), not built | MVP | 00-steer §4, F5 |
| Cluster `ai-m1` (scripted opponent behaviours) | to define | MVP | — |
| Cluster `duels-m1` (10 scenarios: loadouts, opponents, win flags) | to define | MVP | — |
| Playtest protocol | to write | MVP | — |
| Missions / encounters at scale 1–2 | dormant | TARGET | 20 |

## Next actions
1. Write the playtest protocol (one page: what to note per duel, mapped to `00-steer` §6 opens #1–#4 and handoff §5). Gate: none.
2. Recommend which §5 #8 adds go into M1 by what each duel is meant to surface (e.g. `restrained` tests pillar 1; Blood tests the pools model). Gate: Systems' schema direction.
3. Define `ai-m1` and `duels-m1` clusters in handoff form. Gate: `12` distilled (abilities/lanes) + Content's 17.

## Open questions
1. Does the opponent get *knowledge* (D5.10 NPC symmetry, default yes) in M1, or only counter-memory?
2. Are the 10 duels a fixed ladder or free selection?

## Escalates to
Systems for anything the scenario needs the rules to do; Owner for M1 scope.
