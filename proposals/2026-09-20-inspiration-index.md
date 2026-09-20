# Proposal — inspiration index (mechanical + world/art)

**Produced by:** Claude (Cowork), 2026-09-20 · **Targets:** `design/01-pillars.md` §Influence allocation, `design/30-art-direction.md` (stub), `design/21-world-factions.md` (stub) · **Proposes:** two candidate influence-table rows (ukiyo-e, UI-as-animate-paper), a resolved contradiction (animatic over Bunraku), and a wording sharpen on the Paper Mario row (paper-doll / standee construction, already targeted, not yet named) · **Supersedes:** nothing (no D-numbers claimed). Status: `PROPOSED`.

Companion: a browsable artifact mirrors this index for exploring and jotting new sources — link shared in chat, not checked into the repo.

---

## 1. What this is

The mechanical/systems influence table in `01-pillars.md` already has real discipline: every row states what it owns *and* what it explicitly doesn't (pillar 7, scope discipline, D5.5 DECIDED). The world/setting/art references pulled from ChatGPT sessions (`sources/board.md`, `sources/lore.md`) don't have that discipline yet — they're mood-board transcript notes, and `30-art-direction.md` / `21-world-factions.md` are still stubs. This proposal (a) gives the world/art references the same owns/doesn't-own structure so they're ready to fold into those docs when their session comes up, and (b) surfaces what a full read of `lore.md` turned up that isn't in the pillars table yet: one genuine gap and one genuine contradiction.

No changes to the 24-row `01-pillars.md` table are proposed except the one new row in §3 — everything else there checked out as already covering what's in `lore.md`/`board.md` (NITRO GEN OMEGA, Paper Mario, Zero Company/XCOM, Cassette cyber-funk, Noir·caballero/frontier, Historical shinobi all restate rows that already exist).

## 2. World / setting / art references — proposed owns / does-NOT-own pass

**A. The 8 MVP faction culture refs** (`sources/board.md`, world-board logic: ecology → livelihood → architecture → clothing)

| Culture | Real-world pull | Owns | Does NOT own |
|---|---|---|---|
| Jungle / Deep Forest | Borneo longhouses + Amazon river settlements | elevated timber structures, communal houses, woven materials, settlements swallowed by forest | costume rules (Naruto row), world era (Meiji row) |
| Swamp / Wetland | Sudd wetlands | reed islands, seasonal flooding, dugouts, mud, cattle trails | — |
| Desert Nomads | Tuareg / Saharan | wrapped silhouettes, indigo/white cloth, portable tents, near-zero permanent architecture | desert villagers' architecture (below) |
| Desert Villagers / Oasis | — | earthen compounds, painted walls, courtyards, irrigation | nomad silhouette language |
| River People | — | long narrow boats, docks instead of roads, stilt buildings, river markets | — |
| Pilgrims | Ethiopian highland pilgrimage | robes, staffs, processions, sacred roads, rock-cut sanctuaries — a *social identity*, not an ethnicity | any single faction's costume (pilgrims cross factions) |
| City Dwellers | dense premodern medinas | narrow shaded streets, vertical density, workshops on the street, markets, gates | — |
| Agricultural Villagers | — (the world's visual baseline) | fields, irrigation, grain storage, timber/mud houses, communal shrine | exoticized-culture treatment — deliberately the default, not another costume |

**B. Naruto aesthetic moodboard** — distinct from the existing `01-pillars.md` "Naruto" row, which owns narrative/action-readability/progression-arc/anachronism-ceiling. This is specifically the *visual* ingredient list:

| | Owns | Does NOT own |
|---|---|---|
| Naruto aesthetic ingredients | bold high-contrast silhouettes, flat saturated palettes (orange/blue, green/black, navy/white), graphic symbols (insignia/clan marks/seals) as instant affiliation, practical kit (wraps/pouches/mesh) over ornamented armor | world, costume specifics, name (already owned by the "Naruto" pillars row) |

**C. Paper-cutout + tabletop terrain art rule** (owner priority order, `lore.md`): silhouette-first > animation-ready clothing (cloth/straps/sleeves, avoid rigid armor) > flat faction colors (3–5 saturated per culture, minimal shading). Overlaps `01-pillars.md`'s Paper Mario and Tabletop wargaming rows — does NOT own theater/puppet framing (Paper Mario's anti + the anti-goals list) or rules/grid (Tabletop wargaming's anti).

## 3. One gap: proposed new row for `01-pillars.md`

| Influence | Owns | Does NOT own |
|---|---|---|
| **Ukiyo-e (Japanese woodblock landscape prints)** | atmospheric backdrop for travel/overworld: mountains, roads, rice terraces, mist, seasonal light | character costume or color rules (Naruto row owns those) |

This is genuinely new — it's in `lore.md` (cited: Met public-domain woodblock prints, atmospheric reference for travel/landscape) but has no row and nothing else in the table owns "overworld landscape mood." Small, cheap addition; only needs a D-number if you want it locked before the art-direction session.

## 4. One contradiction — resolved

`lore.md` floated **Bunraku / puppet theater** as an alternative presentation lean for the plan→watch camera staging, alongside **"anime animatic."** `01-pillars.md`'s Anti-goals rule out *"theater framing (curtains, puppets, storybook narrator)"*, and Paper Mario's own does-NOT-own column says the same: *tone, theater, puppets*. Bunraku is out on both counts.

**Resolution (session 2):** "animatic" is the surviving half of that either/or, not a new idea — it trips no anti-goal and it's already close to what NITRO GEN OMEGA owns (camera cuts, plan → watch rhythm: an animatic *is* a sequence of held frames cut together with timing). Worth a one-line note in `decisions.md` next time `10-combat-loop.md` or `30-art-direction.md` gets touched: staging reads as *animatic*, never theater/puppet, so a future agent doesn't resurrect Bunraku from `lore.md` thinking it's still live.

## 5. Open questions

1. Does the ukiyo-e row get a D-number now, or wait for the `30-art-direction.md` distillation session (per the successor-review sequencing, 20/21/30 stay stubs until after M1)?
2. Should §2's owns/doesn't-own tables move into `21-world-factions.md` / `30-art-direction.md` verbatim when those come off stub, or get re-derived fresh from `sources/` at that time?
3. Nothing else in `lore.md` beyond §2–4 above needs action — everything else it references restates existing `01-pillars.md` rows.

## 6. New owner-stated directions (session 2, 2026-09-20)

Owner input, not agent-proposed — recorded here for the same reason as §3/§4: neither has a D-number yet, both are cheap to lock later.

| Influence | Owns | Does NOT own |
|---|---|---|
| **UI as animate paper** | UI elements read as physical paper — folding, fluttering, z-depth as interaction feedback (panels sliding like sheets, edges catching light, paper-grain/shadow). Extends the decided "ink over paper" palette value (`docs/05-combat-presentation-plan.md` D3.2) from color into material behavior. Also extends the Paper Mario row's cut-out language from world/character presentation into UI specifically. | Combat camera/animation grammar (that's NITRO GEN OMEGA / animatic, §4); the decided UI/UX boundary in D3.3 ("tabletop language applies to props, not UI/UX") still holds — this doesn't reopen it. |

**"Manga panels come to life" — dropped (session 2).** Traced piece by piece: held-frame timing and cut-to-cut rhythm were already NITRO GEN OMEGA's; the page-turn reveal was rejected by the owner; the one sliver left (panel border/gutter as a drawn object) is thin enough, and animatic (§4) already covers the staging feel it was chasing, that it isn't worth carrying forward as its own thread. No row proposed.

**Paper doll / standee — not a gap, a naming sharpen.** Both are already decided, just not labeled this way in `01-pillars.md`:
- **Standee** is already owned — Tabletop wargaming's row says "grouped-standee mass units," and `00-steer.md` M2 names "cut-out standees" outright.
- **Paper doll** (a base rig with swappable flat pose/costume layers) is already the *target* construction — `00-steer.md` M2 says "pose-swap cut-outs," and the stated production pipeline (3D base model → generated flat 2D pose/costume pieces) is a paper-doll pipeline by definition. It just isn't named that way: Paper Mario's `owns` column currently reads "cut-out material, layered flat sets," which is vaguer than what's actually committed.

**Proposed wording sharpen** (Paper Mario row, `01-pillars.md`) — owns: *cut-out material, layered flat sets, paper-doll pose/costume-layer construction*. No scope change, just naming what's already decided so a future agent doesn't have to re-derive it from `00-steer.md` M2 each time.

**Open:** ukiyo-e (§3), UI-as-paper (above), the animatic resolution (§4), and the Paper Mario wording sharpen — four small items, none with D-numbers yet.
