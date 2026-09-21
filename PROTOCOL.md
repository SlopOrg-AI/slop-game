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

**Build versus steer.** Where a thing has a mechanism underneath it, Builder builds and runs it; the role that uses it says what it should do. The doorbell is the worked example (`queue/_DOORBELL.md`).

## 2. Session contract

1. **Claim your role** — create `sessions/<role>.md`. Creating it is the claim; finding one is the collision. Past **3 hours** since `Last seen` it is presumed dead and may be taken, said so in the file; otherwise it names someone who is not you, so **you are not that role** — ask the owner, who alone says who holds one. Not enforcement: any session can overwrite any claim. It buys seconds, not safety.

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

- **One clone per role.** You write your clone and nobody else's. A conflict is a merge, which is visible; a shared tree gives you a silent overwrite, which is what it did on 2026-09-20.
- **Identity is per clone**, set at creation: `git config user.name "Builder (Claude Code)"` — and the **machine account's** no-reply as the email, never the owner's (D260921.5-P). The name separates the roles for `git log --author`; the email says this was an agent, not the owner. Rail F refuses the mix.
- **Guard rails are per clone too:** `git config core.hooksPath tools/hooks` on every clone, including cloud ones. A clone without it has none.
- **Stage by path. Never `git add -A`.** A wrong name in history is permanent and invisible to every check.
- **Never rewrite pushed history.** Fix a bad commit with another commit.

**What the rails refuse** (`tools/hooks/`): a duplicate decision ID · a raw `.png` under `proposals/art/` that is not a contact sheet or under `accepted/` · a commit adding a decision row whose message does not name that ID · a log whose rows no longer parse, so a blind checker refuses rather than passing everything · a commit authored by the owner, who does not commit.

## 4. Decisions

- A decision is **the owner's words plus a date**, logged by the session the owner was in.
- ID is `D<yymmdd>.<n>` with a tag: `D260921.3-P` — P process · S rules · A art · C content · E engine. Scan the log for the last number used that day. **No session needs another to number anything.**
- No agent logs a decision without the owner's words in that same session.
- Later entry wins. If a document disagrees with the log, the document is wrong.

## 5. Asking, and being asked

- **Between roles:** a row in your own `STATUS.md` section under *asks*. There is no other channel, and no role relays for another — peers read each other's sections directly.
- **To the owner:** a file in `queue/`, one per question: the question, options with trade-offs, your recommendation, what it blocks. The doorbell surfaces unanswered ones.
- **The owner's words** live in the decision row and in the queue file they answer (D260921.2-P). There is no `inbox/`; an answer in a queue file *is* the instruction.

## 6. Budgets

| File | Limit |
|---|---|
| `PROTOCOL.md` | 2 pages |
| `STATUS.md` | 1 page |
| `roles/<role>.md` | 1 page each |
| A fresh session, before it works | ≤ 20 KB |

The Tech lead brief reached 50 KB by being a charter, a board, a channel and a logbook at once. That is what these prevent.

## Changes

- **2026-09-21** Agents merge, too (D260921.6-P): a merge commit carries the clicker's name, so the owner approves and an agent merges — his name then means "he approved this", nothing else
- **2026-09-21** Agents commit as the machine account and the owner does not commit at all (D260921.5-P); §1 and the §3 identity line inverted, rail F added. The `Surface:` sentence goes — §Changes already records it
- **2026-09-21** `sessions/README.md` retired into §2.1 (D260921.1-P); `inbox/` struck from §5 (D260921.2-P) — owner's words live in the decision row and the queue file
- **2026-09-21** Tech lead becomes **Builder**; `leads/systems/tech.md` deprecated, charter is `roles/builder.md`
- **2026-09-21** One clone per role; identity set per clone. `Surface:` trailer retired — `git log --author` does that job now
- **2026-09-21** Guard rail B retired: date IDs have no next-free counter, and it would have refused every commit under the new scheme
- **2026-09-21** Decision IDs become `D<yymmdd>.<n>-<TAG>`; local refs, promotion, ratification and next-free counters all go
- **2026-09-21** Asks between roles move to `STATUS.md` sections; `## For`/`## From` channels, `bridge/` and the handshake retire
- **2026-09-21** Steward steers the doorbell, Builder builds it; the doorbell enables the rails before it commits
- **2026-09-21** Builder no longer edits another role's brief at all; `## Commit me` stays only until every role is on Claude Code with its own clone, then goes with the watcher
