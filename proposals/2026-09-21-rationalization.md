# Proposal — rationalize the machinery, against this project's own principles

**Produced by:** Tech (Claude Code), 2026-09-21 · **Targets:** `tools/sweep.py`, the cross-surface channels, `AGENTS.md` §6, the numbering decisions · **Proposes:** retire three mechanisms, merge two, freeze the rest · **Status:** `PROPOSED`. Owner and Chief of Staff rule. Tech built most of what is on the cut list, and starts the list with its own.

**Owner:** *"can we review and rationalize? i doubt it was perfect on a first pass. recall principles."*

---

## 1. The number

| | |
|---|---|
| Decisions logged, D5.1–D5.51 | **50** |
| …about **how we work** — leads, commits, numbering, surfaces, boards | **31** |
| …about **the game** | 19 |
| Proposals written | **31** |
| Design docs still STUB | **11 of 14** |
| `02-ontology.md` · `data/SCHEMA.md` · `demo/` | **absent · absent · empty** |
| Duels played by a human | **0** |

`01-pillars.md` pillar 7, the project's own scope rule: *"1v1 duel first; everything else is designed, tagged, and waits."* Tonight that rule was applied to the game and not once to the machinery around it.

## 2. Where each principle was breached, and by whom

| Principle | What happened |
|---|---|
| **Rule 6 / pillar 7 — scope discipline** | The MVP was not expanded. The meta-layer was, without limit, and nobody thought the rule applied to itself. This is the finding; the rest are symptoms |
| **§5 — small iterations over big deliverables; ask before large work** | Tech shipped the sweep, the report mechanism, the session register, the watcher and a whole bridge in single passes. Two were asked for. The others were not |
| **§5 — do not lock architecture prematurely** | Numbering authority, party-tagged IDs, agent namespaces and a promotion flow were locked (D5.42–D5.44) before the docs they govern exist. The ID reformat blinded three guard rails the same hour |
| **Rule 2 — the log is the arbiter** | *Who writes `STATUS.md`* has been decided four times in six hours: D5.27 → D5.29 → D5.38 → D5.42 cl.4. Each supersession was reasonable; the sequence is not |
| **Rule 1 — git history is the record** | Three misattributed commits, one mixed-hand commit, one empty junk commit, and attribution that cannot distinguish two sessions of one role |
| **Rule 4 — never self-attribute to the owner** | Held. No agent logged a D-number without instruction, and the one near-miss (a peer relaying an owner ruling) was refused |

## 3. Duplication ledger — five ways to tell Tech something

| Mechanism | Keep? |
|---|---|
| `## For Chief of Staff` / `## From …` sections in briefs | **Keep** — async, symmetric, no new files |
| `## Commit me` block + `tools/watch.py` | **Keep** — the only active path, and what the owner asked for |
| `bridge/` folder | Already retired into the briefs |
| Session reports (`proposals/reports/`) | **Keep, narrowed** — required of a *separate session*, pointless for a lead that writes the repo directly |
| `tools/sweep.py` | **Retire — see §4** |

## 4. Cuts, starting with Tech's own

1. **Retire `tools/sweep.py`.** The watcher supersedes it. The sweep commits other surfaces' work by guessing from a path table and asking Tech to name the author — and that guess produced all three misattributions. The watcher commits only what a surface asked for in writing, and takes the attribution from the file's location, so no one declares and no one guesses. The sweep already carried a stated expiry; it arrives early. **Cost of being wrong:** work sits untracked until someone looks, which is the pre-D5.39 state — mitigated because the watcher runs in every shell session.
2. **Narrow session reports** to separate sessions only. A lead writing its own brief already reports in it.
3. **Question D5.42–D5.44 (owner's, not Tech's to retire).** Two-tier numbering with local namespaces, promotion and ratification, for a 50-row log with a single decider. It cost a guard-rail outage on its first day. Ask plainly: what does it buy that "Tech assigns the next number when the entry is written" does not?
4. **Leave the six guard rails.** Each refused something real, including four of Tech's own commits. Check C duplicates `.gitignore` and stays as belt-and-braces because it is free.
5. **Keep `sessions/` and the `Surface:` trailer.** They answer different questions — who is live now, and who wrote this — and both were paid for in one evening's incidents.

## 5. The freeze, which is already ruled

**Q7, ruled by the owner:** *freeze = leads and agents log concerns; the owner decides whether to change.* Apply it as written, starting now:

> **No new governance mechanism until a human has played a duel**, except to repair something demonstrably broken. Concerns are logged — a line in the relevant brief — not built.

The test for "broken": it refused work that was legitimate, or it silently failed. Both happened tonight and both were repairs worth making. Nothing on the current queue meets that bar.

## 6. What the freeze frees, in order

1. `02-ontology.md` — every stub and the schema wait on it. **C19 deferred every term to this pass**, so it also unblocks the vocabulary.
2. `data/SCHEMA.md` + `validate.py` — the demo gate.
3. Distill `10` → `11` → `13` → `14` → `12` → `15`, against the definition of *distilled* now in the gate (D5.49).
4. D1–D4 compression — no longer urgent; the text is in `sources/v1/`.

## 7. For the owner and Chief of Staff

1. Retire the sweep — or keep it and say what it does that the watcher does not.
2. Narrow reports to separate sessions.
3. Rule on §4 #3: is two-tier numbering worth its cost at this size?
4. Adopt §5 as a dated freeze, with the repair exception stated.
5. Tech's honest position: it built the sweep, the reports, the trailer, the register, the watcher and the bridge, and is proposing to cut two of its own. The machinery is now more sophisticated than the game it is for, and the correction should start with whoever built the most of it.
