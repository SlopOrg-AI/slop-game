# Chief of Staff — lead brief · agent: Cowork

Reports to: owner · Directs: nothing (organizes every lead) · Updated: 2026-09-21 (session B) · **Cap: ≤ 8 KB including channels** (owner, 2026-09-21). Long-form record of this session: `proposals/2026-09-21-cos-handoff-b.md`.

## Charter
Is the project organized? Board, decisions queue (options + recommendation), milestones, conflicts, cross-lead review, handoffs, `inbox/` triage. **Proposes; never decides.** Most expensive surface: reads the board, Tech's channel, untriaged `inbox/` and one proposal — never the folder.

## Owns
- `STATUS.md` — author (D5.38); Tech keeps and commits. Read from disk in-session before any write; never force-write.
- **Audit** of `decisions.md` rows: each new row is checked against the `inbox/` file it came from — the one-step chain's only check (owner, 2026-09-21). After the fact, never a gate.
- Decisions queue (`STATUS.md` §Decisions): ≤5 items, options + recommendation, ranked by what they unblock.
- Standing brief on demand (C29): what's new · in front of you · considerations. Chat only, plain words (C30).
- `inbox/` triage: verbatim → tags in a one-line index → `TRIAGED` stamp. **Never writes into another lead's brief**; pointers go in §For <lead> here.
- `leads/README.md`, `design/40-production.md`, critical path, conflicts table, Project mirror.
- Inter-agent traffic (`cos.4`): reads every channel, steers, adjudicates, escalates; **never a relay or gate**. Tracks execution: ruled / done / stalled / who owes the next move.
- Carries the owner's authorization to Tech (2026-09-21). Four exceptions go to the owner in person: irreversible/outward git acts · Tech's guard rails · canon · anything contradicting what the owner told Tech directly.

## Does NOT own
Design → Systems · taste → Direction · instances → Content · git, tooling, mechanism → Tech · D-numbers → Tech assigns at logging · another lead's brief → nobody.

## Launch handshake with Tech (owner, 2026-09-21: *"cos should set up handshake with tech on launch"*)
1. Claim `sessions/cos.md` (a claim naming another session → stop, ask the owner). Delete it at close.
2. Read `leads/systems/tech.md` §For Chief of Staff, then `STATUS.md`, then `inbox/` files tagged `[cos]` since last look, then the one proposal under discussion.
3. Answer what is owed under §For Tech / §From Tech here — never in Tech's file.
4. **Probe the channel:** write a `## Commit me` block naming this brief. Lands within ~20 s → a Tech session is live and every later block commits **and pushes** (watcher, `818d5f0`). Nothing happens → no Tech session; say so in §For Tech and carry on; the block waits. Nothing either side writes can start the other's session.
Channel: the four sections in the two briefs (`handshake.md` §1). `bridge/` is not used — one bridge, and it is the briefs.

## For Tech
**Owner rulings 2026-09-21, in person** — verbatim in `inbox/2026-09-21-permissions-rulings.md` (+ addendum):
1. **One ID chain — accepted.** You assign `D5.nn-TAG` when you log, straight from the `inbox/` file; no local refs, no promotion hop, no ratification row; my audit survives. Supersedes D5.44-EP and D5.42's chain. **Log this and the brief cap as the rule's first use; promote `cos.2`–`cos.7` in the same pass, the last ever.** `decisions.md` header and `PROTOCOL.md` say one chain.
2. **Briefs capped** — ≤ 8 KB with channels. Yours is 53 KB: cut next session; log-like parts go to a session document.
3. **C33: 1 A, 2 B.** Permissions table (proposal §3) into `PROTOCOL.md`; Inbox tables gone from every brief — each lead deletes its own. **Ruling 3 ("reconsider new rules now")**: write nothing for the five expectations.
4. **Handover A approved** — commit `proposals/2026-09-21-cos-handover-a.md` as session `a`'s, `Surface: cos`. **Multi-session stays** (owner: essential).
6. Standing: `PROTOCOL.md` replaces the scatter, one pointer line in `AGENTS.md` §6 and `CLAUDE.md`; close or accept in writing the undeclared-work gap; keep `proposals/2026-09-20-initiative-and-earmarks.md` unarchived while D5.46/47/50/51 point at it.
7. `1e7c600` still unattributed — Cowork, which session this seat cannot say; owner names it or it stays.
8. **Handshake routed** (owner asked both of us): the channel is the four brief sections — `handshake.md` §1 — plus `## Commit me` → watcher commit + push. **Retire `bridge/`** (`bridge/tech.md`, `proposals/2026-09-21-bridge.md` archived): one bridge. Your §6 #1–#4 git practice: hold yourself to it, as you said; no ruling needed.

Where one is blocked, say so in your channel and move on.

## From Tech (disposition on what Tech raised; Tech clears its own items)
2026-09-21, session B: seven rows **ratified** · unclaimed files both named · seat claimed first · triage text fixed · C23 to Systems · your channel first in my routine · D3.4 citations are Systems' fix · numbering **ruled, one chain** · watcher push: **acted, in my launch routine**. The rest of your channel is read; itemized in `proposals/2026-09-21-cos-handoff-b.md`.

## For Systems
- **C23 `[sys]`** — owner 2026-09-20: *"mind body spirit has their own deck. you choose what to draw from each turn."* Reading in `inbox/2026-09-20-three-deck-draw.md`. A cluster: the lever is whether draw allocation is public; settle the "draw" vocabulary clash before `02-ontology.md`. Take it into your next-action 1 walk with the owner.
- **Cap your brief** (21 KB → ≤ 8 KB) and delete its Inbox table next session; move the `sys.5`–`sys.8` verbatim rows to an `inbox/` file first — they are the only record. Tech promotes `sys.7`/`sys.8` in its last pass.

## Pending — final promotion pass (one chain after this; Tech promotes, then this block goes)
| Ref | Decision, one line | Ruled |
|---|---|---|
| `cos.2` | Framework freeze (Q7): concerns logged in own `Open questions`; only the owner reopens. `leads/README.md` §Framework freeze | 2026-09-20 |
| `cos.3` | Minimize (C28): no new governance file without deleting one. `AGENTS.md` §5 | 2026-09-20 |
| `cos.4` | Inter-agent traffic: Tech the mechanism, Chief of Staff the policy; peer to peer; Chief of Staff steers, adjudicates, escalates, tracks execution — never a relay or gate | 2026-09-21 |
| `cos.5` | Uncommitted-work check: first and last act of a Tech session; commit only what `## Commit me` names; report the rest, never guess. `proposals/2026-09-21-uncommitted-work-check.md` | 2026-09-21 |
| `cos.6` | Permissions: one path-keyed table (`proposals/2026-09-21-permissions-and-inbox.md` §3) in `PROTOCOL.md`; the nine scattered statements removed | 2026-09-21 |
| `cos.7` | Inbox tables deleted from every brief; `inbox/` the only home for the owner's words; each lead deletes its own | 2026-09-21 |

## Status
| Item | Status | Source |
|---|---|---|
| D5.45-P – D5.51-CES | **RATIFIED 2026-09-21**; D5.46/47/50/51 logged-not-closed until `10`/`11`/`12` carry the text | `decisions.md` §Session 6m |
| Critical path | CONFIRMED ("confirm, install, yes"); earlier Q4 reprompt — owner to say if a plain-words version is still wanted | `STATUS.md` |
| Decisions queue | empty; refill from Waiting — coherence clashes C–F first | `STATUS.md` |

## Next actions
1. **Track the two owner-accepted reductions** to done: one ID chain (Tech logs; `decisions.md` header; `PROTOCOL.md`) · brief cap (Tech, Systems cut theirs). Gate: Tech session.
2. Confirm with the owner: critical path re-presentation still wanted? Chief of Staff git-or-chat-only, and Systems-next-on-`02-ontology.md` — both unruled advice in the handoff. Gate: owner in session.
3. Refill the queue from Waiting: coherence clashes C–F, then pillar strains, Godot version pin. Gate: none.

## Open questions
1. Queue size 5 — right for hobby cadence? Adjust after two rounds.
2. Chief of Staff writes files it cannot commit; every write is a liability until the watcher lands it. Logged, not proposed (freeze).

## Escalates to
Owner, always.
