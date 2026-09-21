# Proposal — repo guard rails: versioned git hooks + `.claude/settings.json`

**Produced by:** Tech (Claude Code), 2026-09-20 · **Targets:** `tools/hooks/` (new), `.claude/settings.json` (new), `leads/systems/tech.md` · **Proposes:** three mechanical checks and two permission rules · **Supersedes:** nothing. **Status:** **PROMOTED D5.39** (2026-09-20) — owner ruled A: all four checks, both permission rules. Installed this session.

---

## 1. Evidence from this session, not theory

| # | What happened | Rule it broke | A rule can catch it? |
|---|---|---|---|
| 1 | Two surfaces both read **D5.27** as next free. Admin logged D5.27/D5.28; a concurrent Cowork proposal reserved D5.27 for Systems. | `decisions.md` is the arbiter (AGENTS §1.2) | **Yes** — duplicate-ID scan, and `STATUS.md` "next free" vs the log's max |
| 2 | ~10 MB of raw generations entered history as a default, not a decision (conflict #3, closed by D5.28) | D5.28 | **Yes** — refuse staged PNGs under `proposals/art/` that aren't a contact sheet or under `accepted/` |
| 3 | `git add -A` swept a Systems session's work into an unrelated commit; it had to be split back out | D5.27 (stage by path) | **No** — a hook cannot know whose work it is. Stays social. |
| 4 | `STATUS.md` overwritten twice by two writers | D5.27 (single writer) | **No** — no identity at commit time. Stays social. |

Two of four are mechanisable. The other two are why D5.27 exists as a written rule.

## 2. Versioned hooks, not `.git/hooks`

`.git/hooks` is per-clone and unversioned: Cowork's surface would never get it, which is exactly backwards — the concurrency is the thing being guarded. Use a tracked folder:

```
git config core.hooksPath tools/hooks
```

One command, per clone, reversible with `git config --unset core.hooksPath`. Both surfaces then run the same checks from the same tracked source. `--no-verify` remains the escape hatch.

## 3. The checks

### `tools/hooks/pre-commit` — content

| Check | Fails when | Why |
|---|---|---|
| **A. Duplicate D-number** | `design/decisions.md` has two rows with the same `D#.#` | The collision in §1 #1, caught at the moment it would enter history |
| **B. Board vs log** | `STATUS.md` "Next free numbers" D-value ≤ the highest `D#.#` in `decisions.md` | The board is how every surface learns what's free; stale board = next collision |
| **C. Art binary policy** | a staged `.png` under `proposals/art/` is neither `_contact-sheet.png` nor under `accepted/` | D5.28, including against `git add -f` |

### `tools/hooks/commit-msg` — message

| Check | Fails when | Why |
|---|---|---|
| **D. D-number in the message** | `design/decisions.md` is staged with an added `D#.#` row and the message doesn't name that number | AGENTS §4 / D5.27 commit discipline, currently honour-system |

All four are string scans over two files. No dependencies beyond the Python already required by `tools/`.

## 4. `.claude/settings.json` — two permission rules

Claude Code only; Cowork is unaffected (a second reason the hooks matter more than this file).

| Rule | Effect |
|---|---|
| `deny` Write/Edit on `sources/**` | `sources/` is read-only evidence (AGENTS §1.7). Currently nothing but discipline stops an agent editing it |
| `ask` on Write/Edit to `design/decisions.md` | The arbiter file gets an explicit confirmation every time, even when the owner is in session |

Not proposed: an allowlist of read-only Bash commands. It reduces prompts but widens what runs unattended; worth a separate decision.

## 5. What this costs

- A blocked commit interrupts the owner. All four checks are local string scans (milliseconds) and each failure message names the file, the line and the fix.
- `--no-verify` bypasses everything — deliberate. The hooks are a net, not a lock.
- Checks B and D assume the current shapes of the `STATUS.md` header line and the `decisions.md` table. If those change, the hook fails loudly rather than silently passing; it is a tracked file and gets fixed like any other.

## 6. For the owner

1. Install: `git config core.hooksPath tools/hooks` in this clone, and say so in the other surface's clone too.
2. Checks A–D as scoped above, or a subset — **Tech's read:** all four; A and B are the ones with evidence behind them tonight.
3. `.claude/settings.json`: both rules, or `sources/**` only.
4. No D-number needed — this is tooling, not design. Log one only if the record should say when guard rails went in.
