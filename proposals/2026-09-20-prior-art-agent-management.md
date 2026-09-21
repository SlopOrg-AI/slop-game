# Proposal — prior art in agent management, and what the evidence says about the payoff

**Produced by:** Cowork session, 2026-09-20, owner-requested ("claudebot", outside-agent read) — no lead hat. **Targets:** `AGENTS.md` §4–§6, `design/decisions.md` form, handoff sizing, the freeze decision (Q7). **Proposes:** adopt three named conventions, drop nothing else, and one honest expectation-setting. **Supersedes:** nothing. **Pairs with:** `2026-09-20-context-economics.md` (P1/P2 are restated below as a standard instead of an invention). **Status:** `PROPOSED`.

Method: web research, 2026-09-20. All figures cited to source; vendor blog claims marked as such.

---

## 1. Short answer

No, not the only one. The pattern has been independently invented enough times that it has a name at three levels — a file convention, a method family, and a game-dev-specific template — and **this project has converged on all three without having read any of them.** That is the good news and the warning: convergence means the design is sound; it also means the parts that were hand-rolled can be swapped for standards that already solved the scaling problems.

The unsettled question is not *how* to manage agents. It is **whether multi-agent is the right shape for this kind of work at all** — and there the two most credible sources disagree flatly (§3).

## 2. Prior art — three layers

| Layer | Name | What it is | This project's version |
|---|---|---|---|
| **Convention** | [`AGENTS.md`](https://agents.md/) | Cross-vendor open standard for a repo's agent instructions file; `CLAUDE.md` points at it | `AGENTS.md` + `CLAUDE.md` pointer. **Already correct, already standard.** Nothing to change |
| **Method** | [BMAD-METHOD](https://www.agentic-dev.org/resources/bmad) | Six named agent roles (Analyst, PM, Architect, Scrum Master, Dev, QA); two phases — "agentic planning followed by hyper-detailed story generation"; **documents are the context-handoff mechanism between agents** | `leads/` + `proposals/` + `STATUS.md`. Same idea, different nouns |
| **Method** | [GitHub Spec Kit](https://github.com/github/spec-kit) / spec-driven development | The spec is the source of truth; agents implement *from the spec*, not from chat. GitHub open-sourced the toolkit Sept 2025 | `design/` was meant to be this. It is 7.4% of the repo, six of twelve docs are stubs — which is exactly the failure SDD is built to prevent |
| **Game-dev** | [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 49 agents in three tiers (3 directors / 8 department leads / ~38 specialists), 7-phase pipeline, 12 hooks, `.claude/agents/` definitions, `production/session-state/active.md` for session state | `leads/` (3 tiers: CoS → Systems → Content/Tech), `.claude/agents/`, D5.39 hooks, `STATUS.md`. **Structurally the same system at 1/6 the agent count** |

**Convergent detail worth noting.** That game-studio template's core protocol is: *"Ask before proposing — agents present questions and 2-4 options with trade-offs. User decides."* That is the `Q<n>` queue, arrived at independently. Two systems built by strangers landed on the same answer to "how does a human stay the decision-maker"; that is the strongest available evidence the queue form is right.

**Caveat on that repo:** it appears as several identical forks under different owners. Treat it as evidence the *pattern* is widespread, not as a validated system. Worth mining for its hooks and its session-state file; not worth adopting 49 agents.

## 3. The live disagreement — is multi-agent even the right shape?

| Source | Position | Evidence |
|---|---|---|
| [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | **Pro, with limits.** Orchestrator-worker beat single-agent Opus 4 by **90.2%** on internal research evals | But: *"agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens."* And explicitly: multi-agent **underperforms** where agents need shared context or heavy interdependencies — *"most coding tasks"*, which have *"fewer truly parallelizable tasks than research"* |
| [Cognition, "Don't Build Multi-Agents"](https://cognition.com/blog/dont-build-multi-agents) | **Against.** Two principles: **(1)** *"Share context, and share full agent traces, not just individual messages"* **(2)** *"Actions carry implicit decisions, and conflicting decisions carry bad results"* | Recommends single-threaded linear agents plus a compression step, not parallel subagents |

**Where this project sits.** Game design is one interdependent object — one ruleset, one vocabulary, one set of pillars. It is the *shared-context* case Anthropic warns about, not the breadth-first-search case multi-agent wins. And Cognition's principle 2 has already fired here, twice, in one day:

- **`C23` issued twice** (`inbox/2026-09-20-three-deck-draw.md` vs `inbox/2026-09-20-mac-migration.md` line 1) — two surfaces, one counter, conflicting implicit decisions.
- **`draw` means two things** — the weighted power pull in C7–C10 and the card draw in C23 (`inbox/…three-deck-draw.md` §Conflicts #1). Two agents extended the vocabulary in different directions before anyone arbitrated.

**But the architecture is defensible as built,** and this is the important finding: `leads/` is *not* parallel multi-agent. It is **sequential role-switching with the disk as shared context** — one agent at a time, wearing a hat, reading what the last one wrote. That is much closer to Cognition's recommendation than the folder structure suggests.

**Therefore:** the thing to protect is *sequential + shared disk*. The thing to refuse is fan-out — two surfaces acting concurrently on anything that touches vocabulary, refs, or the log. The parallelism that is safe is the kind already in use: one agent working, others idle, handoff through files.

## 4. Named solutions to the problems already logged

| Problem | Named solution | Change |
|---|---|---|
| `decisions.md` grows O(n) forever and is read every design session (~7,900 tok at 38 rows) | **[Architecture Decision Records](https://learn.microsoft.com/en-us/azure/well-architected/architect-role/architecture-decision-record)** — one immutable file per decision, status field (`Proposed` / `Accepted` / `Superseded by <id>`), **generated index**. Tooling exists ([adrgen](https://github.com/ipfans/adrgen), Log4brains) | `design/decisions/D5-39-guard-rails.md` etc.; `decisions.md` becomes the generated index: ID · `Acts on it` · one-line claim · status · doc. **The one-file-per-decision form exists precisely so nobody loads all of them.** This replaces P1/P2 in `…-context-economics.md` with a convention that has tooling |
| Handoff files are load-bearing required reading (F7); `…-session-6-handoff.md` is 6,477 tok | [Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): sub-agents return **"condensed summaries (1,000-2,000 tokens)"** to the coordinator | Cap handoffs at ~2k tokens. The current one is 3–6× over. A handoff longer than that is a document that has not been written yet |
| Reading order / "do not load every doc" | Same source: **just-in-time retrieval** — keep *"lightweight references (file paths, queries, links)"* and load at runtime, over pre-loading | `AGENTS.md` §2 already does this correctly. Keep it; it is the named best practice |
| The `decisions.md` bulk problem in general | Same source: **compaction** — summarize, *"preserve architectural decisions and critical details while discarding redundant outputs"*; and *"context rot"*: recall degrades as tokens grow, so target *"the smallest possible set of high-signal tokens"* | The guiding principle to cite when arguing for any deletion |
| `design/` stubs while canon lives in the log | **Spec-driven development**: the spec is the artefact agents build from | Distillation is not tidying. It is the step that makes the whole system work |

## 5. The payoff — what the measured evidence actually says

Stated plainly, because the expectation is "once the machine is set we'll get productivity gains."

| Source | Finding |
|---|---|
| [METR RCT, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (16 experienced OSS devs, 246 tasks, randomized) | Devs with AI tools took **19% longer**. They expected **+24% faster** beforehand and **still believed +20% faster afterwards**. A ~40-point gap between felt and measured |
| [DORA 2025](https://dora.dev/insights/balancing-ai-tensions/) (industry-wide) | Higher AI adoption → **both** higher throughput **and** higher instability. AI is an **amplifier**: strong platforms/workflows/testing gain; fragmented or fragile setups get *"help … generate technical debt faster."* 90% use AI; >80% believe it makes them more productive; 30% don't trust the output |
| [GDC 2026 State of the Industry](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/) | Only **36%** of game professionals use generative AI (30% at studios). Top uses: **research/brainstorming 81%**, code assistance 47%, prototyping 35%. **52%** think it is harming the industry — design/narrative roles 63% negative |
| [Indie read of the same data](https://www.strayspark.studio/blog/gdc-2026-ai-takeaways-indie-developers) | *"Every shipping game using AI in production has humans at every meaningful decision point."* What works for small teams: code assistance, editor automation over MCP. What fails: autonomous content generation |

**Honest synthesis, three points:**

1. **DORA's amplifier finding is the one that governs this project.** The gains scale with the quality of the substrate being amplified. Today the substrate is 7.4% game rules and 50% governance (`…-context-economics.md` §1). Amplifying that produces more governance — which is what the last day produced: ~12,000 words of process, 0 words of new system docs.

2. **METR's perception gap is the reason the measurement line matters.** Experienced people were 19% slower and felt 20% faster. A solo dev's sense of "this is working" is not evidence, in either direction. The one-line session metric proposed in `…-context-economics.md` §5 is the only available defence, and it costs one line.

3. **The documented gains are downstream of M1, not here.** Research/brainstorming and code assistance are where measured value sits. Pre-production design-doc work — the current phase — is the phase in which the machine is *built*, and its return is realized later, against a Godot codebase and a schema. Expecting the gain during construction is expecting it one phase early.

**Expectation worth holding:** the setup is likely to pay off, but as *consistency and recoverable state across sessions* — no re-explaining, no lost decisions, a cold agent useful in 20 KB — rather than as raw speed. That is a real and large benefit for a solo hobby project with intermittent sessions. It is not the same claim as "faster", and it should not be measured as if it were.

## 6. Recommendations

| # | Do | Who | Cost |
|---|---|---|---|
| **N1** | Convert `decisions.md` to ADR form: one file per D-number, generated index. Supersedes P1/P2 | Systems + Tech | Half a session; uses an existing convention rather than a new house rule |
| **N2** | Cap every handoff and proposal at ~2k tokens (Anthropic sub-agent guidance). Anything longer is a design doc that has not been written | Chief of Staff | A line in `leads/README.md` §Running a lead session |
| **N3** | **Write the no-fan-out rule into `AGENTS.md` §4**: one surface acts at a time; never two concurrently on refs, vocabulary or the log. C23 and the `draw` collision are the same failure Cognition names | owner ruling | One line; prevents the only failure mode already observed twice |
| **N4** | Mine [Claude Code Game Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) for its hooks and its `session-state/active.md`. Adopt neither the 49 agents nor the 7-phase pipeline | Tech, opportunistic | Read-only, 20 min |
| **N5** | Treat distillation as spec-driven development, not housekeeping — `design/` is the artefact the agents build from, and it is the gate on every gain in §5 | Systems | Already the critical path; this is the argument for why it outranks governance work |

**Against the freeze question (Q7):** the research strengthens the case for freezing. Every remaining improvement above is *adopting an existing standard and deleting the hand-rolled version*. None of them requires inventing process, and all of them shrink what is read.
