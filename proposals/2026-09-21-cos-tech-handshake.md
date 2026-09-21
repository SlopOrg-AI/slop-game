# Proposal — the Chief of Staff ↔ Tech handshake, from Tech's side

**Produced by:** Tech (Claude Code), 2026-09-21, owner-directed via Chief of Staff: *"check with tech - need to set up CoS tech handshake."* **Targets:** `leads/systems/tech.md` (Tech writes its own), `leads/chief-of-staff.md` (Chief of Staff writes its own), `leads/README.md`. **Proposes:** four named sections, two fixed moments, one degradation ladder. **Supersedes:** nothing; instantiates the symmetric channel sketched in `leads/systems/tech.md` and the chain in D5.42-EP cl.3 / D5.44-EP. **Status:** PROPOSED. **No new file** (C28) — four headings in two briefs that already exist.

> **Collision, found at close: `proposals/2026-09-21-bridge.md`.** A **second Claude Code session, also acting as Tech**, wrote the same channel from the same owner instruction while this session ran, and created `bridge/tech.md`. The two agree on the protocol almost exactly — one file per surface, written only by its owner, read at the other's session open, answered in your own file, sender clears. They disagree on **one thing, the path**: this proposal puts the four sections in the briefs that already exist; `bridge/` is a new folder, which its own §6 #2 calls provisional and which costs a file under C28. Its §6 #1 and this line agree on the only thing that matters: **there must not be two bridges.** Chief of Staff owns routing and picks; Tech moves either way. Neither session edited the other's file. That both existed at all is §7 #6.

**Premise neither side can wish away:** the two sessions cannot see or message each other. Nothing is *sent*. Everything is **left at a fixed path and found there**, and a handover that is not on disk did not happen.

## 1. Channel — four sections, symmetric, nobody writes another lead's file

| Section | Lives in | Written by | Read by | Cleared by |
|---|---|---|---|---|
| `## For Tech` | `leads/chief-of-staff.md` | Chief of Staff | Tech, at session open | Chief of Staff, once it sees the disposition |
| `## From Tech` | `leads/chief-of-staff.md` | Chief of Staff | — | Chief of Staff |
| `## For Chief of Staff` | `leads/systems/tech.md` | Tech | Chief of Staff, at session open | Tech |
| `## From Chief of Staff` | `leads/systems/tech.md` | Tech (records the disposition it read) | — | Tech |

Three of the four exist or are one heading away; only `## For Tech` / `## From Tech` are new, and they are Chief of Staff's to add. D5.27 holds: a lead answers **in its own brief**, never by editing the sender's. The one exception is D5.44-EP cl.4 — Tech empties a `Pending` block it has promoted, rows only.

## 2. What Tech needs **from** Chief of Staff, and in what form

| Need | Form | Why this form |
|---|---|---|
| **Board rows** | the finished row, pipe-delimited, verbatim | Tech transcribes and never paraphrases (D5.38). Only needed where Cowork cannot reach the clone (D5.42 cl.4); where it can, Chief of Staff types the board itself |
| **Refs to promote** | `<local ref> · <brief path>` — **list only, no decision text** | Tech reads the text from the owning brief. A copy in the channel is a second record (D5.42 cl.2), and a ref with no text cannot be promoted at all — see §6 #1 |
| **Review flags** | `path · what looks wrong · which rule` | Tech executes mechanical housekeeping; it does not decide that something *is* wrong |
| **Investigation requests** | one question + what a usable answer contains | Tech has git and the filesystem; Chief of Staff has neither. Without the second half Tech guesses at scope |
| **Ratification result** | `D5.nn-TAG: ratified` or `disputed — <one line>` | A promoted row is not settled for the board until this comes back (D5.42 cl.3) |

## 3. What Chief of Staff needs **from** Tech

| Need | Form |
|---|---|
| **Promoted numbers to ratify** | `local ref → D5.nn-TAG` plus the one-line claim, so ratification needs no read of `decisions.md` (D5.43-P cl.6 — matched, never read) |
| **Commit-sweep flags** | `path · what changed · why refused` (D5.39 §A.2), one line each, never dropped, never silently committed |
| **Session commit range** | `opened at <hash> · left at <hash> · N commits · paths swept` | gives the after-the-fact audit (D5.39 cl.4) a start point it currently does not have |
| **Disagreements** | one line, stated as disagreement, **never a board row** — Tech has custody, not judgement (D5.38) |
| **Tag corrections** | `D5.nn-OLD → D5.nn-NEW, reason` (D5.43-P cl.4, corrigible in place) |

## 4. When — two moments, no third

| Moment | Tech does | Chief of Staff does |
|---|---|---|
| **Session open** | sweep · read `leads/chief-of-staff.md` §For Tech · then `STATUS.md` | read `leads/systems/tech.md` §For Chief of Staff · then **every lead's `Pending` block** (D5.45-P) · then the board |
| **Session close** | write §For Chief of Staff · record dispositions in §From Chief of Staff · sweep · commit · leave the commit range | write §For Tech · record dispositions in §From Tech · clear what was answered |
| **On demand** | **does not exist.** Neither session can be woken by the other. "Urgent" means the owner carries it in chat | same |

## 5. After the Mac move — how this degrades

`tech.1` (Q9 = B) puts `Canon clone: <machine>` in the `STATUS.md` header, which is what tells both sides **which disk these four sections are on**. Without it the ladder below has no rung 0.

| State | What breaks | What the handshake falls back to |
|---|---|---|
| Cowork writes the clone | nothing | §1 as written; D5.42 cl.4 keeps the board in Chief of Staff's hands |
| Cowork reads the clone | §For Tech is unwritable; Tech's side still works | Chief of Staff hands rows to the **owner** in chat; owner writes them to `inbox/`, which is a Commit row in the sweep table |
| Cowork sees nothing | both directions dead | owner is the entire channel. Tech keeps writing §For Chief of Staff — it is on the remote (D5.40) and survives the session |
| **Commit sweep** | **inert by its own terms** (`…-commit-sweep.md` §A.4): Cowork never writes a file into Tech's tree, so there is nothing to sweep | its stated replacement is *a remote plus Cowork committing its own work*. The remote landed (D5.40); **git on the Cowork side did not**. Until it does, every Cowork write reaches the record only by the owner's hand |

**The asymmetry the move creates:** Tech ends up holding git alone, and the sweep — the one mechanism that put another surface's work into the record without asking Tech to read it — expires exactly when the attribution problem gets worse. That is a known, dated expiry, not a surprise.

## 6. The unexplained write — `inbox/2026-09-20-queue-verdicts-1.md`

**Determined, from the object store and the reflog** (no shell; loose objects read directly):

| Fact | Evidence |
|---|---|
| The file on disk is byte-identical to blob `a42da74`, 6106 bytes | sha1 of the working-tree file = the blob in tree `64fd167` |
| That blob entered history at `da46ff3`, 1789956325, *"Cowork: … verdicts update (**not authored by Tech**)"* | reflog + commit object. This was **Tech's commit sweep of Cowork's work** — Chief of Staff cannot run git (D5.29), so "committed by Chief of Staff" is wrong in its second half |
| Nothing changed the file in history after that | the `inbox` tree is the same object `64fd167` at `da46ff3` and at `87fdde5` |
| The file was rewritten on disk at 1789959502.859 | mtime = the second of the reflog entry `reset: moving to HEAD~1` (`3de6acb` → `87fdde5`) |
| The commit that reset removed was **empty** | `3de6acb` and `87fdde5` share one tree, `0066451`. Dropping an empty commit cannot change tracked content — unless the reset was `--hard`, which also restores the working tree. The mtime says it was |

**Conclusion:** after the sweep, something appended to that file and did not commit it. Tech's own `git reset --hard HEAD~1` — run to remove its guard-rail-E test commit — restored the working tree and destroyed the append. One surface's uncommitted work, erased by another surface's routine history cleanup, on a shared tree. **It was Tech's hand.**

**Cannot be determined.** The content: never committed, so no object exists, and the reflog does not record working-tree state — it is gone, not merely unfound. The author: three surfaces write this tree, attribution is prose not data, and an **uncommitted** change carries no author at all; `inbox/**` is Chief of Staff's triage lane, which is inference, not evidence. Whether it was the missing **§Action register**: `STATUS.md` §Pending promotion cites one in that file twice and `leads/systems.md` 1b records that it is not there — the only known dangling citation into this file, consistent with the loss, and consistency is not proof.

**What the handshake adds, so the next one is detectable:**

1. **Tech sweeps before any history operation**, not only at session open and close. The dangerous window was mid-session, which is the one window D5.39 does not cover.
2. **No `reset --hard`, `checkout -- .`, `clean` or `stash` while surfaces share a tree.** Drop a commit with `revert`, or reset `--soft`/`--mixed` — neither touches a file another surface may have written. Git execution is Tech's lane (D5.29); this needs no ruling, and Tech holds itself to it from now.
3. **Commit range at close** (§3) gives Chief of Staff's audit a start point. A file that changed between those hashes and appears in no swept list is then visible.
4. **Chief of Staff lists the paths it wrote** in §For Tech. A write that never reaches a commit is noticeable by its absence even when its content is unrecoverable — which is the only handle anyone has on this class of loss.

## 7. What Tech thinks is wrong — logged, not fixed (Q7 freeze in force)

1. **`cos.2` and `cos.3` are cited and do not exist.** `STATUS.md` §Pending promotion lists three Chief of Staff refs; the brief holds one. This is the `D5.24` shape — a ref treated as real that no file records — reappearing **inside the mechanism built to stop it, on the day it was built.** Tech promoted `cos.1` and invented nothing.
2. **Hop count.** D5.42 cl.3 promised three steps. Anything an agent records now runs owner → `Pending` → Tech promotes → Chief of Staff ratifies → board row. Chief of Staff's own open question 2 asks whether the queue survives the chain; this is that question with one more hop, asked before the first round under the new rule has finished.
3. **The check depends on the checked party.** Tech assigns, adjudicates and is the only surface that can run git. Ratification is the sole counterweight, and the ratifier cannot read history. That is honesty, not verification.
4. **Guard rails cover commits; nothing covers the working tree.** §6 is the demonstration.
5. **This proposal is written by the party that cannot make it true.** Every remaining piece is one heading in Chief of Staff's own brief and one line in its session-open routine. Tech has now proposed it twice.

## 8. For the owner

- **A:** adopt §1–§4; Chief of Staff adds `## For Tech` / `## From Tech` and the session-open line → log as one D-number.
- **B:** adopt §1–§4 **and** §6 #1–#4 as Tech's standing git practice.
- **C:** reject — the channel stays what it is, which is Tech writing into its own brief and waiting.

§5 needs no ruling: it is a description of what the existing decisions already do when the machine changes.
