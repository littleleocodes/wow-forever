"""Print a compact view of a class's Forever tree: python show_tree.py warrior [maxlen]"""
import json, sys, pathlib
cls = sys.argv[1]; L = int(sys.argv[2]) if len(sys.argv) > 2 else 150
d = json.load(open(pathlib.Path(__file__).parent / "forever-talents" / f"{cls}.json", encoding="utf-8"))
for tr in d["trees"]:
    print(f"== {tr['name']}  (removed: {', '.join(r if isinstance(r,str) else r.get('name','') for r in tr.get('removed', []))})")
    id2name = {t["id"]: t["name"] for t in tr["talents"]}
    rows = {}
    for t in tr["talents"]:
        rows.setdefault(t["row"], []).append(t)
    for r in sorted(rows):
        print(f"  -- T{r+1} [{r*5}]")
        for t in sorted(rows[r], key=lambda x: x["col"]):
            req = f" <- {id2name.get(t['prereq']['id'], t['prereq']['id'])} {t['prereq'].get('rank','')}" if t.get("prereq") else ""
            mark = {"new": "NEW", "changed": "chg", "moved": "mov", "same": "same"}.get(t["status"], t["status"])
            txt = (t["ranks"][0] or "")[:L]
            print(f"     {t['name']} ({t['maxRank']}) [{mark}]{req}: {txt}")
