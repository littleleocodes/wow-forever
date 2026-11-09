"""Most popular builds per class on talentsforever.com, decoded into our build format (2026-09-28, user request: "compare our
builds with the most popular build of each class on talentsforever.com, e.g. mage 0/29/22").

The site publishes its popularity list as a static script, https://talentsforever.com/popular.js (window.POPULAR = {...}):
per class the top 5 level-60 builds people made, shared, saved or opened on the site ("builds within a few points of each other
count as one"), ranked by a score from shares, saves and opens, with the counts. Each build is a site code such as
`mage/60/-0055103013013304-00550003310003002-4`: one digit string per tree, one digit per talent in the tree's order, and a
trailing `-4` that marks the site's current code version (talents in build 70009's order). The site's own data export
(data.json) lists the talents in exactly the order of our `forever-talents/<class>.json` (checked 2026-09-28), so the digits map
onto our dataset directly.

  python _reference/data/popular_builds.py [--fetch] [--raw <folder under raw/>]

--fetch downloads popular.js into raw/<date>-talentsforever-popular/ first; otherwise the newest archived copy is read. Writes
`_reference/data/popular-builds.json` (generated: every class's top builds with allocation, split, lead tree and counts, each
checked with the validator). The races are `popular_race.py`.
"""
import argparse
import datetime
import json
import pathlib
import sys
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import validate_builds as vb   # noqa: E402

URL = "https://talentsforever.com/popular.js"
RAW = HERE / "raw"
OUT = HERE / "popular-builds.json"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]


def latest_raw():
    dirs = sorted(p for p in RAW.glob("*-talentsforever-popular") if (p / "popular.js").exists())
    if not dirs:
        raise SystemExit("no archived popular.js: run with --fetch")
    return dirs[-1]


def load_popular(path):
    s = path.read_text(encoding="utf-8")
    return json.loads(s[s.index("{"): s.rindex("}") + 1])


# The site's code version whose talent order our forever-talents/ data follows. Version 4 was build 70009's order; the site moved to
# version 6 with its later tree changes (its changelog: old links are translated on open) and to version 7 with the 70425 trees
# (2026-10-17); our data comes from the site's own export at build 70425 (2026-10-16), so version-7 codes map digit by digit onto it.
# Checked for every code of the 2026-10-17 list (and the version-6 codes of 2026-10-09 against the 70291 data): no tree has more
# digits than talents, no digit exceeds its talent's rank cap, the per-tree points equal the site's own `pts`, and the validator passes
# but for builds under 51 points. A code of another version is refused rather than decoded onto the wrong talents.
# 2026-11-09: version 12, the version render_start_here.TF_CODE_VERSION names (the site moved 7 -> 12 between 10-17 and 11-04). All 45 codes
# of the 2026-11-09 list decode onto our data with the site's per-tree points and no rank, tier or prerequisite error; 7 are under 51 points.
CODE_VERSION = "12"


def decode(cls, code, trees_data):
    """Site code -> {tree: [[talent, ranks], ...]} in our dataset's names and order (strict: a digit count or rank that does not fit
    the tree raises, so a talent order that moved is noticed instead of clamped away)."""
    body = code.split("/")[2]
    segs = body.split("-")
    if segs[-1] != CODE_VERSION or len(segs) != len(trees_data) + 1:
        raise ValueError(f"{code}: not a version-{CODE_VERSION} code (our talent data follows that version's order)")
    alloc = {}
    for tr, digits in zip(trees_data, segs[:-1]):
        if digits and len(digits) > len(tr["talents"]):
            raise ValueError(f"{code}: {len(digits)} digits for the {tr['name']} tree, which has {len(tr['talents'])} talents")
        items = []
        for t, d in zip(tr["talents"], digits):
            if int(d) > t["maxRank"]:
                raise ValueError(f"{code}: {int(d)} points in {t['name']} (rank cap {t['maxRank']})")
            if int(d):
                items.append([t["name"], int(d)])
        alloc[tr["name"]] = items
    return alloc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch", action="store_true")
    ap.add_argument("--raw")
    a = ap.parse_args()
    if a.fetch:
        d = RAW / f"{datetime.date.today().isoformat()}-talentsforever-popular"
        d.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(URL, headers={"User-Agent": "wow-forever knowledge base"})
        try:
            (d / "popular.js").write_bytes(urllib.request.urlopen(req, timeout=60).read())
        except urllib.error.URLError as ex:
            # 2026-10-09: Python's certificate store on Windows rejected Let's Encrypt's new chain ("certificate has expired") while the
            # site's certificate was valid; curl verifies with its own store, so it is the fallback (verification stays on)
            import shutil
            import subprocess
            if not shutil.which("curl"):
                raise
            print(f"urllib failed ({ex.reason}); fetching with curl")
            subprocess.run(["curl", "-sSf", "--max-time", "60", "-A", "wow-forever knowledge base", "-o", str(d / "popular.js"), URL], check=True)
        print(f"fetched {URL} -> {d.relative_to(HERE.parents[1])}")
    src = RAW / a.raw if a.raw else latest_raw()
    pop = load_popular(src / "popular.js")
    ftrees = vb.load_forever()
    out = {"about": "Generated by popular_builds.py from talentsforever.com's popular.js (the site's own popularity list: the top level-60 "
                    "builds people made, shared, saved or opened on the site, ranked by a score of shares, saves and opens). Do not hand-edit.",
           "source": URL, "raw": str((src / "popular.js").relative_to(HERE.parents[1])).replace("\\", "/"), "classes": {}}
    for cls in CLASSES:
        pc = pop["classes"][cls.capitalize()]
        data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
        rows = []
        for b in pc.get("top", []):
            alloc = decode(cls, b["code"], data["trees"])
            pts = [sum(r for _, r in alloc[t["name"]]) for t in data["trees"]]
            build = {"id": f"tf-popular-{b['rank']}-{cls}", "allocation": alloc}
            errors = vb.validate_build(ftrees[cls], build, build["id"])
            if pts != b["pts"]:
                errors.append(f"split {pts} != the site's {b['pts']}")
            rows.append({"id": build["id"], "rank": b["rank"], "lead": b["lead"], "split": "/".join(map(str, pts)),
                         "url": f"https://talentsforever.com/{b['code']}", "code": b["code"],
                         "score": b["score"], "shared": b["shared"], "saved": b["saved"], "opened": b["opened"], "variants": b.get("variants"),
                         "valid": not errors, "errors": errors, "allocation": alloc})
            print(f"{cls:<8} #{b['rank']} {b['lead']:<14} {rows[-1]['split']:<9} score {b['score']:>6}  {'ok' if not errors else '; '.join(errors)}")
        epoch = pc.get("epoch")
        out["classes"][cls] = {"window": pc.get("window"), "since_patch": bool(epoch), "builds_counted": pc.get("builds"),
                               "full_builds": pc.get("full"), "spec_share": pc.get("spec"), "top": rows}
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(HERE.parents[1])}")


if __name__ == "__main__":
    main()
