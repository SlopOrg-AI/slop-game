# leads/ — discipline leads (how the project is run)

**Set up:** 2026-09-20, owner-directed. Adopted D5.27; reformulated same day (Chief of Staff on Cowork, Tech takes git + housekeeping, `admin` retired — **D5.29**; board custody split **D5.38**). Owner is the sole decision-maker; leads are agent roles that track status, synthesize owner feedback, and direct next steps within their discipline. `AGENTS.md` rules 1–7 apply unchanged — a lead never logs a D-number on its own — it records a **local ref** in its own brief and Tech promotes it (**D5.44-EP**, §Local refs).

## Tree

```
chief-of-staff.md      Cowork. Organizes: triage, STATUS.md (sole writer), decisions queue, milestones, conflicts, handoffs
systems.md             the game: ontology + rules. Directs content/ and tech/.
  systems/content.md   what is included: data instances, assets, animations, effects, text
  systems/tech.md      Claude Code. What runs it + repo custody: Godot, validator, tooling, git execution, .claude, housekeeping
direction/README.md    umbrella: shared anti-goals, cluster → Content handoff
  direction/art.md     art direction (30, influence table, board critique)
  direction/level.md   scene / zone / diorama / table design
  direction/scenario.md mission, encounter, duel setup, AI opponent behaviour
marketing.md           YouTube / devlog
```

**Flow:** Direction defines a *cluster* → Content produces it → Tech builds and loads it. Systems arbitrates vocabulary and rules for all three. Chief of Staff keeps the board, routes feedback, frames decisions. Tech runs git.

## Roles — what each may decide vs must propose

| Role | Surface | Owns the question | May decide (acts, records in brief) | Must propose (→ `proposals/`, owner rules) |
|---|---|---|---|---|
| Owner | chat | everything | D-numbers, scope, conflicts, sequence | — |
| Chief of Staff | Cowork | is the project organized? | triage routing; queue order; conflict framing | sequence, milestones |
| Systems | any | what is the game? | wording inside a decided D-number; vocabulary | any rule change; schema bumps |
| ↳ Content | any | what's in it? | instance values inside the schema; which board to hand up | instances beyond the MVP list |
| ↳ Tech | Claude Code | what runs it; is the repo sound? | code structure; tooling; git mechanics; housekeeping | anything changing a rule, a doc, or gitignore policy |
| Art | any | how it reads visually | accept/return a board against the style card | influence-table changes; the style card |
| Level | any | what a scene affords | layout inside Systems' spatial model | anything needing a new spatial term |
| Scenario | any | what happens in a fight | opponent scripts, loadouts, playtest protocol | M1 content adds; win-condition changes |
| Marketing | any | how it's shown | episode drafts | scope, cadence, what's showable |

## Routing tags

`[cos] [sys] [content] [tech] [art] [level] [scenario] [mkt]` — one or more per feedback item. Unsure → `[sys]`.

## Local refs (D5.44-EP)

A lead records an owner ruling **the session it is given**, in its own brief's `## Pending` block, under a ref in **its own namespace**: the routing tag above plus a number it issues itself — `sys.12`, `art.3`, `cos.7`. One sequence per issuer, so nothing is coordinated and nothing is advertised.

**Tech promotes.** At its next session Tech assigns the canonical `D5.nn-TAG`, writes the row into `decisions.md`, records the local ref there as a permanent **alias**, and the entry leaves the `Pending` block. Nothing is renumbered: both forms resolve to the same row forever, so a doc may cite `sys.12` before promotion and stay correct after it.

**`Pending` is a queue, not an archive** — same rule as `inbox/` (D5.42-EP cl.2). Everything upstream of the log is a buffer; the log is the record; nothing is copied.

**Two different things:** the local ref names *who recorded it*; the canonical suffix names *who must read it* (D5.43-P: **S**ystems · **A**rt · **C**ontent · **E**ngine · **P**rocess). They need not agree.

## Triage protocol (owner feedback → leads)

1. Owner writes feedback verbatim to `inbox/YYYY-MM-DD-<topic>.md` (or says it in chat; the agent in session files it there).
2. Chief of Staff (or the agent in session, on owner instruction): split into **C<n>** items (next free in `STATUS.md`), tag, append to the target lead's **Inbox** table with the owner's words. No paraphrase that changes meaning. Stamp the file `TRIAGED YYYY-MM-DD`.
3. Lead session: work the inbox → synthesis → `proposals/<date>-<topic>.md` → Chief of Staff queues it (§Adjudication) → owner rules → lead records a **local ref** in its `Pending` block, edits the doc, updates its status table. Tech promotes the ref to a D-number (§Local refs).
4. Cross-lead conflict → same queue; the two positions are options A and B.

## Adjudication — how decisions reach the owner

**One queue, on the board** (`STATUS.md` §Decisions). Chief of Staff keeps it. **≤5 items**, ranked by what they unblock. Each item:

```
Q<n> · <question in plain words> · blocks: <what waits>
  A: <option> — <one-line trade-off>     ← recommended by <lead>
  B: <option> — <one-line trade-off>
```

- **In:** a proposal is reduced to this form by Chief of Staff; the proposing lead's recommendation is marked (Chief of Staff may add its own, marked). Not-yet-queued items sit one-line under **Waiting**.
- **Ruling:** owner answers in chat or in the file — `Q3: A` · `Q3: A, but …` · `Q3: reject` · `Q3: defer to <gate>`. That verdict *is* the instruction rule 4 requires.
- **Out:** Chief of Staff moves it to **Ruled** (dated); the owning lead records a local ref and edits the doc in its next session, then clears the line. Tech promotes the ref (§Local refs).
- **Ladder:** (1) lead decides inside its "may decide" column — no queue; (2) two leads settle by umbrella rule or Systems' vocabulary — no queue; (3) Chief of Staff frames it → queue → owner. Nothing reaches the owner as a raw proposal.

### Framework freeze (Q7, owner 2026-09-20)

The way the project is run is **frozen**. A lead or agent that thinks a rule is wrong **logs the concern** — one line in its own brief, under `Open questions` — and carries on working under the rule. It does not propose a replacement, open a queue item, or write a review. **The owner decides whether anything changes**, and only the owner reopens it.

Scope: everything in this file, `AGENTS.md` §§1–6, and the process decisions in the log (`-P` and `-EP` tags). The game itself is not frozen.

## Single-writer rules (D5.27 → D5.29 → D5.38)

1. **A lead's own brief** has one writer: that lead, on whichever surface runs it. Chief of Staff asks and transcribes; never edits.
2. **`STATUS.md`** has one **author** — Chief of Staff, which decides what every row says, what is blocked, and the queue order — and one **keeper**, Tech, which types the file and commits it (D5.38). Tech transcribes without paraphrase that changes meaning and never re-sequences; where it disagrees, it writes a note in its own brief. Where Chief of Staff can reach a clone it may type its own rows; where it cannot, it hands them to Tech. Drift guard: read from disk in-session before any write; never force-write. No second copy anywhere (Project mirror included).

   *Why the wording changed:* the rule has to survive prompting moving to a Mac, where the surface that authors the board may not be the surface that can reach git. One head decides, one hand types.

## Running a lead session

Prompt shape: *"Act as `<lead>`. Read `AGENTS.md`, `design/00-steer.md`, `leads/<lead>.md`, then only the docs the task touches."* Claude Code defaults to Tech; `.claude/agents/<lead>.md` points at each brief. Codex / ChatGPT / local: same reading order, output to `proposals/`.

End of every lead session: update own brief (inbox, status, next actions) and write the board row there. Chief of Staff transcribes. That is the whole reporting requirement.

## Cost tiers

| Surface | Cost | Use for | Not for |
|---|---|---|---|
| Cowork (Chief of Staff) | highest | organizing, judgement, cross-lead review, owner conversation | reading whole docs, distillation, bulk edits |
| Claude Code (Tech; any lead on request) | mid | building, repo work, doc distillation with owner present | owner-facing sequencing |
| Codex / ChatGPT | mid | proposals, research, second opinions | anything outside `proposals/` |
| Local LLM (5090) | lowest | batch text, image pipeline | design decisions |

## Registers (C21 + C22, `AGENTS.md` §5)

Briefs, proposals, the board, triage, handoffs: **agent-facing** — compress, cite paths, one line per fact. Chat to the owner: **user-facing** — answer first, plain sentences, spell out `M1`, D-numbers, C-refs, lead names on first use or omit.

## Brief template (≤ 1 page)

```
# <Lead> — lead brief
Reports to: owner | Directs: … | Updated: YYYY-MM-DD
## Charter · ## Owns · ## Does NOT own · ## Reads first
## Inbox     | C-ref | Owner said | From | Status |
## Pending   | Local ref | Decision, one line | Ruled | Promoted |   ← D5.44-EP; cleared as Tech promotes
## Status    | Item | Status | Scope | Source |
## Next actions (≤3, each gated) · ## Open questions · ## Escalates to
```
