# Builder — state · next · asks

**Clone:** `C:\Claude\shinobi-v2` · **Identity:** `Builder (Claude Code)` <`…+sloporgAI@…`> ·
**Updated:** 2026-09-21, by `builder-260921-c` at session close · **seat released**

## Start here if you are the next Builder

**Auth is already right. Do not change it.** `gh` is authenticated as **`sloporgAI`**;
`chris-egan` is also in the keyring and **switching to it is the anomaly rail F exists to
catch** (`D260921.5-P`). Check with `gh api user --jq .login` before your first push.

**Two files in this clone are uncommitted and are not yours** — `queue/_DOORBELL.md` and
`sessions/cos.md`, blob hashes `64d29e3` / `b75ace6`, left by a session two ahead of you.
`A260921.8` is unruled. **Never `git reset --hard` in this clone** — it destroyed them once;
use `git pull --ff-only`.

**One thing blocks the next piece of work**, and it is the owner's: the machine-account token
needs **Workflows: Read and write**. Without it `.github/workflows/` is unwritable by anyone,
because the owner does not commit either. That blocks the Godot check.

## state

**Host configuration, the identity model, and the rails are done and demonstrated.**

- Ruleset `23775959` active, **zero bypass actors**: pull request required, `rails` required
  and strict, no force-push, no deletion — binding on every account.
- **Agents act as the machine account** (`D260921.5-P`). Its token has Contents and Pull
  requests write, **no admin**, so the ruleset genuinely binds an agent rather than being a
  convention it chooses to respect. Agents also merge; the owner only approves
  (`D260921.6-P`).
- **Rail F** refuses any non-merge commit authored by the owner. Proven by deliberate
  failure in real CI, not just by a passing run — PR #9 was built to go red and did, citing
  the offending SHA. It was then closed and its branch deleted.
- **Roles decide their own mechanism** (`D260921.7-P`). Game decisions — tags S, A, C — are
  the owner's. P and E are yours, attributed to the role and revocable by him. You may not
  amend `PROTOCOL.md` §1 or §4, or widen what you are allowed to decide.
- **Review is a convention, not a control** (`D260921.8-P`) — approvals are 0 by decision,
  and `PROTOCOL.md` §3 says what binds and what does not. `CODEOWNERS` is inert while
  code-owner review is off. Nothing mechanically stops an agent weakening the rails;
  `checks.py` is an ordinary repo file and a pull request is checked by its own copy of it.
- **Onboarding halved** — 22.5 KB → 14.6 KB, by stopping `CLAUDE.md` auto-loading
  `AGENTS.md`. Budgets now measure context loaded, not file size (`D260921.9-P`).

**Decisions logged today:** `D260921.4-P` … `D260921.9-P`. Next free is `D260921.10`.

## next

**The Godot check** — the original objective of both handovers, and still the only thing in
this repo that would fail when the *game* is wrong. Blocked on the Workflows grant above.
`proposals/2026-09-21-scheduler.md` is the other specced-but-unbuilt piece.

## not finished

- **Archive pass** on `leads/`, `inbox/`, `bridge/` — held on `A260921.9`, deliberately. The
  implementation review §5 says check what points *only* at what is being archived, and
  `leads/` holds the sole live pointer to **C23**.
- **Scheduler** — specced, not built, by the owner's halt.

## asks

- `A260921.9 → designer` · **Do `sys.7` and `sys.8` still mean anything?** Nine refs recorded
  in briefs and never promoted; `D260921.1-P` retired local refs so nothing will promote them.
  *Blocks:* archiving `leads/`. Detail: `status/designer.md` #7.
- `A260921.11 → designer` · **`AGENTS.md` §2 and §4 cite retired machinery** — `D5.44-EP`
  local refs, the Tech seat, the Project mirror. Harmless to Claude Code, which no longer
  loads that file; a platform reading it whole would act on stale rules.
- `A260921.10 → owner` · Three exposure findings, deferred by him. Issue **#12** is a stray
  probe of mine needing closure. `proposals/2026-09-21-machine-account-exposure.md`.
