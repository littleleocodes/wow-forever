"""Every relative markdown link in the project that points at nothing.

    python _reference/data/linkcheck.py

Prints "<n> relative links checked, <m> broken in <k> files" and the broken ones (archived raw data is skipped). Run it after
moving or renaming pages; the checks after a rebuild expect 0 broken.
"""
import collections
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
LINK = re.compile(r"\]\(([^)\s]+)\)")


def main():
    bad = collections.defaultdict(list)
    n = 0
    for md in ROOT.rglob("*.md"):
        if any(part in ("raw", "node_modules", ".git") for part in md.parts):
            continue
        for m in LINK.finditer(md.read_text(encoding="utf-8", errors="replace")):
            t = m.group(1)
            if re.match(r"^[a-z]+:", t) or t.startswith("#") or t.startswith("<"):
                continue
            n += 1
            target = (md.parent / t.split("#")[0]).resolve()
            if not target.exists():
                bad[md.relative_to(ROOT).as_posix()].append(t)
    print(f"{n} relative links checked, {sum(len(v) for v in bad.values())} broken in {len(bad)} files")
    for f, ts in sorted(bad.items()):
        print(f"  {f}: " + ", ".join(sorted(set(ts))[:8]) + (" ..." if len(set(ts)) > 8 else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
