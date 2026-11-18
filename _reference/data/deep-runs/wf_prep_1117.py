"""Record preparation for wf_enh_1117.sh (2026-11-17, the Windfury Totem fix):

    python wf_prep_1117.py family   # take enhancement-dps out of raidsim/families/shaman.json, so a plain (resumed) family_search.py
                                    # shaman --entry enhancement-dps searches it again and the other entries keep their results
    python wf_prep_1117.py ml       # clear the final-step keys of the Enhancement and Elemental/Enhancement ML records, as
                                    # raid_shaman_1103.sh did, so ml_pipeline.py --steps final redoes them in the new setting

Backups go to deep-runs/wf1117/ (never next to the records: the tools read every file in those folders)."""
import json
import pathlib
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
M = DATA / "deep-runs" / "wf1117"
M.mkdir(parents=True, exist_ok=True)


def dump(p, d):
    p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


what = sys.argv[1] if len(sys.argv) > 1 else ""
if what == "family":
    p = DATA / "raidsim" / "families" / "shaman.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    e = d["entries"].pop("enhancement-dps", None)
    if e is None:
        print("families/shaman.json: no enhancement-dps entry (already taken out)")
    else:
        dump(M / "families-shaman-enhancement-dps.json", e)
        dump(p, d)
        print("families/shaman.json: enhancement-dps taken out (backup in deep-runs/wf1117/)")
elif what == "ml":
    d = DATA / "raidsim" / "ml"
    for n in ("shaman-enhancement.json", "shaman-hybrid-elemental-enhancement.json"):
        p = d / n
        r = json.loads(p.read_text(encoding="utf-8"))
        dump(M / f"ml-{n}", r)
        for k in ("bis2", "prebis", "bis-raid", "prebis-raid"):
            r.get("gear", {}).pop(k, None)
        for k in ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid"):
            r.get("search", {}).pop(k, None)
        for k in ("compare", "compare_raid", "builds", "tidied", "aligned_raid", "signature_check"):
            r.pop(k, None)
        dump(p, r)
        print("cleared", n)
else:
    sys.exit("usage: wf_prep_1117.py family|ml")
