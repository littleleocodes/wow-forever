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


def fresh_conversion(cls, path, repo):
    """A converted official rotation against a fresh conversion of upstream's file (None when its source cannot be found)."""
    import siml_upstream_race as SU
    name = path.name.replace(".apl.json", "")
    rot = None
    for src in sorted(repo.glob(f"ui/specs/{cls}/*/apls/{name}.apl.siml")):
        rot = SU.siml2json(repo, src)
        break
    if rot is None:
        for src in sorted(repo.glob(f"ui/specs/{cls}/*/apls/{name}.apl.json")):
            rot = json.load(open(src, encoding="utf-8"))
            break
    if rot is None:
        for src in sorted(repo.glob(f"ui/specs/{cls}/*/builds/{name}.build.json")):
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
    """The rotations' and the gear's content, the builds' talents and the simulator's switches: a record is current while it holds."""
    h = hashlib.sha1()
    for where in ("raid", "dummy"):
        h.update(pathlib.Path(R.apl_path(entry, repo, where)).read_bytes())
    gp = pathlib.Path(R.sim_path(entry["gear"]))
    gp = gp if gp.is_absolute() else repo / entry["gear"]
    h.update(gp.read_bytes() if gp.exists() else entry["gear"].encode())
    h.update(json.dumps(sorted(builds.items())).encode())
    h.update(json.dumps(R.sim_switches(repo), sort_keys=True).encode())
    return h.hexdigest()[:16]


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
            d = fresh_conversion(cls, p, repo)
            if d:
                conv += [f"{p.name}: {x}" for x in d]
    res["rotation_fail"] = rot_fail + [f"differs from a fresh conversion of upstream's file: {x}" for x in conv]
    all_cs = {}
    for b in bids:
        c = casts_by_id(base.get(b) or {}, names)
        for src, al in RR.CAST_ALIASES.items():   # Judgement's casts are booked under the judged seal's ids (as the pages count them)
            c[src] = c.get(src, 0) + sum(c.get(x, 0) for x in al)
        all_cs[b] = c
    for b in bids:
        row = base.get(b) or {}
        cs = all_cs[b]
        have = flat(data[b]["allocation"])
        f = {"dps": round(row.get("dps") or 0, 2), "never_cast": [], "abilities": [], "zero_talents": [], "inert_switches": [], "fail": []}
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
            if sid not in id_name and sid in RACIALS:
                why = "racial (racials are off)"
            elif sid not in id_name:
                why = None   # neither the class's spell nor a racial: Lava Burst, Frost Blast, a trinket's spell cast as a spell
                f["never_cast"].append(f"{part}[{i}] {nm} ({sid}): NOT A SPELL THE CLASS HAS (a removed spell or a wrong id)")
                f["fail"].append(f"a: {nm} ({sid}) is no spell of the class and no racial: the line can never fire ({part}[{i}])")
                continue
            elif nm in talent_names and nm not in have:
                why = "talent not taken"
            elif nm in matters:
                why = booked
            elif any(all_cs[o].get(sid, 0) > 0 for o in bids if o != b):
                why = "cast by another build of the entry (the line serves builds that reach it)"
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
            why = booked if t in matters else kinds.get(t)
            if not why and gate(trees, data[b]["allocation"], t):
                why = "prerequisite"
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
        f["casts"] = {(id_name.get(k) or names.get(k) or str(k)): round(v, 2) for k, v in sorted(cs.items(), key=lambda kv: -kv[1]) if v}
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
        for ename, entry in R.SPECS[cls].items():
            if not isinstance(entry, dict) or not entry.get("apl") or (a.entry and ename not in a.entry):
                continue
            res = check_entry(cls, ename, entry, repo, a.fights, switches=not a.skip_switches)
            if res is None:
                continue
            res["date"] = datetime.date.today().isoformat()
            print(f"== {cls} {ename} ({res['rotation']}): " + (f"FAIL in {', '.join(res['fail'])}" if res["fail"] else "pass"), flush=True)
            for b, f in res["builds"].items():
                print(f"   {b} {f['dps']:.2f}: " + ("; ".join(f["fail"]) if f["fail"] else "pass"), flush=True)
                for k in ("never_cast", "abilities", "zero_talents"):
                    for x in f[k]:
                        print(f"      {k}: {x}", flush=True)
            if a.write:
                rec.setdefault(cls, {})[ename] = res
                OUT.write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
