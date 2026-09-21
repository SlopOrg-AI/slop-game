#!/usr/bin/env python3
"""Claim, release and inspect live session roles.

On 2026-09-20 two Claude Code sessions both read "Claude Code is the Tech lead",
both concluded it was them, and both wrote the same brief for hours. Neither
could see the other. This is the register that makes that visible in seconds.

    python tools/session.py list
    python tools/session.py claim tech --kind lead --name "Review needed [6eb758]"
    python tools/session.py touch tech
    python tools/session.py release tech

One file per role in sessions/, named for the routing tag. Creating it is the
claim; finding it already there is the collision. A role with no file is normal
- not every lead is live, and that is fine.

WHAT THIS IS NOT: proof. A session states who it is and cannot demonstrate it,
so a determined or confused session can overwrite any claim. It is detection,
not enforcement - the difference between finding out in seconds and finding out
after four hours, which is the one that has actually cost this project time.

COWORK HAS NO SHELL. Leads run there, so every operation here is also doable by
hand: the files are plain markdown with a fixed header, and sessions/README.md
says how to write one. Nothing in the register requires this script.
"""

import argparse
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "sessions"
STALE_HOURS = 3
TAGS = ("cos", "sys", "content", "tech", "art", "level", "scenario", "mkt")
FMT = "%Y-%m-%d %H:%M"


def path_for(tag):
    return REG / ("%s.md" % tag)


def parse(path):
    out = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("- **") and "**:" in line:
            key, _, val = line[4:].partition("**:")
            out[key.strip().lower()] = val.strip()
    return out


def age_hours(stamp):
    try:
        then = dt.datetime.strptime(stamp, FMT)
    except (ValueError, TypeError):
        return None
    return (dt.datetime.now() - then).total_seconds() / 3600.0


def write(tag, kind, name, claimed=None):
    now = dt.datetime.now().strftime(FMT)
    body = [
        "# Live session — `%s`" % tag,
        "",
        "- **Role**: %s" % tag,
        "- **Kind**: %s" % kind,
        "- **Session**: %s" % name,
        "- **Claimed**: %s" % (claimed or now),
        "- **Last seen**: %s" % now,
        "",
        "Written by the session that holds this role. Delete it at session close",
        "(`python tools/session.py release %s`). A claim whose **Last seen** is more" % tag,
        "than %d hours old is presumed dead and may be taken - say so when you take it." % STALE_HOURS,
        "",
        "If you are starting a session and this file names someone else, **you are not",
        "this role**. Ask the owner, who confirms lead-or-subordinate at session start.",
    ]
    path_for(tag).write_text("\n".join(body) + "\n", encoding="utf-8", newline="\n")


def cmd_list(_):
    REG.mkdir(exist_ok=True)
    files = sorted(REG.glob("*.md"))
    files = [f for f in files if f.name != "README.md"]
    if not files:
        print("no live claims. That is a normal state - not every lead runs every day.")
        return 0
    print("%-10s %-12s %-34s %-18s %s" % ("ROLE", "KIND", "SESSION", "LAST SEEN", ""))
    for f in files:
        d = parse(f)
        age = age_hours(d.get("last seen"))
        flag = ""
        if age is None:
            flag = "unreadable timestamp"
        elif age > STALE_HOURS:
            flag = "STALE (%.1fh) - presumed dead, may be taken" % age
        print("%-10s %-12s %-34s %-18s %s" % (
            d.get("role", f.stem), d.get("kind", "?"), d.get("session", "?"),
            d.get("last seen", "?"), flag))
    return 0


def cmd_claim(a):
    REG.mkdir(exist_ok=True)
    if a.tag.split("-", 1)[0] not in TAGS:
        print("'%s' is not a routing tag (%s)" % (a.tag, ", ".join(TAGS)), file=sys.stderr)
        return 2
    p = path_for(a.tag)
    if p.exists():
        d = parse(p)
        age = age_hours(d.get("last seen"))
        held_by = d.get("session", "?")
        if held_by == a.name:
            write(a.tag, a.kind, a.name, claimed=d.get("claimed"))
            print("already yours; refreshed.")
            return 0
        if age is not None and age <= STALE_HOURS:
            print("REFUSED: '%s' is held by %s, last seen %s (%.1fh ago)."
                  % (a.tag, held_by, d.get("last seen"), age), file=sys.stderr)
            print("  Two live sessions in one role is the thing this register exists to "
                  "catch. Ask the owner which of you holds it.", file=sys.stderr)
            return 1
        print("taking over from %s - last seen %s, past the %dh staleness line."
              % (held_by, d.get("last seen"), STALE_HOURS))
    write(a.tag, a.kind, a.name)
    print("claimed %s as %s: %s" % (a.tag, a.kind, a.name))
    return 0


def cmd_touch(a):
    p = path_for(a.tag)
    if not p.exists():
        print("no claim on '%s' to touch." % a.tag, file=sys.stderr)
        return 1
    d = parse(p)
    write(a.tag, d.get("kind", "lead"), d.get("session", "?"), claimed=d.get("claimed"))
    print("touched %s" % a.tag)
    return 0


def cmd_release(a):
    p = path_for(a.tag)
    if not p.exists():
        print("nothing to release.")
        return 0
    p.unlink()
    print("released %s" % a.tag)
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    c = sub.add_parser("claim")
    c.add_argument("tag")
    c.add_argument("--kind", default="lead", help="lead | subordinate of <lead>")
    c.add_argument("--name", required=True, help="how this session is identified")
    c.set_defaults(fn=cmd_claim)
    for name, fn in (("touch", cmd_touch), ("release", cmd_release)):
        s = sub.add_parser(name)
        s.add_argument("tag")
        s.set_defaults(fn=fn)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
