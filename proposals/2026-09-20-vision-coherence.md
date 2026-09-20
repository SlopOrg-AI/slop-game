# Vision coherence pass — 2026-09-20 (no lead; Cowork reader session)

**Status:** `PROPOSED`. Nothing here is canon. Next free D-number **D5.29**; next free C-ref **C23**.
**Produced by:** an unassigned agent reading across the whole folder at the owner's request. No lead hat, no writes outside `proposals/`.
**Reads with:** `design/00-steer.md` §1 (the vision paragraph under test), `design/01-pillars.md` (the eight pillars under test), `proposals/2026-09-20-c-coherence.md` (which tested C1–C20 against *each other*), `proposals/2026-09-20-session-6-handoff.md` §2–§3.

**Why this exists:** `01-pillars.md` states its own purpose — *"The test every design, art, and scope question is held against. If a proposal serves no pillar, it is out."* No document in the folder has ever run that test. `c-coherence` checked the C-refs for internal consistency; this checks canon against its stated north star. Two different failure modes.

---

## 1. Clause verdicts — `00-steer.md` §1

Eight clauses. One documented, three contradicted, four unbacked.

| # | Clause (verbatim fragment) | Verdict | Evidence |
|---|---|---|---|
| 1 | "turn-based **card battler**" | **UNBACKED LABEL** | No card mechanism exists. `01` MtG row bars "hand/draw/library"; The Bazaar row owns "loadout-as-deck *feel*" only. The last card-shaped rule was trick-taking order (D2.13), which C2 demotes to "tiebreak at most" (handoff §2 C2). |
| 2 | "persistent campaign and world state" | **HONEST** | `50-world-systems.md`, tagged FUTURE with an MVP obligation in §6. |
| 3 | "learn techniques, build bonds and rivalries, rise to lead a village" | **GAP** | `20-campaign.md`, `21-world-factions.md` are stubs. `bond` appears only as a draw source in an unpromoted proposal (handoff §3.2). Rivalries: zero occurrences. |
| 4 | "queue actions, **arm a hidden reaction**" | **FALSE ON DISK** | D5.25: "There is **no reaction slot** and **no cap on armed count**." Nothing is armed. handoff §6 A already ordered the fix; not applied. |
| 5 | "**a** persistent **initiative** tug-of-war" | **CONTRADICTED, LIVE** | C20 = "Multiple tug-of-wars, nested: individual, team, and skirmish level." C13 = "the bar-as-reach jars." D5.24 (engagement-scoped) cited in `11`/`14`/`00` §6, never logged. `c-coherence` §2 B: "Three things claim to be the initiative bar." The singular noun has no referent. |
| 6 | "variance is **bounded and opt-in**" | **INVERTED** | handoff §3.5 puts RNG at wound *minting* — always on, not per-ability, not opt-in. `c-coherence` §2 C Systems' read retires D2.15's opt-in bands, leaving only the non-opt-in kind. Also fails pillar 1 anti: "Variance that decides fights." |
| 7 | "one table… only the camera changes scale" | **UNTESTED** | C13 imports zones / anchors / edges / derived range bands (FFG Star Wars, Index Card RPG). No proposal asks whether a band overlay is a second visual language (pillar 4 anti) or drifts toward the anti-goal "No tactical grid." `30`/`31` are stubs, so there is nothing to test against. Largest untested surface. |
| 8 | "post-post-apocalyptic… each region its own time-and-place markers" | **GAP** | Zero mechanism. Survives as an art rule (D5.4) and one guard line in handoff §3.8 ("No source above the Y2K ceiling"). The proposed traditions × schools matrix is globally uniform — the magical form of pillar 5's anti-pillar, "A single global tech era." |

---

## 2. Vision ↔ pillar misalignment

The vision paragraph and the pillar table are not the same document about the same game.

| Pillar | Presence in the vision paragraph |
|---|---|
| 1 Reading beats rolling | Strong ("a duel of planning and reading") |
| 2 Commitment is exposure | Absent |
| 3 **Bodies, not bars** | **Absent** — the design's most distinctive claim is not in its own pitch |
| 4 One table, one world | Strong (the longest clause) |
| 5 Living, anachronistic world | Half (era markers yes; "factions and NPCs act while you travel" is in §1's last sentence but unbacked) |
| 6 **One systemic foundation** | **Absent** — the load-bearing architectural commitment |
| 7 Scope discipline | Absent (correctly — it is process, not product) |
| 8 Knowledge is power | One phrase ("learn techniques"), while `15-information.md` is the second-most-developed doc in the folder |

Decision owed: is §1 a **pitch** (then pillars 3 and 6 may stay out, and §1 stops being quotable as a test) or a **test** (then it must carry them)? Today it is used as both — C13's `Supersedes` column names "**Vision paragraph**" as a thing that can be superseded, which only makes sense if it is canon.

---

## 3. Pillars under active strain from live canon or proposals

| Ref | Pillar | Strain | Source |
|---|---|---|---|
| P2a | 2 Commitment is exposure — *"Big moves resolve first and are the most counterable"* | C2's precedence inverts it: "`swift` precedes `heavy`… **craft/casting last**" (handoff §3.4). Under C2 the big move resolves last and is therefore *less* exposed. Pillar 2's meaning-in-play column becomes untrue unless exposure is re-grounded on cost, not order. **Flagged nowhere.** | handoff §3.4, §2 C2 |
| P2b | 2 anti: *"Safe optimal lines"* | `c-coherence` §2 A: "If holding a reaction is free, **the dominant strategy is to arm everything every round**… D5.25 is live canon and currently has a hole in it." A pillar-2 violation inside a *promoted* decision. | c-coherence §2 A |
| P3a | 3 Bodies, not bars — anti: *"Health pools"* | ontology §2 level E introduces **tracks**: "accumulated severity per region within a scene… head, torso, arms, legs · mind · spirit", with "`wounds.json` severity bands become **thresholds on accumulating tracks**" (handoff §3.5). Six per-region accumulating numeric pools with thresholds are HP in mechanism. Only the display rule saves the pillar, and the display rule is not yet written anywhere in `design/`. | ontology §2, handoff §3.5 |
| P3b | 3 open question #2 | `01-pillars.md` Open #2 — "Whether 'Bodies, not bars' extends to mental/spiritual wounds in the same UI language — confirm at M2" — is **silently pre-answered**: ontology §2 level E and the `region` tag family both list mind and spirit as regions. No D-number, no cross-reference. | ontology §2, §4 |
| P1a | 1 anti: *"Hidden math with no tells"* | The draw/budget/star arithmetic (budget 1.0 / +.5 / +.25; ★1 .6 → ★5 1.0) is specified with no statement of how any of it surfaces. Display is addressed for damage (§3.5) and attributes (§3.7) only. | handoff §3.2, ontology §2 |
| P6a | 6 anti: *"Bespoke… separate sims"* | `c-coherence` §2 E fork 3 — Sand as "**Two things:** a Sand reserve… and a sand supply" — adds a pool-like mechanism that is not a pool, for one character. D5.15: a video game "punishes subsystem count." | c-coherence §2 E |
| P8a | 8 *"gated by what they've witnessed"*; anti *"Omniscient player"* | C11: "**Attributes are readable on sight**." Baseline grant of information before any witnessing. Small; arguably serves pillar 1. | handoff §2 C11 |
| P5a | 5 anti: *"A single global tech era"* | Traditions × schools defined purely mechanically, with no region or era binding. See clause 8 above. | handoff §3.8 |

---

## 4. Structural findings

**S1 — the pillars are never used as a test.** Across ~60 KB of session-6 proposals: no C-ref is argued from a pillar, no `c-coherence` clash is adjudicated by one, no §3 synthesis section cites one. Total pillar references in the four proposals: `successor-review` §2.5 (row-ordering cosmetics), `successor-review` §3 and handoff §6 (both "critique vs pillars" as a *future* art task, never performed), C18 (an influence-row aside). A test nobody runs is not a test. This is the cheapest finding here to fix and it retires several others.

**S2 — content mass is inverted against the vision.** Written system docs: `12`, `15`, `50` (+ `00`, `01`, `decisions`). Stubs: `10`, `11`, `13`, `14`, `20`, `21`, `30`, `31`, `40` — nine of fourteen, including four of the six MVP combat docs. The two most-developed system docs (`15-information`, `50-world-systems`) are the ones the vision paragraph mentions least, and one is tagged FUTURE. The project has written most where the vision says least.

**S3 — `00-steer` §2 is one session stale.** It reads "next free is D5.27"; `decisions.md` logs D5.27 and D5.28. `STATUS.md` has it right at D5.29. Housekeeping, not a finding.

---

## 5. Actions proposed

Ordered by leverage ÷ cost. None of these is a decision; each is a thing the owner can say yes or no to.

| # | Action | Who | Gated on | D-number owed |
|---|---|---|---|---|
| **A1** | **Pillar-gate rule.** Every C-ref promotion names the pillar it serves; every clash resolution names the pillar that decides it; a proposal serving no pillar is rejected on that ground alone. Add to `AGENTS.md` §1 as canon rule 8. | Admin + Systems | nothing | **Yes** — process decision |
| **A2** | **Rewrite `00-steer` §1.** Strip "arm a hidden reaction" (D5.25 already decided it — doc correction under canon rule 2, no D-number). Make the initiative clause count-neutral pending C20/C13. Fix the variance sentence *or* the variance model — not both readings can stand. Prompt in Appendix A. | Systems, **owner in session** | `c-coherence` §4 order: A → (B + C20 + C13) → C | No for the strip; **yes** if the variance sentence changes meaning |
| **A3** | **Decide what "card battler" claims.** If a mechanism, name it (trick-taking? loadout-as-deck?) and the doc that owns it. If a pitch word, cut it — it is currently the project's own genre self-description with nothing behind it. | Owner | nothing | **Yes** (one line) |
| **A4** | **Re-run `c-coherence` clashes A, B, C with pillar arguments attached.** A vs pillar 2 anti ("safe optimal lines"). B vs the vision's singular bar. C vs pillar 1 anti + "opt-in". Each of the three has a pillar that decides it; none currently cites one. | Systems | A1 | No (feeds existing promotions) |
| **A5** | **Resolve P2a: C2 vs pillar 2.** Either re-ground "commitment is exposure" on cost/reserve exposure rather than resolution order, or reject craft-last precedence. Currently pillar 2's own meaning-in-play column would become false on C2's promotion, unnoticed. | Owner | rides with C2's reading (`c-coherence` §3 row C2) | **Yes** either way |
| **A6** | **Resolve P3b: mind/spirit as wound regions.** Either log the ontology draft's answer against `01-pillars.md` Open #2, or strike it from the ontology until M2 confirms. It is currently decided-by-draft. | Systems | `02-ontology` pass | **Yes** |
| **A7** | **When `13-damage-wounds.md` is distilled, state the pillar-3 defence explicitly** — that tracks are engine-internal and `surface: never`, names and bands only. Without that sentence on disk, "No HP" is breached in mechanism and defended only by a proposal. | Systems | `13` distillation | No (doc content) |
| **A8** | **Mark `30-art-direction.md` as the gate for C13.** Pillar 4's "one render style across every layer" cannot be tested against zones/anchors/range bands while `30` is a stub. Blocking for C13 *promotion*, not for M1 engine work. | Direction / Art | — | No (sequencing; goes to `STATUS.md`) |
| **A9** | **Settle whether §1 is a pitch or a test** (see §2 above). If a test, add pillars 3 and 6 to it. If a pitch, stop letting proposals cite it in `Supersedes` columns. | Owner | A2 | **Yes** (one line, but it changes how §1 is read everywhere) |
| **A10** | **Flag P5a against the traditions cluster** (C14, C15, C17): traditions need a region/era binding or pillar 5's anti-pillar is breached the moment magic is authored. Park, do not solve now. | Systems | traditions cluster | No (a flag) |
| **A11** | Housekeeping: `00-steer` §2 "next free is D5.27" → D5.29. | Admin | — | No |

**Suggested order:** A1 → A3 + A11 (cheap, unblock nothing) → A4 → A2 (after `c-coherence` §4's A/B/C land) → A5, A6 → A9 → A7, A8, A10 as their docs come up.

---

## 6. What this pass does not claim

- It does not test whether the C-refs cohere with each other — `c-coherence` owns that and is not re-litigated here.
- It does not propose game-design content. Every finding is a mismatch between two things already on disk.
- It names no pillar as wrong. Where a pillar and the content disagree, either could be the thing that should change; the actions above ask for a pick, not a direction.

---

## Appendix A — session prompt for the `00-steer` §1 rework

Paste when A2's gate is clear (`c-coherence` §4 clashes A, B, C resolved and logged). Owner must be in session — §1 is the project's self-description and canon rule 4 forbids an agent attributing it.

```
Act as Systems lead. Read AGENTS.md, design/00-steer.md, design/01-pillars.md,
leads/systems.md, design/decisions.md (session 5–6c only), and
proposals/2026-09-20-vision-coherence.md §1–§2. Nothing else.

Task: rewrite design/00-steer.md §1 (the vision paragraph) and only that
section. I am in session; promote nothing on your own.

The paragraph is wrong in three places and silent in two. Fix in this order,
one at a time, stopping for my word on each:

1. STRIP "arm a hidden reaction". D5.25 removed the thing being armed.
   This is doc correction under canon rule 2 — no D-number. Propose the
   replacement phrasing for what Plan actually is now: one budget, one kind
   of thing, kind governs only when it resolves.

2. INITIATIVE. The paragraph says "a persistent initiative tug-of-war",
   singular. C20 (nested bars) and C13 (bar-as-reach jars) are now decided —
   tell me what they decided to, then rewrite the clause to match. If the
   answer is more than one bar, the paragraph must not imply one.

3. VARIANCE. The paragraph says "variance is bounded and opt-in". The model
   we landed puts randomness at wound minting, which is neither. Give me two
   options and the cost of each:
   (a) change the sentence to describe the model we have;
   (b) change the model so the sentence stays true.
   Do not pick. Option (a) needs a D-number because it changes what the
   project claims about itself.

4. ADD or DON'T — pillars 3 (Bodies, not bars) and 6 (One systemic
   foundation) are absent from the paragraph. Both are load-bearing. Propose
   one clause for each, then ask me whether §1 is a pitch or a test. If it's
   a pitch, we cut them and stop citing §1 in Supersedes columns. If it's a
   test, they go in. Log the answer as a D-number either way.

5. "CARD BATTLER" — tell me what mechanism, if any, that phrase still names,
   then ask whether it stays.

Constraints:
- Rewrite §1 only. Do not touch §2–§7 except the "next free is D5.27" →
  D5.29 correction in §2.
- Do not expand the paragraph. It is one paragraph; it stays one paragraph.
- Do not introduce any term that is not already in decisions.md or
  01-pillars.md.
- Every clause of the new paragraph must be traceable to a D-number or a
  pillar. Show me that mapping as a table before you write the prose.
- Anything you want to change outside §1 goes to proposals/ as a note, not
  into the file.

Output: the mapping table first, then the new paragraph, then the diff you
intend to write. Wait for my word before editing the file.
```
