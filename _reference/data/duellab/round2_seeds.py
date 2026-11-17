"""Round-2 starts for the PvP search (2026-11-17; user: "Go with all your recommendations"): per tree, the round-1 winner
(duellab/search/), the blind-spot check's improved build and battleground version (duellab/results-1117.json), and for a winner without
its tree's signature talent (the PvP rule of 2026-11-17) the check's put-back of it (blind-spots.json: the Holy paladin's Holy Shock).
Written to duellab/seeds/r2/<class>-<tree slug>-<kind>.json; pvp_search_all.starts_for adds them to the tree's starts.

    python _reference/data/duellab/round2_seeds.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "seeds" / "r2"


def slug(s):
    return "".join(c for c in s.lower().replace(" ", "-") if c.isalnum() or c == "-")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    extra = json.loads((HERE / "results-1117.json").read_text(encoding="utf-8"))
    bs = json.loads((HERE / "blind-spots.json").read_text(encoding="utf-8"))["trees"]
    sig = json.loads((HERE.parent / "signature_spells.json").read_text(encoding="utf-8"))
    n = 0
    for f in sorted((HERE / "search").glob("*.json")):
        r = json.loads(f.read_text(encoding="utf-8"))
        cls, tree = r["class"], r["tree"]
        key = f"{cls}:{tree}"
        builds = {"winner": {k: v for k, v in r["final"].items() if v}}
        im = (extra.get("improved") or {}).get(key)
        if im and im.get("adopt"):
            builds["improved"] = im["allocation"]
        bg = (extra.get("battleground") or {}).get(key)
        if bg:
            builds["battleground"] = bg["allocation"]
        need = [s for s in sig.get(cls, {}).get(tree, {}).get("required", []) if s in {row["talent"] for row in bs.get(key, {}).get("rows", [])}]
        for s in need:   # the winner lacks a signature talent: the check put it back (cheapest payment)
            row = next(x for x in bs[key]["rows"] if x["talent"] == s)
            builds[f"signature-{slug(s)}"] = row["allocation"]
        for kind, al in builds.items():
            p = OUT / f"{cls}-{slug(tree)}-{kind}.json"
            p.write_text(json.dumps({"id": f"r2-{cls}-{slug(tree)}-{kind}", "class": cls, "tree": tree, "kind": kind,
                                     "allocation": al}, indent=1) + "\n", encoding="utf-8")
            n += 1
    print(f"wrote {n} round-2 starts to {OUT}")


if __name__ == "__main__":
    main()
