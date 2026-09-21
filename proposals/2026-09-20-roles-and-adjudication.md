# Roles and adjudication — 2026-09-20

**Produced by:** Chief of Staff (Cowork), owner in session · **Status:** **PROMOTED D5.29** (2026-09-20) · rides with `2026-09-20-lead-reformulation.md` (D5.29); §2 here becomes `leads/README.md` §"Adjudication" if accepted.

## 1. Roles — one line each

| Role | Surface | Owns the question | May decide | Must propose |
|---|---|---|---|---|
| **Owner** | chat | everything | D-numbers, scope, conflicts, sequence | — |
| **Chief of Staff** | Cowork | is the project organized? | triage routing; what goes on the decisions queue and in what order; conflict framing | sequence, milestones (`40`) |
| **Systems** | any | what is the game? (ontology + rules) | wording of rules inside a decided D-number; vocabulary | any rule change; schema bumps |
| ↳ **Content** | any | what's in it? (instances, assets, text) | instance values inside the schema; which generated board to hand up | new instances beyond the MVP list |
| ↳ **Tech** | Claude Code | what runs it, is the repo sound? | code structure; tooling; git mechanics; housekeeping | anything that changes a rule, a doc, or `.gitignore` policy |
| **Art** | any | how it reads visually | accept/return a board against the style card | influence-table changes; style card itself |
| **Level** | any | space: what a scene affords | layout inside Systems' spatial model | anything needing a new spatial term |
| **Scenario** | any | what happens in a fight | opponent scripts, loadouts, playtest protocol | M1 content adds; win-condition changes |
| **Marketing** | any | how it's shown | episode drafts | scope, cadence, what's showable |

"May decide" = acts without asking, records in its own brief. "Must propose" = writes to `proposals/`, waits for the owner.

## 2. Adjudication — how decisions reach the owner

**One queue, on the board.** `STATUS.md` gets a section **Decisions queue**, kept by Chief of Staff. Never more than **5 items**; ranked by what they unblock. Each item is four lines:

```
Q<n> · <question in plain words> · blocks: <what waits on it>
  A: <option> — <one-line trade-off>          ← recommended by <lead>
  B: <option> — <one-line trade-off>
  C: <option> — <one-line trade-off>          (optional)
```

**How an item gets there.** A lead writes a proposal → Chief of Staff reduces it to the four-line form (the lead's recommendation is marked; Chief of Staff may add its own if different, marked as such) → it enters the queue when there is room. Proposals not yet queued are listed one-line under **Waiting** so nothing is lost.

**How the owner rules.** In chat or by editing the file: `Q3: A` · `Q3: A, but <amendment>` · `Q3: reject` · `Q3: defer to <gate>`. One word suffices. A verdict in the file or in chat *is* the instruction rule 4 requires.

**What happens next.** Chief of Staff moves the item to **Ruled** (one line, dated) and hands it to the owning lead. The lead logs the D-number and edits the doc in its next session (rule 5), then clears the line. Conflicts between leads use the same queue — the two leads' positions are options A and B.

**Ladder.** A question is answered at the lowest rung that can:
1. Lead, inside its "may decide" column — no queue.
2. Two leads, by the umbrella rule (`direction/README.md` §split) or Systems' vocabulary — no queue.
3. Chief of Staff frames it → queue → owner.
Anything that reaches the owner arrives with options and a recommendation, never as a raw proposal.

**Reading load for the owner:** the queue, and nothing else, unless they want the proposal behind an item. Detail stays on disk.

## 3. Seed queue (what would be on it today)

```
Q1 · Armed-ability economy: holding a reaction is free, so arming everything every round is dominant · blocks: 10, 12, schema v3
  A: `hold` cost mandatory for reactions/sustained — existing vocabulary, no new mechanic   ← Systems
  B: pay on arm, spent whether or not it fires — arming becomes a bet
Q2 · Initiative: one bar, or nested bars (pair · team · fight), with distance moved off the bar onto the map · blocks: 11, 14, D5.24
  A: nested bars, distance on the map (C13 + C20 as stated)   ← Systems
  B: keep one bar as-is until the demo is played; C13/C20 wait
Q3 · Vision paragraph: is it the pitch, or the test everything is held against? · blocks: 00-steer §1, vision-coherence findings
  A: pitch — pillars are the test; §1 stops being cited as canon   ← Chief of Staff
  B: test — §1 must carry pillars 3 and 6 and be corrected now
Q4 · Confirm the critical path on the board as written · blocks: nothing, settles sequence
  A: confirm   ← Chief of Staff
  B: amend (say what)
Q5 · Marketing: record from now, or from the first playable demo · blocks: marketing scope
  A: from M1 — nothing showable yet   ← Chief of Staff
  B: from now — design-process devlog
```

Waiting: coherence-pass clashes C–F and the four readings (`c-coherence` §2–§3); pillar strains P2a/P3a (`vision-coherence` §3); Godot version; which smoketest PNGs to keep.
