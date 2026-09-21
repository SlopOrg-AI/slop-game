# Continuity — successor, failover, stale git

**Produced by:** Chief of Staff (Cowork), 2026-09-20, owner-directed · **Status:** PROPOSED; queue row §5. If ruled: `FAILOVER.md` at repo root (≤40 lines, provider-neutral) + one header field in `STATUS.md`.
**Owner said:** *"assume CoS successor is also fable and has access. consider also a failover assistant if claude network not accessible. and of course that git which i assume is primary is not update[d] and tech not responsive."*

## 1. Assumptions
- Successor Chief of Staff = same model class (Fable), Cowork, repo folder connected on whatever machine is current. Handoff files assume full capability; no degraded mode needed for the normal successor.
- After C24, the private remote is **primary for transport**, but rule 1 stands: **the working clone the owner is sitting at is canon.** The remote is a backup that may lag.

## 2. Tiers

| Tier | Condition | Who acts | What changes |
|---|---|---|---|
| 0 | normal | CoS = Cowork; Tech = Claude Code | as documented |
| 1 | **Tech unresponsive** (Claude Code down or absent) | CoS + owner | D5.38 custody split **lapses**: CoS writes `STATUS.md` directly (drift guard still applies). Owner commits by hand with the recipe in `FAILOVER.md`. Hooks still run locally. CoS stamps the board header `TECH DOWN since <date>`; Tech reconciles on return |
| 2 | **Claude network unreachable** (Cowork + Claude Code both down) | **Failover assistant** — ChatGPT/Codex first, local LLM (5090) if offline too | Boots from `FAILOVER.md`: read `AGENTS.md` → `STATUS.md` → `leads/chief-of-staff.md`. May write **only** `inbox/`, `proposals/`, and `STATUS.md` rows stamped `FAILOVER <provider> <date>`. Same canon rules: no D-numbers, no `design/`/`data/` edits without owner instruction in that session. Owner commits by hand. Local LLM: read + triage + inbox only (AGENTS §4 already bars it from decisions) |
| 3 | **Git stale or unreachable** (remote behind, or clones diverged) | owner declares | `STATUS.md` header carries **`Canon clone: <machine>`**, set at the Mac move and whenever the owner switches. That clone wins; the other is rebased onto it by Tech (or by owner recipe) — never merged blind. If the remote is unreachable, work continues on the canon clone; push when it returns |

Tiers stack: 1+3 = CoS on the canon clone, owner commits, no push. 2+3 = failover assistant on the canon clone, everything stamped, owner commits.

## 3. Return protocol (Claude back / Tech back)
1. Tech: `git log` since last own commit; list every file touched under `FAILOVER` or `TECH DOWN`.
2. CoS: reconcile stamped `STATUS.md` rows and any failover proposals **before** any new work; strike the stamp.
3. Nothing a failover assistant wrote is canon until CoS has read it and the owner has ruled on anything decision-shaped — same as any proposal.

## 4. `FAILOVER.md` contents (to write if ruled)
Boot order (3 files) · permitted writes · the stamp format · forbidden actions · owner's manual git recipe (`git status` → `git add <paths>` → `git commit -m "<what> [FAILOVER]"` → `git push`) · "Canon clone" rule · return protocol pointer. Provider-neutral: no Claude-specific tooling, no `.claude/` dependence.

## 5. Queue row (Tech transcribes)
```
Q9 · Continuity: adopt the three tiers, `FAILOVER.md`, and the `Canon clone` header field · blocks: Mac move safety
  A: adopt   ← Chief of Staff
  B: adopt tier 3 only (canon clone rule); failover assistant handled ad hoc
```
