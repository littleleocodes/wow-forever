"""The simulator's spell data between two pins (2026-11-23, the audit session's ask for the re-pin of 2026-11-23: our talent and spell text
is on client 70938, upstream's head on 71037 with the hotfixes of 2026-11-22; the fight lab, the stats model, the healer lab and the pages
read our text, the raid simulator its own). Lists every spell id whose generated data (sim/core/spelldata/spells_auto_gen.go: curves,
base points, coefficients) changed between the commits, named from our spellbooks (forever-spells/<class>.json rank ids) where we have
the spell. It changes nothing: a moved spell that a leveling pick casts goes through hotfix_text.py after the lists (2026-11-16's way).

    python _reference/data/raidsim/spelldata_diff.py <old commit> <new commit> [--write]   # raidsim/spelldata-diff.json
"""
import argparse
import collections
import datetime
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
FILE = "sim/core/spelldata/spells_auto_gen.go"
ID = re.compile(r"^\s*(?:\{\s*)?(?:ID:\s*|SpellID:\s*)?(\d{2,8})\s*[:,]")
ATTR = [re.compile(r"Attr: \[17\]uint32\{[^}]*\},\s*"), re.compile(r"NoSpellLevels: true,\s*")]


def numbers_moved(v):
    """False when the old and new lines differ only in attribute bits (Attr, NoSpellLevels): no number of the spell moved."""
    def norm(xs):
        out = []
        for s in xs:
            for p in ATTR:
                s = p.sub("", s)
            out.append(s)
        return sorted(out)
    return norm(v["old"]) != norm(v["new"])


def ours():
    """{spell id: (class, spell, rank)} from our spellbooks."""
    out = {}
    for f in sorted((DATA / "forever-spells").glob("*.json")):
        d = json.load(open(f, encoding="utf-8"))
        for tab in d.get("tabs") or []:
            for s in tab.get("spells") or []:
                for r in s.get("ranks") or []:
                    if isinstance(r, dict) and r.get("id"):
                        out[int(r["id"])] = (f.stem, s.get("name"), r.get("rank") or "")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("old")
    ap.add_argument("new")
    ap.add_argument("--repo", default=str(pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever"))
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    r = subprocess.run(["git", "-C", a.repo, "diff", "--unified=0", a.old, a.new, "--", FILE], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"git diff failed: {r.stderr[-500:]}")
    lines = collections.defaultdict(lambda: {"old": [], "new": []})
    unkeyed = 0
    for ln in r.stdout.splitlines():
        if ln.startswith(("+++", "---", "@@")) or not ln[:1] in "+-":
            continue
        m = ID.match(ln[1:])
        if not m:
            unkeyed += 1
            continue
        lines[int(m.group(1))]["old" if ln[0] == "-" else "new"].append(ln[1:].strip()[:300])
    known = ours()
    by_class = collections.defaultdict(list)
    other = []
    for sid, v in sorted(lines.items()):
        row = {"id": sid, "numbers_moved": numbers_moved(v), **v}
        if sid in known:
            c, name, rank = known[sid]
            by_class[c].append(dict(row, spell=name, rank=rank))
        else:
            other.append(row)
    print(f"spell data {a.old[:9]} -> {a.new[:9]}: {len(lines)} spell ids changed ({unkeyed} changed lines without an id); "
          f"{sum(len(v) for v in by_class.values())} in our spellbooks, {len(other)} elsewhere (talents, items, procs, other)")
    for c, rows in sorted(by_class.items()):
        print(f"  {c}: " + "; ".join(f"{x['spell']} {x['rank']} ({x['id']}{'' if x['numbers_moved'] else ', attributes only'})" for x in rows))
    print(f"  numbers moved: {sum(1 for v in by_class.values() for x in v if x['numbers_moved'])} of ours, "
          f"{sum(1 for x in other if x['numbers_moved'])} elsewhere")
    if a.write:
        out = {"date": datetime.date.today().isoformat(), "old": a.old, "new": a.new, "changed_ids": len(lines), "unkeyed_lines": unkeyed,
               "ours": dict(by_class), "other": other}
        (HERE / "spelldata-diff.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("wrote raidsim/spelldata-diff.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
