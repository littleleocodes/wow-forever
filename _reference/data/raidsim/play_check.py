"""The play check (2026-11-20; the user on the audit session's recommendations after D11, Hunter's Mark never cast in the converted
official hunter rotations: "Go with your recommendations"). We had judged builds by a DPS number two seeds reproduce, nobody read what
they pressed, and drops were silent. This reads what each build a page may show presses, and what does nothing, on the entry's
committed raid rotation in a full raid.

    python _reference/data/raidsim/play_check.py [classes] [--entry E] [--fights 3000] [--skip-switches] [--write]

Per raid entry and listed build (full raid, the entry's raid rotation and gear, seed 1, common random numbers; DPS compared to the cent):
 a. rotation spells never cast: every spell a cast line names (pre-pull, priority list, groups) that the build casts 0 times (Judgement
    counted under the judged seal, as the pages count it). Reasons: "talent not taken" (a talent's ability the build lacks), "used: its
    casts are booked under another id" (removing the talent changes the result: Swift Judgement), "switch off" (the line's condition is
    a variable held at false), "condition never held" (any other condition), "racial" (an id the simulator's racials.go names; racials
    are off). A FAIL: a class spell on an unconditional line, never cast; an id that is neither a spell of the class nor a racial (the
    line can never fire: Lava Burst and Frost Blast, gone from the game, and a trinket's spell cast as a spell sat in our rotations until
    2026-11-20; the client's own name is shown when the local tables have it); a debuff the class turns off in the raid for its own cast
    (the hunter's mark, the warlock's assigned curse) that the rotation never casts.
 b. talent abilities never cast: an ability a talent of the build grants, cast 0 times. Reasons: booked under another id (as in a),
    raidsim/unused-abilities.json's kind (automatic, prerequisite, situational), "prerequisite" (removing it breaks the build), a
    defensive tooltip ("situational": an absorb, a heal, damage taken, an immunity such as Ice Block), a parry or block trigger; else a
    FAIL.
 c. talents worth nothing: removing the talent leaves the DPS the same to the cent. Fine when the removal breaks the build (a gate: tier
    points or a prerequisite), a filler record lists it (a free point, or a utility move's destination), (b) accepts it, or it carries
    a raid utility tag (utility_tags.py: range, survival ...; the audit session's ruling on Flame Throwing); else a FAIL (a dead point).
 d. inert raid switches: each raid buff or debuff the build's role should feel (ROLE_SWITCHES), switched off alone (a category's
    partners together: Expose and Sunder Armor, Faerie Fire and Recklessness, Leader of the Pack and Moonkin Aura), leaving the DPS the
    same to the cent: a FAIL. Not judged: what the class or the build's own talent supplies (the hunter's mark, the warlock's assigned
    curse, a mage's Arcane Intellect, Trueshot Aura, Leader of the Pack, Moonkin Form).
 e. the rotations: a cast of a class spell the simulator does not register for the class (the bench's validate mode; the line never
    fires) on any rotation the entry points at is a FAIL; a converted official rotation (apls/<class>/upstream/) that differs from a
    fresh conversion of upstream's file is a FAIL.
Record raidsim/play-check.json: per class and entry the fingerprint (rotation, gear and builds), per build the findings, `fail` lists.
Tanks are checked on (a), (b), (e) and on (c) by tank value; healers are not simulated.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path[:0] = [str(HERE), str(DATA), str(DATA / "deep-runs")]
import run as R  # noqa: E402
import apl_opt as A  # noqa: E402
import filler_audit as FA  # noqa: E402
import render_rotations as RR  # noqa: E402
import trainer_ranks as TR  # noqa: E402
import validate_builds as VB  # noqa: E402
import utility_tags as UT  # noqa: E402
import paths  # noqa: E402
import flags_bench as FB  # noqa: E402  (the audit's D12 guard a, 2026-11-20)

OUT = HERE / "play-check.json"
RACIALS, CLIENT = None, {}
# the simulator's exclusive categories (buffs_auto_gen.go, debuffs_auto_gen.go): partners switch off together, or the one left on covers
# the other (Forever's Leader of the Pack and Moonkin Aura both give every raid member 3% crit; RaidCrit holds one of them)
MAJOR_ARMOR, MINOR_ARMOR, RAID_CRIT = ("sunder_armor", "expose_armor"), ("faerie_fire", "curse_of_recklessness"), ("leader_of_the_pack", "moonkin_aura")
PHYS = ["battle_shout", "greater_blessing_of_might", "strength_of_earth_totem", "windfury_totem", RAID_CRIT, MAJOR_ARMOR, MINOR_ARMOR,
        "gift_of_arthas"]
RANGED = ["trueshot_aura", RAID_CRIT, MAJOR_ARMOR, MINOR_ARMOR, "gift_of_arthas"]
CASTER = ["arcane_intellect", RAID_CRIT]
# per class and entry kind: the switches its damage should feel (conservative: a school a debuff does not touch is left out)
ROLE_SWITCHES = {
    "warrior": PHYS, "rogue": PHYS,
    "paladin": PHYS + ["judgement_of_the_crusader"],
    "druid:feral-cat-dps": PHYS,
    "druid:balance-dps": CASTER,
    "shaman:enhancement-dps": [s for s in PHYS if s != "windfury_totem"],    # never_buffs: Windfury Weapon disables the totem
    "shaman": CASTER,
    "hunter:melee-dps": PHYS, "hunter:survival-pet-raid": PHYS, "hunter": RANGED,
    "mage": [RAID_CRIT, "curse_of_elements"],                              # its own Arcane Intellect
    "warlock": CASTER,                                                     # its own assigned curse
    "priest": CASTER,
}
NOT_CLASS_OWN = {"mage:arcane-dps": ["curse_of_elements"]}   # entries whose school a listed debuff may not touch: left out
# a switch the build supplies itself, by a talent (the class turns the raid's copy on: Trueshot Aura, Leader of the Pack, Moonkin Form)
# or by a spell it casts (its own totem, shout, sunder, judgement or Faerie Fire holds the same category): not judged for that build
OWN_TALENT = {"trueshot_aura": {"Trueshot Aura"}, "leader_of_the_pack+moonkin_aura": {"Leader of the Pack", "Moonkin Form"}}
OWN_CAST = {"strength_of_earth_totem": {"Strength of Earth Totem"}, "windfury_totem": {"Windfury Totem"}, "battle_shout": {"Battle Shout"},
            "judgement_of_the_crusader": {"Seal of the Crusader", "Judgement of the Crusader"},
            "sunder_armor+expose_armor": {"Sunder Armor", "Expose Armor"}, "faerie_fire+curse_of_recklessness": {"Faerie Fire", "Faerie Fire (Feral)"},
            "greater_blessing_of_might": {"Blessing of Might", "Greater Blessing of Might"}, "arcane_intellect": {"Arcane Intellect"}}
# a talent that is the raid buff itself: worth nothing in a full raid that already has the buff, the raid's source in a real one
RAID_BUFF_TALENT = {"Leader of the Pack": "leader_of_the_pack", "Trueshot Aura": "trueshot_aura", "Moonkin Form": "moonkin_aura"}
# a spell only for some creature types: never cast on the bench's Elemental (Exorcism, Holy Wrath: Undead and Demons)
TARGET_TYPE = re.compile(r"\bUndead\b|\bDemons?\b", re.I)
# a raid debuff the class turns off in favour of its own cast (the official simulator's hunter.go: the mark; warlock.go: the assigned
# curse, default Elements): the rotation must cast it (D11, 2026-11-20: no hunter rotation of ours had cast the mark)
CURSES = {"Recklessness": "Curse of Recklessness", "Weakness": "Curse of Weakness", "NoCurse": None}
# a defensive the filler audit's pattern misses: Ice Block ("protecting you from all physical attacks and spells"), immunities
SHIELD = re.compile(r"protecting you|immune to|immunity", re.I)


def racial_ids(repo):
    """Every spell id the simulator's racials.go names (racials are off: their lines never fire, by design)."""
    p = repo / "sim" / "core" / "racials.go"
    return {int(x) for x in re.findall(r"(?<![0-9])([0-9]{4,7})(?![0-9])", p.read_text(encoding="utf-8"))} if p.exists() else set()


def client_names():
    """The client's spell names, when the local wago tables are there (never in the repository): names a dead line's id."""
    f = sorted((pathlib.Path.home() / ".wow-forever-tools" / "wago").glob("SpellName-*.csv"))
    out = {}
    if f:
        for ln in f[-1].read_text(encoding="utf-8", errors="replace").splitlines()[1:]:
            m = re.match(r'(\d+),"?(.*?)"?$', ln)
            if m:
                out[int(m.group(1))] = m.group(2)
    return out


# The audit's D12 guards (2026-11-20 night): the bear's rotation had cast Maul's swing-damage spell off the swing timer for four days
# (about seven times the threat) and nothing physical was checked. b2: an on-next-swing attack's hits and the white main-hand swings
# together cannot exceed twice the swings the weapon makes in the fight (haste and extra attacks stay well under that); b3: the
# rotation's casts on the global cooldown cannot exceed one a second; c2: our rotation beating the simulator's own rotation for the same
# build by more than TOO_GOOD is suspect until raidsim/too-good-notes.json explains the casts ({class: {entry: {build or "*": why}}}).
TOO_GOOD = 0.20
TOO_GOOD_NOTES = HERE / "too-good-notes.json"
OFF_GCD = json.load(open(DATA / "fightlab" / "spell_gcd.json", encoding="utf-8")).get("off_gcd", {})
_DB = {}


def mh_speed(cls, entry, repo):
    """The main hand's swing time in the entry's gear: Bear Form swings 2.5 s, Cat Form 1.0 s (the forms replace the weapon)."""
    if cls == "druid":
        return 2.5 if entry.get("tank") else 1.0
    try:
        g = R.sim_path(entry["gear"])
        g = pathlib.Path(g) if pathlib.Path(g).is_absolute() else repo / entry["gear"]
        items = json.load(open(g, encoding="utf-8")).get("items") or []
        mh = (items[14] or {}).get("id") if len(items) > 14 else None
        if not _DB:
            _DB.update({int(x["id"]): x for x in json.load(open(repo / "assets/database/db.json", encoding="utf-8")).get("items", [])})
        return (_DB.get(int(mh)) or {}).get("weaponSpeed") if mh else None
    except (OSError, ValueError, KeyError, TypeError):
        return None


U = "_reference/data/raidsim/apls/"
# The official simulator's own rotations for each entry's spec (2026-11-20; c2 compares ours with the best of them): our converted copies
# under apls/<class>/upstream/ (trainer ranks, the hunter's mark rank; the hunter's and paladin's are SIML upstream), else its JSON files
# under ui/specs/ (trainer ranks swapped here). The official simulator ships none for the priest and the shaman.
SIM_ROTATIONS = {
    "mage": {"frost-raid": [U + "mage/upstream/frost.apl.json"], "arcane-dps": [U + "mage/upstream/arcane.apl.json", U + "mage/upstream/arcaneFireFill.apl.json"],
             "fire-raid": [U + "mage/upstream/deepFire.apl.json"], "frostfire-raid": [U + "mage/upstream/ffb.apl.json"],
             "arcane-frost-raid": [U + "mage/upstream/frost.apl.json", U + "mage/upstream/arcane.apl.json"]},
    "druid": {"balance-dps": ["ui/specs/druid/balance/apls/default.apl.json"], "feral-cat-dps": [U + "druid/upstream/adaptive.apl.json"],
              "feral-bear-tank": [U + "druid/upstream/feralbear-adaptive.apl.json"]},
    "hunter": {e: [U + f"hunter/upstream/{n}.apl.json" for n in ("default", "turret", "turret_hawk", "melee")]
               for e in ("mm-raid", "mm-lonewolf-raid", "bm-raid", "melee-dps", "survival-pet-raid")},
    "paladin": {"ret-dps": [U + "paladin/upstream/default.apl.json"], "shockadin-raid": [U + "paladin/upstream/holy_shock.apl.json"],
                "prot-tank": [U + "paladin/upstream/protection-default.apl.json"]},
    "rogue": {e: ["ui/specs/rogue/dps/apls/default.apl.json"] for e in ("combat-swords-raid", "combat-daggers-raid", "assassination-raid", "subtlety-raid")},
    "warrior": {"arms-2h-raid": ["ui/specs/warrior/dps/apls/arms.apl.json", "ui/specs/warrior/dps/apls/fury.apl.json"],
                "arms-battle-raid": ["ui/specs/warrior/dps/apls/arms.apl.json"], "fury-dw-raid": ["ui/specs/warrior/dps/apls/fury.apl.json"],
                "prot-tank": ["ui/specs/warrior/protection/apls/default.apl.json"]},
    # each official warlock rotation is written for one build (Wrack, a demon brand, Destruction, SM/Ruin): every entry against the best
    "warlock": {e: [U + f"warlock/upstream/{n}.apl.json" for n in ("aff_wrack", "demo_shadow_brand", "demo_fire_brand", "destro", "sm_ruin")]
                for e in ("affliction-raid", "affliction-wrack-raid", "demonology-raid", "destro-raid", "fire-destro-raid", "incinerate-raid", "sb-raid")},
}


def simulator_rotations(cls, ename, repo, ours):
    """[(rotation, label)] of the simulator's own rotations for the entry (SIM_ROTATIONS) that differ from ours, and a note."""
    out, skipped = [], []
    fwd = None
    for ap in (SIM_ROTATIONS.get(cls) or {}).get(ename) or []:
        p = (repo / ap) if ap.startswith("ui/") else (ROOT / ap)
        if not p.exists():
            skipped.append(f"{p.name} missing")
            continue
        rot = json.loads(p.read_text(encoding="utf-8"))
        if ap.startswith("ui/"):
            if fwd is None:
                fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in TR.load_map().items()}
            rot = json.loads(TR.swap_text(json.dumps(rot), fwd))
        if json.dumps(rot, sort_keys=True) == json.dumps(ours, sort_keys=True):
            return [], f"the entry's raid rotation is the simulator's own ({p.name})"
        out.append((rot, p.name))
    if not out:
        return [], "the official simulator ships no rotation for this spec" + (f" ({'; '.join(skipped)})" if skipped else "")
    return out, ", ".join(x[1] for x in out)


def class_options(entry):
    return (next(iter(entry["spec"].values())).get("options") or {}).get("classOptions", {}) if entry.get("spec") else {}


def stance_of(entry):
    """The stance the entry starts in ("WarriorStanceDefensive" -> "Defensive Stance"), or None."""
    s = str(class_options(entry).get("defaultStance") or "")
    m = re.match(r"WarriorStance(\w+)", s)
    return f"{m.group(1)} Stance" if m else None


def own_debuff(cls, entry):
    if cls == "hunter":
        return "Hunter's Mark"
    if cls == "warlock":
        co = str((next(iter(entry["spec"].values())).get("options") or {}).get("classOptions", {}).get("curseOptions", "Elements"))
        return CURSES.get(co.replace("CurseOptions", ""), "Curse of the Elements")
    return None


def flat(al):
    return {n: r for items in (al or {}).values() for n, r in items if r}


def casts_by_id(row, names):
    c = R.action_casts(row.get("actions"), names)[0] if row and row.get("actions") else {}
    out = {}
    for k, v in c.items():
        try:
            out[int(k)] = out.get(int(k), 0) + v
        except (TypeError, ValueError):
            pass
    return out


def cast_lines(apl):
    """[(part, index, spell id, condition or None, the line)] of every cast line, groups inlined."""
    out = []
    for part, items in (("prepull", apl.get("prepullActions") or []), ("priority", RR.expand_groups(apl) or [])):
        for i, x in enumerate(items):
            act = (x or {}).get("action") or x or {}
            for k in ("castSpell", "channelSpell", "multidot", "strictMultidot"):
                sid = ((act.get(k) or {}).get("spellId") or {}).get("spellId")
                if sid:
                    out.append((part, i, int(sid), act.get("condition"), act))
    return out


def false_switch(cond, apl):
    vv = {v.get("name"): v.get("value") for v in apl.get("valueVariables") or []}
    ref = (cond or {}).get("variableRef", {}).get("name")
    return ref if ref and vv.get(ref) == {"const": {"val": "false"}} else None


def gate(trees, alloc, talent):
    st = {}
    for t, items in alloc.items():
        st[t] = {n: r for n, r in items if r and n != talent}
    errors = []
    VB.check_state(trees, st, "x", errors)
    return errors[0] if errors else None


def filler_records(cls, bid, have):
    """Talents a filler record lists for this build's current allocation: free points and utility moves' destinations."""
    names = set()
    files = list((ROOT / cls / "research" / "raid" / "raidsim").glob(f"*-fillers-{bid}.json"))
    for f in files:
        x = json.load(open(f, encoding="utf-8"))
        if flat(x.get("allocation")) == have or flat(x.get("start")) == have:
            names |= set(x.get("free") or []) | {m["to"] for m in x.get("moves") or [] if m.get("kind") == "utility"}
    for f in HERE.glob("credited-fillers*.json"):
        x = json.load(open(f, encoding="utf-8")).get(f"{cls}/{bid}")
        if x and (flat(x.get("allocation")) == have or flat(x.get("start")) == have):
            names |= set(x.get("free") or []) | {m["to"] for m in x.get("moves") or []}
    return names


def unused_kinds(cls, entry, bid):
    p = HERE / "unused-abilities.json"
    rows = json.load(open(p, encoding="utf-8")).get("rows", []) if p.exists() else []
    return {r["talent"]: r.get("kind") for r in rows if r.get("class") == cls and r.get("entry") == entry and r.get("build") == bid}


def validate_unknown(cls, entry_name, entry, repo, talents):
    """The bench's validate mode for each rotation the entry points at: class-book casts the simulator does not register."""
    import apl_validate as AV
    exe = repo / ("foreverbench.exe" if (repo / "foreverbench.exe").exists() else "foreverbench")
    book = AV.class_book(cls)
    files = {}
    for where in ("dummy", "raid"):
        files.setdefault(str(R.apl_path(entry, repo, where)), where)
    base = R.sim_path(entry["apl"])
    files.setdefault(base if pathlib.Path(base).is_absolute() else str(repo / entry["apl"]), "dummy")
    out = []
    for apl, where in files.items():
        cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": R.sim_path(entry["gear"]), "apl": apl,
               "spec": entry.get("spec", {}), **R.setting_cfg(entry, where), "iterations": 1, "duration": R.FIGHT, "seed": 1,
               "isTank": entry.get("tank", False), "validate": True, "builds": [{"label": "v", "talents": talents}]}
        path = repo / "bench" / f"playcheck-validate-{cls}-{entry_name}.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(cfg), encoding="utf-8")
        r = subprocess.run([str(exe), "--config", str(path), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8",
                           errors="replace", cwd=str(repo))
        rows = [json.loads(x) for x in r.stdout.splitlines() if x.startswith("{")]
        if r.returncode or not rows:
            out.append(f"{pathlib.Path(apl).name}: the validate run failed")
            continue
        rot = json.load(open(apl, encoding="utf-8"))
        for kind, items in (("priority", rot.get("priorityList") or []), ("prepull", rot.get("prepullActions") or [])):
            for i, msgs in (rows[0].get(kind) or {}).items():
                cid = AV.cast_id(items[int(i)]) if int(i) < len(items) else None
                if (cid and f"does not know spell {{SpellID: {cid}}}" in " ".join(msgs) and cid in book
                        and book[cid][0] not in AV.RACE_ONLY):
                    out.append(f"{pathlib.Path(apl).name} {kind}[{i}] casts {book[cid][0]} {book[cid][1]} ({cid}), which the simulator "
                               "does not register for the class: the line never fires")
    return out


def fresh_conversion(cls, path, repo, entry=None):
    """A converted official rotation against a fresh conversion of upstream's file (None when its source cannot be found). Two specs
    of a class can ship a rotation of the same name (the druid's feralbear and feralcat adaptive.apl.json, 2026-11-20: the cat's copy
    was compared with the bear's file): the entry's own spec folder wins (its proto spec key, feralCatDruid -> feralcat)."""
    import siml_upstream_race as SU
    name = path.name.replace(".apl.json", "")
    key = next(iter((entry or {}).get("spec") or {}), "")
    want = key.lower().replace(cls, "")

    def ordered(paths):
        paths = sorted(paths)
        return [x for x in paths if x.parts[-3] == want] + [x for x in paths if x.parts[-3] != want]
    rot = None
    for src in ordered(repo.glob(f"ui/specs/{cls}/*/apls/{name}.apl.siml")):
        rot = SU.siml2json(repo, src)
        break
    if rot is None:
        for src in ordered(repo.glob(f"ui/specs/{cls}/*/apls/{name}.apl.json")):
            rot = json.load(open(src, encoding="utf-8"))
            break
    if rot is None:
        for src in ordered(repo.glob(f"ui/specs/{cls}/*/builds/{name}.build.json")):
            rot = (json.load(open(src, encoding="utf-8")).get("player") or {}).get("rotation")
            break
    if rot is None:
        return None
    SU.patch_auras(rot)
    mp = TR.load_map()
    fwd = {b: (v["trainer"], v["trainer_rank"]) for b, v in mp.items()}
    fresh = json.loads(TR.swap_text(json.dumps(rot, indent=1) + "\n", fwd))
    ours = json.load(open(path, encoding="utf-8"))
    if fresh == ours:
        return []
    diffs = [k for k in sorted(set(fresh) | set(ours)) if fresh.get(k) != ours.get(k)]
    out = []
    for k in diffs:
        a, b = fresh.get(k), ours.get(k)
        if isinstance(a, list) and isinstance(b, list):
            out.append(f"{k}: {len(a)} lines in a fresh conversion, {len(b)} in ours" + ("" if len(a) != len(b) else " (lines differ)"))
        else:
            out.append(f"{k} differs")
    return out


def fingerprint(entry, repo, builds):
    """The rotations' and the gear's content, the builds' talents and the simulator's switches: a record is current while it holds
    (run.play_fingerprint, which run.py --all and the pages read too)."""
    return R.play_fingerprint(entry, repo, builds)


def same(a, b):
    return a is not None and b is not None and abs(a - b) < 0.005


def check_entry(cls, ename, entry, repo, fights, switches=True):
    trees_sim = R.load_trees(repo, cls)
    trees = VB.load_forever()[cls]
    data = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    bids = [b for b in entry.get("builds", []) if b in data]
    if not bids:
        return None
    tank = bool(entry.get("tank"))
    names = R.spell_names(repo, cls)
    book = FA.spell_ids(cls)   # {name: (ids, tooltip)}
    id_name = {i: n for n, (ids, _) in book.items() for i in ids}
    talent_names = {t["name"] for t in sum((tr["talents"] for tr in json.load(open(DATA / "forever-talents" / f"{cls}.json",
                                                                                     encoding="utf-8"))["trees"]), [])}
    strings = {b: R.talents_string(trees_sim, R.alloc_of(data[b])) for b in bids}
    tag = f"playcheck-{ename}"
    use = UT.usefulness(cls, tank)
    global RACIALS, CLIENT
    if RACIALS is None:
        RACIALS, CLIENT = racial_ids(repo), client_names()
    def val(r):   # to the cent; a tank by every number its row carries
        if not tank:
            return round(r.get("dps") or 0, 2)
        return tuple(round(v, 2) for k, v in sorted(r.items()) if isinstance(v, (int, float)) and not isinstance(v, bool))
    base = A.bench(entry, repo, [{"label": b, "talents": t} for b, t in strings.items()], fights, 1, "raid", tag)
    apl = json.load(open(R.apl_path(entry, repo, "raid"), encoding="utf-8"))
    lines = cast_lines(apl)
    res = {"fingerprint": fingerprint(entry, repo, strings), "fights": fights, "rotation": R.apl_label(entry, repo, "raid"), "builds": {}}
    key = f"{cls}:{ename}"
    sw_list = [] if tank or not switches else [s for s in ROLE_SWITCHES.get(key, ROLE_SWITCHES.get(cls, []))
                                                  if s not in NOT_CLASS_OWN.get(key, [])]
    never_buffs = set(entry.get("never_buffs") or []) | set(entry.get("buffs_off") or []) | set(entry.get("debuffs_off") or [])
    sw_list = [s for s in sw_list if not (set(s if isinstance(s, tuple) else (s,)) & never_buffs)]
    sw_rows = {}
    for s in sw_list:
        group = list(s if isinstance(s, tuple) else (s,))
        e2 = json.loads(json.dumps(entry))
        debuff_fields = {"sunder_armor", "expose_armor", "faerie_fire", "curse_of_recklessness", "gift_of_arthas", "curse_of_elements",
                         "judgement_of_the_crusader", "judgement_of_wisdom", "judgement_of_light", "hunters_mark", "insect_swarm",
                         "scorpid_sting", "thunder_clap", "demoralizing_roar", "demoralizing_shout"}
        e2["buffs_off"] = list(e2.get("buffs_off") or []) + [g for g in group if g not in debuff_fields]
        e2["debuffs_off"] = list(e2.get("debuffs_off") or []) + [g for g in group if g in debuff_fields]
        sw_rows["+".join(group)] = A.bench(e2, repo, [{"label": b, "talents": t} for b, t in strings.items()], fights, 1, "raid", tag)
    # every talent at full rank, as apl_validate --all-talents: a talent the build lacks is (a)'s "talent not taken", not an unknown cast
    rot_fail = validate_unknown(cls, ename, entry, repo, "-".join("".join(str(t["maxPoints"]) for t in tr["talents"]) for tr in trees_sim))
    conv = []
    for where in ("raid", "dummy"):
        p = pathlib.Path(R.apl_path(entry, repo, where))
        if "/upstream/" in p.as_posix():
            d = fresh_conversion(cls, p, repo, entry)
            if d:
                conv += [f"{p.name}: {x}" for x in d]
    res["rotation_fail"] = rot_fail + [f"differs from a fresh conversion of upstream's file: {x}" for x in conv]
    # a: a cast the simulator registers only as an internal sub-action (D12; flags_bench.py), and which ids the character registers at
    # all (every talent at full rank): an id it registers is the class's, whatever our spellbook calls it (Feral Charge (Bear) 16979)
    reg_ids = None
    try:
        fv = FB.verdicts(cls, ename, entry, repo)
        for path, rws in fv.items():
            res["rotation_fail"] += [f"{pathlib.Path(path).name}: {part}[{i}] casts {names.get(sid, sid)} ({sid}{f' tag {tg}' if tg else ''}), "
                                     "which the simulator registers only as an internal sub-action (it fires outside the game's rules)"
                                     for part, i, sid, tg, v in rws if v == "INTERNAL"]
        reg_ids = {sid for part, i, sid, tg, v in fv.get(str(R.apl_path(entry, repo, "raid")), []) if v == "rotation"}
    except SystemExit as e:
        res["rotation_fail"].append(f"the internal-cast check could not run ({e})")
    # a: a rank the trainer teaches below level 20 of a spell with a rank taught at 20 or above (2026-11-20, the audit session): the
    # simulator gives it its full spell power coefficient, Classic's rule a cut of 3.75% a level below 20 (Smite rank 2 at level 6 had won
    # as a mana tool on the gap); allowed again when the rule is patched in at the next re-pin
    sr = A.spell_ranks(cls)
    res["rotation_fail"] += [f"{part}[{i}] casts {sr[sid][0]} rank {sr[sid][1]} (taught at level {lv}): below-20 rank, penalty not modelled"
                             for part, i, sid, lv in A.low_ranks(cls, apl)]
    # c2: the simulator's own rotation on the same builds and fights
    sims, simname = simulator_rotations(cls, ename, repo, apl)
    sim_rows = {}   # {build: [row under each simulator rotation]}
    for k, (srot, sname) in enumerate(sims):
        rr = A.bench(entry, repo, [{"label": b, "talents": t, "apl_json": srot} for b, t in strings.items()], fights, 1, "raid", f"{tag}-sim{k}")
        for b in strings:
            if rr.get(b) and not rr[b].get("error"):
                sim_rows.setdefault(b, []).append((sname, rr[b]))
    res["simulator_rotation"] = simname
    try:
        too_good_notes = ((json.loads(TOO_GOOD_NOTES.read_text(encoding="utf-8")) if TOO_GOOD_NOTES.exists() else {}).get(cls) or {}).get(ename) or {}
    except ValueError:
        too_good_notes = {}
    qtag = R.queue_ids(cls)
    spd = mh_speed(cls, entry, repo)
    rot_casts = {(x[2], x[3]) for x in FB.casts(apl)}
    offg = set(OFF_GCD.get(cls) or [])
    all_cs, raw_cs = {}, {}
    for b in bids:
        c = casts_by_id(base.get(b) or {}, names)
        raw_cs[b] = dict(c)
        for src, al in RR.CAST_ALIASES.items():   # Judgement's casts are booked under the judged seal's ids (as the pages count them)
            c[src] = c.get(src, 0) + sum(c.get(x, 0) for x in al)
        all_cs[b] = c
    for b in bids:
        row = base.get(b) or {}
        cs = all_cs[b]
        have = flat(data[b]["allocation"])
        f = {"dps": round(row.get("dps") or 0, 2), "never_cast": [], "abilities": [], "zero_talents": [], "inert_switches": [], "fail": []}
        acts = [x for x in (row.get("actions") or []) if not x.get("pet")]   # the character's own rows (the bench marks a pet's "pet": true)
        # b2: swings (Maul's damage cast directly read 227 hits on top of 72 white swings; a 2.5 s weapon makes 72 in 180 s)
        queued = sum(x.get("casts") or 0 for x in acts if x.get("spellId") in qtag and (x.get("tag") or 0) != qtag[x["spellId"]])
        white = sum(x.get("casts") or 0 for x in acts if x.get("other") == "OtherActionAttack" and x.get("tag") == 14)
        if queued and spd and queued + white > 2.0 * R.FIGHT / spd:
            f["fail"].append(f"b2: {queued:.0f} on-next-swing hits plus {white:.0f} white main-hand swings in a {R.FIGHT} s fight, more than "
                             f"twice the {R.FIGHT / spd:.0f} swings a {spd} s weapon makes: a line fires the hit itself")
        # b3: the global cooldown (one cast a second at the fastest)
        on_gcd = sum(x.get("casts") or 0 for x in acts if x.get("spellId") and (x["spellId"], x.get("tag") or 0) in rot_casts
                     and x["spellId"] not in qtag and (names.get(x["spellId"]) or id_name.get(x["spellId"]) or "") not in offg)
        if on_gcd > R.FIGHT * 1.02 + 2:
            f["fail"].append(f"b3: the rotation's casts on the global cooldown add up to {on_gcd:.0f} in a {R.FIGHT} s fight, more than one a second")
        f["physical"] = {"queued_hits": round(queued, 1), "white_mh_swings": round(white, 1), "mh_speed": spd, "gcd_casts": round(on_gcd, 1)}
        # c2: too good against the simulator's own rotation
        srows = sim_rows.get(b) or []
        if srows:
            best = {k: max(srows, key=lambda x: x[1].get(k) or 0) for k in (("dps", "threat") if tank else ("dps",))}
            pairs = [("DPS" if k == "dps" else "threat", row.get(k) or 0, best[k][1].get(k) or 0, best[k][0]) for k in best]
            f["simulator_rotation"] = {k: [round(o, 2), round(t_, 2), nm] for k, o, t_, nm in pairs}
            for k, o, t_, nm in pairs:
                if t_ > 0 and o / t_ - 1 > TOO_GOOD:
                    why = too_good_notes.get(b) or too_good_notes.get("*")
                    txt = (f"c2: ours beats the simulator's own rotation ({nm}) by {o / t_ - 1:.0%} in {k} ({o:.1f} against {t_:.1f})")
                    if why:
                        f.setdefault("notes", []).append(txt + f": {why}")
                    else:
                        f["fail"].append(txt + ": suspect until the casts explain it (raidsim/too-good-notes.json)")
        # the build without each talent, first: an ability whose casts are booked under another id (Swift Judgement under the judged
        # seal, as Judgement) is used when its removal changes the result
        rm = A.bench(entry, repo, [{"label": t, "talents": R.talents_string(trees_sim, {k: v for k, v in have.items() if k != t})} for t in have],
                     fights, 1, "raid", tag)
        ref = val(row)
        matters = {t for t in have if rm.get(t) and val(rm[t]) != ref}
        booked = "used: its casts are booked under another id (removing it changes the result)"
        # a. the rotation's spells
        seen = set()
        for part, i, sid, cond, act in lines:
            if cs.get(sid, 0) > 0 or (sid, cond is None) in seen:
                continue
            seen.add((sid, cond is None))
            nm = id_name.get(sid) or names.get(sid) or CLIENT.get(sid) or str(sid)
            # a talent's ability under an id the beta spellbook lacks is the class's (Death Mark 1325758, Reckless Swings 1329555: the
            # simulator names them, the talent data holds them); a removed spell or an item's spell is not (Lava Burst, Jom Gabbar)
            bn = re.sub(r" [(](Bear|Cat)[)]$", "", nm)   # Feral Charge (Bear): the talent Feral Charge's bear spell
            talent_ability = sid not in id_name and (nm in talent_names or bn in talent_names)
            known = sid in id_name or talent_ability or (reg_ids is not None and sid in reg_ids)
            if not known and sid in RACIALS:
                why = "racial (racials are off)"
            elif not known:
                why = None   # neither the class's spell nor a racial: Lava Burst, Frost Blast, a trinket's spell cast as a spell
                f["never_cast"].append(f"{part}[{i}] {nm} ({sid}): NOT A SPELL THE CLASS HAS (a removed spell or a wrong id)")
                f["fail"].append(f"a: {nm} ({sid}) is no spell of the class and no racial: the line can never fire ({part}[{i}])")
                continue
            elif (nm in talent_names and nm not in have) or (bn != nm and bn in talent_names and bn not in have):
                why = "talent not taken"
            elif nm in matters or bn in matters:
                why = booked
            elif any(all_cs[o].get(sid, 0) > 0 for o in bids if o != b):
                why = "cast by another build of the entry (the line serves builds that reach it)"
            elif nm.endswith(" Stance") and stance_of(entry) == nm:
                why = f"already in {nm} (the entry's starting stance; the line returns to it)"
            elif nm == "Battle Shout" and class_options(entry).get("useBattleShout"):
                why = "kept up by the class option useBattleShout"
            elif nm in book and TARGET_TYPE.search(book[nm][1]):
                why = "needs an Undead or Demon target (the bench's boss is an Elemental)"
            elif cond is not None and false_switch(cond, apl):
                why = f"switch off ({false_switch(cond, apl)})"
            elif cond is not None:
                why = "condition never held"
            else:
                why = None
            f["never_cast"].append(f"{part}[{i}] {nm} ({sid}): {why or 'NEVER CAST on an unconditional line'}")
            if why is None:
                f["fail"].append(f"a: {nm} never cast on an unconditional line ({part}[{i}])")
        own = own_debuff(cls, entry)
        if own and own in book and sum(cs.get(i, 0) for i in book[own][0]) == 0:
            f["fail"].append(f"a: the class turns the raid's {own} off for its own cast, and the rotation never casts it")
        # b. talent abilities
        kinds = unused_kinds(cls, ename, b)
        reasons = {}
        for t in sorted(have):
            if t not in book or sum(cs.get(i, 0) for i in book[t][0]) > 0:
                continue
            txt = book[t][1]
            why = booked if t in matters else None
            if not why and gate(trees, data[b]["allocation"], t):   # before unused-abilities' kind: its "wasted" can predate the build
                why = "prerequisite"
            if not why:
                why = kinds.get(t)
            if not why and FA.TRIGGERED.search(txt):
                why = "needs a parry or a block"
            if not why and (FA.DEFENSIVE.search(txt) or SHIELD.search(txt)):
                why = "situational (defensive)"
            if not why and use.get(t, UT.NONE) < UT.NONE:   # an interrupt, a threat cut, a range tool: pressed when the fight calls for it
                why = f"situational (utility: {[g for g, _ in UT.TAGS][use[t]]})"
            if not why and TARGET_TYPE.search(txt):
                why = "needs an Undead or Demon target (the bench's boss is an Elemental)"
            f["abilities"].append(f"{t}: {why or 'NEVER CAST, no reason'}")
            if why and why != "wasted":
                reasons[t] = why
            if not why or why == "wasted":
                f["fail"].append(f"b: talent ability {t} never cast" + (" (unused-abilities: wasted)" if why == "wasted" else ""))
        # summed by name over the ranks (the audit session, 2026-11-20: a name-keyed record had let a later rank's row overwrite an
        # earlier one, Lightning Bolt 0.0 for 67.1); the verdicts above read casts by id. The bench's own rows, before the Judgement alias.
        # 2026-11-20 night (the audit session): the pet's casts apart, and what the rotation never presses (procs, a seal's judgement
        # booked under its own id, items) apart from what it does: the bench's rows carry all three under the player's id
        pressed, procs, pet = {}, {}, {}
        for x in row.get("actions") or []:
            c = x.get("casts") or 0
            if not c or not x.get("spellId"):
                continue
            nm = id_name.get(x["spellId"]) or names.get(x["spellId"]) or str(x["spellId"])
            if x.get("pet"):
                pet[nm] = pet.get(nm, 0) + c
            elif (x["spellId"], x.get("tag") or 0) in rot_casts:
                pressed[nm] = pressed.get(nm, 0) + c
            else:
                procs[nm] = procs.get(nm, 0) + c
        srt = lambda d: {n: round(v, 2) for n, v in sorted(d.items(), key=lambda kv: -kv[1])}   # noqa: E731
        f["casts"], f["procs_and_triggered"], f["pet_casts"] = srt(pressed), srt(procs), srt(pet)
        f["casts_by_id"] = {str(k): round(v, 2) for k, v in sorted(raw_cs[b].items(), key=lambda kv: -kv[1]) if v}
        res["builds"][b] = f
        # c. talents worth nothing
        recorded = filler_records(cls, b, have)
        for t in sorted(have):
            if t in matters or not rm.get(t):
                continue
            g = gate(trees, data[b]["allocation"], t)
            why = ("gate: " + g.split(": ", 1)[-1][:80]) if g else ("recorded filler" if t in recorded else None)
            if not why and t in reasons:   # an ability (b) accepts: automatic, situational, a prerequisite
                why = f"ability: {reasons[t]}"
            if not why and use.get(t, UT.NONE) < UT.NONE:   # a raid utility tag (range, survival ...): a filler, not a dead point
                why = f"utility filler ({[g for g, _ in UT.TAGS][use[t]]})"   # (the audit session's ruling, 2026-11-20: Flame Throwing)
            if not why and t in RAID_BUFF_TALENT:
                why = f"the raid's {RAID_BUFF_TALENT[t]} itself (the full raid already holds it; in a real raid this build is its source)"
            f["zero_talents"].append(f"{t} {have[t]}: {why or 'WORTH NOTHING, not a gate or a recorded filler'}")
            if not why:
                f["fail"].append(f"c: {t} worth nothing and not a gate or a recorded filler")
    for b in bids:
        f = res["builds"][b]
        have = flat(data[b]["allocation"])
        # d. inert raid switches
        cs = all_cs[b]
        for s, srows in sw_rows.items():
            if OWN_TALENT.get(s, set()) & set(have):
                continue
            if any(cs.get(i, 0) > 0 for n in OWN_CAST.get(s, ()) for i in book.get(n, (set(), ""))[0]):
                continue   # the build casts the spell that supplies it (its own totem, shout, sunder, judgement)
            r = srows.get(b)
            if r and same(r.get("dps"), (base.get(b) or {}).get("dps")):
                f["inert_switches"].append(s)
                f["fail"].append(f"d: the raid's {s} changes nothing for it")
        if res["rotation_fail"]:
            f["fail"] += [f"e: {x}" for x in res["rotation_fail"]]
    res["fail"] = sorted({b for b, f in res["builds"].items() if f["fail"]})
    return res


def judge_at_home(cls_rec):
    """A build listed in several entries is judged where its page number comes from: the entry with its highest full-raid number, as
    render_modes.raid_numbers takes it (a pet build in the Lone Wolf entry holds pet talents worth nothing there). Its failures in the
    other entries become notes. `cls_rec` is {entry: record} for one class."""
    best = {}
    for e, r in cls_rec.items():
        for b, f in (r.get("builds") or {}).items():
            if f.get("dps") and (b not in best or f["dps"] > best[b][1]):
                best[b] = (e, f["dps"])
    for e, r in cls_rec.items():
        for b, f in (r.get("builds") or {}).items():
            home = best.get(b, (e,))[0]
            if home != e and f.get("fail"):
                f["notes"] = [f"its page number comes from {home}: its failures in {e} are notes"] + f["fail"] + list(f.get("notes") or [])
                f["fail"] = []
        r["fail"] = sorted({b for b, f in (r.get("builds") or {}).items() if f.get("fail")})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--entry", action="append")
    ap.add_argument("--fights", type=int, default=3000)
    ap.add_argument("--skip-switches", action="store_true")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    classes = a.classes or [c for c in R.SPECS if isinstance(R.SPECS[c], dict)]
    for cls in classes:
        done = {}
        for ename, entry in R.SPECS[cls].items():
            if not isinstance(entry, dict) or not entry.get("apl") or (a.entry and ename not in a.entry):
                continue
            res = check_entry(cls, ename, entry, repo, a.fights, switches=not a.skip_switches)
            if res is not None:
                res["date"] = datetime.date.today().isoformat()
                done[ename] = res
        # judged at home over the class's whole record (the entries this run checked, the others as last written)
        merged = {**(rec.get(cls) or {}), **done}
        judge_at_home(merged)
        for ename, res in done.items():
            res = merged[ename]
            print(f"== {cls} {ename} ({res['rotation']}): " + (f"FAIL in {', '.join(res['fail'])}" if res["fail"] else "pass"), flush=True)
            for b, f in res["builds"].items():
                print(f"   {b} {f['dps']:.2f}: " + ("; ".join(f["fail"]) if f["fail"] else "pass"), flush=True)
                for k in ("never_cast", "abilities", "zero_talents"):
                    for x in f[k]:
                        print(f"      {k}: {x}", flush=True)
        if a.write and done:
            rec[cls] = merged
            OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
