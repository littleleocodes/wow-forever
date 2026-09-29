"""Specs and modes (2026-09-29, user request: "each class's 3 specs get a build for each of the 3 modes: leveling, raid/dummy/parse,
PvP; a split like 0/29/22 is its own hybrid section").

The one place that decides which spec a build belongs to (render_modes.py and spec_builds.py use it):

- a tank build belongs to the class's tank tree (Protection, Feral Combat), a healer build to its healing tree (the one of Holy /
  Discipline / Restoration it spends most in): a role, whatever the split;
- otherwise the tree with 30 or more points is the spec;
- otherwise the build is a hybrid of its two biggest trees, named in the class's tree order ("Fire/Frost");
- a build's own `spec` field overrides all of this: builds played around another tree's spells are filed as hybrids although one
  tree has 30 points (Frostfire 0/35/16 casts Frostfire Bolt; Shockadin 31/0/20 heals and shocks as a melee; Smite 31/17/3 is a
  Discipline build that casts Holy spells). The user left the judgment to us (2026-09-29).

Modes: leveling (content leveling or solo), raid (raid or dungeon: the training dummy and the parse/raid setting), pvp.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
MODES = ("leveling", "raid", "pvp")
MODE_TITLE = {"leveling": "Leveling", "raid": "Raid (training dummy and parse)", "pvp": "PvP"}
SPEC_POINTS = 30
HEAL_TREES = {"priest": ("Holy", "Discipline"), "paladin": ("Holy",), "shaman": ("Restoration",), "druid": ("Restoration",)}
TANK_TREE = {"warrior": "Protection", "paladin": "Protection", "druid": "Feral Combat"}
# healer and tank specs level as a damage spec and respec at 60 (agreed 2026-09-29): the spec they level as
LEVEL_AS = {("druid", "Restoration"): "Feral Combat", ("paladin", "Holy"): "Retribution", ("paladin", "Protection"): "Retribution",
            ("priest", "Discipline"): "Shadow", ("priest", "Holy"): "Shadow", ("shaman", "Restoration"): "Enhancement",
            ("warrior", "Protection"): "Arms"}


def trees(cls):
    return [t["name"] for t in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"]]


def tree_points(cls, build):
    return {t: sum(r for _, r in build["allocation"].get(t, [])) for t in trees(cls)}


def mode_of(build):
    return {"leveling": "leveling", "solo": "leveling", "raid": "raid", "dungeon": "raid", "pvp": "pvp"}.get(build.get("content"), "raid")


def spec_of(cls, build):
    """The spec a build belongs to: a tree name, or 'Hybrid A/B'."""
    if build.get("spec"):
        return build["spec"]
    pts = tree_points(cls, build)
    if build.get("role") == "tank" and cls in TANK_TREE:
        return TANK_TREE[cls]
    if build.get("role") == "healer" and cls in HEAL_TREES:
        return max(HEAL_TREES[cls], key=lambda t: pts.get(t, 0))
    top = sorted(pts, key=lambda t: -pts[t])
    if pts[top[0]] >= SPEC_POINTS:
        return top[0]
    return "Hybrid " + "/".join(t for t in pts if t in top[:2])   # the class's tree order, so 22/29 and 29/22 share a section


def slug(spec):
    return spec.lower().replace("hybrid ", "hybrid-").replace("/", "-").replace(" ", "-")


def grid(cls, builds):
    """{spec: {mode: [build, ...]}} with the class's three trees first (empty where no build exists), hybrids after."""
    out = {t: {m: [] for m in MODES} for t in trees(cls)}
    for b in builds:
        out.setdefault(spec_of(cls, b), {m: [] for m in MODES})[mode_of(b)].append(b)
    return out
