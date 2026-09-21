# tools/hooks — guard rails (D5.39)

Tracked, so every clone gets the same checks. `.git/hooks` is per-clone and
unversioned, which is the wrong shape for a repo two surfaces write.

**Enable, once per clone — including the Mac successor's:**

```
git config core.hooksPath tools/hooks
```

Disable: `git config --unset core.hooksPath`. Bypass one commit: `--no-verify`.

| Check | Hook | Refuses |
|---|---|---|
| A | pre-commit | the same `D#.#` on two logged rows in `design/decisions.md` |
| B | pre-commit | `STATUS.md` advertising a next-free D-number that is already used — only on commits touching `decisions.md` or `STATUS.md`, so a stale board never blocks unrelated work |
| C | pre-commit | a `.png` under `proposals/art/` that is not `_contact-sheet.png` and not under `accepted/` (D5.28, including `git add -f`) |
| D | commit-msg | a commit that adds a `D#.#` row without naming it in the message |

All four are string scans over two files; stdlib only. Logic lives in
`checks.py` — the shell files are shims that find python.

A logged decision row is recognised as a table row starting `| D#.#` with at
least six columns. The three-column *deferred* table is deliberately not a
logged decision: `D5.24` sits there precisely because it has never been logged.
