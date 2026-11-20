"""Two of the official simulator's own builds added as credited raid builds (2026-11-20, the audit session's calls after the parity races in
the lanes' setup; "Simulator build first" in CLAUDE.md):
- Retribution's Unsealed Wrath build (wowsims/forever ui/specs/paladin/retribution/builds/unsealed_wrath.siml, 14/6/31) in ret-dps. Under
  our raid rotation (ours leads the simulator's Default rotation by 0.75% on both seeds) our open-search build leads it by only 0.25% /
  0.22% (769.3 against 767.4 / 767.6, 10,000 fights): under the 0.5% bar. The dead-talent test (the audit's condition): Unsealed Wrath is
  worth 14.9% in it under our rotation (767.4 against 667.7 without it), so it is live and the simulator's build is the starting pick;
  our build is derived, so the pages' DERIVED_BAR puts the simulator's first while ours leads by less than 0.5%.
- Marksmanship's Lone Wolf build (ui/specs/hunter/dps/builds/mm.siml, 5/41/5) in mm-lonewolf-raid: a tie with ours there under the new
  turret base (963.6 / 963.6 against mm-lone-wolf-raid's 962.8 / 963.3), so race-all ranks it with the others.

    python _reference/data/deep-runs/add_sim_builds_1120.py [--write]
"""
import argparse
import json
import pathlib
import re
import sys

DATA = pathlib.Path(__file__).resolve().parents[1]
ROOT = DATA.parents[1]
sys.path[:0] = [str(DATA), str(DATA / "raidsim")]
SIM = "https://github.com/wowsims/forever/blob/2e6e77d844dc4d6790f984b9a1817fc583f7ca2e/"
NOTE_CREDIT = ("The simulator's own build, credited (Simulator build first, 2026-11-20): the page starts from it; ours replaces it only when 0.5% "
               "ahead on two seeds and passing the spec's rules.")
NOTE_SIM = "Simulator numbers are the community's model of the game, not in-game measurements."
NEW = [
    {"cls": "paladin", "entry": "ret-dps", "id": "retribution-unsealed-wrath-raid", "preset": "Unsealed Wrath", "spec": "Retribution",
     "talents": "050250002-501-05233011201301351",
     "name": "Retribution — Unsealed Wrath (the simulator's own build)",
     "summary": ("The official wowsims/forever simulator's own Retribution build (Unsealed Wrath, 14/6/31): Seal of Command and Seal of "
                 "Righteousness twisted for Unsealed Wrath's stored seals, Holy Strike, Consecration, judgements. In a full raid under our "
                 "raid rotation (2026-11-20, 10,000 fights, seeds 1 / 2): 767.4 / 767.6 against our open-search build's 769.3 / 769.3, "
                 "within 0.3%; Unsealed Wrath is worth 14.9% of it there (667.7 without the talent)."),
     "source": SIM + "ui/specs/paladin/retribution/builds/unsealed_wrath.siml",
     "extra_notes": ["Within 0.3% of our open-search build (769.3) under the same rotation: Retribution's full search of the optimality pass, "
                     "with the seal-twist knob in the rotation search, settles which leads."]},
    {"cls": "hunter", "entry": "mm-lonewolf-raid", "id": "marksmanship-lone-wolf-sim-raid", "preset": "MM", "spec": "Marksmanship",
     "talents": "5-0053452511522051-5",
     "name": "Marksmanship — Lone Wolf (the simulator's own build)",
     "summary": ("The official wowsims/forever simulator's own Marksmanship build (MM, 5/41/5), played without a pet (Lone Wolf) in the "
                 "mm-lonewolf-raid entry on the simulator's own turret rotation: 963.6 / 963.6 in a full raid against our Lone Wolf build's "
                 "962.8 / 963.3 (2026-11-20, 10,000 fights, seeds 1 / 2): a tie."),
     "source": SIM + "ui/specs/hunter/dps/builds/mm.siml", "extra_notes": []},
]


def tree_data(cls):
    return json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]


def make(spec):
    import render_rotations as rr
    flat = {n: r for n, r in rr.decode(spec["cls"], spec["talents"]).items() if r}
    trees = tree_data(spec["cls"])
    where = {t["name"]: (tr["name"], t.get("row", 0), t) for tr in trees for t in tr["talents"]}
    unknown = [n for n in flat if n not in where]
    if unknown:
        raise SystemExit(f"{spec['id']}: talents not in our data: {unknown}")
    alloc = {tr["name"]: [[t["name"], flat[t["name"]]] for t in tr["talents"] if flat.get(t["name"])] for tr in trees}
    main = spec["spec"]
    deep = sorted((n for n in flat if where[n][0] == main), key=lambda n: -where[n][1])[:5]

    def why(n):
        t = where[n][2]
        txt = (t.get("ranks") or [""])[-1].replace("\n", " ")
        return re.split(r"(?<=\.)\s", txt, maxsplit=1)[0].rstrip(".")
    return {"id": spec["id"], "name": spec["name"], "role": "dps", "content": "raid", "tier": "draft", "spec": spec["spec"],
            "preset": spec["preset"], "summary": spec["summary"], "allocation": alloc,
            "core": [{"talent": n, "why": why(n)} for n in deep], "flex": [],
            "notes": [NOTE_CREDIT] + spec["extra_notes"] + [NOTE_SIM], "sources": [spec["source"]]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    import builds_io as BIO
    from filelock import locked
    for spec in NEW:
        b = make(spec)
        pts = {t: sum(r for _, r in v) for t, v in b["allocation"].items()}
        print(f"{spec['cls']} {b['id']}: {pts}, core {[c['talent'] for c in b['core']]}")
        if a.write:
            BIO.update(spec["cls"], add=[b])
    if not a.write:
        return
    sp = DATA / "raidsim" / "specs.json"
    with locked(sp.with_suffix(".json.lock")):
        text = sp.read_text(encoding="utf-8")
        d = json.loads(text)
        for spec in NEW:
            e = d[spec["cls"]][spec["entry"]]
            if spec["id"] in e["builds"]:
                continue
            # a text edit (the file's layout): the entry's "builds" list gains the id at its end
            h = text.index(f'"{spec["cls"]}": {{')
            i = text.index(f'"{spec["entry"]}": {{', h)
            j = text.index('"builds": [', i)
            k = text.index("]", j)
            inner = text[j + len('"builds": ['):k]
            new_inner = inner.rstrip() + (", " if inner.strip() else "") + f'"{spec["id"]}"' + ("\n      " if "\n" in inner else "")
            text = text[:j + len('"builds": [')] + new_inner + text[k:]
            print(f"specs.json: {spec['cls']} {spec['entry']} builds + {spec['id']}")
        d2 = json.loads(text)
        for spec in NEW:
            assert spec["id"] in d2[spec["cls"]][spec["entry"]]["builds"]
        sp.write_text(text, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
