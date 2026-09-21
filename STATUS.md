# STATUS — one board

> **Read before the clean-slate migration runs:** `proposals/2026-09-21-clean-slate-implementation-review.md` — four implementation risks and one correction to the diagnosis in `clean-slate.md` §0.1. Pushed by the owner's console on his instruction, 2026-09-21. Delete this line and that file once the migration is done.

## Steward — state · asks

**state** · `steward-260921-a` live (`sessions/steward.md`). Full state: `status/steward.md`.

**asks** · `A260921.1 → builder` · **Run the §11 migration checklist in `proposals/2026-09-21-clean-slate.md`.** Read `proposals/2026-09-21-clean-slate-implementation-review.md` first — its §3 (make the worktrees by hand; the launcher comes *after* the hard stop, not inside the migration) and §4 (four revertible commits; delete nothing until the new world is proven) change how §11 should be run. Create the doorbell from a Claude Code cloud session — it has never run. · **blocks:** every Steward duty, the owner's queue, and the hard stop on `design/02-ontology.md`.

**note** · everything below this section is the pre-clean-slate board and has not been revised since D260921.1-P; §11 replaces it with a render of `status/<role>.md`, which is why the ask is mirrored here — until that render exists, `status/steward.md` has no reader. Two snags found while claiming the seat: `tools/session.py` rejects the tags `steward` and `builder`, so claims are written by hand; and `sessions/tech.md` is a ghost claim from the retired seat, which only the owner can clear.


**Authored by Chief of Staff** (`leads/chief-of-staff.md`, Cowork) — it decides what every row says. **Kept by Tech** (Claude Code): types and commits it, transcribing without paraphrase, never re-sequencing (D5.27 → D5.29 → **D5.38**). Leads write their row in their own brief first. **Typed by Chief of Staff wherever Cowork can reach the clone; Tech transcribes only where it cannot (D5.42 clause 4).** Tech still commits. This page answers only: **phase · blocked on · next · what the owner must decide**.

**Phase:** pre-production → Godot 1v1 duel demo (M1). No human has played a duel yet.
**No next-free number is advertised here (D5.42).** IDs carry a routing tag (D5.43-P): **S**ystems · **A**rt · **C**ontent · **E**ngine · **P**rocess. Tech assigns at the moment of logging; derive by scanning `decisions.md`. Recent: D5.38 board custody · D5.39 guard rails + sweep (done) · D5.40 private remote (done) · D5.41 context economics P1–P4 · **D5.42 numbering authority + hop count**. C-refs: C25 earmark mechanic · C26 vision-as-test · C27 "distilled" · C28 minimize · C29 standing brief. D5.24 still unlogged — folds into Q2's entry.
**Git:** `main` + private remote `chris-egan/slop-game`, **pushed and verified 2026-09-20** (D5.40). Tech (Claude Code) executes git, staging by path — never `git add -A`. **Three** surfaces write this repo: Claude Code (Tech) · Cowork (Chief of Staff) · the **art execution agent** under Art, which commits its own work.

## Decisions — for the owner

Answer in chat or here: `Q1: A` · `Q1: A, but …` · `Q1: reject` · `Q1: defer to <gate>`.

**Queue is empty.** Round 1 closed 2026-09-20 — all nine items ruled and actioned (`inbox/2026-09-20-queue-verdicts-1.md` §Action register, which supersedes that file's §Board rows). Chief of Staff refills from Waiting: **coherence clashes C–F first**.

**Waiting** (queued as slots free): coherence clashes C–F + four readings (`c-coherence` §2–§3) · pillar strains P2a, P3a (`vision-coherence` §3) · Godot version pin · which smoketest PNGs are keepers · agent-experience review R1–R8 (`proposals/2026-09-20-agent-experience-review.md` §4).
**Ruled** (2026-09-20, `inbox/2026-09-20-queue-verdicts-1.md`):
- **Q1 — A, with the owner's own mechanic** (**C25** `[sys]`): earmarks clear each round; arming earmarks that round; the earmark equals the ability's check number (D5.30). Systems logs, reconciles against D5.31 where they differ, writes into `10`/`12`.
- **Q2 — A**: nested bars (pair · team · fight), distance on the map (C13 + C20 promoted). Systems logs and resolves **D5.24** in the same entry → `11-initiative.md`.
- **Q3 — vision paragraph *and* pillars are together the test** for all work (**C26** `[sys] [cos]`), not pitch-only. Systems corrects `00-steer` §1 against the log; Chief of Staff cites both as the test in templates.
- **Q5 — hold.** Marketing stays dormant and off the queue.
- **Q6 — ruled by the addendum** (**C27**): *distilled* = written against `02-ontology.md` and `data/SCHEMA.md`, produced by synthesis across sources, carrying no STUB marker and no OPEN row at MVP scope. Cited by the `demo/README.md` gate and `40-production.md` open #3.
- **Q7 — A, as the owner reads it**: framework freeze means leads and agents *log* concerns; the owner decides whether to change. Chief of Staff adds it to `leads/README.md`.
- **D5.39 — guard rails, commit sweep, Chief of Staff audit**: ruled in chat and logged; the verdicts file predates it and lists it as unruled.
- **D5.40 — a private remote before the Mac move** (C24). Logged; **done** — remote added, pushed and verified, v1 rescued into `sources/v1/`.
- **Q4 — CONFIRMED (owner, 2026-09-20)**: the critical path below, as written (*"confirm, install, yes"*).
- **Q9 — B**: canon-clone rule only (a `Canon clone: <machine>` header field, set at the Mac move). No `FAILOVER.md`; failover ad hoc. Tech adds the field with C24 and archives `proposals/2026-09-20-continuity.md`.
- **Q8 — A, logged as D5.41**: context-economics P1–P4 + the session measurement line, inside the D5.39 window. Tech executes P3+P4 first, then P1 with Systems, then P2 as the standing rule for every new D-number. **The Q7 freeze is in force once this lands.**
- **D5.44-EP — agents number in their own namespace; Tech promotes.** A lead records a ruling the session it is given, in its own brief's `Pending` block, under `sys.12` / `art.3` / `cos.7`. Tech assigns the canonical `D5.nn-TAG` and keeps the local ref as a permanent alias — nothing is renumbered, and a doc may cite the local ref immediately. `Pending` is a queue; promoted entries leave it. Supersedes D5.43-P's interim numbering note.
- **D5.43-P — decision IDs carry an interested-party tag; one log, no lead copies.** Suffix letters **S** Systems · **A** Art/Direction · **C** Content · **E** Engine/tooling · **P** Process. Replaces the `Acts on it` column. A per-lead log is a tag match, never a second file. The number is identity, the tag is routing and is corrigible in place. `decisions.md` leaves the `AGENTS.md` §2 reading table — matched, never read. **All 42 rows retro-tagged and the column deleted, 2026-09-20.**
- **D5.42 — numbering authority to Tech; no addenda; three-step chain.** Tech assigns and adjudicates D-numbers at the moment of logging and reports to Chief of Staff to ratify; numbers are settled when logged and never renumbered; an `inbox/` file is a capture buffer that closes once logged, and no doc cites an addendum. Chain: owner rules → Tech logs with a number → Chief of Staff ratifies and writes the board row. Amends D5.38 (board custody conditional).
- **D5.45-P … D5.51-CES — RATIFIED (Chief of Staff, 2026-09-21)** against the verdict sources (`inbox/2026-09-20-queue-verdicts-1.md` Q1/Q2/Q3/Q6; owner verbatim in `proposals/2026-09-20-initiative-and-earmarks.md` §1; `cos.1` in the Chief of Staff brief). Each row states what the owner ruled. Read the rows in `decisions.md` §Session 6m; the board keeps no copy.
  - **D5.45-P** `cos.1` — Pending review at session open, refs only.
  - **D5.46-ES** `sys.1` — earmarks per-round, equal the check (Q1, C25).
  - **D5.47-AES** `sys.2` — nested bars pair·team·fight, distance on the map; absorbs `D5.24`, which gets no number (Q2). Propagation detail is Systems' rule text, owed to `11`.
  - **D5.48-ACPS** `sys.3` — vision paragraph and pillars together are the test (Q3, C26).
  - **D5.49-EPS** `sys.4` — *distilled* defined (Q6 + addendum, C27).
  - **D5.50-CES** `sys.5` — a multi-attribute ability earmarks every attribute it checks, in full.
  - **D5.51-CES** `sys.6` — attribute is capability, reserve is economy; supersedes D3.4. Systems' synthesis of the owner's "make the statement cohere"; percentages illustrative. Flagged for an owner glance, not held.
  - Four of the seven (D5.46/47/50/51) are **logged, not closed** — rule text still only in the proposal; `10`/`11`/`12` owed on an owner instruction. Do not archive the proposal.
- **One ID chain — RULED 2026-09-21** (owner: *"accept one id chain"*; `inbox/2026-09-21-permissions-rulings.md` addendum): Tech assigns `D5.nn-TAG` at logging from `inbox/`; no local refs, no promotion hop, no separate ratification; Chief of Staff audits rows after the fact. Supersedes D5.44-EP and D5.42's three-step chain. Tech logs it as the rule's first use.
- **Briefs capped — RULED 2026-09-21** (owner: *"cap the briefs"*): ≤ 8 KB including channels. Chief of Staff's done (26 → 8 KB); Tech (53 KB) and Systems (21 KB) cut theirs next session.
- **Serial sessions — REJECTED 2026-09-21** (owner: *"multi session is essential"*). Register, watcher, `## Commit me` stay.
- **C33 — RULED 2026-09-21** (`inbox/2026-09-21-permissions-rulings.md`): **1: A** — one path-keyed permissions table, into `PROTOCOL.md` (`cos.6`) · **2: B** — Inbox tables deleted from every brief, `inbox/` the only home for the owner's words, each lead deletes its own (`cos.7`) · **3: "reconsider new rules now"** — reading unconfirmed, nothing built. **Handover A approved** — Tech commits `proposals/2026-09-21-cos-handover-a.md` as session `a`'s.
- **C28 — standing rule: minimize.** Manage project bloat at all times; reduce governance overhead. Every lead, every proposal. No new governance file without deleting one. Chief of Staff writes one line into `AGENTS.md` §5 with the freeze; Tech transcribes.

## Pending promotion — **final pass** (one ID chain from 2026-09-21; this section goes once Tech has promoted the refs below)

**Refs only. To read one, open the brief** — the board keeps no second copy (D5.42-EP cl.2).

**Promoted 2026-09-21** (Tech, `decisions.md` §Session 6m) — **ratified 2026-09-21 (Chief of Staff)**; nothing outstanding from these
| Local ref | Canonical |
|---|---|
| `cos.1` | **D5.45-P** |
| `sys.1` … `sys.6` | **D5.46-ES · D5.47-AES · D5.48-ACPS · D5.49-EPS · D5.50-CES · D5.51-CES** |

`D5.47-AES` absorbs **`D5.24`**, which gets no number of its own; six files still assert `D5.24` as DECIDED and re-point when the rule text lands. `D5.51-CES` supersedes **D3.4**.

**Recorded, awaiting Tech's last promotion pass** — 9
| Ref | Brief |
|---|---|
| `cos.2` `cos.3` `cos.4` `cos.5` `cos.6` `cos.7` | `leads/chief-of-staff.md` — `cos.2`/`cos.3` rewritten 2026-09-21 after being lost, see below |
| `sys.7` `sys.8` | `leads/systems.md` |
| `tech.1` | `leads/systems/tech.md` |

**Ruled but holding no reference** — none.

## Working tree is not committed — read before writing anything here

**Partly stale — Tech reports (its channel, 2026-09-21) that commits resumed via the watcher (`f05f9a0`, first `## Commit me` landing).** Unverified from this seat: Chief of Staff cannot run git. What is in the record is what `git log` says, not this paragraph. Still unclaimed as of Tech's last report: `proposals/2026-09-21-cos-handover-a.md` (session `a`'s; only `a` or the owner can name it).

**Confirmed cause of the lost writes** (Tech, `proposals/2026-09-21-cos-tech-handshake.md` §5): a `git reset --hard HEAD~1` run to drop an empty test commit also discarded uncommitted work in the shared tree. It is not a mystery and it was not a second author. **Three CoS writes were destroyed this way** — `AGENTS.md` §5 (C28), `leads/README.md` §Framework freeze, and `leads/chief-of-staff.md` rows `cos.2`/`cos.3`, all rewritten 2026-09-21 — plus the `§Action register` in `inbox/2026-09-20-queue-verdicts-1.md`, not restored.

**Until a Tech session with a working shell commits:** no history operation on this tree — no `reset --hard`, `checkout -- .`, `clean` or `stash`. Guard rails cover commits; nothing covers the working tree.

**Two Claude Code sessions held the Tech seat simultaneously on 2026-09-21**, against `AGENTS.md` §6. They produced `proposals/2026-09-21-cos-tech-handshake.md` and `proposals/2026-09-21-bridge.md` + `bridge/tech.md`, agreeing on protocol and differing on where it lives. **Routed 2026-09-21 (Chief of Staff, owner instruction): the handshake lives in the two briefs; `bridge/` is retired.** Directed commits push to the remote via the watcher (Tech, `818d5f0`).

## Board

| Lead | Phase | Blocked on | Next action | Updated |
|---|---|---|---|---|
| Chief of Staff | D5.45–D5.51 ratified · C23 to Systems · C33 ruled (1 A, 2 B) · **one ID chain + brief cap ruled**; own brief capped at 8 KB | Tech: log the two rulings, last promotion pass, commit handover A · every lead: cap own brief, delete own Inbox table | re-present the critical path (Q4 reprompt still owed); route the two handshake proposals; refill queue from Waiting | 2026-09-21 |
| Systems | C1→D5.25, C3→D5.26; coherence pass done — 20 C-refs → 9 statements, 7 clashes + 4 readings open | — (Q1, Q2 ruled) | log Q1/Q2 D-numbers (D5.24 resolves in Q2's entry); write `11-initiative.md`; correct `00-steer` §1 (C26); cite C27 in the `demo` gate | 2026-09-20 |
| ↳ Content | v1-schema data on disk; no accepted board | schema v3 · accepted style card | hold; then Kaede/Genzo × 2 poses | 2026-09-20 |
| ↳ Tech | **owes: promote local refs (D5.44-EP); add its own `Pending` block; D5.33-EP tag looks wrong** — guard rails + sweep live and verified (D5.39); **remote pushed and verified** (D5.40); **v1 rescued** into `sources/v1/`; retired-role residue cleared; stub redirects + required-reading stamps landed (X2, X3); Godot gated | — | **take D-numbering from D5.43** (D5.42 cl.1) + fold cl.2 into `tech.md`/`inbox/README.md`, collapse hooks A/B; **D5.41 P3+P4**; Q9 canon-clone field; tag the critical path block CONFIRMED; Mac clone, then `validate.py` with schema v3 | 2026-09-20 |
| Direction / Art | table decided; 30/31 stubs | — | distill `31-ui.md` component list | 2026-09-20 |
| Direction / Level | spatial model PROPOSED | Q2 · §5 #2 | `arena-m1` cluster | 2026-09-20 |
| Direction / Scenario | nothing authored | — | playtest protocol | 2026-09-20 |
| Marketing | scope undefined | Q5 | define scope | 2026-09-20 |

Systems' input for the walk: `proposals/2026-09-20-c-coherence.md` (§2 clashes, §4 order).

## Critical path to M1 — **`CONFIRMED (owner, 2026-09-20)`**
Q1 + Q2 rulings → `02-ontology` + `SCHEMA.md` → distill 10→11→13→14→12→15 (+ D1–D4 compression) → schema v3 + validator → Godot headless engine → screens (needs `31` component list) → owner plays 10 duels (needs Scenario's `duels-m1`).
Parallel, not blocking: Art style card → Content cut-outs → M1 restyle.

## Conflicts (cross-lead)
| # | Between | Issue | Status |
|---|---|---|---|
| 1 | Systems ↔ 00-steer | D5.24 cited in `11`/`14`/`00` §6, not in `decisions.md` | OPEN — folds into Q2 |
| 2 | Systems ↔ data | "+ reaction" slot | RESOLVED — D5.25; dead fields go in schema-v3 migration |
| 3 | Tech ↔ Chief of Staff | art binaries in git | RESOLVED — D5.28; residue in Waiting |
| 4 | Cowork ↔ Claude Code | two writers of `STATUS.md` | RESOLVED — D5.27/D5.29/**D5.38**; Chief of Staff **authors** the board, Tech **keeps** it |

## For Systems
- **C23 delivered** — cards as three decks drawn by choice, owner verbatim in `inbox/2026-09-20-three-deck-draw.md`. Handed over in `leads/chief-of-staff.md` §For Systems (triage hands over; it never writes your brief). Systems files its own Inbox row. Owed since 2026-09-20.

### Two tag corrections (D5.43-P cl.4: corrigible in place, no renumber)
- **`D5.33-EP`** — escape as a fifth exit condition is a **game rule**, tagged from an `Acts on it` cell that read "Tech + Production". Almost certainly wants **S**.
- **`D5.2-PS`** — carries a Production clause and an Engine clause; the log's own header says a row carrying two is really two rows.

## Housekeeping (Tech owns; listed here until Tech's brief carries it)
- `decisions.md` `Acts on it` value "Production" names a retired lead — Systems' call (`Process`?); rows are history
- **`D5.24` cited as canon in six files** and absent from `decisions.md` — `00-steer` §6, `11-initiative.md` (status table asserts DECIDED), `14-scenes-conditions.md`, `STATUS.md`, `leads/systems.md`, `leads/direction/level.md`. Folds into Q2
- `design/40-production.md` §5 M1/M2 definitions — after Q1/Q2
- D1–D4 not compressed into `decisions.md` — **no longer a deadline**: the text is in the repo at `sources/v1/docs/combat-scene-decisions.md`. Compressing it is Systems' judgement; Tech executes
- Sweep table A.1 has **no row for a third writing surface**, and classifies `tools/**` as Tech's own work — wrong in both directions now that the art execution agent writes there. Chief of Staff owns the table
- `rules.json` `_note`s cite v1 open numbers; `insight.reveal_timing` references the removed Arm step
- Project mirror: level as of this write (Chief of Staff re-syncs)
