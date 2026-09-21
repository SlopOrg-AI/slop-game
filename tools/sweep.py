#!/usr/bin/env python3
"""Cross-surface commit sweep (D5.39).

Cowork can write this folder; only Claude Code has git. Work written by
another surface sits untracked until a Tech session notices. This sweeps it.

The test is the PATH, never the content (commit-sweep.md A.1). Nothing here
reads a file to decide whether it counts - that judgement is not Tech's
(D5.38), and a sweep that cannot launder a rule violation is safe to run.

  plan (default)   python tools/sweep.py
  commit           python tools/sweep.py --commit --surface Cowork \
                       --summary "coherence pass and handoff"

Flags are never committed and never dropped: they print, and the Tech session
files them under "For Chief of Staff" in leads/systems/tech.md (A.2).
Run at session open (other surfaces' leftovers) and close (its own).
"""

import argparse
import subprocess
import sys

COMMIT = "commit"   # swept
CUSTODY = "custody"  # Tech's hand already, under D5.38 - not a sweep
OWN = "tech-own"    # Tech's own files; commits as its own work, not a sweep
FLAG = "flag"       # never swept

# Cowork is the only other writing surface today. If that changes, add a row.
OTHER_SURFACE_BRIEF = "leads/chief-of-staff.md"
TECH_BRIEF = "leads/systems/tech.md"


def classify(path):
    if path == "STATUS.md":
        return CUSTODY, "authored by Chief of Staff, typed by Tech (D5.38) - not a sweep"
    if path == "design/decisions.md":
        return FLAG, "a D-number is an owner act; it rides with the session that logged it (A.5)"
    if path.startswith("proposals/") or path.startswith("inbox/"):
        return COMMIT, "non-canon by definition; nothing here can be a decision"
    if path == OTHER_SURFACE_BRIEF:
        return COMMIT, "the writing surface's own brief (single-writer, D5.27)"
    if path == TECH_BRIEF:
        return OWN, "Tech's own brief"
    if path.startswith("leads/"):
        return FLAG, "another lead's brief - committing it would ratify a write that broke D5.27"
    if path.startswith(("design/", "data/", "demo/")):
        return FLAG, "changes only on an owner instruction in the session doing the edit (rule 5)"
    if path.startswith("tools/") or path in (".gitignore", ".gitattributes") or path.startswith(".claude/"):
        return OWN, "Tech owns it; commits as its own work"
    return FLAG, "not in the sweep table"


def git(*args, check=True):
    # UTF-8 explicitly; the locale default is cp1252 on Windows and raises on
    # the em-dashes in these documents.
    return subprocess.run(
        ["git"] + list(args), capture_output=True, check=check,
        encoding="utf-8", errors="replace",
    )


def changed():
    out = git("status", "--porcelain").stdout.splitlines()
    paths = []
    for line in out:
        if not line.strip():
            continue
        path = line[3:].strip().strip('"')
        if " -> " in path:  # rename
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return paths


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true", help="stage and commit the COMMIT rows")
    ap.add_argument("--surface", help="which surface wrote the work; required with --commit")
    ap.add_argument("--summary", default="", help="short phrase for the commit subject")
    args = ap.parse_args()

    buckets = {COMMIT: [], CUSTODY: [], OWN: [], FLAG: []}
    for path in changed():
        kind, why = classify(path)
        buckets[kind].append((path, why))

    if not any(buckets.values()):
        return 0  # an empty sweep is silent (A.5)

    for kind, label in ((COMMIT, "SWEEP"), (CUSTODY, "CUSTODY"), (OWN, "TECH'S OWN"), (FLAG, "FLAG")):
        for path, why in buckets[kind]:
            print("%-11s %-52s %s" % (label, path, why))

    if not args.commit:
        print("\nplan only. --commit --surface <name> to sweep.")
        return 0

    if not buckets[COMMIT]:
        print("\nnothing to sweep.")
        return 0
    if not args.surface:
        print("\n--surface is required: attribution must name who wrote it (A.3).", file=sys.stderr)
        return 2

    paths = [p for p, _ in buckets[COMMIT]]
    git("add", "--", *paths)
    subject = "%s: %s (not authored by Tech)" % (
        args.surface, args.summary or "swept %d file(s)" % len(paths))
    body = [
        "",
        "Commit sweep, D5.39. Swept by path, not by content; nothing here was",
        "read to decide whether it counted.",
        "",
    ] + ["  " + p for p in paths]
    if buckets[FLAG]:
        body += ["", "Flagged, not committed (see leads/systems/tech.md, For Chief of Staff):"]
        body += ["  %s - %s" % (p, why) for p, why in buckets[FLAG]]
    body += ["", "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"]

    done = git("commit", "-m", subject, "-m", "\n".join(body), check=False)
    print(done.stdout or "", done.stderr or "")
    if done.returncode != 0:
        # A hook refused a swept commit: stop, report, change nothing else.
        print("sweep stopped: a guard rail refused the commit. Nothing retried.", file=sys.stderr)
        return done.returncode
    return 0


if __name__ == "__main__":
    sys.exit(main())
