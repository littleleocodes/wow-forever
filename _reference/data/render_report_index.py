"""A "## Report index" on each research README: every generated report under it that no other page links to (2026-10-15 page audit
D7: 231 generated reports, from raid-sim and healer-lab reports to the Classic baseline's optimizer pages, were reachable only by
browsing folders).

    python _reference/data/render_report_index.py [classes]

Per class, the reports under `research/leveling/`, `research/raid/` and `research/talents/` that no tracked page (outside the index
itself) links to are listed under the nearest README: the leveling and raid READMEs (readme_sections order) and the Classic baseline
README; `research/talents/forever/` reports go to the raid README's index (its own README is hand-kept). Build pages are left out:
the Builds tables link them. Run after every renderer (rebuild.py's regen step runs it last).
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import readme_sections  # noqa: E402

CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
HEADING = "## Report index"
LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")


def inbound():
    """{resolved .md path: number of pages linking to it}, ignoring links inside a Report index section."""
    seen = {}
    for p in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in p.relative_to(ROOT).parts):
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        i = txt.find("\n" + HEADING)
        if i >= 0:
            j = txt.find("\n## ", i + 1)
            txt = txt[:i] + (txt[j:] if j >= 0 else "")
        for m in LINK.finditer(txt):
            t = (p.parent / m.group(1)).resolve()
            if t != p.resolve():
                seen[t] = seen.get(t, 0) + 1
    return seen


def title(p):
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return p.stem


def main():
    classes = [c for c in sys.argv[1:] if c in CLASSES] or CLASSES
    links = inbound()
    for cls in classes:
        base = ROOT / cls / "research"
        homes = {"leveling": base / "leveling" / "README.md", "raid": base / "raid" / "README.md",
                 "classic": base / "talents" / "classic-baseline" / "README.md"}
        groups = {k: [] for k in homes}
        for p in sorted(base.rglob("*.md")):
            if p.name == "README.md" or "builds" in p.relative_to(base).parts or links.get(p.resolve()):
                continue
            rel = p.relative_to(base).parts
            key = "leveling" if rel[0] == "leveling" else "classic" if rel[:2] == ("talents", "classic-baseline") else "raid"
            groups[key].append(p)
        for key, files in groups.items():
            home = homes[key]
            if not home.exists():
                continue
            if not files:
                readme_sections.drop(home, HEADING)
                continue
            o = [HEADING, "", "Reports under this folder that no other page links to (generated):", ""]
            for p in files:
                o.append(f"- [{p.relative_to(home.parent).as_posix()}]({p.relative_to(home.parent).as_posix()}): {title(p)}")
            text = "\n".join(o)
            if key in ("leveling", "raid"):
                readme_sections.splice_ordered(home, key, HEADING, text)
            else:
                readme_sections.splice(home, HEADING, text)
        print(f"{cls}: " + ", ".join(f"{k} {len(v)}" for k, v in groups.items()))


if __name__ == "__main__":
    main()
