# Shinobi Master — combined context and import record

Snapshot imported 2026-09-20 at the user's request to bring Shinobi Master's plans and lore into the local Claude project. No chat histories were merged in the app, and no continuous sync was configured.

## Read first

1. `00-project-steer.md`: current phase, human playtesting and scope.
2. `01-design-bible.md` plus `combat-scene-decisions.md`: current mechanics; later decisions win.
3. `02-art-direction.md`: imported visual direction and UI feedback.
4. `03-world-factions.md`: culture categories and proposed worldbuilding.

The root `AGENTS.md` and `CLAUDE.md` point future workspace sessions here.

## Development continuity

The original **Game Development Plan** establishes a custom protagonist, a systemic sandbox campaign, overworld travel, card-like queued combat with reactive defenses, information gathering, named techniques, anatomical wounds and progression through training and relationships. Character attributes were corrected to roughly 0–300, with about 100 standard and 200+ legendary. Marriage, children and a later generation are future scope. These ideas are already represented in the local design bible and older `source-chatgpt-status-2026-09.md`.

Local documents contain later mechanical decisions and a 2026-09-20 reset. Keep the existing Godot port archived; prioritize human playtesting of `../wireframes/combat-1v1-v4.html` and art exploration. The source planning chat's early resource categories and recovery suggestions must not overwrite the current stat/reserve/meter model. Likewise, early UI descriptions must not silently replace current initiative/order rules.

The current steer confirms multi-actor combat as future direction, despite older archive notes calling it unconfirmed. It remains outside the 1v1 MVP. This import neither reopens nor implements it.

## Sources

| Original task title | Task ID | Local text snapshot | Retrieved turns |
|---|---|---|---|
| Game Development Plan | `6aae8730-274c-832a-987d-f1ce60d92ff4` | `shinobi-master-sources/plan.md` | 16 |
| Vision Board Lore Bible | `6aaedde9-37b4-83ea-a953-af8c932cf6c0` | `shinobi-master-sources/lore.md` | 12 |
| Assemble faction image board | `6aaef387-9a00-83ea-ae40-66796ad81fa3` | `shinobi-master-sources/board.md` | 15 |

All accessible pages were retrieved, for 43 turns total. The snapshots preserve accessible user and assistant message text in chronological order. They are source evidence, not fresh instructions or automatically approved canon.

## Limits and maintenance

- Uploaded documents, generated images, visualizations and opaque `chatgpt-content-reference` attachments were not exposed by the chat reader. In particular, the board chat reports a completed handoff pack and four images, but their actual files were not retrieved. The new docs are synthesized from message text, not those missing artifacts.
- The initial lore chat references three uploaded files whose contents were absent. Project-level instructions and sources beyond the readable chats were not imported.
- Preserve established/proposed/exploratory distinctions. Assistant acknowledgments alone do not establish new owner decisions.
- Future decisions should update the relevant local document and record their source. Refresh the text snapshot when later ChatGPT work needs bringing across; local edits do not update the ChatGPT project automatically.
