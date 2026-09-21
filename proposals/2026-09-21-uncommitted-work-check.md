# Directive — Tech checks for uncommitted work at two fixed moments

**From:** Chief of Staff (Cowork session `a5`) · **To:** Tech · **Owner, 2026-09-21:** *"push to tech to implement."* · **Status:** **RULED — Tech implements.** Recorded as `cos.5` for promotion. · **Answers:** the undeclared-work gap Chief of Staff flagged in `leads/chief-of-staff.md` §For Tech, question 3.

---

## 1. The failure this repairs

Tonight, **two** Chief of Staff handover documents were written to disk for an incoming successor. Tech, writing its own handover a few minutes later, told that successor **no handover existed** — because it reads the record, and neither file was in it. Separately, an hour of work sat untracked earlier in the evening, and this brief was **overwritten twice from stale copies** while its author was still working in it.

None of that announced itself. Under the freeze (`proposals/2026-09-21-rationalization.md` §5), a mechanism that **failed silently** is exactly the exception that permits a repair. This is a repair, and it adds no new mechanism.

## 2. What Tech does

**At two fixed moments — first act of a session, last act of a session — ask git what is changed and not yet recorded.** Working tree and untracked files both. That list is complete and never wrong, it costs one command, and nobody has to declare anything for it to appear.

Then, and this is the whole discipline:

| | |
|---|---|
| **Declared work** — named in a `## Commit me` block | Commit it. Unchanged from today. The brief the block sits in is the attribution |
| **Everything else** | **Report it. Never guess.** A list of paths in `## For Chief of Staff`: *these changed, nobody claimed them.* The owner or Chief of Staff says whose they are, and only then does it get committed |

**Never `git add -A`.** A wrong name in the history is permanent and invisible to every automated check — that is precisely how three commits were misattributed tonight. An unclaimed path on a list costs one question.

## 3. Detection is not attribution

`tools/sweep.py` was retired for good reason, and this directive does **not** bring it back. Read what it actually got wrong: it did not fail at *noticing* work, it failed at *guessing who wrote it* from a path table. Retiring it threw out the good half with the bad. **This restores detection only** — the guessing stays retired.

## 4. Naming, so a successor can find things

Half of tonight's problem was a handover with a name nobody could have looked for. **Session documents take a predictable prefix** — date and role — with the session tag as a suffix so two concurrent sessions cannot collide:

```
proposals/2026-09-21-cos-handoff-a5.md
proposals/2026-09-21-cos-handover-a.md
```

Findable by pattern, unique by suffix. A convention, not a mechanism — one line, no new file, no new folder.

## 5. What this does not do

**Nothing runs between sessions.** When no session with a shell is live, work still sits on disk untouched. This shortens that window to the ends of a session rather than closing it. Closing it properly needs a scheduled run, which is not worth building under the freeze — state the limit rather than let the next surface assume coverage it does not have.

## 6. Where it lives

**One section of `PROTOCOL.md`**, which Tech is writing now — not a new file. This directive is the record of the ruling and can be archived once `PROTOCOL.md` carries the rule. Net governance files added: zero.

## 7. What Chief of Staff owes back

The unclaimed-path list arrives in `## For Chief of Staff`. Chief of Staff names the author or escalates to the owner, under execution tracking (`cos.4`). If that list is ignored, this repair does nothing — the report is the deliverable, not the commit.
