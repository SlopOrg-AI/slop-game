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
  E  every commit names the surface that wrote it: "Surface: <tag>"

Escape hatch: git commit --no-verify. The hooks are a net, not a lock.
"""

import re
import subprocess
import sys

DECISIONS = "design/decisions.md"
BOARD = "STATUS.md"

# A logged decision row starts with its ID and has at least five columns.
# The three-column deferred table must not be mistaken for one - D5.24 lives
# there precisely because it is NOT logged.
#
# The ID may carry an interested-party suffix (D5.41-EP). Only the number is
# captured: under "the log stays single", D5.41-EP and D5.41-P are the same
# number twice and check A should say so.
DECISION_ROW = re.compile(r"^\|\s*\*{0,2}(D\d+\.\d+)(?:-[A-Za-z]+)?\*{0,2}\s*\|")
# Anything that merely looks like a decision row. If this finds rows and
# DECISION_ROW finds none, the parser has gone blind and must say so rather
# than report a clean file - see check_blind().
LOOKS_LIKE_ROW = re.compile(r"^\|\s*\*{0,2}D\d")
MIN_PIPES = 6

NEXT_FREE = re.compile(r"Next free numbers:.*?D-number\s*\*{0,2}(D\d+\.\d+)", re.S)

# Check E. Three surfaces share one working tree, so they share one git
# identity: every commit here is authored by the owner and `git log --author`
# cannot tell us apart. The trailer is the only machine-readable attribution
# available, and it survives the move to one clone per surface rather than
# being replaced by it.
#
# The vocabulary is the routing tags in leads/README.md - deliberately reused
# rather than invented, because two lists drift and then both must be kept in
# step. An optional /N suffix distinguishes two surfaces serving one lead.
SURFACES = ("cos", "sys", "content", "tech", "art", "level", "scenario", "mkt")
SURFACE_LINE = re.compile(r"^Surface:[ 	]*(\S+)[ 	]*$", re.M)
SURFACE_LOOSE = re.compile(r"^[ 	]*surface[ 	]*:", re.M | re.I)
GENERATED = ("merge ", "revert ", "fixup!", "squash!")
# A to D come from D5.39. E does not - it is tonight's trailer ruling, unlogged.
E_ORIGIN = "owner 2026-09-20, not yet logged"


def git(*args, required=True):
    """Run git and return stdout.

    UTF-8 explicitly: the default is the locale encoding, which is cp1252 on
    Windows and raises on the em-dashes in these documents. That bug made the
    first version of this hook fail OPEN - it crashed in a reader thread, the
    checks saw empty content, and the commit went through. A guard rail that
    cannot read its input must refuse, never shrug.
    """
    try:
        out = subprocess.run(
            ["git"] + list(args),
            capture_output=True,
            check=True,
            encoding="utf-8",
            errors="replace",
        )
        return out.stdout
    except (subprocess.CalledProcessError, FileNotFoundError, OSError) as exc:
        if required:
            raise RuntimeError("git %s failed: %s" % (" ".join(args), exc))
        return None


def staged_paths():
    out = git("diff", "--cached", "--name-only", "--diff-filter=ACMR")
    return [p for p in (out or "").splitlines() if p]


def content(path, staged):
    """Staged version of a file if it is staged, else the HEAD version.

    A file absent from HEAD (new, unstaged) is genuinely empty here, so that
    lookup is optional; a staged file must be readable or we refuse.
    """
    if staged:
        return git("show", ":" + path)
    return git("show", "HEAD:" + path, required=False) or ""


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


def fail(check, message, fix, origin="D5.39"):
    print("", file=sys.stderr)
    print("  guard rail %s (%s) refused this commit" % (check, origin), file=sys.stderr)
    print("  %s" % message, file=sys.stderr)
    print("  fix: %s" % fix, file=sys.stderr)
    print("", file=sys.stderr)
    return 1


def check_blind(staged):
    """Refuse when the log has rows we can no longer parse.

    Checks A, B and D all read DECISION_ROW. On 2026-09-20 the log was
    reformatted to carry party suffixes and the pattern matched nothing -
    three rails passed every commit while seeing an empty file. A guard rail
    that cannot read its input must refuse, not report all clear.
    """
    text = content(DECISIONS, DECISIONS in staged)
    loose = sum(1 for line in text.splitlines()
                if LOOKS_LIKE_ROW.match(line) and line.count("|") >= MIN_PIPES)
    if loose and not decision_ids(text):
        return fail(
            "blind - the log changed shape",
            "%d rows in %s look like decisions and none of them parse."
            % (loose, DECISIONS),
            "checks A, B and D all read that pattern, so they would pass "
            "everything while seeing nothing. Update DECISION_ROW in "
            "tools/hooks/checks.py to the log's new shape, in the same commit "
            "that changes the log.",
        )
    return 0


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
    before = set(decision_ids(git("show", "HEAD:" + DECISIONS, required=False) or ""))
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


def check_e(message):
    first = (message.lstrip().splitlines() or [""])[0].lower()
    if first.startswith(GENERATED):
        return 0  # git wrote this message, not an agent

    m = SURFACE_LINE.search(message)
    if not m:
        hint = (
            "you wrote it in the wrong case or shape - the exact spelling is "
            "'Surface: <tag>' on its own line"
            if SURFACE_LOOSE.search(message)
            else "add a last line: Surface: <tag>"
        )
        return fail(
            "E - no Surface: trailer",
            "this commit does not say which surface wrote it.",
            "%s. Tags are the routing tags in leads/README.md: %s. "
            "Three surfaces share one git identity here, so this line is the only "
            "attribution a machine can read." % (hint, ", ".join(SURFACES)),
            origin=E_ORIGIN,
        )

    tag = m.group(1)
    base = tag.split("/", 1)[0]
    if base not in SURFACES:
        return fail(
            "E - unknown surface tag",
            "'%s' is not a surface tag." % tag,
            "use one of: %s (optionally '<tag>/N' when one lead runs two surfaces). "
            "The list is the routing tags in leads/README.md; if a new surface is real, "
            "that file and this hook change together." % ", ".join(SURFACES),
            origin=E_ORIGIN,
        )
    return 0


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre-commit"
    staged = staged_paths()
    if mode == "commit-msg":
        path = sys.argv[2]
        with open(path, encoding="utf-8") as fh:
            message = fh.read()
        return check_d(staged, message) or check_e(message)
    return check_blind(staged) or check_a(staged) or check_b(staged) or check_c(staged)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:  # fail closed: a broken check refuses the commit
        print("", file=sys.stderr)
        print("  guard rails (D5.39) could not run: %s" % exc, file=sys.stderr)
        print("  refusing the commit. Fix tools/hooks/checks.py, or use", file=sys.stderr)
        print("  --no-verify deliberately if you know why it broke.", file=sys.stderr)
        print("", file=sys.stderr)
        sys.exit(1)
