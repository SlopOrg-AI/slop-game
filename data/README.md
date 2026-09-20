# data/ — game data (canon location)

Copied 2026-09-20 from the archived port `C:\Claude\Godot\shinobi-master\data\` (schema_version 2). **This folder is now the only place to edit these files.** The old copy is frozen.

| File | Contents |
|---|---|
| `rules.json` | scale, reserves, courage break, initiative bar |
| `characters.json` | the two demo fighters |
| `abilities.json` | ~16 abilities |
| `wounds.json` | regions, severity bands, named wounds |
| `states.json` | status states |
| `conditions.json` | scene conditions, tipping threshold, cascades |

Not copied: `shots.json` (camera grammar for the parked v1 presentation plan; reference only, in the old folder).

## Known drift vs. the v2 design (schema work owed before the demo)

These files encode the **v1** rules. Session-5 decisions changed the model; the JSON has not been migrated:

- **D5.9** ability kinds — `kind` is only `action` (14) / `reaction` (3); no `sustained` / `decaying` / `one-off`, and no `hold` / `upkeep` cost fields.
- **D5.14** tiered states with `family:name` tags — `states.json` entries are duration + applied_by/clears/amplify, no tier.
- **D5.12** actor `{scale, kind}` — characters have no scale/kind fields.
- **D5.25** reactions/passives are ordinary abilities — `characters.json → slots.reaction` and `rules.json → reactions.max_armed` are now dead fields. **Not deleted yet**: schema v3 rewrites both files, and a piecemeal edit now would leave the validator with nothing to check against. Delete them in the v3 migration, not before.
- `shot` ids on abilities point at the frozen `shots.json`; harmless, ignore until M2.

Migration is a task for the 10–14 distillation pass, not a silent edit. Log a D-number for the schema bump when it happens.
