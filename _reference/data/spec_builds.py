"""Fill every empty spec x mode slot with a generated build (2026-09-29, user request: "each class's 3 specs get a build for each of
the 3 modes").

    python _reference/data/spec_builds.py [classes] [--dry-run] [--fresh]

For every (class, tree, mode) with no build (spec_modes.grid; healer and tank trees level as another spec, spec_modes.LEVEL_AS, so they
get no leveling build) this writes a build `<tree>-<mode>` into proposed-builds.json:

- leveling: the scorer's best build with 30+ points in the tree under the class's nearest leveling model (MODEL below), the scorer's
  leveling order, then the fight lab at levels 20-60 under that model (its rotation) for the numbers the pages show;
- raid: the scorer's best such build under the nearest raid model, refined in the community simulator by raidsim/talent_opt.py in the
  nearest raid entry with --min-tree <tree>=30 (training dummy);
- pvp: the scorer's best such build under the PvP profile (an assumption: no simulator plays PvP).

Each generated build says so in its summary and notes and carries `spec` (its tree) and `generated`. Numbers:
`_reference/data/spec-builds.json` (generated). Re-running replaces the generated builds (never a hand draft).
"""
import argparse
import datetime
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
from fmt_json import dumps  # noqa: E402

OUT = HERE / "spec-builds.json"
TODAY = datetime.date.today().isoformat()
LEVELS = [20, 30, 40, 50, 60]
# Protection PvP builds are scored on a damage model (the tank model's "burst" would be threat, meaningless in PvP), 30+ points kept in
# Protection. Trees without a scorer model of their own borrow the nearest one: their own spells are under-valued, and the build says so.
ROUGH = {("mage", "Arcane"): "No Arcane model exists: scored with the Frost leveling model, whose damage is mostly Frostbolt, so talents "
                             "that raise Arcane spells are under-valued (leveling: the fight lab plays Frost's priority list).",
         ("rogue", "Subtlety"): "Scored with the Combat swords model (no Subtlety leveling model): Subtlety's openers and Hemorrhage are under-valued.",
         ("warlock", "Demonology"): "Scored with the Affliction leveling model (no Demonology leveling model): demon talents count only as far as that model's pet share.",
         ("warlock", "Destruction"): "Scored with the Affliction leveling model (no Destruction leveling model): fire spells are under-valued.",
         ("hunter", "Survival"): "Scored with the melee hunter model (the only Survival model): a ranged Survival PvP hunter is not modelled.",
         ("paladin", "Protection"): "Scored with the Retribution damage model (PvP values damage, not threat), keeping 30+ points in Protection.",
         ("warrior", "Protection"): "Scored with the Arms damage model (PvP values damage, not threat), keeping 30+ points in Protection."}
# the scorer model (and, for raid, the simulator entry) nearest to each tree, per mode
MODEL = {
    ("druid", "Balance"): {"leveling": "balance-dps", "raid": ("balance-dps", "balance-dps"), "pvp": "balance-dps"},
    ("druid", "Feral Combat"): {"leveling": "feral-cat-dps", "raid": ("feral-cat-dps", "feral-cat-dps"), "pvp": "feral-cat-dps"},
    ("druid", "Restoration"): {"raid": ("resto-heal", None), "pvp": "resto-heal"},
    ("hunter", "Beast Mastery"): {"leveling": "bm-leveling", "raid": ("bm-leveling", "bm-raid"), "pvp": "bm-leveling"},
    ("hunter", "Marksmanship"): {"leveling": "mm-raid", "raid": ("mm-raid", "mm-raid"), "pvp": "mm-raid"},
    ("hunter", "Survival"): {"leveling": "melee-dps", "raid": ("melee-dps", "melee-dps"), "pvp": "melee-dps"},
    ("mage", "Arcane"): {"leveling": "frost-leveling", "raid": ("frost-raid", "arcane-dps"), "pvp": "frost-leveling"},
    ("mage", "Fire"): {"leveling": "fire-leveling", "raid": ("fire-raid", "fire-raid"), "pvp": "fire-leveling"},
    ("mage", "Frost"): {"leveling": "frost-leveling", "raid": ("frost-raid", "frost-raid"), "pvp": "frost-leveling"},
    ("paladin", "Holy"): {"raid": ("holy-heal", None), "pvp": "holy-heal"},
    ("paladin", "Protection"): {"raid": ("prot-tank", None), "pvp": "ret-dps"},
    ("paladin", "Retribution"): {"leveling": "ret-dps", "raid": ("ret-dps", "ret-dps"), "pvp": "ret-dps"},
    ("priest", "Discipline"): {"raid": ("holy-heal", None), "pvp": "holy-heal"},
    ("priest", "Holy"): {"raid": ("holy-heal", None), "pvp": "holy-heal"},
    ("priest", "Shadow"): {"leveling": "shadow-dps", "raid": ("shadow-dps", "shadow-dps"), "pvp": "shadow-dps"},
    ("rogue", "Assassination"): {"leveling": "combat-daggers-raid", "raid": ("combat-daggers-raid", "assassination-raid"), "pvp": "combat-daggers-raid"},
    ("rogue", "Combat"): {"leveling": "combat-swords-raid", "raid": ("combat-swords-raid", "combat-swords-raid"), "pvp": "combat-swords-raid"},
    ("rogue", "Subtlety"): {"leveling": "combat-swords-raid", "raid": ("combat-swords-raid", "subtlety-raid"), "pvp": "combat-swords-raid"},
    ("shaman", "Elemental"): {"leveling": "elemental-dps", "raid": ("elemental-dps", "elemental-dps"), "pvp": "elemental-dps"},
    ("shaman", "Enhancement"): {"leveling": "enhancement-dps", "raid": ("enhancement-dps", "enhancement-dps"), "pvp": "enhancement-dps"},
    ("shaman", "Restoration"): {"raid": ("resto-heal", None), "pvp": "resto-heal"},
    ("warlock", "Affliction"): {"leveling": "affliction-leveling", "raid": ("affliction-raid", "affliction-raid"), "pvp": "affliction-leveling"},
    ("warlock", "Demonology"): {"leveling": "affliction-leveling", "raid": ("sb-raid", "demonology-raid"), "pvp": "affliction-leveling"},
    ("warlock", "Destruction"): {"leveling": "affliction-leveling", "raid": ("fire-destro-raid", "fire-destro-raid"), "pvp": "affliction-leveling"},
    ("warrior", "Arms"): {"leveling": "arms-2h-raid", "raid": ("arms-2h-raid", "arms-battle-raid"), "pvp": "arms-2h-raid"},
    ("warrior", "Fury"): {"leveling": "fury-dw-raid", "raid": ("fury-dw-raid", "fury-dw-raid"), "pvp": "fury-dw-raid"},
    ("warrior", "Protection"): {"raid": ("prot-tank", None), "pvp": "arms-2h-raid"},
}
LOOKAHEAD = {"mage": 12, "warrior": 20}
ROLE = {"heal": "healer", "tank": "tank"}


def forced_optimizer(cls, model, profile, tree):
    """The scorer with a bonus no talent can match while the tree holds 30+ points: its best build is the best spec build of that tree."""
    from optimize import Optimizer

    class Forced(Optimizer):
        def score(self, alloc, level=60, detail=False):
            s = super().score(alloc, level, detail)
            if detail:
                return s
            pts = sum(r for n, r in alloc.items() if self.tree.info.get(n, (None,))[0] == tree)
            return s + (1000.0 if pts >= SM.SPEC_POINTS else pts)   # climb toward 30, then the real score decides
    return Forced("forever", cls, model, profile)


def to_allocation(cls, flat):
    data = json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    return {tr["name"]: [[t["name"], flat[t["name"]]] for t in tr["talents"] if flat.get(t["name"])] for tr in data["trees"]}


def core_of(cls, model, profile, flat):
    """The talents the scorer values most in this build (removal value), for the page's core list."""
    from optimize import Optimizer
    opt = Optimizer("forever", cls, model, profile)
    base = opt.score(flat, 60)
    rows = sorted(((base - opt.score({k: v for k, v in flat.items() if k != n}, 60)) / max(abs(base), 1e-9), n) for n in flat)[::-1]
    return [{"talent": n, "why": f"The scorer's value in this build: {v * 100:+.1f}% of its score (model {model})."} for v, n in rows[:6] if v > 0]


def generate(cls, tree, mode, a, tmp):
    spec_map = MODEL[(cls, tree)]
    if mode == "raid":
        model, entry = spec_map["raid"]
    else:
        model, entry = spec_map.get(mode), None
    if not model:
        return None, None
    profile = {"leveling": "leveling-st", "raid": "raid-dps", "pvp": "pvp"}[mode]
    models = json.load(open(HERE / "scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"]
    if model.endswith("-heal"):
        profile = "raid-heal" if mode == "raid" else profile
    if model.endswith("-tank"):
        profile = "raid-tank" if mode == "raid" else profile
    opt = forced_optimizer(cls, model, profile, tree)
    flat, _ = opt.best_build(level=60)
    flat = {k: v for k, v in flat.items() if v}
    info = {"model": model, "profile": profile}
    if mode == "raid" and entry:   # refine in the simulator, keeping 30+ points in the tree
        start = pathlib.Path(tmp) / f"{cls}-{SM.slug(tree)}-start.json"
        start.write_text(json.dumps({"id": "start", "allocation": to_allocation(cls, flat)}), encoding="utf-8")
        cand = paths.raidsim_dir(cls) / "candidates" / f"cand-{entry}-spec-{SM.slug(tree)}.json"
        if a.fresh or not cand.exists():   # the search takes 20-40 minutes: a re-run reuses its candidate unless --fresh
            r = subprocess.run([sys.executable, str(HERE / "raidsim/talent_opt.py"), cls, "--spec", entry, "--start", str(start), "--setting", "dummy",
                                "--min-tree", f"{tree}={SM.SPEC_POINTS}", "--write", str(cand)], capture_output=True, text=True)
            print(r.stdout[-600:], r.stderr[-400:], flush=True)
        if cand.exists():
            c = json.load(open(cand, encoding="utf-8"))
            flat = {n: v for items in c["allocation"].values() for n, v in items if v}
            info.update({"entry": entry, "search": c.get("search")})
    role = next((v for k, v in ROLE.items() if model.endswith(k)), "dps")
    title = SM.MODE_TITLE[mode].split(" (")[0]
    b = {"id": f"{SM.slug(tree)}-{mode}", "name": f"{tree} — {title} (generated)", "role": role,
         "content": {"leveling": "leveling", "raid": "raid", "pvp": "pvp"}[mode], "tier": "draft", "spec": tree, "generated": TODAY,
         "summary": (f"The best {tree} {title.lower()} build with at least {SM.SPEC_POINTS} points in {tree}, generated on {TODAY} by "
                     f"spec_builds.py: the stats model's optimum ({model}, profile {profile})"
                     + (f", refined in the community simulator's talent search ({entry})" if info.get("entry") else "")
                     + ". No hand draft exists for this spec and mode yet; treat it as a starting point."),
         "allocation": to_allocation(cls, flat), "core": core_of(cls, model, profile, flat), "flex": [],
         "notes": [f"Generated {TODAY} (spec_builds.py) so every spec has a {title.lower()} build; model {model}, profile {profile}."
                   + (" PvP values are assumptions: no simulator plays PvP." if mode == "pvp" else "")]
                  + ([ROUGH[(cls, tree)]] if (cls, tree) in ROUGH and not (mode == "raid" and info.get("entry")) else []),
         "open_questions": [f"A generated {tree} build: check it against the community's {tree} builds at launch."],
         "sources": ["https://talentsforever.com/" + cls]}
    if mode == "leveling":
        from optimize import Optimizer
        plain = Optimizer("forever", cls, model, profile)
        steps = plain.order(flat, lookahead=LOOKAHEAD.get(cls, 16))
        b["order"] = [{"levels": lv, "tree": t, "talent": n, "points": pts} for lv, t, n, pts in plain.compress_order(steps)]
    return b, info


def fightlab_numbers(cls, bid, spec):
    """Time per kill at 20-60 in the fight lab, in a fresh process (the fight lab's modules clash with the raid sim's by name)."""
    code = (f"import sys,json; sys.path.insert(0, {str(HERE / 'fightlab')!r}); import run\n"
            f"b = run.load_build({cls!r}, {bid!r})\n"
            f"print(json.dumps({{L: run.simulate({cls!r}, run.allocation_at(b, L), L, {spec!r}, 1500, 1, 0)['time_per_kill'] for L in {LEVELS!r}}}))")
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    return json.loads(r.stdout.strip().splitlines()[-1]) if r.returncode == 0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--fresh", action="store_true", help="re-run the simulator talent searches instead of reusing their candidates")
    a = ap.parse_args()
    res = json.load(open(OUT, encoding="utf-8")) if OUT.exists() else {}
    for cls in a.classes or SM.CLASSES:
        bp = paths.builds_json("forever", cls)
        data = json.load(open(bp, encoding="utf-8"))
        data["builds"] = [b for b in data["builds"] if not b.get("generated")]   # re-generate from scratch
        g = SM.grid(cls, data["builds"])
        todo = [(t, m) for t in SM.trees(cls) for m in SM.MODES if not g[t][m] and not (m == "leveling" and (cls, t) in SM.LEVEL_AS)]
        print(f"== {cls}: {', '.join(f'{t} {m}' for t, m in todo) or 'nothing to fill'}", flush=True)
        if a.dry_run or not todo:
            continue
        with tempfile.TemporaryDirectory() as tmp:
            for t, m in todo:
                b, info = generate(cls, t, m, a, tmp)
                if not b:
                    print(f"  {t} {m}: no model", flush=True)
                    continue
                data["builds"].append(b)
                res.setdefault(cls, {})[b["id"]] = dict(info, spec=t, mode=m, date=TODAY)
                print(f"  {b['id']}: {'/'.join(str(sum(r for _, r in v)) for v in b['allocation'].values())}", flush=True)
        bp.write_text(dumps(data) + "\n", encoding="utf-8")
        for bid, info in res.get(cls, {}).items():
            if info["mode"] == "leveling" and "levels" not in info:
                info["levels"] = fightlab_numbers(cls, bid, info["model"])
        OUT.write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
