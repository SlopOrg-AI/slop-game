#!/usr/bin/env python3
"""Guard-rail checks for shinobi-v2 (D5.39).

Run by git through core.hooksPath -> tools/hooks/{pre-commit,commit-msg}.
Four checks, all string scans over two files. No dependencies.

  A  no duplicate D#.# row in design/decisions.md
  B  RETIRED 2026-09-21 - date-based IDs (D260921.n) have no next-free
     counter to go stale, and a board still advertising a D5.x number reads
     as LOWER than any date ID, so the check would have refused every commit
     from the day the new scheme started. Deleted rather than ported.
  C  no .png under proposals/art/ except _contact-sheet.png and accepted/
  D  a commit that adds a D#.# row must name that number in its message
  E  RETIRED 2026-09-21 - each clone now sets its own git identity, so
     `git log --author` separates the roles and the trailer is redundant.

Modes: pre-commit, commit-msg, and `ci <base-sha> <head-sha>` (D260921.3-P),
which runs A and the blind check as a required status check so the rails
bind a clone that never ran `git config core.hooksPath`.

Escape hatch: git commit --no-verify. The hooks are a net, not a lock.
"""

import re
import subprocess
import sys

DECISIONS = "design/decisions.md"
BOARD = "STATUS.md"

# Rail F. Attribution is the control now (owner, 2026-09-21: "audit / review
# should flag unexpected chris-egan commits which should not be the norm if
# everything is working"). Agents authenticate and commit as the machine
# account, so an owner-authored commit inside an agent's pull request means
# either the owner worked in an agent clone or an agent switched auth back to
# his credential. Both are worth seeing; neither should be routine.
OWNER_EMAILS = (
    "chris-egan@users.noreply.github.com",
    "51842005+chris-egan@users.noreply.github.com",
)
OWNER_LOGIN = "chris-egan"
F_ORIGIN = "D260921.5-P"

# A logged decision row starts with its ID and has at least five columns.
# The three-column deferred table must not be mistaken for one - D5.24 lives
# there precisely because it is NOT logged.
#
# The ID may carry a tag suffix (D5.41-EP, D260921.1-P) and may be either
# scheme: D5.41 or the date form D260921.1 from the clean-slate plan. Only the
# number is captured, so two rows sharing one number read as a duplicate.
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


def range_paths(base, head):
    """Paths a pull request touches, for the CI rail (D260921.3-P).

    Three-dot: what the PR side added since the merge base, not everything
    that landed on main meanwhile. The file contents the checks read come from
    SOURCE (the head revision), not from the index, so the rail does not depend
    on the runner having staged anything.
    """
    out = git("diff", "--name-only", "--diff-filter=ACMR", "%s...%s" % (base, head))
    return [p for p in (out or "").splitlines() if p]


# Set by the ci mode to the revision under test. The hooks leave it None and
# keep reading the index, which is what a pre-commit rail must judge. CI has no
# meaningful index -- depending on one made the rail pass a file it had not
# read, which is the same failure check_blind() exists to refuse.
SOURCE = None


def content(path, staged):
    """The version of a file this run is judging.

    SOURCE when the caller named a revision, else the staged version if it is
    staged, else HEAD. A file absent from the revision is genuinely empty here,
    so that lookup is optional; a staged file must be readable or we refuse.
    """
    if SOURCE is not None:
        return git("show", "%s:%s" % (SOURCE, path), required=False) or ""
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


def check_f(base, head):
    """Refuse commits authored by the owner. He does not commit (D260921.5-P).

    The first version of this rail only refused them in pull requests opened by
    someone else, because it assumed the owner sometimes commits himself. He
    ruled that he does not, which removes the carve-out and with it the hole:
    an agent could have opened nothing and simply committed as him. Now there
    is no condition -- an owner-authored commit is wrong wherever it appears.

    That also drops the dependency on the Actions event payload and on branch
    naming, so there is less to be wrong about and nothing to evade.

    Merge commits are excluded: GitHub authors those as whoever clicks merge,
    which is a review action rather than authorship. If the owner is to stop
    appearing in the history entirely, agents have to do the merging -- that is
    a ruling, not something this rail should quietly decide.
    """
    out = git("log", "--no-merges", "--format=%h %ae", "%s..%s" % (base, head))
    bad = [
        ln for ln in (out or "").splitlines()
        if ln.strip() and ln.split(" ", 1)[-1].strip().lower() in OWNER_EMAILS
    ]
    if bad:
        return fail(
            "F - owner-authored commit",
            "the owner does not commit, but these are authored by him: %s"
            % "; ".join(bad),
            "agents commit as the machine account. Check `git config user.email` "
            "in this clone; it should be the machine account no-reply address.",
            origin=F_ORIGIN,
        )
    return 0


def check_blind_or_a_or_c(paths):
    """The tree-level rails, shared by the commit hook and CI."""
    return check_blind(paths) or check_a(paths) or check_c(paths)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "pre-commit"
    if mode == "ci":
        # Check D is deliberately absent here. It reads a commit message, and
        # PROTOCOL 3 forbids rewriting pushed history - so a CI failure on a
        # bad message would be unfixable except by force. It stays a local
        # rail, where it can still be obeyed.
        global SOURCE
        base, head = sys.argv[2], sys.argv[3]
        SOURCE = head
        return check_blind_or_a_or_c(range_paths(base, head)) or check_f(base, head)
    staged = staged_paths()
    if mode == "commit-msg":
        path = sys.argv[2]
        with open(path, encoding="utf-8") as fh:
            message = fh.read()
        return check_d(staged, message)
    return check_blind_or_a_or_c(staged)




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
