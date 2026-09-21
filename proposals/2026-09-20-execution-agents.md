# Proposal — one execution agent per lead, and what Tech oversees

**Produced by:** Tech (Claude Code), 2026-09-20 · **Targets:** `CLAUDE.md`, `AGENTS.md` §4/§6, `leads/README.md`, `tools/claude-agents/`, `proposals/2026-09-20-commit-sweep.md` §A.1 · **Proposes:** adopt the owner's model with two corrections · **Status:** `PROPOSED` — Chief of Staff and the owner rule; Tech states the mechanism only. Next free D-number **D5.41**.

**Owner, in chat:** *"i think each lead has a claude code subordinate to execute on their behalf. you as tech lead also oversee these subordinates. does that cohere"*

---

## 1. Short answer: yes, and it is already half-built

`tools/claude-agents/` has held one pointer per lead since the structure went in — `art`, `content`, `level`, `scenario`, `systems`, `marketing`, `tech` — each a thin file that says *act as this lead, read this brief*. The owner's model is that folder's premise, stated out loud. The art execution agent running against the local Qwen stack is the first one in the wild.

It also matches the split the project already made twice: **D5.38** separated deciding what the board says from typing it; **D5.39 A.1** separated judging work from committing it by path. Lead decides, subordinate executes, is the same cut a third time. That is coherence, not coincidence.

## 2. Correction 1 — Tech's interest in another agent's output is **custodial**, and that is a real interest

*Owner, clarifying:* **"since you have custody, you care about the other cc agents' output right?"** — yes, and the first draft of this section argued against a position the owner was not taking. Custody is not editorship, but it is not indifference either. Every line below is something Tech is obliged to care about **without reading the work for meaning**:

| Tech's business, because Tech holds the record | Why |
|---|---|
| **Does it reach the record at all?** Uncommitted work is invisible and dies with the machine | Canon rule 1: git history is the record. Caught by hand twice before the sweep existed |
| **Where was it written?** `design/`, `data/`, another lead's brief, `sources/` | Rule 5 and D5.27. A path test, never a content test |
| **Is it attributed to whoever wrote it?** | A.3. Got this wrong three times on 2026-09-20 and had to correct the log |
| **Does it pass the mechanical checks?** Duplicate D-number, stale board number, art binary, D-number named in the message | D5.39. Impartial: they refuse Tech's own commits too, and did |
| **Did it log a D-number?** No agent may, ever | AGENTS §1.4 — checkable without judging the decision |
| **Is the tree left readable for the next session?** No half-staged work, no clean-tree lie on the board | Custody |

And the line that does not move:

| Not Tech's, at any point | Whose |
|---|---|
| Whether the board is any good | Art |
| Whether a rule is balanced or a term is right | Systems |
| Whether a scene or duel is worth authoring | Level / Scenario |
| Whether the work should have been done at all | The commissioning lead, and the owner |

**One line for `CLAUDE.md`:** *Tech is answerable for whether every agent's output reaches the record, correctly placed and correctly named; each lead is answerable for whether it is any good.*

This is why the sweep is built on paths: it is the mechanism that lets Tech care about another agent's output **without judging it**. With one execution agent per lead that interest does not grow — it **scales**, which is the argument in §4.1 for each surface committing its own work. The checks then sit in the hooks, which are impartial, rather than in Tech's discretion. Chief of Staff's after-the-fact audit (D5.39) covers the layer no machine can see.

## 2b. The part that still does not hold — supervision of content

Taken literally, Tech overseeing every lead's execution agent undoes the reason Tech exists in its current shape. **D5.29** took judgement off Tech deliberately; **D5.38** kept Tech out of what the board *says*; Tech's own brief says it never resolves a rule in code and escalates instead. If Tech supervises what every subordinate produces, Tech becomes everyone's editor through the back door — reviewing art, content and scenario work it has no standing to judge.

The version that holds:

| Tech oversees | Tech does not |
|---|---|
| The agent definitions (`tools/claude-agents/`, `.claude/`), permissions, hooks, the sweep | Whether the board is any good — Art |
| Git: who commits, under what name, staged by path | Whether an ability is balanced — Systems |
| That a subordinate's output lands where its lead can see it | Whether a scene is worth authoring — Level / Scenario |
| That a subordinate does not exceed its brief *mechanically* — writing outside its lead's paths, committing another lead's brief, editing `sources/` | Whether the work is *right*. **That is the commissioning lead's, always** |

**One line for `CLAUDE.md`:** *Tech runs the agents; each lead judges what its own agent produced.*

## 3. Correction 2 — two different things are both being called "subordinate"

This distinction decides the rules, so it cannot stay blurred:

| | **Subagent** (inside a session) | **Separate session** (what the art agent is) |
|---|---|---|
| What it is | A task the parent Claude Code session delegates, from `.claude/agents/` | Its own Claude Code instance, own context, own git |
| Working tree | The parent's | Its own — or worse, *the same one*, which is today |
| Can it commit? | Only as the parent; its work **is** the parent's work | Yes, independently |
| Attribution | The parent's name. Nothing to decide | Its own name, or the log lies — as it did three times today |
| Governance | None needed | Needs a brief, a routing tag, and a row in the sweep table |

`tools/claude-agents/` describes the first. What is actually running is the second. **D5.27, D5.38 and D5.39 were all written for two surfaces**; there are now three, and this model implies up to eight.

## 4. What it costs, mechanically

1. **Attribution stops being guessable.** Today the sweep asks Tech to name the author and Tech guessed from a stale assumption — `--surface Cowork` on two files an art agent wrote. With N surfaces that is not an occasional slip, it is the default outcome. **Fix: each separate session commits its own work.** If it has git, it does not need Tech to carry it.
2. **One working tree stops being viable.** Three surfaces on one tree produced a duplicate D-number claim and two misattributions in a day. **The remote landed today (D5.40), so the structural fix is now available: one clone per surface, each pushing.** The sweep was logged with an expiry for exactly this; it expires here, not at the Mac move.
3. **`CLAUDE.md` currently tells every Claude Code session it is Tech.** The art agent, read literally, believes it is me. Each execution agent needs its identity in its own pointer file, and `CLAUDE.md` needs to say *this default applies unless you were launched as another lead's agent*.
4. **Hooks and settings apply per clone.** `git config core.hooksPath tools/hooks` on arrival, every time — already in `README.md`, now load-bearing.

## 5. Where the model is genuinely untested

- **Chief of Staff does not obviously need one.** Cowork writes the folder itself. An execution agent for it would be a second writer of the same brief — the thing D5.27 exists to prevent.
- **Two leads, one agent.** Content and Art both want the image pipeline. If the art execution agent serves both, "its lead" is ambiguous the first time they disagree, and §2's rule has no answer.
- **Cost.** Every execution agent is a context that must be paid for and re-oriented. `proposals/2026-09-20-context-economics.md` (not written by Tech) is the relevant reading before multiplying surfaces.

## 6. For the owner and Chief of Staff

1. Adopt §2 as the definition of "oversee" — Tech runs the agents, each lead judges its own agent's output. One line in `CLAUDE.md`.
2. Adopt §3's distinction, and give any **separate session** a pointer file that names it, a routing tag, and the instruction that **it commits its own work**.
3. Rule on §4.2: one clone per surface now that a remote exists, which retires the sweep early — or keep one tree and keep sweeping.
4. Name the art execution agent's lead (Content or Art) and whether it commits its own art output.
