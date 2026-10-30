"""Signature spells in the raid tools (user rule 2026-10-22: "make sure that the specs we're testing are actually using the spells for that
spec, or else it's pointless ... The specs should use the spells that make that spec, that spec. Especially the hybrid ones. You're
testing too much for pure optimizations"; strictness "main damage": a spec's signature spells are the core of its rotation, never
dropped, and a spec played that way that is slower is shown slower).

The rule lives in `_reference/data/signature_spells.json` (per class and spec: `required` spells, `core` sources and `min_share`, with
per-mode overrides). This module is what the raid tools share:

- `rule(cls, spec)`: the raid rule of a spec (the `modes.raid` override applied), or None;
- `required_talents(cls, spec)`: the talents that grant a required spell (a talent named after the spell: Holy Shock, Mortal Strike,
  Summon Hawk); the talent searches never take them to 0 ranks for a build of that spec (ml_talents.Space.valid, talent_opt.py,
  filler_audit.py);
- `entry_spec(cls, entry, alloc, build=None)`: the spec a build plays in a raid entry (its `spec` field; else the entry's hybrid when
  the entry is built for one hybrid and the split sits in its trees, as open_builds.raid_spec files it; else spec_modes.spec_of);
- `check(cls, spec, actions, names, held)`: the full-raid test of one simulator result row: every required spell the build can cast is
  cast, and the core sources carry at least min_share of its damage;
- `apl_violation(cur, cand, req_ids, cooldown_ids)`: a rotation edit that drops a line casting a required spell, or moves one below the
  filler (apl_opt.py screens every candidate with it);
- `penalty(chk)`: the search objective's factor for a build that fails (ml_talents.Sim with `signature=True`): core share / min_share,
  halved when a required spell goes uncast, so the open and deep searches look for the best build that plays its spec.

WOW_FOREVER_SIGNATURE=0 switches every check off (an escape hatch for reproducing older records; the default is on).
"""
import functools
import json
import os
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
SIG_PATH = DATA / "signature_spells.json"
SPEC_POINTS = 30
SHARE_TOL = 0.005    # rotation search: a candidate may not lower a protected build's core share below min(min_share, current) - this
CAST_KEEP = 0.5      # rotation search: a required spell's casts may not fall below this share of the current rotation's (gated off)
NON_SPELL = ("pet", "melee", "Auto Shot")
WHITE = ("Auto Attack", "Melee", "Melee (off-hand)", "Melee (Off Hand)", "Attack")   # "Attack": the bench's name for some white swings


def enabled():
    return os.environ.get("WOW_FOREVER_SIGNATURE", "1") not in ("0", "", "off", "false")


@functools.lru_cache(maxsize=None)
def table():
    return json.load(open(SIG_PATH, encoding="utf-8")) if SIG_PATH.exists() else {}


def rule(cls, spec, mode="raid"):
    """{required, core, min_share, note} of a spec in a mode (the `modes` override applied), or None."""
    r = (table().get(cls) or {}).get(spec)
    if not isinstance(r, dict):
        return None
    out = {k: r[k] for k in ("required", "core", "min_share", "note") if k in r}
    out.update((r.get("modes") or {}).get(mode) or {})
    out.setdefault("required", [])
    out.setdefault("core", [])
    out.setdefault("min_share", 0.0)
    return out


def specs(cls):
    return [s for s in (table().get(cls) or {}) if not s.startswith("_")]


# ------------------------------------------------------------------------------------------------ talents
@functools.lru_cache(maxsize=None)
def _talents(cls):
    """({talent: tree}, {talent: row}, [tree names]) from forever-talents/<class>.json."""
    d = json.load(open(DATA / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    tree_of, row = {}, {}
    for tr in d["trees"]:
        for t in tr["talents"]:
            tree_of[t["name"]] = tr["name"]
            row[t["name"]] = t.get("row", 0)
    return tree_of, row, [tr["name"] for tr in d["trees"]]


def required_talents(cls, spec, mode="raid"):
    """Talents that grant a required spell of the spec (a talent named after the spell)."""
    r = rule(cls, spec, mode) if enabled() else None
    if not r:
        return set()
    tree_of = _talents(cls)[0]
    return {s for s in r["required"] if s in tree_of}


def required_talents_by_spec(cls, mode="raid"):
    """{spec: talents} for every spec of the class with talent-granted required spells."""
    out = {}
    for s in specs(cls):
        t = required_talents(cls, s, mode)
        if t:
            out[s] = t
    return out


def talents_ok(cls, spec, alloc, trees=None, mode="raid"):
    """True when the build holds every talent that grants a required spell of one of the specs whose rule it must pass (rule_specs), or
    no rule applies. A build without them cannot play its spec's signature spells, so it is no bar a new build must beat and no build a
    rotation is tuned on (2026-10-24 audit: the three Assassination raid builds lack Mutilate; the rotation was tuned on one of them and
    a Mutilate winner would only have 'confirmed' it)."""
    if not enabled():
        return True
    specs_ = rule_specs(cls, spec, trees, mode)
    if not specs_:
        return True
    held = flat_of(alloc)
    return any(all(held.get(t) for t in required_talents(cls, s, mode)) for s in specs_)


def flat_of(alloc):
    """{talent: rank} from {tree: [[talent, rank]]} or {talent: rank}."""
    if not alloc:
        return {}
    if all(isinstance(v, list) for v in alloc.values()):
        return {n: r for items in alloc.values() for n, r in items if r}
    return {n: r for n, r in alloc.items() if r}


def by_tree(cls, flat):
    tree_of, _, trees = _talents(cls)
    out = {t: [] for t in trees}
    for n, r in flat.items():
        if r and n in tree_of:
            out[tree_of[n]].append([n, r])
    return out


def classify(cls, flat):
    """spec_modes.spec_of on a {talent: rank} allocation of a damage build (a tree with 30+ points, else 'Hybrid A/B' in tree order)."""
    tree_of, _, trees = _talents(cls)
    pts = {t: 0 for t in trees}
    for n, r in flat.items():
        if n in tree_of:
            pts[tree_of[n]] += r
    top = sorted(trees, key=lambda t: -pts[t])
    if pts[top[0]] >= SPEC_POINTS:
        return top[0]
    return "Hybrid " + "/".join(t for t in trees if t in top[:2])


def _entry_trees(cls, entry):
    import sys
    sys.path.insert(0, str(DATA))
    import spec_modes as SM
    return SM.RAID_ENTRY_TREES.get((cls, entry)) or set()


@functools.lru_cache(maxsize=None)
def _tank_entry(cls, entry):
    """True for a specs.json tank entry (`"tank": true`)."""
    if not entry:
        return False
    try:
        return bool(((json.load(open(HERE / "specs.json", encoding="utf-8")).get(cls) or {}).get(entry) or {}).get("tank"))
    except (OSError, ValueError):
        return False


def entry_spec(cls, entry, alloc, build=None, role=None):
    """The spec a build plays in a raid entry: its own `spec` field; tanks the class's tank tree; else the entry's hybrid when the entry is
    built for one hybrid (Frostfire's frostfire-raid, Smite's smite-dps) and the split is that hybrid or one of its trees; else by split."""
    tank = (role or (build or {}).get("role")) == "tank" or _tank_entry(cls, entry)
    if build and build.get("spec") and not tank:   # a tank build's spec field names its tree ("Feral Combat"), not the bear
        return build["spec"]
    if tank:   # 2026-10-26 audit: unlabelled tank-entry builds (a
        # search's "deep: tank", the simulator's presets) were filed by split, so the bear rotation search kept the cat's core share
        import sys
        sys.path.insert(0, str(DATA))
        import spec_modes as SM
        if cls in SM.TANK_TREE:
            # the druid's Feral Combat rule is the cat's (Claw, Rip, Ferocious Bite): a bear tank has no signature rule of its own
            return SM.TANK_TREE[cls] + (" (Bear)" if cls == "druid" else "")
    spec = classify(cls, flat_of(alloc))
    for t in _entry_trees(cls, entry) if entry else ():
        if t.startswith("Hybrid ") and (spec == t or spec in t[len("Hybrid "):].split("/")):
            return t
    return spec


def entry_specs(cls, entry, builds=()):
    """Every spec whose signature lines an entry's rotation must keep: the trees it is built for (RAID_ENTRY_TREES) and the specs of the
    builds it lists (hybrids of those trees)."""
    import sys
    sys.path.insert(0, str(DATA))
    import spec_modes as SM
    own = set(_entry_trees(cls, entry))
    out = {s for s in own if rule(cls, s)}
    for b in builds:
        s = b if isinstance(b, str) else entry_spec(cls, entry, b.get("allocation") or {}, b)
        if s and rule(cls, s) and (not own or SM.rotation_allows(s, own)):
            out.add(s)
    return out


# ------------------------------------------------------------------------------------------------ spell ids and names
def ids_by_name(names):
    """{spell name: {ids}} from an id -> name map (run.spell_names)."""
    out = {}
    for i, n in names.items():
        out.setdefault(n, set()).add(int(i))
    return out


def required_ids(cls, spec_list, names, mode="raid"):
    """{required spell: {ids}} over the given specs."""
    inv = ids_by_name(names)
    out = {}
    for s in spec_list:
        r = rule(cls, s, mode)
        for sp in (r or {}).get("required", []):
            out.setdefault(sp, set()).update(inv.get(sp, set()))
    return out


# bench names that differ from the spell names the rule uses: the simulator books Deep Wounds as "Deep Wound"; id-names.json lacks the
# rogue's level-60 poison procs (the official store names them Instant Poison VI and Deadly Poison V), so they read "spell N"
NAME_ALIASES = {"Deep Wound": "Deep Wounds", "spell 11337": "Instant Poison", "spell 25349": "Deadly Poison"}
ID_NAMES = {11337: "Instant Poison VI", 25349: "Deadly Poison V"}


def _strip(name):
    return re.sub(r"\s+(?:[IVX]+|Rank \d+)$", "", name.split(" (")[0]).strip()


def matches(core, name):
    """Whether a bench action name (run.action_shares: 'Pet: Claw', 'Auto Attack', 'Judgement of Righteousness') is a core source."""
    if core == "pet":
        return name.startswith("Pet: ")
    if name.startswith("Pet: "):
        return False
    if core == "melee":
        return name in WHITE
    if core == "Auto Shot":
        return name in ("Auto Shot", "Shoot")
    name = NAME_ALIASES.get(name, name)
    base = _strip(name)
    if base == core or name == core or base.startswith(core + " "):
        return True
    if core.endswith(" Weapon") and base == core[: -len(" Weapon")] + " Attack":   # Windfury Weapon's hits
        return True
    return False


def shares_of(actions, names, key="damage"):
    """{action name: share of the build's damage} from the bench's per-action rows (as run.action_shares)."""
    import sys
    sys.path.insert(0, str(HERE))
    import id_names
    dmg = {}
    for a in actions or []:
        if a.get("spellId"):
            n = names.get(int(a["spellId"])) or ID_NAMES.get(int(a["spellId"])) or id_names.spell(a["spellId"])
        elif a.get("itemId"):
            n = id_names.item(a["itemId"])
        else:
            n = {"OtherActionAttack": "Auto Attack", "OtherActionShoot": "Auto Shot"}.get(a.get("other", ""), a.get("other", "other"))
        if a.get("pet"):
            n = "Pet: " + n
        dmg[n] = dmg.get(n, 0.0) + float(a.get(key, 0.0) or 0.0)
    tot = sum(dmg.values()) or 1.0
    return {k: v / tot for k, v in sorted(dmg.items(), key=lambda kv: -kv[1]) if v > 0}


def casts_of(actions, names):
    """{spell name: casts per fight} of the player (pets left out)."""
    import sys
    sys.path.insert(0, str(HERE))
    import id_names
    out = {}
    for a in actions or []:
        if a.get("pet") or not a.get("spellId"):
            continue
        c = float(a.get("casts") or 0.0)
        if c <= 0:
            continue
        n = names.get(int(a["spellId"])) or id_names.spell(a["spellId"])
        out[n] = out.get(n, 0.0) + c
    return out


def core_share(cls, spec, shares, mode="raid"):
    r = rule(cls, spec, mode)
    if not r:
        return None
    return round(sum(v for k, v in shares.items() if any(matches(c, k) for c in r["core"])), 4)


def rule_specs(cls, spec, trees=None, mode="raid"):
    """The specs whose rule a build filed under `spec` must pass (any one): its own; a hybrid without a rule of its own, its trees' (only
    those the entry is built for when `trees` names any; 2026-10-23, the paladin's 17/17/17 Holy/Protection leveling winner without Holy
    Shock had passed as 'no rule'; signature.rule_specs)."""
    if rule(cls, spec, mode):
        return [spec]
    if not spec or not spec.startswith("Hybrid "):
        return []
    two = spec[len("Hybrid "):].split("/")
    own = [t for t in two if trees and t in trees]
    return [t for t in (own or two) if rule(cls, t, mode)]


def check_shares(cls, spec, shares, casts, held=None, mode="raid", trees=None):
    """The rule on already-mapped shares ({name: share}) and casts ({name: casts per fight}; None = unknown). `held` ({talent: rank}):
    a required spell granted by a talent the build lacks fails as 'talent missing'. Returns {spec, ok, core_share, min_share,
    uncast, missing_talents, why} or None when no rule applies (or the check is switched off). A hybrid without a rule of its own passes
    on either of its trees' rules (rule_specs; `trees`: the entry's)."""
    if not enabled():
        return None
    specs_ = rule_specs(cls, spec, trees, mode)
    if specs_ != [spec]:
        best = None
        for s_ in specs_:
            c = check_shares(cls, s_, shares, casts, held, mode)
            c["filed_as"] = spec
            if best is None or c["ok"] or penalty(c) > penalty(best):
                best = c
            if c["ok"]:
                break
        return best
    r = rule(cls, spec, mode)
    if not r:
        return None
    tree_of = _talents(cls)[0]
    missing = sorted(s for s in r["required"] if s in tree_of and held is not None and not held.get(s))
    cast = {_strip(k): v for k, v in (casts or {}).items()} if casts is not None else None
    uncast = sorted(s for s in r["required"] if s not in missing and cast is not None and not any(
        (k == s or k.startswith(s + " ")) and v >= 0.5 for k, v in cast.items()))
    cs = core_share(cls, spec, shares or {}, mode) if shares else None
    low = cs is not None and cs < r["min_share"]
    why = []
    if missing:
        why.append("lacks " + ", ".join(missing))
    if uncast:
        why.append("never casts " + ", ".join(uncast))
    if low:
        f = ".1%" if f"{cs:.0%}" == f"{r['min_share']:.0%}" else ".0%"   # "12% under 12%" read as no failure (2026-10-30)
        why.append(f"core share {cs:{f}} under {r['min_share']:{f}} ({', '.join(r['core'])})")
    return {"spec": spec, "ok": not (missing or uncast or low) and cs is not None, "core_share": cs, "min_share": r["min_share"],
            "uncast": uncast, "missing_talents": missing, "why": "; ".join(why) if why else ("no damage shares" if cs is None else "")}


def check(cls, spec, actions, names, held=None, mode="raid", trees=None):
    """check_shares on one bench result row's actions."""
    if not actions:
        return None
    return check_shares(cls, spec, shares_of(actions, names), casts_of(actions, names), held, mode, trees)


FAIL_STEP = 0.9   # the factor every failing build pays on top of its core-share ratio (the leveling searches' too)


def penalty(chk):
    """The search objective's factor for a build (1 when it passes or has no rule)."""
    if not chk or chk.get("ok") or chk.get("core_share") is None:
        return 1.0
    f = FAIL_STEP * (min(1.0, chk["core_share"] / chk["min_share"]) if chk["min_share"] else 1.0)   # 2026-10-26 audit (fl_signature):
    if chk.get("uncast") or chk.get("missing_talents"):   # a near miss (49.5% of 50%, x0.99) had beaten passing builds 2% slower
        f *= 0.5
    return max(0.05, f)


def measure(cls, entry, alloc, repo, R, A, iterations=3000, seed=7, setting="raid", gear_json=None, build=None):
    """Run one build of an entry in the full raid and check it: (check dict, dps). R, A: the caller's run.py and apl_opt.py modules."""
    flat = flat_of(alloc)
    spec = entry_spec(cls, entry, flat, build)
    trees = R.load_trees(repo, cls)
    b = {"label": "sig", "talents": R.talents_string(trees, flat), **({"gear_json": gear_json} if gear_json else {})}
    row = A.bench(R.SPECS[cls][entry], repo, [b], iterations, seed, setting, f"sig-{cls}-{entry}").get("sig") or {}
    names = R.spell_names(repo, cls)
    chk = check(cls, spec, row.get("actions"), names, flat, trees=_entry_trees(cls, entry))
    if chk is None:
        chk = {"spec": spec, "ok": True, "core_share": None, "min_share": None, "uncast": [], "missing_talents": [], "why": "no rule for this spec"}
    # the shares and casts too, so a caller that files the build under another spec can re-check it without a run (check_shares)
    chk.update({"entry": entry, "setting": setting, "iterations": iterations, "dps": round(row.get("dps") or 0.0, 1), "date": __import__("datetime").date.today().isoformat(),
                "commit": R.git_commit(repo), "shares": {k: round(v, 4) for k, v in shares_of(row.get("actions"), names).items()},
                "casts": {k: round(v, 2) for k, v in casts_of(row.get("actions"), names).items()}})
    return chk, row.get("dps")


def recheck(cls, spec, chk, flat):
    """A stored check (measure) for another spec: the same shares and casts against that spec's rule."""
    if not chk or chk.get("shares") is None:
        return None
    out = check_shares(cls, spec, chk["shares"], chk.get("casts"), flat_of(flat))
    if out is None:
        return {"spec": spec, "ok": True, "core_share": None, "min_share": None, "uncast": [], "missing_talents": [], "why": "no rule for this spec"}
    return dict(out, entry=chk.get("entry"), dps=chk.get("dps"), date=chk.get("date"), commit=chk.get("commit"))


# ------------------------------------------------------------------------------------------------ rotations
CASTS = ("castSpell", "channelSpell", "multidot")


def item_casts(item):
    """Spell ids an APL item casts (not the ones its condition reads)."""
    out = set()

    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k == "condition":
                    continue
                if k in CASTS and isinstance(v, dict) and isinstance(v.get("spellId"), dict) and v["spellId"].get("spellId"):
                    out.add(int(v["spellId"]["spellId"]))
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(item.get("action") or {})
    return out


@functools.lru_cache(maxsize=None)
def book_ids(cls):
    """(every spell id of the class spellbook, the ids of spells with a cooldown): forever-spells/<class>.json, talent spells included."""
    p = DATA / "forever-spells" / f"{cls}.json"
    every, cd = set(), set()
    for tab in (json.load(open(p, encoding="utf-8")).get("tabs", []) if p.exists() else []):
        ids = {int(r["id"]) for sp in tab.get("spells", []) for r in sp.get("ranks", []) if r.get("id")}
        every |= ids
        for sp in tab.get("spells", []):
            if any((r.get("cooldown") or "").strip() for r in sp.get("ranks", [])):
                cd |= {int(r["id"]) for r in sp.get("ranks", []) if r.get("id")}
    return frozenset(every), frozenset(cd)


def filler_index(lst, cooldown_ids, known_ids=None):
    """Index of the rotation's filler: the first shown line with no condition that casts a spellbook spell without a cooldown (else the
    end). Items, racials and spells outside the spellbook (`known_ids`, when given) are never the filler."""
    for i, it in enumerate(lst):
        if it.get("hide"):
            continue
        act = it.get("action") or {}
        if act.get("condition"):
            continue
        kind = next((k for k in act if k in ("castSpell", "channelSpell")), None)   # a multidot only refreshes a dot: never the filler
        if not kind:
            continue
        ids = item_casts(it)
        if ids and not (ids & cooldown_ids) and (known_ids is None or ids <= known_ids):
            return i
    return len(lst)


def line_counts(apl, req_ids, cooldown_ids, known_ids=None):
    """{required spell: (shown lines casting it, of them at or above the filler)}."""
    lst = apl.get("priorityList") or []
    fill = filler_index(lst, cooldown_ids, known_ids)
    out = {}
    for sp, ids in req_ids.items():
        n = up = 0
        for i, it in enumerate(lst):
            if it.get("hide") or not (item_casts(it) & ids):
                continue
            n += 1
            up += i <= fill
        out[sp] = (n, up)
    return out


def apl_violation(cur, cand, req_ids, cooldown_ids, known_ids=None):
    """A reason when the candidate rotation drops (or hides) a line that casts a required spell, or moves one below the filler; else None."""
    if not req_ids or not enabled():
        return None
    a, b = line_counts(cur, req_ids, cooldown_ids, known_ids), line_counts(cand, req_ids, cooldown_ids, known_ids)
    for sp, (n, up) in a.items():
        n2, up2 = b.get(sp, (0, 0))
        if n2 < n:
            return f"drops a line casting {sp}"
        if up2 < up:
            return f"moves a line casting {sp} below the filler"
    return None


def cast_drop(cur_casts, cand_casts, spells):
    """A reason when a required spell's casts fall under CAST_KEEP of the current rotation's (or to none)."""
    for sp in spells:
        c0 = sum(v for k, v in cur_casts.items() if _strip(k) == sp)
        c1 = sum(v for k, v in cand_casts.items() if _strip(k) == sp)
        if c0 >= 1 and c1 < max(0.5, CAST_KEEP * c0):
            return f"{sp} casts {c0:.1f} -> {c1:.1f} a fight"
    return None
