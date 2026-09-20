"""Board annotator - pin critique notes to regions of generated art.

Serves the pages in this folder and reads/writes under shinobi-v2/proposals/art.
Annotations are saved next to each image as <image>.annotations.json so agents
reading the repo find feedback anchored to coordinates, not just prose.

Run:  python server.py            (default port 8189)
      python server.py --port N
Stdlib only - any Python 3.9+, including ComfyUI's embedded interpreter.
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import posixpath
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

HERE = Path(__file__).resolve().parent
ART = (HERE / ".." / ".." / "proposals" / "art").resolve()
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".webp"}


def safe_art_path(rel: str) -> Path | None:
    """Resolve rel inside ART, refusing traversal."""
    if not rel:
        return None
    candidate = (ART / rel).resolve()
    try:
        candidate.relative_to(ART)
    except ValueError:
        return None
    return candidate


def sidecar_for(image: Path) -> Path:
    return image.with_suffix(image.suffix + ".annotations.json")


def list_boards() -> list[dict]:
    boards = []
    if not ART.exists():
        return boards
    for p in sorted(ART.rglob("*")):
        if p.suffix.lower() not in IMAGE_EXT or not p.is_file():
            continue
        rel = p.relative_to(ART).as_posix()
        side = sidecar_for(p)
        count = 0
        if side.exists():
            try:
                count = len(json.loads(side.read_text("utf-8")).get("annotations", []))
            except (ValueError, OSError):
                count = 0
        boards.append({
            "path": rel,
            "bytes": p.stat().st_size,
            "mtime": p.stat().st_mtime,
            "annotations": count,
        })
    boards.sort(key=lambda b: b["mtime"], reverse=True)
    return boards


class Handler(BaseHTTPRequestHandler):
    server_version = "BoardAnnotator/1.0"

    # -- helpers -------------------------------------------------------
    def _send(self, code: int, body: bytes, ctype: str = "application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj):
        self._send(code, json.dumps(obj).encode("utf-8"))

    def log_message(self, fmt, *args):  # quieter console
        if "api" not in (args[0] if args else ""):
            return

    # -- routes --------------------------------------------------------
    def do_GET(self):
        u = urlparse(self.path)
        route = unquote(u.path)

        if route in ("/", "/index.html"):
            return self._file(HERE / "index.html", "text/html; charset=utf-8")

        if route == "/api/boards":
            return self._json(200, {"root": str(ART), "boards": list_boards()})

        if route == "/api/annotations":
            rel = (parse_qs(u.query).get("path") or [""])[0]
            img = safe_art_path(rel)
            if img is None or not img.exists():
                return self._json(404, {"error": "unknown image"})
            side = sidecar_for(img)
            if not side.exists():
                return self._json(200, {"image": rel, "annotations": []})
            try:
                return self._json(200, json.loads(side.read_text("utf-8")))
            except ValueError:
                return self._json(200, {"image": rel, "annotations": [],
                                        "warning": "existing sidecar was unreadable"})

        if route.startswith("/img/"):
            img = safe_art_path(posixpath.normpath(route[len("/img/"):]))
            if img is None or not img.exists():
                return self._json(404, {"error": "not found"})
            ctype = mimetypes.guess_type(img.name)[0] or "application/octet-stream"
            return self._file(img, ctype)

        return self._json(404, {"error": "no route"})

    def do_POST(self):
        u = urlparse(self.path)
        if unquote(u.path) != "/api/annotations":
            return self._json(404, {"error": "no route"})

        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0 or length > 4_000_000:
            return self._json(400, {"error": "bad body size"})
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            return self._json(400, {"error": "bad json"})

        rel = payload.get("image") or ""
        img = safe_art_path(rel)
        if img is None or not img.exists():
            return self._json(400, {"error": "unknown image"})

        doc = {
            "image": rel,
            "image_size": payload.get("image_size"),
            "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "annotations": payload.get("annotations") or [],
        }
        side = sidecar_for(img)
        side.write_text(json.dumps(doc, indent=2, ensure_ascii=False), "utf-8")
        return self._json(200, {"ok": True, "saved": side.name,
                                "count": len(doc["annotations"])})

    def _file(self, path: Path, ctype: str):
        try:
            return self._send(200, path.read_bytes(), ctype)
        except OSError:
            return self._json(404, {"error": "missing file"})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8189)
    args = ap.parse_args()

    if not ART.exists():
        print(f"warning: art directory not found at {ART}")
    print(f"Board annotator -> http://127.0.0.1:{args.port}")
    print(f"Reading boards from {ART}")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()


if __name__ == "__main__":
    main()
