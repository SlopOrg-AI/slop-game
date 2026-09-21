# Proposal — one permissions table, one home for owner feedback

**Produced by:** Chief of Staff (Cowork session `a5`), 2026-09-21 · **Targets:** `AGENTS.md` §§5–6, `leads/README.md` §Triage/§Single-writer, `inbox/README.md`, the brief template, `PROTOCOL.md` (in progress) · **Proposes:** replace nine scattered write rules with one table keyed by path; delete the Inbox table from every brief · **Status:** `PROPOSED` — owner rules.

**Owner, 2026-09-21:** *"propose org change to simplify next iteration of interactions. i think we need clear file read and write permissions and expectations, are /inbox being used appropriately or clearly instructed in agent briefs?"*

**Freeze note:** the framework freeze reserves reopening to the owner. This is the owner reopening it, and the proposal is **subtractive** — it adds no file and no mechanism.

---

## 1. The `inbox/` answer: used correctly, instructed incorrectly

| | |
|---|---|
| **Used correctly** | Five files, all of them the owner's words, one per sitting, none deleted. Two carry `TRIAGED` stamps. Nothing agent-to-agent has been filed there — which is right, and is the distinction the rationalization's channel ledger missed |
| **Instructed incorrectly** | The triage protocol's step 2 tells the triaging agent to *"append each C-ref to the target lead's Inbox table"*. **That is a write into another lead's brief, which D5.27 forbids and the owner tightened on 2026-09-21.** The instruction cannot be followed by an agent obeying canon |
| **Already failed in the field** | `inbox/2026-09-20-three-deck-draw.md` records a session refusing that append for exactly this reason. Its item, **`C23`, has been owed to Systems since yesterday and never arrived.** The protocol did not just contradict canon — it dropped a piece of owner feedback |
| **Routinely bypassed** | Four owner items today (`C29`–`C32`) went straight into a brief's Inbox table and were **never filed in `inbox/` at all**, though the README says chat feedback is written there first and then triaged. Chief of Staff broke that rule four times in two sessions, this one included |
| **Instructed in three places** | `inbox/README.md`, `leads/README.md` §Triage protocol, and the brief template. Two of the three disagree with canon |

**So the honest answer to the question: the folder is fine, the instructions around it are not, and no brief instructs a lead on it at all** — the briefs carry an Inbox *table* but no statement of where its rows come from or who writes them.

## 2. The general cause: rules keyed to roles, not to paths

Write permission is currently stated in **nine** places — `AGENTS.md` rule 5, `AGENTS.md` §6, `leads/README.md` §Roles, §Single-writer, §Triage, `inbox/README.md`, the sweep's path table, `D5.27`/`D5.29`/`D5.38`/`D5.42` cl.4, and each brief's own §Owns. Every one of them is phrased as *what a role may do*. An agent holding a file open has to reverse the mapping — *given this path, am I allowed?* — from nine sources, and tonight it got that wrong repeatedly:

| What happened tonight | Cost |
|---|---|
| Chief of Staff's brief overwritten **three times** from stale copies while its author was working in it | A ruling, a channel section and a commit request silently lost; each had to be written twice |
| Two handover documents written for the successor, invisible to the one surface that could record them | Tech told the incoming Chief of Staff that no handover existed |
| `C23` never delivered to Systems | Owner feedback dropped for a day, and still owed |
| Three commits misattributed | Permanent, and invisible to every automated check |
| A second Tech session rebuilt a channel that already existed | Hours, plus a folder that had to be retired |

Not one of these was a disagreement about *policy*. Every one was a surface that could not tell, at the moment it wrote, whether the file under its hand was its own.

## 3. Proposed — one table, keyed by path

The whole of write permission, in the order an agent actually needs it:

| Path | Who writes | Who reads | Notes |
|---|---|---|---|
| `leads/<own brief>.md` | **that lead only** | anyone | Two exceptions, both mechanical, both already ruled: the watcher removes a `## Commit me` block after committing it; Tech clears a `Pending` row it has promoted (D5.44 cl.4). Nothing else, for any reason |
| `leads/<another lead>.md` | **nobody** | anyone | Hand the line over in your own `## For <lead>` section. This is the rule that the triage protocol currently contradicts |
| `STATUS.md` | Chief of Staff authors · Tech types and commits | anyone | Unchanged (D5.38) |
| `design/decisions.md` | **Tech only** | matched, never read (D5.43 cl.6) | |
| `design/**`, `data/**` | the owning lead, on a logged decision | anyone | |
| `proposals/**` | **anyone, in a file of their own** | anyone | Never edit someone else's proposal — file a response beside it, as the art agent's correction did |
| `inbox/**` | the agent in session, filing the **owner's words verbatim** · triage adds a `TRIAGED` stamp and tags | anyone | Never agent-to-agent. Content is never edited after filing |
| `sessions/<own tag>.md` | the session holding that seat | anyone | Creating it is the claim; delete at close |
| `tools/**`, `.claude/**`, hooks, `PROTOCOL.md` | **Tech only** | anyone | Mechanism is Tech's (`cos.4`) |
| `AGENTS.md`, `leads/README.md`, `CLAUDE.md`, the Project mirror | **Chief of Staff**, on an owner instruction | everyone, first | Policy is Chief of Staff's and the owner's (`cos.4`) |

**Reading is unrestricted everywhere.** Saying so explicitly removes a question nobody has needed to ask but several agents have hesitated over — and it is why the table has a read column at all.

## 4. Proposed — delete the Inbox table from every brief

The table is the only reason the triage protocol needs a cross-write. Three ways out:

| | Option | Trade-off |
|---|---|---|
| **A** | **Triage hands over**: the C-ref goes in the triaging agent's `## For <lead>` section; the lead files its own Inbox row | Canon-safe, no deletions. But it is **two hops for every item**, and a hop is where `C23` died |
| **B** | **Delete the Inbox table from every brief.** The owner's words live in `inbox/` only, tagged in the file itself. A lead reads `inbox/` for its own tag at session open | **Recommended.** One home, zero cross-writes, zero second copies, and it deletes a section from eight briefs plus a step from the triage protocol. The contradiction disappears rather than being worked around |
| **C** | Keep the table, drop `inbox/` for chat feedback | Rejected: it makes the owner's words a copy in a brief with no original, and loses the one place the record is verbatim |

**Under B, the whole of triage becomes:** file the owner's words in `inbox/` → split into `C<n>` items → tag each `[sys] [tech] [art] …` → stamp `TRIAGED` with a one-line tag index at the top. Nobody writes to anybody else's file. A lead's session-open read is *"`inbox/` files carrying my tag since I last looked."* Five files exist; this is not a cost.

**What B loses:** a per-lead history of what the owner said to that lead. Mitigated — `inbox/` is that history, tagged and greppable, and the board keeps the C-ref index. The `Pending` and `Status` blocks in each brief are untouched.

## 5. Expectations — the behaviour half, five lines

1. **Claim your seat before you write.** `sessions/<tag>.md`. A claim already there naming another session means you are not that role; ask the owner.
2. **Read from disk in the same session, immediately before you write.** Never force. Never write back a copy you read more than a few minutes ago — that is precisely what overwrote this brief three times tonight.
3. **One writer at a time per file.** Not one writer per role — one *session*. Two Chief of Staff sessions ran tonight and neither claimed the seat.
4. **To get something recorded, declare it** in a `## Commit me` block in your own brief. Work on disk is not in the record.
5. **Report, never guess, when the author is unclear** — the unclaimed-path list (`cos.5`). A wrong name in the history is permanent.

## 6. What this deletes

| Deleted | From |
|---|---|
| Inbox table (8 of them) | every brief + the brief template |
| Triage step 2 (the cross-write) | `leads/README.md` §Triage protocol |
| The triage paragraph | `inbox/README.md` — replaced by one line: *owner's words, verbatim, tagged, never edited* |
| Nine scattered statements of who-may-write | `AGENTS.md` §§5–6, `leads/README.md` §Roles/§Single-writer, brief §Owns lines |

**Added:** one table, inside `PROTOCOL.md`, which Tech is writing now. **Net new files: zero.** C28 satisfied by a wide margin.

## 7. For the owner — three rulings

1. **Adopt the permissions table** as the single statement of who writes what, absorbing the nine scattered ones. *(Recommended.)*
2. **Inbox: A, B or C.** *(Recommended: B — delete the table from the briefs.)*
3. **Adopt the five expectations**, in particular *one writer at a time per file, claim the seat first*. *(Recommended.)*

And one that is not a ruling but a consequence: **`C23` is still owed to Systems.** Whatever is adopted, that item needs delivering.

## 8. Risks

- **A table keyed by path goes stale when paths move.** Mitigation: it lives in the one document Tech maintains, and renames are Tech's to make.
- **Deleting the brief Inbox tables costs a lead its at-a-glance view.** If a lead misses items after a week under B, the answer is a tag index at the top of each `inbox/` file — not the table back.
- **None of this prevents an overwrite.** It makes the rule legible; the register and read-before-write are what prevent it, and both already exist and were not used.
