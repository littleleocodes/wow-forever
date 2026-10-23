"""Derive one leveling build per spec in the fight lab (2026-09-30, user request: "each spec to have a leveling, raid and PvP spec that we
can best derive from everything"; healer and tank specs get their own leveling build and a comparison with the recommended spec).

    python _reference/data/derive_leveling.py [classes] [--only <tree>] [--fresh] [--write] [--jobs 4]

For every (class, tree), LEVEL below names the fight-lab rotation (spec string) and the scorer model that screens moves and orders the
talents. Per spec:
1. Starts: the spec's leveling builds (hand drafts and generated ones) and the scorer's best build with 30+ points in the tree under the
   model (spec_builds.forced_optimizer), with the scorer's leveling order.
2. A rotation written for this derivation (NEW_ROTATIONS: Arcane, Demonology, Destruction, Subtlety, the healer and tank specs) is tuned
   first on the fastest start (fightlab/rotation_opt.py --spec --build; rules in fightlab/rotations/<class>-<spec>.json).
3. fightlab/fl_talent_opt.py: local search at level 60 from the fastest start, 30+ points kept in the tree, then the level-weighted race
   (20-60, seed 3) against the incumbent: the best hand draft, else the generated build.
4. The user's replacement rule: the derived build becomes the spec's leveling build only when it is 2%+ faster than the hand draft
   (--min-gain); the hand draft stays as the alternative. Without a hand draft it replaces the generated build when it is faster.
   The signature rule (2026-10-22, signature_spells.json): fl_talent_opt.py keeps the talents that grant the tree's required spells and
   penalizes builds that do not play them; a result that fails the check is never written, and one that passes replaces a hand draft
   that fails it whatever the race says.
Records: `_reference/data/derived-leveling.json` (generated; one entry per spec, reused unless --fresh), candidates under
`<class>/research/leveling/fightlab/candidates/derived-<tree>.json`. --write puts winners into proposed-builds.json.
"""
import argparse
import datetime
from filelock import locked
import json
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path[:0] = [str(HERE / "scorer"), str(HERE)]
import paths  # noqa: E402
import spec_modes as SM  # noqa: E402
import spec_builds as SB  # noqa: E402
from fmt_json import dumps  # noqa: E402

OUT = HERE / "derived-leveling.json"
TODAY = datetime.date.today().isoformat()
# (class, tree) -> (fight-lab spec string, scorer model). Healer and tank trees borrow the damage model nearest their play for screening
# and the order; their rotation is their own where one exists. Restoration shaman and druid play the Enhancement and Cat rotations: with
# the Restoration raid build at 60 (2026-09-30, 600 fights) Enhancement 52.4 s per kill against Elemental 54.5 s, Cat 39.8 s against
# Balance 85.6 s.
LEVEL = {
    ("druid", "Balance"): ("balance-dps", "balance-dps"), ("druid", "Feral Combat"): ("feral-cat-dps", "feral-cat-dps"),
    ("druid", "Restoration"): ("feral-cat-dps", "feral-cat-dps"),
    ("hunter", "Beast Mastery"): ("bm-leveling", "bm-leveling"), ("hunter", "Marksmanship"): ("mm-raid", "mm-raid"),
    ("hunter", "Survival"): ("melee-dps", "melee-dps"),
    ("mage", "Arcane"): ("arcane-leveling", "frost-leveling"), ("mage", "Fire"): ("fire-leveling", "fire-leveling"),
    ("mage", "Frost"): ("frost-leveling", "frost-leveling"),
    ("paladin", "Holy"): ("holy-leveling", "ret-dps"), ("paladin", "Protection"): ("prot-leveling", "ret-dps"),
    ("paladin", "Retribution"): ("ret-dps", "ret-dps"),
    ("priest", "Discipline"): ("discipline-leveling", "shadow-dps"), ("priest", "Holy"): ("holy-leveling", "shadow-dps"),
    ("priest", "Shadow"): ("shadow-dps", "shadow-dps"),
    ("rogue", "Assassination"): ("combat-daggers-raid", "combat-daggers-raid"), ("rogue", "Combat"): ("combat-swords-raid", "combat-swords-raid"),
    ("rogue", "Subtlety"): ("subtlety-leveling", "combat-swords-raid"),
    ("shaman", "Elemental"): ("elemental-dps", "elemental-dps"), ("shaman", "Enhancement"): ("enhancement-dps", "enhancement-dps"),
    ("shaman", "Restoration"): ("enhancement-dps", "enhancement-dps"),
    ("warlock", "Affliction"): ("affliction-leveling", "affliction-leveling"), ("warlock", "Demonology"): ("demonology-leveling", "affliction-leveling"),
    ("warlock", "Destruction"): ("destruction-leveling", "affliction-leveling"),
    ("warrior", "Arms"): ("arms-2h-raid", "arms-2h-raid"), ("warrior", "Fury"): ("fury-dw-raid", "fury-dw-raid"),
    ("warrior", "Protection"): ("prot-leveling", "arms-2h-raid"),
}
NEW_ROTATIONS = {("mage", "arcane-leveling"), ("warlock", "demonology-leveling"), ("warlock", "destruction-leveling"),
                 ("rogue", "subtlety-leveling"), ("priest", "holy-leveling"), ("priest", "discipline-leveling"),
                 ("paladin", "holy-leveling"), ("paladin", "prot-leveling"), ("warrior", "prot-leveling")}
# further starts where the scorer's model is borrowed and misses the tree's own spells (candidate files, relative to the class's fight-lab
# candidates folder)
EXTRA_STARTS = {("mage", "Arcane"): ["arcane-blast-leveling-start.json"]}
PY = sys.executable


def sh(args, log):
    print("  $ " + " ".join(str(x) for x in args[1:4]) + " ...", flush=True)
    r = subprocess.run(args, capture_output=True, text=True)
    log.write(r.stdout + r.stderr)
    log.flush()
    tail = [ln for ln in r.stdout.splitlines() if ln.strip()][-4:]
    for ln in tail:
        print("    " + ln, flush=True)
    if r.returncode:
        print("    FAILED: " + r.stderr[-800:], flush=True)
    return r.returncode == 0


def save(cls, tree, rec):
    with locked(OUT.with_suffix(".lock")):
        old = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
        old.setdefault(cls, {})[tree] = rec
        OUT.write_text(json.dumps(old, indent=1) + "\n", encoding="utf-8")


def derive(cls, tree, a, log):
    spec, model = LEVEL[(cls, tree)]
    bp = paths.builds_json("forever", cls)
    builds = json.load(open(bp, encoding="utf-8"))["builds"]
    slot = SM.grid(cls, builds)[tree]["leveling"]
    hands = [b["id"] for b in slot if not b.get("generated")]
    gens = [b["id"] for b in slot if b.get("generated")]
    cdir = paths.fightlab_dir(cls) / "candidates"
    cdir.mkdir(parents=True, exist_ok=True)
    forced_p = cdir / f"derived-{SM.slug(tree)}-scorer.json"
    if a.fresh or not forced_p.exists():
        opt = SB.forced_optimizer(cls, model, "leveling-st", tree)
        flat, _ = opt.best_build(level=60)
        flat = {k: v for k, v in flat.items() if v}
        from optimize import Optimizer
        plain = Optimizer("forever", cls, model, "leveling-st")
        steps = plain.order(flat, lookahead=SB.LOOKAHEAD.get(cls, 16))
        forced_p.write_text(json.dumps({"id": f"derived-{SM.slug(tree)}-scorer", "allocation": SB.to_allocation(cls, flat),
                                        "order": [{"levels": lv, "tree": t, "talent": n, "points": p} for lv, t, n, p in plain.compress_order(steps)],
                                        "note": f"The scorer's best build with 30+ points in {tree} under {model} (leveling-st), {TODAY}."}, indent=1) + "\n",
                            encoding="utf-8")
    starts = hands + gens + [str(forced_p)] + [str(cdir / f) for f in EXTRA_STARTS.get((cls, tree), [])]
    incumbent = hands[0] if hands else (gens[0] if gens else str(forced_p))
    rec = {"spec": spec, "model": model, "tree": tree, "hands": hands, "generated": gens, "date": TODAY}
    if (cls, spec) in NEW_ROTATIONS and (a.fresh or not (HERE / "fightlab/rotations" / f"{cls}-{spec}.json").exists()):
        # tune the new rotation on the fastest start at level 60 (the scorer's build when nothing else exists)
        sh([PY, HERE / "fightlab/rotation_opt.py", cls, "--spec", spec, "--build", incumbent if hands else str(forced_p), "--write",
            "--jobs", str(a.jobs), "--rounds", "8"], log)
        rec["rotation_tuned"] = True
    cand = cdir / f"derived-{SM.slug(tree)}.json"
    args = [PY, HERE / "fightlab/fl_talent_opt.py", cls, "--spec", spec, "--model", model, "--tree", tree,
            "--jobs", str(a.jobs), "--write", str(cand)]
    for s in starts:
        args += ["--start", s]
    for s in (hands or [incumbent]):   # the race bar: the fastest hand draft (every hand draft races), else the generated build
        args += ["--incumbent", s]
    if not sh(args, log) or not cand.exists():
        rec["error"] = "search failed"
        return rec
    c = json.load(open(cand, encoding="utf-8"))
    s = c["search"]
    rec.update({"candidate": str(cand.relative_to(ROOT)), "search": s, "gain": s["race"]["gain"], "incumbent": s["incumbent"]})
    # the signature rule (2026-10-22, signature_spells.json; fl_talent_opt records the checks): a search result that does not play the
    # tree's signature spells is never written; one that does replaces a hand draft that does not, whatever the race says
    sg = s.get("signature") or {}
    cand_ok = (sg.get("search") or {}).get("ok", True)
    inc_ok = sg.get("incumbent_passes", True)
    rec["signature"] = {"search": (sg.get("search") or {}).get("verdict"), "incumbent": ((sg.get("incumbents") or {}).get(s["incumbent"]) or {}).get("verdict")}
    if hands:
        rec["verdict"] = "replaces" if cand_ok and (s["race"]["gain"] >= a.min_gain or not inc_ok) else "hand stays"
    else:
        # no hand draft: the spec always gets a derived build (the rotation may be new, so the old generated build's numbers are stale),
        # holding the search's result or, when that lost the race (or fails the signature rule while the old build passes), the old build's talents
        rec["verdict"] = "new"
        rec["keep_incumbent"] = (s["race"]["gain"] <= 0 and (inc_ok or not cand_ok)) or (not cand_ok and inc_ok)
    won = rec["verdict"] == "replaces" or (rec["verdict"] == "new" and not rec.get("keep_incumbent"))
    rec["levels"] = {str(L): v for L, v in (s["race"]["search"][1] if won else s["race"]["incumbent"][1]).items()}
    return rec


def build_of(cls, tree, rec, c):
    spec, model = rec["spec"], rec["model"]
    s = rec["search"]
    heal_tank = (cls, tree) in SM.LEVEL_AS
    moves = "; ".join(m["move"] for m in s["moves"]) or "none (the start was already the best the search found)"
    b = {"id": f"{SM.slug(tree)}-leveling", "name": f"{tree} — Leveling (derived)", "role": "dps", "content": "leveling", "tier": "draft",
         "spec": tree, "generated": TODAY, "derived": "leveling",
         "summary": (f"The {tree} leveling build derived on {TODAY} (derive_leveling.py): searched in the fight lab at level 60 from the fastest "
                     f"of the spec's builds and the stats model's best {tree} build, 30+ points kept in {tree}, playing the {spec} rotation; "
                     f"the talent order is the stats model's ({model})."
                     + (f" {tree} is a {'healing' if tree in SM.HEAL_TREES.get(cls, ()) else 'tanking'} spec: this is how to level while "
                        f"keeping it, compared with {SM.LEVEL_AS[(cls, tree)]} on the leveling page." if heal_tank else "")),
         "allocation": c["allocation"], "order": c["order"], "core": SB.core_of(cls, model, "leveling-st", {n: r for it in c["allocation"].values() for n, r in it}),
         "flex": [],
         "notes": [f"Fight-lab talent search (fightlab/fl_talent_opt.py): start {pathlib.Path(s['start']).stem}, moves: {moves}. Race against "
                   f"{s['incumbent']} over levels 20-60 (seed 3, {s['confirm']} fights per level): {s['race']['gain']:+.1%} faster per kill.",
                   "Fight-lab numbers are a model of the beta, not in-game measurements."],
         "open_questions": [f"A derived {tree} leveling build: check it while leveling at launch."],
         "sources": ["https://talentsforever.com/" + cls]}
    if rec["verdict"] == "replaces":
        b["replaces"] = rec["incumbent"]
        b["notes"].insert(0, f"{s['race']['gain']:+.1%} faster than the hand draft {rec['incumbent']}, over the replacement bar: this build "
                             f"is the spec's leveling pick, the hand draft stays as the alternative.")
    return b


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--only")
    ap.add_argument("--fresh", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--min-gain", type=float, default=0.005)   # the replacement bar: 0.5% since 2026-10-07 (2% before)
    ap.add_argument("--jobs", type=int, default=4)
    a = ap.parse_args()
    done = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    logdir = pathlib.Path(tempfile.gettempdir()) / "derive-leveling"
    logdir.mkdir(exist_ok=True)
    for cls in a.classes or SM.CLASSES:
        for tree in SM.trees(cls):
            if a.only and tree != a.only:
                continue
            if not a.fresh and done.get(cls, {}).get(tree, {}).get("verdict"):
                print(f"== {cls} {tree}: done ({done[cls][tree]['verdict']})", flush=True)
                continue
            print(f"== {cls} {tree}", flush=True)
            with open(logdir / f"{cls}-{SM.slug(tree)}.log", "w") as log:
                rec = derive(cls, tree, a, log)
            save(cls, tree, rec)
            print(f"  -> {rec.get('verdict', rec.get('error'))} ({rec.get('gain', 0):+.2%})", flush=True)
    if a.write:
        write_builds(a)


def write_builds(a):
    res = json.load(open(OUT, encoding="utf-8"))
    for cls, per in res.items():
        if a.classes and cls not in a.classes:
            continue
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        for tree, rec in per.items():
            if rec.get("verdict") not in ("replaces", "new"):
                continue
            c = json.load(open(ROOT / rec["candidate"], encoding="utf-8"))
            if rec.get("keep_incumbent"):   # the old build's talents and order, under the derived id and the spec's rotation
                inc = rec["incumbent"]
                cf = paths.fightlab_dir(cls) / "candidates" / f"{inc}.json"   # the scorer's start is a candidate file, recorded by its id
                src = next((x for x in data["builds"] if x["id"] == inc), None) or json.load(open(inc if inc.endswith(".json") else cf, encoding="utf-8"))
                c = dict(c, allocation=src["allocation"], order=src.get("order") or c["order"])
            b = build_of(cls, tree, rec, c)
            # the derived build takes the slot's generated build's place (a generated build is never kept next to it)
            data["builds"] = [x for x in data["builds"] if not (x.get("generated") and SM.spec_of(cls, x) == tree and SM.mode_of(x) == "leveling")
                              and x["id"] != b["id"]]
            data["builds"].append(b)
        bp.write_text(dumps(data) + "\n", encoding="utf-8")
        print(f"wrote {bp.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
