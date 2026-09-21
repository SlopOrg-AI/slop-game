# sessions/ — who is live, in which role, right now

One file per role, named for its routing tag: `tech.md`, `cos.md`, `art.md`, `sys.md`…
**Creating the file is the claim. Finding one already there is the collision.**

**An empty folder is a normal state.** Not every lead runs every day, and a role with no file simply has no live session. Absence is never an error.

## Why it exists

On 2026-09-20 two Claude Code sessions both read *"Claude Code is the Tech lead"*, both concluded it meant them, and both spent hours writing the same brief, designing the same bridge and holding the same numbering authority. Neither could see the other, and `Surface: tech` cannot tell two sessions of one seat apart. This register makes that visible in seconds.

## At session start

The **owner confirms lead or subordinate**. Then:

1. Read this folder. If your role already has a live claim naming a different session, **you are not that role** — stop and ask the owner.
2. Claim it. With a shell: `python tools/session.py claim tech --kind lead --name "<session name>"`. **Cowork has no shell**, so write the file by hand — the format below is the whole specification.
3. Refresh `Last seen` as you work, and **release at session close**: delete the file, or `python tools/session.py release <tag>`.

## The format — copy this

```markdown
# Live session — `cos`

- **Role**: cos
- **Kind**: lead
- **Session**: Cowork — chief of staff, 2026-09-21
- **Claimed**: 2026-09-21 00:30
- **Last seen**: 2026-09-21 00:30
```

`Kind` is `lead` or `subordinate of <lead>`. A second subordinate under one lead takes `art-2.md`.

## Staleness

A claim whose **Last seen** is more than **3 hours** old is presumed dead and may be taken — say so in the file when you take it. Sessions end without warning and nothing cleans up after them, so a register with no expiry becomes a register of ghosts.

## What this is not

**Not proof, and not enforcement.** A session states who it is and cannot demonstrate it, so any session can overwrite any claim in good faith — which is exactly how the collision it exists to catch happened. Only the owner can say who holds a role. What the register buys is finding out in seconds rather than after four hours.
