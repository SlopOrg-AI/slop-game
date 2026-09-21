#!/usr/bin/env python3
"""Build a self-contained wireframe from the template + design-data JSON.

    python build.py            -> builds every combat-1v1-v*.template.html next to this script

Why: browsers block fetch() from file:// pages, and the claude.ai artifact host
strips <script type="application/json"> blocks, so the JSON is inlined as a plain
JS object (window.__DD). The JSON files stay the single source
of truth; Godot reads the same files directly. Re-run after editing any JSON.
"""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "Godot" / "shinobi-master" / "data"
TEMPLATES = sorted(HERE.glob("combat-1v1-v*.template.html"))
CSS_SOURCE = HERE / "combat-1v1-v1.html"   # v2 borrows v1's stylesheet via <!--CSS-->; later versions carry their own

files = {
    "dd-rules": DATA / "rules.json",
    "dd-characters": DATA / "characters.json",
    "dd-abilities": DATA / "abilities.json",
    "dd-wounds": DATA / "wounds.json",
    "dd-states": DATA / "states.json",
    "dd-conditions": DATA / "conditions.json",
    "dd-snapshot": HERE / "snapshot-round3.json",
}

def main():
    blocks = []
    for el_id, path in files.items():
        data = json.loads(path.read_text(encoding="utf-8"))  # validates
        text = json.dumps(data, separators=(",", ":")).replace("</", "<\\/")
        blocks.append(f'window.__DD["{el_id}"]={text};')
    css = re.search(r"<style>.*?</style>", CSS_SOURCE.read_text(encoding="utf-8"), re.S).group(0)
    css3 = re.search(r"<style>.*?</style>", (HERE / "combat-1v1-v3.template.html").read_text(encoding="utf-8"), re.S).group(0)
    data_script = "<script>window.__DD=window.__DD||{};\n" + "\n".join(blocks) + "\n</script>"
    for tpl in TEMPLATES:
        out = HERE / tpl.name.replace(".template", "")
        html = tpl.read_text(encoding="utf-8")
        html = html.replace("<!--CSS-->", css, 1).replace("<!--CSS3-->", css3, 1).replace("<!--DATA-->", data_script, 1)
        out.write_text(html, encoding="utf-8")
        print(f"wrote {out.name}  ({out.stat().st_size:,} bytes)")

if __name__ == "__main__":
    main()
