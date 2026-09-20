# Review response — `admin` lead absorbs Production

**Produced by:** Cowork (the agent that built `leads/`), 2026-09-20 · **Answers:** `2026-09-20-admin-lead-review.md` §5–§6 · **Status:** **PROMOTED D5.27** (2026-09-20) — owner confirmed §1–§3; §4–§5 applied. Not edited: `STATUS.md` (per §7 of the request).

## 0. Correction on the evidence
The two `STATUS.md` overwrites were mine: Cowork re-committed its own copy with a force flag over Claude Code's on-disk edits. Diagnosis in the request is correct; the cause is now named. Single-writer is the right fix.

## 1. Does absorbing Production strand Cowork? — Yes as phrased; fix the phrasing
- Change every brief header `Reports to: owner (via Production)` → **`Reports to: owner`**. Reporting was never through Production; Production kept the record. Admin keeps the record.
- Make it **two single-writer rules**, not one:
  - A lead's **own brief** (`leads/<lead>.md`) has one writer: that lead, on whichever surface is running it (Cowork, Claude Code, Codex).
  - **`STATUS.md`** has one writer: Admin (Claude Code). It transcribes each lead's row from that lead's brief.
- Consequence: a Cowork session acting as Systems updates `leads/systems.md` and stops. Nothing is stranded; nothing is transcribed twice.

## 2. Sequencing is judgement — bind it with a status tag, not adjectives
- The **Critical path** block in `STATUS.md` carries a tag: `PROPOSED (Admin, YYYY-MM-DD)` until the owner confirms, then `CONFIRMED (owner, YYYY-MM-DD)`. A change re-opens it as PROPOSED.
- Same for any reorder of a lead's "Next actions" that Admin makes on a lead's behalf — Admin doesn't; it asks the lead (or the owner) and transcribes.
- This reuses DECIDED/PROPOSED/OPEN semantics already in AGENTS §1.3. No new vocabulary.

## 3. Tech and Admin — two hats, keep both
- **Keep.** Admin = session open and close (board, triage, commit, mirror check). Tech = the work in between. Same agent; the separation is what gives *"never resolves a conflict Tech created"* any force.
- Count stays at eight (Admin replaces Production).
- Review trigger to merge: if Admin's open/close work is consistently under ~5 minutes a session, it is a checklist, not a role — fold it into Tech then.

## 4. Additions to the draft brief (`leads/admin.md`)
- **Owns →** "Stages explicitly by path; never `git add -A`." (Also belongs in Tech's pre-commit hook proposal — both, belt and braces.)
- **Does NOT own →** keep *"Never resolves a conflict Tech created"* verbatim; add *"Never edits another lead's brief; asks the lead or the owner and transcribes."*
- **Project mirror:** stays at `AGENTS.md`, `00-steer.md`, `01-pillars.md` (AGENTS §4). Cowork added a `STATUS.md` mirror to the Project today; Cowork is removing it — a second copy of a single-writer file is the drift being fixed.
- Routing tag `[prod]` → `[admin]`.

## 5. Reference inventory (§4 of the request) — confirmed complete, one addition
- Add `inbox/README.md` (mentions triage) to the list.
- Agree: `decisions.md` rows naming "Production" are history; do not rewrite.

## 6. For the owner
1. Confirm §1–§3 (Cowork's recommendation: all three as written).
2. D-number: log **one** entry for the leads structure *including* Admin and the two single-writer rules (precedent D5.1, D5.2 for process decisions). Suggested: D5.27, "Leads structure; Admin (Claude Code) sole writer of STATUS.md; each brief written only by its lead." Closes Production open #1.
3. Then Claude Code applies the file changes in §4 of the request, plus §4–§5 here, with the owner in session.
