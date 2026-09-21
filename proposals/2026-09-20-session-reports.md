# Proposal — execution agents file a session report; Tech reviews the report, not the output

**Produced by:** Tech (Claude Code), 2026-09-20 · **Targets:** `proposals/reports/` (new), `leads/README.md`, `leads/systems/tech.md`, `CLAUDE.md`, `tools/claude-agents/*.md` · **Proposes:** a fixed short report per prompted execution-agent session, read by two readers · **Status:** `PROPOSED` — rides with `2026-09-20-execution-agents.md` (**D5.41**). Owner ruled the principle; Tech proposes the mechanism only.

**Owner, in chat:** *"other cc leads should output reports as session artifacts upon prompting, these should be provided to tech and respective lead. that should be what tech is reviewing rather than larger output from other cc agents"*

---

## 1. What this fixes

Tech's custodial interest (`2026-09-20-execution-agents.md` §2) is real but it does not scale by reading everything. Tonight, one art agent produced two tools, five prompt passes, a 1.8 MB contact sheet and an 85-line board document. Multiply that by seven leads and "Tech notices what lands in the record" becomes either a full-time read or a lie.

A report inverts the cost: **the agent that did the work states what it did, and Tech reviews that statement.** Raw output stays where it belongs — with the lead who commissioned it.

It also closes a gap nothing else covers. The hooks catch malformed commits; the sweep catches unstaged work; neither can see *what an agent chose not to do*, what it deferred, or what it hit and worked around. Only the agent knows, and only if asked.

## 2. Two readers, one file

| Reader | Reads for | Acts on |
|---|---|---|
| **Tech** | custody: paths touched, commits made, anything written outside the agent's lane, any rule it had to bend, anything left uncommitted | records, flags to Chief of Staff, fixes mechanism |
| **The commissioning lead** | substance: what was produced, what it means, what it unblocks, what it recommends next | judges the work, decides what happens next |

Tech does not review the substance half. It is in the same file so there is one artefact per session, not two that drift.

## 3. Where it lives

`proposals/reports/YYYY-MM-DD-<agent>-<topic>.md`

- Inside `proposals/`, so it is **non-canon by definition** (rule 5) and already covered by the sweep table's Commit row — no change to `tools/sweep.py`, `.gitignore` or the hooks.
- One file per prompted session. Filed by the agent that did the work, in its own commit, under its own name.
- Never deleted, never edited by another agent. A correction is a new report that cites the old one.

## 4. The form (short on purpose)

```markdown
# Session report — <agent name> · <lead it serves> · YYYY-MM-DD

**Asked:** one line — what the owner or lead prompted.
**Commits:** <hashes + one-line subjects>. None → say "none, and why".

## For Tech (custody)
- Paths written: …
- Outside my lane: none | <path + why>
- Rules bent or hit: none | <which, what I did instead>
- Left uncommitted: none | <what, and why it is not finished>
- **Wrote outside the repo:** none | <what, where> — staged inputs, model folders, anything a reader of the commit cannot see

## For <lead> (substance)
- Produced: …
- What it means: 1–3 lines. The finding, not the log.
- Unblocks / blocks: …
- Recommend next: …

## Open — not decided by me
- <anything that needs the lead, Chief of Staff or the owner>
```

Rules for the writer: **no D-numbers** (AGENTS §1.4), no board rows (D5.38 — hand them over), no editing another lead's brief (D5.27). A report **states**; it never rules.

### 4b. Two things the first report taught, same evening

- **A row was missing.** The art agent staged two reference images into ComfyUI's `input/` folder — outside the repo, invisible to any reader of the commit, and a real side effect of `gen_styled.py`. It filed them under paths because the template had nowhere to put them. Row added above; it raised it rather than dropping it, which is the mechanism working.
- **Reviewing beat trusting, mildly.** Its counts were *"22 raw frames and four per-variant contact sheets"*; the record holds **20 frames and five sheets**. The claim that matters — everything raw ignored, nothing raw committed, all of it intentional — verifies exactly. Worth one line to establish that the custody half *is* checked against the record, not read.

## 5. What Tech does with it

1. Reads the custody half. Anything outside the agent's lane, any bent rule, anything uncommitted → `leads/systems/tech.md` §For Chief of Staff, one line each.
2. Checks the claimed commits exist and are attributed to the agent that wrote them. Tonight's three misattributions would have been caught here in seconds.
3. Transcribes any brief row the agent hands over, and nothing else.
4. **Does not** read the board document, the prompts, the images, or the tool diffs unless a custody line points at them.

A session with no report is the exception worth noticing: it means work exists in the record that nobody has accounted for.

## 6. Cost, honestly

- A short report per session, written by the agent that already has the context — cheap for it, and the only moment the information exists.
- It is a *claim*, not evidence. An agent can misreport. That is what the hooks and the sweep are for: they check the record itself, and they do not read reports.
- If reports become long, the mechanism has failed. The form above is a page; the detail belongs in the board document or the tool, cited by path.

## 7. For the owner and Chief of Staff

1. Adopt §3 and §4 — or rule the location and form differently and Tech will implement it.
2. **Trigger:** end of each prompted session, or on request? Tech's read: **end of session, always**, because the agent's context is gone afterwards and nobody can reconstruct it.
3. Does Chief of Staff want the report routed to it as well, or is the lead's copy enough? Its audit (D5.39) reads the log; reports would give it the layer the log cannot show.
4. The line for `CLAUDE.md` and each pointer in `tools/claude-agents/`, so a new execution agent knows on launch: *end your session by filing `proposals/reports/<date>-<you>-<topic>.md`.*
