# 00 — Project Steer (READ FIRST)

**Shinobi Master** · solo dev · PC/Steam · Godot 4.7 / GDScript (when active) · hobby cadence
**Updated 2026-09-20 (session 4).** This is the read-first doc for any new chat or agent. It says *where we are, what matters next, and what is deliberately out of scope*. Design detail lives in `01-design-bible.md`; decision history in `combat-scene-decisions.md`.

---

## 1. One-paragraph vision

Turn-based card battler with a persistent campaign and world state. Create a shinobi, learn techniques, build bonds and rivalries, and rise to lead a village. Combat is a duel of **planning and reading**: queue actions, arm hidden reactions, and fight over a persistent **initiative** tug-of-war — the fighter who *understands* the opponent turns the tables. Decisions carry the weight; variance is bounded and opt-in, there to tip thresholds, not decide fights. Combat is staged as flattened, stylized characters posed within a live 3D scene. Above the duel, a sandbox campaign tracks political and personal ties over time, and an overworld carries you between them.

*(External comps for each element — Naruto, NITRO GEN OMEGA, Paper Mario, Crusader Kings 3, Mount & Blade — live in `01-design-bible.md` → Reference touchstones, kept there as decision anchors rather than pitch copy.)*

## 2. Where we are

**Phase: design + art direction, no engine work.** The Godot port (started and abandoned same day, 2026-09-20 — see `combat-scene-decisions.md` D4.1) is archived: `Godot/shinobi-master/` kept as reference only, not resumed. A future Godot attempt starts clean once combat is human-playtested and art direction is settled.

**Current track (owner-led):**
1. **Human playtest** of `combat-1v1-v4.html` — no AI-vs-AI simulation driving tuning for now (D4.2). Owner flags when simulation is useful again.
2. **Art direction via image generation** — character/pose art first (cutaway-shot style, comps: Paper Mario, NITRO GEN OMEGA), then UI skin. Owner generates, Claude reacts/iterates on prompts (D4.4). No image-gen tool connected in this session yet.

**What triggered the reset (2026-09-20):** one day into the Godot port, the engine (Phase 1, golden-tested) was solid, but Phase 2 UI was already being rebuilt a second time (3D stage, cinematic Director, multi-actor roster façade) before anyone had played a single human duel — and a chunk of that later work (`05-combat-presentation-plan.md`, `06-multi-actor-combat.md`) existed only on disk, never synced to this Project, citing source docs that no longer exist anywhere reachable. The problem was never the *content* of that work — the multi-actor combat direction it contains is confirmed real (D4.5) — the problem was that it landed unsynced and unreviewed, mid an unpaused multi-phase engine push. Full account: `combat-scene-decisions.md` D4.1–D4.5. **Lesson for any future agent: check this Project against `C:\Claude\docs\` before treating either as current — they diverged once already.**

Design discovery (ChatGPT status doc, this project's decisions log, a headless Python sim) is merged into `01-design-bible.md`, the single design source of truth. The core combat loop (Declare→Arm→Resolve, tag-stack damage, anatomical wounds, initiative bar) is settled across three design sessions. What's genuinely open: the variance mechanism (bible §1a), reaction slots (§7 open decisions), and — the big one — **it has never been played by a human.**

## 3. What's on disk (C:\Claude)

| Path | What | Status |
|---|---|---|
| `docs/` | Mirror of the project docs. | Active — project copy is canonical; sync when either changes. **Verify this before trusting it — see §2.** |
| `design-data/` | `MOVED.md` pointer only. | Retired — contents moved into the (now archived) Godot repo. |
| `wireframes/` | **`combat-1v1-v4.html` = playable prototype** (JS engine: Declare → Arm → Resolve, AI, wounds, reactions, insight interrupts, trick-taking order). This is the human-playtest target now. `build.py` inlines JSON data into every `*.template.html`. | **Active.** This is where playtesting happens. |
| `shinobi-prototype/` | Python duel sim + old-schema JSON | Archived (`ARCHIVED.md` inside). |
| `Godot/shinobi-master/` | Godot 4.7 project. Engine ported (golden test passed), two UI attempts, one multi-actor scope expansion — all same day, none human-played. | **Archived 2026-09-20** (`ARCHIVED.md` inside). Reference only — see D4.1. Not resumed as-is. |

**Data flow while archived:** `wireframes/build.py` reads the game-data JSON that used to live at `design-data/` (now inside the archived Godot repo at `Godot/shinobi-master/data/`) and inlines it into the HTML. If you're playtesting and the build breaks, that's why — the data's location moved with the archive.

## 4. Priorities (in order)

1. **Human playtest** `combat-1v1-v4.html` — the actual reading-your-opponent loop, never yet exercised by a person. This is the input the next round of design decisions needs.
2. **Image-gen art direction** — character/pose art exploration, owner-run, in parallel with playtest.
3. Resolve the design opens that playtest surfaces (variance mechanism §1a and reaction slots are the two with real mechanical weight; wound regions / UI number display / Mind attribute are lower-stakes).
4. Confirm or reject the multi-actor combat question (`combat-scene-decisions.md` D4.3) — needs owner's direct recall, not more investigation.
5. Only after 1–4: restart a Godot MVP, scoped to what's actually validated.

## 5. MVP boundary (what "one 1v1 duel" means)

### IN (MVP)
- Two characters loaded from JSON; player controls one, simple scripted AI for the other.
- Full stat model: 5 attributes, 3 reserves, 2 meters, 3 guards.
- Round loop: **Declare → Arm → Resolve**. Action budget = whatever the reserves afford (no fixed action count). Resolution order = trick-taking by requirement sum (D2.13).
- Initiative bar (−50…+50) with reach threshold and dominant/desperate zones.
- Insight meter: built by abilities, spent *partially* as a hidden initiative modifier, secondary spend for info reveal. Capped at Wits/2, drained on reaction fire (D3.2, pending human-playtest confirmation).
- Reactions: one armed, hidden, persistent until triggered, graded by trigger specificity. Perfect-counter reversal = countered ability's delta only (D3.3, pending). Held reserve excludes itself from refill while armed (D3.4, pending).
- **Anatomical injuries**: typed damage → guard → severity band → named wound with stat effects. ~12 wounds authored. Damage amount scales with attacker Strength/100 before hitting guard (D3.1, pending).
- Win conditions configurable per scene: courage break · incapacitation · surrender · kill.
- ~16 abilities across body/mind/spirit including 4 reactions and 3 insight-generating openers.
- Scene conditions: engine supports the tracks; only **footing** and **light** authored.
- Cutaway stage: static pose images swapped per ability "shot" type; text log of resolution.
- Loadout screen before the duel (choose from library into typed slots).

### OUT (TARGET or FUTURE — designed, not built)
- Location node map, overworld, campaign, factions, NPC simulation.
- **Party combat, multi-target abilities** — sequenced after the 1v1 MVP, not rejected. N-vs-M (teams of three default, up to 3×3 allied) is confirmed real direction (D4.5); the MVP is still 1v1 first (S1.§0). Blocking open question before this is built: the initiative model for 3+ sides (`06-multi-actor-combat.md` §3).
- Technique acquisition/modification, traits, bonds, progression.
- Heart demeanor stances (TARGET — designed in bible, built after MVP).
- Elemental tag synergies beyond one demo pair (wet × lightning).
- Animation beyond pose swap; VFX; music; save system.
- Generations, marriage, time skips.
- A cinematic camera Director / beat-queue system (parked, D4.3) — revisit only once art direction is settled through image gen.

## 6. Doc map

**Context import (2026-09-20):** Shinobi Master's three ChatGPT chats have been brought into this workspace as text snapshots and reconciled art/lore notes. Read `07-shinobi-master-context.md` for provenance and limits, `02-art-direction.md` for current visual direction, and `03-world-factions.md` for culture exploration. This adds context without restarting the archived Godot work or changing the MVP. The import is a snapshot, not automatic synchronization.

| Doc | Role | Update when |
|---|---|---|
| `00-project-steer.md` | Read first. Phase, priorities, MVP boundary. | Phase or priority changes |
| `01-design-bible.md` | Single design source of truth. Every system, tagged MVP/TARGET/FUTURE. | Any design decision lands |
| `combat-scene-decisions.md` | Chronological decisions log with rationale and supersessions. | Any decision is made or reversed |
| `prototype-findings-01.md` | Session-1 sim results. **Historical** — read for ideas, not as canon. | Never (archive) |
| `prototype-findings-02.md` | What the v4 playable prototype shows (AI-vs-AI). **Superseded by human playtest going forward.** | After each play/tuning pass |
| `source-chatgpt-status-2026-09.md` | ChatGPT's parallel handoff doc, verbatim. Provenance only. | Never (archive) |
| `05-combat-presentation-plan.md` | Presentation rework plan. **Parked** (Godot-specific, D4.1) — historical. | Never, unless the parked thread is formally revived |
| `06-multi-actor-combat.md` | Multi-actor combat requirement + engine audit. **Confirmed design direction** (D4.5), TARGET not MVP. Engine audit (§2) is historical — refers to the archived port. | When the initiative model (§3) is decided, or a future Godot attempt redoes the engine audit |

**Rule:** if the bible and the decisions log disagree, the *later-dated* decision wins and the bible is corrected.

## 7. Open decisions (highest leverage first)

0. **Initiative model for N-vs-M** — a single shared bar can't represent 3+ sides. Per-actor / per-side / pairwise, none chosen (`06-multi-actor-combat.md` §3). Blocking for multi-actor combat (confirmed direction, D4.5); not blocking the 1v1 MVP.
1. **Variance mechanism** (bible §1a) — direction set, mechanism undecided. Highest-leverage open combat question for the 1v1 MVP.
2. **Confirm D2.13 trick-taking interleave** and tune it via human playtest.
3. **Wound regions** — proposal: head, torso, arms, legs (physical) + mind (mental) + spirit (spiritual). Confirm or expand.
4. **Reaction slots** — dedicated reaction slot(s) in the loadout, or reactions compete with actions for typed slots. Proposal: one dedicated reaction slot + optional second via build.
5. **Number scale in UI** — show raw 0–300 values, or bands (weak/sound/strong/elite/legendary) with raw on hover.
6. **Attribute list beyond the five** — does Mind need a *tested* attribute for genjutsu/perception separate from Wits? Currently no.

D3.1–D3.4 (damage-Strength scaling, Insight cap, reversal size, reaction refill exclusion) — reasoning stands, **application now gated on human playtest, not simulation or a Godot build** (D4.2).

## 8. Working preferences (for any agent)

- First-time game dev; basic Python/HTML/CS. **Explain Godot concepts when they become relevant, not before.**
- Concise. Bullets. No niceties. Present options with trade-offs. Ask before large/ambiguous work.
- Prefer open-source tooling. Data-driven design: decisions live as JSON, not prose to be reimplemented.
- Do not lock architecture prematurely. Do not treat unresolved items as settled.
- **Do not self-attribute a decision to "owner direction" without an actual instruction in this thread or this Project.** This went wrong once (D4.3) — an agent working solo in the Godot repo logged a major scope expansion as canon based on documents that can no longer be found.
- **Before trusting `C:\Claude\docs\` or this Project as current, check the other.** They diverged once (D4.3) without anyone noticing until the next session.
- Bold, multitudinous design thinking is welcome; scope discipline is mandatory.
