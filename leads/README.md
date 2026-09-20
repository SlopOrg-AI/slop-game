# leads/ — discipline leads (how the project is run)

**Set up:** 2026-09-20, owner-directed (Cowork session); adopted with the `admin` lead by **D5.27**. Owner is the sole decision-maker; leads are agent roles that track status, synthesize owner feedback, and direct next steps within their discipline. `AGENTS.md` rules 1–7 apply unchanged — a lead never logs a D-number on its own.

## Tree

```
admin.md               router: triage, STATUS.md (sole writer), milestones, 40-production, git
systems.md             the game: ontology + rules. Directs content/ and tech/.
  systems/content.md   what is included: data instances, assets, animations, effects, text
  systems/tech.md      what runs it — Tech lead = Claude Code: Godot, validator, tooling, git, .claude
direction/README.md    umbrella: shared anti-goals, cluster → Content handoff
  direction/art.md     art direction (30, influence table, board critique)
  direction/level.md   scene / zone / diorama / table design
  direction/scenario.md mission, encounter, duel setup, AI opponent behaviour
marketing.md           YouTube / devlog
```

**Flow:** Direction defines a *cluster* (a coherent set of things the game needs) → Content produces it → Tech loads it. Systems arbitrates vocabulary and rules for all three. Admin keeps the board, routes feedback and runs git.

## Routing tags

`[admin] [sys] [content] [tech] [art] [level] [scenario] [mkt]` — one or more per feedback item. Unsure → `[sys]` and let Systems re-route.

## Triage protocol (owner feedback → leads)

1. Owner writes feedback verbatim to `inbox/YYYY-MM-DD-<topic>.md` (or says it in chat; the agent in session files it there).
2. Triage — Admin, or whichever agent is in session, on owner instruction: split into numbered items **C<n>** (continuing the C-ref sequence; next free is noted in `STATUS.md`), tag each, append to the target lead's **Inbox** table with the C-ref and the owner's words. No paraphrase that changes meaning. Mark the inbox file `TRIAGED YYYY-MM-DD` at the top.
3. Lead session: work the inbox → synthesis → `proposals/<date>-<topic>.md` → owner promotes (D-number in `decisions.md`, doc edited) → lead moves the item to its status table as DECIDED / REJECTED / DEFERRED.
4. Cross-lead conflict → `STATUS.md` **Conflicts** table. Owner resolves; Admin records the outcome.

## Single-writer rules (D5.27)

Two writers, two scopes — the fix for `STATUS.md` being overwritten twice in one day:

1. **A lead's own brief** (`leads/<lead>.md`) has one writer: that lead, on whichever surface is running it (Claude Code, Cowork, Codex). No other lead edits it; Admin included — Admin asks the lead or the owner and transcribes.
2. **`STATUS.md`** has one writer: **Admin** (Claude Code). It transcribes each lead's row from that lead's brief. A row edited anywhere else is a draft, not the board. A second copy of the board anywhere (Project mirror included) is drift by construction.

## Running a lead session

Prompt shape: *"Act as `<lead>`. Read `AGENTS.md`, `design/00-steer.md`, `leads/<lead>.md`, then only the docs the task touches."* Claude Code: `.claude/agents/<lead>.md` points at the same brief. Codex / ChatGPT / local: same reading order, output to `proposals/`.

At the end of every lead session the lead updates its own file (inbox, status, next actions) and writes its board row there — phase, blocked on, next action. Admin transcribes it into `STATUS.md` (single-writer rule 2). That is the whole reporting requirement.

## Registers (C21 + C22, `AGENTS.md` §5)

Briefs, proposals, the board, triage and handoffs are **agent-facing**: compress hard, cite paths, one line per fact. Chat replies to the owner are **user-facing**: lead with the answer, plain sentences, and spell out `M1`, D-numbers, C-refs and lead names on first use or leave them out. Same budget, different readers.

## Brief template (≤ 1 page each)

```
# <Lead> — lead brief
Reports to: owner | Directs: … | Updated: YYYY-MM-DD
## Charter        one paragraph: the question this lead owns
## Owns           docs / data / dirs
## Does NOT own   explicit exclusions (mirrors the influence-table discipline)
## Reads first    ordered list
## Inbox          | C-ref | Owner said | From | Status |
## Status         | Item | Status | Scope | Source |   (DECIDED/PROPOSED/OPEN · MVP/TARGET/FUTURE)
## Next actions   ≤ 3, each with a gate
## Open questions
## Escalates to   who decides what this lead can't
```
