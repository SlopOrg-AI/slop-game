# PROTOCOL — how we work

Kept by Builder. **Two pages, hard.** A change to how we work is one dated line in §Changes, and must delete a line somewhere. Framework: `proposals/2026-09-21-clean-slate.md` (owner-approved, D260921.1-P).

The game is not in here. `design/` and `data/` are the game; `design/decisions.md` is the arbiter and outranks this file.

## 1. Roles

| Role | Owns the question | Runs on |
|---|---|---|
| **Owner** | everything. Decides and approves — **never commits, never merges** (D260921.5-P, D260921.6-P) | chat |
| **Designer** | what the game *is* — rules, ontology, direction, content | Claude Code, own clone |
| **Builder** | what runs it — engine, data schema, tools, git, this file | Claude Code, own clone |
| **Steward** | is the project organised — the board, the owner's queue, triage, digests | Claude Code, own clone |

Anything else is a **task**: a session with a prompt, output to `proposals/`. Cowork is the owner's read-only console; it never writes the repo.

**Build versus steer.** Where a thing has a mechanism underneath it, Builder builds and runs it; the role that uses it says what it should do.

## 2. Session contract

1. **Claim your role** — create `sessions/<role>.md`. Creating it is the claim; finding one is the collision. Over **3 hours** since `Last seen` it may be taken, said so in the file; otherwise **you are not that role** — ask the owner, who alone says who holds one. Not enforcement: any session can overwrite any claim. It buys seconds, not safety.

   ```markdown
   # Live session — `builder`
   - **Role**: builder · **Kind**: lead | subordinate of <lead>
   - **Session**: what you are, and which clone you are in
   - **Claimed**: 2026-09-21 12:21 · **Last seen**: 2026-09-21 12:21
   ```
2. **Read §Changes below**, from your last session's date down. Then your own charter (`roles/<role>.md`) and `STATUS.md`.
3. **`git pull`.** Work only in your own clone.
4. **Commit as you go. Push before you stop.** Work that never left your machine is not in the record.
5. **Leave your `STATUS.md` section true**: state · next · asks.
6. **Release the claim** at close — delete the file.

## 3. Git is the channel

- **One clone per role.** You write your clone and nobody else's. A conflict is a visible merge; a shared tree is a silent overwrite, which is what it did on 2026-09-20.
- **Identity is per clone**, set at creation: `git config user.name "Builder (Claude Code)"` — and the **machine account's** no-reply as the email, never the owner's (D260921.5-P). The name separates the roles for `git log --author`; the email says this was an agent, not the owner. Rail F refuses the mix.
- **Guard rails are per clone too:** `git config core.hooksPath tools/hooks` on every clone, including cloud ones. A clone without it has none.
- **Stage by path. Never `git add -A`.** A wrong name in history is permanent and invisible to every check.
- **Never rewrite pushed history.** Fix a bad commit with another commit.

**What binds, and what does not.** The ruleset is real and has no bypass actors: no direct push to `main`, no force-push, no deletion, `rails` must pass — for every account including the owner's. **Not enforced: that a human looked.** Approvals are **0** by decision (D260921.8-P), so review here is a **convention**. The rails are a net, not a lock — a pull request that weakens `checks.py` is checked by its own weakened copy — and `CODEOWNERS` is inert while code-owner review is off. What remains is attributable history, and the owner reading it.

**What the rails refuse** (`tools/hooks/`): a duplicate decision ID · a raw `.png` under `proposals/art/` that is neither a contact sheet nor under `accepted/` · a commit adding a decision row whose message does not name that ID · a log whose rows no longer parse · a commit authored by the owner.

## 4. Decisions

- A **game** decision (tags S · A · C) is **the owner's words plus a date**, logged by the session he was in. A **mechanism** decision (P · E) is the **owning role's**, logged the same way and attributed to the role, revocable by him (D260921.7-P).
- ID is `D<yymmdd>.<n>` with a tag: `D260921.3-P` — P process · S rules · A art · C content · E engine. Scan the log for the last number used that day. **No session needs another to number anything.**
- **No agent attributes a decision to the owner without his words in that same session.** And no role widens what it may decide — §1 and this section are the owner's alone.
- Later entry wins. If a document disagrees with the log, the document is wrong.

## 5. Asking, and being asked

- **Between roles:** a row in your own `STATUS.md` section under *asks*. No other channel, and no role relays for another.
- **To the owner:** a file in `queue/`, one per question: question, options with trade-offs, recommendation, what it blocks.
- **The owner's words** live in the decision row and in the queue file they answer (D260921.2-P). There is no `inbox/`; an answer in a queue file *is* the instruction.

## 6. Budgets

| File | Limit |
|---|---|
| `PROTOCOL.md` | 2 pages |
| `STATUS.md` | 1 page |
| `roles/<role>.md` | 1 page each |
| A fresh session, before it works | ≤ 20 KB |

A fresh session's required reading is `CLAUDE.md` + this file + its charter + `STATUS.md`. `AGENTS.md` is looked up, not loaded.

## Changes

- **2026-09-21** Approvals stay at 0 (D260921.8-P): review here is a convention and §3 says so, because an approval requirement and D260921.7-P cannot both hold — GitHub has no per-path approval count
- **2026-09-21** Roles decide their own mechanism (D260921.7-P): game decisions S/A/C stay the owner's, P/E become the owning role's, and no role may widen its own remit
- **2026-09-21** `CLAUDE.md` stops auto-loading `AGENTS.md`; required reading becomes lookup-on-demand, halving what a session pays before it works
- **2026-09-21** Agents merge, too (D260921.6-P): a merge commit carries the clicker's name, so the owner approves and an agent merges — his name then means "he approved this", nothing else
- **2026-09-21** Agents commit as the machine account and the owner does not commit at all (D260921.5-P); §1 and the §3 identity line inverted, rail F added. The `Surface:` sentence goes — §Changes already records it
- **2026-09-21** `sessions/README.md` retired into §2.1 (D260921.1-P); `inbox/` struck from §5 (D260921.2-P) — owner's words live in the decision row and the queue file
- **2026-09-21** Tech lead becomes **Builder**; `leads/systems/tech.md` deprecated, charter is `roles/builder.md`
- **2026-09-21** One clone per role; identity set per clone. `Surface:` trailer retired — `git log --author` does that job now
- **2026-09-21** Guard rail B retired: date IDs have no next-free counter, and it would have refused every commit under the new scheme
- **2026-09-21** Decision IDs become `D<yymmdd>.<n>-<TAG>`; local refs, promotion, ratification and next-free counters all go
- **2026-09-21** Asks between roles move to `STATUS.md` sections; `## For`/`## From` channels, `bridge/` and the handshake retire
