# Proposal — who writes the board once there are two machines

**Produced by:** Tech (Claude Code), 2026-09-20 · **Targets:** D5.29 (amend), `leads/README.md` §Single-writer rules, `leads/chief-of-staff.md`, `leads/systems/tech.md` · **Proposes:** separate *authorship* of `STATUS.md` from *custody* of it · **Status:** **PROMOTED D5.38** (2026-09-20) — owner: "custody is with tech - agreed". §6 #1 applied.

---

## 1. The premise that changed

D5.27 and D5.29 were both decided while **one disk held everything** and two agent surfaces wrote the same working tree. "Chief of Staff is the sole writer of `STATUS.md`; Tech commits it, never writes it" was executable because Cowork could simply save the file and Claude Code would find it there — which is exactly what happened three times tonight.

After the move (`proposals/2026-09-20-two-machine-migration.md`): the owner prompts from a Mac, a **Claude Code Tech successor** holds the clone and git there, and the PC disk is unreachable. Whether Cowork can reach a clone at all is unknown and may change again. A custody rule that depends on an unknown is a rule that will be broken silently.

## 2. The distinction

Two things were bundled into the phrase "sole writer":

| | Question | Who | Why |
|---|---|---|---|
| **Authorship** | what the board *says* — blocked, next, conflicts, what the owner must decide | **Chief of Staff** | judgement; the organizing role's entire output. D5.29's reason for existing |
| **Custody** | who types the file and commits it | **Tech** | mechanical; Tech holds git on whichever machine is live |

One head decides, one hand types. Drift is then impossible regardless of who can reach what — which was the actual purpose of the single-writer rule, not the identity of the writer.

## 3. What this is *not*

Not a return to D5.27. Tech gains no judgement: it transcribes the rows Chief of Staff authors in `leads/chief-of-staff.md` (or in `inbox/`), without paraphrase that changes meaning, and it may not reorder the queue, restate a blocker or re-sequence the critical path. The conflict of interest D5.29 identified — the agent doing the work also grading it — is untouched, because grading stays with Chief of Staff.

If Tech disagrees with a row, the mechanism is the one already in `leads/systems/tech.md`: a "For Chief of Staff" note in Tech's own brief. Tonight used it once.

## 4. The three cases, and why the rule survives all of them

| Cowork's reach after the move | What happens | Rule needed |
|---|---|---|
| Read **and** write a clone | Chief of Staff drafts the board in its brief; Tech transcribes and pushes. Cowork never pushes | this proposal |
| Read only | Chief of Staff authors in chat or in its brief; Tech types it | this proposal |
| No repo access — chat only | Chief of Staff's output reaches disk through the owner or Tech; it owns no file | this proposal, plus a re-read of `leads/chief-of-staff.md` §Owns |

The same sentence covers all three, which is the argument for it: the project should not need a governance change each time a surface's access changes.

## 5. Cost

- One extra step when Chief of Staff and Tech are not the same session: the board lags the brief by one transcription. Tonight that lag was zero because both wrote one disk; it becomes real.
- Mitigation: Chief of Staff's row drafts live in its own brief, so the board is never the only copy — and an out-of-date board is visible (`Updated:` per row), whereas a silently forked one is not.

## 6. For Chief of Staff and the owner

1. Amend D5.29 with **D5.38**: authorship of `STATUS.md` → Chief of Staff; custody (writing and committing the file) → Tech. Single-writer principle unchanged.
2. Or reject, and instead state which surface will definitely hold write access to a clone after the move — the rule then follows from that fact.
3. Either way, `leads/README.md` §Single-writer rules needs the sentence it ends up with, because a successor on a new machine reads that file and nothing of this conversation.
