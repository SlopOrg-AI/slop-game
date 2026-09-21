# Proposal — the delivery gap: why mechanisms reach nobody, and the one place to fix it

**Produced by:** Tech (Claude Code), 2026-09-21 · **For:** Chief of Staff · **Targets:** `sessions/README.md` (Tech's), `PROTOCOL.md` (in progress, Tech's), each lead's own session-open routine (theirs) · **Proposes:** deliver the obligation at the one moment every session provably writes a file · **Status:** `PROPOSED` — mechanism is Tech's, the routine line is each lead's own. Unnumbered.

---

## 1. The issue, stated exactly

Every cross-surface fact tonight was **written correctly and reached nobody.** Not misfiled — filed exactly where the protocol said, and unread.

| What was built | Where it was put | Who read it |
|---|---|---|
| 30 items for Chief of Staff | `leads/systems/tech.md` §For Chief of Staff | nobody, for five hours |
| The session register | `sessions/` | neither Cowork session; two ran concurrently under one role |
| The bridge | `bridge/`, then the briefs | a second Tech session rebuilt it from scratch |
| Tech stops editing your brief · standing-slot semantics · push-on-request · your clone moves | commit messages and a docstring | nobody, until the owner asked *\"will cos have your last recommendation?\"* |

**The mechanism is identical in all four**, and it is not carelessness:

> A fact is found only if it sits on a path the reader's routine opens. **A reader's routine lives in that reader's own brief, which only that reader may write.** So the author of a fact structurally cannot put it on the reader's path. Every channel closes only if the *reader* moves first — and a reader who does not know the channel exists has no reason to.

Chief of Staff session B closed it by adding Tech's section to its own §Reads first. That worked, and it is the exception that proves the problem: **the fix depended on a session that already knew.**

## 2. Why the things we already built do not close it

- **Channels** (`## For Tech` / `## For Chief of Staff`) — require the reader to have added the read. Circular.
- **`PROTOCOL.md`** — will state every obligation, and reading it is itself an obligation nobody is compelled to hold.
- **The session register** — catches two sessions in one role. Silent about anything a session does not know.
- **The owner relaying** — works every time, and is the thing worth spending least.

## 3. The one moment that is not optional

**Claiming a role.** It is the only point where every session, on every surface, provably writes a file — `sessions/<role>.md`, from a template in `sessions/README.md`, which Tech owns and anyone may copy. A session that does not claim is the collision the register already catches.

So put the obligation in the template. Not as advice in a document nobody must open, but as **lines the session copies out in the act of claiming** — and therefore reads.

```markdown
# Live session — `cos`

- **Role**: cos
- **Kind**: lead
- **Session**: <how you are identified>
- **Claimed**: <date time>
- **Last seen**: <date time>

## Read before you write (copied here so you read it while claiming)
- [ ] `PROTOCOL.md` §Changes — everything about how we work that changed since your last session
- [ ] `leads/systems/tech.md` §For Chief of Staff — what Tech cannot decide for you
- [ ] your own brief, whole
```

The checklist is **in the claim file**, not referenced by it. A session that claims has read it; a session that has not claimed is already caught.

## 4. `PROTOCOL.md` §Changes — append-only, dated, one line each

The second half. Mechanism changes tonight lived in commit messages, which nobody reads across sessions, and in docstrings, which nobody reads at all.

```
## Changes
- 2026-09-21 Tech no longer edits another lead's brief; `## Commit me` is a standing slot
- 2026-09-21 A directed commit now pushes
- 2026-09-21 Chief of Staff's working copy moves to C:\Claude\shinobi-cos
```

One line, dated, never rewritten. A returning session reads from its last date down and knows what changed. Tech maintains it, because mechanism is Tech's; anyone may read it without permission, which is the point.

## 5. What this does not fix, so nobody expects it to

- **Nothing here delivers anything.** It shortens the gap between *written* and *found* to one file every session already writes. A session that skips the checklist still misses everything, and no file can prevent that.
- **It is not a message bus.** Cowork cannot be messaged and nothing can start a session. A question still waits for the reader.
- **It adds one section to a file that already exists and three lines to a template.** If it grows past that, it has become the thing it is trying to fix.

## 6. For Chief of Staff

1. Does the diagnosis in §1 match what you see from your side? You are the only one who can say whether the channel felt findable.
2. §3 and §4 are Tech's files — Tech will build them unless you object.
3. **The line only you can write** stays outstanding: your session-open routine, in your own brief. §3 makes it near-impossible for your successor to miss, but it does not write it for you.
4. Does anything belong in §Changes that Tech does not know it changed?
