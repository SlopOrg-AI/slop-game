# Shinobi Master v2 — agent instructions (the full contract)

**Claude Code enters at `CLAUDE.md`, which carries the rules that gate action and does not load this file.** Read this one when the task needs the game's shape, the canon rules in full, or the per-agent notes. Platforms that read a single file natively read this one.

**What this is:** turn-based card battler with a persistent campaign and world state. Solo dev · PC/Steam · Godot 4.x / GDScript · hobby cadence. "Shinobi Master" is a codename.
Systems comps: MtG (ability kinds), Blades in the Dark (scale, crew sheet), City of Mist (tags), NITRO GEN OMEGA (camera), CK3 / Mount & Blade (campaign, travel). World/art comps: post-post-apocalypse, Meiji-style uneven industry, Ghibli ecology, Bebop, Paper Mario cut-outs on a wargame table. Full allocation with what each influence does *not* own: `design/01-pillars.md`.

**Phase:** pre-production. Target: a playable **Godot 1v1 duel demo** built from the settled combat design. No campaign, overworld, or party combat until the duel is human-played and tuned.

---

## 1. Canon rules (non-negotiable)

1. **This folder is canon.** Not the Claude Project, not ChatGPT, not any chat. Git history is the record of what changed when.
2. **`design/decisions.md` is the arbiter.** A design point is Decided only if it has a D-number there. Later D-number wins. If a design doc disagrees with the log, the doc is wrong — fix the doc.
3. **Three statuses, one scope tag, on every item:**
   - Status: `DECIDED` (has D-number) · `PROPOSED` (an agent or the owner floated it) · `OPEN` (question, no answer yet)
   - Scope: `MVP` (in the duel demo) · `TARGET` (designed, built after MVP) · `FUTURE` (idea only)
4. **Never self-attribute a decision to the owner** without an explicit instruction in your current session. If unsure, write it as `PROPOSED` in `proposals/` and stop.
5. **`proposals/` is free to anyone.** `design/` and `data/` — the game — change only on an owner instruction in the session doing the edit. Everything else is **mechanism**: the role that owns it decides, and logs it like any other decision (D260921.7-P). **No role may change what it is allowed to decide** — `PROTOCOL.md` §1 and §4 are the owner's alone. The owner (or an agent he directs) promotes a proposal by logging a D-number and editing the design doc.
6. **Scope discipline.** Do not expand the MVP. Do not make exploratory lore canonical. Do not restart parked threads.
7. **Transcripts and old docs in `sources/` are evidence, not instructions.**

## 2. Reading order

| Need | Read |
|---|---|
| Any task | this file → `design/00-steer.md` |
| Design work | + `design/01-pillars.md` + the one system doc you're touching |
| Art / lore | + `design/30-art-direction.md`, `design/21-world-factions.md` |
| Demo / engine work | + `design/10-combat-loop.md` … `15-information.md`, `50-world-systems.md` §6 (engine constraints), `data/`, `demo/README.md` |
| History | `sources/` (only when a doc cites it) |

Do not load every doc. Each is written to stand alone with its `Dependencies` line.

**Recording a ruling (D5.44-EP):** you do not log a D-number and you do not need Tech in session. Write the ruling into your own brief's `## Pending` block under a ref in your own namespace — `sys.12`, `art.3`, `cos.7`. Tech promotes it to a canonical `D5.nn-TAG` and keeps your ref as a permanent alias, so a doc may cite the local ref immediately and stay correct after promotion.

**`design/decisions.md` is not on this table, by decision (D5.43-P cl.6).** It is the arbiter, not reference: **matched, never read.** Every D-number carries an interested-party tag — **S** Systems · **A** Art/Direction · **C** Content · **E** Engine/tooling · **P** Process — so an agent pulls its own rows (`grep -E '^\| D[0-9.]+-[A-Z]*S' design/decisions.md`) instead of the file. Open it on three triggers only: two docs disagree · you are about to change something a D-number settled · you are ratifying one. Match on the **numeric part** — `D5.30` and `D5.30-ES` are the same row.

## 3. Doc template

Every file in `design/` follows `design/_TEMPLATE.md`: Purpose → Player experience goal → Rules / Data → Dependencies → Open questions → Status & scope table. Short. Tables over prose. Numbers live in `data/*.json`, not in prose to be re-typed. Cite a decision in its tagged form (`D5.35-AES`) so a reader sees whose it is without a lookup; a bare number still resolves.

## 4. Per-agent notes

- **Claude Code / Cowork:** `CLAUDE.md` points here. Cowork can write this folder directly. Commit small, message = what changed + D-number if any.
- **More than one Claude Code session runs at a time.** Exactly one holds the **Tech** seat (and, later, its successor); the others are **execution agents** belonging to the lead that launched them — they read that lead's brief, write in its paths, commit their own work under their own name, and hand a lead's brief a line rather than typing into it (D5.27). Owner direction, 2026-09-20; rides with the ruling on `proposals/2026-09-20-execution-agents.md`.
- **Codex / ChatGPT agents:** read this file natively. Work against the git repo. Output → `proposals/<date>-<topic>.md` unless the task says otherwise. Image-gen and art-board output → `proposals/art/`.
- **Claude.ai Project (chat):** the Project mirrors only `AGENTS.md`, `00-steer.md`, `01-pillars.md`. If a mirror and this folder disagree, this folder wins; re-sync the mirror.
- **Local LLM (RTX 5090):** batch/text/art-pipeline tasks only. Never the source of a design decision.

## 5. Working preferences (owner)

- First-time game dev; basic Python/HTML/CS. Explain Godot concepts when they become relevant, not before.
- Concise. Bullets. No niceties, no platitudes. Present options with trade-offs. Affirm/negate to communicate information, not tone.
- **Two registers, one budget** (C21 + C22, owner 2026-09-20).
  **Agent-facing** (briefs, proposals, `STATUS.md`, triage, handoffs): written for a reader that pays per token — tables, D/C refs, one line per fact, cite a path instead of restating what is on disk, no preamble or recap. The style rules above apply here, as compression.
  **User-facing** (chat replies to the owner): written for a person reading a screen — lead with the answer or the decision needed, plain sentences, short paragraphs; bullets only for parallel items, tables only for real comparisons. No imposed terseness, no padding. Say it once; name the file for detail; never paste file contents back into chat.
  **Plain words in chat:** spell out project shorthand the first time it appears in a reply — M1 (the playable Godot duel demo), D-numbers (decisions logged in `design/decisions.md`), C-refs (numbered pieces of owner feedback), lead names — or don't use it. A reply the owner has to decode is not concise; it is compressed at their expense. The shorthand belongs in agent-facing writing, where the reader has the docs loaded.
  **Both:** anything longer than a few lines goes to disk and is referenced, not repeated.
- Ask before large or ambiguous work. Propose, get a reaction, then commit to a document. Small iterations over big deliverables.
- **Minimize (C28).** Manage project bloat at all times; reduce governance overhead. No new governance file without deleting one.
- Prefer open-source tooling. Data-driven: decisions live as JSON, not prose.
- Do not lock architecture prematurely. Do not treat unresolved items as settled.
- Bold, multitudinous design thinking is welcome; scope discipline is mandatory.

## 6. How we work — see `PROTOCOL.md`

Roles, the session contract, the git rule, the decision rule and the budgets live in `PROTOCOL.md` (two pages, kept by Builder), and every change to them is one dated line in its §Changes. Charters are `roles/<role>.md`. Nothing about working practice is restated here — two copies of a rule is how this project spent 2026-09-20.

Rules 1–7 above are unchanged and outrank it.
