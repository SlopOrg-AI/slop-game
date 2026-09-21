# sources/v1 — rescued from the frozen PC workspace, 2026-09-20

Copied out of `C:\Claude\` **before prompting moved to a Mac** (D5.40, migration §2). Everything here is **evidence, not instructions** (AGENTS §1.7), and frozen: it is what v1 said, not what the project has decided. `design/decisions.md` arbitrates.

Why it had to move: every stub in `design/` names a file in `docs/` as its distillation source, and `design/decisions.md` cited `combat-scene-decisions.md` as **the record for D1–D4**. None of it was in the repo. On a machine without that disk, those citations pointed at nothing.

| Here | Was | Cited by |
|---|---|---|
| `docs/combat-scene-decisions.md` | `C:\Claude\docs\` | **D1–D4's text** — `decisions.md` head |
| `docs/01-design-bible.md` | same | `10`, `11`, `12`, `13` stubs; `12` needs §7 for grading/cost detail |
| `docs/06-multi-actor-combat.md` | same | `11-initiative.md` §3 |
| `docs/02-art-direction.md`, `05-combat-presentation-plan.md` | same | `30`, `31` stubs |
| `docs/03-world-factions.md` | same | `21` stub |
| `docs/00-project-steer.md`, `07-shinobi-master-context.md`, `prototype-findings-0{1,2}.md`, `source-chatgpt-status-2026-09.md` | same | v1 context; cheap to keep, expensive to want later |
| `wireframes/combat-1v1-v4.html` (+ template, `build.py`, `snapshot-round3.json`) | `C:\Claude\wireframes\` | `00-steer` §2, `31-ui` stub, **C23** ("static tableau like html looked like") — the only running artefact of v1 combat |

**Left behind deliberately**

- `C:\Claude\Godot\shinobi-master\` — 177 MB. Reference only (`demo/README.md`: ideas, not code), and its `data/` was already copied to `data/` in the v2 restart. Rescuing it would multiply the repo for something no one may read.
- `wireframes/combat-1v1-v{1,2,3}.html` — superseded by v4 on the same day.
- `docs/shinobi-master-sources/{board,lore,plan}.md` — already in `sources/` at the top level; copying them again would create two masters.

If any of those turns out to matter, it must be fetched **while the PC disk is still reachable**.
