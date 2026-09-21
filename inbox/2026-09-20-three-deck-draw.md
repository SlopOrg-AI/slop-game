**TRIAGED 2026-09-20** — one item, **`C23`**, tagged `[sys]`. Row **not** appended to `leads/systems.md` Inbox: D5.27 gives that brief exactly one writer, and this session is not Systems. Owed to Systems or Admin.

# Owner feedback — cards as three decks, drawn by choice (2026-09-20, Cowork chat)

**Owner said (verbatim):**
> let's focus on card aspect - i know there should be more in there, easy idea is to remix how cards are thought of - instead of static tableau like html looked like. mind body spirit has their own deck. you choose what to draw from each turn

Context: said during a vision-coherence pass (`proposals/2026-09-20-vision-coherence.md`), immediately after that pass flagged "turn-based **card battler**" in `00-steer.md` §1 as a genre label with no mechanism behind it (clause 1) and asked whether the phrase names anything (action A3). This is the owner answering A3 by proposing a mechanism rather than cutting the word.

"static tableau like html looked like" = `wireframes/combat-1v1-v4.html` (v1, frozen), where the ability set was a fixed visible list.

**`C23`** · **Tags:** `[sys]` · **Rides with:** C7–C10 (draw budget), C1/D5.25 (armed-ability economy), `00-steer` §1 clause 6 (variance) · **Status:** PROPOSED, not walked with the owner.

---

## Reading

Three decks — body, mind, spirit — one per reserve. Each round the player allocates draws across them. The mix is the decision; the contents are the variance. This is not a tableau replacement, it is a **resource-and-information mechanism wearing cards**.

It is not a small C-ref. It touches the ability economy, the variance model, the reserve model, the tell model, and the vision paragraph. Treat it as a cluster, not a line item.

## Pillar test

Applied per `proposals/2026-09-20-vision-coherence.md` A1 (pillar-gate rule — **proposed, not adopted**; this is the first use).

| Pillar | Effect | Weight |
|---|---|---|
| **1 Reading beats rolling** | **Serves, strongly** — *if allocation is public.* A visible "three mind, one body" is a tell the opponent pays for, produced before the action, not after. Nothing else in the design currently generates a pre-action tell. | The strongest argument for C23 |
| **1 anti: "Variance that decides fights"** | **Violates** — a missing card is not a smaller number, it is a plan that cannot be executed. Largest randomness injection available to this design. | The strongest argument against |
| **2 Commitment is exposure** | Neutral-to-serves. A held hand is a standing commitment; spending three draws on spirit and getting nothing is overextension made literal. | — |
| **2 anti: "Safe optimal lines"** | **Serves** — closes the hole `c-coherence` §2 A names in D5.25 ("the dominant strategy is to arm everything every round"). A hand caps concurrency without a cap *rule*. Deletes a problem instead of patching it. | Second-strongest argument for |
| **3 Bodies, not bars** | **Serves.** Wounds that mill a deck or shuffle in a dead card express "wounds change what you can do" in the exact resource being spent — more legible than a stat penalty, and it is the same mechanism at every scale. | — |
| **6 One systemic foundation** | **Serves, conditionally.** Only if a draw costs its matching reserve — then draw budget and reserve budget are one act, not two subsystems. Scale-generic: a settlement's deck is its available projects (D5.11). | Gate on sub-decision 2 |
| **7 Scope discipline** | **Neutral if bounded to M1.** Violated the moment deckbuilding becomes campaign progression. See sub-decision 5. | — |
| **8 Knowledge is power** | **Serves.** Deck composition is a fact with knower-tiers (`15-information.md`): *unknown* → band, *studied* → you know what is in their spirit deck. Fits the existing model with no new machinery. | — |
| 4, 5 | Untouched. | — |

**Net:** serves five pillars, violates one — and the violation and the strongest service are the same mechanism seen from two sides, resolved by one call (below).

## The deciding lever

**Is the draw allocation public?**

| | Effect |
|---|---|
| **Public allocation, private cards** | Variance lives in contents; the decision and the tell are both real. Pillar 1 served. Recommended reading. |
| **Fully hidden** | Simpler against D5.8 (hidden simultaneous commit), but buys a large randomness source and returns no tell. Pillar 1's anti-pillar wins on net. |

Everything else in C23 is detail hanging off this.

## Conflicts to resolve before any promotion

| # | Conflict | Cost of ignoring |
|---|---|---|
| 1 | **Vocabulary collision.** C7–C10 already use **draw** for the weighted power pull (`Σ value × weight` over attributes, reserves, elements, scene). C23 uses **draw** for cards. Two meanings of the load-bearing verb in one schema. | Untangling it in `data/SCHEMA.md` and in code. Must be picked **before** `02-ontology.md` is written (Systems next action 2). Suggested: cards are *drawn*, power is *derived*. |
| 2 | **Overturns D5.5.** `01-pillars.md` MtG row: owns ability kinds and cost identity, **does NOT own "hand/draw/library"**. C23 takes exactly that. | Needs a D-number reversing the row, not a doc edit. The Bazaar row ("loadout-as-deck feel") also needs re-scoping. |
| 3 | **`00-steer` §1 clause 6** — "variance is bounded and opt-in." C23 makes this plainly false unless sub-decision 1 bounds it. | Already flagged as inverted by the coherence pass. C23 and vision-coherence action A2 step 3 are now **the same decision**; do not resolve them separately. |
| 4 | **D5.8 draw timing.** Plan→Resolve is hidden and simultaneous. Where the draw sits — before Plan, at Plan, at round end — is unspecified and changes what "hidden" covers. | Ambiguity lands in the engine. |

## Sub-decisions for the walk

1. **Randomness shape.** True shuffle · deterministic learnable order (mastery = knowing your own sequence) · **draw N+2, keep N** (agency absorbs variance; the only option under which clause 6 stays true).
2. **Does a draw cost its matching reserve?** Yes collapses two budgets into one (pillar 6). No keeps them separable but adds a subsystem D5.15 warns against.
3. **Do unplayed cards persist across rounds?** Persistence restores a slow-built hidden threat — the thing "arm a hidden reaction" named before D5.25 removed it. `00-steer` §1 clause 4 may become true again by a different route.
4. **Deck vs typed loadout.** Replaces the body/mind/spirit slots, or sits under them as their contents?
5. **Is deckbuilding campaign progression?** Recommend **no, explicitly**, and log it — pillar 7. The duel is still unplayed.
6. **Flood/drought policy.** Three shallow decks flood worse than one deep one. Needs an answer, or the first ten duels will fail for a reason that isn't the design.

## Not decided here

Nothing in this file is canon. No D-number is claimed. C23 has not been walked with the owner; the pillar table above is an agent's test, made under a gate rule that is itself only proposed (A1).

**Owed:**
- `leads/systems.md` Inbox — append the `C23` row (Systems or Admin; D5.27 single-writer)
- `STATUS.md` — next free C-ref advances to **C24** (Admin, sole writer)
