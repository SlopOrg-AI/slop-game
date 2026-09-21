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
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

# Windows consoles default to cp1252 and these documents are full of arrows and
# dashes. The first run of this watcher died printing one. Third encoding bug of
# the same family tonight: read UTF-8, write UTF-8, never inherit the locale.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

# A fenced block is documentation, not a request. The first run matched the
# EXAMPLE in leads/systems/tech.md that shows a lead how to write one, and
# treated the rest of the brief as paths. Documentation that fires the
# mechanism it documents is a bug in the mechanism, not in the documentation.
FENCE = re.compile(r"^```.*?^```", re.M | re.S)

ROOT = Path(__file__).resolve().parents[1]
# Per-clone state, deliberately inside .git: which request was last consumed
# from each brief. Two surfaces write these files, and a lead saving its brief
# from its own buffer restores a block Tech has already stripped - which is
# what happened tonight and produced two commits of one request.
CONSUMED = ROOT / ".git" / "watch-consumed.json"
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


def fingerprint(message, paths):
    blob = "|".join([message or ""] + sorted(paths))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def already_consumed(brief, fp):
    try:
        return json.loads(CONSUMED.read_text(encoding="utf-8")).get(brief) == fp
    except (OSError, ValueError):
        return False


def mark_consumed(brief, fp):
    try:
        data = json.loads(CONSUMED.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        data = {}
    data[brief] = fp
    try:
        CONSUMED.write_text(json.dumps(data, indent=1), encoding="utf-8")
    except OSError:
        pass


def find_block(text):
    """-> (message, [paths], start, end) for the first real '## Commit me' section.

    Fenced examples are blanked first, with their length preserved so the
    offsets still point into the original text.
    """
    nl = chr(10)
    blank = lambda m: nl.join(" " * len(l) for l in m.group(0).split(nl))
    scannable = FENCE.sub(blank, text)
    m = HEADING.search(scannable)
    if not m:
        return None
    rest = scannable[m.end():]
    nxt = re.search(r"^##\s", rest, re.M)
    body = rest[: nxt.start()] if nxt else rest
    # A request is short. Anything longer is a false match on prose.
    if len([l for l in body.splitlines() if l.strip()]) > 25:
        return None
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


def handle(brief, surface, no_push=False):
    text = (ROOT / brief).read_text(encoding="utf-8", errors="replace")
    found = find_block(text)
    if not found:
        return False
    message, paths, start, end = found
    fp = fingerprint(message, paths)
    if already_consumed(brief, fp):
        print("")
        print("--- %s: SAME request again, not committing (%s) ---"
              % (surface, time.strftime("%H:%M:%S")))
        print("  This exact request was already carried out. The brief was")
        print("  written back from a buffer that still held the block, which")
        print("  overwrote the strip - the drift guard in your own brief says")
        print("  read the file from disk in the same session before any write.")
        print("  Remove the block, or change it if the request is genuinely new.")
        return False
    print("\n--- %s asks to commit (%s) ---" % (surface, time.strftime("%H:%M:%S")))
    if not message or not paths:
        print("REFUSED: the block needs a 'Message:' line and at least one path.")
        print("  left in place to be corrected - Tech does not rewrite another lead's brief.")
        return False

    changed = {p[3:].strip().strip('"') for p in git("status", "--porcelain", "--untracked-files=all").stdout.splitlines() if p}
    live = [p for p in paths if p in changed or any(c.startswith(p) for c in changed)]
    for p in paths:
        if p not in live:
            print("SKIPPED %-44s not modified in the tree" % p)
    if not live:
        print("nothing to commit.")
        return False

    # Strip the consumed request BEFORE committing, so the requesting lead's own
    # brief edits land in ITS commit under ITS name. The first version excluded
    # the brief and cleared it afterwards in a separate commit of Tech's, which
    # would have attributed a lead's own writing to Tech - the exact error this
    # mechanism exists to prevent, built into the mechanism.
    stripped = (text[:start] + text[end:]).rstrip() + chr(10)
    (ROOT / brief).write_text(stripped, encoding="utf-8", newline=chr(10))
    if brief not in live:
        live.append(brief)

    git("add", "--", *live)
    body = ["", "Committed by Tech on request: the '## Commit me' block in %s," % brief,
            "which this commit also consumes. Not authored by Tech - the brief's",
            "path is the attribution, so nobody declared a surface and nobody",
            "guessed.", ""] + ["  " + p for p in live]
    body += ["", "Surface: %s" % surface, "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"]
    # A lead that prefixes its own Message with its tag should not get "cos: cos:".
    if message.lower().startswith(surface.lower() + ":"):
        message = message.split(":", 1)[1].strip()
    done = git("commit", "-m", "%s: %s (committed by Tech on request)" % (surface, message),
               "-m", chr(10).join(body), check=False)
    print(done.stdout or "", done.stderr or "")
    if done.returncode != 0:
        # Put the request back exactly as it was: a refused commit must leave the
        # tree as it found it, or the lead loses its request to a failed attempt.
        (ROOT / brief).write_text(text, encoding="utf-8", newline=chr(10))
        git("reset", "-q", check=False)
        print("REFUSED by a guard rail. Request restored; nothing retried.")
        return False

    mark_consumed(brief, fp)
    print("committed, request consumed: %s" % git("log", "-1", "--format=%h %s").stdout.strip())
    push(no_push)
    return True


def push(no_push=False):
    """Push after a requested commit (owner, 2026-09-21).

    A commit that never leaves this machine is not in the record any other
    surface or machine can see - and the whole point of the remote is that the
    repo stopped existing on one disk. A lead directing a commit is directing
    it into the record, not into this clone.

    Never force. A rejected push is reported and left alone: the commit is
    safe locally and the next push takes it, whereas a force would discard
    whatever the rejection was protecting.
    """
    if no_push:
        print("push skipped (--no-push).")
        return
    if not git("remote", check=False).stdout.strip():
        print("no remote configured; commit is local only.")
        return
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    done = git("push", "origin", branch, check=False)
    if done.returncode == 0:
        print("pushed to origin/%s." % branch)
    else:
        print((done.stderr or "").strip())
        print("PUSH FAILED. The commit is safe locally and unpushed; nothing")
        print("was forced and nothing retried. Next push carries it.")


def report():
    """List what git sees as unrecorded, split by whether anyone claimed it.

    Run as the first and last act of a session (cos.5, owner 2026-09-21).
    Detection only. tools/sweep.py was retired for guessing WHO wrote a path
    from a path table - that guess caused three misattributions - and this does
    not bring the guessing back. It notices; a person names.
    """
    out = git("status", "--porcelain", "--untracked-files=all").stdout.splitlines()
    paths = [l[3:].strip().strip('"') for l in out if l.strip()]
    if not paths:
        print("nothing unrecorded. Tree is clean.")
        return 0

    declared = {}
    for brief, surface in BRIEFS.items():
        f = ROOT / brief
        if not f.exists():
            continue
        found = find_block(f.read_text(encoding="utf-8", errors="replace"))
        if found and found[1]:
            for d in found[1]:
                declared[d] = (surface, brief)

    claimed, unclaimed = [], []
    for p in paths:
        hit = next((d for d in declared if p == d or p.startswith(d)), None)
        (claimed if hit else unclaimed).append((p, declared.get(hit)))

    for p, who in claimed:
        print("DECLARED   %-52s by %s (%s)" % (p, who[0], who[1]))
    for p, _ in unclaimed:
        print("UNCLAIMED  %-52s nobody has asked for this" % p)

    if unclaimed:
        print("")
        print("%d unclaimed path(s). DO NOT COMMIT THEM. Put the list in" % len(unclaimed))
        print("leads/systems/tech.md section For Chief of Staff - these changed,")
        print("nobody claimed them - and let the owner or Chief of Staff say whose")
        print("they are. A wrong name in history is permanent and invisible to")
        print("every automated check.")
    return 0


def sweep_once(no_push=False):
    acted = False
    for brief, surface in BRIEFS.items():
        if (ROOT / brief).exists():
            acted = handle(brief, surface, no_push) or acted
    return acted


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--interval", type=int, default=20)
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--no-push", action="store_true",
                    help="commit but do not push; the default is to push")
    ap.add_argument("--report", action="store_true",
                    help="list unrecorded work, declared vs unclaimed; commit nothing")
    a = ap.parse_args()
    if a.report:
        return report()
    print("watching %d briefs for '## Commit me' (every %ds) - Ctrl-C to stop"
          % (len(BRIEFS), a.interval))
    while True:
        sweep_once(a.no_push)
        if a.once:
            return 0
        time.sleep(a.interval)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nstopped.")
