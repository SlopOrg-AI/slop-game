# Systems — lead brief

Reports to: owner · Directs: `systems/content.md`, `systems/tech.md` · Updated: 2026-09-20 (queue round 1 rulings recorded — §Pending)

## Charter
The game itself: **what exists** (ontology — entities, actor kinds, sheets, pools, tag dictionary, materials, scenes/zones, naming) and **how it resolves** (rules — Plan→Resolve, precedence, momentum, damage→mint, information, chemistry, Push). Scale-generic by pillar 6: campaign and world systems are the same rules at scale 2–4, not a second sim. Arbitrates vocabulary for every other lead; the ontology is Tech's contract.

## Owns
- `design/02-ontology.md` (to create), `data/SCHEMA.md`, `data/tags.json`, `data/materials.json`, sheets/pools definitions
- `design/10–15` (combat/information), `20-campaign`, `50-world-systems`
- `design/decisions.md` edits **on owner instruction only** (rule 4)
- Schema versions (one D-number per bump); the validator's *rules* (Tech writes the script)

## Does NOT own
- Instances (which 17 abilities, Kaede/Genzo, factions, lore) → Content · Godot code → Tech · look/feel, space *aesthetics*, encounter authoring → Direction · milestones → Chief of Staff

## Reads first
`AGENTS.md` → `00-steer.md` → `01-pillars.md` → `proposals/2026-09-20-session-6-handoff.md` (§2 C-refs, §3 model, §4 corrections) → `…-ontology-draft.md` → `decisions.md` latest → the one doc being touched

## Pending — local refs awaiting promotion (D5.44-EP)
| Local ref | Decision, one line | Ruled | Promoted |
|---|---|---|---|

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| **C25** | earmarks clear each round; arming earmarks that round; earmark = the ability's check | queue-verdicts-1 Q1 | **RECORDED → `sys.1`**; rule text in `proposals/2026-09-20-initiative-and-earmarks.md` §2–§4 |
| — | Q2: nested bars (pair · team · fight), distance on the map | queue-verdicts-1 Q2 | **RECORDED → `sys.2`** (C13 + C20 promoted); rule text in the same proposal §5 |
| **C26** | vision paragraph + pillars are together the test, not pitch-only | queue-verdicts-1 Q3 | **RECORDED → `sys.3`**; `00-steer` §1 corrected 2026-09-20 |
| **C27** | *distilled* = ontology/schema + synthesis + no STUB, no MVP OPEN | queue-verdicts-1 Q6 addendum | **RECORDED → `sys.4`**; `demo/README.md` gate and `40-production.md` open #3 cite it |
| — | "multi-attribute abilities earmark all corresponding attributes" | chat 2026-09-20, relayed by Chief of Staff | **RECORDED → `sys.5`**; proposal §2a |
| — | MtG hold-up framing · "reserves should primarily be fuel for immediate moves, with a bit committed to maintenanc requirements" · the 10–30 / 50 / 66% dial | chat 2026-09-20, relayed by Chief of Staff | **RECORDED → `sys.6`**; proposal §2 rewritten around it, §2b fork struck. One question raised back: upkeep % vs flat (§7 #1) |
| C1, C3 | reactions-as-abilities · no ability modes | Cowork 2026-09-20 | **PROMOTED → D5.25, D5.26** |
| C12, C17, C19 | gold = two classes · Devotion · provisional terms | Cowork 2026-09-20 | DEFERRED — ride with C10, the traditions cluster, the ontology pass |
| C7, C9, C10 | consistent % -of-stat damage · weighted attribute pull · fixed-at-acquisition distribution | Cowork 2026-09-20 | **ABSORBED → D5.30** (the pull is now a `check`; no in-fight dial) |
| C18 | Push — spend attributes at critical moments | Cowork 2026-09-20 | OPEN, reshaped — now overlaps the D5.32 momentum unlock and "force a failed check"; decide which hat it wears |
| C11 | attributes readable on sight; holding back | Cowork 2026-09-20 | OPEN — `restrained-N` (ontology draft §2 F) remains the mechanism; it never needed a commitment dial |
| C2, C4–C6, C8, C13–C16, C20 | RPS precedence, tag dictionary, materials, damage tags+numbers, stars, range/space, magic traditions, instantiated reserves, sheets, nested tug-of-wars | Cowork 2026-09-20 | PROPOSED — walk continues, one at a time → D5.38+ |
| — | D5.24 (engagement-scoped initiative) cited in `11`, `14`, `00-steer` §6 but not in `decisions.md` | handoff §1b | **RESOLVED inside `sys.2`** — "engagement" = the team bar; no separate rule, no separate number. Citations in `11`/`14`/`00` §6 re-point at `sys.2` when the proposal is applied |

## Status
| Item | Status | Scope | Source |
|---|---|---|---|
| `00`, `01`, `12`, `15`, `50` | written | mixed | D5.x |
| `10`, `11`, `13`, `14`, `20` | STUB | MVP (20: TARGET) | — |
| `02-ontology.md`, `data/SCHEMA.md` | not created | MVP | handoff §6 B |
| `data/*.json` | v1 schema; drift vs D5.9 / D5.12 / D5.14 documented | MVP | data/README |
| `12-reactions-insight.md` | **deleted 2026-09-20** (mechanical housekeeping, Claude Code; the rename was D5.9) | — | successor-review |
| `decisions.md` `Acts on it` column | added + backfilled D5.1–D5.23 (Tech / Vocabulary / Designers / Content / Art / Production) | — | D5.25 session |
| Reach-on-bar (D2.8/D2.12), trick-taking (D2.13), `00-steer` §4 boundary | UNDER REVIEW pending C-ref promotion | MVP | handoff §1b |
| Attribute economy: `check` at resolution, commit-for-round, toggle-off, lockout | DECIDED | MVP | D5.30–D5.32 |
| Cards + three class decks + draw step; `draw` reserved for cards | DECIDED | MVP | D5.34, D5.35 |
| Courage = spirit attribute | DECIDED | MVP | D5.36 |
| Escape as fifth exit | DECIDED | MVP | D5.33 |
| `02-ontology.md` momentum row (per-actor) vs C20 (nested shared) | CONFLICT — draft must be corrected when 02 is written | MVP | ontology draft §2 D |
| `11-initiative.md` status table asserts D5.24 DECIDED | CONFLICT — CLEARS when `sys.2` is promoted and the proposal applied; until then the row is still unbacked | MVP | `11` |
| Damage as option-denial (channel closes the matching deck) | PROPOSED — agent synthesis of D5.36 + D5.30 | MVP | c-coherence §4b |
| Earmark economy (per-round, every check, two resources) · nested bars · `D5.24` | RECORDED, rule text drafted, **not yet in `10`/`11`/`12`** | MVP | `sys.1`, `sys.2`, `sys.5`, `sys.6`; `proposals/2026-09-20-initiative-and-earmarks.md` |
| ~~Attribute or reserve?~~ | **CLOSED — `sys.6`: both, different jobs.** Attribute = capability, reserve = economy | MVP | `sys.6` |
| `upkeep` — % of own reserve, or flat | **RAISED, with the owner** (proposal §7 #1). Blocks `data/SCHEMA.md`'s `upkeep.per_round` type and any authored ability number | MVP | `sys.6` |
| D3.4 (held reserve excluded from refill) | **SUBJECT RETIRED by `sys.6`** — must be marked superseded when Tech logs. Still cited in `00-steer` §4 and `12` | MVP | `sys.6` vs D3.4 |
| `12-reactions-passives.md` §"Costs per ability: `hold` … and/or `upkeep`. Any kind may use either" | DEFECT — `hold` is retired and `upkeep` is now mandatory for persisting kinds; not fixed (no owner instruction) | MVP | `12` vs `sys.6` |
| `12` §Commitment: "un-fired reaction persists, cost locked, stands unless play says otherwise" | DEFECT — contradicted by `sys.1`; not fixed | MVP | `12` vs `sys.1` |
| `00-steer` §4: "`hold`/`upkeep` costs" · "held reserve excluded from refill (D3.4)" | DEFECT — both now wrong; §1 was this session's only mandate, so §4 untouched | MVP | `00` vs `sys.6` |
| `data/abilities.json` carries v1-schema `hold` fields | DEFECT — dead key on every ability; Tech's to strip with schema v3 | MVP | data/README |
| `00-steer` §1 as the test, with pillars 3 and 6 | DONE 2026-09-20 | all | `sys.3` |
| "Distilled" defined; `demo` gate + `40` open #3 cite it | DONE 2026-09-20 | MVP | `sys.4` |
| `12-reactions-passives.md` §Slots + status row still print `OPEN #3` | DEFECT — D5.25 closed it; not fixed (no owner instruction) | MVP | `12` |
| `demo/README.md` says "10–14 system docs", `40-production.md` §4 says "10–15" | DEFECT — one of the two gates is wrong; not fixed | MVP | `demo`, `40` |

## Next actions
1. **Close the card model** (owner present): hand persistence between rounds · where a gold two-class card lives · deck exhaustion/reshuffle · hand size and what sets it. These block `02-ontology` because they change what a character *is*. **Put proposal §2b (earmark on the attribute or on the reserve) to the owner in the same exchange** — it is forked, not open, and it blocks the actor record in schema v3. Gold's arming cost is now known (`sys.5`: both classes), which should inform where a gold card lives.
1a. **Apply `proposals/2026-09-20-initiative-and-earmarks.md` to `10`/`11`/`12`** once Tech promotes `sys.1`/`sys.2` (owner instruction needed to write canon: `AGENTS.md` rule 5). Same pass fixes `12`'s stale `OPEN #3` and re-points the `D5.24` citations in `11`/`14`/`00` §6 at `sys.2`. Then archive the proposal (P3).
1b. Done 2026-09-20 (this session): `sys.1`–`sys.5` recorded · `00-steer` §1 corrected (C26, + pillars 3 and 6) · `demo/README.md` gate and `40-production.md` §4 / open #3 / status row cite C27 · rule text for the earmark economy and the nested bars drafted to `proposals/`. **Owed to Chief of Staff:** four queue rulings now hold references (board rows A1, A2, A3, A6 clear); `D5.24` is resolved inside `sys.2` and needs no number of its own; `sys.5` is a fifth ruling, same-session, taken straight from chat; **one fork goes back up** (proposal §2b); two defects logged in §Status that Systems could not fix without an owner instruction; `STATUS.md` §Pending promotion cites an `§Action register` in `inbox/2026-09-20-queue-verdicts-1.md` that does not exist in that file.
1c. Earlier, 2026-09-20: C1 → **D5.25**, C3 → **D5.26**; the `Acts on it` column added and backfilled; **D5.30–D5.37** logged; `00-steer` §2/§4/§6, `data/README.md` and `proposals/2026-09-20-c-coherence.md` updated to match.
2. `02-ontology.md` + `data/SCHEMA.md`, one section per exchange, PROVISIONAL/LOCKED column on every term (C19). Gate: action 1. **Both are now gate conditions for every distilled doc (`sys.4`), so nothing in `10`–`15` can clear the demo gate until they exist.**
3. Distill `10 → 11 → 13 → 14 → 12 → 15` against the ontology to the `sys.4` standard, citing D-numbers or local refs; compress D1–D4 during `10`. Gate: action 2.

## Open questions
Handoff §5 #1–#11, minus Courage's class (closed, D5.36). Added by session 6e:
1. Hand persistence between rounds; hand size and what sets it.
2. Where a gold (two-class) card lives — either deck, its own deck, or fixed at acquisition. Gold now checks **both** classes, so it is doubly darkenable; the deck answer should pay for that.
3. Deck exhaustion — reshuffle, or does running out mean something?
4. The mind class's second attribute (`00-steer` Open #13), now that Courage is spirit.
5. Whether Grit and Will earn two separate guards, or terror is one thing with two flavours.
6. What C18 Push is, now that D5.32 unlocks on momentum and "force a failed check" is available as its shape. `sys.2`'s pair-bar Dominant gate depends on the answer.

Added by this session (`sys.1`, `sys.2`, `sys.5`, `sys.6` — detail in `proposals/2026-09-20-initiative-and-earmarks.md` §7):
7. ~~Which `check` is the earmark~~ **RULED, `sys.5`: all of them.** ~~Attribute or reserve~~ **RULED, `sys.6`: both, different jobs.** Live in their place: **is `upkeep` a percentage of the actor's own reserve or a flat cost?** Raised, with the owner — it decides whether reserve depth differentiates builds.
8. Does upkeep clear **before or after** refill at end of round, and does a darkened ability's upkeep stop that round or the next? Written as *next* round in the proposal; neither ruling speaks, and it decides whether darkening is relief or sunk cost.
9. Team- and fight-bar thresholds. Unset, and should stay unset until a party fight is played.
10. When Σ held exceeds the attribute, **the player chooses** what darkens (`sys.6`). Does the AI choose by the same rule, and is the choice made at the moment of the wound (a mid-round interrupt) or at the next Plan (cheaper, may feel worse)?

## Board row
| Lead | Phase | Blocked on | Next action | Updated |
|---|---|---|---|---|
| Systems | five rulings recorded as `sys.1`–`sys.5` (earmarks per round · nested bars + `D5.24` · vision+pillars as the test · "distilled" · multi-attribute earmarks); `00-steer` §1, `demo` gate and `40` open #3 corrected; earmark + initiative rule text drafted to `proposals/` — **not applied to `10`/`11`/`12`** | **owner: proposal §2b — is the earmark on the attribute or the reserve?** (forked, blocks schema v3's actor record) · owner instruction to write `10`/`11`/`12` canon · Tech to promote `sys.1`–`sys.5` | §2b + card model (owner present) → `02-ontology` + `SCHEMA.md` → apply the proposal | 2026-09-20 |

## Escalates to
Owner. Rule for the lead: if a v1 rule and an unpromoted C-ref conflict, write the v1 rule and flag the conflict — never silently harmonise.
