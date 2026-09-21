# Proposal — context economics (what inter-agent communication costs, and what breaks first)

**Produced by:** Cowork session, 2026-09-20, owner-requested ("claudebot", outside-agent read) — no lead hat. **Targets:** `design/decisions.md` form, `proposals/` lifecycle, ref allocation, the Project mirror. **Proposes:** one measurement, four structural changes, no new rules. **Supersedes:** nothing. **Builds on:** `2026-09-20-agent-experience-review.md` (F2, F7) and its Chief of Staff response (X1, X2) — same diagnosis, measured. **Status:** `PROPOSED`.

Method: full tree read + counted. All figures below are measured off disk at `mtime` 2026-09-20 ~20:00, not estimated.

---

## 1. The measurements

| Quantity | Value |
|---|---|
| Markdown in `shinobi-v2/` | **50,712 words** (~79 KB of tokens), built in ~1 day |
| Of which the **owner's own words** (blockquoted verbatim) | **262 words — 0.52%** |
| Governance (`AGENTS` + `leads/` + `STATUS` + `inbox/` + 15 process proposals) | **25,240 w** |
| Design (`design/` + `data/README` + 6 content proposals) | **25,167 w** |
| Of which **game rules actually on disk** (`design/10–50`) | **3,769 w — 7.4% of the repo** |
| `proposals/` split | 13,567 w process-about-process · 13,143 w design/tooling |
| Owner input → agent output expansion, `inbox/` | **14.9×** |

**Mandatory read before any work happens** (per `AGENTS.md` §2 + `leads/README.md` §Running a lead session):

| Session | Cold-start tokens |
|---|---|
| Any task (`CLAUDE` → `AGENTS` → `00-steer`) | ~4,450 |
| Chief of Staff | ~8,700 |
| Tech | ~12,100 |
| Systems design | **~20,100** |
| Systems design + the two load-bearing proposals (F7) | **~29,400** |

`design/decisions.md` alone is ~7,900 tok, 38 rows, and its cost per row is **accelerating**: first ten rows averaged ~440 chars, last three were 1,400 / 1,400 / 2,100. Process rows (`Acts on it` = Production/Tech) average 936 chars against 588 for game rows — the repo spends more per decision on itself than on the game.

## 2. The structural cause — no materialized view

`decisions.md` is a **journal**: append-only, never delete, later wins. `design/` was meant to be the **projection** of that journal — the current rule, readable in one place. Six of twelve system docs are ~300 B stubs (F2), so the projection does not exist and every reader replays the journal instead.

The column split proves it: the **Decision** column is **61%** of the log's mass, because it is carrying rule text that belongs in `11-initiative.md`. Rationale is 27%; ID, `Acts on it`, Supersedes and Doc together are 12%.

Cost curves, and why this is the long-term item:

| Artefact | Read cost grows with | At 400 D-numbers (plausible by M1) |
|---|---|---|
| Journal (`decisions.md`) | **number of decisions ever made**, forever | ~80,000 tok — unskimmable; rule 2's arbiter stops being consultable |
| Projection (`design/` docs) | number of *systems*, ~12 | flat, ~8,000 tok, and only the doc you touch is read |

"Skim latest entries" (`AGENTS.md` §2) is already an admission that the journal does not scale. It is also unfalsifiable: an agent cannot know whether the row it needed was 30 entries back.

## 3. What is working — the high-density forms

Per token read, these carry the most decision-relevant information. They are all **fixed schemas**, where structure carries meaning and prose does not have to:

| Form | Where | Why it is dense |
|---|---|---|
| `Q<n>` four-line queue item | `STATUS.md` §Decisions | Decision-complete in ~40 words: question, options, trade-off, recommender, what it blocks. The single best artefact in the repo |
| `Acts on it` column | `decisions.md` | Turns an O(n) log into an O(n/5) one per role |
| **Does NOT own** / **Escalates to** | brief template | Negative space is what prevents an agent acting outside its lane; almost no repo writes it |
| "Known drift" + "migration is not a silent edit" | `data/README.md` | Pre-empts a whole class of helpful-agent damage in ~60 words |
| Verbatim owner quote + explicit `Not decided here` | `inbox/2026-09-20-three-deck-draw.md` | Provenance is inspectable; the agent's 1,200-word analysis cannot be mistaken for the owner's 50 words |

Textual duplication across governance docs is **near zero** (8-gram overlap between `AGENTS.md`, `leads/README.md`, `STATUS.md`, the briefs and `00-steer` is under 3% everywhere). The repo restates rules in different words rather than copy-pasting them — which is why rule changes (D5.27 → D5.29 → D5.38) require an edit in four places and leave residue (F1). **The redundancy here is semantic, not textual, so no diff tool will ever find it.**

## 4. Where it fails — measured, not asserted

| # | Failure | Evidence | Class |
|---|---|---|---|
| **E1** | **Ref allocation collides under concurrent surfaces.** `C23` was issued twice | `inbox/2026-09-20-three-deck-draw.md` takes C23; `inbox/2026-09-20-mac-migration.md` line 1: *"board says next free is C23; three-deck-draw took it — Chief of Staff to correct"*. `leads/systems.md` still advertises next-free C23, `STATUS.md` says C25 | Same bug D5.39 hook **B** catches for D-numbers. C-refs have no guard, and an advertised "next free" counter in three files is a shared mutable variable with no lock |
| **E2** | **Protocol debt accrues faster than sessions drain it.** 17 `Owed` · 12 `For Chief of Staff` · 22 `PENDING` · 2 `still unlogged`, in one day | `inbox/…three-deck-draw.md` §Owed could not append one table row because of single-writer; `STATUS.md` §Housekeeping is eight items | Single-writer (correct rule) converts every cross-lead fact into a message. A message costs one line to write and **a whole session to clear** |
| **E3** | **Half of what an agent reads is non-binding.** 58 `DECIDED` · 50 `PROPOSED` · 38 `OPEN` · 15 `STUB` | repo-wide grep | An agent evaluates provenance per line. This is the cost of the three-status rule and it is worth paying — but it means raw word count understates the read cost by roughly 2× |
| **E4** | **The most expensive surface is the blindest.** Project mirror is 3 files of ~40 | `leads/chief-of-staff.md` §Owns; `AGENTS.md` §4 | Chief of Staff authors `STATUS.md` from ~7 KB of a ~300 KB repo. It works today only because Cowork has disk access; on the Mac it will not |
| **E5** | **Register leak — the owner is billed for agent compression.** | `inbox/2026-09-20-user-facing-jargon.md`: *"M1, C23 are barely comprehensible to the user"* | C21/C22 already fix the rule. There is no check on the one output no file records: chat. The owner also wrote "C23" for C22 — the refs are not held in the owner's head, and never will be |

## 5. Proposals

No new process. Four changes, each of which **reduces** what is read.

| # | Do | Who | Effect |
|---|---|---|---|
| **P1** | **Split the arbiter.** `decisions.md` keeps ID · `Acts on it` · one-line decision · Supersedes · Doc. **Rationale moves to `decisions-rationale.md`**, keyed by D-number, read only when a decision is challenged. Rule 2 unchanged — the ledger is still the arbiter | Systems + Tech | −27% on the file every design session reads; removes the column that grows fastest |
| **P2** | **Make the Decision column a pointer, not the rule.** A D-number is not closed until its rule text lands in a `design/` doc line in the same session; the log row then shrinks to the claim. This is X2's stub-redirect run in the *other* direction — and it is the only thing that stops the journal absorbing the projection | Systems | −61% column over time; restores "read the one doc you're touching" |
| **P3** | **Archive on ruling.** A proposal whose content is logged as a D-number moves to `proposals/archive/` or is deleted — git history is the record (canon rule 1). `proposals/` is a queue, not a library | Tech, at commit | 21 files in one day; at this rate the folder out-masses `design/` within a week |
| **P4** | **Stop advertising next-free refs.** Delete the counters from `STATUS.md`, `leads/systems.md` and proposal headers; derive next-free by scanning the log (and an `inbox/` scan for C-refs), enforced by extending D5.39 hook **B** to C-refs | Tech | Closes E1 permanently; removes three stale-able fields |

**And one measurement, not a rule.** One line on `STATUS.md`, updated at session close:

```
Session N: design/ +<x> words · governance +<y> words · D-numbers logged <n> · docs distilled <m>
```

Today's line would read `design/ +0 · governance +~12,000 · D-numbers 12 · docs distilled 0`. The freeze already proposed (X1 / Q7) is the right call; this is what tells you whether it held, and what tells you when to lift it. **If governance exceeds design two sessions running, the framework is the product.**

## 6. Big picture

The communication protocol is not the problem — it is unusually good, and the fixed-schema forms in §3 are the reason a cold agent can be useful here in 20 KB. The problem is **mass**: 79 KB of tokens and 0.52% owner words in one day, against 3,769 words of game rules, with the arbiter growing super-linearly and the projection empty.

An outside read of the failure: this repo has built an excellent **compression protocol for a corpus that does not exist yet**. Every rule in it is a rule about how to handle design content — while 92.6% of what is on disk is the handling, not the content. That is survivable for one more session and fatal at 400 decisions, because the journal is the one artefact no rule ever shrinks.

Sequencing note against the Chief of Staff response: **P1–P4 belong inside the D5.39 → freeze window, not after it.** They are the last governance changes worth making, and each of them deletes something.
