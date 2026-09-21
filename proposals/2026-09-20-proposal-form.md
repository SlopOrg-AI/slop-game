# Proposal — a form for proposals

**Produced by:** Chief of Staff (Cowork), 2026-09-20, owner-directed in chat. **Targets:** `proposals/_TEMPLATE.md` (new), `proposals/README.md`, `tools/hooks/pre-commit`. **Proposes:** promote the existing four-field header into a template file, add three fields it lacks, and make it checkable. **Supersedes:** `proposals/README.md` header sentence. **Status:** `PROPOSED` — nothing installed, template body inline in §3. **D-number if ruled:** rides with D5.39 or takes the next free.

*This file is written in the form it proposes.*

---

## 1. Evidence

Fifteen proposals on disk, scored against the header `proposals/README.md` already specifies:

| Field | Conformance | What depends on it |
|---|---|---|
| Who produced it | **14/15** | attribution only |
| Status line | **13/15** | — |
| **Targets** | **7/15** | Chief of Staff routes by it; Tech edits the named doc after promotion |
| **Proposes** | **6/15** | reduction to queue form (`leads/README.md` §Adjudication) |
| **Supersedes** | **4/15** | canon rule 2 — what this would make wrong |
| Promotion stamp | 4/15 | — but see §2.2 |

The fields describing the **author** are filled. The fields another agent needs to **act** on the file are not. Supersedes at 27% is not a field; it is a suggestion.

## 2. Diagnosis — two distinct failures

**2.1 Prose convention vs. template file.** `design/` has `_TEMPLATE.md`, named by `AGENTS.md` §3. `leads/` has a template block in `leads/README.md` §Brief template. `proposals/` has a sentence in a README. An agent that lists `proposals/` sees fifteen files of varying shape and imitates the nearest one; an agent that lists `design/` sees a file called `_TEMPLATE.md` and copies it. The convention is not weaker — it is less discoverable at the moment of writing.

**2.2 The stamp has no state for what actually happens.** `README.md` offers `PROMOTED D#.#` or `REJECTED`. Real outcomes are partial: `c-coherence` (C1 → D5.25, C3 → D5.26, remainder open) and `session-6-handoff` (D5.30–D5.37 from part of it) are both partly promoted and therefore stamped as neither. The 4/15 figure is mostly this, not neglect. A vocabulary gap reads as discipline failure and gets "fixed" by nagging, which will not work.

## 3. `proposals/_TEMPLATE.md` — body to install verbatim

```
# Proposal — <one-line title>

**Produced by:** <surface> (<lead hat, or "no lead hat">), YYYY-MM-DD, <owner-directed | own initiative | task from …>. **Targets:** <files this would change, or "nothing on disk yet">. **Proposes:** <one sentence>. **Supersedes:** <named doc/section/D-number, or the literal word `nothing`>. **Status:** `PROPOSED`. **D-number if ruled:** <next free, or "none — tooling, not design">.

---

## 1. <Problem / evidence>
What is wrong, with evidence from disk or this session. Not theory.

## 2…n. <Argument, options, detail>
Tables over prose. Cite paths; never restate what is on disk.

## Last section — For the owner
A: <option> — <one-line consequence>     ← recommended by <lead>
B: <option> — <one-line consequence>
C: reject — <what stays as it is>
```

### 3.1 Three changes to the current header

| Field | Change | Why |
|---|---|---|
| **Supersedes** | mandatory; the literal word `nothing` when nothing | A blank is ambiguous — considered and empty, or skipped? `nothing` is an assertion. `guard-rails` already does this |
| **Status** | add `PARTLY PROMOTED — <ref> → D#.#; remainder OPEN (date)` | §2.2. Without it, the two largest proposals in the repo are unstampable |
| **For the owner** (closing section) | new, required when the proposal asks for a ruling | Strongest pattern in the good files (`guard-rails` §6, `board-custody`, `commit-sweep` §C). It is what lets Chief of Staff reduce a proposal to queue form without re-reading it. Currently nowhere in the README |

**`D-number if ruled`** is also new and is the cheapest of the lot: it forces the author to check the log's max before writing, which is one half of the collision logged in `guard-rails` §1 #1.

## 4. `proposals/README.md` amendments

1. Replace the header sentence with: *"Copy `_TEMPLATE.md`."*
2. Promotion: add the partial state and state where the stamp goes (top of file, replacing the `Status` value — not a new line).
3. New rule, from `…-agent-experience-review.md` F7: **a proposal named in any lead's "Reads first" is a distillation debt.** `proposals/` is non-canon by definition; a non-canon file every session must read is a second canon exempt from rule 2. When it happens, Chief of Staff puts the distillation in `Waiting`. Currently true of `session-6-handoff` (26 KB) and `ontology-draft` in both `leads/systems.md` and `leads/systems/tech.md`.

## 5. Enforcement — `[tech]`

A template that is not checked decays the same way: `design/_TEMPLATE.md` is mandated by `AGENTS.md` §3 and six of twelve `design/` docs are stubs. The check is ~10 lines and belongs with `guard-rails` checks A–D, not as its own mechanism:

> **Check E — proposal header.** An added file under `proposals/` matching `????-??-??-*.md` must carry `Produced by:`, `Targets:`, `Proposes:`, `Supersedes:` and `Status:` in its first eight lines. Fail names the missing fields. Art directories and `_TEMPLATE.md` exempt.

Deliberately weak: presence, not quality. It cannot tell whether `Supersedes: nothing` is true — it only makes the author type it.

## 6. Not proposed

- No length cap. Proposals run 3.6–26 KB and a genuine handoff needs the room; §4.3 handles the real cost of long ones.
- No retro-fit of the fifteen existing files. Stamps go on as each is ruled; the rest are history and rule 7 covers them.
- No new folder, index, or status page. The board already answers "what is live."

## 7. For the owner

A: adopt — install `_TEMPLATE.md` §3, amend the README §4, check E rides with the guard-rails hooks — *← Chief of Staff*
B: adopt the template and README only; no check — accepts the `design/_TEMPLATE.md` decay pattern knowingly
C: reject — the README sentence stands; conformance stays at 6/15 on `Proposes`
