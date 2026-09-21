# Prototype Findings #2 — v4 playable duel

**2026-09-19.** First runs of `wireframes/combat-1v1-v4.html` (JS engine on `design-data` schema v2, stat model v2, 100-pt initiative, trick-taking order). Auto-played with a naive "queue the first affordable cards, arm the first reaction" policy vs the aggressive-brute AI, 8 rounds. **Tuning observations, not conclusions.**

## What works as designed
- Declare → Arm → Resolve loop, reserve-budgeted queues, refill, state durations, cascades (rain → wet), win check.
- Reactions fire on tag matches; partial halves, perfect negates + reverses initiative + punishes.
- Wounds apply from region × severity × form (Cracked ribs from blunt torso; Unnerved from spirit).
- `staggered` amplifies the next physical hit ×1.3 and blocks arming — the "overextend and get punished" beat happens on its own.
- Out-of-reach melee is wasted at resolve time, not at declare — moving the bar mid-round matters.
- Trick-taking order reads clearly on the bar (`Crushing Blow 120 → Lunge Kick 80 → Shoulder Charge 110 → Palm Strike 60`). Heavy first, exposed first.

## Finding 1 — Guards zero most damage
Genzo's Toughness 26 vs Kaede's 22–30 physical: net 2–4, **no wound in 8 rounds**. Kaede's Toughness 14 vs Genzo's 34–37: net 20+, wounds every round. Average competent hit should net ~10–20 after guard. Options: guards ~5–15 at the 100 level; or form bypass larger; or amounts scale with Strength.

## Finding 2 — Insight differential makes reactions auto-perfect
Insight only goes up (reads +9, absorbed heavy +6, reaction +8) and the naive player never spends it. Once Kaede's Insight > Genzo's, the 1-predicate `Anticipate` upgrades to **perfect every round**, negating Shoulder Charge and pinning initiative at +50. Options: cap Insight (e.g. Wits/2); Insight resets partially when a reaction fires; differential shifts grade only when the gap ≥ N; or the AI must spend Insight too.

## Finding 3 — Perfect-counter reversal is too large on the 100-pt bar
Reverse = ability delta + 10 → +27 in one step. Combined with #2 the bar pins. Consider reverse = ability delta only, or a flat 8–12.

## Finding 4 — Refill hides the cost of reactions
Focus refills 100%, so a 20-Focus reaction held across rounds costs nothing real. Holding a trap should bite: exclude held Focus from refill, or reactions should hold Stamina/Chakra primarily.

## Finding 5 — The brute AI never adapts
It re-queues Shoulder Charge into the same reaction forever. Fine for a prototype; the real AI needs "was I countered last round?" memory. Not a design finding.

## Not yet exercised
Insight interrupts by a human (only the AI used them) · Lightning Palm ×2 vs wet · courage break path (Pressure/Killing Intent) · fight length under human play.
