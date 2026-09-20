# C1–C20 coherence pass — 2026-09-20 (Systems lead, Cowork)

**Status:** `PROPOSED`. Nothing here is canon. Owner promotes pieces of it by logging D-numbers (next free: **D5.27**).
**Produced by:** Systems lead, owner in session. First pass in which the C-refs are checked *against each other* rather than one at a time.
**Reads with:** `proposals/2026-09-20-session-6-handoff.md` §2 (the C-refs themselves), §3 (agent synthesis), §5 (open list).

**Why this exists:** C1–C20 were captured sequentially across one long conversation. Each is internally sensible. Nothing had ever tested whether they compose. Six places they don't, and four places a reading has to be picked, are below.

---

## 1. The distillation — what the twenty add up to

Nine statements. Every other C-ref is detail hanging off one of these.

| # | Statement | From |
|---|---|---|
| 1 | **There is one kind of thing: the ability.** Chosen during Plan, paid from one budget. `kind` governs only *when* it resolves. | C1 (D5.25), C3 (D5.26), D5.8 |
| 2 | **An ability's power is a weighted draw** from attributes, reserves, elements and the scene. Weights fixed at acquisition, scaled by stars. | C7, C8, C9, C10 |
| 3 | **Everything a rule touches is an entity with tags.** Rules test tags, never the subclass. Fighter, wound, footing, wall, settlement — same shape. | C3, C5, C16, D5.12 |
| 4 | **A published dictionary says how tags interact,** so players can predict combination. | C4, D5.14 |
| 5 | **Numbers accumulate; names are minted.** A number crosses a threshold and the game writes a *named* condition chosen by the tags that caused it. One machine for wounds, materials and morale. | C6, C5, D5.14 |
| 6 | **Pools are per-character, not a fixed list** — each with its own fill source, tell, and sometimes physical substance. | C14, C15, C17 |
| 7 | **Distance lives on the map; the bar carries only pressure.** | C13, C20, D5.23 |
| 8 | **What is known is a fact with a tier,** advanced by watching, by being hit, or by insight. | C8, C11, D5.10 |
| 9 | **You can spend yourself** — burn attribute points at a critical moment. | C18 |

Plus C19: every term above is provisional (deferred, rides with the ontology pass).

---

## 2. Where they do not cohere

Six clashes. Each needs a **pick**, not a clarification. Ordered by leverage.

### A. The armed-ability economy is unbounded — introduced by D5.25
**The clash.** D5.25 removed the cap on armed abilities, saying concurrency is limited by "what the character can afford." But D5.9 makes the `hold` cost **optional** ("any kind may use either"). If holding a reaction is free, the dominant strategy is to arm everything every round — precisely the degenerate case the old cap prevented. D5.25 is live canon and currently has a hole in it.

**The fork.**
1. **`hold` becomes mandatory** for `reaction` and `sustained` kinds — the locked, non-refilling reserve *is* the cap. No new mechanic; uses D5.9's existing vocabulary.
2. **Pay on arm**, spent whether or not it fires. Arming becomes a bet on reading the opponent.
3. **A separate concurrency currency** (an attention budget — pre-decides handoff §5 #4, "what Focus is").
4. **Cap on firing, not arming.** Reintroduces the cap C1 called a false question; listed for completeness.

**Systems' read:** (1). It is the only option that adds no mechanic, and it makes the sacrifice *continuous* — a fighter holding three reactions has nothing left to attack with, which is the tension the design wants. (2) is the live alternative and changes the feel from sacrifice to gamble.

### B. Three things claim to be the initiative bar
**The clash.** C13 takes distance off the bar. C20 says there are three nested bars (individual · team · skirmish). D5.24 (cited in `11`, `14`, `00-steer` §6, never logged) scopes initiative to "engagements" and describes scene bleed at end of round — a *spatial* framing that C13 just relocated to zones. The handoff assumes C20's team level and D5.24's engagement are the same object. That assumption is untested.

**The fork.** An engagement is:
1. **Derived from space** — who is in range of whom, recomputed as people move;
2. **A declared pairing** — you commit to fighting someone, independent of where you stand;
3. **Not spatial at all** — simply the name for the team-level meter.

Consequence: (1) makes disengaging a movement problem; (2) makes it a commitment problem; (3) makes it neither and leaves "scene bleed" meaningless.

### C. Randomness has three incompatible stories
**The clash.** C7: ability damage is consistent (% of stat). D2.15: opt-in per-ability variance bands, kept on two abilities. Handoff §3.5: minting may choose among several valid conditions by weighted draw.

**The fork.** RNG survives in **zero**, **one**, or **two** places.

**Systems' read:** C7 kills damage rolls outright. Keep variance at the *minting* step: a surprising wound **name** is a story, a surprising **number** is noise. D2.15's bands then become redundant and should be retired explicitly rather than left half-alive.

### D. The dictionary is doing two unrelated jobs
**The clash.** C4's dictionary is chemistry — how tags combine (BotW model). The precedence model (handoff §3.4) puts turn order in the same table as `precedes` entries. Combination and ordering are not the same kind of fact, and a player learning "fire + oil" is not thereby learning "fast beats strong."

**The fork.** One dictionary with an ordering verb, or two tables — a chemistry dictionary and a precedence table. Decides what a single in-game reference screen can show.

### E. Sand is both a pool and physical matter
**The clash.** C15 makes Sand a reserve *and* states that spending it transitions material into hardened, reclaimable objects. If spent sand becomes a wall, mass moved — the pool did not merely decrease.

**The fork.**
1. Sand is an ordinary pool; created objects are free effects.
2. The pool **is** the mass — conserved, reclaimable, and a wall you break gives it back.
3. **Two things:** a Sand reserve (the effort of controlling it) and a sand supply (the matter itself).

(2) is the version that matches the fiction and gives the scene-fed fill rule something to mean. (3) is the version that survives contact with the schema.

### F. Stars grow the budget, but distribution is "fixed at acquisition"
**The clash.** C8 scales an ability's budget with star level; C10 fixes its draw distribution at acquisition. Both cannot be literally true without saying *which* is fixed.

**The fork.** Training fixes the **ratio** (70/30 stays 70/30, both numbers grow — character identity persists) or the **absolute weights** (stars hand you headroom you then allocate — training becomes a choice).

### G. Push is visible, and attributes are readable
**The clash.** C18 drops an attribute mid-scene; C11 makes attributes readable and confirmable. Push is therefore a public tell the moment it lands.

**The fork.** Intended — a dramatic beat everyone at the table sees — or hidden until it resolves. Interacts with `restrained` (holding back), which the handoff already says cannot coexist with Push.

### Not a conflict
**C16 (places need different attributes) vs C9 (abilities draw on attributes)** is already answered by the sheet model: abilities address a *role* (`body.force`), each sheet names it locally (Strength / Population). No decision owed.

---

## 3. Where a reading has to be picked

| C-ref | The two readings | Why it matters |
|---|---|---|
| **C2** | "Rock-paper-scissors" as a **literal cycle** (something beats `swift`, closing the loop) vs. simply **"tags beat tags"** with no guaranteed cycle | A literal cycle must be authored and balanced; the loose version is emergent and may leave a dominant tag |
| **C5** | Destruction/creation is **MVP** vs **TARGET** | Stated as a rule, but the M1 content list has only "one destructible + one creatable object." Materials + chemistry is a large system to build for two objects |
| **C11** | Holding back is a **player** choice vs **NPC-only** | If the player can sandbag, it needs a UI and a cost; if not, it is an AI behaviour and an information puzzle |
| **C20** | The individual level is one bar **per pair** vs one **per actor** against all comers | Per-pair scales as N², per-actor loses the duel's symmetry |

---

## 4. Suggested order of resolution

1. **A** — live canon, currently broken. Smallest fix, highest urgency.
2. **B** + C20 + C13 together — they are one exchange, not three. Output: `11-initiative.md` stops being a stub.
3. **C** — cheap once B is settled; mostly a retirement of D2.15.
4. **E**, **F**, **D** — ride with the traditions cluster, the draw-budget cluster and the ontology pass respectively.
5. **G** and the §3 readings — cheap, resolve in passing.

## 5. Status & scope

| Item | Status | Scope |
|---|---|---|
| The nine statements (§1) | PROPOSED — synthesis, not decided | MVP |
| Conflicts A–G (§2) | OPEN — owner picks | MVP (E partly TARGET) |
| Readings (§3) | OPEN | MVP |
| C16 vs C9 | RESOLVED by the sheet model — no D-number owed | MVP |
