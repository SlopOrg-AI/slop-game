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
| E | commit-msg | a commit that does not name the surface that wrote it: `Surface: <tag>` |

All four are string scans over two files; stdlib only. Logic lives in
`checks.py` — the shell files are shims that find python.

**Check E and the `Surface:` trailer.** Three surfaces share one working tree and therefore one git identity — every commit is authored by the owner, and `git log --author` cannot separate them. The trailer is the only attribution a machine can read: `git log --format='%h %(trailers:key=Surface,valueonly)'`. Tags are the routing tags in `leads/README.md` (`cos sys content tech art level scenario mkt`), optionally `<tag>/N` when one lead runs two surfaces. Git-generated messages (merge, revert, fixup!, squash!) are exempt. It checks presence, never honesty — a surface can write the wrong tag, and only a reader catches that. Commits predating the rule are untouched: a `commit-msg` hook sees only the commit in flight.

A logged decision row is recognised as a table row starting `| D#.#` with at
least six columns. The three-column *deferred* table is deliberately not a
logged decision: `D5.24` sits there precisely because it has never been logged.
