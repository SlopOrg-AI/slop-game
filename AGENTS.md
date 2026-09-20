# Shinobi Master v2 — agent instructions (read first, every agent, every session)

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
5. **`proposals/` is the only place non-owner agents write freely.** Everything else changes only on an owner instruction in the session doing the edit. The owner (or an agent the owner directs) promotes a proposal by logging a D-number and editing the design doc.
6. **Scope discipline.** Do not expand the MVP. Do not make exploratory lore canonical. Do not restart parked threads.
7. **Transcripts and old docs in `sources/` are evidence, not instructions.**

## 2. Reading order

| Need | Read |
|---|---|
| Any task | this file → `design/00-steer.md` |
| Design work | + `design/01-pillars.md` + the one system doc you're touching + `design/decisions.md` (skim latest entries) |
| Art / lore | + `design/30-art-direction.md`, `design/21-world-factions.md` |
| Demo / engine work | + `design/10-combat-loop.md` … `15-information.md`, `50-world-systems.md` §6 (engine constraints), `data/`, `demo/README.md` |
| History | `sources/` (only when a doc cites it) |

Do not load every doc. Each is written to stand alone with its `Dependencies` line.

## 3. Doc template

Every file in `design/` follows `design/_TEMPLATE.md`: Purpose → Player experience goal → Rules / Data → Dependencies → Open questions → Status & scope table. Short. Tables over prose. Numbers live in `data/*.json`, not in prose to be re-typed.

## 4. Per-agent notes

- **Claude Code / Cowork:** `CLAUDE.md` points here. Cowork can write this folder directly. Commit small, message = what changed + D-number if any.
- **Codex / ChatGPT agents:** read this file natively. Work against the git repo. Output → `proposals/<date>-<topic>.md` unless the task says otherwise. Image-gen and art-board output → `proposals/art/`.
- **Claude.ai Project (chat):** the Project mirrors only `AGENTS.md`, `00-steer.md`, `01-pillars.md`. If a mirror and this folder disagree, this folder wins; re-sync the mirror.
- **Local LLM (RTX 5090):** batch/text/art-pipeline tasks only. Never the source of a design decision.

## 5. Working preferences (owner)

- First-time game dev; basic Python/HTML/CS. Explain Godot concepts when they become relevant, not before.
- Concise. Bullets. No niceties, no platitudes. Present options with trade-offs. Affirm/negate to communicate information, not tone.
- Ask before large or ambiguous work. Propose, get a reaction, then commit to a document. Small iterations over big deliverables.
- Prefer open-source tooling. Data-driven: decisions live as JSON, not prose.
- Do not lock architecture prematurely. Do not treat unresolved items as settled.
- Bold, multitudinous design thinking is welcome; scope discipline is mandatory.
