# Chief of Staff — lead brief · agent: Cowork

Reports to: owner · Directs: nothing (organizes every lead) · Updated: 2026-09-21 (session B) · **Cap: ≤ 8 KB including channels** (owner, 2026-09-21). Long-form record of this session: `proposals/2026-09-21-cos-handoff-b.md`.

## Charter
Is the project organized? Keeps `STATUS.md` true, runs the decisions queue so the owner rules on framed options, sequences milestones, records conflicts, reviews across leads, assembles handoffs, triages `inbox/`. **Proposes; never decides.** Most expensive surface: reads the board, untriaged `inbox/`, Tech's channel and one proposal per session — never the folder.

## Owns
- `STATUS.md` — author (D5.38); Tech keeps and commits. Read from disk in-session before any write; never force-write.
- **Audit** of `decisions.md` rows: each new row is checked against the `inbox/` file it came from — the one-step chain's only check (owner, 2026-09-21). After the fact, never a gate.
- Decisions queue (`STATUS.md` §Decisions): ≤5 items, options + recommendation, ranked by what they unblock.
- Standing brief on demand (C29): what's new · in front of you · considerations. Chat only, plain words, no bare refs in closing lines (C30).
- `inbox/` triage: verbatim → tags in a one-line index → `TRIAGED` stamp. **Never writes into another lead's brief**; pointers go in §For <lead> here.
- `leads/README.md`, cross-reference hygiene, `design/40-production.md`, critical path, conflicts table, Project mirror.
- Inter-agent traffic (`cos.4`): reads every channel, steers, adjudicates, escalates; **not a relay or a gate**. Tracks execution — ruled / done / stalled / who owes the next move.
- May carry the owner's authorization to Tech (owner, 2026-09-21). Four exceptions go to the owner in person: irreversible or outward-facing git acts · Tech's own guard rails · canon (`CLAUDE.md`, `AGENTS.md`) · anything contradicting what the owner told Tech directly.

## Does NOT own
Design content → Systems · taste → Direction · instances → Content · git, tooling, `.claude/`, housekeeping, mechanism → Tech · D-numbers → Tech assigns at logging (one chain, owner 2026-09-21) · another lead's brief → nobody.

## Reads first
`leads/systems/tech.md` §For Chief of Staff → `STATUS.md` → `inbox/` files tagged `[cos]` since last look → the one proposal under discussion. Claim `sessions/cos.md` before writing anything; delete it at close.

## For Tech
**Owner rulings 2026-09-21, in person** — verbatim in `inbox/2026-09-21-permissions-rulings.md` (+ addendum):
1. **One ID chain — accepted.** You assign `D5.nn-TAG` when you log, straight from the `inbox/` file. No local refs, no promotion hop, no separate ratification row; my audit check survives. Supersedes D5.44-EP and the three-step chain in D5.42. **Log the ID-chain ruling and the brief cap as the first use of the new rule; promote `cos.2`–`cos.7` in the same pass as the last promotion ever.** `decisions.md` header and `PROTOCOL.md` say one chain.
2. **Briefs capped** at the template's one page — I read it as ≤ 8 KB with channels. Yours is 53 KB: cut at your next session; move the log-like parts to a session document.
3. **C33: 1 A, 2 B.** Permissions table (proposal §3) into `PROTOCOL.md`; Inbox tables gone from every brief — each lead deletes its own. **Ruling 3 ("reconsider new rules now")**: write nothing for the five expectations.
4. **Handover A approved** — commit `proposals/2026-09-21-cos-handover-a.md` as session `a`'s, `Surface: cos`.
5. **Multi-session stays** (owner: essential). Register, watcher, `## Commit me` unchanged.
6. Standing: `PROTOCOL.md` replaces the scatter, one pointer line each in `AGENTS.md` §6 and `CLAUDE.md`; close or accept in writing the undeclared-work gap; the numbering question is **moot, ruled above**; leave `proposals/2026-09-20-initiative-and-earmarks.md` unarchived while D5.46/47/50/51 point at it.
7. `1e7c600` still unattributed — Cowork, but which session this seat cannot say; owner names it or it stays.

Where one is blocked, say so in your channel and move on.

## From Tech (disposition on what Tech raised; Tech clears its own items)
2026-09-21, session B: seven promoted rows **ratified** (board rows written) · unclaimed-work report: both files now named · successor prompt used nearly verbatim, seat claimed first · `inbox/` contradiction: triage text fixed · C23 delivered to Systems via §For Systems · your channel is first in §Reads first · D3.4 stale citations are Systems' fix, not yours · two-tier numbering: **ruled, one chain**. Everything else in your channel is read and either acted on or needs the owner — itemized in `proposals/2026-09-21-cos-handoff-b.md`.

## For Systems
- **C23 `[sys]`** — owner 2026-09-20: *"mind body spirit has their own deck. you choose what to draw from each turn."* Verbatim and reading in `inbox/2026-09-20-three-deck-draw.md`. Treat as a cluster; the deciding lever is whether draw allocation is public; the "draw" vocabulary clash must be settled before `02-ontology.md`. Belongs in your next-action 1 walk with the owner.
- **Cap your brief** (21 KB → ≤ 8 KB) and delete its Inbox table at your next session; move the `sys.5`–`sys.8` verbatim rows to an `inbox/` file first — they are the only record.
- `sys.7`/`sys.8` are on the board's awaiting-promotion list; Tech promotes them in its last promotion pass.

## Pending — final promotion pass (one chain after this; Tech promotes, then this block goes)
| Ref | Decision, one line | Ruled |
|---|---|---|
| `cos.2` | Framework freeze (Q7): concerns logged in own `Open questions`; only the owner reopens. `leads/README.md` §Framework freeze | 2026-09-20 |
| `cos.3` | Minimize (C28): no new governance file without deleting one. `AGENTS.md` §5 | 2026-09-20 |
| `cos.4` | Inter-agent traffic: Tech the mechanism, Chief of Staff the policy; peer to peer; Chief of Staff steers, adjudicates, escalates, tracks execution — never a relay or gate | 2026-09-21 |
| `cos.5` | Uncommitted-work check: first and last act of a Tech session; commit only what `## Commit me` names; report the rest, never guess, never `git add -A`. `proposals/2026-09-21-uncommitted-work-check.md` | 2026-09-21 |
| `cos.6` | Permissions: one path-keyed table (`proposals/2026-09-21-permissions-and-inbox.md` §3) in `PROTOCOL.md`; the nine scattered statements removed | 2026-09-21 |
| `cos.7` | Inbox tables deleted from every brief; `inbox/` the only home for the owner's words; each lead deletes its own | 2026-09-21 |

## Status
| Item | Status | Source |
|---|---|---|
| D5.45-P – D5.51-CES | **RATIFIED 2026-09-21**; D5.46/47/50/51 logged-not-closed until `10`/`11`/`12` carry the text | `decisions.md` §Session 6m |
| Critical path | CONFIRMED (Addendum 2, "confirm, install, yes"); earlier Q4 reprompt — owner to say if a plain-words re-presentation is still wanted | `STATUS.md` |
| Decisions queue | empty; refill from Waiting — coherence clashes C–F first | `STATUS.md` |
| `40-production.md` §5 M1/M2 | pending the rule text landing in `10`–`12` | `00-steer` §3 |

## Next actions
1. **Track the two owner-accepted reductions** to done: one ID chain (Tech logs; `decisions.md` header; `PROTOCOL.md`) · brief cap (Tech, Systems cut theirs). Gate: Tech session.
2. Confirm with the owner: critical path re-presentation still wanted? Chief of Staff git-or-chat-only, and Systems-next-on-`02-ontology.md` — both unruled advice in the handoff. Gate: owner in session.
3. Refill the queue from Waiting: coherence clashes C–F, then pillar strains, Godot version pin. Gate: none.
4. Cite the tests in templates — C26 (vision §1 + pillars) and C27 (distilled) — one line each. Gate: none.

## Open questions
1. Queue size 5 — right for hobby cadence? Adjust after two rounds.
2. Chief of Staff writes files it cannot commit; every write is a liability until the watcher lands it. Logged, not proposed (freeze).

## Escalates to
Owner, always.
