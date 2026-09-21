# Scheduler — spec for a successor Builder

**Status:** PROPOSED · `builder-260921-c`, 2026-09-21. Not built deliberately: the owner
called a halt to bootstrapping, and this is the largest remaining piece. Recorded so it is a
decision to take rather than a thing rediscovered.

## The problem it solves

Roles only exist when the owner starts them. Designer has **never run**. Steward ran once and
went stale in three hours. So an ask addressed to a role that is not running — `A260921.9` has
been open since this morning — stalls indefinitely, and **nothing reports that it is stuck**.

That is the gap between "three roles" as written and "one agent at a time" as observed. No
amount of channel design fixes it; something has to either start a session or tell the owner
one is needed.

## What exists, and why it does not work

`D260921.2-P` ruled a doorbell: a scheduled Claude Code cloud task, every two hours, push
notification when `queue/` holds an unanswered item. The prompt is `queue/_DOORBELL.md`.

It has never run, and as written it cannot:

1. **Step 5 pushes to `main`**, which is gated with no bypass actors. It would fail every time
   it actually had a ruling to record, and its own instruction is to leave the commit local —
   so the owner's answer would never reach the repo.
2. **Step 1 names `chris-egan/slop-game`**, the pre-transfer URL. Redirects save it, for now.
3. It was written for an owner who commits. `D260921.5-P` and `D260921.6-P` say he does not.

## Recommendation: make it read-only, and build nothing else yet

The doorbell's write half is what breaks it, and the write half is unnecessary. The owner
answers in chat, in a session that can log the decision properly under `PROTOCOL.md` §4 —
which is how every decision on 2026-09-21 was logged.

So: **pull, read, notify. No commits, no pushes, no credentials beyond read.**

- Reads `queue/` for items with no `Ruled:` line, and `STATUS.md` for ask rows.
- Notifies only when something is genuinely waiting. Silence otherwise — a doorbell that rings
  every two hours is one the owner stops hearing.
- Reports an ask's age. **Age is the signal** — the failure being caught is an ask nobody has
  looked at, not an ask that exists.
- Writes nothing. A read-only task cannot corrupt the repo, cannot trip a guard rail, and
  needs no machine-account credential at all.

That is a prompt and a schedule. It is not a program.

## What is deliberately out of scope

**Starting role sessions automatically.** An autonomous Designer that commits unattended is a
much larger claim than a notifier, and nothing yet shows it is needed: the owner has been
present for every session so far. Build the notifier, watch whether stalled asks actually
surface, and decide with evidence. `C28` — no new machinery without a demonstrated need.

## Acceptance

Not done until all four hold:

1. It runs on a schedule, from an environment that can reach the repo.
2. With nothing waiting, it is silent — verified by a run with an empty queue.
3. With something waiting, the owner gets a notification naming the item and its age —
   verified by a deliberate unanswered item, then removed.
4. It has no write credential. If it can push, it is the wrong design.

Point 2 is the one that will be skipped. A notifier that cannot demonstrate silence has not
been tested, only observed being noisy.

## Owed first

`queue/_DOORBELL.md` still carries the broken write steps and the stale URL. Whoever builds
this replaces that file rather than working around it — two versions of the same instruction
is how this project spent 2026-09-20.
