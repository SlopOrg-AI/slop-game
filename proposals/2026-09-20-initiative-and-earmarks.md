# Initiative and earmarks — rule text for `10`, `11`, `12`

**Status:** `PROPOSED`. Nothing here is canon. Written by **Systems** 2026-09-20 in a session the owner is not in: the rulings below are owner verdicts, but turning them into system-doc prose is design writing, so it lands here and not in `design/`.
**Promoted 2026-09-20:** `sys.1` → **D5.46-ES** · `sys.2` → **D5.47-AES** · `sys.5` → **D5.50-CES** · `sys.6` → **D5.51-CES** (with `sys.3` → D5.48-ACPS, `sys.4` → D5.49-EPS elsewhere). Both forms resolve to the same rows forever (D5.44-EP), so citations here stay correct. **Still recorded, awaiting promotion:** `sys.7` (upkeep is an authored cost) in `leads/systems.md` §Pending.
**Logged, not closed (D5.41-EP P2):** D5.46, D5.47, D5.50 and D5.51 are settled numbers whose rule text is still *here* and not in `10`/`11`/`12`. This file is applied in one pass, then archived (P3).
**Held open on purpose:** §7 #2–#5, all raised by `sys.8` (regen shape · where `max` comes from · whether anything degrades a pool mid-fight · whether regen can be suppressed), plus §7a on Sand. Written as consequences, not recommendations. §7 #1 is **dissolved**, not ruled — see the note there before looking for a verdict.
**Retires:** **D3.4** (held reserve excluded from refill — no subject left; Tech has marked it superseded by D5.51) · D5.31's clauses on `hold`, on the reserve earmark, and on per-ability toggle-off · D5.9's "any kind may use either" (upkeep is mandatory for persisting kinds) · D2.8/D2.12 (reach on the bar) · **`max_from` keyed to an attribute** (`sys.8`; the non-attribute sources are §7 #3).
**Reads with:** `decisions.md` D5.8, D5.9, D5.25, D5.30, D5.31, D5.32 · `proposals/2026-09-20-session-6-handoff.md` §3.1, §3.3b · `proposals/2026-09-20-c-coherence.md` §2 A, §2 B (this closes both) · `inbox/2026-09-20-queue-verdicts-1.md` §Ruled Q1, Q2.
**Scope:** MVP unless a row says TARGET. Numbers name `data/` fields; none are set here.

---

## 1. What the owner ruled

| Ruling | Verbatim | Local ref |
|---|---|---|
| Q1 (C25) | "each round the previous round's ability earmarks are cleared. to arm abilities there is an earmark that round. the earmark amount lines up with the ability check number" | `sys.1` |
| Q2 | "a" → nested bars (pair · team · fight), distance on the map. C13 + C20 promoted; `D5.24` resolves in the same entry | `sys.2` |
| follow-up, same day | "multi-attribute abilities earmark all corresponding attributes" — relayed by Chief of Staff | `sys.5` |
| follow-up, same day | the MtG hold-up framing + "reserves should primarily be fuel for immediate moves, with a bit committed to maintenanc requirements" + the 10–30 / 50 / 66% dial — relayed by Chief of Staff, resolving the §2b fork | `sys.6` → **D5.51-CES** |
| follow-up, same day | "upkeep is defined cost, goes back to how you can tune card ability requirements and then the value is set for the encounter" — relayed by Chief of Staff | `sys.7` |
| follow-up, same day | "chakra and magicka and related should be more like stamina with it's own regen rate. that should cohere" — relayed by Chief of Staff, **dissolving** the open `sys.7` left | `sys.8` |

C25 is `c-coherence` §2 A **fork 2 (pay on arm)**, in the owner's own terms — not fork 1 (`hold` mandatory), which was Systems' read. The read was wrong; the ruling stands.

---

## 2. The two-resource model (`sys.6`) — and what it supersedes

> **Owner, verbatim, 2026-09-20:** *"consider for reserves how you hold up mana in mtg. your instants are still available to play while you hold it. there should be choices and consequences that result in abilitiies going offline and there not being enough stanima to have both defense maintained. can we make the statement cohere"*
>
> *"reserves should primarily be fuel for immediate moves, with a bit committed to maintenanc requirements - for illustrative example (numbers for consideration only) 50% stamina held up for maintaining an active defense would be a lot. perhaps a massive transformation would be 66%+ of stamina - it's most of what you do that round. normally 10-30% range would make more defense to hold."*

**The statement, made to cohere.** The MtG analogy has two halves that were being asked of one currency, which is why §2b forked. Split across the two resources they both hold:

| Resource | Job | MtG shape |
|---|---|---|
| **Attribute** | **capability** — whether you *can* have it up | the mana you hold up. Holding it is what keeps the instant castable, not what stops it |
| **Reserve** | **economy** — whether you can *afford* to keep it up and still act | the upkeep cost on a permanent. Fuel first, maintenance second |

Neither pays for the other's job, so nothing is charged twice.

### 2.1 Attribute — held up, not spent

Arming holds up **every attribute the ability checks, at that check's value** (`sys.5`). **Held-up attribute does not block its own check** — that is the whole point of holding it. Two subtractions, never conflated:

| Question | Formula | When |
|---|---|---|
| What can I still **arm**? | attribute − wounds − **everything already held up** | Plan |
| What do I **check** against? | attribute − wounds − **what is committed this round** (D5.30, unchanged) | resolution / trigger |

A sibling ability's hold-up does not shrink your check pool; a *committed* action does. So a heavy strike that commits 60 Str can starve the guard you were holding — the choice-and-consequence the owner asked for — while merely holding two guards does not.

**Wounds are the pressure.** A wound shrinks the attribute *underneath* what is already held. When total held exceeds attribute − wounds, abilities **darken, and the player chooses which**. That is D5.31's toggle-off finally given a mechanism.

### 2.2 Reserve — upkeep, an authored number

> **Owner, verbatim, 2026-09-20:** *"upkeep is defined cost, goes back to how you can tune card ability requirements and then the value is set for the encounter"*

Reserve is **primarily fuel for immediate moves**. An ability that persists between rounds — armed reaction, sustained or decaying passive — pays an **`upkeep` against its reserve each round it stays up**. This is D5.9's `upkeep`, which has existed since the kinds table and never had a magnitude.

**The magnitude is an authored number on the card, in points of the named reserve** (`sys.7`). It is **the tuning dial** — you balance a card by what it costs to keep up, the way any card game balances a permanent. It is not a percentage and it is not derived from the holder.

**The owner's earlier dial is now an outcome, not the input.** 10–30% normal · 50% a lot · 66%+ a massive transformation: these are the **proportions an authored number produces against a given actor's reserve**, and they are how an author checks whether a number sits in the right place. A sanity check on tuning, never a formula.

| Authored on the card | Against this actor | Reads as |
|---|---|---|
| upkeep **25** | Stamina 100 | 25% — normal for a defense worth holding |
| upkeep **25** | Stamina 40 | 62% — most of that fighter's round; the same card is a real burden to them |
| upkeep **25** | Stamina 250 | 10% — barely felt; the card has stopped being a decision at that depth |

That spread **is** the build differentiation a flat cost was chosen for. It is also the tuning risk it carries: a card authored for one depth of reserve is un-holdable below it and free above it. That is the author's problem to manage, and it is what "tune card ability requirements" means.

`hold` as a reserve lock **does not come back**. Upkeep replaces it.

### 2.2a The principle, so nobody re-opens it

> **A check scales with the holder; an upkeep does not. Skill is personal, fuel is not — a torch burns the same oil whoever carries it.**

D5.30 sizes an ability's *check* as a percentage of the holder's own attribute, so the same technique is the same proportional demand on anyone's skill. `sys.7` makes *upkeep* a fixed number, so the same card is a different proportional burden depending on reserve depth. **These are coherent, not clashing** — two resources with two natures, and the log already treats them that way:

| | Attribute | Reserve |
|---|---|---|
| What it is | a **rating** of the actor, 0–300, degraded by wounds | a **pool of a quantity** — `max_from` a fill source, refilled, spent (session-6 model §3.2) |
| Can be literally matter | no | **yes** — Sand is a supply drawn from the scene and from the gourd's capacity (C15) |
| So a cost against it is | a demand relative to *your* capability | an amount of *the stuff* |

"25% of your sand" is not a sentence this model can say. "25 sand" is. The asymmetry is the two resources being honest about what they are.

*Where it already sits:* the proposed ability split (session-6 handoff §3.3) puts `cost` on the **template** and per-owner numbers on the **instance**. `sys.7` lands `upkeep` beside `cost` on the template; D5.50's `checks{}` stays on the instance. Nothing new is introduced — though that split is itself still PROPOSED and rides with `02-ontology.md`.

### 2.2b What a reserve is (`sys.8`)

> **Owner, verbatim, 2026-09-20:** *"chakra and magicka and related should be more like stamina with it's own regen rate. that should cohere"*

Every reserve is **the same kind of object**: a pool with a maximum, a current value, and **its own regeneration rate per round**. Chakra is stamina-shaped. Magicka is stamina-shaped. **A reserve's maximum is not derived from an attribute** — the attribute→pool-max coupling (`max_from: spirit attributes` for Chakra, `max_from: body.force` for Blood) is deleted.

It coheres, and it does so by **completing D5.51** rather than merely fitting beside it. D5.51 split the two resources by job — attribute is capability, reserve is fuel. `max_from` quietly violated that split: a wound to Heart shrank the Chakra pool, so **one damage event hit both currencies at once**. Cutting the derivation makes the split real: *damage touches capability, never fuel.*

**Maintenance becomes a rate question, not a stock question.** Derived, and the most tuning-critical line in this file: a defense is sustainable when **regen covers its upkeep**. Above that line you are burning the pool down and holding is a countdown; below it, holding costs only the fuel you are not spending on moves. **Where an authored upkeep sits relative to regen decides whether maintenance is a real constraint or a speed bump** — whoever authors numbers needs this before authoring any.

*Scope note:* the session-6 model makes guards and meters **roles of the same pool object**. The owner named reserves. This is written for `role: reserve`; whether guards and meters also take a regen rate is not assumed here.

### 2.3 What this supersedes

D5.31-ES: *"Reactions are free to keep prepped: their **reserve** cost is earmarked by `hold` (D5.9, D3.4 — locked, excluded from refill) and spent **only when they fire**… A prepped or sustained ability whose attribute falls below its check **toggles off** — visibly dark, **earmark still held**."*

| # | D5.31 / D5.9 says | Now | Ruling |
|---|---|---|---|
| 1 | **Duration.** The earmark is a `hold`: locked once, excluded from refill, persisting across rounds. Keeping a reaction up costs nothing after round 1. | Holds clear at end of round and are re-declared in Plan; upkeep is charged every round it stays up. | `sys.1`. Closes `c-coherence` §2 A — "if holding a reaction is free, the dominant strategy is to arm everything every round." Pillar 2. |
| 2 | **Currency.** The earmark is a **reserve** figure (`hold.amount`), authored independently of the check. | The earmark is **attribute**, equal to the check — every check the ability carries (`sys.5`). Reserve is not earmarked at all. | `sys.6`. Retires `hold` in both halves: `.amount` died with `sys.1`, `.reserve` dies here. |
| 3 | **Toggle-off test.** *Per ability*: an ability whose attribute falls below **its own** check goes dark, automatically. | *Portfolio*: when **total held** exceeds attribute − wounds, the player **chooses** what darkens. | `sys.6`. **A real change, not a clarification** — see the worked example: under D5.31 both guards survive the wound, under `sys.6` one must go. |
| 4 | **Maintenance.** Nothing recurring; the lock was one-time. | `upkeep` each round, magnitude per the dial above. | `sys.6`. Gives D5.9's `upkeep` field a magnitude for the first time. |

**D3.4 loses its subject.** "Held reserve excluded from refill" describes a lock that no longer exists. It should be marked superseded when Tech logs `sys.6`, not silently ignored — it is cited in `00-steer` §4 and `12`.

**What survives untouched:** the attribute **check is made at the trigger**, not at arm (D5.31) · the ability's own `cost` is spent **when it fires or resolves**, not before — reserve is fuel for the move, so an un-fired reaction never pays its firing cost *(the one inference in this section; everything else is the rulings read literally)* · attribute commitments clear each round; a wound lasts the scene · earmarks clear each round (`sys.1`).

### 2.4 Worked example — two guards, then a wound

Kaede: **Str 120 · Stamina 100.** Iron Guard (sustained): checks Str 40, **upkeep 25**. Deflect (reaction): checks Str 45, **upkeep 20**. Every number is authored; the percentages below are what those numbers *come to* against Kaede's 100 Stamina, and would read differently for someone else. *Illustrative — no number here is decided.*

| | Attribute (capability) | Reserve (economy) | Result |
|---|---|---|---|
| **R1 Plan** — hold both up | held 40 + 45 = **85** ≤ 120 − 0 wounds | upkeep 25 + 20 = **45 of her 100** — 45%, near the "50% is a lot" line for two defenses | both lit, 55 Stamina left to act with |
| **R1** — also queue a strike (checks Str 60, costs 30 Stamina) | holding 85 does **not** block it: the strike checks against 120 − 0 committed = 120 ✓ | 45 upkeep + 30 cost = **75 of 100** ✓ | all three fit, but the round is nearly spent |
| **R1 Resolve** — strike lands, commits 60 | Deflect triggers, checks Str 45 against 120 − **60 committed** = 60 ✓ | Deflect pays its firing `cost` | fires. Had the strike committed 80, Deflect would have failed → D5.32 lockout |
| **R2** — leg wound, Str 120 → **70** | held 85 > 70. **Over by 15.** Each ability individually still passes its own check (70 ≥ 45, 70 ≥ 40) | unchanged — **25 and 20 are still 25 and 20**; a wound to Str does not make the guards cost more fuel | **under D5.31 both stay lit; under D5.51 one must go.** Player chooses |
| **R2** — player drops Deflect | held 40 ≤ 70 ✓ | upkeep falls to **25 of 100**, freeing 20 Stamina | Iron Guard stays. The wound **took capability and handed back economy** — she acts more freely with less protection |

**The same two cards in another pair of hands.** Genzo: Str 90 · **Stamina 45**. Holding both costs him the same authored 45 — *all* of his stamina, leaving nothing to act with, though his Str 90 carries the 85 held comfortably. He can afford the capability and not the fuel; Kaede can afford both. That is the flat cost doing its job.

**And the rate, which is where `sys.8` puts the real pressure.** Give Kaede **regen 30/round** and Genzo **regen 15/round** (illustrative):

| | Σ upkeep | Regen | Net per round | What holding both actually means |
|---|---|---|---|---|
| Kaede (Stamina 100) | 45 | 30 | **−15** | affordable but not free: a **countdown**. She can hold both about three rounds before the pool cannot pay, unless she drops one or stops acting |
| Genzo (Stamina 45) | 45 | 15 | **−30** | not a posture at all. One round and he is empty, with nothing spent on a single move |

This is the sentence the owner asked for — *"not enough stamina to have both defense maintained"* — and `sys.8` is what makes it a **sustained** constraint rather than a one-off subtraction. Note what the example no longer needs: **no wound shrinks either pool.** Kaede's R2 leg wound closes her *capability* (Σ held 85 > Str 70, one guard must go) and leaves her fuel economy untouched — which is exactly the clean split D5.51 asked for and `max_from` was breaking.

The last row is the model's signature: damage closes options without reducing output (`00-steer` §4, pillar 3).

**What this closes.** `c-coherence` §2 A (unbounded armed economy) · the §2b fork · `12-reactions-passives.md` §Slots / Open #3, already closed by D5.25 but still printed as `OPEN` in that doc's body and status table.

---

## 2a. How many earmarks — ruled (`sys.5`)

> **Owner, verbatim, 2026-09-20:** *"multi-attribute abilities earmark all corresponding attributes."*

This rules §7 #1 as it was posed. The candidates were *highest check* · *sum* · *one per named reserve*; the answer is **none of those as a selection rule — every check the ability carries is earmarked**. Nothing is dropped and nothing is nominated.

**Reconciled against D5.30.** D5.30 gives an ability *"a check per attribute it uses, sized as a percentage of that character's own attribute."* That plural was already in the log; `sys.1` then said "the earmark equals the check", which only parses for a mono-attribute ability. `sys.5` closes the gap: the earmark is the **whole check set**, not one member of it. `check` was never a scalar — the data has to stop pretending it was (§6).

**Reconciled against `sys.1`.** Unchanged: the whole set is paid at arming, clears at end of round, and must be paid again next Plan to stay armed. `sys.5` multiplies the cost; it does not change when it is paid or when it clears.

**What it costs**

| Ability | At arming |
|---|---|
| One attribute (mono) | its one check — as `sys.1` already said |
| **Two attributes, one class** (e.g. Str + Qck, both body) | **both** checks, in full. No discount, no max-of. Darkened from either side: a wound to either attribute counts against that attribute's held total (§2.1) |
| **Gold, two classes** (checks a body attribute *and* a mind or spirit one) | **both** checks, in full, **in both classes** — so it draws on two different parts of the sheet at once. It is the most expensive thing on the board to keep armed and the easiest to darken, which is what `leads/systems.md` open #2 asked the gold answer to pay for |

The general shape: arming cost scales with the **breadth** of an ability, not just its size. A wide ability is hard to keep up and fragile to any wound that touches it.

## 2b. ~~What the earmark sits on — forked~~ **RULED, `sys.6`, owner 2026-09-20**

The fork asked whether the earmark sits on the attribute (A) or the reserve (B). **The answer is neither: both resources are in play, doing different jobs** — attribute holds the capability, reserve pays the upkeep. §2 above is the resolved model; the fork table is retired. What each option got right: A was right that the hold is attribute-side; B was right that the reserve remains the thing that stops you keeping everything up. Neither was right that one currency does both.

---

## 3. Rule text — `12-reactions-passives.md` (holding an ability up)

> ### Holding an ability up (D5.25, D5.30, D5.9 `upkeep`, `sys.1`, `sys.5`, `sys.6`)
>
> An ability is **up** for a round when its attribute hold is declared in Plan and its upkeep is paid. Two resources, two jobs: **attribute says whether you can**, **reserve says whether you can afford to**.
>
> | Step | When | Attribute | Reserve | Field |
> |---|---|---|---|---|
> | Declare | Plan | Hold **every** check the ability carries, one per attribute, each in full (`sys.5`). Gate: Σ held ≤ attribute − wounds. Short on any one → it cannot go up | Pay `upkeep` for this round | `checks{}`, `upkeep` |
> | Hold | during the round | Held attribute cannot support another ability — but **does not block its own check** | Upkeep is spent, not locked. It does not come back | — |
> | Darken | when a wound lands | Σ held > attribute − wounds → the **player chooses** what goes dark until it fits. Dark abilities release their hold | Upkeep for a darkened ability stops next round, not this one | `sys.6` |
> | Fire / resolve | on trigger | Check against available attribute (value − wounds − **committed**, D5.30). Pass → resolves and commits. Fail → D5.32 lockout | The ability's own `cost` is spent **now** — never before | D5.30, D5.32 |
> | Clear | end of round | Every hold releases | Reserves refill | `sys.1` |
> | Re-declare | next Plan | Staying up costs the hold **again** | …and the upkeep **again** | `sys.1` |
>
> **Consequences, stated so they are not rediscovered:**
> - No cap on how many abilities are up and no reaction slot (D5.25). Two arithmetic caps instead: **Σ held ≤ attribute − wounds** and **Σ upkeep ≤ reserve, minus whatever you want to spend acting**.
> - Holding a guard does **not** make it unavailable — that is what holding is for. What starves it is a *committed* action eating the same attribute at resolution.
> - A fighter with three things up pays three upkeeps every round and has little fuel left to act. The sacrifice is continuous, and blanket-arming is self-defeating.
> - `hold` is **removed** from `abilities.json` entirely — `.amount` with `sys.1`, `.reserve` with `sys.6`. Maintenance is `upkeep`. **D3.4 ("held reserve excluded from refill") has no subject and should be marked superseded.**
> - "Un-fired reaction persistence" (`12` open #3) is answered: it does not persist. Re-declare or it lapses.
> - Sustained and decaying passives work the same way — they are not a separate economy.

## 4. Rule text — `10-combat-loop.md` (one line in the round)

> **Round:** Plan (declare holds, pay upkeep) → Resolve → **End of round: attribute commitments clear (D5.30), holds release (`sys.1`), reserves refill, decaying passives tick.** Nothing an ability held survives into the next Plan unless it is declared and paid for again.

## 5. Rule text — `11-initiative.md` (nested bars; resolves `D5.24`)

> ### Momentum — three nested bars (C20 + C13 promoted, `sys.2`)
>
> Initiative is **momentum**: pressure, never distance.
>
> | Level | One bar per | Range | Reads |
> |---|---|---|---|
> | **Pair** | each engaged pair of actors | −50…+50 · reach −10 · Dominant ≥ +25 · Desperate ≤ −25 | who is dictating this exchange; gates Push, D5.32 unlock |
> | **Team** | each engagement (side vs side) | same datatype | which side is pressing |
> | **Fight** | the scene | same datatype | which way the field is going |
>
> **Propagation** — up as conditions, down as modifiers (D5.12 shape, same numbers→thresholds→minted-name discipline as damage):
>
> | Direction | Rule |
> |---|---|
> | Pair → Team | a pair bar crossing Dominant/Desperate mints a team-level condition (`pressing-N`) |
> | Team → Fight | team momentum crossing a threshold mints a scene condition (`routing-N`) — **this is the end-of-round "scene bleed"** |
> | Fight → all | scene momentum shifts every child bar's thresholds |
>
> Bleed applies **at end of round**, not continuously.
>
> **Distance is not on any bar (C13).** Position is zone + (anchor | open); range is **derived, never tracked** (same anchor → Engaged · same zone → Short · adjacent → Medium · two steps → Long · else Extreme; edges modify). Reach is a descriptor read by one rule. Movement is a maneuver that changes band or anchor. D2.8/D2.12 (reach on the bar) are **superseded**.
>
> ### `D5.24` — resolved, not logged as its own rule
>
> D5.24 ("engagement-scoped initiative"; concurrent engagements; scene bleed at end of round) has been cited as canon in six files and never logged. It is **absorbed here**, and carries no separate rule:
>
> | D5.24 claim | Where it lives now |
> |---|---|
> | "initiative is scoped per engagement, not per scene" | the **team** bar. An *engagement* is the team-level container — `c-coherence` §2 B fork 3 |
> | "multiple simultaneous engagements, each its own track" | multiple team bars under one fight bar, each with its own pair bars |
> | "condition bleed applies at end of round" | Team → Fight propagation, above |
>
> An engagement is **not** derived from space (fork 1) and **not** a declared pairing (fork 2): space is zones and bands, which the team bar does not read. Two fights across a courtyard are two team bars because they are two sides-vs-sides, whichever zones they stand in.
>
> Citations in `11` and `14` stay, re-pointed at `sys.2`. `00-steer` §6 Open #5 (initiative model for N-vs-M *within* one engagement) is **closed by the same ruling**: pairs have pair bars, sides have a team bar, the scene has one; a third party joining opens a new pair bar and joins or opens a team bar. Group actors carry one bar per opposing group.
>
> ### Scope
>
> | Item | Scope |
> |---|---|
> | Pair bar, full behaviour | MVP |
> | Team + fight bars | TARGET — the **datatype and the propagation hooks are written at MVP** so they are data, not engine work (D5.12: the code never assumes one actor a side) |

## 6. Data

| Field | Change | File |
|---|---|---|
| `abilities[].checks{}` | **the field that changes shape.** A **map keyed by attribute role** — `{"body.force": 0.4, "mind.acuity": 0.25}` — never a scalar `check`. `sys.5` makes the plural load-bearing: every entry is earmarked, so no reader may take one and no author may write a bare number | `data/abilities.json`, schema v3 |
| `abilities[].hold` | **delete the whole key** — `.amount` with `sys.1`, `.reserve` with `sys.6`. There is no reserve lock. **D3.4 goes with it**; mark it superseded rather than leaving it cited in `00-steer` §4 and `12` | `data/abilities.json` |
| `abilities[].upkeep {reserve, per_round}` | D5.9's existing shape, now **mandatory for every kind that persists between rounds** (reaction, sustained, decaying). **`per_round` is an integer — absolute points of the named reserve, authored, never a fraction** (`sys.7`). It belongs on the **template**, beside `cost`, not on the per-owner instance (§2.2a) | `data/abilities.json` |
| `abilities[].checks{}` — *placement* | stays on the **instance**: derived from the holder's own attribute (D5.30). The two fields sit on different objects on purpose; that split is the schema's expression of §2.2a | schema v3 |
| `pools[].max_from` | **delete, for attribute sources** (`sys.8`). A reserve's maximum is not a function of an attribute. Non-attribute sources — Sand ← the gourd, Favor ← bond tier, relic ← `const` — never caused the problem this removes; whether the field survives for them is **§7 #3, open** | schema v3 |
| `pools[].max`, `.current`, `.regen` | **the reserve object** (`sys.8`): an authored maximum, a current value, and a per-round regeneration rate. `regen`'s shape (flat / % of max / build-set) is **§7 #2, open**; where `max` comes from is **§7 #3** | schema v3 |
| `actors[].attributes[].held` | **new** — running total held up on that attribute this round. Gate: Σ held ≤ value − wounds | schema v3 |
| `actors[].attributes[].committed` | **stays separate from `held`.** Checks test against value − wounds − **committed** only. Conflating the two is the bug the §2b fork was about: held attribute must not block its own check | schema v3 |
| `rules.reactions.max_armed` | already dead by D5.25 — delete with this pass | `data/rules.json` |
| `momentum` | one record per bar: `{level: pair\|team\|fight, parties[], value, thresholds{}}` | schema v3 |
| `zone`, `anchor`, `edge`, range bands | the map half of C13 — lands with `02-ontology.md`, not here | schema v3 |

Validator rules (Tech writes the script, Systems owns the rules): `checks` is a non-empty map and every key is an attribute role on the owner's sheet · **the hold is derived from the whole `checks` map, never one entry** · no `check` scalar and **no `hold` key anywhere** · every persisting-kind ability carries an `upkeep` · **`upkeep.per_round` is an integer > 0, never a fraction — a value < 1 is an authoring error, not a percentage** · `upkeep.reserve` names a pool the holder's actor kind can instantiate · gold ⇔ two classes in `checks` ⇔ two classes held · `held` and `committed` are separate accumulators and only `committed` enters a check · every pair bar's parties are in the same engagement · no bar carries a distance term.

Plus, from `sys.8`: **no `max_from` keyed to an attribute role anywhere** · every `role: reserve` pool carries `max`, `current` and `regen` · `regen` ≥ 0.

**Authoring aids, not rules:** warn when an authored `upkeep` exceeds ~50% of the reserve of any actor that can hold the card, and again above ~66% — the owner's dial (§2.2) as a lint. **Warn when Σ upkeep of a plausible loadout exceeds the holder's `regen`**, because that is the line between a posture and a countdown (§2.2b), and it is the number an author is most likely to miss.

## 7. Open, raised by these rulings — not decided here

1. ~~**Does "the value is set for the encounter" mean the proportion is snapshotted?**~~ **DISSOLVED by `sys.8` — not ruled, and there is no verdict to look for.** The question existed only because `max_from` made a reserve's maximum a function of an attribute, so a wound could shrink the pool *underneath* something already held; "live share vs snapshot share" was a choice about how to handle that shrinkage. `sys.8` deletes the dependency, so the pool no longer shrinks under you and the question has no subject. What "set for the encounter" now means is the plain reading: **the authored number does not drift once the fight starts.** Also still closed, from `sys.7`: upkeep re-derived from *current* reserve — that is the percentage model, rejected.

**Raised by `sys.8`, all four for the owner:**

2. **What shape is `regen`?**

   | | Consequence |
   |---|---|
   | **Flat authored per round** | symmetric with `sys.7`'s flat upkeep, so "regen vs upkeep" is a direct comparison of two authored numbers — the easiest version to tune and to reason about at the table. But every holder of the same reserve then regenerates identically unless the number sits on the character rather than the pool template, which is a placement decision in itself |
   | **Percentage of max** | self-scaling across actor kinds (pillar 6): one number works for a genin and a settlement. But deep pools then refill faster in absolute terms too, so reserve depth compounds — big pool *and* fast refill — and may become doubly dominant |
   | **Set by build** | recovery becomes an investment axis distinct from capacity: a character can buy staying power instead of size. Most expressive, most to author and balance, and it re-couples the reserve to something the player chooses — a different coupling from the one `sys.8` just cut, but worth seeing as one |

   *`sys.7` ruled the cost side flat. Symmetry is an argument for flat regen; it is not a decision.*
3. **Where does a reserve's `max` come from** — authored on the character, bought in a build, or derived from a non-attribute source? *Authored* is simplest and sits on the sheet with Content. *Bought* makes depth a spend, which pairs with `sys.7`'s differentiation intent. *Derived from a non-attribute source* is the live residue: Sand ← the gourd's capacity and Favor ← bond tier are **not** attribute-derived and never caused the problem `sys.8` removes. **Consequence of keeping them: `max_from` survives as a field and the "every reserve is the same kind of object" claim becomes partial rather than total.** This is the one place this file's reading of `sys.8` goes further than the owner's words, which named chakra, magicka "and related" — it is flagged rather than assumed.
4. **Does anything still degrade a reserve's maximum mid-fight, or is the pool fixed for the encounter?** *Fixed* keeps the pool a stable platform and all pressure in spend-vs-regen; it is what keeps #1 dissolved. *Not fixed* — a broken gourd, a curse, a condition — **revives the shape of the question the owner just dissolved**, arriving through effects instead of through attribute derivation. Worth answering deliberately rather than discovering later.
5. **Is regen unconditional at end of round, or can it be suppressed?** *Unconditional* is predictable and keeps the upkeep arithmetic stable. *Suppressible* — by a condition or tag (`bleeding`, `exhausted`), or by having overspent — hands damage and conditions a lever on the fuel economy. Note what that is: **the deliberate, designed version of the damage→fuel coupling `sys.8` just deleted as an accident.** It is where "a wound makes you tire" would live, and it fits the tag/tiered-state machinery (D5.14, City of Mist) rather than needing a new one.
6. **Does upkeep clear before or after regen** at end of round, and does a darkened ability's upkeep stop that round or the next? Stated in §3 as *next* round; neither ruling speaks, and it decides whether darkening is a relief or a sunk cost. Sharper under `sys.8`: with a regen step in the same phase, the order decides whether a pool that cannot pay recovers first or fails first.
7. **Thresholds on the team and fight bars** — the pair bar's ±25 is inherited from v1 (D2.x). Team and fight numbers are unset and should stay unset until a party fight is played.
8. **When Σ held exceeds the attribute, the player chooses what darkens** (§2.1). Does the AI choose by the same rule, and is the choice made at the moment of the wound (a mid-round interrupt) or at the next Plan (cheaper, may feel worse)?

### 7a. Sand — not forced into this model

C15 files Sand as "a magic reserve in its own right," and the session-6 model gives it `max_from: the container object's capacity`, fill "from scene `sand` tier and carried supply", and the note that it **is matter** — spending it transitions material into `hardened` / `packed` / `coffin` objects, **reclaimable**.

**Under `sys.8` it is a reserve in its pool half and not in its regen half.** A gourd of sand has a maximum and a current value like any pool. It does not *regenerate*: it is **resupplied**, from the scene and by reclaiming what you already spent. That is not a rate belonging to the character; it is an environmental and positional fact — a desert refills you, a ship's deck does not.

It fits the uniform model **only if refill has two channels**: an intrinsic `regen` (Sand's is **0**) plus resupply arriving as an *effect* — scene-driven, condition-driven, or a reclaim action. If `regen` is the only refill channel a pool may have, Sand does not fit and is a different kind of object wearing the word "reserve."

**This does not settle it, and `sys.8` makes it sharper rather than softer.** `c-coherence` §2 E is the live, unresolved clash — three forks: (1) an ordinary pool with free effects, (2) the pool **is** the mass, conserved and reclaimable, (3) **two things**, a Sand reserve and a sand supply. That file's own read: (2) matches the fiction, (3) survives the schema. Declaring every reserve the same kind of object raises the stakes on choosing, because Sand is now the one instance that has to justify itself against a uniform shape. It stays on the board as clash E; it is not resolved here and should not be.

## 8. What this does not do

Does not write `02-ontology.md` or the zone/anchor half of C13 · **does not author a single upkeep number** — Kaede's 25 and 20 are illustrative, and the real ones are Content's to author against §2.2's dial · does not touch `decisions.md` · does not decide C18 Push, which §5's Dominant gate now depends on · **does not choose between §7 #1's Live and Snapshot** — that one is the owner's, and the rest of this file is written so either answer drops in without rework.
