# Proposal — cross-surface commit sweep: framework (Chief of Staff) + implementation ask (Tech)

**Produced by:** Chief of Staff (Cowork), 2026-09-20, owner-directed in chat: *"have tech propose schedule and implementation. have chief of staff establish framework for valid and applicable."* **Targets:** `leads/systems/tech.md` (Owns), `leads/README.md`, `tools/hooks/`. **Proposes:** a path-based sweep policy (§A) and the task Tech answers (§B). **Supersedes:** nothing; extends D5.29 git execution. **Status:** **PROMOTED D5.39** (2026-09-20) — owner ruled A: §A adopted as written, §B answered in the D5.39 row (session open + close; script over one path table; hooks first; stop on refusal). Expiry stated in the log.

**Problem:** Cowork can write this folder; only Claude Code has git (D5.29). Work written by any non-Tech surface sits untracked until a Tech session happens to notice it. It has been caught by hand twice (`git log`: *"Systems: C1-C20 coherence pass (Cowork session, not authored by Admin)"*, *"Systems: log D5.30-D5.37 (Cowork session, not authored by Tech)"*). Canon rule 1 says git history is the record of what changed when; today that is true only for what Tech happened to see.

---

## §A — Framework (Chief of Staff owns this table)

**Principle: the test is the path, never the content.** Tech does not read a file to decide whether it counts. D5.38 keeps Tech out of judgement on what another lead's work means; a sweep that asked Tech to rule on "valid" would put it straight back in. A sweep that cannot launder a rule violation is safe to run unattended. One that can, is not.

### A.1 Sweep table

| Path | Action | Why |
|---|---|---|
| `proposals/**` | **Commit** | Non-canon by definition (rule 5). Nothing here can be a decision, so nothing can be laundered |
| `inbox/**` | **Commit** | Evidence, not instructions (rule 7). Same reasoning |
| `STATUS.md` | **Commit** — as custody, not sweep | Already Tech's hand under D5.38; listed so the two mechanisms are not confused |
| `leads/<lead>.md` | **Commit only the brief of the lead that surface is** (Cowork → `chief-of-staff.md`). Any other brief → **flag** | Single-writer, D5.27. Tech committing an unexpected brief would ratify a write that broke the rule |
| `design/**`, `data/**`, `demo/**` | **Never sweep — flag** | These change only on an owner instruction in the session doing the edit (rule 5). An uncommitted change here is either already someone's job to commit, or a rule violation. Committing it makes the violation canon history, quietly |
| `tools/**`, `.gitignore`, `.gitattributes`, `.claude/**` | Tech's own; commits as its own work | Tech Owns them (`leads/systems/tech.md`) |
| anything gitignored | invisible — not a sweep failure | `.claude/agents/`, raw art PNGs (D5.28). Second argument for un-ignoring the agent pointers |

**"Valid and applicable" = appears in a Commit row of A.1, and nothing else.** No content test, no staleness test, no quality test. If a path is not in the table, it is a flag.

### A.2 Flags

A flag is never dropped and never silently committed. Destination: **`leads/systems/tech.md` §For Chief of Staff** — the channel that already exists for "Tech noticed, Chief of Staff decides." One line per flag: path · what changed · why it was refused. Chief of Staff reads and clears that section at session open (this also answers R6 of `…-agent-experience-review.md`).

### A.3 Attribution

Precedent is already set and becomes the required form: **`<surface>: <what> (not authored by Tech)`**. The log must never imply Tech wrote another surface's work.

### A.4 Shelf life — read before ruling

This rule assumes **one disk, two surfaces, one working tree**. If prompting moves to a Mac and the Tech successor holds the only clone, Cowork never writes a file into that tree, so there is nothing to sweep and this rule is inert — not wrong, just empty. D5.38 was written to survive that move; **this one is not.** Its replacement is a git remote plus Cowork committing its own work, or Cowork handing text to Tech in chat. `proposals/2026-09-20-two-machine-migration.md` §1 (no remote exists) is the blocker either way. Ruling this in is still worth it — it pays from tonight until the move — but it should be logged with its expiry stated, not discovered dead later.

### A.5 Not in scope

- The sweep does not commit `design/decisions.md`. A D-number is an owner act; it rides with the session that logged it.
- The sweep does not fix, tidy, rename or reformat anything it commits.
- An empty sweep is silent.

---

## §B — Ask to Tech (`[tech]`, Claude Code picks this up)

Chief of Staff does not specify mechanism. Tech proposes, against the A.1 table as given:

1. **Schedule.** "Periodically" has no trigger — nothing runs between sessions. Tech's read on: sweep at **session open** (catches other surfaces' leftovers), at **session close** (catches its own), or both. Say which, and what it costs in session time.
2. **Implementation.** Script or checklist; how A.1 is expressed so it is one place to edit; how flags are written to §For Chief of Staff; behaviour when the tree is clean.
3. **Order against guard rails.** `proposals/2026-09-20-guard-rails.md` §6 is still unruled. A swept commit should pass checks A–D. Tech's read on whether hooks must land first, and whether the two should be one owner ask.
4. **Failure mode.** What the sweep does when a hook rejects a swept commit mid-sweep — stop, skip, or report.
5. **Brief edit.** The line this adds to `leads/systems/tech.md` §Owns. Tech writes its own brief (D5.27); Chief of Staff does not.

---

## §C — For the owner

One ruling covers §A and §B. Suggested bundling: rule this together with `guard-rails` §6, since the sweep is only safe with those checks in place.

- **A:** adopt §A as written; Tech answers §B next session → log **D5.39**.
- **B:** adopt with changes to the A.1 table (say which rows).
- **C:** reject — keep it ad hoc, as it has been twice.
