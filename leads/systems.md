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
| `sys.7` | **Upkeep is an authored cost, not a percentage.** Owner, verbatim: *"upkeep is defined cost, goes back to how you can tune card ability requirements and then the value is set for the encounter."* An ability card carries an **upkeep number in points of its named reserve**, authored on the card and identical in every pair of hands; it is **the tuning dial** — you balance a card by what it costs to keep up. The owner's earlier 10–30% / 50% / 66% figures become **outcomes** of that number against a given actor's reserve — a sanity check for authors, never a formula. Completes D5.51-CES, which gave upkeep a magnitude but not a kind, and unblocks `upkeep.per_round` in schema v3 as an **integer** (a value below 1 is an authoring error, not a fraction); `upkeep` belongs on the ability **template** beside `cost`, while D5.50's `checks{}` stays on the per-owner **instance**. **The asymmetry with D5.30 is intended, not a clash** — a check scales with the holder, an upkeep does not: skill is personal, fuel is not, and a torch burns the same oil whoever carries it. Its price is the tuning risk the owner owns: one card is un-holdable below a given reserve depth and free above it. **Not settled by these words, raised back:** whether "set for the encounter" snapshots the proportion at encounter start or simply means the number does not drift — it matters because a reserve's max moves mid-fight when a wound hits its `max_from` attribute (proposal §7 #1) | 2026-09-20 | — |
| `sys.8` | **Every reserve is one kind of object: a pool with a max, a current value and its own regen rate — and its maximum is not derived from an attribute.** Owner, verbatim: *"chakra and magicka and related should be more like stamina with it's own regen rate. that should cohere."* Chakra is stamina-shaped, magicka is stamina-shaped; the attribute→pool-max coupling (`max_from: spirit attributes`, `max_from: body.force`) is deleted. **It coheres by completing D5.51-CES, not merely fitting beside it:** D5.51 split the resources by job — attribute is capability, reserve is fuel — and `max_from` quietly broke that split, since a Heart wound shrank the Chakra pool and so one damage event hit **both** currencies. Cutting the derivation makes it true that **damage touches capability, never fuel**. **D5.36 is unaffected and sharpened** — spiritual damage still degrades Heart/Courage, which still darkens the spirit deck and can still end the fight by courage break, because that whole chain runs through attributes; it simply no longer also drains the pool. D5.30/D5.31 untouched; `sys.7`'s authored upkeep is *cleaner* against a pool whose size stops moving; D3.4 was already dead. **Derived consequence, the tuning-critical one:** maintenance becomes a **rate** question — a defense is sustainable when regen covers its upkeep, and above that line holding is a countdown. **Dissolves** (does not rule) the open `sys.7` left about "set for the encounter": that question existed only because a pool could shrink under something already held. **Not settled, raised back:** regen's shape · where `max` comes from · whether anything still degrades a max mid-fight · whether regen can be suppressed — proposal §7 #2–#5. **Scoped:** the owner named reserves; guards and meters are other roles of the same pool object and are not assumed to take a regen rate. **Sand is not forced in** — §7a | 2026-09-20 | — |

**Cleared 2026-09-20** — Tech promoted and these rows left the queue (D5.44-EP; `Pending` is a queue, not an archive): `sys.1` → **D5.46-ES** · `sys.2` → **D5.47-AES** · `sys.3` → **D5.48-ACPS** · `sys.4` → **D5.49-EPS** · `sys.5` → **D5.50-CES** · `sys.6` → **D5.51-CES**. Both forms resolve to the same row forever, so docs citing `sys.n` stay correct. D5.46/47/50/51 are **logged, not closed** (D5.41-EP P2): their rule text is still in `proposals/2026-09-20-initiative-and-earmarks.md`, not in `10`/`11`/`12`.

## Inbox
| C-ref | Owner said | From | Status |
|---|---|---|---|
| **C25** | earmarks clear each round; arming earmarks that round; earmark = the ability's check | queue-verdicts-1 Q1 | **PROMOTED → D5.46-ES** (`sys.1`); rule text still in `proposals/2026-09-20-initiative-and-earmarks.md` §2–§4, not yet in `10`/`12` |
| — | Q2: nested bars (pair · team · fight), distance on the map | queue-verdicts-1 Q2 | **PROMOTED → D5.47-AES** (`sys.2`, C13 + C20); rule text still in the same proposal §5, not yet in `11` |
| **C26** | vision paragraph + pillars are together the test, not pitch-only | queue-verdicts-1 Q3 | **PROMOTED → D5.48-ACPS** (`sys.3`); `00-steer` §1 corrected 2026-09-20 — done |
| **C27** | *distilled* = ontology/schema + synthesis + no STUB, no MVP OPEN | queue-verdicts-1 Q6 addendum | **PROMOTED → D5.49-EPS** (`sys.4`); `demo/README.md` gate and `40-production.md` open #3 cite it — done |
| — | "multi-attribute abilities earmark all corresponding attributes" | chat 2026-09-20, relayed by Chief of Staff | **PROMOTED → D5.50-CES** (`sys.5`); proposal §2a |
| — | MtG hold-up framing · "reserves should primarily be fuel for immediate moves, with a bit committed to maintenanc requirements" · the 10–30 / 50 / 66% dial | chat 2026-09-20, relayed by Chief of Staff | **PROMOTED → D5.51-CES** (`sys.6`); proposal §2 rewritten around it, §2b fork struck. The question it raised back — upkeep % vs flat — is now ruled, `sys.7` |
| — | "upkeep is defined cost, goes back to how you can tune card ability requirements and then the value is set for the encounter" | chat 2026-09-20, relayed by Chief of Staff | **RECORDED → `sys.7`**; proposal §2.2, §2.2a, §6 |
| — | "chakra and magicka and related should be more like stamina with it's own regen rate. that should cohere" | chat 2026-09-20, relayed by Chief of Staff | **RECORDED → `sys.8`**; proposal §2.2b, §2.4, §6, §7 rewritten. **Dissolves** the open `sys.7` left; raises four new ones and leaves Sand (clash E) unforced |
| C1, C3 | reactions-as-abilities · no ability modes | Cowork 2026-09-20 | **PROMOTED → D5.25, D5.26** |
| C12, C17, C19 | gold = two classes · Devotion · provisional terms | Cowork 2026-09-20 | DEFERRED — ride with C10, the traditions cluster, the ontology pass |
| C7, C9, C10 | consistent % -of-stat damage · weighted attribute pull · fixed-at-acquisition distribution | Cowork 2026-09-20 | **ABSORBED → D5.30** (the pull is now a `check`; no in-fight dial) |
| C18 | Push — spend attributes at critical moments | Cowork 2026-09-20 | OPEN, reshaped — now overlaps the D5.32 momentum unlock and "force a failed check"; decide which hat it wears |
| C11 | attributes readable on sight; holding back | Cowork 2026-09-20 | OPEN — `restrained-N` (ontology draft §2 F) remains the mechanism; it never needed a commitment dial |
| C2, C4–C6, C8, C13–C16, C20 | RPS precedence, tag dictionary, materials, damage tags+numbers, stars, range/space, magic traditions, instantiated reserves, sheets, nested tug-of-wars | Cowork 2026-09-20 | PROPOSED — walk continues, one at a time → D5.38+ |
| — | D5.24 (engagement-scoped initiative) cited in `11`, `14`, `00-steer` §6 but not in `decisions.md` | handoff §1b | **RESOLVED inside D5.47-AES** — "engagement" = the team bar; no separate rule, no separate number. Citations in `11`/`14`/`00` §6 re-point at D5.47 when the proposal is applied |

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
| `11-initiative.md` / `14` assert D5.24 DECIDED | **HALF-CLEARED** — D5.47-AES now backs the rule, but both docs still cite a number that has no row. Re-point at D5.47 when the proposal is applied | MVP | `11`, `14` |
| Damage as option-denial (channel closes the matching deck) | PROPOSED — agent synthesis of D5.36 + D5.30 | MVP | c-coherence §4b |
| Earmark economy (per-round · every check · two resources · authored upkeep) · nested bars · `D5.24` | **LOGGED, NOT CLOSED** (D5.41-EP P2) — numbers settled, rule text still in the proposal, **not in `10`/`11`/`12`** | MVP | D5.46, D5.47, D5.50, D5.51 + `sys.7`; `proposals/2026-09-20-initiative-and-earmarks.md` |
| ~~Attribute or reserve?~~ | **CLOSED — D5.51-CES: both, different jobs.** Attribute = capability, reserve = economy | MVP | D5.51-CES |
| ~~`upkeep` — % of own reserve, or flat~~ | **CLOSED — `sys.7`: flat, authored on the card.** `upkeep.per_round` is an integer; schema v3 unblocked. The D5.30 asymmetry is intended — check scales with the holder, upkeep does not | MVP | `sys.7` |
| ~~"The value is set for the encounter" — snapshot or live?~~ | **DISSOLVED by `sys.8`, not ruled** — the question had a subject only while `max_from` let a pool shrink under something already held. No verdict to look for | MVP | `sys.7` → `sys.8` |
| Reserve = pool + max + current + **own regen rate**; `max_from` (attribute) deleted | RECORDED; **completes D5.51's two-resource split** — damage now touches capability, never fuel | MVP | `sys.8` |
| Regen shape · where `max` comes from · mid-fight max degradation · suppressible regen | **RAISED, with the owner** (proposal §7 #2–#5). Block the reserve object in schema v3 | MVP | `sys.8` |
| Sand (C15) — pool half yes, regen half no | **UNFORCED.** Fits only if refill has two channels (intrinsic `regen: 0` + resupply as an effect). `sys.8` **sharpens** the live clash `c-coherence` §2 E rather than settling it | MVP | C15, c-coherence §2 E |
| `02-ontology.md` / `data/SCHEMA.md` pool object: `max_from` | **DEFECT-IN-WAITING** — the ontology draft and session-6 §3.2 both specify `max_from`; neither is written yet, so this is a correction to make *before* they are, not after | MVP | handoff §3.2 |
| D3.4 (held reserve excluded from refill) | **SUPERSEDED by D5.51-CES — Tech has logged the marker.** Still cited as live in `00-steer` §4 and `12`; both are Systems' to correct and both need an owner instruction | MVP | decisions.md §D3.4 marker |
| `12-reactions-passives.md` §"Costs per ability: `hold` … and/or `upkeep`. Any kind may use either" | DEFECT — `hold` is retired and `upkeep` is now mandatory for persisting kinds; not fixed (no owner instruction) | MVP | `12` vs D5.51 |
| `12` §Commitment: "un-fired reaction persists, cost locked, stands unless play says otherwise" | DEFECT — contradicted by D5.46-ES; not fixed | MVP | `12` vs D5.46 |
| `00-steer` §4: "`hold`/`upkeep` costs" · "held reserve excluded from refill (D3.4)" | DEFECT — both now wrong; §1 was this session's only mandate, so §4 untouched | MVP | `00` vs D5.51 |
| `data/abilities.json` carries v1-schema `hold` fields | DEFECT — dead key on every ability; Tech's to strip with schema v3 | MVP | data/README |
| `00-steer` §1 as the test, with pillars 3 and 6 | DONE 2026-09-20 | all | D5.48-ACPS |
| "Distilled" defined; `demo` gate + `40` open #3 cite it | DONE 2026-09-20 | MVP | D5.49-EPS |
| `12-reactions-passives.md` §Slots + status row still print `OPEN #3` | DEFECT — D5.25 closed it; not fixed (no owner instruction) | MVP | `12` |
| `demo/README.md` says "10–14 system docs", `40-production.md` §4 says "10–15" | DEFECT — one of the two gates is wrong; not fixed | MVP | `demo`, `40` |

## Next actions
1. **Close the card model** (owner present): hand persistence between rounds · where a gold two-class card lives · deck exhaustion/reshuffle · hand size and what sets it. These block `02-ontology` because they change what a character *is*. **Put proposal §7 #2–#5 (the reserve object — regen shape · where `max` comes from · mid-fight degradation · suppressible regen) to the owner in the same exchange**; they block the pool object in schema v3, and #5 is where a designed damage→fuel link would live if the owner wants one. Gold's cost is now known on both sides (D5.50: both classes held; D5.51 + `sys.7`: an authored upkeep per round), which should inform where a gold card lives.
1a. **Apply `proposals/2026-09-20-initiative-and-earmarks.md` to `10`/`11`/`12`.** D5.46/47/50/51 are logged but **not closed** (D5.41-EP P2) precisely because their text is still in a proposal; only an owner instruction can move it into canon (`AGENTS.md` rule 5). The same pass fixes `12`'s stale `OPEN #3`, its `hold`/`upkeep` line and its un-fired-persistence line, corrects `00-steer` §4's `hold` and D3.4 citations, and re-points the `D5.24` citations in `11`/`14`/`00` §6 at **D5.47-AES**. Then archive the proposal (P3).
1b. Done 2026-09-20 (this session): `sys.1`–`sys.8` recorded, of which **`sys.1`–`sys.6` are promoted (D5.46–D5.51) and cleared from `Pending`** · `00-steer` §1 corrected (C26, + pillars 3 and 6) · `demo/README.md` gate and `40-production.md` §4 / open #3 / status row cite C27 · full rule text for the ability economy and the nested bars drafted to `proposals/`. **Owed to Chief of Staff:** the four queue rulings hold references (board rows A1, A2, A3, A6 clear); `D5.24` is resolved inside D5.47 and needs no number of its own; **four further rulings arrived in-session from chat** (`sys.5`–`sys.8`), so the ability economy went from one open question to settled in one sitting, and `sys.8` then **dissolved** the open `sys.7` had left rather than ruling it; **four questions go back up** — proposal §7 #2–#5, the reserve object — plus **Sand, unforced**: `sys.8` sharpens the live clash `c-coherence` §2 E instead of settling it; **D5.46/47/50/51 are logged, not closed**, and stay that way until an owner instruction lets the text into `10`/`11`/`12`; eight defects listed in §Status that Systems cannot fix without one; `STATUS.md` §Pending promotion cites an `§Action register` in `inbox/2026-09-20-queue-verdicts-1.md` that does not exist in that file.
1c. Earlier, 2026-09-20: C1 → **D5.25**, C3 → **D5.26**; the `Acts on it` column added and backfilled; **D5.30–D5.37** logged; `00-steer` §2/§4/§6, `data/README.md` and `proposals/2026-09-20-c-coherence.md` updated to match.
2. `02-ontology.md` + `data/SCHEMA.md`, one section per exchange, PROVISIONAL/LOCKED column on every term (C19). Gate: action 1. **Both are now gate conditions for every distilled doc (D5.49-EPS), so nothing in `10`–`15` can clear the demo gate until they exist.** `SCHEMA.md` is unblocked on `upkeep.per_round` (integer, `sys.7`) and now blocked instead on §7 #2–#3 for the **pool object** — `max`, `current`, `regen`, and whether `max_from` survives for non-attribute sources. **Correct `max_from` out of the draft before `02` is written, not after** (handoff §3.2 still specifies it).
3. Distill `10 → 11 → 13 → 14 → 12 → 15` against the ontology to the D5.49-EPS standard, citing D-numbers or local refs; compress D1–D4 during `10`. Gate: action 2.

## Open questions
Handoff §5 #1–#11, minus Courage's class (closed, D5.36). Added by session 6e:
1. Hand persistence between rounds; hand size and what sets it.
2. Where a gold (two-class) card lives — either deck, its own deck, or fixed at acquisition. Gold now checks **both** classes, so it is doubly darkenable; the deck answer should pay for that.
3. Deck exhaustion — reshuffle, or does running out mean something?
4. The mind class's second attribute (`00-steer` Open #13), now that Courage is spirit.
5. Whether Grit and Will earn two separate guards, or terror is one thing with two flavours.
6. What C18 Push is, now that D5.32 unlocks on momentum and "force a failed check" is available as its shape. D5.47's pair-bar Dominant gate depends on the answer.

Added by this session (D5.46, D5.47, D5.50, D5.51, `sys.7`, `sys.8` — detail in `proposals/2026-09-20-initiative-and-earmarks.md` §7):
7. ~~Which `check` is the earmark~~ **RULED, D5.50.** ~~Attribute or reserve~~ **RULED, D5.51.** ~~% or flat upkeep~~ **RULED, `sys.7`.** ~~"Set for the encounter" — snapshot or live~~ **DISSOLVED by `sys.8`, not ruled** — no verdict to look for. In their place, four on the reserve object, all with the owner: **(a)** regen's shape — flat authored, % of max, or build-set · **(b)** where `max` comes from, and whether `max_from` survives for non-attribute sources like Sand's gourd and Favor's bond tier · **(c)** whether anything still degrades a max mid-fight, which would revive the dissolved question through effects · **(d)** whether regen is unconditional or suppressible, which is where a *designed* damage→fuel link would live.
8. Does upkeep clear **before or after regen** at end of round, and does a darkened ability's upkeep stop that round or the next? Written as *next* round in the proposal; neither ruling speaks. Sharper under `sys.8`: with a regen step in the same phase, the order decides whether a pool that cannot pay recovers first or fails first.
9. Team- and fight-bar thresholds. Unset, and should stay unset until a party fight is played.
10. When Σ held exceeds the attribute, **the player chooses** what darkens (D5.51). Does the AI choose by the same rule, and is the choice made at the moment of the wound (a mid-round interrupt) or at the next Plan (cheaper, may feel worse)?

## Board row
| Lead | Phase | Blocked on | Next action | Updated |
|---|---|---|---|---|
| Systems | **the ability economy is settled** — attribute holds capability, reserve pays an authored upkeep, `hold` and D3.4 retired. D5.46–D5.51 promoted and cleared from `Pending`; `sys.7` (authored upkeep) awaiting promotion; `00-steer` §1, `demo` gate and `40` open #3 corrected. Full rule text for `10`/`11`/`12` sits in `proposals/` — **logged, not closed** (D5.41-EP P2) | **owner instruction to write `10`/`11`/`12` canon** — four D-numbers cannot close without it · owner: proposal §7 #1, "set for the encounter" — snapshot or live? · Tech to promote `sys.7` | §7 #1 + card model (owner present) → `02-ontology` + `SCHEMA.md` → apply the proposal | 2026-09-20 |

## Escalates to
Owner. Rule for the lead: if a v1 rule and an unpromoted C-ref conflict, write the v1 rule and flag the conflict — never silently harmonise.
