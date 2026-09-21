# Proposal — clean slate: three roles, one tree per role, one board, two pages of protocol

**Produced by:** Chief of Staff, Cowork session B, 2026-09-21 · **Owner:** *"keep the game; consider all governance previously decided as background and a first rough draft; propose a clean slate design; redefine roles and protocols creatively."* · **Status:** **APPROVED by the owner 2026-09-21** (*"approved"*, after the amendments in §10) — logged **D260921.1-P** and **D260921.2-P**. Builder works from this document. The game design (`design/`, `data/`, D-numbers about rules) is untouched. Everything about how agents work is redesigned from the failures, not from the existing rules.

## 0. The diagnosis, in one line each

1. **Several agents write one working tree; one of them cannot commit.** Every lost write, misattribution, revert, sweep, watcher, drift guard, permissions table and unclaimed-work report exists because of this one fact.
2. **Communication is files the reader must already know to open.** Channels, bridges, `## For` sections, handshakes — all are attempts to make a reader open a path. None can.
3. **Nine roles for a solo hobby project** with two or three sessions at a time. Six of the nine briefs are stubs; the three that are used became logs (21–53 KB).
4. **The state of the project is spread across briefs, channels, handoffs and proposals**, so every fresh session starts with 150 KB of reading and still misses things.
5. **Governance became the product.** 31 of 50 decisions, ~25 of 40 proposals.

## 1. Five principles

| # | Principle | What it deletes |
|---|---|---|
| 1 | **One clone per role. Git is the only channel.** A role writes only its own clone; attribution is the clone; merging is git's job; a conflict is visible, never silent | shared-tree overwrites · sweep · watcher attribution · `Surface:` trailer · permissions table · single-writer rules · drift guard · unclaimed-work report · `## Commit me` |
| 2 | **One board, `STATUS.md`, is the only inter-agent document.** Every session reads it first and updates its own section last. Asks between roles are rows on it. Nothing else is a channel | `## For`/`## From` sections · `bridge/` · handshake · per-session handoff files · 30-item channel logs |
| 3 | **Three roles.** Owner decides. **Designer** — the game (rules, ontology, direction, content). **Builder** — what runs it (engine, data, tools, git). **Steward** — the board, the queue, triage, the owner's digest. Everything else is a *task*, run as a session with a prompt, output to `proposals/` | six briefs · sub-lead hierarchy · execution-agent rules · routing tags |
| 4 | **Decisions are the owner's words plus a date.** The session with the owner present logs the row itself; the ID is `D<yymmdd>.<n>` (`D260921.3`), so no session needs another to number anything | local refs · promotion · ratification · next-free counters · C-refs · `inbox/` as a separate stage |
| 5 | **Budgets are the rules.** `PROTOCOL.md` ≤ 2 pages · `STATUS.md` ≤ 1 page · each charter ≤ 1 page · a fresh session reads ≤ 20 KB before working. A process change is one dated line in `PROTOCOL.md` §Changes and must delete a line somewhere | freeze-as-doctrine · minimize-as-doctrine · rationalization passes |

## 2. The files — everything a session can touch

```
PROTOCOL.md          how we work: roles, the session contract, git rule, decision rule, budgets, §Changes   ≤ 2 pages  (Builder keeps it)
STATUS.md            one board: phase · queue for the owner · one section per role (state · next · asks)   ≤ 1 page   (each role its own section)
roles/{designer,builder,steward}.md   charter only — what it owns, what it never does                       ≤ 1 page each, rarely changes
design/  data/       the game — unchanged                                                                   (Designer, with owner present; Builder for data/schema)
design/decisions.md  the log — unchanged format, new ID scheme going forward                               (any role, owner present)
proposals/           anything, by anyone, in a file of its own; archived when ruled                        (all)
sessions/            live-claim files, one per role, deleted at close                                      (each role, its own)
```

Deleted or archived: `leads/` (9 briefs + README) · `inbox/` (owner's words go straight into the decision row or the proposal they answer) · `bridge/` · `sessions/README.md` (template moves into `PROTOCOL.md`) · `tools/sweep.py`, `tools/watch.py` (see §3) · hooks that check attribution (a clone is its own attribution; keep the hook that refuses `git add -A` and edits to `decisions.md` without an owner-present line) · handoff and handshake proposals (archived) · the Project mirror (the Project reads the repo, or nothing).

## 3. The session contract — the whole of `PROTOCOL.md` §1

> **Start.** Pull. Claim `sessions/<role>.md` (one already there = ask the owner). Read `STATUS.md`, your charter, and only the docs your task names.
> **Work.** Write only in your clone. Owner present → you may log a decision and edit canon. Owner absent → `proposals/` only.
> **Stop.** Update your section of `STATUS.md` (state · next · not finished · asks). Commit with a message that is your report. Push. Delete your claim.

That is the handoff, the report, the channel and the audit, in one act every session already does.

**Cowork has no git — two ways to satisfy the contract, owner picks:**
- **A. Steward's own clone, committed wholesale.** A Builder-side script commits and pushes *everything* in the Steward clone on a timer or at Builder's session start — no path guessing, no request block, no attribution problem: everything in that clone is the Steward's by construction. Tech has already started moving the Steward copy to `C:\Claude\shinobi-cos`, so this is half-built.
- **B. Steward is chat-only.** It reads the repo, briefs the owner, frames the queue, and the owner or Builder types its rows. Zero mechanism. Costs the owner keystrokes.

## 4. `STATUS.md` — the one board

```
# STATUS — <date>
Phase: pre-production → Godot 1v1 duel demo. Human duels played: 0.
## For the owner — rule on these (≤ 5)
Q1 · <question> · A: … / B: …   ← recommended
## Designer      state · next · not finished · asks: Builder → <one line>
## Builder       state · next · not finished · asks: Designer → …
## Steward       state · next · not finished · asks: owner → …
## Critical path  <one line, dated CONFIRMED>
```

An **ask** is a row in the asker's section naming the other role. The other role reads the board at start, so it is found. When done, the asker deletes its row. No other mechanism exists, so nothing can be missed by not knowing it exists.

## 5. Decisions — the whole of `PROTOCOL.md` §3

> A decision is one row in `design/decisions.md`: ID `D<yymmdd>.<n>`, the owner's words verbatim, the rule in one line, tag (S/A/C/E/P), what it supersedes. Written **in the session the owner rules**, by whichever role is present. Never renumbered, never rewritten; later row wins. A doc that disagrees with the log is wrong.

The owner's verbatim words *are* the inbox; they live in the row. `proposals/` is where a question is framed before the owner rules; `STATUS.md` §For the owner is where it waits.

## 6. Roles — one paragraph each (the charters)

- **Designer** (any surface; owner present for canon). *Owns:* what the game is — rules, ontology, vocabulary, art and level direction, content lists, `design/`, `data/` values. *Never:* tooling, git policy, the board's queue order.
- **Builder** (Claude Code; the only role that must have git). *Owns:* what runs it — Godot, schema and validator, tools, hooks, `PROTOCOL.md`, the repo's health, archiving. *Never:* a rule, a look, a decision, another role's board section.
- **Steward** (Cowork). *Owns:* `STATUS.md` shape and the owner's queue, triage of the owner's words into questions, the digest on demand, the audit of `decisions.md` rows against the owner's words, conflict framing. *Never:* content, mechanism, numbering, another role's section.

Tasks that used to be leads — art execution, level, scenario, marketing — are sessions launched by a role with a one-line prompt, writing to `proposals/` (or `proposals/art/`), under that role's name.

## 7. Migration — one Builder session, one Steward session, then stop

1. **Builder:** one clone per role (Steward's already moving) · write `PROTOCOL.md` (§3 + §5 + budgets + §Changes) · write the three charters from the existing briefs' *Owns* lines · collapse `STATUS.md` to §4 · archive `leads/`, `inbox/`, `bridge/`, ruled proposals, handoffs · delete sweep/watcher or reduce to the wholesale-commit script (§3 A) · keep D5.x rows as they are; new IDs from the switch date.
2. **Steward (owner present):** audit `PROTOCOL.md` against this proposal · confirm the three charters · seed the board's §For the owner with the game questions that actually block M1 (card model, reserve object, `02-ontology.md`).
3. **Hard stop.** Next session is Designer with the owner: `02-ontology.md`. No process change until a paper duel has been played. The measure: a fresh session's reading before first useful act, ≤ 20 KB.

## 8. What is lost, honestly

- Per-lead history in briefs — it is in git; the briefs are archived, not deleted.
- The hop between "owner said" and "row logged" that let a second party check — replaced by the Steward's after-the-fact audit of rows against quoted words, which is what the hop was for.
- Fine-grained roles (Direction/Level/Scenario) as standing seats — they return as tasks, and as seats if the project ever needs them.
- Anything the sessions register cannot catch: two sessions of one role on two clones will merge, not overwrite; the worst case becomes a visible git conflict.

## 9. For the owner

**Ruled: adopted, with §10.** `proposals/2026-09-21-simplify-a.md` is superseded by this document.

## 10. Amendments agreed in conversation before approval (2026-09-21) — these override §1–§9 where they differ

1. **Every role runs on Claude Code**, including the Steward. Cowork is the owner's **read-only console** (digest, framing, reading) on any device; it never writes to the repo. §3's Cowork options A/B are struck.
2. **Worktrees, not clones.** One repo, `git worktree add` per role; the launcher creates them. A history operation in one worktree cannot touch another.
3. **One launcher command** (Builder writes it, `tools/start`): pulls, creates the worktrees, writes the `sessions/<role>.md` claims, opens one Claude Code tab per role with that role's standing prompt. Task sessions (art batch, archive pass) launch the same way with a task string, headless where unattended. `stop` runs each role's close and reports any merge conflict.
4. **Per-role status files, rendered board.** Each role owns `status/<role>.md` (≤ 5 lines: state · next · not finished · asks). `STATUS.md` is **generated** by the stop step from those files plus the Steward's queue view — never hand-edited. §4 as a hand-edited file is struck; four small files that never conflict, one page that is always the latest render.
5. **Escalation is `queue/` and nothing else.** A role that needs the owner writes `queue/<date>-<topic>.md` in the four-line form (question · A/B with one trade-off each · recommendation · what it blocks), commits, pushes. **Cap five unanswered.** Anything that does not block work is a proposal, not a queue item.
6. **The owner is prompted, never expected to read.** A scheduled cloud task pulls the repo, reads `queue/`, and sends a push notification to the owner's phone only when something is unanswered. The owner answers in that session (`Q1: A`); the session writes the words into the queue file as the ruling, logs the decision row, commits, pushes, deletes the queue file. An answer in a queue file **is** the owner's instruction, wherever it was given — "owner present" is no longer a bottleneck for logging.
7. **Symmetric surfaces.** Phone, Mac and PC each run Claude Code and Cowork; a session from any of them is a clone of the GitHub repo with git. The PC is where the launcher and the Godot build live; nothing else is PC-bound.
8. **Decision IDs** `D<yymmdd>.<n>-TAG` from 2026-09-21; D5.x rows stand as they are.
9. **Hard stop after migration** (§7 step 3) stands: next session is Designer with the owner on `02-ontology.md`; no process change until a paper duel has been played; the measure is a fresh session's reading before its first useful act, ≤ 20 KB.
10. **Interim rulings earlier tonight** (one ID chain, brief cap ≤ 8 KB, multi-session essential, C33 1 A / 2 B, handshake binds, handover A attributed) are recorded verbatim in `inbox/2026-09-21-permissions-rulings.md` and are **superseded by this design where they differ**; where they agree (multi-session, short documents, one chain) they are simply restated here.

## 11. Builder's migration checklist (one session)

- [ ] `tools/start` / `stop` launcher; worktrees per role; claims written by the launcher
- [ ] `PROTOCOL.md` ≤ 2 pages: session contract (§3) · git rule (own worktree only; never `add -A` outside it; no history ops on a worktree you do not own) · decision rule (§5 + §10.6) · queue rule (§10.5) · budgets · §Changes (append-only, dated)
- [ ] `roles/designer.md`, `roles/builder.md`, `roles/steward.md` ≤ 1 page each, from §6 and the existing briefs' Owns lines
- [ ] `status/<role>.md` × 3 seeded from the current board; `STATUS.md` render script in the stop step
- [ ] `queue/` folder with a `_TEMPLATE.md` (four lines)
- [ ] Archive: `leads/`, `inbox/`, `bridge/`, ruled governance proposals, handoffs → `proposals/archive/` (keep anything an open decision points at: `initiative-and-earmarks`, `c-coherence`, `vision-coherence`, `ontology-draft`, design/world content)
- [ ] Retire `tools/sweep.py`, `tools/watch.py`, attribution hook; keep the `add -A` and `decisions.md` guards
- [ ] `AGENTS.md` → what the game is + the seven rules + one pointer to `PROTOCOL.md` (≤ 3 KB); `CLAUDE.md` → one line
- [ ] `PROTOCOL.md` §Changes first line: this migration, dated
- [ ] Verify: a fresh Steward tab from the launcher reads ≤ 20 KB before its first act; the stop step renders `STATUS.md`; a test `queue/` item round-trips through the doorbell

**Steward's session after that (owner present):** audit `PROTOCOL.md` and the charters against this document; seed `queue/` with the three game questions that block M1 (card model / C23 · reserve object · `02-ontology.md` scope). Then the hard stop.

## 12. Naming and messaging grammar (Steward, 2026-09-21 — one section of `PROTOCOL.md`, ≤ half a page)

**Ruled (owner, 2026-09-21):** the owner answers the doorbell as `Q1: A` / `Q1: B` / `Q1: A but …` / `Q1: later`. The doorbell numbers items per message, oldest first, and resolves `Q<n>` only against the list it sent in that session; the `Ruled:` line and the decision row cite the queue file, so the record is stable while the reply stays short.

**Proposed, for Builder to implement unless the owner objects:**

| Naming | Form | Example |
|---|---|---|
| Role | lowercase, one word; the tag everywhere | `designer` · `builder` · `steward` |
| Session | `<role>-<yymmdd>-<letter>`; task session `<role>/<task>-<yymmdd>-<letter>`. Launcher assigns the letter. Used as claim-file name, worktree name, commit author string | `steward-260921-b` · `designer/art-260922-a` |
| Worktree / branch | `wt/<session-id>`; merged to `main` at stop, deleted after | |
| Commit message | `<session-id>: <what changed>` + `D…` / `Q…` refs. The commit is the report | `builder-260922-a: PROTOCOL.md v1 (D260921.1)` |
| Decision | `D<yymmdd>.<n>-TAG` (S A C E P) | `D260921.2-P` |
| Queue item | the filename is the ID and is stable | `queue/260921-card-model.md` |
| Ask | `A<yymmdd>.<n>` per asker, in the asker's status file | `A260922.1` |
| Document markers | unchanged, `design/` only: DECIDED / PROPOSED / OPEN · MVP / TARGET / FUTURE | |

**Messaging — four verbs, nothing else**
1. **Report** — commit message + `status/<role>.md`. Audience: everyone, at next start.
2. **Ask** — one row in the asker's own status file: `A260922.1 → builder · <one line> · blocks: <what>`. Addressee writes `ack A260922.1 <date>` in its own file, then `done A260922.1 · <one line>`; asker deletes its row. Two files, no cross-writing; the rendered board shows both.
3. **Escalate** — a queue file, to the owner only (§10.5).
4. **Propose** — a proposals file, to anyone; no reply owed.

**Live nudge:** a Claude Code session may message another live session only to say "read the board" — never to carry content. Nothing is lost if the addressee is not live, because the content is already on the board.
**Task sessions** report in `status/<role>/<task>.md`; the role folds it into its own file.
