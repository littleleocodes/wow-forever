"""The leveling play check (2026-11-20; the user's decision on the audit session's recommendations after D11: the raid play check's
leveling counterpart, before the leveling pages are pushed; its rules drafted with the audit session, La-Lf by this session, Lg-Ll by
the audit's). For every leveling page pick (level_guides.pick: its build, order and tuned rotation), on level_guides' measured record of
it (standard gear, single pulls, the guide's stage levels; `level_guides.py <class> --measure`, current by its fingerprint):

 La  a spell a stage names (bold in its text) that the lab presses 0 times at every measured level of the stage (level_guides --check's
     warning): FAIL.
 Lb  a spell a stage presses before its trainer level or before the order takes its talent (level_guides --check's error): FAIL.
 Lc  a talent worth exactly nothing (time per kill the same to 0.01 s, seed 1) at 60 and at every level of 20-60 by tens the order holds
     it: FAIL unless a prerequisite (another held talent requires it by name: gate_kind.py), a leveling utility tag (utility_tags.usefulness
     with avoidance counted: the character is hit) or a recorded filler (fightlab/filler/<class>-<slug>.json). A TIER POINT (one of the
     points a deeper talent's tier needs) is not excused by being a gate (2026-11-21, the audit session): any legal talent of the rows
     below can hold it, so it passes only when the filler pass's record on the build as it stands says it tried every legal home and
     found none more useful (fl_filler_pass.py step 5b: "no better home", "no legal home", "kept: utility"), else FAIL. Measured at 60
     first; only talents worth nothing there are measured lower.
 Ld  a tuned rule (fightlab/rotations/<class>-<rotation>.json `veto`) that takes off a spell a stage names or a required signature spell
     (signature_spells.json, leveling): FAIL, naming the rule.
 Le  the lab presses a spell at least 0.5 times a kill in a stage that never names it (level_guides --check's warning): FAIL.
 Lf  a key bound to a spell the build cannot have at that level (level_guides --check's error): FAIL.
 Lg  never tried: a damaging, absorbing or resource ability the character has (the class's spellbook by trainer level, the build's talent
     abilities by its order) that the lab presses 0 times at every measured level from the one it arrives and no rule vetoes: FAIL "never
     tried" unless fightlab/never-tried.json records a verdict for the class and rotation ("forced into the priority on <date>: slower by
     X%", written by fightlab/force_run.py; a "LEAD" verdict or a spell the module cannot cast stays a FAIL). Area spells are left to the
     AoE variants (tables.AOE_SPELLS), unless a held talent makes one a single-target tool (AOE_SINGLE, 2026-11-21: Winter's Chill for
     Cone of Cold), which a rule's veto does not excuse either; the class's pet tab is left to the pet. A verdict of a forced run with a
     talent added or a condition ("Cone of Cold (with Winter's Chill 5) at 5+ Winter's Chill") counts for the spell. A never-pressed
     talent ability that is a tier point is Lc's (its homes), whatever its forced verdict.
 Lh  a jump: time per kill rising more than 5% from one measured level to the next (levels at 10 and up): FAIL until
     fightlab/play-check-notes.json explains it or the order is repaired.
 Li  survival and idle: more than 2 deaths per 100 kills, or more than 40% of the time per kill out of the fight (drinking, eating,
     waiting), at a measured level: FAIL for a look (the audit session's thresholds, to tune on the spread).
 Lj  the pet: at a measured level where the build keeps one (pet sources in the damage shares), the pet under 5% of the damage, or dead in
     more than 10 of 100 pulls: FAIL.
 Lk  what is kept up: the module's standing effects (the lab's armor_spell field: armor, aura, stance, aspect, imbue, form, poisons) at each
     measured level from the class's first one (FIRST_STANDING), and Hunter's Mark cast where the build holds Expose Prey: FAIL.
 Ll  parsing: fightlab/module_lint.py's rows for the class (a name the data lacks, a tooltip number that parses to 0): FAIL.
The record (fightlab/play-check.json) carries each pick's presses per kill by measured level (its cast list, for the audit's reading) and a
fingerprint of what the numbers depend on (the class module, engine, tables, run.py, the rules file, the class's talent and spell data,
the data build): a page row from another fingerprint is refused.

    python _reference/data/fightlab/play_check.py [classes] [--fights 1500] [--jobs 8] [--skip-removal] [--write]
"""
import argparse
import datetime
import hashlib
import json
import multiprocessing
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent
ROOT = DATA.parents[1]
sys.path[:0] = [str(HERE), str(DATA)]
import run as FR  # noqa: E402
import level_guides as LG  # noqa: E402
import signature as SG  # noqa: E402
import utility_tags as UT  # noqa: E402
import validate_builds as VB  # noqa: E402
import spec_modes as SM  # noqa: E402
import gate_kind as GK  # noqa: E402

OUT = HERE / "play-check.json"
VERDICTS = HERE / "never-tried.json"
NOTES = HERE / "play-check-notes.json"
FORCED = HERE / "forced-leads.json"   # forced_leads.py (2026-11-22)
DAMAGE = re.compile(r"\d+ (?:to \d+ )?(?:\w+ ){0,2}damage|\babsorb|restores? [^.]*\b(?:mana|rage|energy)\b|\bgains? \d+ (?:rage|energy|mana)",
                    re.I)
CHECK_LEVELS = [20, 30, 40, 50, 60]
# module_lint rows that read a retired mechanism behind a switch that is off (not a misread): Ll records them as notes
LINT_RETIRED = {"mage": {"MB_MISSILE": "the 70425 wording of Missile Barrage's missile procs, hotfixed out (mage.MB_MISSILE_PROCS False)"},
                "warlock": {"WRACK_DEBUFF": "Wrack's wording before 2026-11-10 (a debuff on the target); Wrack now speeds up the dots, read by "
                                            "WRACK_SPEED",
                            "TICK": "an unused pattern: the module reads periodic damage through TICK_FOR"}}
# Ll rows that name a spell no leveling module casts as parsed (2026-11-21, the audit session: "act on each row: fix the parser where a
# module casts the spell, else note that none does"): the reason, by class and spell
HEAL_BOOK = "a healer's spell: no leveling module casts it, and the healer lab reads it from its own book (heallab/engine.load_book)"
PET_ONLY = "a pet ability the lab's pet never uses (the cat presses Claw, Bite and Growl)"
DEMON_ONLY = "a demon's spell the lab never casts (the Voidwalker presses Torment; the Imp's Firebolt is its swing)"
LINT_UNCAST = {
    "druid": {"Lacerate": "no leveling module casts it: the druid plays Maul and Swipe in Bear Form at 10-19 and Cat Form from 20",
              "Wild Growth": HEAL_BOOK},
    "hunter": {"Savage Rend": PET_ONLY, "Scorpid Poison": PET_ONLY, "Tendon Rip": PET_ONLY, "Swipe": PET_ONLY,
               "Disengage": "no leveling module casts it: a threat drop with no damage", "Distracting Shot": "no leveling module casts it: a "
               "taunt with no damage"},
    "paladin": {"Blessing of Sacrifice": "party only: it targets another member (a recorded Lg verdict)",
                "Holy Shield": "the paladin module reads Holy Shield's block damage itself (paladin.py), not from this parse",
                "Holy Wrath": "Undead and Demons only (a recorded Lg verdict), and the lab's mobs are neither",
                "Light's Vigil": HEAL_BOOK, "Seal of Justice": "no leveling module casts it: a stun seal the tunes never chose",
                "Seal of Righteousness": "rank 1's client tooltip has no judgement and no spell-power coefficient; the lab plays it as "
                                         "written at levels 1-9, ranks 2-8 parse in full",
                "Lay on Hands": "rank 1's client tooltip has no cost or amount; no leveling module casts it (its forced run decides)"},
    "priest": {"Feedback": "a racial the lab plays without", "Shadowguard": "a racial the lab plays without",
               "Touch of Weakness": "a racial the lab plays without", "Prayer of Mending": HEAL_BOOK,
               "Mana Burn": "its damage is half the mana it drains, and the lab's mobs have no mana (a recorded Lg verdict)"},
    "warlock": {"Bane of Doom": "its hit lands a minute after the cast, after every leveling fight has ended (a recorded Lg verdict)",
                "Fire Shield": DEMON_ONLY, "Lash of Pain": DEMON_ONLY, "Soothing Kiss": DEMON_ONLY,
                "Inferno": "a one-hour cooldown that summons an Infernal the lab does not model (a recorded Lg verdict)",
                "Torment": "rank 1's client tooltip has no number; the lab reads Torment's threat from the client's table "
                           "(warlock.TORMENT_TABLE)"},
}
JUMP, DEATHS, IDLE, PET_SHARE, PET_DEATHS, LE_MIN = 0.05, 2.0, 0.40, 0.05, 10.0, 0.5
# Lh (2026-11-21, the audit session's ruling on the first run): a rise of at most JUMP_MAX across more than JUMP_NEAR levels passes as
# ordinary scaling against the mob, its printed cause the note; a rise over JUMP within JUMP_NEAR levels, any rise over JUMP_MAX, and a
# drop over DROP within JUMP_NEAR levels (too good needs explaining as well) need a person's note in play-check-notes.json
JUMP_MAX, JUMP_NEAR, DROP = 0.12, 3, 0.15
# Lc for the healer and tank picks that level as their raid build (raid_path_leveling.py; the user's decision of 2026-09-30)
# a key whose job is a pull of several mobs (the Shift bar's pack keys): the single-target veto does not apply to it; a mention that
# stands between fights (Regrowth's heal after the fight) is no press in one (2026-11-21, the lane session's reading, put to the audit)
PACK_KEY = re.compile(r"\bpacks?\b|two or more|several mobs|a group|the group", re.I)
BETWEEN = re.compile(r"between fights|after the fight|after a fight", re.I)
NOT_IN_LIST = re.compile(r"not in the list", re.I)
RAID_PATH_VERDICT = "the raid build's point: this page levels as its raid build (the user's decision of 2026-09-30)"
# Ld reads negation as page_lint does (2026-11-21, the audit session): a note that says a vetoed spell is not cast passes; a press
# line, a key or a positive mention fails
NOT_CAST = re.compile(r"never (?:cast|casts|press|presses|uses|used)|\bnot cast|n't cast|(?:is|are) not part of|stays? off|off your bars?|"
                      r"leaves? (?:it|them) out|(?:tuned|the) (?:rotation|rules|list)(?:'s)?(?: \w+)? never|"
                      r"leave it off|switch(?:es)? it off|is off\b|no longer|without it|measured (?:slower|faster) without", re.I)


def code_fingerprint(cls, rot):
    files = [HERE / "engine.py", HERE / "tables.py", HERE / "run.py", FR.rotation_file(cls, rot), DATA / "forever-talents" / f"{cls}.json",
             DATA / "forever-spells" / f"{cls}.json", DATA / "signature_spells.json"]
    mod = (FR.MODULES.get(cls) or (None,))[0] if isinstance(FR.MODULES, dict) else None
    if mod:
        files.append(HERE / f"{mod}.py")
    h = hashlib.sha1()
    for f in files:
        f = pathlib.Path(f)
        h.update(f.name.encode("utf-8"))
        h.update(f.read_bytes() if f.exists() else b"-")
    import data_build as DB
    h.update(str(DB.BUILD).encode("utf-8"))
    return h.hexdigest()[:16]


# An area spell Lg does not leave to the AoE variants (2026-11-21, the audit session): a held talent makes it a single-target tool, so a
# single pull can pay for it. Winter's Chill: each Frostbolt adds a stack the next Cone of Cold spends (in a raid, Frostbolt to five
# stacks and Cone of Cold was a quarter of Frost's damage, worth 21%; a leveling mob runs into the cone's reach). The others found by
# their tooltips: a bonus on the target or the closest enemy, a second cast on the same target, a free cast, no cooldown.
AOE_SINGLE = {
    "mage": {"Cone of Cold": {"Winter's Chill"}},
    "shaman": {"Chain Lightning": {"Stormstrike", "Lightning Overload", "Lightning Mastery"}},
    "warrior": {"Whirlwind": {"Improved Whirlwind"}},
    "priest": {"Holy Nova": {"Searing Light"}},
    "paladin": {"Consecration": {"Consecrated Ground"}},
}


def inputs_fingerprint(cls, spec):
    """What a pick's Lc and Lg verdicts read besides the lab (2026-11-21, the audit session: the four filler records whose written pass
    was dropped and restored that night): the spec's filler records, the forced-run verdicts, the notes, the gate and utility rules."""
    import zero_talents as ZT   # the record files by the names fl_filler_pass.py writes (2026-11-21)
    files = ZT.filler_paths(cls, spec) + ZT.filler_paths(cls, spec, dry=True) + [VERDICTS, NOTES, FORCED, DATA / "gate_kind.py", DATA / "utility_tags.py"]
    h = hashlib.sha1()
    for f in files:
        h.update(f.name.encode("utf-8"))
        h.update(f.read_bytes() if f.exists() else b"-")
    return h.hexdigest()[:16]


def book_levels(cls):
    """{spell: (trainer level of its first rank, the top rank's tooltip)} of the class's spellbook, the pet tab left out."""
    out = {}
    for tab in json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        if str(tab.get("name", "")).lower().startswith("pet") or str(tab.get("name", "")).lower() == "demons":   # the pet's (2026-11-21:
            continue                                                                                          # the warlock's tab)
        for sp in tab.get("spells", []):
            rk = [r for r in sp.get("ranks", []) if r.get("id")]
            if not rk:
                continue
            lv = min(int(r.get("level") or 1) for r in rk)
            out[sp["name"]] = (lv, str(rk[-1].get("text", "")))
    return out


def aoe_names():
    try:
        import tables as T
        return set(getattr(T, "AOE_SPELLS", {}) or {})
    except Exception:   # noqa: BLE001
        return set()


def _init():
    FR.apply_gear("greens")


def _ttk(job):
    cls, rot, alloc, level, fights = job
    try:
        return FR.simulate(cls, alloc, level, rot, fights, 1, 0)["time_per_kill"]
    except Exception as e:   # noqa: BLE001
        return f"error {type(e).__name__}: {e}"


def held_at(b, level):
    return {n for n, r in FR.allocation_at(b, level).items() if r} if level < 60 else {n for v in b["allocation"].values() for n, r in v if r}


def zero_talents(cls, rot, b, pool, fights):
    """Lc: {talent: levels} of the talents whose removal leaves time per kill the same to 0.01 s at 60 and at every level of 20-60 by
    tens the order holds them."""
    a60 = FR.allocation_at(b, 60)
    names = [n for n, r in a60.items() if r]
    jobs = [(cls, rot, a60, 60, fights)] + [(cls, rot, {k: v for k, v in a60.items() if k != n}, 60, fights) for n in names]
    res = pool.map(_ttk, jobs, chunksize=1)
    if isinstance(res[0], str):
        return {"_error": res[0]}
    zero = [n for n, r in zip(names, res[1:]) if not isinstance(r, str) and abs(r - res[0]) < 0.005]
    out = {}
    for n in zero:
        lv = [L for L in CHECK_LEVELS[:-1] if n in held_at(b, L)]
        if not lv:
            out[n] = [60]
            continue
        jl = []
        for L in lv:
            aL = FR.allocation_at(b, L)
            jl += [(cls, rot, aL, L, fights), (cls, rot, {k: v for k, v in aL.items() if k != n}, L, fights)]
        rl = pool.map(_ttk, jl, chunksize=1)
        if all(not isinstance(rl[2 * i], str) and abs(rl[2 * i] - rl[2 * i + 1]) < 0.005 for i in range(len(lv))):
            out[n] = lv + [60]
    return out


def pet_names(cls):
    """The class's pet tab (the hunter's Pets, the warlock's Demons): their casts are the pet's, not the player's presses (2026-11-21,
    the audit session's B16 on the leveling side: Claw, Bite, Growl and Torment had stood in the player's list)."""
    out = set()
    for tab in json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        if str(tab.get("name", "")).lower().startswith("pet") or str(tab.get("name", "")).lower() == "demons":
            out |= {sp["name"] for sp in tab.get("spells", [])}
    return out


def said_not_cast(text, m):
    """Whether the bold name at match m stands in a passage that says it is not cast: page_lint's negation (the words before and after
    it, the sentence it stands in), or a not-cast phrase in its sentence or the note's next sentence."""
    import page_lint as PL
    low = text.lower()
    if any(k in low[max(0, m.start() - 40):m.start()] for k in PL.NEGATE):
        return True
    if any(k in low[m.end():m.end() + 45] for k in PL.NEGATE_AFTER):
        return True
    s0 = max(text.rfind(". ", 0, m.start()), text.rfind("\n", 0, m.start())) + 1
    ends = [x for x in (text.find(". ", m.end()), text.find("\n", m.end())) if x >= 0]
    s1 = min(ends) if ends else len(text)
    nxt = text.find(". ", s1 + 1)
    sent = text[s0:(nxt if nxt > 0 else len(text))]
    return bool(NOT_CAST.search(sent) or BETWEEN.search(text[s0:s1]) or PACK_KEY.search(text[s0:s1]))


def ld_mentions(g, sp):
    """Where a guide presents a vetoed spell as pressed: a press line, a key, or a mention not said to be off (stage changes, ifs, notes)."""
    out = []
    pat = re.compile(r"\*\*" + re.escape(sp) + r"\*\*")
    for s in LG.stages(g):
        for i, t in enumerate(s.get("press") or []):
            if pat.search(t):
                out.append(f"stage {s['from']} press")
        for k in ("change", "if_hurt"):
            t = s.get(k) or ""
            if any(not said_not_cast(t, m) for m in pat.finditer(t)):
                out.append(f"stage {s['from']} {k}")
        for i, t in enumerate(s.get("notes") or []):
            if any(not said_not_cast(t, m) for m in pat.finditer(t)):
                out.append(f"stage {s['from']} note {i}")
    for k in LG.key_slots(g["keys"]) if g.get("keys") else []:
        role = str(k.get("role") or "")
        if PACK_KEY.search(role) or NOT_IN_LIST.search(role):   # a pack key, or a key for a bad pull whose role says the list never
            continue                                              # presses it (the audit session's ruling, 2026-11-21)
        if any(bd.get("spell") == sp for bd in k.get("binds", [])):
            out.append(f"key {k['key']}")
    return sorted(set(out))


def book_ranks(cls):
    """{spell: sorted trainer levels of its ranks}."""
    out = {}
    for tab in json.load(open(DATA / "forever-spells" / f"{cls}.json", encoding="utf-8")).get("tabs", []):
        for sp in tab.get("spells", []):
            lv = sorted(int(r.get("level") or 1) for r in sp.get("ranks", []) if r.get("id"))
            if lv:
                out[sp["name"]] = lv
    return out


def what_changed(cls, bb, a, c, casts_c):
    """What differs between two measured levels (the audit session: a jump from a talent order or a missing rank is the one to catch):
    the build's points, the ranks of the spells pressed at the later level, the gear's main stats and the mob."""
    out = []
    A, C = FR.allocation_at(bb, a), FR.allocation_at(bb, c)
    pts = [f"{n} {A.get(n, 0)}->{r}" for n, r in sorted(C.items()) if r and r != A.get(n, 0)]
    out.append("points: " + (", ".join(pts) if pts else "none"))
    br = book_ranks(cls)
    rk = [f"{sp} rank {sum(1 for x in br[sp] if x <= a)}->{sum(1 for x in br[sp] if x <= c)}" for sp in sorted(casts_c or {})
          if sp in br and sum(1 for x in br[sp] if x <= a) != sum(1 for x in br[sp] if x <= c)]
    out.append("ranks: " + (", ".join(rk) if rk else "none new"))
    try:
        import tables as T
        ga, gc = T.gear_stats(a, cls=cls), T.gear_stats(c, cls=cls)
        main = lambda g: sum(g.get(s, 0) for s in ("intellect", "stamina", "agility", "strength", "spirit"))   # noqa: E731
        out.append(f"gear main stats {main(ga):.0f}->{main(gc):.0f}")
    except Exception:   # noqa: BLE001
        pass
    try:
        import tables as T   # the mob the lab plays (2026-11-21: mob_stats.json's raw by_level medians had printed Arms 35-40 at +88%
        ha, hc = T.mob_health(a), T.mob_health(c)   # health where the lab plays +41%)
        out.append(f"mob health {ha:.0f}->{hc:.0f} ({hc / ha - 1:+.0%}), swing {T.mob_melee_damage(a):.0f}->{T.mob_melee_damage(c):.0f}, "
                   f"armor {T.mob_armor(a):.0f}->{T.mob_armor(c):.0f}")
    except Exception:   # noqa: BLE001
        pass
    return "; ".join(out)


# Lk: the level from which the class keeps a standing effect up (its first armor, aura, stance, aspect, imbue, form or poison)
FIRST_STANDING = {"mage": 1, "warrior": 1, "paladin": 1, "hunter": 10, "rogue": 20, "shaman": 1, "druid": 10, "priest": 12, "warlock": 1}


def is_gate(cls, b, talent):
    st = {t: {n: r for n, r in v if r and n != talent} for t, v in b["allocation"].items()}
    errors = []
    VB.check_state(VB.load_forever()[cls], st, "x", errors)
    return errors[0] if errors else None


def filler_homes(cls, spec, order):
    """{talent: (verdict, why)} from the leveling filler pass's record made on the build as it stands (its final_order is the order;
    the written record or a dry run's): the dead points whose every legal home it tried (`no_better_home`: steps 3-4's zero points, step
    5b's gates that do nothing) and step 5b's verdict on each gate (`gates_checked`). 2026-11-21, the audit session's gate rule."""
    out = {}
    import zero_talents as ZT   # the record files, by the names fl_filler_pass.py writes (2026-11-21: hybrids were never found)
    for p in ZT.filler_paths(cls, spec) + ZT.filler_paths(cls, spec, dry=True):
        if not p.exists():
            continue
        try:
            x = json.load(open(p, encoding="utf-8"))
        except ValueError:
            continue
        if x.get("final_order") != order:
            continue
        for t, e in (x.get("gates_checked") or {}).items():
            out.setdefault(t, (e.get("verdict") or "", e.get("does_nothing") or ""))
        for t, e in (x.get("no_better_home") or {}).items():
            out[t] = ("no better home", f"{e.get('why')}; {e.get('homes')} legal homes tried ({x.get('date')})")
    return out


def filler_recorded(cls, spec):
    import zero_talents as ZT
    p = next((x for x in ZT.filler_paths(cls, spec) if x.exists()), ZT.filler_paths(cls, spec)[0])
    if not p.exists():
        return set()
    try:
        x = json.load(open(p, encoding="utf-8"))
    except ValueError:
        return set()
    out = set()
    for k in ("zero", "zero_points", "kept", "free", "gates"):
        v = x.get(k)
        if isinstance(v, dict):
            out |= set(v)
        elif isinstance(v, list):
            out |= {(e[0] if isinstance(e, (list, tuple)) else e.get("talent") if isinstance(e, dict) else e) for e in v}
    return {n for n in out if isinstance(n, str)}


def check_class(cls, pool, fights, removal):
    data = LG.load(cls)
    if not data:
        return {}
    rows = LG.check(cls)
    verdicts = (json.load(open(VERDICTS, encoding="utf-8")).get(cls) or {}) if VERDICTS.exists() else {}
    notes = (json.load(open(NOTES, encoding="utf-8")).get(cls) or {}) if NOTES.exists() else {}
    # the forced-run leads beside the tuned rules (forced_leads.py, 2026-11-22): {rotation: {spell: {"verdict", "text", ...}}}
    forced = (json.load(open(FORCED, encoding="utf-8")).get(cls) or {}) if FORCED.exists() else {}
    use = UT.usefulness(cls, True)   # leveling: the character is hit, avoidance counts (the tank order)
    book = book_levels(cls)
    aoe = aoe_names()
    try:
        import module_lint as ML
        bad, zero_parse, fields, patterns = ML.lint(cls)
        lint_rows = [f"unknown name {x}" for x in (bad or [])] + [f"parses to 0: {x}" for x in (zero_parse or [])] \
            + [str(x) for x in (fields or [])] + [str(x) for x in (patterns or [])]
    except Exception as e:   # noqa: BLE001
        lint_rows = [f"module_lint failed: {type(e).__name__}: {e}"]
    out = {}
    for g in LG.own_guides(data):   # a guide by reference (same_as, 2026-11-21) is the other spec's and is checked there
        spec = g["spec"]
        b, order, prov, rot = LG.pick(cls, spec)
        if not b:
            continue
        bb = dict(b, order=order)
        f = {"build": b["id"], "rotation": rot, "provisional_order": prov, "fingerprint": code_fingerprint(cls, rot),
             "inputs_fingerprint": inputs_fingerprint(cls, spec),
             "guide_fingerprint": LG.fingerprint(cls, b, order, rot), "fail": [], "notes": [], "levels": {}}
        out[spec] = f
        m = LG.measured(cls, spec, b, order, rot)
        if not m:
            f["fail"].append("the guide's fight-lab numbers are not current: run level_guides.py <class> --measure first")
            continue
        lv = {int(L): r for L, r in m["levels"].items() if isinstance(r, dict) and r.get("seconds")}
        pets = pet_names(cls)
        f["levels"] = {str(L): {"seconds": r.get("seconds"), "deaths_per_100": r.get("deaths_per_100"), "idle_share": r.get("idle_share"),
                                "casts": {k: v for k, v in (r.get("casts") or {}).items() if k not in pets},
                                "pet_casts": {k: v for k, v in (r.get("casts") or {}).items() if k in pets} or None,
                                "shares": r.get("shares")} for L, r in sorted(lv.items())}
        # La, Lb, Le, Lf: level_guides' own check of the guide against the measured record
        for level, txt in rows:
            if not (txt.startswith(f"{spec}:") or txt.startswith(f"{spec} ")):
                continue
            if level == "error":
                f["fail"].append(f"Lb/Lf: {txt}")
            elif "never casts it there" in txt:
                f["fail"].append(f"La: {txt}")
            elif "never names it" in txt:
                n = re.search(r"presses .+? ([0-9.]+) times a kill", txt)
                (f["fail"] if n and float(n.group(1)) >= LE_MIN else f["notes"]).append(f"Le: {txt}")
            elif "no fight-lab numbers" in txt:
                f["fail"].append(f"La: {txt}")
            else:
                f["notes"].append(txt)
        # Ld: a rule that takes off a named or signature spell
        named = {n for s in LG.stages(g) for n in LG.bold_names(s)}
        rl = SG.rule(cls, spec, "leveling") or {}
        try:
            veto = json.load(open(FR.rotation_file(cls, rot), encoding="utf-8")).get("veto") or {}
        except (OSError, ValueError):
            veto = {}
        for sp, v in sorted(veto.items()):
            if not v.get("off"):
                continue
            if sp in rl.get("required", []):
                f["fail"].append(f"Ld: the rules file's veto takes {sp} off ({json.dumps(v)}) and it is a required signature spell")
                continue
            where = ld_mentions(g, sp)
            if where:
                f["fail"].append(f"Ld: the rules file's veto takes {sp} off ({json.dumps(v)}) and the guide presents it as pressed: "
                                 + ", ".join(where))
            elif sp in named:
                f["notes"].append(f"Ld: the rules file's veto takes {sp} off; the guide names it only to say it is not cast")
        # Lh: a jump between measured levels
        ls = sorted(L for L in lv if L >= 10)
        for a, c in zip(ls, ls[1:]):
            s0, s1 = lv[a]["seconds"], lv[c]["seconds"]
            if not s0:
                continue
            r = s1 / s0 - 1
            near = c - a <= JUMP_NEAR
            need = r > JUMP_MAX or (r > JUMP and near) or (r < -DROP and near)
            if not need and r <= JUMP:
                continue
            why = ((notes.get(spec) or {}).get("jump") or {}).get(f"{a}-{c}")
            txt = f"Lh: {s0} s a kill at {a}, {s1} at {c} ({r:+.0%})"
            cause = what_changed(cls, bb, a, c, lv[c].get("casts"))
            if need and not why:
                f["fail"].append(f"{txt} [{cause}]")
            else:
                f["notes"].append(txt + (f": {why}" if why else ": ordinary scaling over four or more levels") + f" [{cause}]")
        # Lk: what is kept up (the module's standing effects, the lab's armor_spell field), and Hunter's Mark where a talent keys on it
        if not any("standing" in r for r in lv.values()):
            f["notes"].append("Lk: the measured record predates the standing-effects field (level_guides --measure again)")
        else:
            for L, r in sorted(lv.items()):
                if L >= FIRST_STANDING.get(cls, 1) and not r.get("standing"):
                    f["fail"].append(f"Lk: no standing effect kept up at {L} (the class trains one from {FIRST_STANDING.get(cls, 1)})")
            f["standing"] = {str(L): r.get("standing") for L, r in sorted(lv.items())}
        if cls == "hunter":
            for L, r in sorted(lv.items()):
                if L >= 10 and "Expose Prey" in held_at(bb, L) and not (r.get("casts") or {}).get("Hunter's Mark"):
                    f["fail"].append(f"Lk: the build holds Expose Prey at {L}, which keys on Hunter's Mark, and the lab never casts the mark there")
        # Li: survival and idle
        for L, r in sorted(lv.items()):
            if L < 10:
                continue
            if (r.get("deaths_per_100") or 0) > DEATHS:
                f["fail"].append(f"Li: {r['deaths_per_100']} deaths per 100 kills at {L}")
            if r.get("idle_share") is not None and r["idle_share"] > IDLE:
                f["fail"].append(f"Li: {r['idle_share']:.0%} of the time out of the fight at {L}")
        # Lj: the pet
        for L, r in sorted(lv.items()):
            ps = set(r.get("pet_sources") or [])
            if not ps or L < 10:
                continue
            share = sum(v for k, v in (r.get("shares") or {}).items() if k in ps)
            if share < PET_SHARE:
                f["fail"].append(f"Lj: the pet deals {share:.0%} of the damage at {L}")
            if (r.get("pet_deaths_per_100") or 0) > PET_DEATHS:
                f["fail"].append(f"Lj: the pet dies in {r['pet_deaths_per_100']} of 100 pulls at {L}")
        if "idle_share" not in next(iter(lv.values()), {}):
            f["notes"].append("Li/Lj: the measured record predates the idle and pet fields (level_guides --measure again)")
        # Lg: never tried
        pressed = {sp for r in lv.values() for sp, n in (r.get("casts") or {}).items() if n}
        tal_abil = {t for t in held_at(bb, 60) if t in book}
        ver = (verdicts.get(rot) or {})
        for sp, (lv0, tip) in sorted(book.items()):
            arrive = SG.learn_level(cls, sp, bb) if sp in SG.talent_names(cls) else lv0
            if arrive is None or sp in pressed or not DAMAGE.search(tip):
                continue
            tools = (AOE_SINGLE.get(cls) or {}).get(sp, set())
            if sp in aoe:   # left to the AoE variants, unless a held talent makes it a single-target tool (from the first measured
                t_from = min((L for L in lv if tools & held_at(bb, L)), default=None)   # level it is held); a rule's veto,
                if t_from is None:                                                       # tuned on the module's own lines,
                    continue                                                             # then does not excuse it either
                arrive = max(arrive, t_from)
            elif sp in veto:
                continue
            if sp in SG.talent_names(cls) and sp not in tal_abil:
                continue
            if not any(L >= arrive for L in lv):
                continue
            # force_run.py's verdicts: the spell's own, and those of runs with a talent added or a condition ("Cone of Cold (with
            # Winter's Chill 5) at 5+ Winter's Chill")
            vs = [x for k, x in ver.items() if k == sp or k.startswith((sp + " (", sp + " at "))]
            open_ = [x for x in vs if x.startswith(("LEAD", "never cast when forced"))]
            why = " (a single-target tool with " + ", ".join(sorted(tools & held_at(bb, 60))) + ")" if sp in aoe else ""
            lead_note = ((notes.get(spec) or {}).get("lead") or {}).get(sp)   # a lead the audit session put on the optimality pass's list
            if vs and not open_:   # tried and slower
                f["notes"].append(f"Lg: {sp}{why} never pressed: " + " | ".join(vs))
            elif vs and lead_note and all(x.startswith("LEAD") for x in open_):   # (2026-11-22: under 1%, a note, not a fail)
                f["notes"].append(f"Lg: {sp}{why} never pressed; forced: " + " | ".join(open_) + f": {lead_note}")
            elif vs and all(x.startswith("LEAD") for x in open_) and ((forced.get(rot) or {}).get(sp) or {}).get("verdict") == "agrees":
                # (2026-11-22, the audit session's ruling: the tune compared the lead as a rules knob and left it off, and an A/B on the
                # installed rules agrees: not 0.5% faster on both seeds. A "missed" lead stays a fail until its window is installed)
                f["notes"].append(f"Lg: {sp}{why} never pressed; forced: " + " | ".join(open_) + "; " + forced[rot][sp]["text"])
            elif vs:   # faster when forced (a lead for the rotation tune), or the module could not cast it: still open
                f["fail"].append(f"Lg: {sp}{why} (from level {arrive}) is never pressed; forced: " + " | ".join(open_))
            else:
                f["fail"].append(f"Lg: {sp}{why} (from level {arrive}) is never pressed and no verdict says it was tried"
                                 + (" (a rule vetoes it on the module's own lines)" if sp in veto else ""))
        # Ll: parsing (a retired mechanism behind an off switch is a note, with its reason)
        for x in lint_rows:
            why = next((w for k, w in (LINT_RETIRED.get(cls) or {}).items() if f"`{k}`" in x), None) \
                or next((w for k, w in (LINT_UNCAST.get(cls) or {}).items() if f"**{k}**" in x), None)
            (f["notes"] if why else f["fail"]).append(f"Ll: {x}" + (f" ({why})" if why else ""))

        # Lc: talents worth nothing at every level held
        if removal:
            zt = zero_talents(cls, rot, bb, pool, fights)
            if "_error" in zt:
                f["fail"].append(f"Lc: the removal runs failed: {zt['_error']}")
            else:
                rec = filler_recorded(cls, spec)
                raid_path = any("raid_path_leveling" in n for n in b.get("notes", []))
                homes = filler_homes(cls, spec, order)
                trees = VB.load_forever()[cls]
                for t, levels in sorted(zt.items()):
                    at = f"Lc: {t} worth nothing at {', '.join(map(str, levels))}"
                    if raid_path:   # a healer or tank page levels as its raid build: its points are the raid build's
                        f["notes"].append(f"{at} ({RAID_PATH_VERDICT})")
                        continue
                    kind = GK.gate_kind(trees, GK.state_of(b["allocation"]), t)
                    tag = ("utility: " + [x for x, _ in UT.TAGS][use[t]]) if use.get(t, UT.NONE) < UT.NONE else None
                    if GK.is_prerequisite(kind):   # it can be nowhere else: its point is the price of the talent that needs it
                        f["notes"].append(f"{at} (gate: {kind})")
                    elif kind:
                        # 2026-11-21 (the audit session): a tier point can be held by any legal talent of the rows below, so it must be
                        # the most useful one: the filler pass tried its homes (fl_filler_pass.py step 5b) and found none, or it moves
                        v, why = homes.get(t, ("", ""))
                        if v in ("no better home", "no legal home") or v.startswith("kept: utility"):
                            f["notes"].append(f"{at} ({kind}; the filler pass: {v}" + (f", {why}" if why and v != "no legal home" else "") + ")")
                        else:
                            f["fail"].append(f"{at}: only a {kind}, and no filler record on this build shows a more useful legal home "
                                             f"was tried" + (f" (its verdict: {v})" if v else "") + " (fightlab/fl_filler_pass.py)")
                    else:
                        v0 = homes.get(t, ("", ""))[0]
                        why = tag or ("recorded filler" if t in rec or v0 == "no better home" else None) or (v0 if v0.startswith("kept: utility") else None)
                        (f["notes"] if why else f["fail"]).append(at + (f" ({why})" if why else ""))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("classes", nargs="*")
    ap.add_argument("--fights", type=int, default=1500)
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--skip-removal", action="store_true", help="leave Lc out (its removal runs are the slow part)")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    rec = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    classes = a.classes or [c for c in SM.CLASSES if LG.load(c)]
    with multiprocessing.Pool(a.jobs, initializer=_init) as pool:
        for cls in classes:
            res = check_class(cls, pool, a.fights, not a.skip_removal)
            for spec, f in res.items():
                print(f"== {cls} {spec} ({f['build']}, {f['rotation']}): " + ("FAIL" if f["fail"] else "pass"), flush=True)
                for x in f["fail"]:
                    print(f"   FAIL {x}", flush=True)
                for x in f["notes"]:
                    print(f"   note {x}", flush=True)
                for L, r in f["levels"].items():
                    casts = ", ".join(f"{sp} {n}" for sp, n in sorted((r.get("casts") or {}).items(), key=lambda kv: -kv[1]))
                    print(f"   L{L}: {r.get('seconds')} s; {casts}", flush=True)
            if a.write:
                rec[cls] = {"date": datetime.date.today().isoformat(), "specs": res}
                OUT.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
