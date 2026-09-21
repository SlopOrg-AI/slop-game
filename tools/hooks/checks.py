#!/usr/bin/env python3
"""Guard-rail checks for shinobi-v2 (D5.39).

Run by git through core.hooksPath -> tools/hooks/{pre-commit,commit-msg}.
Four checks, all string scans over two files. No dependencies.

  A  no duplicate D#.# row in design/decisions.md
  B  STATUS.md's advertised next-free D-number is not already used
     (only when the commit touches decisions.md or STATUS.md, so a stale
      board never blocks unrelated work)
  C  no .png under proposals/art/ except _contact-sheet.png and accepted/
  D  a commit that adds a D#.# row must name that number in its message

Escape hatch: git commit --no-verify. The hooks are a net, not a lock.
"""

import re
import subprocess
import sys

DECISIONS = "design/decisions.md"
BOARD = "STATUS.md"

# A logged decision row has six columns: ID | Acts on it | Decision |
# Rationale | Supersedes | Doc. The deferred table elsewhere in the file
# has three, and must not be mistaken for a logged decision - D5.24 lives
# there precisely because it is NOT logged.
DECISION_ROW = re.compile(r"^\|\s*\*{0,2}(D\d+\.\d+)\*{0,2}\s*\|")
MIN_PIPES = 6

NEXT_FREE = re.compile(r"Next free numbers:.*?D-number\s*\*{0,2}(D\d+\.\d+)", re.S)


def git(*args):
    """Run git, return stdout, or None when the command fails."""
    try:
        out = subprocess.run(
            ["git"] + list(args), capture_output=True, text=True, check=True
        )
        return out.stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def staged_paths():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACMR")
    return [p for p in (out or "").splitlines() if p]


def content(path, staged):
    """Staged version of a file if it is staged, else the HEAD version."""
    if staged:
        return git("show", ":" + path) or ""
    return git("show", "HEAD:" + path) or ""


def decision_ids(text):
    ids = []
    for line in text.splitlines():
        m = DECISION_ROW.match(line)
        if m and line.count("|") >= MIN_PIPES:
            ids.append(m.group(1))
    return ids


def as_tuple(d):
    major, minor = d[1:].split(".")
    return (int(major), int(minor))


def fail(check, message, fix):
    print("", file=sys.stderr)
    print("  guard rail %s (D5.39) refused this commit" % check, file=sys.stderr)
    print("  %s" % message, file=sys.stderr)
    print("  fix: %s" % fix, file=sys.stderr)
    print("", file=sys.stderr)
    return 1


def check_a(staged):
    ids = decision_ids(content(DECISIONS, DECISIONS in staged))
    seen, dupes = set(), []
    for d in ids:
        if d in seen and d not in dupes:
            dupes.append(d)
        seen.add(d)
    if dupes:
        return fail(
            "A - duplicate decision number",
            "%s appears on more than one logged row in %s." % (", ".join(dupes), DECISIONS),
            "two sessions logged the same number. Renumber the later one to the "
            "next free D-number and update STATUS.md.",
        )
    return 0


def check_b(staged):
    if DECISIONS not in staged and BOARD not in staged:
        return 0
    board = content(BOARD, BOARD in staged)
    m = NEXT_FREE.search(board)
    if not m:
        return 0  # board says nothing about numbers; not this hook's business
    advertised = m.group(1)
    ids = decision_ids(content(DECISIONS, DECISIONS in staged))
    if not ids:
        return 0
    highest = max(ids, key=as_tuple)
    if as_tuple(advertised) <= as_tuple(highest):
        return fail(
            "B - board advertises a used number",
            "%s says next free is %s, but %s is already logged in %s."
            % (BOARD, advertised, highest, DECISIONS),
            "set the next-free line past %s. A stale board is how two sessions "
            "claim one number." % highest,
        )
    return 0


def check_c(staged):
    bad = [
        p
        for p in staged
        if p.startswith("proposals/art/")
        and p.lower().endswith(".png")
        and not p.endswith("_contact-sheet.png")
        and "/accepted/" not in p
    ]
    if bad:
        return fail(
            "C - art binary policy (D5.28)",
            "staged raw generation(s): %s" % ", ".join(bad),
            "contact sheets and accepted boards only. git restore --staged <path>, "
            "or move the keeper under an accepted/ folder.",
        )
    return 0


def check_d(staged, message):
    if DECISIONS not in staged:
        return 0
    before = set(decision_ids(git("show", "HEAD:" + DECISIONS) or ""))
    after = decision_ids(content(DECISIONS, True))
    added = [d for d in after if d not in before]
    missing = [d for d in added if d not in message]
    if missing:
        return fail(
            "D - decision number not in the message",
            "this commit adds %s to %s; the message names none of them."
            % (", ".join(missing), DECISIONS),
            "put the D-number in the commit message. History has to be searchable "
            "by decision.",
        )
    return 0


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre-commit"
    staged = staged_paths()
    if mode == "commit-msg":
        path = sys.argv[2]
        with open(path, encoding="utf-8") as fh:
            message = fh.read()
        return check_d(staged, message)
    return check_a(staged) or check_b(staged) or check_c(staged)


if __name__ == "__main__":
    sys.exit(main())
