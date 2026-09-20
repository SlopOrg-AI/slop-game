# Direction — umbrella (art · level · scenario)

Reports to: owner (via Production) · Three authoritative leads: `art.md`, `level.md`, `scenario.md` · Updated: 2026-09-20

## What Direction is
The leads with an **authoritative grasp** of how the game should look, how its spaces are built, and how its encounters are staged. Each defines **clusters of content** — a coherent, named set of things the game needs (e.g. "Kaede + Genzo cut-outs, 2 poses", "one duel arena: 2 zones, 2 anchors, 1 cover edge", "M1 scripted opponent with counter-memory"). Content produces the cluster; Engine loads it; Systems supplies the vocabulary it is expressed in.

## Shared rules (all three)
- The test is `design/01-pillars.md`: pillars, the **influence allocation table** (each influence owns one job and is barred from others), anti-goals. Direction may propose a new row; only the owner adds one (D5.5, D5.16–D5.23 precedent).
- **One table, one world** (pillar 4): terrain table → diorama → cut-out; only the camera changes scale. Any direction that needs a second visual language is out.
- **Scope discipline** (pillar 7): Direction defines clusters for M1/M2 first. TARGET/FUTURE clusters are written as one-line stubs, not designed.
- Direction critiques; it does not produce. Critique is anchored — `tools/annotate/` pins for boards, C-refs for owner words.
- Direction never edits `data/` or `demo/`.

## Cluster handoff to Content
A cluster is ready for Content when its Direction lead has written, in its own brief's status table:

| Field | Meaning |
|---|---|
| Cluster name | short, stable id (`cutouts-m1`, `arena-m1`, `ai-m1`) |
| Spec | one paragraph + the pillar rows it must satisfy |
| Acceptance | what "done" looks like — the critique checklist Direction will apply |
| Scope | MVP / TARGET / FUTURE |
| Systems dependency | which ontology terms / schema fields it needs (blocks until Systems has them) |

Content works only from a cluster in that form. Direction reviews the result against **Acceptance** and either accepts (Engine may load) or returns with annotated critique.

## Split between the three
| Lead | Owns | Overlap rule |
|---|---|---|
| **Art** | look: character, costume, material, palette, UI paper grammar, camera register | if it's about *how it reads visually* → art |
| **Level** | space: scene shape, zones/anchors/edges, dioramas, table, cover, footing/light authoring | if it's about *where things are and what the space affords* → level |
| **Scenario** | staging: which actors, which abilities, what the opponent does, win conditions, pacing of a fight | if it's about *what happens and why the player is there* → scenario |

Cross-overlaps (a diorama's *look* vs its *layout*) → the two leads write one joint cluster; art holds the pen.
