#!/usr/bin/env python3
"""Watch the lead briefs for a commit request and act on it.

Cowork and the shell-less Tech session write this tree but have no git, so
their work sits untracked until someone looks. On 2026-09-20 that was nine
files and ten decision entries, for over an hour.

This closes the gap in the only direction the architecture allows: while a
session with a shell is live, it watches. Another surface asks by adding a
block to **its own brief**; the watcher picks it up within seconds, commits
exactly what the block names, and reports what it refused.

    python tools/watch.py                  # poll every 20s until stopped
    python tools/watch.py --once
    python tools/watch.py --interval 10

THE REQUEST — a section in the requesting lead's OWN brief:

    ## Commit me
    Message: log D5.45-D5.51 and the queue verdicts

    design/decisions.md
    STATUS.md

ATTRIBUTION COMES FROM THE FILE, NOT FROM A FLAG. The brief the block sits in
names the surface: leads/chief-of-staff.md is cos, leads/systems/tech.md is
tech, leads/direction/art.md is art. Nobody declares who they are and nobody
guesses - the earlier version took a --surface argument and three commits were
misattributed because the guess was made from a stale assumption.

WHY A REQUEST AND NOT JUST WATCHING THE TREE: a watcher that committed whatever
appeared would commit half-written files. The block is the author saying "this
is a good point", which is the one thing a watcher cannot know.

WHAT IT WILL NOT DO: the sweep table (D5.39 A.1) refuses design/**, data/**,
demo/** and another lead's brief, because an uncommitted change there is either
someone else's job or a rule violation. A block naming those paths is different:
it is the authoring surface asking, in writing, for its own work. That is the
authorisation A.1's blanket refusal stands in for. Paths not named are still
refused, and every guard rail still runs on the commit.

The watcher removes the block after a successful commit - it is a request, not
a document. That is the one edit any surface may make to another's brief, and
it exists because the alternative is the request firing twice.
"""

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING = re.compile(r"^##\s+Commit me\s*$", re.M)
# The brief's path is the attribution. No surface declares itself here.
BRIEFS = {
    "leads/chief-of-staff.md": "cos",
    "leads/systems.md": "sys",
    "leads/systems/tech.md": "tech",
    "leads/systems/content.md": "content",
    "leads/direction/art.md": "art",
    "leads/direction/level.md": "level",
    "leads/direction/scenario.md": "scenario",
    "leads/marketing.md": "mkt",
}


def git(*args, check=True):
    return subprocess.run(
        ["git", "-C", str(ROOT)] + list(args),
        capture_output=True, check=check, encoding="utf-8", errors="replace",
    )


def find_block(text):
    """-> (message, [paths], start, end) for the first '## Commit me' section."""
    m = HEADING.search(text)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^##\s", rest, re.M)
    body = rest[: nxt.start()] if nxt else rest
    end = m.end() + (nxt.start() if nxt else len(rest))
    message, paths = None, []
    for raw in body.splitlines():
        line = raw.strip().lstrip("-* ").strip()
        if not line:
            continue
        if line.lower().startswith("message:"):
            message = line.split(":", 1)[1].strip()
        else:
            paths.append(line.strip("`"))
    return message, paths, m.start(), end


def handle(brief, surface):
    text = (ROOT / brief).read_text(encoding="utf-8", errors="replace")
    found = find_block(text)
    if not found:
        return False
    message, paths, start, end = found
    print("\n--- %s asks to commit (%s) ---" % (surface, time.strftime("%H:%M:%S")))
    if not message or not paths:
        print("REFUSED: the block needs a 'Message:' line and at least one path.")
        print("  left in place to be corrected - Tech does not rewrite another lead's brief.")
        return False

    changed = {p[3:].strip().strip('"') for p in git("status", "--porcelain").stdout.splitlines() if p}
    live = [p for p in paths if p in changed or any(c.startswith(p) for c in changed)]
    for p in paths:
        if p not in live:
            print("SKIPPED %-44s not modified in the tree" % p)
    # The brief itself carries the request; committing it would commit the block.
    live = [p for p in live if p != brief]
    if not live:
        print("nothing to commit.")
        return False

    git("add", "--", *live)
    body = ["", "Committed by Tech on request: the '## Commit me' block in %s." % brief,
            "Not authored by Tech. The brief's path is the attribution - nobody",
            "declared a surface and nobody guessed.", ""] + ["  " + p for p in live]
    body += ["", "Surface: %s" % surface, "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"]
    done = git("commit", "-m", "%s: %s (committed by Tech on request)" % (surface, message),
               "-m", "\n".join(body), check=False)
    print(done.stdout or "", done.stderr or "")
    if done.returncode != 0:
        print("REFUSED by a guard rail. Nothing retried; the request stays for a fix.")
        return False

    # Remove the consumed request, and commit that removal separately so the
    # requesting lead sees exactly one edit of its brief, explained.
    after = (text[:start] + text[end:]).rstrip() + "\n"
    (ROOT / brief).write_text(after, encoding="utf-8", newline="\n")
    git("add", "--", brief)
    git("commit", "-m", "Clear the consumed 'Commit me' request from %s" % brief,
        "-m", "\n".join([
            "", "The only edit Tech makes to another lead's brief, and only this:",
            "removing a request it has just carried out. Leaving it would fire the",
            "request again on the next poll.", "",
            "Surface: tech", "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"]),
        check=False)
    print("committed and request cleared: %s" % git("log", "-1", "--format=%h %s").stdout.strip())
    return True


def sweep_once():
    acted = False
    for brief, surface in BRIEFS.items():
        if (ROOT / brief).exists():
            acted = handle(brief, surface) or acted
    return acted


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--interval", type=int, default=20)
    ap.add_argument("--once", action="store_true")
    a = ap.parse_args()
    print("watching %d briefs for '## Commit me' (every %ds) - Ctrl-C to stop"
          % (len(BRIEFS), a.interval))
    while True:
        sweep_once()
        if a.once:
            return 0
        time.sleep(a.interval)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nstopped.")
