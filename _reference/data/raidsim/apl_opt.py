"""Search a raid spec's rotation (the simulator's action priority list, APL) for a better one.

    python _reference/data/raidsim/apl_opt.py mage --spec frost-raid [--rounds 15] [--write]
    python _reference/data/raidsim/apl_opt.py --all [--write]

Local search over the priority list, starting from the rotation the spec uses now (our optimized one when specs.json names
`apl_opt`, else the simulator's): move an action up, to the top or down; drop it; show a hidden one; drop its condition or one
part of an and/or; change a numeric threshold (mana %, seconds, stacks); insert an action taken from the class's other
rotations in the simulator (at the top, in the middle or before the filler). Every candidate runs through the ElliotWood/Forever
simulator with common random numbers (seed 1, `--iterations`) on the spec's tuning builds (our best build and the simulator's best
preset from the last race, or the `--tune` builds), in the setting the spec is ranked in (the training dummy for DPS, the raid
setting for tanks, where the score is the tank value). The best candidates are run again on seed 2 with `--confirm` iterations on
every build the entry lists, and a change is kept only when it wins there by more than `--min-gain` on the tuning builds and costs no
listed build more than `--max-loss` (against the current rotation and against the pass's start). The loop stops when no change wins.
Until 2026-10-07 every candidate ran on every listed build and the score averaged over all of them (see `search`).

With --write: the rotation goes to `_reference/data/raidsim/apls/<class>/<spec>.apl.json` (changed items carry a note), the
search record to `<class>/research/raid/raidsim/<spec>-rotation-search.json`, and specs.json gets `apl_opt` pointing at the file, so the
races, calibrations and rotation pages use it from then on (run.py `apl_path`).
"""
import argparse
import contextlib
import copy
import datetime
import functools
import importlib.util
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "_reference/data"))
import paths  # noqa: E402


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# this folder's run.py under its own name: render_sim_presets imports the fight lab's run.py as `run`
R = _load("raidrun", HERE / "run.py")


@functools.lru_cache(maxsize=None)
def RSP():
    return _load("render_sim_presets_mod", ROOT / "_reference/data/render_sim_presets.py")

OUT_DIR = HERE / "apls"
CLASS = [None]   # the class being searched (spell_ranks)


# ------------------------------------------------------------------------------------------------ simulator calls
def bench(entry, repo, builds, iterations, seed, setting, tag, extra=None):
    """{label: result row} for builds [{label, talents, apl_json?, gear_json?}] in one simulator run. The rotation is the setting's own
    (run.py apl_path(entry, repo, setting)): until 2026-10-01 this took the entry's ranking setting, so raid-setting calls of damage
    entries (talent_opt.py --setting raid, fullraid_search.py, setting_audit.py's raid half) ran the dummy rotation in a full raid."""
    cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]), "apl": str(R.apl_path(entry, repo, setting)),
           "spec": entry.get("spec", {}), **R.setting_cfg(entry, setting),
           "profession1": entry.get("profession1", "Engineering"), "profession2": entry.get("profession2", ""),
           "distanceFromTarget": entry.get("distance", 5), "inFrontOfTarget": entry.get("in_front", False), "reactionTimeMs": 200,
           "iterations": iterations, "duration": R.FIGHT, "seed": R.sim_seed(seed), "isTank": entry.get("tank", False), "builds": builds,
           **(extra or {})}   # extra config keys: {"link": true, "api_version": n} makes share links (gear_links.py)
    d = repo / "bench"
    d.mkdir(exist_ok=True)
    import threading
    worker = threading.current_thread() is not threading.main_thread()   # threaded callers (the family polish) get their own file
    p = d / (f"aplopt-{tag}-{os.getpid()}" + (f"-t{threading.get_ident()}" if worker else "") + ".json")
    p.write_text(json.dumps(cfg), encoding="utf-8")
    bench_exe = repo / ("foreverbench.exe" if (repo / "foreverbench.exe").exists() else "foreverbench")
    r = subprocess.run([str(bench_exe), "--config", str(p), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"bench failed: {r.stderr[-1500:]}")
    if worker:
        p.unlink(missing_ok=True)
    rows = {}
    for line in r.stdout.splitlines():
        if line.startswith("{"):
            x = json.loads(line)
            rows[x["label"]] = x
    return rows


def value(row, ref, tank):
    """A candidate's result against the current rotation's on the same build: DPS ratio, or tank value for tanks."""
    if not row or row.get("error") or not ref:
        return None
    if tank:
        return R.tank_value(row, ref)
    return (row.get("dps") or 0.0) / (ref.get("dps") or 1.0)


def score(rows, cur, labels, tank):
    vals = [value(rows.get(lab), cur.get(b), tank) for lab, b in labels]
    if any(v is None for v in vals) or not vals:
        return None
    return sum(vals) / len(vals)


# ------------------------------------------------------------------------------------------------ rotation edits
def items(apl):
    return apl.get("priorityList") or []


def text(item, N):
    return ("(hidden) " if item.get("hide") else "") + RSP().action(item.get("action", {}), N)


def const_paths(x, path=()):
    """Paths to every numeric constant ({"const": {"val": "30%"}}) under x."""
    if isinstance(x, dict):
        c = x.get("const")
        if len(x) == 1 and isinstance(c, dict) and isinstance(c.get("val"), str):
            yield path + ("const", "val"), c["val"]
            return
        for k, v in x.items():
            yield from const_paths(v, path + (k,))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from const_paths(v, path + (i,))


def set_path(x, path, v):
    for k in path[:-1]:
        x = x[k]
    x[path[-1]] = v


NUM = re.compile(r"^(-?[0-9]*\.?[0-9]+)(ms|s|%)?$")


def fmt(y, unit):
    s = f"{y:.3f}".rstrip("0").rstrip(".")
    return (s if s not in ("", "-0") else "0") + unit


def const_variants(s):
    m = NUM.match(s.strip())
    if not m:
        return []
    x, unit = float(m.group(1)), m.group(2) or ""
    out = set()
    if unit == "%":
        out |= {x + d for d in (-20, -10, -5, 5, 10, 20) if 0 <= x + d <= 100}
    elif unit in ("s", "ms"):
        step = 1000.0 if unit == "ms" else 1.0
        out |= {x * f for f in (0.0, 0.5, 0.75, 1.5, 2.0)} | {x + d * step for d in (-1.0, -0.5, 0.5, 1.0) if x + d * step >= 0}
    else:
        if x == int(x):
            out |= {x + d for d in (-2, -1, 1, 2) if x + d >= 0}
        out |= {x * f for f in (0.5, 0.75, 1.5, 2.0)}
    return [fmt(y, unit) for y in sorted(out) if fmt(y, unit) != s.strip()]


def mana_ge(x):
    return {"cmp": {"op": "OpGe", "lhs": {"currentManaPercent": {}}, "rhs": {"const": {"val": f"{x}%"}}}}


def mana_lt(x):
    return {"cmp": {"op": "OpLt", "lhs": {"currentManaPercent": {}}, "rhs": {"const": {"val": f"{x}%"}}}}


def time_ge(x):
    return {"cmp": {"op": "OpGe", "lhs": {"remainingTime": {}}, "rhs": {"const": {"val": f"{x}s"}}}}


def add_cond(action, c):
    old = action.get("condition")
    if not old:
        action["condition"] = c
    elif isinstance(old.get("and"), dict):
        old["and"]["vals"] = list(old["and"].get("vals", [])) + [c]
    else:
        action["condition"] = {"and": {"vals": [old, c]}}


CASTS = ("castSpell", "channelSpell", "multidot")


@functools.lru_cache(maxsize=None)
def spell_ranks(cls):
    """{spell id: (name, rank, [(rank, id), ...] of that spell)} from the beta spellbook (forever-spells/<class>.json)."""
    out = {}
    p = ROOT / "_reference/data/forever-spells" / f"{cls}.json"
    if not p.exists():
        return out
    for tab in json.load(open(p, encoding="utf-8")).get("tabs", []):
        for sp in tab.get("spells", []):
            ranks = []
            cooldown = any((r.get("cooldown") or "").strip() for r in sp.get("ranks", []))
            for r in sp.get("ranks", []):
                m = re.search(r"(\d+)", r.get("rank") or "")
                if r.get("id") and m:
                    ranks.append((int(m.group(1)), int(r["id"])))
            ranks.sort()
            for rk, sid in ranks:
                out[sid] = (sp.get("name"), rk, tuple(ranks), cooldown)
    return out


def key(item):
    return json.dumps({k: v for k, v in item.items() if k != "notes"}, sort_keys=True)


INSERT_ONLY = [False]   # set by --insert-only (2026-09-29): the spellbook sweep tries only insertions of spells no rotation casts


def neighbors(apl, pool, N):
    """[(description, new apl)] one edit away."""
    out = []
    lst = items(apl)
    vis = [i for i, it in enumerate(lst) if not it.get("hide")]

    def with_list(new, desc):
        a = copy.deepcopy(apl)
        a["priorityList"] = new
        out.append((desc, a))

    for pos, i in (() if INSERT_ONLY[0] else enumerate(vis)):   # --insert-only: skip every edit but the insertions below
        it = lst[i]
        t = text(it, N)
        # drop
        with_list([x for j, x in enumerate(lst) if j != i], f"drop: {t}")
        # move up by one, to the top, down by one (among the shown items)
        if pos > 0:
            j = vis[pos - 1]
            new = list(lst)
            new[i], new[j] = new[j], new[i]
            with_list(new, f"move up above '{text(lst[j], N)}': {t}")
            if pos > 1:
                new = [x for j2, x in enumerate(lst) if j2 != i]
                new.insert(vis[0], it)
                with_list(new, f"move to the top: {t}")
        if pos < len(vis) - 1:
            j = vis[pos + 1]
            new = list(lst)
            new[i], new[j] = new[j], new[i]
            with_list(new, f"move down below '{text(lst[j], N)}': {t}")
        # conditions: drop it, or one part of an and / or
        cond = it.get("action", {}).get("condition")
        if cond:
            new_it = copy.deepcopy(it)
            del new_it["action"]["condition"]
            new = list(lst)
            new[i] = new_it
            with_list(new, f"drop the condition: {t}")
            for op in ("and", "or"):
                vals = (cond.get(op) or {}).get("vals") if isinstance(cond.get(op), dict) else None
                if vals and len(vals) >= 2:
                    for k in range(len(vals)):
                        rest = [v for n, v in enumerate(vals) if n != k]
                        new_it = copy.deepcopy(it)
                        new_it["action"]["condition"] = rest[0] if len(rest) == 1 else {op: {"vals": rest}}
                        new = list(lst)
                        new[i] = new_it
                        with_list(new, f"drop '{RSP().val(vals[k], N)}' from the condition: {t}")
        # thresholds
        for path, s in const_paths(it.get("action", {})):
            for v in const_variants(s):
                new_it = copy.deepcopy(it)
                set_path(new_it["action"], path, v)
                new = list(lst)
                new[i] = new_it
                with_list(new, f"threshold {s} -> {v}: {t}")
    # guards: only with enough mana, only with enough fight left
    for i in (() if INSERT_ONLY[0] else vis):
        it = lst[i]
        kind = next((k for k in it.get("action", {}) if k != "condition"), None)
        if kind not in CASTS + ("sequence", "strictSequence"):
            continue
        t = text(it, N)
        for x in (10, 25, 40, 60):
            new_it = copy.deepcopy(it)
            add_cond(new_it["action"], mana_ge(x))
            new = list(lst)
            new[i] = new_it
            with_list(new, f"only above {x}% mana: {t}")
        for x in (3, 6, 10, 20):
            new_it = copy.deepcopy(it)
            add_cond(new_it["action"], time_ge(x))
            new = list(lst)
            new[i] = new_it
            with_list(new, f"only with {x}s or more of the fight left: {t}")
    # lower spell ranks: always, or while mana is low (inserted just above the item)
    for i in (() if INSERT_ONLY[0] else vis):
        it = lst[i]
        kind = next((k for k in it.get("action", {}) if k != "condition"), None)
        if kind not in ("castSpell", "channelSpell"):
            continue
        sid = (it["action"][kind].get("spellId") or {}).get("spellId")
        info = spell_ranks(CLASS[0]).get(sid) if sid else None
        if not info:
            continue
        name, rk, ranks, cooldown = info
        lower = sorted({r for r in (rk - 1, rk - 2, max(1, rk // 2)) if any(r == x for x, _ in ranks) and r < rk}, reverse=True)
        for r in lower:
            rid = next(i2 for x, i2 in ranks if x == r)
            low = copy.deepcopy(it)
            low["action"][kind]["spellId"] = {"spellId": rid, "rank": r}
            new = list(lst)
            new[i] = low
            with_list(new, f"always rank {r} instead of rank {rk}: {t if False else text(it, N)}")
            if cooldown:
                # a spell with a cooldown: the simulator gives every rank its own cooldown (the game shares it), so a second rank next
                # to the first would be cast twice (Lay on Hands three times a fight, 2026-09-27): only the replacement above
                continue
            for x in (15, 30, 50):
                guard = copy.deepcopy(low)
                add_cond(guard["action"], mana_lt(x))
                new = list(lst)
                new.insert(i, guard)
                with_list(new, f"rank {r} below {x}% mana, above: {text(it, N)}")
    # show a hidden item
    for i, it in (() if INSERT_ONLY[0] else enumerate(lst)):
        if it.get("hide"):
            new_it = copy.deepcopy(it)
            new_it.pop("hide", None)
            new = list(lst)
            new[i] = new_it
            with_list(new, f"show the hidden: {text(new_it, N)}")
    # insert an action from the class's other rotations
    have = {key(x) for x in lst}
    # top, middle, before the filler and (2026-09-29) after everything: a spell used only when nothing else is ready (the traps won there)
    spots = sorted({vis[0] if vis else 0, vis[len(vis) // 2] if vis else 0, vis[-1] if vis else 0, len(lst)})
    for cand in pool:
        if key(cand) in have:
            continue
        for s in spots:
            new = list(lst)
            new.insert(s, copy.deepcopy(cand))
            where = "at the top" if s == (vis[0] if vis else 0) else ("before the filler" if vis and s == vis[-1] else ("at the end" if s == len(lst) else "in the middle"))
            with_list(new, f"insert {where}: {text(cand, N)}")
    seen, uniq = set(), []
    for d, a in out:
        k = json.dumps(a.get("priorityList"), sort_keys=True)
        if k not in seen:
            seen.add(k)
            uniq.append((d, a))
    return uniq


def key_list(apl):
    return json.dumps([key(x) for x in items(apl)])


def sim_base(entry, repo):
    """The entry's base rotation (the simulator's, or our base file), or None when it cannot be read."""
    p = R.sim_path(entry["apl"])
    p = pathlib.Path(p) if pathlib.Path(p).is_absolute() else repo / entry["apl"]
    try:
        return json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return None


NOT_COMBAT = ("Teleport", "Revive", "Call of the", "Totemic Recall", "Totemic Projection", "Enchanted Flare", "Confounding Flash",
              "Contingency Plan", "Voice of Truth")


def new_spell_pool(cls):
    """Casts of the class's spellbook, the top rank of each: every spell that could deal damage or raise it (2026-09-29, user request
    "make sure we are not missing a spell in a rotation"; until then only the spells the beta spellbook marks new against Classic Era,
    which left Arcane Shot and the hunter's traps untried). Pet abilities, travel, utility and crowd control are left out
    (NOT_COMBAT_SPELLS, and a tooltip must speak of damage, attack power, speed, crit, spell power, armor or mana). A spell with a
    duration ("over N sec") also comes guarded by "only while its dot is not ticking", so a bleed or a dot is not re-cast on every
    GCD. A spell the simulator does not know is dropped from the rotation by its validator, so such a candidate changes nothing."""
    p = ROOT / "_reference/data/forever-spells" / f"{cls}.json"
    if not p.exists():
        return []
    out = []
    for tab in json.load(open(p, encoding="utf-8")).get("tabs", []):
        if tab.get("name") == "Pets":
            continue
        for sp in tab.get("spells", []):
            ranks = [r for r in sp.get("ranks", []) if r.get("id")]
            if not ranks or "Passive" in (ranks[-1].get("rank") or "") or (sp.get("name") not in COMBAT_ALLOW
                                                                            and any(sp.get("name", "").startswith(x) for x in NOT_COMBAT + NOT_COMBAT_SPELLS)):
                continue
            text_all = " ".join(str(r.get("text", "")) for r in ranks)
            if not COMBAT_TEXT.search(text_all):
                continue
            top = max(ranks, key=lambda r: (r.get("level") or 0, int(re.search(r"\d+", r.get("rank") or "0").group() or 0) if re.search(r"\d+", r.get("rank") or "") else 0))
            sid = int(top["id"])
            out.append({"action": {"castSpell": {"spellId": {"spellId": sid}}}})
            if re.search(r"over \d+ sec", str(top.get("text", ""))):
                out.append({"action": {"condition": {"not": {"val": {"dotIsActive": {"spellId": {"spellId": sid}}}}},
                                       "castSpell": {"spellId": {"spellId": sid}}}})
            # a lasting debuff or buff ("for 5 min", "for 30 sec": curses, Sunder Armor, marks, armors): a plain cast recasts it on every
            # GCD, so it also comes guarded by "only while its aura is not on the target" and "... not on you" (2026-09-29: a plain Curse
            # of the Elements took a warlock to 0 DPS)
            if re.search(r"for \d+ (sec|min)", str(top.get("text", ""))):
                for unit in ("CurrentTarget", "Self"):
                    out.append({"action": {"condition": {"auraIsInactive": {"sourceUnit": {"type": unit}, "auraId": {"spellId": sid}}},
                                           "castSpell": {"spellId": {"spellId": sid}}}})
    return out


def point_blank_ids(cls):
    """Spell ids whose tooltip reaches only enemies near the caster ("within 10 yards", "nearby", "in a cone", "in front of the caster"):
    the spellbook sweep of 2026-09-29 kept Blast Wave and Cone of Cold for a mage standing 20 yards away, where they cannot reach."""
    p = ROOT / "_reference/data/forever-spells" / f"{cls}.json"
    out = set()
    for tab in (json.load(open(p, encoding="utf-8")).get("tabs", []) if p.exists() else []):
        for sp in tab.get("spells", []):
            text = " ".join(str(r.get("text", "")) for r in sp.get("ranks", []))
            if re.search(r"radiates? outward from the caster|enemies within \d+ yards(?! of the (?:target|totem))|in a cone|in front of the caster|"
                         r"around the caster|nearby enemies(?! of the target)(?!.*(?:jump|bounc|chain))", text, re.I) and "Totem" not in sp.get("name", ""):
                out |= {int(r["id"]) for r in sp.get("ranks", []) if r.get("id")}
    return out


# spells no damage rotation should try (travel, summons, crowd control, stealth, resurrection, pet care)
NOT_COMBAT_SPELLS = ("Summon", "Conjure", "Create", "Track", "Find ", "Portal", "Resurrect", "Redemption", "Ancestral Spirit", "Rebirth", "Travel Form",
                     "Aquatic Form", "Ghost Wolf", "Water Walking", "Water Breathing", "Levitate", "Slow Fall", "Unending Breath", "Detect", "Sense",
                     "Eye of", "Far Sight", "Mind Vision", "Beast Lore", "Tame", "Feed Pet", "Dismiss", "Revive Pet", "Mend Pet", "Eyes of the Beast",
                     "Disenchant", "Pick Lock", "Sap", "Distract", "Stealth", "Vanish", "Prowl", "Shadowmeld", "Fade", "Feign Death", "Soulstone",
                     "Ritual", "Enslave", "Banish", "Fear", "Hibernate", "Polymorph", "Shackle", "Mind Control", "Scare", "Turn Undead",
                     "Psychic Scream", "Howl of Terror", "Seduction", "Blind", "Gouge", "Freezing Trap", "Frost Trap", "Scatter Shot", "Repentance")
COMBAT_ALLOW = ("Summon Hawk",)   # damage spells the prefixes above would drop (2026-10-01: Summon Hawk is a Beast Mastery damage talent)
COMBAT_TEXT = re.compile(r"damage|attack power|attack speed|haste|critical|spell power|chance to hit|armor by|mana regen|restores? \d+ mana|increas\w+ (your|all)", re.I)


def class_pool(repo, entry):
    """Every priority item of the class's rotations in the simulator (all its spec folders), hidden or not, shown."""
    cls_dir = repo / "ui/specs" / entry["sim_spec"].split("/")[0]
    pool, seen = [], set()
    for f in sorted(cls_dir.glob("*/apls/*.apl.json")):
        try:
            a = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        for it in items(a):
            it = {k: v for k, v in it.items() if k not in ("hide", "notes")}
            k = key(it)
            if k not in seen and it.get("action"):
                seen.add(k)
                pool.append(it)
    return pool


def explicit_ids(apl):
    """(kind, id) of every spell and item the rotation casts by name."""
    out = set()

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in CASTS and isinstance(v, dict) and isinstance(v.get("spellId"), dict):
                    for kind in ("spellId", "itemId"):
                        if v["spellId"].get(kind):
                            out.add((kind, v["spellId"][kind]))
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(apl)
    return out


def cooldown_pool(entry, repo, builds, setting, tag, apls):
    """Explicit casts of the cooldowns the builds use (2026-09-28): every action with no damage of its own that a run of the given
    rotations casts 1 to 4 times a fight (trinkets, potions, racials, Bestial Wrath, Intimidation). `use every other cooldown` is
    all or nothing, so without these the search could only keep or drop the lot: the Beast Mastery dummy rotation dropped it (+3%)
    and with it the mana potion and Bestial Wrath, because Intimidation spent mana for nothing on a dummy. One line per cooldown
    lets the search keep the useful ones."""
    found = {}
    for n, ap in enumerate(apls):
        bl = [{"label": f"{n}|{i}", "talents": b["talents"], "apl_json": ap, **gear_of(b)} for i, b in enumerate(builds)]
        for r in bench(entry, repo, bl, 300, 1, setting, tag + "-cd").values():
            for x in r.get("actions") or []:
                if (x.get("damage") or 0) == 0 and 0 < (x.get("casts") or 0) <= 4:
                    kind = "itemId" if x.get("itemId") else "spellId" if x.get("spellId") else None
                    if kind:
                        found[(kind, x[kind])] = True
    have = set().union(*(explicit_ids(ap) for ap in apls))
    return [{"action": {"castSpell": {"spellId": {kind: i}}}} for kind, i in sorted(found) if (kind, i) not in have]


# ------------------------------------------------------------------------------------------------ targets
def gear_of(b):
    """A tuning build's own gear (bench gear_json), when it carries one."""
    return {"gear_json": b["gear_json"]} if b.get("gear_json") else {}


def tune_builds(path, cls, trees):
    """--tune: builds to tune on, from a JSON list of {label, allocation ({talent: rank} or by tree) or talents, gear (a .gear.json
    path, optional)}, on top of the entry's main builds, which stay protected (2026-10-01: ml_pipeline.py tunes each entry's rotation
    on the talent search's winners in their tier gear; a first version tuned on them alone, so a change could cost the hand drafts)."""
    out = []
    for b in json.load(open(path, encoding="utf-8")):
        al = b.get("allocation")
        if isinstance(al, dict) and al and all(isinstance(v, list) for v in al.values()):
            al = {n: r for items in al.values() for n, r in items}
        t = b.get("talents") or R.talents_string(trees, al)
        g = b.get("gear")
        out.append({"label": b["label"], "talents": t, **({"gear_json": {"items": json.load(open(ROOT / g, encoding="utf-8"))["items"]}, "gear": g} if g else {})})
    return out


def main_builds(cls, spec, entry, repo, trees, where=None):
    """The builds a spec's rotation is tuned on: our best build and the simulator's best preset in the last race, the entry's
    `tune_builds` (builds whose own lines the rotation carries), and since 2026-10-02 every other build of ours the entry lists (the
    pages show them as alternatives; parse builds only in the raid setting): no change may cost any of them more than --max-loss.
    Before, an alternative was unprotected: the 2026-10-01 pass dropped the Frost rotation's Evocation line and cost the 1/13/37 Frost
    build, which has no Arcane mana talents, 6.1%."""
    rep_path = paths.raidsim_dir(cls) / f"{spec}.json"
    tank = bool(entry.get("tank"))
    out = []
    if rep_path.exists():
        rep = json.load(open(rep_path, encoding="utf-8"))
        rows = [x for x in rep["results"] if x.get("dps") and not x.get("error") and not x["label"].startswith("cand-")]
        keyf = (lambda x: x.get("value") or 0) if tank else (lambda x: x["dps"])
        ours = sorted([x for x in rows if x["ours"]], key=lambda x: -keyf(x))
        theirs = sorted([x for x in rows if not x["ours"]], key=lambda x: -keyf(x))
        for x in ours[:1] + theirs[:1]:
            if x.get("talents") and x["talents"] not in {b["talents"] for b in out}:
                out.append({"label": x["label"], "talents": x["talents"]})
    data = {b["id"]: b for b in json.load(open(ROOT / cls / "research/talents/forever/proposed-builds.json", encoding="utf-8"))["builds"]}
    if not out:
        for bid in entry["builds"][:1]:
            out.append({"label": bid, "talents": R.talents_string(trees, R.alloc_of(data[bid]))})
        for pr in R.sim_presets(repo, entry)[:1] if "preset_names" in entry else []:   # a rotation-only tree before its first race
            out.append({"label": pr["label"], "talents": pr["talents"]})
    for bid in entry.get("tune_builds", []):   # builds of another rotation family sharing the entry (2026-09-28: the Arcane Power Frost draft)
        t = R.talents_string(trees, R.alloc_of(data[bid]))
        if t not in {b["talents"] for b in out}:
            out.append({"label": bid, "talents": t})
    raid = (where or R.setting(entry)) == "raid"
    for bid in entry.get("builds", []):   # every alternative the pages show is protected too
        if bid in data and (raid or not bid.endswith("-parse")):
            t = R.talents_string(trees, R.alloc_of(data[bid]))
            if t not in {b["talents"] for b in out}:
                out.append({"label": bid, "talents": t})
    return out


# ------------------------------------------------------------------------------------------------ search
def search(cls, spec, a, repo, N, where=None):
    entry = R.SPECS[cls][spec]
    CLASS[0] = cls
    tank = bool(entry.get("tank"))
    setting = where or R.setting(entry)
    trees = R.load_trees(repo, cls)
    builds = main_builds(cls, spec, entry, repo, trees, setting)
    if getattr(a, "tune", None):   # the given builds first; the entry's main builds stay protected (no change may cost them 0.1% either)
        extra = tune_builds(a.tune, cls, trees)
        builds = extra + [dict(b, protect_only=True) for b in builds if b["talents"] not in {x["talents"] for x in extra}]
    # Tuning builds and protected builds (2026-10-07): candidates are scored on the tuning builds only (the --tune builds, else our best
    # build, the simulator's best preset and the entry's tune_builds) and run on them alone on seed 1; the protected builds (every
    # other build the entry lists) are run only for the confirmed few on seed 2, where no change may cost any build --max-loss against
    # the current rotation or against this pass's start. Before, every candidate ran on every build and the score averaged over all of
    # them: a re-tune of the hunter's bm-raid rotation ran 365 candidates on 6 builds for one round that kept nothing (2 h 17 min),
    # and a gain on the tuned build alone was diluted by the number of protected builds (6 builds: +0.6% on the winner read +0.1%).
    tune_idx = [bi for bi, b in enumerate(builds) if not b.get("protect_only")] or list(range(len(builds)))
    tune_labels = [(bi, bi) for bi in tune_idx]
    base_path = (repo / entry["apl"]) if getattr(a, "fresh", False) and not entry["apl"].startswith("_reference/") else R.apl_path(entry, repo, setting)
    base = json.load(open(base_path, encoding="utf-8"))
    pool = class_pool(repo, entry)
    tag = f"{cls}-{spec}"
    sim_apl = sim_base(entry, repo)
    cds = cooldown_pool(entry, repo, builds, setting, tag, [base] + ([sim_apl] if sim_apl and key_list(sim_apl) != key_list(base) else []))
    pool += [c for c in cds if key(c) not in {key(x) for x in pool}]
    have_ids = explicit_ids({"priorityList": pool}) | explicit_ids(base)
    news = [c for c in new_spell_pool(cls) if ("spellId", c["action"]["castSpell"]["spellId"]["spellId"]) not in have_ids]
    if entry.get("distance", 5) > 8:   # a caster at range: no point-blank spells (the simulator does not range-check Blast Wave or Cone of Cold)
        pb = point_blank_ids(cls)
        news = [c for c in news if c["action"]["castSpell"]["spellId"]["spellId"] not in pb]
    pool += news
    if INSERT_ONLY[0]:
        pool = news
    print(f"== {cls} {spec}: {len(items(base))} actions from {base_path.name}, {len(pool)} pool actions ({len(cds)} cooldowns, {len(news)} spellbook spells), tuned on "
          + ", ".join(builds[bi]["label"] for bi in tune_idx)
          + (("; protected: " + ", ".join(b["label"] for bi, b in enumerate(builds) if bi not in tune_idx)) if len(tune_idx) < len(builds) else "")
          + f" ({setting}{', tank value' if tank else ''})", flush=True)

    def run_set(apls, iterations, seed, which=None):
        """{"<candidate>|<build>": row} for the candidate rotations on the builds `which` (indices; default every build)."""
        idx = list(range(len(builds))) if which is None else which
        bl = [{"label": f"{ci}|{bi}", "talents": builds[bi]["talents"], "apl_json": ap, **gear_of(builds[bi])} for ci, ap in enumerate(apls) for bi in idx]
        return bench(entry, repo, bl, iterations, seed, setting, tag)

    def per_build(rows, ci):
        return {bi: rows.get(f"{ci}|{bi}") for bi in range(len(builds))}

    cur = base
    cur1 = per_build(run_set([cur], a.iterations, 1), 0)
    start_rows = {1: cur1, 2: per_build(run_set([cur], a.confirm, 2), 0)}
    log = []
    for rnd in range(1, a.rounds + 1):
        cands = neighbors(cur, pool, N)
        rows = run_set([ap for _, ap in cands], a.iterations, 1, tune_idx)
        scored = []
        for ci, (d, ap) in enumerate(cands):
            sc = score({bi: r for bi, r in per_build(rows, ci).items()}, cur1, tune_labels, tank)
            if sc is not None:
                scored.append((sc, ci, d, ap))
        scored.sort(key=lambda x: -x[0])
        top = [x for x in scored if x[0] > 1 + a.screen_gain][: a.top]
        if not top and a.lookahead and scored:
            # no single edit wins: expand the best few one step further (two edits that only pay together)
            seeds_ = scored[: a.lookahead]
            pairs = []
            for sc_a, ci_a, d_a, ap_a in seeds_:
                for d_b, ap_b in neighbors(ap_a, pool, N):
                    pairs.append((f"{d_a} + {d_b}", ap_b))
            prow = run_set([ap for _, ap in pairs], a.iterations, 1, tune_idx)
            ps = []
            for ci, (d, ap) in enumerate(pairs):
                sc = score(per_build(prow, ci), cur1, tune_labels, tank)
                if sc is not None:
                    ps.append((sc, ci, d, ap))
            ps.sort(key=lambda x: -x[0])
            top = [x for x in ps if x[0] > 1 + a.screen_gain][: a.top]
            if top:
                print(f"  round {rnd}: no single edit ahead; {len(pairs)} two-edit candidates, {len(top)} ahead on seed 1", flush=True)
        if not top:
            print(f"  round {rnd}: {len(cands)} candidates, none ahead on seed 1 (best {scored[0][0] - 1:+.2%}: {scored[0][2][:110]})" if scored else f"  round {rnd}: no candidates", flush=True)
            break
        conf = run_set([cur] + [x[3] for x in top], a.confirm, 2)
        ref2 = per_build(conf, 0)
        best = None
        for k, (sc1, ci, d, ap) in enumerate(top, start=1):
            rows_k = per_build(conf, k)
            sc2 = score(rows_k, ref2, tune_labels, tank)
            # a change must not cost any of the builds (a preset's gain cannot pay for our build's loss), neither against the current
            # rotation nor against this pass's start (so kept changes cannot wear a protected build down round by round)
            worst = min((value(rows_k.get(bi), ref2.get(bi), tank) or 0.0) for bi in range(len(builds)))
            worst0 = min((value(rows_k.get(bi), start_rows[2].get(bi), tank) or 0.0) for bi in range(len(builds)))
            if worst < 1 - a.max_loss or worst0 < 1 - a.max_loss:
                continue
            if sc2 is not None and (best is None or sc2 > best[0]):
                best = (sc2, sc1, d, ap)
        if not best or best[0] <= 1 + a.min_gain:
            print(f"  round {rnd}: {len(cands)} candidates, {len(top)} ahead on seed 1, none confirmed on seed 2 (best {best[0] - 1 if best else 0:+.2%})", flush=True)
            break
        sc2, sc1, d, ap = best
        log.append({"round": rnd, "change": d, "gain_seed1": sc1 - 1, "gain_seed2": sc2 - 1, "candidates": len(cands)})
        print(f"  round {rnd}: {d[:150]}  ({sc1 - 1:+.2%} seed 1, {sc2 - 1:+.2%} seed 2; {len(cands)} candidates)", flush=True)
        cur = ap
        cur1 = per_build(run_set([cur], a.iterations, 1), 0)
    # final check on a third seed, in the setting searched
    final = {}
    for st in [setting]:
        extra = [sim_apl] if sim_apl is not None and key_list(sim_apl) != key_list(base) else []
        rows = run_set([base, cur] + extra, a.confirm, 3)
        final[st] = {b["label"]: {"before": (rows.get(f"0|{bi}") or {}).get("dps"), "after": (rows.get(f"1|{bi}") or {}).get("dps"),
                                   "base": (rows.get(f"{2 if extra else 0}|{bi}") or {}).get("dps"),
                                   "before_value": 1.0 if tank else None,
                                   "after_value": R.tank_value(rows.get(f"1|{bi}"), rows.get(f"0|{bi}")) if tank and rows.get(f"1|{bi}") and rows.get(f"0|{bi}") else None,
                                   "oom_before": (rows.get(f"0|{bi}") or {}).get("oom_seconds"), "oom_after": (rows.get(f"1|{bi}") or {}).get("oom_seconds")}
                     for bi, b in enumerate(builds)}
    for st, rows in final.items():
        for lab, v in rows.items():
            if v["before"] and v["after"]:
                print(f"  {st:6s} {lab[:44]:44s} {v['before']:8.1f} -> {v['after']:8.1f} DPS ({v['after'] / v['before'] - 1:+.2%})"
                      + (f", tank value {v['after_value']:.3f}" if v.get("after_value") else ""), flush=True)
    return {"class": cls, "spec": spec, "date": datetime.date.today().isoformat(), "commit": R.git_commit(repo), "setting": setting, "tank": tank,
            "simulator_apl": entry["apl"],
            "start": str(base_path.relative_to(repo) if str(base_path).startswith(str(repo)) else base_path.relative_to(ROOT)),
            "builds": [{k: v for k, v in b.items() if k != "gear_json"} for b in builds], "tuned_on": [builds[bi]["label"] for bi in tune_idx], "iterations": a.iterations, "confirm": a.confirm, "changes": log, "final": final}, base, cur


def write(cls, spec, rec, base, cur, N):
    OUT_DIR.joinpath(cls).mkdir(parents=True, exist_ok=True)
    entry = R.SPECS[cls][spec]
    k = R.apl_key(entry, rec["setting"])
    out = OUT_DIR / cls / (f"{spec}.apl.json" if k == "apl_opt" else f"{spec}-raid.apl.json")
    started_from_ours = str(R.apl_path(entry, R.repo_path(__import__("argparse").Namespace(repo=None)), rec["setting"])).startswith(str(ROOT))
    if not rec["changes"] and not started_from_ours:
        # nothing beat the simulator's rotation: keep it (no copy, no apl_opt key); the record says the search found nothing
        rep = paths.raidsim_dir(cls) / f"{spec}-rotation-search.json"
        allrec = json.load(open(rep, encoding="utf-8")) if rep.exists() else {}
        if "changes" in allrec:
            allrec = {allrec.get("setting", "dummy"): allrec}
        allrec[rec["setting"]] = rec
        rep.write_text(json.dumps(allrec, indent=1), encoding="utf-8")
        print(f"  no change beat the simulator's rotation ({rec['setting']}): kept it; recorded in {rep.relative_to(ROOT)}", flush=True)
        return
    rep = paths.raidsim_dir(cls) / f"{spec}-rotation-search.json"
    allrec = json.load(open(rep, encoding="utf-8")) if rep.exists() else {}
    if "changes" in allrec:   # an older single-setting record
        allrec = {allrec.get("setting", "dummy"): allrec}
    prior = allrec.get(rec["setting"])
    if started_from_ours and prior and prior.get("changes"):
        # a later pass from our tuned rotation (2026-09-28: the bench's potion fix): the changes accumulate, and the third-seed
        # check compares the entry's base rotation (run again now) with the final one
        n0, p0 = len(prior["changes"]), prior.get("passes", 1)
        rec = dict(rec, start=prior.get("start", rec["start"]), first_date=prior.get("first_date", prior.get("date")), passes=p0 + 1,
                   changes=[dict(c, **{"pass": c.get("pass", 1)}) for c in prior["changes"]]
                   + [dict(c, round=n0 + c["round"], **{"pass": p0 + 1}) for c in rec["changes"]])
        for rows in rec["final"].values():
            for v in rows.values():
                if v.get("base"):
                    v["before"] = v["base"]
    if rec["changes"]:
        # note the items that differ from the starting rotation
        before = {key(x) for x in items(base)}
        for it in items(cur):
            if key(it) not in before:
                it["notes"] = f"apl_opt {rec['date']}: changed or added by the rotation search (see {spec}-rotation-search.json)"
    out.write_text(json.dumps(cur, indent=1), encoding="utf-8")
    allrec[rec["setting"]] = rec
    rep.write_text(json.dumps(allrec, indent=1), encoding="utf-8")
    # specs.json: point the spec at our rotation for this kind of setting (text edit keeps the file's layout)
    sp = HERE / "specs.json"
    with specs_lock():   # several searches may run at once (one per class): read and write specs.json under a lock
        _point_specs(sp, cls, spec, k, out)
    print(f"  wrote {out.relative_to(ROOT)} and {rep.relative_to(ROOT)}", flush=True)


@contextlib.contextmanager
def specs_lock():
    """An exclusive lock on specs.json.lock (Linux and Windows: filelock.py), so searches of different classes can run in parallel."""
    from filelock import locked
    with locked(HERE / "specs.json.lock"):
        yield


def _point_specs(sp, cls, spec, k, out):
    s = sp.read_text(encoding="utf-8")
    rel = out.relative_to(ROOT).as_posix()
    data = json.loads(s)
    block = re.search(r'"' + re.escape(cls) + r'": \{.*?\n  \}', s, re.S)
    if data[cls][spec].get(k) != rel and block:
        sub = s[block.start():block.end()]
        if f'"{k}": ' in sub.split(f'"{spec}": {{', 1)[1].split('"sim_class"', 1)[0]:
            head, tail = sub.split(f'"{spec}": {{', 1)
            tail = re.sub(r'"' + k + r'": "[^"]*"', f'"{k}": "{rel}"', tail, count=1)
            sub = head + f'"{spec}": {{' + tail
        else:
            m = re.search(r'("' + re.escape(spec) + r'": \{\n(\s+))', sub)
            if not m:
                raise SystemExit(f"specs.json: cannot find the {spec} entry")
            sub = sub[: m.end(1)] + f'"{k}": "{rel}",\n{m.group(2)}' + sub[m.end(1):]
        s = s[: block.start()] + sub + s[block.end():]
        json.loads(s)
        sp.write_text(s, encoding="utf-8")
        R.SPECS[cls][spec][k] = rel


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cls", nargs="?")
    ap.add_argument("--spec")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--rounds", type=int, default=15)
    ap.add_argument("--iterations", type=int, default=3000, help="iterations per candidate and build on seed 1")
    ap.add_argument("--confirm", type=int, default=20000, help="iterations per confirmation run on seed 2 (and the final check on seed 3)")
    ap.add_argument("--top", type=int, default=6, help="candidates confirmed per round")
    ap.add_argument("--screen-gain", type=float, default=0.001, help="gain on seed 1 a candidate needs to be confirmed")
    ap.add_argument("--min-gain", type=float, default=0.0015, help="gain on seed 2 a change needs to be kept")
    ap.add_argument("--lookahead", type=int, default=3, help="when no single edit wins, expand this many of the best one step further (0 = off)")
    ap.add_argument("--max-loss", type=float, default=0.001, help="a change may not cost any tuning build more than this on seed 2")
    ap.add_argument("--fresh", action="store_true", help="start from the simulator's rotation, not our tuned one")
    ap.add_argument("--setting", choices=["dummy", "raid"], help="search only this kind of setting (default: the dummy and the raid for DPS specs, the raid for tanks)")
    ap.add_argument("--repo")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--insert-only", action="store_true", help="try only insertions of spellbook spells the rotation does not cast (the sweep of 2026-09-29)")
    ap.add_argument("--tune", help="JSON list of builds to tune on instead of the last race's best (see tune_builds)")
    a = ap.parse_args()
    INSERT_ONLY[0] = a.insert_only
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=a.repo))
    N = RSP().Names(repo)
    todo = [(c, s) for c, sp in R.SPECS.items() if not c.startswith("_") and isinstance(sp, dict) for s in sp if isinstance(sp[s], dict) and "apl" in sp[s]] if a.all else [(a.cls, a.spec)]
    for cls, spec in todo:
        entry = R.SPECS[cls][spec]
        wheres = [a.setting] if a.setting else (["raid"] if entry.get("tank") else ["dummy", "raid"])
        for where in wheres:
            rec, base, cur = search(cls, spec, a, repo, N, where)
            if a.write:
                write(cls, spec, rec, base, cur, N)


if __name__ == "__main__":
    main()
