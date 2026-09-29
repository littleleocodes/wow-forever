"""Every build judged in its own scenario: which talents do nothing there, and what the points would buy instead.

    python _reference/data/scorer/scenario_audit.py [classes] [--game forever|classic-era|both] [--write]

Each build is scored with the spec model and profile of its scenario (raid DPS, raid tank, raid healer, leveling, solo at 60,
AoE grinding, PvP): an optimizer build names them in its id (opt-<model>-<profile>); a hand draft gets them from the
pipeline metadata (fight lab, raid sim, healer lab, PvP check) or from BUILD_MODEL below. For each talent the audit computes
its removal value (the score lost without it, in that scenario) and flags

  dead      no value in this scenario (the kind of value it gives is weighted to zero here: a kiting root for a melee,
            parry behind a raid boss, a pet talent without a pet, a heal for a Moonkin) and not needed for tier gating
  filler    no value, but the tree needs the points to unlock a deeper talent (fine; the least-bad filler is named)

and names the best legal use of the same points (the highest next-rank value among talents the build could take).
The page is `_reference/scenario-audit.md` (generated). Values are the scorer's (calibrated to the fight lab, the community
raid simulator and the healer lab where those measure the talent); PvP values are assumptions (scorer/pvp_check.py).
"""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "_reference/data"))

CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
PROFILES = ["leveling-st", "leveling-aoe", "solo-60", "raid-dps-extwc", "raid-dps", "raid-heal", "raid-tank", "parse", "pvp"]
DEAD = 0.0005    # a talent worth less than 0.05 points of score in its scenario does nothing there

# hand drafts whose model the pipeline metadata does not name: (model, profile)
BUILD_MODEL = {
    "druid": {"leveling-feral": ("feral-cat-dps", "leveling-st"), "feral-bear-tank": ("feral-bear-tank", "raid-tank"), "feral-cat-dps": ("feral-cat-dps", "raid-dps"),
              "balance-moonkin-raid": ("balance-dps", "raid-dps"), "resto-raid-healer": ("resto-heal", "raid-heal"), "resto-regrowth-natures-grace": ("resto-heal", "raid-heal"),
              "resto-swiftmend-healer": ("resto-heal", "raid-heal"), "pvp-resto": ("resto-heal", "pvp"), "pvp-resto-feral-hybrid": ("resto-heal", "pvp")},
    "hunter": {"leveling-beast-mastery": ("bm-leveling", "leveling-st"), "leveling-melee": ("melee-dps", "leveling-st"), "melee-survival-raid": ("melee-dps", "raid-dps"),
               "bm-mm-raid": ("mm-raid", "raid-dps"), "mm-lone-wolf-raid": ("mm-lonewolf-raid", "raid-dps"), "survival-melee": ("melee-dps", "raid-dps"),
               "bm-solo-farm": ("bm-leveling", "solo-60"), "mm-surv-hit-raid": ("mm-raid", "raid-dps"), "pvp-mm-surv": ("mm-raid", "pvp")},
    "mage": {"leveling-frost": ("frost-leveling", "leveling-st"), "pvp-frost": ("frost-leveling", "pvp")},
    "paladin": {"leveling-retribution": ("ret-dps", "leveling-st"), "ret-raid-dps": ("ret-dps", "raid-dps"), "holy-raid-healer": ("holy-heal", "raid-heal"),
                "prot-tank": ("prot-tank", "raid-tank"), "pvp-shockadin": ("holy-heal", "pvp")},
    "priest": {"leveling-shadow": ("shadow-dps", "leveling-st"), "shadow-pvp": ("shadow-dps", "pvp"), "pvp-shadow": ("shadow-dps", "pvp")},
    "rogue": {"leveling-combat-swords": ("combat-swords-raid", "leveling-st"), "combat-swords-raid": ("combat-swords-raid", "raid-dps"),
              "combat-daggers-raid": ("combat-daggers-raid", "raid-dps"), "pvp-seal-fate-daggers": ("combat-daggers-raid", "pvp"), "pvp-hemo-prep": ("combat-swords-raid", "pvp"),
              "assassination-mutilate-raid": (None, None)},   # no Mutilate model: the swords model would call its poison talents dead
    "shaman": {"leveling-enhancement": ("enhancement-dps", "leveling-st"), "pvp-elemental-ns": ("elemental-dps", "pvp")},
    "warlock": {"leveling-affliction": ("affliction-leveling", "leveling-st"), "leveling-affliction-demo": ("affliction-leveling", "leveling-st"), "pvp-soul-link": ("affliction-leveling", "pvp")},
    "warrior": {"leveling-arms": ("arms-2h-raid", "leveling-st"), "arms-pvp": ("arms-2h-raid", "pvp"), "prot-raid-tank": ("prot-tank", "raid-tank")},
}
KEYWORDS = [("heal", "raid-heal"), ("tank", "raid-tank")]


def guess(cls, b, models):
    """(model, profile) for a hand draft without an entry: the content picks the profile, the id's words pick the model."""
    bid = b["id"]
    if bid in BUILD_MODEL.get(cls, {}):
        return BUILD_MODEL[cls][bid]
    content, role = b.get("content"), b.get("role")
    profile = {"leveling": "leveling-st", "solo": "solo-60", "pvp": "pvp", "dungeon": "raid-tank"}.get(content) or {"healer": "raid-heal", "tank": "raid-tank"}.get(role, "raid-dps")
    words = set(re.split(r"[-_ ]", bid))
    best, best_n = None, 0
    for m in models:
        n = len(words & set(re.split(r"[-_ ]", m)))
        if role == "healer" and "heal" in m:
            n += 2
        if role == "tank" and "tank" in m:
            n += 2
        if n > best_n:
            best, best_n = m, n
    return (best, profile) if best else (None, None)


def simulator_only(cls):
    """Builds raced only in a rotation-only raid entry (raidsim/specs.json): simulator-searched builds of a tree or hybrid no scorer
    spec model covers (the Frostfire mage, 2026-09-28). The audit has no model to judge them with, so it leaves them out."""
    sp = json.load(open(ROOT / "_reference/data/raidsim/specs.json", encoding="utf-8")).get(cls, {})
    return {bid for e in sp.values() if isinstance(e, dict) and e.get("rotation_only") for bid in e.get("builds", [])}


def model_profile(cls, b, models):
    bid = b["id"]
    if bid in simulator_only(cls):
        return None, None
    if bid.startswith("opt-"):
        rest = bid[4:]
        for p in sorted(PROFILES, key=len, reverse=True):
            if rest.endswith("-" + p) and rest[: -len(p) - 1] in models:
                return rest[: -len(p) - 1], p
    return guess(cls, b, models)


def audit_build(opt, alloc):
    base = opt.score(alloc, 60)
    rows = []
    for name, r in sorted(alloc.items()):
        trial = {k: v for k, v in alloc.items() if k != name}
        value = base - opt.score(trial, 60)
        needed = not opt.tree.legal(trial)   # removing it breaks gating or a prerequisite
        rows.append((name, r, value, needed))
    marg = opt._marginals(dict(alloc), 60, None)
    legal_next = sorted(((v, n) for n, v in marg.items() if opt.tree.can_add(dict(alloc), n)), reverse=True)   # tier gating and prerequisites
    return base, rows, legal_next[:3]


def reason(opt, name):
    """Why a talent is worth nothing here: the kind weight, the pet rule or the scenario scope."""
    e = opt.effects.get(name, {})
    ev = opt.evaluator(60)
    kinds = e.get("kinds") or {}
    parts = []
    for ch, k in kinds.items():
        w = ev.kind_w.get(k, 1.0)
        if w == 0:
            parts.append(f"{k} counts 0 here")
    if e.get("needs_pet"):
        parts.append("needs " + ("a pet" if e["needs_pet"] is True else f"the {e['needs_pet']}"))
    return "; ".join(parts)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--game", default="both", choices=["forever", "classic-era", "both"])
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    from optimize import Optimizer
    games = ["forever", "classic-era"] if a.game == "both" else [a.game]
    out = {}
    for game in games:
        for cls in (a.classes or CLASSES):
            models = list(json.load(open(HERE / "specs" / f"{cls}.json", encoding="utf-8"))["models"])
            path = ROOT / cls / ("research/talents/forever/proposed-builds.json" if game == "forever" else "research/talents/classic-baseline/builds.json")
            cache = {}
            for b in json.load(open(path, encoding="utf-8"))["builds"]:
                model, profile = model_profile(cls, b, models)
                if not model:
                    out.setdefault((game, cls), []).append({"id": b["id"], "skip": "no model"})
                    continue
                key = (model, profile)
                if key not in cache:
                    try:
                        cache[key] = Optimizer(game, cls, model, profile)
                    except Exception as ex:  # noqa: BLE001
                        cache[key] = ex
                opt = cache[key]
                if isinstance(opt, Exception):
                    out.setdefault((game, cls), []).append({"id": b["id"], "skip": str(opt)[:80]})
                    continue
                alloc = {n: r for items in b["allocation"].values() for n, r in items}
                base, rows, nxt = audit_build(opt, alloc)
                dead = [(n, r, v, need, reason(opt, n)) for n, r, v, need in rows if v < DEAD]
                out.setdefault((game, cls), []).append({"id": b["id"], "model": model, "profile": profile, "content": b.get("content"), "score": base,
                                                        "dead": dead, "next": nxt})
                tag = f"{game[:7]:7s} {cls:8s} {b['id']:36s} {model:20s} {profile:12s}"
                flags = [f"{n} {r}{' (filler)' if need else ''}" for n, r, v, need, _ in dead]
                print(tag + ("  dead: " + ", ".join(flags) if flags else "  clean"))
    if a.write:
        write_page(out)


def write_page(out):
    lines = ["# Scenario audit", "",
             "> Generated by `_reference/data/scorer/scenario_audit.py --write`. Every build scored in its own scenario (the spec model and profile its id",
             "> or the pipeline names): talents worth nothing there are listed, as **dead** (free points: move them) or *filler* (worth nothing but needed to",
             "> unlock a deeper tier or a prerequisite). \"Best next point\" is the most valuable talent rank the build could still add, in the same scenario.",
             "> Values are the scorer's (calibrated to the fight lab, the community raid simulator and the healer lab where they measure the talent);",
             "> PvP values are assumptions. A talent can be dead because its kind of value counts nothing in the scenario (kiting for a melee, avoidance",
             "> behind a raid boss), because it needs a pet the build does not have, or because the scenario never uses it.", ""]
    for (game, cls), rows in sorted(out.items(), key=lambda kv: (kv[0][1], kv[0][0] != "forever")):
        lines += [f"## {cls} — {'Forever' if game == 'forever' else 'Classic Era'}", "",
                  "| Build | Scenario (model / profile) | Dead points | Filler points | Best next point |", "|---|---|---|---|---|"]
        for r in rows:
            if r.get("skip"):
                lines.append(f"| {r['id']} | not scored ({r['skip']}) | | | |")
                continue
            dead = ", ".join(f"{n} {k}" + (f" ({why})" if why else "") for n, k, v, need, why in r["dead"] if not need) or "-"
            fill = ", ".join(f"{n} {k}" for n, k, v, need, why in r["dead"] if need) or "-"
            nxt = ", ".join(f"{n} {v * 100:+.2f}" for v, n in r["next"][:2]) or "-"
            lines.append(f"| {r['id']} | {r['model']} / {r['profile']} | {dead} | {fill} | {nxt} |")
        lines.append("")
    lines += ["---", "*Generated file — do not edit by hand.*", ""]
    (ROOT / "_reference" / "scenario-audit.md").write_text("\n".join(lines), encoding="utf-8")
    print("wrote _reference/scenario-audit.md")


if __name__ == "__main__":
    main()
