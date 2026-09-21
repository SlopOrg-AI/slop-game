**TRIAGED 2026-09-21** by Chief of Staff (session B). Tags: **C33** rulings `[cos] [tech] [sys]` · handover-A attribution `[tech]` · migrated items C29–C32 `[cos]`. Under ruling 2 (B) this file is the only home for these words; no brief carries a copy.

# Owner rulings — permissions and inbox (C33), handover A (2026-09-21, Cowork chat)

**Owner said (verbatim), answering the three rulings in `proposals/2026-09-21-permissions-and-inbox.md` §7 as framed in chat:**
> 1. A
> 2. b
> 3. reconsider new rules now.
>
> handover a decision approved

## Ruled

| Item | Verdict | Local ref | Owning lead → action |
|---|---|---|---|
| C33 ruling 1 | **A — adopt the path-keyed permissions table** (proposal §3) as the single statement of who writes what, absorbing the nine role-phrased statements | `cos.6` | Tech: table into `PROTOCOL.md`; the scattered statements come out in the same pass (Chief of Staff's approval conditions on `PROTOCOL.md` already require this). Chief of Staff: `leads/README.md` §Single-writer and §Roles lose their write-rule text once `PROTOCOL.md` carries it; `AGENTS.md` §§5–6 pointer line on the owner's instruction |
| C33 ruling 2 | **B — delete the Inbox table from every brief.** The owner's words live in `inbox/` only, tagged in the file; a lead reads `inbox/` for its tag at session open | `cos.7` | Every lead: delete its own Inbox table at its next session (single-writer — nobody deletes another lead's). Chief of Staff: template and triage protocol in `leads/README.md`, `inbox/README.md` triage line, own brief — done 2026-09-21 |
| C33 ruling 3 | **"reconsider new rules now"** — read by Chief of Staff as *not adopted as written; the five expectations are reconsidered under the freeze rather than added*. **Reading unconfirmed** — one-word confirmation asked | — | Chief of Staff: confirm reading; nothing written to `PROTOCOL.md` for the five expectations until it is |
| Handover A | **Approved** — `proposals/2026-09-21-cos-handover-a.md` is attributed to Chief of Staff session `a` and commits `Surface: cos` | — | Tech: commit it. Owner's word given in person, not a relay |

## Migrated from the Chief of Staff brief's Inbox table (deleted under ruling 2) — owner's words, verbatim, as originally recorded

| C-ref | Owner said | When | Where it went |
|---|---|---|---|
| — | "status.md is owned by chief of staff. housekeeping may make sense for tech" · "I think of you as chief of staff - organizing the project" | chat 2026-09-20 | D5.29 |
| — | "outline roles of named agents and propose means to adjudicate for me" → "implement" | chat 2026-09-20 | `leads/README.md` §Roles, §Adjudication |
| **C29** `[cos]` | "I want you to be my quick, what's new what's latest and priority considerations" | chat 2026-09-20 | brief §Standing brief; no D-number |
| **C30** `[cos]` | on a chat closing line: "this bit is not user friendly" | chat 2026-09-20 | brief §Standing brief, closing-line rule |
| **C31** `[cos]` | "correct" · "cos should [handle] interagent traffic, execution, adjudication and escalation" · "I don't want things running out of control" | chat 2026-09-21 | `cos.4` |
| **C32** `[cos]` | "consider if tech should browse the folder, or at least one location consistently to know what cowork agents are writing to disk and what to then commit" → "push to tech to implement" | chat 2026-09-21 | `cos.5`, `proposals/2026-09-21-uncommitted-work-check.md` |
| **C33** `[cos]` | "propose org change to simplify next iteration of interactions. i think we need clear file read and write permissions and expectations, are /inbox being used appropriately or clearly instructed in agent briefs?" | chat 2026-09-21 | `proposals/2026-09-21-permissions-and-inbox.md` → rulings above |
| **C23** `[sys]` | see `inbox/2026-09-20-three-deck-draw.md` | chat 2026-09-20 | delivered to Systems 2026-09-21 via `leads/chief-of-staff.md` §For Systems |

## Addendum — same sitting: the Chief of Staff was asked to step back

Chief of Staff was asked *"think if the end state of your proposals are fit for purpose, is this efficient and controlled?"* and recommended five reductions (serial sessions · one ID chain · Chief of Staff gets git or stops writing files · cap the briefs · Systems next, on `02-ontology.md`).

**Owner said (verbatim):**
> no, multi session is essential. accept one id chain. cap the briefs

| Item | Verdict | Owning lead → action |
|---|---|---|
| Serial sessions | **Rejected — multi-session is essential.** `sessions/` register, watcher and `## Commit me` stay | — |
| **One ID chain** | **Accepted.** Tech assigns the canonical `D5.nn-TAG` when it logs a ruling, straight from the `inbox/` file; no local refs, no promotion hop, no separate ratification step. Chief of Staff's check that a row says what the owner ruled survives as the audit. Supersedes D5.44-EP and D5.42's three-step chain; C-refs stop being issued — an `inbox/` path + date is the reference | Tech: log this and the brief cap **as its own first use** (canonical numbers, no `cos.n`); promote `cos.2`–`cos.7` in the same pass as the last promotion ever; `PROTOCOL.md` and `decisions.md` header say one chain. Chief of Staff: `leads/README.md` §Local refs and the template — done 2026-09-21 |
| **Cap the briefs** | **Accepted.** The template's "≤ 1 page" is enforced. Chief of Staff reads it as **≤ 8 KB including `## For` / `## From` channels**; overflow is cut or moved to a session document in `proposals/`. Each lead cuts its own at its next session | Chief of Staff: own brief 26 KB → under the cap, 2026-09-21. Tech (53 KB) and Systems (21 KB): next session |
| Chief of Staff git-or-chat-only · Systems next on `02-ontology.md` | **Not ruled** | stays as advice in the handoff |

## Addendum 2 — same sitting: handshake and pushing commits

**Owner said (verbatim):**
> cos should be able to communicate with tech lead to push commits. how can we enable that. i have asked tech lead for same solution. refer to handshake if possible

(To Tech, same sitting, per `leads/systems/tech.md` §For Chief of Staff: *"cos should set up handshake with tech on launch. tech should ensure cos can direct tech to push commits."*)

| Item | Disposition | Owning lead |
|---|---|---|
| Directing commits + push | **Already enabled**: a `## Commit me` block in the lead's own brief → watcher commits those paths under that lead's tag and **pushes** (Tech, verified `818d5f0`). Works only while a Tech session is live; otherwise the block waits | Tech — done |
| Handshake on launch | Chief of Staff's four-step launch routine written into `leads/chief-of-staff.md` §Launch handshake (claim seat · read Tech's channel · answer in own brief · probe with a `## Commit me` block) | Chief of Staff — done 2026-09-21 |
| Which bridge | **The briefs** (`proposals/2026-09-21-cos-tech-handshake.md` §1: four sections in two briefs). `bridge/` retired — one bridge (routing is Chief of Staff's; both Tech proposals said so) | Tech retires `bridge/tech.md`; archive `proposals/2026-09-21-bridge.md` |
| Handshake proposal §8 | Effectively **A** in practice (four sections exist, session-open routine exists); Tech's §6 git practice is Tech's own lane. Owner may log one D-number or leave it as practice | owner |
