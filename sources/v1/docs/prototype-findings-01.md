> **HISTORICAL — NOT CANONICAL (marked 2026-09-19, session 2).** These findings came from a Python sim built on the *session-1* stat model (wits/insight/courage as pools, percentile threshold damage, fixed 2 actions/round). That model is superseded — see `combat-scene-decisions.md` D2.2–D2.9 and `01-design-bible.md`. Read for ideas about what tends to break (one-round kills, mandatory reactions, dead abilities, sensitivity of action count), not as tuning truth.

# Prototype Findings #1 — Combat Sim

**2026-09-19.** 324 duels per run: 3 characters × 3 characters × 3 AI policies × 3 AI policies × 4 scene conditions. Fully deterministic — no dice anywhere in the engine.

---

## Headline: the design works, with two real problems

Final tuned state:

| Metric | Value |
|---|---|
| Fight length | mean 6.9 rounds, median 3, max 30 |
| Stalemate rate | 8.6% |
| Counters fired | 490 (64% perfect, 36% partial) |
| Initiative pinned at extreme | 27.8% |
| Mirror matchups | balanced (19/17, 18/18) |

All 16 design-rule assertions pass — initiative spend costs position, counters grade by specificity, conditions gate/cost/amplify, cascades stay clamped, resources never go negative.

---

## Finding 1 — Flat threshold damage was killing 52% of duels in one round

**Problem:** strength and quickness double as capability gates *and* the health bar. A quickness specialist with strength 6 dies to two Crushing Blows. Specialising was suicide.

**Fix (already applied):** threshold damage is **percentile** — each net point removes ~4% of the target's *max* threshold. Proportional durability is now build-independent.

**Result:** one-round kills went **52% → 0%**. Median fight length 1 → 3.

**Bonus:** the knob is insensitive between 0.03 and 0.06 — a robustly tunable value rather than a knife edge.

> This matches the earlier instinct that threshold damage should be percentile. The sim confirms it isn't a preference — flat damage is structurally broken.

---

## Finding 2 — Spending initiative for discounts is a trap

Share of rounds spent locked out of melee reach:

| Policy | Lockout rate |
|---|---|
| Counter-puncher (*never* spends initiative) | **14.2%** |
| Aggressive (spends 2/action) | **42.1%** |
| Balanced (spends 1/action) | **49.4%** |

**Why it matters:** initiative does two jobs — it gates melee reach *and* it's the discount currency. Spending it to afford a big melee attack pushes you below the reach threshold, so you can't use your melee kit next round. **The aggressive build defeats itself.** Aggressive wins only 22% of duels.

**Important:** sweeping `aggression_scale` from 0.0 to 0.30 barely moved win rates. **Counter punishment is not what makes aggression weak** — the discount mechanic is.

### Options

1. **Accept it** — spending initiative is a deliberate trap for the unwary. Thematically fine ("overextension"), but new players will fall into it invisibly.
2. **Discounts only on advancing moves** — spending drives you at the opponent instead of away. The two roles stop fighting each other.
3. **Spend floor** — can't spend below the reach threshold.
4. **Split the bar** — separate positional standing from spendable tempo. Most expressive, two systems to teach.

---

## Finding 3 — Reactions are mandatory, not optional

Same aggressive policy, only difference is whether it arms a reaction at all:

- Never arms: **15 wins**
- Arms broadly: **33 wins**

Arming more than doubles the win rate. A choice that you always take isn't a choice.

Related: **264 wasted arms** across 324 duels — reserved resources that were never spent because nothing triggered. That's the intended opportunity cost working, but it's high.

---

## Finding 4 — Reactions lose the loadout competition

Reactions occupy the same typed slots as actions. A greedy loadout **never picks one**, because an unconditional action always scores higher than a conditional. The first sim run fired **zero counters** for this reason.

Currently forced via `reserve_reaction_slot=True`.

**Open question:** do reactions get dedicated slots, or do they compete? If they compete, they need to be strong enough to be worth a slot — and Finding 3 suggests they already are, which means they'd dominate.

---

## Finding 5 — Courage is doing too much work

Win condition distribution:

| Condition | Share |
|---|---|
| Courage break | **55.6%** |
| Strength zero | 27.8% |
| Quickness zero | 8.0% |
| Stalemate | 8.6% |

Over half of all fights end in a morale break rather than physical defeat. Killing Intent (5 spirit damage to courage) is 23% of all ability activations. Either courage pools need raising, spirit damage needs lowering, or this is the intended identity of the game — **fights are won by breaking will, not bodies.** That's a defensible and distinctive answer, but it should be chosen rather than inherited from a tuning accident.

---

## Finding 6 — Ability usage is top-heavy

Three abilities account for **69%** of all activations: Read the Field (23.6%), Killing Intent (23.0%), Flicker Step (22.5%).

Six of twenty abilities are **never used at all**: grapple, thrown_needles, pressure, anticipate, flame_wave, steel_nerve.

Partly greedy-AI artefact, but the pattern is clear: **initiative-generating and courage-attacking abilities dominate; pure damage and utility abilities are dead weight.**

---

## Finding 7 — Actions per round is the most sensitive knob in the design

At 4 actions/round, every fight ended on round 1. At 2, fights run 3–10 rounds. Nothing else in the system comes close to this sensitivity.

**Implication:** whatever governs how many actions a round contains needs to be tightly controlled. This argues against "spend until resources run out" as an unbounded rule.

> *Session-2 note:* D2.7 adopted exactly that rule (reserves are the budget). This finding is the reason to watch fight length closely in the first Godot playtests.

---

## Structural inference baked into the engine

The design says actions are visible and reactions hidden. For visibility to mean anything, it must precede reaction-setting. The engine therefore runs each round as:

1. **DECLARE** — both queue actions simultaneously; queues revealed
2. **ARM** — both set one hidden reaction, knowing the opponent's declared actions
3. **RESOLVE** — actions execute in initiative order

**This is an inference, not a decision you made.** It's what makes reaction-arming a genuine read and overextension possible. Confirm or correct. *(Confirmed in session 2 — bible §6.)*

Also: when the initiative bar sits at exactly 0, whoever resolves first has a decisive advantage. Currently alternates by round parity. Needs a real rule.

---

## Next decisions (as of session 1 — see decisions log for status)

1. Initiative discount trap — *resolved: dropped (D2.8)*
2. Reaction slots — dedicated or competing — *open*
3. Courage dominance — *moot under new model; re-observe in Godot*
4. Confirm the Declare/Arm/Resolve round structure — *confirmed*
5. Dead abilities — redesign or cut — *ability list being rebuilt for v2 model*
