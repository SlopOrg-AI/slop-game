# Initiative and earmarks — rule text for `10`, `11`, `12`

**Status:** `PROPOSED`. Nothing here is canon. Written by **Systems** 2026-09-20 in a session the owner is not in: the two rulings below are owner verdicts, but turning them into system-doc prose is design writing, so it lands here and not in `design/`.
**Records:** `leads/systems.md` §Pending — `sys.1` (per-round earmarks, C25) · `sys.2` (nested bars, + `D5.24`) · `sys.5` (multi-attribute holds) · `sys.6` (the two-resource model). Tech promotes all four to `D5.nn-S` (D5.44-EP); this file is then applied to `10`/`11`/`12` in one pass and archived (P3).
**One question is held open on purpose:** §7 #1 — whether `upkeep` is a percentage of the actor's own reserve or a flat cost. Written as options, not a recommendation: it decides whether reserve depth differentiates builds, and that is the owner's call.
**Retires:** D3.4 (held reserve excluded from refill — no subject left) · D5.31 clauses on `hold`, on the reserve earmark, and on per-ability toggle-off · D5.9's "any kind may use either" (upkeep is now mandatory for persisting kinds) · D2.8/D2.12 (reach on the bar).
**Reads with:** `decisions.md` D5.8, D5.9, D5.25, D5.30, D5.31, D5.32 · `proposals/2026-09-20-session-6-handoff.md` §3.1, §3.3b · `proposals/2026-09-20-c-coherence.md` §2 A, §2 B (this closes both) · `inbox/2026-09-20-queue-verdicts-1.md` §Ruled Q1, Q2.
**Scope:** MVP unless a row says TARGET. Numbers name `data/` fields; none are set here.

---

## 1. What the owner ruled

| Ruling | Verbatim | Local ref |
|---|---|---|
| Q1 (C25) | "each round the previous round's ability earmarks are cleared. to arm abilities there is an earmark that round. the earmark amount lines up with the ability check number" | `sys.1` |
| Q2 | "a" → nested bars (pair · team · fight), distance on the map. C13 + C20 promoted; `D5.24` resolves in the same entry | `sys.2` |
| follow-up, same day | "multi-attribute abilities earmark all corresponding attributes" — relayed by Chief of Staff | `sys.5` |
| follow-up, same day | the MtG hold-up framing + "reserves should primarily be fuel for immediate moves, with a bit committed to maintenanc requirements" + the 10–30 / 50 / 66% dial — relayed by Chief of Staff, resolving the §2b fork | `sys.6` |

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

### 2.2 Reserve — upkeep, not a lock

Reserve is **primarily fuel for immediate moves**. An ability that persists between rounds — armed reaction, sustained or decaying passive — pays an **`upkeep` against its reserve each round it stays up**. This is D5.9's `upkeep`, which has existed since the kinds table and never had a magnitude.

**Owner's dial — illustrative, explicitly not decided:**

| Share of the reserve | Reads as |
|---|---|
| 10–30% | normal for a defense worth holding |
| 50% | a lot |
| 66%+ | a massive transformation — most of what you do that round |

`hold` as a reserve lock **does not come back**. Upkeep replaces it.

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

Kaede: **Str 120 · Stamina 100.** Iron Guard (sustained): checks Str 40, upkeep 25%. Deflect (reaction): checks Str 45, upkeep 20%. *All numbers illustrative — the dial is not decided.*

| | Attribute (capability) | Reserve (economy) | Result |
|---|---|---|---|
| **R1 Plan** — arm both | held 40 + 45 = **85** ≤ 120 − 0 wounds | upkeep 25 + 20 = **45%**, leaving 55 for the round | both lit. Near the owner's "50% is a lot" line with two defenses up |
| **R1** — also queue a strike (checks Str 60, costs 30 Stamina) | holding 85 does **not** block it: the strike checks against 120 − 0 committed = 120 ✓ | 45 upkeep + 30 cost = 75 of 100 ✓ | all three fit, but the round is nearly spent |
| **R1 Resolve** — strike lands, commits 60 | Deflect triggers, checks Str 45 against 120 − **60 committed** = 60 ✓ | Deflect pays its firing `cost` | fires. Had the strike committed 80, Deflect would have failed → D5.32 lockout |
| **R2** — leg wound, Str 120 → **70** | held 85 > 70. **Over by 15.** Each ability individually still passes its own check (70 ≥ 45, 70 ≥ 40) | — | **under D5.31 both stay lit; under `sys.6` one must go.** Player chooses |
| **R2** — player drops Deflect | held 40 ≤ 70 ✓ | upkeep falls to 25%, freeing 20 Stamina | Iron Guard stays. The wound **took capability and handed back economy** — you can act more freely with less protection |

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
| `abilities[].upkeep {reserve, per_round}` | D5.9's existing shape, now **mandatory for every kind that persists between rounds** (reaction, sustained, decaying) and given a magnitude for the first time. Whether `per_round` is a fraction or an absolute is **§7 #1, open** | `data/abilities.json` |
| `actors[].attributes[].held` | **new** — running total held up on that attribute this round. Gate: Σ held ≤ value − wounds | schema v3 |
| `actors[].attributes[].committed` | **stays separate from `held`.** Checks test against value − wounds − **committed** only. Conflating the two is the bug the §2b fork was about: held attribute must not block its own check | schema v3 |
| `rules.reactions.max_armed` | already dead by D5.25 — delete with this pass | `data/rules.json` |
| `momentum` | one record per bar: `{level: pair\|team\|fight, parties[], value, thresholds{}}` | schema v3 |
| `zone`, `anchor`, `edge`, range bands | the map half of C13 — lands with `02-ontology.md`, not here | schema v3 |

Validator rules (Tech writes the script, Systems owns the rules): `checks` is a non-empty map and every key is an attribute role on the owner's sheet · **the hold is derived from the whole `checks` map, never one entry** · no `check` scalar and **no `hold` key anywhere** · every persisting-kind ability carries an `upkeep` · gold ⇔ two classes in `checks` ⇔ two classes held · `held` and `committed` are separate accumulators and only `committed` enters a check · every pair bar's parties are in the same engagement · no bar carries a distance term.

## 7. Open, raised by these rulings — not decided here

1. **Is `upkeep` a percentage of the actor's own reserve, or a flat authored cost?** `sys.6` gives upkeep a magnitude ("10–30% normal") but not a *kind*. The owner's dial is stated in percentages, which reads toward P — but the dial is explicitly illustrative, and the choice has a consequence the percentages hide. **Options, with the trade-off; not resolved here.**

   | | **P — percentage of the actor's own reserve** | **F — flat authored cost** |
   |---|---|---|
   | Shape | `upkeep.per_round: 0.25` → 25% of *this* actor's Stamina | `upkeep.per_round: 25` → 25 points, whoever holds it |
   | Symmetry with the log | **Mirrors D5.30** — checks are already "a percentage of that character's own attribute" (C7, C9). One rule for both resources | **Breaks it.** The same technique becomes a different burden in different hands — the thing C7/C9 explicitly rejected for damage |
   | Scale (pillar 6, D5.12) | **Survives the jump.** One authored number is meaningful for a genin, a war party and a settlement alike | **Does not.** A flat 25 is crippling to a genin and nothing to a settlement; every ability needs re-authoring per actor kind, or a scale multiplier — a new mechanism |
   | Build differentiation | **Weak.** Every character holds the same *number* of defenses regardless of reserve depth: a 200-Stamina bruiser and a 60-Stamina scholar each hold exactly three 30% guards. Reserve depth then matters only for immediate moves | **Strong.** A deep reserve genuinely holds more up. "Not enough stamina for both" becomes a build question as well as a round question |
   | Risk to the owner's intent | May undercut the tension they asked for — "not enough stamina to have both defense maintained" is the *same* sentence for every character | May undercut the illustrative dial — percentages stop being stable across the roster, so "10–30% is normal" is no longer a statement anyone can author against |

   *A third shape exists and is named, not recommended: percentage with an authored floor or cap, or percentage of a per-kind template reserve rather than the instance's. It buys build differentiation back at the cost of a second number per ability.*
2. ~~Which check is the earmark on a multi-attribute ability.~~ **RULED — `sys.5`: all of them** (§2a). ~~Whether the earmark sits on the attribute or the reserve.~~ **RULED — `sys.6`: both resources, different jobs** (§2).
3. **Does upkeep clear before or after refill** at end of round, and does a darkened ability's upkeep stop that round or the next? Stated in §3 as *next* round; flagged because neither ruling speaks and it decides whether darkening is a relief or a sunk cost.
4. **Thresholds on the team and fight bars** — the pair bar's ±25 is inherited from v1 (D2.x). Team and fight numbers are unset and should stay unset until a party fight is played.
5. **When Σ held exceeds the attribute, the player chooses what darkens** (§2.1). Does the AI choose by the same rule, and is the choice made at the moment of the wound or at the next Plan? The first is a UI question with a mid-round interrupt attached; the second is cheaper and may feel worse.

## 8. What this does not do

Does not write `02-ontology.md` or the zone/anchor half of C13 · does not set a number — the owner's percentages are illustrative throughout · does not touch `decisions.md` · does not decide C18 Push, which §5's Dominant gate now depends on · **does not pick between §7 #1's P and F** — that one is the owner's, and the rest of this file is written so either answer drops in without rework.
