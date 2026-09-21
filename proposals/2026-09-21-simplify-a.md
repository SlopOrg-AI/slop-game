# Proposal — simplify agent files, briefs and protocols (option A: collapse to four reads)

**Produced by:** Chief of Staff, Cowork session B, 2026-09-21 · **Owner:** *"can we simplify agent files, briefs and protocols? next time user access will be spinning up fresh sessions"* → *"consider plan for A and ask tech lead for advice"* · **Status:** `PROPOSED` — plan only; nothing here lands until the owner rules and Tech has advised (§5). **Freeze note:** the owner reopened this; the plan is subtractive and adds no file that does not delete more.

## 1. The test

A fresh session of any lead starts from **one prompt and four reads** and nothing else:

> Act as `<lead>`. Claim your seat (`sessions/<tag>.md`). Read `PROTOCOL.md`, `leads/<lead>.md`, `STATUS.md`. Nothing else unless a question turns on it. At close: update your brief, release the seat.

If a rule is not reachable from those four, it does not bind.

## 2. File by file — what happens to each

| File | Today | Fate | Whose hand |
|---|---|---|---|
| `PROTOCOL.md` | being written by Tech (mechanism) | **the one how-we-work file.** Sections: roles + who-answers-to-whom · permissions table (path-keyed, C33 ruling 1) · session register · handshake + `## Commit me` + push (ruled) · one ID chain · `inbox/` (verbatim, tagged, only home) · freeze + minimize · registers (agent-facing / user-facing) · brief template (≤ 8 KB, six sections) · Tech's git practice (handshake §6). Policy text supplied by Chief of Staff in §For Tech; Tech assembles and owns the file | Tech (file), Chief of Staff (policy text) |
| `AGENTS.md` | 9 KB; §§1–7 + mirror + registers | **cut to ≤ 3 KB:** what the game is (pointer to `00-steer`, `01-pillars`) · the seven rules · one line → `PROTOCOL.md` · the reading table for `decisions.md` tags. §§4–6 text moves to `PROTOCOL.md` | Chief of Staff, owner instruction (canon) |
| `CLAUDE.md` (root, v1 pointer) and `shinobi-v2/CLAUDE.md` if any | tells every Claude Code session it is Tech | **one line:** *"Claude Code sessions: the owner names your lead at start; read `PROTOCOL.md`."* Fixes the art-agent falsehood Tech flagged | Tech, owner instruction (canon) |
| `leads/README.md` | 10 KB: tree, roles, tags, ID chain, triage, adjudication, freeze, single-writer, cost tiers, registers, template | **reduced to the tree + one pointer.** Everything else is `PROTOCOL.md` content | Chief of Staff |
| `sessions/README.md`, `inbox/README.md`, `tools/hooks/README.md`, `proposals/reports/README.md` + `_TEMPLATE.md` | four rule files | **absorbed** into `PROTOCOL.md` sections; each folder keeps a **one-line** README pointing there, or none | Tech |
| `bridge/` | duplicate channel | **deleted** (ruled) | Tech |
| `.claude/agents/*.md`, `tools/claude-agents/*` | per-lead pointers | keep as **one line each**: the prompt in §1 with the lead filled in. If Tech says they are redundant with `CLAUDE.md`, delete | Tech |
| `STATUS.md` | 16 KB; board + working-tree essay + housekeeping + for-Systems | **≤ 6 KB:** header (phase, git, surfaces) · queue (≤5) · Ruled since last brief · board · critical path · conflicts. Housekeeping → Tech's brief; per-lead notes → §For <lead> in the Chief of Staff brief; the working-tree section → one line | Chief of Staff |
| Lead briefs (9) | 2–53 KB, varying shapes | **≤ 8 KB each, six sections in this order:** Charter · Owns / Does not · For <lead> / From <lead> channels · Status · Next actions (≤ 5, gated) · Open questions. Pending and Inbox tables gone (ruled). Each lead cuts its own at its next session; cut text goes to a session document | each lead |
| `proposals/` (≈ 40) | ruled and unruled mixed | **archive on ruling (P3, already ruled, never run):** every governance proposal whose rulings are logged moves to `proposals/archive/` (a folder, not a rule file; or a `ARCHIVED` line at the top if Tech prefers no move). **Stays live:** anything an open decision still points at — at least `initiative-and-earmarks` (D5.46/47/50/51), `c-coherence` and `vision-coherence` (Waiting queue), `ontology-draft`, design/world content. Tech lists the references before moving anything | Tech (mechanical), Chief of Staff (the keep list) |
| `decisions.md` header | numbering rules, tags, D1–D4 note | tag table stays (it is the reading key); the numbering paragraph becomes one line → `PROTOCOL.md` | Tech |

**Net:** rule files a fresh session must find: **11 → 1** (+ its brief + the board). Files deleted or reduced to a pointer: ~8. New files: `PROTOCOL.md` (already approved) and possibly `proposals/archive/` as a folder.

## 3. Order — two sessions, then stop

1. **Tech session (now live):** finish `PROTOCOL.md` with the section list in §2, using the policy text Chief of Staff hands over; retire `bridge/`, the sweep, and the four folder READMEs; write the pointer lines; produce the proposal reference list for the archive; cap its own brief. Report in §For Chief of Staff what could not be absorbed and why.
2. **Chief of Staff session (next):** audit `PROTOCOL.md` against the rulings; cut `AGENTS.md` and `leads/README.md` on the owner's instruction; rewrite `STATUS.md` to the short form; confirm the archive keep-list; re-sync the Project mirror.
3. **Hard stop.** The session after that is Systems with the owner on `02-ontology.md`; no process work until a paper duel has been played. Measured, not hoped: the D5.41 measurement line is computed at the end of step 2 and put on the board.

## 4. What this does not do

Does not change any rule already ruled (freeze, minimize, one chain, cap, permissions, inbox-only, handshake, multi-session). Does not touch `design/`, `data/`, `demo/`, `tools/` code. Does not merge leads or retire roles. Does not write `PROTOCOL.md` from the Chief of Staff side — mechanism is Tech's; policy text is handed over.

## 5. Questions to Tech — advice wanted before anything lands (owner: *"ask tech lead for advice"*)

1. What does `PROTOCOL.md` already contain, and which §2 sections would you rather not carry (too policy-shaped for a file you maintain)? Say where they should live instead — the answer must still be one of the four reads.
2. Do the guard-rail hooks or the watcher read `AGENTS.md`, `leads/README.md` or any README by path or content? If so, which lines must survive where they are.
3. Archive: move to `proposals/archive/` vs. an `ARCHIVED` header line — which keeps links valid and hooks quiet? And can you produce the list of proposals still referenced from `decisions.md`, `STATUS.md`, `design/` and the briefs, so the keep-list is checked, not guessed?
4. `.claude/agents/*.md` and `tools/claude-agents/`: needed, or redundant once `CLAUDE.md` carries the one-line prompt?
5. Sequencing: can step 1 fold into your current `PROTOCOL.md` pass without a second session, and what would you cut from §2 to make it fit?
6. Anything in §2 that is wrong about your files — say so; this plan was written without a shell.

## 6. For the owner

- **A1:** approve the plan as written; Tech advises in its channel, Chief of Staff adjusts, both sessions run, hard stop after.
- **A2:** approve the file fates in §2 but let Tech run both steps alone (it has the shell); Chief of Staff audits after. Cheaper by one Cowork session; the canon edits (`AGENTS.md`, `CLAUDE.md`) then need your word to Tech in person.
- **Reject:** fall back to B (cap and archive only).
