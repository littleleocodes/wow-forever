"""Render the WoW: Forever talent JSON into per-class markdown tree docs.

Usage (from anywhere): python _reference/data/render_trees.py [class ...]
Reads  _reference/data/forever-talents/<class>.json
Writes <class>/talents/forever/talent-trees.md
"""
import json, sys, pathlib, collections

CLASSES = ["warrior", "paladin", "hunter", "rogue", "priest", "shaman", "mage", "warlock", "druid"]
root = pathlib.Path(__file__).resolve().parents[2]
DATA = root / "_reference" / "data" / "forever-talents"


def esc(s) -> str:
    if not s:
        return "*(not captured)*"
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def render(cls: str) -> str:
    d = json.load(open(DATA / f"{cls}.json", encoding="utf-8"))
    name = d["name"]
    out = []
    build = d.get("build", "BlizzCon 2026 demo")
    out.append(f"# {name} — WoW: Forever talent trees (beta client {build})\n")
    out.append(f"> **Data status:** WoW: Forever beta client build {build}, captured {d.get('captured')}. "
               + d.get("source", "") + " Every rank's tooltip is the client's (level-" + str(d.get("tooltip_level", 60)) + " values, no gear); "
               "talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). "
               "**Everything here can change before the November 4, 2026 launch** — re-verify against the live game "
               "or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.\n")
    out.append("> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. "
               "51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.\n")

    # summary table
    out.append("## At a glance\n")
    out.append("| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |")
    out.append("|---|---|---|---|---|---|---|")
    for tr in d["trees"]:
        c = collections.Counter(t["status"] for t in tr["talents"])
        out.append(f"| {tr['name']} | {len(tr['talents'])} | {c.get('new',0)} | {c.get('changed',0)} | "
                   f"{c.get('moved',0)} | {c.get('same',0)} | {len(tr.get('removed', []))} |")
    out.append("")

    for tr in d["trees"]:
        out.append(f"## {tr['name']}\n")
        by_row = collections.defaultdict(list)
        for t in tr["talents"]:
            by_row[t["row"]].append(t)
        id2name = {t["id"]: t["name"] for t in tr["talents"]}
        for row in sorted(by_row):
            out.append(f"### Tier {row + 1} — requires {row * 5} points in {tr['name']}\n")
            out.append("| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |")
            out.append("|---|---|---|---|---|---|")
            for t in sorted(by_row[row], key=lambda x: x["col"]):
                req = "—"
                if t.get("prereq"):
                    p = t["prereq"]
                    req = f"{id2name.get(p['id'], p['id'])} ({p.get('rank', '?')})"
                status = t["status"]
                if status == "new":
                    status = "**NEW**"
                elif status == "same":
                    status = "unchanged"
                r1 = esc(t["ranks"][0]) if t["ranks"] else ""
                if t["maxRank"] > 1 and len(t["ranks"]) >= t["maxRank"]:
                    rmax = esc(t["ranks"][t["maxRank"] - 1])
                    if (t["maxRank"] - 1) in t.get("estimated", []):
                        rmax += " *(est.)*"
                elif t["maxRank"] > 1:
                    rmax = "*(not captured)*"
                else:
                    rmax = "—"
                out.append(f"| **{esc(t['name'])}** | {t['maxRank']} | {esc(req)} | {status} | {r1} | {rmax} |")
            out.append("")

        removed = tr.get("removed", [])
        if removed:
            out.append(f"**Removed from Classic {tr['name']}:** " + ", ".join(
                esc(r if isinstance(r, str) else r.get("name", str(r))) for r in removed) + "\n")

    # change log section
    out.append("## Changes vs Classic Era (talent by talent)\n")
    out.append("Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.\n")
    for tr in d["trees"]:
        changed = [t for t in tr["talents"] if t["status"] in ("changed", "moved") and t.get("classic")]
        if not changed:
            continue
        out.append(f"### {tr['name']}\n")
        for t in sorted(changed, key=lambda x: (x["row"], x["col"])):
            diff = ", ".join(t.get("diff", [])) or t["status"]
            out.append(f"- **{esc(t['name'])}** ({diff})")
            out.append(f"  - Classic: {esc(t['classic'][0])}")
            out.append(f"  - Forever: {esc(t['ranks'][0])}")
        out.append("")

    out.append("---\n")
    out.append(f"*Generated from `_reference/data/forever-talents/{cls}.json` by "
               "`_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*")
    return "\n".join(out) + "\n"


for cls in [c for c in CLASSES if not sys.argv[1:] or c in sys.argv[1:]]:
    dest = root / cls / "talents" / "forever" / "talent-trees.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(render(cls), encoding="utf-8")
    print("wrote", dest)
