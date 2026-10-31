"""Level-60 raid builds through the official wowsims/forever simulator (the ElliotWood/Forever fork until 2026-10-18): DPS per talent build, one report per spec.

    python _reference/data/raidsim/run.py mage --spec frost-raid [--builds id ...] [--iterations 3000] [--duration 180] [--write]
    python _reference/data/raidsim/run.py --all --write            # every spec in specs.json

Needs the simulator checkout with the bench tool built (`setup.py`; default location %USERPROFILE%/.wow-forever-tools, or
--repo / the WOW_FOREVER_SIM environment variable). `specs.json` maps each of our scorer spec ids to the simulator's spec folder,
gear preset, rotation (APL), player options and consumables; the sim's own preset talent builds are raced alongside ours.
Talent strings are built from `<repo>/ui/sim/talents/trees/<class>.json` (same beta client as our data, names match).

Outputs (--write): `<class>/research/raid/raidsim/<spec>.md` and `.json` (generated). The simulator is the community's model of
the Forever beta (its own tests and presets); its numbers are simulations of that model, not measurements.
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data/scorer"))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import id_names  # noqa: E402  (spell and item names the simulator's lists miss)
import setup as SETUP  # noqa: E402  (the checkout path: setup.checkout)
import sim_info  # noqa: E402  (_reference/data/sim_info.py: which simulator and client a record ran on)
GAME = "forever"   # or "classic-era": set by main() from --game; every path below follows it
GAMES = {"forever": {"specs": "specs.json", "env": "WOW_FOREVER_SIM", "repo": "wowsims-forever", "bench": "foreverbench", "builds": "research/talents/forever/proposed-builds.json",
                     "trees": "ui/sim/talents/trees", "reports": "research/raid/raidsim", "name_key": "fancyName", "ui": "ui/specs"},
         "classic-era": {"specs": "specs-classic.json", "env": "WOW_FOREVER_CLASSIC_SIM", "repo": "classic-repo", "bench": "classicbench", "builds": "research/talents/classic-baseline/builds.json",
                         "trees": "ui/core/talents/trees", "reports": "research/talents/classic-baseline/raidsim", "name_key": "fieldName", "ui": "ui"}}
SPECS = json.load(open(HERE / "specs.json", encoding="utf-8"))


def set_game(game):
    global GAME, SPECS
    GAME = game
    SPECS = json.load(open(HERE / GAMES[game]["specs"], encoding="utf-8"))


def repo_path(a):
    g = GAMES[GAME]
    p = pathlib.Path(a.repo) if a.repo else SETUP.checkout("forever" if GAME == "forever" else "classic")   # setup.py: env override or <tools>/<dir>
    if not (p / f"{g['bench']}.exe").exists() and not (p / g["bench"]).exists():
        raise SystemExit(f"no bench tool in {p}: run _reference/data/raidsim/setup.py{' --game classic' if GAME != 'forever' else ''} (or pass --repo)")
    return p


def load_trees(repo, cls):
    return json.load(open(repo / GAMES[GAME]["trees"] / f"{cls}.json", encoding="utf-8"))


def field_name(name):
    """Our talent name as the upstream Classic simulator's camelCase field name (Nature's Grasp -> naturesGrasp)."""
    words = re.sub(r"[^A-Za-z0-9 ]", "", name.replace("'", "").replace("-", " ")).split()
    return words[0].lower() + "".join(w[:1].upper() + w[1:] for w in words[1:]) if words else ""


# talents the Forever client renamed before the simulator's data did: the simulator's name -> ours (2026-10-08: build 70291 renamed the
# druid's Predatory Instincts to Natural Instinct; the fork at 2ce8265 still uses the old name). Harmless once the fork renames it.
SIM_RENAMES = {"Predatory Instincts": "Natural Instinct"}


def talent_key(t):
    g = GAMES[GAME]
    if GAME != "forever":
        return t["fieldName"]
    n = t.get(g["name_key"])
    return SIM_RENAMES.get(n, n)


def talents_string(trees, alloc):
    """The sim's talent string: per tree the digit of every talent in the tree's listed order, trailing zeros and dashes trimmed."""
    conv = (lambda n: n) if GAME == "forever" else field_name
    known = {talent_key(t) for tr in trees for t in tr["talents"]}
    missing = [n for n in alloc if conv(n) not in known]
    if missing:
        raise SystemExit(f"talents unknown to the simulator: {missing}")
    a2 = {conv(n): r for n, r in alloc.items()}
    parts = []
    for tr in trees:
        digits = "".join(str(min(a2.get(talent_key(t), 0), t["maxPoints"])) for t in tr["talents"])
        parts.append(digits.rstrip("0"))
    return "-".join(parts).rstrip("-")


def alloc_of(build):
    return {n: r for items in build["allocation"].values() for n, r in items}


def split(build):
    return "/".join(str(sum(r for _, r in items)) for items in build["allocation"].values())


def sim_path(rel):
    """A gear set or rotation for the bench: a project file (`_reference/...`, our own: the melee hunter's gear, a base rotation)
    as an absolute path, else unchanged (relative to the simulator repository)."""
    return str(ROOT / rel) if rel and rel.replace("\\", "/").startswith("_reference/") else rel


RAID_SETTINGS = ("raid", "max", "max60")   # settings with the raid's buffs: they run the raid rotation


def apl_key(entry, where=None):
    """specs.json key of the rotation a setting runs: `apl_opt` for the training dummies (own buffs, short of mana),
    `apl_opt_raid` for the raid settings (full buffs); `where` defaults to the setting the spec is ranked in."""
    where = where or setting(entry)
    return "apl_opt_raid" if where in RAID_SETTINGS else "apl_opt"


def apl_path(entry, repo, where=None):
    """The rotation a spec runs in a setting: ours when specs.json names one for that kind of setting (written by apl_opt.py,
    the rotation search, 2026-09-27) and the file exists, else the simulator's own (`apl`, relative to the simulator repository)."""
    own = entry.get(apl_key(entry, where))
    if own and (ROOT / own).exists():
        return ROOT / own
    base = sim_path(entry["apl"])
    return pathlib.Path(base) if pathlib.Path(base).is_absolute() else repo / entry["apl"]


def apl_label(entry, repo, where=None):
    p = apl_path(entry, repo, where)
    return p.relative_to(ROOT).as_posix() if str(p).startswith(str(ROOT)) else entry["apl"]


def rotation_only(entry):
    """A talent tree none of the scorer's spec models covers (specs.json `rotation_only`): raced and given a tuned rotation, never
    calibrated or optimized."""
    return bool(entry.get("rotation_only"))


def sim_presets(repo, entry):
    """Talent presets of the sim's spec folder. The official wowsims/forever presets.ts files (2026-10-22) use four forms:
    makePresetTalents('N', SavedTalents.create({ talentsString: '...' })) (the string or `<Json>.player.talentsString` of an imported
    build file), talentsOf('N', <Json>), talents('N', '...') and { name: 'N', data: SavedTalents.create({ talentsString: ... }) }; the
    first literal form alone missed the hunter, rogue, priest, warlock and shaman presets."""
    path = repo / GAMES[GAME]["ui"] / entry["sim_spec"] / "presets.ts"
    if not path.exists():
        return []
    s = path.read_text(encoding="utf-8")
    imports = {m.group(1): path.parent / m.group(2) for m in re.finditer(r"import\s+(\w+)\s+from\s+'(\.[^']+\.json)'", s)}

    def value(expr):
        expr = expr.strip()
        m = re.fullmatch(r"'([^']*)'", expr)
        if m:
            return m.group(1)
        m = re.fullmatch(r"(\w+)(?:\.player\.talentsString)?", expr)
        if m and m.group(1) in imports and imports[m.group(1)].exists():
            return (json.load(open(imports[m.group(1)], encoding="utf-8")).get("player") or {}).get("talentsString")
        return None
    out = []
    pats = [r"makePresetTalents\(\s*'([^']+)'\s*,\s*SavedTalents\.create\(\{\s*talentsString:\s*([^}]+?)\s*,?\s*\}\)",
            r"\btalentsOf\(\s*'([^']+)'\s*,\s*(\w+)\s*\)",
            r"\btalents\(\s*'([^']+)'\s*,\s*('[^']*')\s*\)",
            r"\{\s*name:\s*'([^']+)'\s*,\s*data:\s*SavedTalents\.create\(\{\s*talentsString:\s*([^}]+?)\s*,?\s*\}\)"]
    for pat in pats:
        for m in re.finditer(pat, s, re.S):
            v = value(m.group(2))
            if v is not None and f"sim preset: {m.group(1)}" not in [x["label"] for x in out]:
                out.append({"label": f"sim preset: {m.group(1)}", "talents": v})
    if "preset_names" in entry:   # a rotation-only tree: only its own presets
        out = [p for p in out if p["label"][len("sim preset: "):] in entry["preset_names"]]
    return out


PRESET_MARGIN = 0.06   # a simulator preset within 6% of the spec's best build in its last race competes (write_preset_candidates)


def preset_allocation(trees, talents):
    """The simulator's talent string -> our allocation {tree: [[talent, rank], ...]} (the inverse of talents_string)."""
    out = {}
    for tr, part in zip(trees, (talents or "").split("-")):
        items = [[talent_key(t) or t["fieldName"], int(ch)] for t, ch in zip(tr["talents"], part) if ch != "0"]
        if items:
            out[tr["name"]] = items
    return out


def preset_slug(label):
    return re.sub(r"[^a-z0-9]+", "-", label.split(": ", 1)[-1].lower()).strip("-")


def write_preset_candidates(cls, spec, repo, margin=PRESET_MARGIN):
    """Save the simulator's presets that compete with our builds as raid candidates `cand-<spec>-preset-<name>.json` (2026-09-27):
    a preset within `margin` of the best build of the spec's last race (DPS on the training dummy, tank value for tanks). The
    calibration then measures their talents too (a preset that beats us holds the talents the model under-values: Frost's mana
    talents), the optimizer starts from them (scorer/run.py --seed takes candidate files) and the race and the adopt step can pick
    them. Preset candidates of the spec that no longer qualify are removed; returns the files written."""
    if GAME != "forever":
        return []
    entry = SPECS[cls][spec]
    folder = paths.raidsim_dir(cls, GAME) / "candidates"
    rep_path = paths.raidsim_dir(cls, GAME) / f"{spec}.json"
    if not rep_path.exists():
        return []
    rep = json.load(open(rep_path, encoding="utf-8"))
    key = (lambda x: x.get("value") or 0.0) if entry.get("tank") else (lambda x: x.get("dps") or 0.0)
    rows = [x for x in rep["results"] if key(x) and not x.get("removal")]
    if not rows:
        return []
    best = max(key(x) for x in rows)
    trees = load_trees(repo, cls)
    ours = json.load(open(ROOT / "_reference/data/forever-talents" / f"{cls}.json", encoding="utf-8"))
    known = {t["name"] for tr in ours["trees"] for t in tr["talents"]}
    presets = {p["label"]: p["talents"] for p in sim_presets(repo, entry)}
    written = []
    folder.mkdir(parents=True, exist_ok=True)
    keep = set()
    for x in rows:
        if not x["label"].startswith("sim preset: ") or x["label"] not in presets or key(x) < best * (1 - margin):
            continue
        alloc = preset_allocation(trees, presets[x["label"]])
        unknown = [n for items in alloc.values() for n, _ in items if n not in known]
        if unknown:
            print(f"  {spec}: {x['label']} skipped: talents unknown to our dataset {unknown}")
            continue
        path = folder / f"cand-{spec}-preset-{preset_slug(x['label'])}.json"
        keep.add(path.name)
        doc = {"id": path.stem, "allocation": alloc, "preset": x["label"][len("sim preset: "):], "talents": presets[x["label"]],
               "note": (f"The community simulator's preset '{x['label'][len('sim preset: '):]}' ({entry['sim_spec']}/presets.ts), a raid candidate since it "
                        f"ran within {margin:.0%} of the best build of {spec} ({key(x):.4g} vs {best:.4g} in the race of {rep.get('date', '?')}).")}
        old = json.load(open(path, encoding="utf-8")) if path.exists() else None
        if not old or old.get("talents") != doc["talents"]:
            path.write_text(json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
        written.append(path)
    for stale in folder.glob(f"cand-{spec}-preset-*.json"):
        if stale.name not in keep:
            stale.unlink()
    return written


_NAMES = {}


ALIASES = {25505: "Windfury Weapon", 15851: "Dragonbreath Chili", 10646: "Goblin Sapper Charge", 21162: "Elemental Sharpening Stone", 11340: "Dense Sharpening Stone"}   # proc / consumable ids the icon tables lack


def spell_names(repo, cls):
    """spell id -> name: the simulator's icon table, our beta spellbook ranks and the simulator's talent tree."""
    if cls in _NAMES:
        return _NAMES[cls]
    names = dict(ALIASES)
    db = repo / "assets/database/db.json"
    if db.exists():
        for s in json.load(open(db, encoding="utf-8")).get("spellIcons", []):
            if s.get("id") and s.get("name"):
                names[int(s["id"])] = s["name"]
    book = ROOT / "_reference/data/forever-spells" / f"{cls}.json"
    if book.exists():
        for tab in json.load(open(book, encoding="utf-8")).get("tabs", []):
            for sp in tab.get("spells", []):
                for r in sp.get("ranks", []):
                    if r.get("id"):
                        names[int(r["id"])] = sp["name"]
    for tr in load_trees(repo, cls):
        for t in tr["talents"]:
            ids = [t["spellId"]] if t.get("spellId") else (t.get("spellIds") or [])
            for sid in ids:
                names.setdefault(int(sid), t.get("fancyName") or t.get("fieldName", ""))
    _NAMES[cls] = names
    return names


def action_shares(actions, names, key="damage"):
    """{action name: share of the build's damage (or threat, for tanks)} from the bench's per-action rows (player and pet)."""
    dmg = {}
    for a in actions or []:
        if a.get("spellId"):
            name = names.get(int(a["spellId"])) or id_names.spell(a["spellId"])
        elif a.get("itemId"):
            name = id_names.item(a["itemId"])
        else:
            name = a.get("other", "other")
            if name in ("OtherActionAttack", "OtherActionShoot"):
                name = "Auto Attack" if name == "OtherActionAttack" else "Auto Shot"
        if a.get("pet"):
            name = "Pet: " + name
        dmg[name] = dmg.get(name, 0.0) + float(a.get(key, 0.0) or 0.0)
    tot = sum(dmg.values()) or 1.0
    return {k: v / tot for k, v in sorted(dmg.items(), key=lambda kv: -kv[1]) if v > 0}


def action_casts(actions, names):
    """({spell id: casts per fight}, {action name: casts per fight}) from the bench's per-action rows (player and pet, cast-only
    actions included): what a build actually casts, for the rotation pages."""
    by_id, by_name = {}, {}
    for a in actions or []:
        c = float(a.get("casts") or 0.0)
        if c <= 0:
            continue
        if a.get("spellId"):
            by_id[str(a["spellId"])] = by_id.get(str(a["spellId"]), 0.0) + c
            name = names.get(int(a["spellId"])) or id_names.spell(a["spellId"])
        elif a.get("itemId"):
            name = id_names.item(a["itemId"])
        else:
            name = {"OtherActionAttack": "Auto Attack", "OtherActionShoot": "Auto Shot"}.get(a.get("other", ""), a.get("other", "other"))
        if a.get("pet"):
            name = "Pet: " + name
        by_name[name] = by_name.get(name, 0.0) + c
    return by_id, by_name


def tank_weights():
    p = json.load(open(ROOT / "_reference/data/scorer/profiles.json", encoding="utf-8"))
    p = p["profiles"]["raid-tank"] if "profiles" in p else p["raid-tank"]
    return p.get("threat_weight", 0.5), p.get("mit_weight", 0.5)


def tank_value(row, ref):
    """A tank build's worth relative to the reference build: the raid-tank profile's weights on threat per second and on damage
    avoided (the reference's damage taken over this build's)."""
    tw, mw = tank_weights()
    if not (row.get("threat") and row.get("dtps") and ref.get("threat") and ref.get("dtps")):
        return None
    return tw * row["threat"] / ref["threat"] + mw * ref["dtps"] / row["dtps"]


def source_shares(cls, spec, shares):
    """Map action shares onto the spec model's sources: `ability:<Name>` tags, white attacks (Auto Attack / Auto Shot ->
    tags 'white'; 'offhand' when the name says so) and pets (tag 'pet'). Returns ({source id: share}, unmatched share)."""
    path = ROOT / "_reference/data/scorer/specs" / f"{cls}.json"
    if not path.exists():
        return {}, 1.0
    model = json.load(open(path, encoding="utf-8"))["models"].get(spec)
    if not model:
        return {}, 1.0
    sources = [s for s in model["sources"] if not s.get("max_level")]
    by_ability = {}
    whites, pets = [], []
    for s in sources:
        tags = s.get("tags", [])
        for t in tags:
            if t.startswith("ability:"):
                by_ability.setdefault(t[8:].lower(), []).append(s["id"])
        if "white" in tags and "pet" not in tags:
            whites.append(s)
        if "pet" in tags:
            pets.append(s["id"])
    out = {}
    unmatched = 0.0
    for name, share in shares.items():
        key = name.lower()
        if key.startswith("pet: "):
            if pets:
                out[pets[0]] = out.get(pets[0], 0.0) + share
            else:
                unmatched += share
            continue
        if key in ("auto attack", "auto shot", "melee", "melee (off-hand)", "shoot"):
            if whites:
                oh = [s for s in whites if "offhand" in s.get("tags", [])]
                mh = [s for s in whites if "offhand" not in s.get("tags", [])]
                if key == "melee (off-hand)" and oh:
                    out[oh[0]["id"]] = out.get(oh[0]["id"], 0.0) + share
                elif mh and oh and key in ("auto attack", "melee"):
                    out[mh[0]["id"]] = out.get(mh[0]["id"], 0.0) + share * 0.65
                    out[oh[0]["id"]] = out.get(oh[0]["id"], 0.0) + share * 0.35
                else:
                    out[(mh or whites)[0]["id"]] = out.get((mh or whites)[0]["id"], 0.0) + share
            else:
                unmatched += share
            continue
        base = re.sub(r"\s+(?:[ivx]+|rank \d+)$", "", key.split(" (")[0])   # "Instant Poison VI" -> "instant poison"
        ids = by_ability.get(base) or by_ability.get(key)
        if not ids:   # generic tags: "Seal" covers Seal of Righteousness, "Judgement" every Judgement of X, "Poisons" every poison
            for tag in sorted(by_ability, key=len, reverse=True):
                stem = tag[:-1] if tag.endswith("s") else tag
                if base == stem or base.startswith(stem + " ") or base.endswith(" " + stem):
                    ids = by_ability[tag]
                    break
        if ids:
            out[ids[0]] = out.get(ids[0], 0.0) + share
        else:
            unmatched += share
    tot = sum(out.values()) or 1.0
    return {k: round(v / tot, 4) for k, v in sorted(out.items(), key=lambda kv: -kv[1])}, round(unmatched, 4)


def scorer_scores(cls, spec, profile, allocs):
    try:
        from optimize import Optimizer
        opt = Optimizer(GAME, cls, spec, profile)
        return {bid: opt.score(a, 60) for bid, a in allocs.items()}
    except Exception as e:   # the scorer model may not exist for this spec (healers, hybrids)
        print(f"  (scorer unavailable for {spec}/{profile}: {e})")
        return {}


SETTING_OVERRIDE = None   # --setting dummy|raid


def sim_seed(seed):
    """The bench's RandomSeed for our seed k (2026-09-29): the simulator reseeds iteration i with RandomSeed + i, so seeds 1, 2 and 3
    over 20,000 iterations shared all but one iteration and a "second seed" re-ran the first one's random numbers. Seed k starts at
    1 + (k - 1) * 1,000,000: seed 1 is unchanged (every earlier seed-1 number stands) and the others are disjoint below a million iterations."""
    return 1 + (int(seed) - 1) * 1_000_000


def setting(entry):
    """The setting of a spec's main runs (the table, the removal deltas the calibration fits, the races): Forever DPS specs on a
    boss-level training dummy with only the class's own buffs (2026-09-27: raw personal DPS decides the raid DPS builds); tanks, whose
    value is threat and damage taken under boss melee, and the Classic sim in the raid setting."""
    if SETTING_OVERRIDE:
        return SETTING_OVERRIDE
    return "dummy" if GAME == "forever" and not entry.get("tank") else "raid"


# every mana-only buff the simulator has: the "dummy-surplus" setting (raidsim/calibrate.py) runs the dummy with them on top, and the
# damage a build gains is what running short of mana costs it on the dummy (waiting out of mana, Evocation, Life Tap, Innervate, the
# rotation's mana conditions); out-of-mana seconds alone miss most of it (a Frost mage's Evocation, a warlock's Life Taps)
# The standard fight length (2026-09-29, user request "compare dummy and raid fairly"): 180 s, the middle of a Classic boss fight's
# 2-4 minutes. At 120 s the ranking flattered front-loaded cooldowns and specs that run out of mana late (the fight-length test:
# 60 s to 360 s moved the Lone Wolf hunter -31%, the Frost mage -3%). Every bench config takes its duration from here.
FIGHT = 180.0
# The buff ladder: from the training dummy to the raid one group at a time (cumulative), so a spec's raid gain splits into mana,
# armor, physical and spell parts. Groups hold the simulator's full raid buffs (core/test_utils.go FullRaidBuffs, FullPartyBuffs,
# FullIndividualBuffs, FullDebuffs at 40be98e); what no group names (Kings, stamina, spirit, auras, Atiesh...) arrives in the last step,
# together with the raid rotation.
LADDER = [
    ("mana", {"mana_spring_totem": "TristateEffectImproved", "mana_tide_totems": 1, "greater_blessing_of_wisdom": True}, {"judgement_of_wisdom": True}),
    ("armor", {}, {"sunder_armor": True, "expose_armor": True, "faerie_fire": True, "curse_of_recklessness": True}),
    ("physical", {"battle_shout": 1,   # 1 = rank 6, as the full raid (b90e2b9 made it a rank number: 1 trainer rank, 2 book rank, 3 book + T2)
                   "greater_blessing_of_might": True, "windfury_totem": True, "strength_of_earth_totem": True,
                  "leader_of_the_pack": True, "trueshot_aura": True}, {"hunters_mark": True, "gift_of_arthas": True}),
    ("spell", {"arcane_brilliance": True, "moonkin_aura": True}, {"curse_of_elements": True, "judgement_of_the_crusader": True}),
]
CURVE = [60, 120, 180, 240, 360]   # fight lengths of the DPS-over-time curve (training dummy without execute phases)
MANA_SURPLUS = {"buffs": {"mana_spring_totem": "TristateEffectImproved", "mana_tide_totems": 4, "greater_blessing_of_wisdom": True, "innervates": 4},
                "debuffs": {"judgement_of_wisdom": True}}


def setting_cfg(entry, name, level=0, no_execute=False):
    """Bench config fields of a setting: buffs, consumables and the target."""
    if name in ("dummy", "dummy-surplus") or name.startswith("ladder-"):   # your own buffs include your own consumables (flask, elixirs, food, potions, weapon oils and stones)
        sb, sd = dict(entry.get("self_buffs", {})), dict(entry.get("self_debuffs", {}))
        if name == "dummy-surplus":
            sb.update(MANA_SURPLUS["buffs"])
            sd.update(MANA_SURPLUS["debuffs"])
        if name.startswith("ladder-"):   # the dummy plus every ladder group up to and including this one
            upto = [g for g, _, _ in LADDER].index(name[len("ladder-"):])
            for _, gb, gd in LADDER[:upto + 1]:
                sb.update(gb)
                sd.update(gd)
            for k in entry.get("buffs_off", []) + entry.get("debuffs_off", []):   # the spec's own buff stays its own (as in the raid setting)
                sb.pop(k, None)
                sd.pop(k, None)
        return {"consumables": entry.get("consumables", {}), "buffs": "self", "buffs_on": sb, "debuffs_on": sd,
                "buffs_off": [], "debuffs_off": [], "targetLevel": level, "noExecute": no_execute}
    if name == "none":
        return {"consumables": {}, "buffs": "none", "buffs_off": [], "debuffs_off": [], "targetLevel": level, "noExecute": no_execute}
    return {"consumables": entry.get("consumables", {}), "buffs": "full", "buffs_off": entry.get("buffs_off", []), "debuffs_off": entry.get("debuffs_off", []),
            "targetLevel": level, "noExecute": no_execute}


def setting_text(entry, name):
    if name == "dummy":
        own = [*entry.get("self_buffs", {}), *entry.get("self_debuffs", {})]
        return ("a boss-level training dummy (level 63, execute phases as a dying boss) with only your own buffs: what the class code "
                "adds itself (its talent auras, Arcane Brilliance, the priest buffs, its own shout, curses, totems and weapon imbues in the rotation)"
                + (f" plus {', '.join(own)}" if own else "") + " and the spec's standard consumables; no raid or party buffs and no debuffs from others")
    return ("full raid/party/individual buffs and debuffs (the sim's test defaults)"
            + (f" minus the spec's own {', '.join(entry.get('buffs_off', []) + entry.get('debuffs_off', []))} (its talent is under test)"
               if entry.get("buffs_off") or entry.get("debuffs_off") else "") + ", the sim spec's default consumables")


def run_spec(cls, spec, a, repo):
    entry = SPECS[cls][spec]
    trees = load_trees(repo, cls)
    data = json.load(open(ROOT / cls / GAMES[GAME]["builds"], encoding="utf-8"))
    by_id = {b["id"]: b for b in data["builds"]}
    ids = a.builds or entry["builds"]
    builds = []
    allocs = {}
    for bid in ids:
        if bid.endswith(".json"):
            b = json.load(open(bid, encoding="utf-8"))
            b.setdefault("id", pathlib.Path(bid).stem)
            if b.get("preset") and not a.no_presets:   # a saved preset candidate: the simulator's preset runs below under its own label
                continue
        else:
            b = by_id[bid]
        al = alloc_of(b)
        allocs[b["id"]] = al
        # a preset candidate (write_preset_candidates) is the simulator's build, not ours, but it is measured like ours (removal runs)
        builds.append({"label": b["id"], "talents": talents_string(trees, al), "split": split(b), "ours": not b.get("preset"), "measured": True,
                       **({"preset": b["preset"]} if b.get("preset") else {})})
    if not a.no_presets:
        for p in sim_presets(repo, entry):
            builds.append(dict(p, split="", ours=False))
    delta_builds = [b for b in builds if b.get("measured") and (b["label"] in (a.deltas or []) or (a.deltas == ["all"]))] if a.deltas else []
    apl_dependent = apl_talents(repo, entry, trees) if delta_builds else set()
    removals = []   # (build label, talent, variant label)
    for b in delta_builds:
        al = allocs[b["label"]]
        for name in sorted(al):
            trial = {k: v for k, v in al.items() if k != name}
            removals.append((b["label"], name, f"{b['label']} -{name}"))
            builds.append({"label": f"{b['label']} -{name}", "talents": talents_string(trees, trial), "split": "", "ours": False, "removal": True})
    cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": sim_path(entry["gear"]), "apl": str(apl_path(entry, repo)), "spec": entry.get("spec", {}),
           **setting_cfg(entry, setting(entry)),
           "profession1": entry.get("profession1", "Engineering"),
           "profession2": entry.get("profession2", ""), "distanceFromTarget": entry.get("distance", 5), "inFrontOfTarget": entry.get("in_front", False),
           "reactionTimeMs": 200, "iterations": a.iterations, "duration": a.duration, "seed": sim_seed(a.seed), "isTank": entry.get("tank", False),
           "builds": [{"label": b["label"], "talents": b["talents"]} for b in builds]}
    bench_dir = repo / "bench"
    bench_dir.mkdir(exist_ok=True)
    cfg_path = bench_dir / f"{cls}-{spec}.json"
    cfg_path.write_text(json.dumps(cfg, indent=1), encoding="utf-8")
    bench = GAMES[GAME]["bench"]
    exe = repo / (f"{bench}.exe" if (repo / f"{bench}.exe").exists() else bench)
    print(f"== {cls} {spec}: {len(builds)} builds x {a.iterations} iterations, {entry['sim_spec']} {pathlib.Path(entry['gear']).name} + {pathlib.Path(entry['apl']).name}")
    r = subprocess.run([str(exe), "--config", str(cfg_path), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(repo))
    if r.returncode:
        print(r.stderr[-2000:])
        raise SystemExit(f"bench failed for {cls} {spec}")
    rows = {}
    for line in r.stdout.splitlines():
        if line.startswith("{"):
            d = json.loads(line)
            rows[d["label"]] = d
    scores = scorer_scores(cls, spec, entry.get("profile", "raid-dps"), allocs)
    results = []
    names = spell_names(repo, cls)
    tank = bool(entry.get("tank"))
    for b in builds:
        if b.get("removal"):
            continue
        d = rows.get(b["label"], {})
        sh = action_shares(d.get("actions"), names, "threat" if tank else "damage") if d.get("actions") else {}
        src, unmatched = source_shares(cls, spec, sh) if sh else ({}, 0.0)
        spell_casts, casts = action_casts(d.get("actions"), names)
        results.append({**b, "spell_casts": spell_casts, "casts": casts, "dps": d.get("dps"), "dps_stdev": d.get("dps_stdev"), "threat": d.get("threat"), "dtps": d.get("dtps"), "tmi": d.get("tmi"), "hps": d.get("hps"),
                        "oom_seconds": d.get("oom_seconds"), "error": d.get("error"), "scorer": scores.get(b["label"]), "shares": sh, "source_shares": src, "unmatched_share": unmatched})
    if tank:   # rank tanks by threat and damage taken, relative to the first of our builds (the hand draft)
        ref = next((x for x in results if x["ours"] and x.get("dtps")), None)
        for x in results:
            x["value"] = tank_value(x, ref) if ref else None
    deltas = {}
    if removals:
        ev = scorer_removals(cls, spec, entry.get("profile", "raid-dps"), {b["label"]: allocs[b["label"]] for b in delta_builds})
        tw, mw = tank_weights()
        for blabel, name, vlabel in removals:
            base = rows.get(blabel, {}).get("dps")
            without = rows.get(vlabel, {}).get("dps")
            if base and without:
                row = {"talent": name, "ranks": allocs[blabel][name], "sim_delta": (base - without) / without,
                       "dps_with": base, "dps_without": without, "ev_delta": ev.get(blabel, {}).get(name),
                       "apl_dependent": (name if GAME == "forever" else field_name(name)) in apl_dependent}
                if tank:   # threat and mitigation, weighted as the raid-tank profile scores them
                    tb, tw_ = rows[blabel].get("threat"), rows[vlabel].get("threat")
                    db, dw = rows[blabel].get("dtps"), rows[vlabel].get("dtps")
                    if tb and tw_ and db and dw:
                        row.update({"threat_with": tb, "threat_without": tw_, "dtps_with": db, "dtps_without": dw,
                                    "sim_delta": tw * (tb - tw_) / tw_ + mw * (dw - db) / db})
                deltas.setdefault(blabel, []).append(row)
        for blabel, rws in deltas.items():
            print(f"  talent values for {blabel} (DPS lost when removed, relative to the build without it; EV = scorer on the same scale):")
            for r in sorted(rws, key=lambda r: -r["sim_delta"]):
                print(f"    {r['talent']:<32} {r['ranks']}  sim {r['sim_delta'] * 100:+6.1f}%   EV {(r['ev_delta'] * 100 if r['ev_delta'] is not None else float('nan')):+6.1f}%"
                      + ("   (rotation-dependent: its removal breaks the rotation)" if r.get("apl_dependent") else ""))
    for x in sorted(results, key=lambda x: -((x.get("value") if tank else x["dps"]) or 0)):
        print(f"  {x['label']:<42} {x['split']:>8}  DPS {x['dps'] or 0:8.1f} ± {x['dps_stdev'] or 0:5.1f}  threat {x['threat'] or 0:8.0f}  oom {x['oom_seconds'] or 0:5.1f}s" + (f"  dtps {x['dtps'] or 0:7.1f}  tank-value {x['value'] or 0:6.3f}" if tank else "") + (f"  scorer {x['scorer'] * 100:+.1f}%" if x.get('scorer') is not None else "") + (f"  ERROR {x['error']}" if x.get("error") else ""))
    first = next((x for x in results if x.get("shares")), None)
    if first:
        print(f"  damage shares of {first['label']}: " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in list(first["shares"].items())[:8])
              + f" | model sources: " + ", ".join(f"{k} {v * 100:.0f}%" for k, v in first["source_shares"].items()) + f" (unmatched {first['unmatched_share'] * 100:.0f}%)")
    out = {"class": cls, "spec": spec, "game": GAME, "sim": {"repo": str(repo), "commit": git_commit(repo), **sim_switches(repo), "spec_folder": entry["sim_spec"], "gear": entry["gear"], "apl": apl_label(entry, repo), "apl_sim": entry["apl"],
                                              "race": cfg["race"], "setting": setting(entry), "buffs": setting_text(entry, setting(entry)), "consumables": cfg["consumables"],
                                              "encounter": (f"a boss-level training dummy (level 63, creature type Elemental), {a.duration}s, execute phases 20/25/35/45/90%" if setting(entry) == "dummy" else f"single level-63 target (creature type Elemental), {a.duration}s, execute phases 20/25/35/45/90%"), "iterations": a.iterations, "seed": a.seed, "duration": a.duration},
           "date": datetime.date.today().isoformat(), "results": results, "deltas": deltas}
    if a.write:
        write_report(out)
    return out


def apl_talents(repo, entry, trees, where=None):
    """Talents whose spell ids the rotation (APL) *conditions* on: removing one changes what the rotation does (Improved Scorch's
    'keep 5 stacks' loop spams Scorch forever without the debuff; the Classic mage APL casts Fireball only while Combustion is
    known), so the removal run measures a broken rotation, not the talent. A talent the APL merely casts is not flagged: an
    unknown spell is skipped and the rotation goes on, which is the talent's real value."""
    ids = set()

    def walk(x, in_condition):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "spellId" and isinstance(v, int) and in_condition:
                    ids.add(v)
                # a (strict) sequence stops at a spell the build does not know, so every spell in it depends on the others
                # (the Smite rotation's "Inner Focus; Devouring Plague": without Inner Focus, Devouring Plague is never cast)
                walk(v, in_condition or k in ("condition", "sequence", "strictSequence"))
        elif isinstance(x, list):
            for v in x:
                walk(v, in_condition)
    apl = apl_path(entry, repo, where)
    if apl.exists():
        walk(json.load(open(apl, encoding="utf-8")), False)
    # a proc aura the talent creates has its own spell id (Fingers of Frost's FingersOfFrostTriggered 400669, Hot Streak's 400625,
    # Maelstrom Weapon's 408505): the simulator's spell data names it after the talent, so a condition on it flags the talent too
    # (without the talent the aura is unknown and the rotation misreads the condition: removing Fingers of Frost measured +189%)
    named = {}
    for i in ids:
        n = spelldata_names(repo, entry).get(i) or APL_AURA_NAMES.get(i)
        if n:
            named[i] = n
    out = set()
    for tr in trees:
        for t in tr["talents"]:
            tids = [t["spellId"]] if t.get("spellId") else (t.get("spellIds") or [])
            field = t.get("fieldName") or ""
            pascal = field[:1].upper() + field[1:]
            if any(int(i) in ids for i in tids) or (pascal and any(n in (pascal + s for s in AURA_SUFFIXES) for n in named.values())):
                out.add(t.get("fancyName") or t.get("fieldName"))
    return out


AURA_SUFFIXES = ("Triggered", "Aura", "Proc", "Buff", "Debuff", "Effect")
# aura ids the rotations use that the simulator's spell data does not name (a legacy id the class code registers the aura under)
APL_AURA_NAMES = {44404: "MissileBarrageTriggered"}
_SPELLDATA = {}


def spelldata_names(repo, entry):
    """Spell id -> the simulator's spell-data name (FingersOfFrostTriggered), from sim/<class>/spell_data_auto_gen.go when the clone
    has one (ElliotWood/Forever does; the Classic clone does not, and its talents are matched by their own ids only)."""
    key = (str(repo), entry.get("sim_spec", ""))
    if key not in _SPELLDATA:
        out = {}
        p = repo / "sim" / entry.get("sim_spec", "").split("/")[0] / "spell_data_auto_gen.go"
        if p.exists():
            for m in re.finditer(r"^\s*(\w+):\s*spelldata\.\w+\(([^)]*)\)", p.read_text(encoding="utf-8"), re.M):
                for i in re.findall(r"\d+", m.group(2)):
                    if int(i) > 1000:
                        out.setdefault(int(i), m.group(1))
        _SPELLDATA[key] = out
    return _SPELLDATA[key]


PHASE = re.compile(r"(?:^|[_.-])p(?:hase_)?(\d)(?:[_.-]|$)")


def gear_family(name):
    n = pathlib.Path(name).name.replace(".gear.json", "")
    n = PHASE.sub("_", n)
    for tok in ("bis", "pre-bis", "prebis", "preraid", "launch", "default", "mc"):
        n = n.replace(tok, "")
    return n.strip("_.-")


def gear_complete(path):
    """A preset with a main-hand weapon and its jewelry, trinkets, neck and back filled (some presets list only the armor slots:
    shadow priest and Protection warrior p1.bis, feral cat p0.bis in ElliotWood/Forever 40be98e)."""
    try:
        items = json.load(open(path, encoding="utf-8")).get("items", [])
    except (OSError, ValueError):
        return False
    need = (1, 3, 10, 11, 12, 13, 14)   # neck, back, two rings, two trinkets, main hand
    return all(i < len(items) and items[i] and items[i].get("id") for i in need)


def best_gear(repo, entry):
    """The highest-phase gear preset of the spec's family (combat_sinister_strike_p2_bis over _p1_bis; phase_6 over phase_1;
    mc over prebis): the 'maximum' environment's gear. Falls back to the spec's own preset."""
    own = pathlib.Path(entry["gear"])
    folder = repo / own.parent
    fam = gear_family(own.name)

    def phase(name):
        m = PHASE.search(name.replace(".gear.json", ""))
        if m:
            return int(m.group(1))
        return 1 if "mc" in name else 0
    cands = [f for f in folder.glob("*.gear.json") if gear_family(f.name) == fam and gear_complete(f)] if folder.exists() else []
    if not cands:
        return entry["gear"]
    best = max(cands, key=lambda f: (phase(f.name), f.name == own.name))
    return str(best.relative_to(repo)).replace(os.sep, "/")


ENVIRONMENTS = {
    "dummy": {"label": "training dummy", "how": "a boss-level (63) training dummy with only your own buffs (the class's self-buffs and the spec's standard consumables, no raid or party buffs, no debuffs from others), execute phases as a dying boss, phase-1 gear, 180 s: the setting that ranks the raid DPS builds (Forever)"},
    "dummy60": {"label": "level-60 dummy", "how": "an in-game style dummy: level 60, never dies (no execute phase), your own buffs and consumables only (Forever; the Classic sim: no buffs and no consumables), phase-1 gear, 180 s"},
    "raid": {"label": "raid", "how": "phase-1 gear, full raid buffs and debuffs minus the buff this spec brings itself, the standard raid consumables, 180 s"},
    "max": {"label": "maximum", "how": "the best gear preset of the spec, every raid buff and debuff on (own buff supplied by someone else), consumables (and the Classic sim's world buffs), 180 s"},
    "max60": {"label": "maximum, 60 s", "how": "as maximum with a 60 s fight: cooldowns weigh more"},
    **{f"ladder-{g}": {"label": f"+ {g}", "how": f"the training dummy plus the raid's {g} buffs and debuffs"
                       + (" (and every group before it)" if i else "") + ": " + ", ".join([*gb, *gd])} for i, (g, gb, gd) in enumerate(LADDER)},
    **{f"curve{n}": {"label": f"{n} s", "how": f"the training dummy without execute phases, a {n} s fight (the DPS-over-time curve)"} for n in CURVE},
}


def ladder_steps(rows):
    """{label: {"dummy", "raid", "steps": {group: gain as a share of the dummy DPS}}} from an environments run's rows."""
    out = {}
    for x in rows:
        d = x["dps"]
        seq = ["dummy"] + [f"ladder-{g}" for g, _, _ in LADDER] + ["raid"]
        if not all(d.get(k) for k in seq):
            continue
        steps = {(k[len("ladder-"):] if k.startswith("ladder-") else "rest"): (d[k] - d[prev]) / d["dummy"] for prev, k in zip(seq, seq[1:])}
        out[x["label"]] = {"dummy": d["dummy"], "raid": d["raid"], "steps": steps}
    return out


def curve_windows(rows):
    """{label: {"1 min": dps, ...}}: average DPS by fight length (training dummy, no execute phase). Differences between lengths
    (the DPS inside each stretch) were tried and dropped: subtracting two noisy totals swung the stretches by 7% at 3000 iterations."""
    out = {}
    for x in rows:
        d = x["dps"]
        if all(d.get(f"curve{n}") for n in CURVE):
            out[x["label"]] = {(f"{n // 60} min" if n % 60 == 0 else f"{n} s"): d[f"curve{n}"] for n in CURVE}
    return out


def run_environments(cls, spec, a, repo):
    """Every build (ours and the presets) in every environment; the raid column comes from the spec's main report when it exists."""
    entry = SPECS[cls][spec]
    trees = load_trees(repo, cls)
    data = json.load(open(ROOT / cls / GAMES[GAME]["builds"], encoding="utf-8"))
    by_id = {b["id"]: b for b in data["builds"]}
    ids = a.builds or (entry["builds"] + [f"opt-{spec}-parse"] * (f"opt-{spec}-parse" in by_id))   # the parse build as rebuild.py passes it
    builds = []
    for bid in ids:
        if bid.endswith(".json"):
            b = json.load(open(bid, encoding="utf-8"))
            b.setdefault("id", pathlib.Path(bid).stem)
        elif bid in by_id:
            b = by_id[bid]
        else:
            print(f"  (no build {bid})")
            continue
        builds.append({"label": b["id"], "talents": talents_string(trees, alloc_of(b)), "split": split(b), "ours": True})
    if not a.no_presets:
        for pr in sim_presets(repo, entry):
            builds.append(dict(pr, split="", ours=False))
    gear_max = sim_path(best_gear(repo, entry))
    base_cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "apl": str(apl_path(entry, repo)), "spec": entry.get("spec", {}), "profession1": entry.get("profession1", "Engineering"),
                "profession2": entry.get("profession2", ""), "distanceFromTarget": entry.get("distance", 5), "inFrontOfTarget": entry.get("in_front", False), "reactionTimeMs": 200,
                "iterations": a.iterations, "seed": sim_seed(a.seed), "isTank": entry.get("tank", False), "builds": [{"label": b["label"], "talents": b["talents"]} for b in builds]}
    envs = {}
    dummy_apl, raid_apl = str(apl_path(entry, repo, "dummy")), str(apl_path(entry, repo, "raid"))   # each setting runs its own rotation
    if GAME == "forever":
        envs["dummy"] = dict(base_cfg, gear=sim_path(entry["gear"]), duration=FIGHT, apl=dummy_apl, **setting_cfg(entry, "dummy"))
        envs["dummy60"] = dict(base_cfg, gear=sim_path(entry["gear"]), duration=FIGHT, apl=dummy_apl, **setting_cfg(entry, "dummy", level=60, no_execute=True))
    else:
        envs["dummy60"] = dict(base_cfg, gear=entry["gear"], duration=FIGHT, **setting_cfg(entry, "none", level=60, no_execute=True))
    if GAME == "forever" and not entry.get("tank"):
        for g, _, _ in LADDER:
            envs[f"ladder-{g}"] = dict(base_cfg, gear=sim_path(entry["gear"]), duration=FIGHT, apl=dummy_apl, **setting_cfg(entry, f"ladder-{g}"))
    envs["raid"] = dict(base_cfg, gear=sim_path(entry["gear"]), duration=FIGHT, apl=raid_apl, **setting_cfg(entry, "raid"))
    if GAME == "forever" and not entry.get("tank"):
        for n in CURVE:
            envs[f"curve{n}"] = dict(base_cfg, gear=sim_path(entry["gear"]), duration=float(n), apl=dummy_apl, **setting_cfg(entry, "dummy", no_execute=True))
    envs.update({
        "max": dict(base_cfg, gear=gear_max, consumables=entry.get("consumables", {}), buffs="full", buffs_off=[], debuffs_off=[], duration=FIGHT, apl=raid_apl),
        "max60": dict(base_cfg, gear=gear_max, consumables=entry.get("consumables", {}), buffs="full", buffs_off=[], debuffs_off=[], duration=60.0, apl=raid_apl),
    })
    bench = GAMES[GAME]["bench"]
    exe = repo / (f"{bench}.exe" if (repo / f"{bench}.exe").exists() else bench)
    bench_dir = repo / "bench"
    bench_dir.mkdir(exist_ok=True)
    dps = {b["label"]: {} for b in builds}
    raid_casts = {b["label"]: ({}, {}) for b in builds}   # (spell casts, action casts) in the raid: the raid pages' rotation (2026-10-02)
    raid_shares = {b["label"]: {} for b in builds}   # damage shares in the raid (2026-10-22: the signature-spell check, raidsim/raid_signature.py)
    names = spell_names(repo, cls)
    for env, cfg in envs.items():
        cfg_path = bench_dir / f"{cls}-{spec}-{env}.json"
        cfg_path.write_text(json.dumps(cfg, indent=1), encoding="utf-8")
        r = subprocess.run([str(exe), "--config", str(cfg_path), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(repo))
        if r.returncode:
            print(r.stderr[-1500:])
            raise SystemExit(f"bench failed for {cls} {spec} ({env})")
        for line in r.stdout.splitlines():
            if line.startswith("{"):
                d = json.loads(line)
                if d["label"] in dps:
                    dps[d["label"]][env] = d.get("dps")
                    if env == "raid":
                        raid_casts[d["label"]] = action_casts(d.get("actions"), names)
                        raid_shares[d["label"]] = {k: round(v, 4) for k, v in action_shares(d.get("actions"), names, "damage").items()} if d.get("actions") else {}
    rows = [{"label": b["label"], "split": b["split"], "ours": b["ours"], "dps": dps[b["label"]],
             "raid_spell_casts": raid_casts[b["label"]][0], "raid_casts": raid_casts[b["label"]][1], "raid_shares": raid_shares[b["label"]]} for b in builds]
    out = {"class": cls, "spec": spec, "game": GAME, "date": datetime.date.today().isoformat(), "sim": {"repo": str(repo), "commit": git_commit(repo), **sim_switches(repo), "gear_raid": entry["gear"], "gear_max": gear_max,
                                                                                                          "iterations": a.iterations, "seed": a.seed}, "environments": ENVIRONMENTS, "results": rows}
    print(f"== {cls} {spec} environments (gear raid {pathlib.Path(entry['gear']).name}, max {pathlib.Path(gear_max).name}):")
    key = "dummy" if GAME == "forever" else "raid"
    base = [k for k in envs if not k.startswith(("ladder-", "curve"))]
    for x in sorted(rows, key=lambda x: -(x["dps"].get(key) or 0)):
        print(f"  {x['label']:<42} {x['split']:>8}  " + "  ".join(f"{k} {x['dps'].get(k) or 0:7.1f}" for k in envs))
    if a.write:
        d = paths.raidsim_dir(cls, GAME)
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{spec}-environments.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
        o = [f"# DPS by environment — {cls} {spec}" + (" (Classic Era)" if GAME != "forever" else ""), "",
             f"> Generated by `_reference/data/raidsim/run.py --env environments` on {out['date']} with {sim_info.label(dict(out['sim'], game=GAME))}, {a.iterations} iterations per build. "
             "Personal DPS of the same builds in every setting: the boss-level training dummy with your own buffs (it ranks the raid DPS builds), an in-game "
             "level-60 dummy, the fully buffed raid, and the theoretical maximum (best gear preset, everything on). Simulations of the community's model, "
             "not measurements. Do not hand-edit.", "",
             "| Build | Split | " + " | ".join(ENVIRONMENTS[k]["label"].capitalize() for k in base) + " |", "|---|---|" + "---|" * len(base)]
        for x in sorted(rows, key=lambda x: -(x["dps"].get(key) or 0)):
            name = f"`{x['label']}`" if x["ours"] else x["label"]
            cell = lambda k: (f"{x['dps'][k]:.0f}" if x["dps"].get(k) else "-")   # noqa: E731
            o.append(f"| {name} | {x['split'] or '-'} | " + " | ".join(cell(k) for k in base) + " |")
        o += [""] + [f"- **{ENVIRONMENTS[k]['label']}**: {ENVIRONMENTS[k]['how']}" for k in base] + [""]
        lad = ladder_steps(rows)
        if lad:
            o += ["## Where the raid gain comes from", "",
                  "Each build from the training dummy to the raid, one group of raid buffs at a time (each step adds to the one before; "
                  "\"rest\" is every other raid buff plus the raid rotation). Percent of the dummy DPS.", "",
                  "| Build | Dummy | " + " | ".join(f"+ {g}" for g, _, _ in LADDER) + " | + rest | Raid |", "|---|---|" + "---|" * (len(LADDER) + 2)]
            for x in sorted(rows, key=lambda x: -(x["dps"].get(key) or 0)):
                st = lad.get(x["label"])
                if st:
                    name = f"`{x['label']}`" if x["ours"] else x["label"]
                    o.append(f"| {name} | {st['dummy']:.0f} | " + " | ".join(f"{v:+.0%}" for v in st["steps"].values()) + f" | {st['raid']:.0f} |")
            o += ["", "Groups: " + "; ".join(f"**{g}** " + ", ".join([*gb, *gd]) for g, gb, gd in LADDER) + ". A spec's own raid buff stays its own "
                  "(the raid setting's rule). The order matters a little: a buff is worth more on top of the ones before it.", ""]
        cur = curve_windows(rows)
        if cur:
            o += ["## DPS by fight length", "",
                  "Average DPS on the training dummy (no execute phase) if the fight lasts this long. A row that falls is a spec that "
                  "front-loads its cooldowns or runs out of mana; about ±1% per cell at 3000 iterations.", "",
                  "| Build | " + " | ".join(w for w in next(iter(cur.values()))) + " |", "|---|" + "---|" * len(next(iter(cur.values())))]
            for x in sorted(rows, key=lambda x: -(x["dps"].get(key) or 0)):
                c = cur.get(x["label"])
                if c:
                    name = f"`{x['label']}`" if x["ours"] else x["label"]
                    o.append(f"| {name} | " + " | ".join(f"{v:.0f}" for v in c.values()) + " |")
            o.append("")
        o += [f"Gear presets: raid `{pathlib.Path(entry['gear']).name}`, maximum `{pathlib.Path(gear_max).name}`. "
              "`opt-<spec>-parse` is the scorer's parse build (personal DPS only, the raid brings every buff); the raid builds bring their own buff.", ""]
        (d / f"{spec}-environments.md").write_text("\n".join(o) + "\n", encoding="utf-8")
        print(f"wrote {(d / f'{spec}-environments.md').relative_to(ROOT)}")
    return out


def scorer_removals(cls, spec, profile, allocs):
    """Scorer's value of each single-talent removal on the sim's scale: (score_with - score_without) / (1 + score_without)."""
    try:
        from optimize import Optimizer
        opt = Optimizer(GAME, cls, spec, profile)
    except Exception as e:
        print(f"  (scorer unavailable for {spec}/{profile}: {e})")
        return {}
    out = {}
    for bid, al in allocs.items():
        with_s = opt.score(al, 60)
        for name in al:
            wo = opt.score({k: v for k, v in al.items() if k != name}, 60)
            out.setdefault(bid, {})[name] = (with_s - wo) / (1.0 + wo)
    return out


def sim_switches(repo=None):
    """The patch switches a run was made with (2026-10-18, audit 2 row 96: race-neutral numbers depended on an environment variable no
    report recorded): racials on or off (WOW_FOREVER_NO_RACIALS=1), the pet swing rule (WOW_FOREVER_PET_NORMALIZE=1). With the checkout
    also the simulator and its data's client build (2026-10-22, sim_info.identity), so the pages can name what a record ran on."""
    return {"racials": "off" if os.environ.get("WOW_FOREVER_NO_RACIALS") == "1" else "on",
            "pet_normalize": os.environ.get("WOW_FOREVER_PET_NORMALIZE") == "1", **(sim_info.identity(repo) if repo else {})}


def git_commit(repo):
    try:
        return subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    except Exception:
        return "?"


def write_report(out):
    cls, spec = out["class"], out["spec"]
    if not out["results"]:   # an entry with no builds and no presets (the Shockadin survey target): nothing to report
        print(f"  {cls} {spec}: no builds to report")
        return
    d = paths.raidsim_dir(cls, GAME)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{spec}.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    sim = out["sim"]
    tank = any(x.get("value") is not None for x in out["results"])
    rows = sorted(out["results"], key=lambda x: -((x.get("value") if tank else x["dps"]) or 0))
    if not rows:   # an entry with no builds and no presets (the Shockadin survey target): nothing to report
        print(f"  {cls} {spec}: no builds to report")
        return
    best = rows[0]["dps"] or 1.0
    o = [f"# Raid sim — {cls} {spec}" + (" (Classic Era)" if out.get("game") == "classic-era" else ""), "",
         f"> Generated by `_reference/data/raidsim/run.py` on {out['date']} with {sim_info.label(dict(sim, game=out.get('game', 'forever')))}: "
         f"{sim['iterations']} iterations per build, seed {sim['seed']}, {sim['encounter']}, gear preset `{pathlib.Path(sim['gear']).name}`, rotation `{pathlib.Path(sim['apl']).name}`, "
         f"race {sim['race']}, {sim['buffs']}, the sim spec's default options. Every build uses the same gear and rotation, so the table ranks talents only; "
         "a build whose playstyle the rotation does not express (a Fire build under a Frost rotation) is not fairly measured. The simulator models the beta from the "
         "community's reading of it: simulations, not measurements. Do not hand-edit.", "",
         ("| Build | Split | Tank value | Threat/s | Damage taken/s | DPS | OOM s | Scorer |" if tank else "| Build | Split | DPS | ± | vs best | Threat | OOM s | Scorer |"), "|---|---|---|---|---|---|---|---|"]
    for x in rows:
        sc = f"{(x['scorer'] * 100):+.1f}%" if x.get("scorer") is not None else "-"
        name = '`' + x['label'] + '`' if x['ours'] else x['label']
        if tank:
            o.append(f"| {name} | {x['split'] or '-'} | {(x.get('value') or 0):.3f} | {x['threat'] or 0:.0f} | {x.get('dtps') or 0:.0f} | {x['dps'] or 0:.0f} | {x['oom_seconds'] or 0:.0f} | {sc} |")
        else:
            o.append(f"| {name} | {x['split'] or '-'} | {x['dps'] or 0:.0f} | {x['dps_stdev'] or 0:.0f} | {((x['dps'] or 0) - best) / best * 100:+.1f}% | {x['threat'] or 0:.0f} | {x['oom_seconds'] or 0:.0f} | {sc} |")
    if tank:
        tw, mw = tank_weights()
        o += ["", f"Tank value = {tw:.1f} x threat per second / the hand draft's + {mw:.1f} x the hand draft's damage taken per second / this build's (the raid-tank profile's weights); "
              "the shares below are threat shares."]
    first = next((x for x in rows if x.get("shares")), None)
    if first:
        o += ["", f"## Damage shares (`{first['label']}`, simulator actions)", "",
              "| Action | Share |", "|---|---|"] + [f"| {k} | {v * 100:.1f}% |" for k, v in list(first["shares"].items())[:14]] + ["",
              "Mapped onto the spec model's sources: " + ", ".join(f"`{k}` {v * 100:.0f}%" for k, v in first["source_shares"].items())
              + f"; {first['unmatched_share'] * 100:.0f}% of the damage matched no source (raidsim/calibrate.py writes the mapped split into the model's base shares).", ""]
    for blabel, rws in (out.get("deltas") or {}).items():
        if tank:
            o += ["", f"## Talent values in `{blabel}` (tank value lost when the talent is removed: threat and mitigation, weighted as the raid-tank profile scores them)", "",
                  "| Talent | Ranks | Sim | Scorer | Threat with | without | Damage taken with | without |", "|---|---|---|---|---|---|---|---|"]
            for r in sorted(rws, key=lambda r: -r["sim_delta"]):
                ev = f"{(r['ev_delta'] * 100):+.1f}%" if r["ev_delta"] is not None else "-"
                o.append(f"| {r['talent']} | {r['ranks']} | {r['sim_delta'] * 100:+.1f}% | {ev} | {r.get('threat_with', 0):.0f} | {r.get('threat_without', 0):.0f} | {r.get('dtps_with', 0):.0f} | {r.get('dtps_without', 0):.0f} |")
            continue
        o += ["", f"## Talent values in `{blabel}` (DPS lost when the talent is removed, relative to the build without it)", "",
              "| Talent | Ranks | Sim | Scorer | DPS with | without |", "|---|---|---|---|---|---|"]
        for r in sorted(rws, key=lambda r: -r["sim_delta"]):
            o.append(f"| {r['talent']} | {r['ranks']} | {r['sim_delta'] * 100:+.1f}% | {(r['ev_delta'] * 100):+.1f}% | {r['dps_with']:.0f} | {r['dps_without']:.0f} |" if r["ev_delta"] is not None else
                     f"| {r['talent']} | {r['ranks']} | {r['sim_delta'] * 100:+.1f}% | - | {r['dps_with']:.0f} | {r['dps_without']:.0f} |")
    o += ["", "Scorer = the expected-value stats model's score of the same allocation for its raid profile (relative to a talentless character; only comparable within a spec model). "
          "Talent strings sent to the sim:", ""]
    for x in rows:
        o.append(f"- {x['label']}: `{x['talents']}`")
    o.append("")
    (d / f"{spec}.md").write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {(d / f'{spec}.md').relative_to(ROOT)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--spec")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--builds", nargs="*")
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--duration", type=float, default=FIGHT)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--repo")
    ap.add_argument("--no-presets", action="store_true")
    ap.add_argument("--deltas", nargs="*", help="build ids to measure talent by talent (removal runs); 'all' = every one of our builds")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--game", default="forever", choices=list(GAMES), help="classic-era: our Classic builds through the upstream wowsims/classic clone")
    ap.add_argument("--env", default="raid", choices=["raid", "environments"], help="environments: the builds on the training dummies, in the raid and at the maximum")
    ap.add_argument("--setting", choices=["dummy", "raid"], help="the main runs' setting (default: the training dummy for Forever DPS specs, the raid for tanks and Classic)")
    ap.add_argument("--preset-candidates", action="store_true", help="save the simulator's presets that compete with our builds as raid candidates (write_preset_candidates) and stop")
    a = ap.parse_args()
    set_game(a.game)
    global SETTING_OVERRIDE
    SETTING_OVERRIDE = a.setting
    repo = repo_path(a)
    if a.preset_candidates:
        todo = [(c, s) for c, sp in SPECS.items() if not c.startswith("_") for s in sp if isinstance(sp[s], dict) and "apl" in sp[s]] if a.all else [(a.cls, a.spec)]
        for c, s in todo:
            w = write_preset_candidates(c, s, repo)
            print(f"{c} {s}: " + (", ".join(p.name for p in w) or "no preset within " + f"{PRESET_MARGIN:.0%} of the best build"))
        return
    runner = run_environments if a.env == "environments" else run_spec
    if a.all:
        for cls, specs in SPECS.items():
            if cls.startswith("_"):
                continue
            for spec in specs:
                runner(cls, spec, a, repo)
    else:
        if not a.cls or not a.spec:
            raise SystemExit("give <class> --spec <spec model id> or --all")
        runner(a.cls, a.spec, a, repo)


if __name__ == "__main__":
    main()
