"""Player pages by class, mode and spec (2026-09-29, user request: "each class has 3 modes, leveling, raid/dummy/parse and PvP; each
spec gets a build and rotation for each mode; hybrids get their own section; extremely organized for new players").

    python _reference/data/render_modes.py [classes...]

Writes, from the same data as every research page (proposed-builds.json, the raid sim, fight lab and healer lab reports,
spec-builds.json for the generated builds; spec_modes.py decides a build's spec):

  README.md                           every class and where to start (the project's own docs: _reference/README.md)
  <class>/README.md                   the sections "Pick your spec" (a grid of its specs and hybrids x the three modes, the
                                      recommended picks marked) and "Which spec is best?" (per mode); the rest is hand-written
  <class>/<mode>/README.md            one mode: its specs ranked
  <class>/<mode>/<spec>.md            one spec in one mode: the build (talentsforever.com link), talent order (leveling), what to
                                      press, the numbers (raid: also by gear tier, pre-BiS and phase-1 BiS, from the
                                      machine-learning pipeline's records raidsim/ml/), alternatives

Everything technical stays in <class>/research/. Generated: never hand-edit (rebuild.py's regen step runs this).
"""
import datetime
import json
import re
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import paths  # noqa: E402
import readme_sections  # noqa: E402
import gear_tables  # noqa: E402
import simple_rotation  # noqa: E402
import guides  # noqa: E402
import render_rotations as rr  # noqa: E402
import render_start_here as rs  # noqa: E402
import spec_modes as SM  # noqa: E402
import sim_info as SI  # noqa: E402  (which simulator a record ran on)
from data_build import BUILD as DATA_BUILD, CAPTURED as DATA_CAPTURED  # noqa: E402

TODAY = datetime.date.today().isoformat()
BUILD = DATA_BUILD
GEN = json.load(open(HERE / "spec-builds.json", encoding="utf-8")) if (HERE / "spec-builds.json").exists() else {}
GEN_MARK = "⚗"   # marks a generated build (spec_builds.py) wherever a player picks one
DER_MARK = "🔬"   # marks a derived build (derive_leveling.py, derive_raid.py, derive_pvp.py): searched in a simulator or from the model + community
DERIVED = {m: json.load(open(HERE / f"derived-{m}.json", encoding="utf-8")) if (HERE / f"derived-{m}.json").exists() else {}
           for m in ("leveling", "raid", "pvp")}


ML_KEYS = ("bis-dummy", "bis-raid", "prebis-dummy", "prebis-raid")   # raidsim/ml_builds.KEYS


def ml_complete(r):
    """A finished record (as raidsim/ml_builds.complete: every tier x setting searched and the comparison race run)."""
    return all(k in (r.get("search") or {}) for k in ML_KEYS) and "compare" in r


def _ml_records(d):
    out = {}
    for p in sorted(d.glob("*.json")) if d.exists() else []:
        if p.name in ("spell-probe.json", "rotations.json"):
            continue
        try:
            r = json.load(open(p, encoding="utf-8"))
        except ValueError:   # a record the pipeline is writing right now
            continue
        if r.get("class") and any(((r.get("search") or {}).get(k) or {}).get("winner") for k in ("bis-dummy", "prebis-dummy")):
            out[(r["class"], r["spec"])] = r
    return out


def ml_tiers():
    """{(class, spec): record} of the machine-learning pipeline (raidsim/ml_pipeline.py) with a pre-BiS or BiS result.
    2026-10-15 page audit B2: the same choice as raidsim/gear_links.py, so a page's tier numbers and its gear table come from one record:
    the current record when it is finished, else the finished one ml_pipeline --fresh kept in ml/prev/ (flagged `_prev`), else a
    current record still being searched (numbers without a gear table)."""
    d = HERE / "raidsim" / "ml"
    cur, prev = _ml_records(d), _ml_records(d / "prev")
    out = {}
    for k in set(cur) | set(prev):
        c, p = cur.get(k), prev.get(k)
        if c and ml_complete(c):
            out[k] = c
        elif p and ml_complete(p):
            out[k] = dict(p, _prev=True)
        else:
            out[k] = c or dict(p, _prev=True)
    return out


TIERS = ml_tiers()
OWN_ROT = (json.load(open(HERE / "fightlab" / "own-rotation.json", encoding="utf-8"))
           if (HERE / "fightlab" / "own-rotation.json").exists() else {})   # {class: {build id: {rotation, levels}}}


def unused_talents():
    """{(class, build id): [row]} of raidsim/unused_abilities.py: talents whose ability the rotation does not cast, and why they stay."""
    p = HERE / "raidsim" / "unused-abilities.json"
    out = {}
    if p.exists():
        for r in json.load(open(p, encoding="utf-8")).get("rows", []):
            out.setdefault((r["class"], r["build"]), []).append(r)
    return out


UNUSED = unused_talents()
TIER_KEYS = (("prebis", "Pre-BiS"), ("bis", "Phase 1 BiS"))
SLOTS = ["Head", "Neck", "Shoulders", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet", "Finger", "Finger", "Trinket", "Trinket",
         "Main hand", "Off hand", "Ranged/relic"]
RANKINGS = ROOT / "_reference" / "dps-rankings.md"


# the simulator the pages' other numbers come from: beta 70291 (2ce8265) with the 2026-10-09 audit (Atiesh out of the full raid, the
# downranking penalty, hit rules). Gear-tier records searched before it ran on older simulators (40be98e / b0f0df3, Atiesh in): flagged
# (2026-10-09: the mage page ranked Arcane first in a full raid and last in its tier table)
SIM_SINCE = "2026-10-09"


def tier_sim(r):
    """The simulator commit an ML record's page numbers ran on (as raidsim/ml_builds.sim_of): the comparison race's, the final search's,
    the record's own, else the pin of its date."""
    c = (r.get("compare") or {}).get("commit") or ((r.get("search") or {}).get("bis-dummy") or {}).get("commit") or r.get("commit")
    return {"commit": c[:7]} if c else {"commit": SI.commit_of_date(r.get("date"))}


def tier_date(r):
    """The latest date of a record's tier searches (its own date when they carry none)."""
    ds = [((r.get("search") or {}).get(f"{t}-{w}") or {}).get("date") for t, _ in TIER_KEYS for w in ("raid", "dummy")]
    return max([d for d in ds if d] or [r.get("date") or ""])


def tier_stale_note(dates):
    old = sorted({d for d in dates if d and d < SIM_SINCE})
    if not old:
        return []
    return [f"*Gear-tier numbers searched on {', '.join(old)}, on an older simulator build than the rest of this page (before beta "
            f"70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs "
            f"differently than the full-raid ranking. The searches are queued to run again.*", ""]


def tier_not_split(r, k):
    """A hybrid's tier winner with 30 points in the tree its entry's rotation is built for (as raidsim/ml_builds.not_split): that tree's
    build, not a split, so the hybrid's page and the class index leave its number out (2026-10-16: the Elemental-Enhancement page showed
    the search's 19/32/0, an Enhancement build)."""
    s = (r.get("search") or {}).get(k) or {}
    if not r.get("spec", "").startswith("Hybrid") or not s.get("winner"):
        return ""
    own = SM.RAID_ENTRY_TREES.get((r["class"], s.get("entry")), set())
    deep = [t for t, v in s["winner"]["allocation"].items() if sum(n for _, n in v) >= 30 and t in own]
    return f"the search ended at {s['winner']['split']}, 30 points in {deep[0]}: that tree's build, not a split" if deep else ""


def tier_dps(r, k):
    w = ((r.get("search") or {}).get(k) or {}).get("winner")
    return f"{w['dps']:.0f}" if w and not tier_not_split(r, k) else "-"


def page_gear(r, tier):
    """The set a page shows for a tier (as raidsim/ml_builds.page_gear): the full-raid winner's own set when it plays another entry."""
    g = r.get("gear") or {}
    return g.get(f"{tier}-raid") or g.get(tier)


def tier_lines(cls, spec, src, top):
    """A spec raid page's DPS by gear tier: the best talents per tier and setting in the spec's own gear, and that gear."""
    r = TIERS.get((cls, spec))
    if not r:
        return []
    flat = lambda a: {n: k for items in a.values() for n, k in items}   # noqa: E731
    o = ["**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning "
         f"search in the community simulator, {SI.label(tier_sim(r), short=True)}; [every spec]({paths.rel(src, RANKINGS)})):", "",
         "| Gear | Full raid DPS | Best talents |", "|---|---|---|"]
    for t, name in TIER_KEYS:
        w = ((r.get("search") or {}).get(f"{t}-raid") or {}).get("winner")
        if not w:
            continue
        ns = tier_not_split(r, f"{t}-raid")
        if ns:
            o.append(f"| {name} | - | none as a split ({ns}) |")
            continue
        # the talents ml_builds.shown() gives: moved out of abilities the winner never casts (tidy_winners), else the BiS raid winner
        # with its free points following the hand draft (the written build), else the winner
        al = ((r.get("tidied") or {}).get(f"{t}-raid") or ((r.get("aligned_raid") or {}) if t == "bis" and (r.get("aligned_raid") or {}).get("moves") else None)
              or w)
        same = {n: k for n, k in flat(al["allocation"]).items() if k}
        tl = "this build" if rs.flat(top) == same else f"[{al['split']}]({rs.tf_link(cls, same)})"
        if tl != "this build" and t == "bis" and f"confirms {top['id']} " in ((r.get("builds") or {}).get("why") or ""):
            tl += " (ties this build)"
        o.append(f"| {name} | {tier_dps(r, f'{t}-raid')} | {tl} |")
    o.append("")
    if r.get("_prev"):   # 2026-10-15 page audit B2: the previous run keeps the stale caveat when it predates the current simulator
        o += [f"*From the previous search run (searched {tier_date(r) or 'on an earlier date'}); a new run is under way and will replace "
              "these numbers and the gear.*", ""]
    o += tier_stale_note([tier_date(r)])
    gt = gear_tables.table(cls, spec)   # every item and enchant linked to Wowhead, where it drops (raidsim/gear_links.py)
    if gt:
        il = "; ".join(f"{name} {(page_gear(r, t) or {}).get('ilvl', '-')}" for t, name in TIER_KEYS if page_gear(r, t))
        o += [f"**The gear** (average item level: {il}; each item opens its Wowhead page, with where it drops and its enchant):", ""] + gt + [""]
        sl = gear_tables.sim_line(cls, spec)
        if sl:
            o += [sl, ""]
        return o
    for t, name in TIER_KEYS:
        g = page_gear(r, t) or {}
        if g.get("names"):
            o.append(f"- **{name} gear** (average item level {g.get('ilvl', '-')}): "
                     + "; ".join(f"{SLOTS[i] if i < len(SLOTS) else '?'}: {n}" for i, n in enumerate(g["names"]) if n))
    return o + [""]


def support_gear(cls, spec, role):
    """A healer or tank raid page's pre-BiS and BiS sets (2026-10-15, user decision of 2026-10-14: real sets for both, the same linked
    table as the damage pages). Tanks: chosen in the community simulator on tank value (raidsim/tank_gear.py); healers: chosen by stat
    weights measured in this project's healer lab (heallab/heal_gear.py)."""
    gt = gear_tables.table(cls, spec, role)
    if not gt:
        return []
    s = gear_tables.spec(cls, spec, role) or {}
    il = "; ".join(f"{name} {s['ilvl'][t]}" for t, name in TIER_KEYS if (s.get("ilvl") or {}).get(t))
    how = ("chosen in the community simulator on tank value, threat and damage taken, for this build in a full raid. The simulator's item "
           "database lists base armor for only about one armor item in five; this project's patch fills in the rest from Classic's values "
           "(our assumption: Forever may have changed some)" if role == "tank" else
           "chosen by the stat weights this project's healer lab measures for this build, the healing capacity each stat adds; "
           "healers are in no community simulator, so this is our model")
    o = [f"**The gear** (average item level: {il}; {how}; each item opens its Wowhead page, with where it drops and its enchant):", ""] + gt + [""]
    sl = gear_tables.sim_line(cls, spec, role=role)
    return o + ([sl, ""] if sl else [])


def tier_table(cls, specs, src):
    """A class raid index's DPS by gear tier for its damage specs."""
    rows = [(spec, TIERS[(cls, spec)]) for spec in specs if (cls, spec) in TIERS]
    if not rows:
        return []
    rows.sort(key=lambda x: 0 if tier_not_split(x[1], "bis-raid") else
              -((((x[1].get("search") or {}).get("bis-raid") or {}).get("winner") or {}).get("dps") or 0))
    o = ["**By gear tier**: each damage spec with its best talents for each tier, in its own gear (DPS in a full raid; "
         f"[every class]({paths.rel(src, RANKINGS)})):", "", "| Spec | Pre-BiS | Phase 1 BiS |", "|---|---|---|"]
    for spec, r in rows:
        o.append(f"| [{SM.spec_name(cls, spec)}]({SM.spec_slug(cls, spec)}.md) | {tier_dps(r, 'prebis-raid')} | {tier_dps(r, 'bis-raid')} |")
    return o + [""] + tier_stale_note([tier_date(r) for _, r in rows])


def mark(b):
    return f" {DER_MARK}" if b.get("derived") else f" {GEN_MARK}" if b.get("generated") else ""
PAGE_MODES = ("leveling", "raid")   # 2026-10-04, user decision: "I just want a raid DPS build and a leveling build ... clean up the pages to only have leveling and raid builds"; PvP stays in research/
BADGE = "✅ Recommended"
DERIVED_BAR = 0.005   # a derived build leads its slot only while this much better than the best other build (2% from 2026-09-30, a rule
                      # Claude set and the notes misattributed to the user; 0.5% since 2026-10-07: the user's principle is the highest DPS
                      # in a raid, and 0.5% is above the noise between separate page races)
TIE = 0.03   # specs within 3% of the best share the recommendation: the simulations cannot separate them
def foot(sims=None):
    """The page footer: the talent and spell data's client build and, for a page that prints raid numbers, the simulator, commit and
    client build of the records behind them (2026-10-22, sim-port: the raid numbers came from the ElliotWood/Forever fork at 2ce8265,
    client 70291, while the footer named only the talent data's 70425)."""
    raid = SI.summary(sims or [])
    return (f"*Generated by `_reference/data/render_modes.py` on {TODAY} from this project's builds and simulations of the WoW: Forever beta "
            f"(talent and spell data: client build {BUILD}" + (f"; raid numbers: {raid}" if raid else "") + "). Simulations, not in-game "
            "measurements. Do not hand-edit.*")


FOOT = foot()   # pages without raid numbers


def raid_sims(R, ids=None):
    """The simulator blocks behind raid_numbers rows (the environments run's for the full-raid numbers, else the race's), for the build
    ids given or every row."""
    out = []
    for bid, r in R.items():
        if ids is not None and bid not in ids:
            continue
        d = r.get("d") or {}
        s = d.get("sim_env") if not r.get("tank") and d.get("sim_env") else d.get("sim")
        if s:
            out.append(s)
    return out


# ------------------------------------------------------------------------------------------------ numbers
def raid_numbers(cls):
    """{build id: {"dps", "raid", "group", "value", "entry", "d", "row"}} over every raid entry: a build's best entry by full-raid DPS.
    Since 2026-10-02 (user decision: "raid/parse builds should assume a group setting ... the recommendations should always be what offers
    the highest DPS in a raid/group setting") raid pages rank by `group` = DPS in a full raid (every raid buff and debuff), the training
    dummy's DPS when a build has no raid number; `d`/`row` carry the raid rotation's lines (render_rotations.spec_data, raid view)."""
    out = {}
    B = rr.builds(cls)
    for x in rs.raid_rows(cls, "raid"):
        r = x["row"]
        lab = r["label"]
        own = SM.RAID_ENTRY_TREES.get((cls, x["spec"]))
        if lab in B and own and not SM.rotation_allows(SM.spec_of(cls, B[lab]), own):
            continue   # 2026-10-08 (user decision): a build counts only in an entry built for its own spec, never in a faster sibling's
        grp = r.get("value") if x["tank"] else (r.get("raid") or r.get("dps"))
        cur = out.get(lab)
        if cur is None or (grp or 0) > (cur["group"] or 0):
            out[lab] = {"dps": r.get("dps"), "raid": r.get("raid"), "group": grp, "value": r.get("value"), "entry": x["spec"], "d": x["d"], "row": r,
                        "tank": x["tank"]}
    return out


def current_record(rec):
    """Audit 2026-10-18 row 75: a record's numbers count only from the day the current data were captured, like the reports (B13).
    derived-leveling.json, spec-builds.json, own-rotation.json and the open-search records carry a `date`; one older than
    data_build.CAPTURED (or without a date) is ignored, so a 2026-09-30 race never overrides a report on the current data."""
    return not DATA_CAPTURED or (rec.get("date") or "")[:10] >= DATA_CAPTURED


def leveling_numbers(cls):
    """{build id: {level: seconds per kill}} from the fight lab reports (main build and the compared ones) and spec-builds.json."""
    out = {}
    d = paths.fightlab_dir(cls)
    # 2026-10-15 page audit B13: the newest report first, and none older than the data the fight lab now runs on. Before, setdefault over
    # the sorted file names let a stale variant report win (Elemental leveling 38 s from elemental-dps-opt.json, a 70009 run of
    # 2026-09-29, ahead of elemental-dps.json of 2026-10-09). The reports carry no date or data build of their own (their .md said
    # "70009" whatever the data until 2026-10-09), so a report's date is its last commit (its file time while uncommitted), and it
    # counts only from the day the current talent and spell data were captured (data_build.CAPTURED).
    cands = {}   # build id -> [(sort key, levels, the rotation it played)]
    for f in (d.glob("*.json") if d.exists() else []):
        if f.stem.endswith(("-aoe", "sensitivity", "-calibration")):
            continue
        fd = report_date(f)
        if DATA_CAPTURED and fd < DATA_CAPTURED:
            continue
        try:
            rep = json.load(open(f, encoding="utf-8"))
        except ValueError:
            continue
        if not isinstance(rep, dict) or "levels" not in rep or "build" not in rep or rep.get("mob_level_offset") or rep.get("gear", "greens") != "greens":
            continue
        rows = [(rep["build"], rep["levels"], True)] + [(bid, lv, False) for bid, lv in (rep.get("compare") or {}).items()]
        for bid, lv, main in rows:
            # an optimizer build plays under its own model (fightlab/run.py spec_of_build): opt-<model>-<profile>
            own = next((m for m in STEPS.get(cls, {}) if bid.startswith(f"opt-{m}-")), None)
            per = {int(L): r["time_per_kill"] for L, r in lv.items() if isinstance(r, dict) and "time_per_kill" in r}
            # the newest report; on one date the report of the build's own rotation (mage: frostfire-leveling.json also runs
            # opt-frost-leveling-leveling-st), then the one it is the main build of, then the file name
            key = (fd, own is None or own == rep.get("spec"), main, [-ord(c) for c in f.name])
            cands.setdefault(bid, []).append((key, per, (own if not main else None) or rep.get("spec")))
    for bid, cs in cands.items():
        _, per, model = max(cs, key=lambda x: x[0])
        out[bid] = per
        LEVEL_MODEL.setdefault((cls, bid), model)
    for tree, rec in (DERIVED["leveling"].get(cls) or {}).items():   # derived builds: the race's numbers (seed 3)
        if rec.get("verdict") in ("replaces", "new") and rec.get("levels") and current_record(rec):
            bid = f"{SM.slug(tree)}-leveling"
            out[bid] = {int(Lv): v for Lv, v in rec["levels"].items()}
            LEVEL_MODEL[(cls, bid)] = rec["spec"]
    whole = open_leveling(cls, whole=True)
    for spec, rec in (whole.get("rotations") or {}).items():   # open-search builds (open_builds.py): the 20-60 race's numbers (seed 3)
        if not current_record({"date": rec.get("date") or whole.get("date")}):   # a rotation's own date, else the record's (its start)
            continue
        lv = ((rec.get("race") or {}).get("open winner") or {}).get("levels") or {}
        model = spec   # the rotation it was found in: a faster sibling rotation (fl_synergy.cross_rotations) is research only since
                       # 2026-10-08 (user decision: no spec takes another spec's rotation because it is faster)
        for bid in (rec.get("builds") or {}).get("written") or []:
            if lv:
                out[bid] = {int(Lv): v for Lv, v in lv.items()}
                LEVEL_MODEL[(cls, bid)] = model
        # 2026-10-22: the race's other rows are our builds of the trees that level with this rotation, raced in it (seed 3, 20-60).
        # Only the winner's row was read, so a spec whose own build lost to a hybrid (Demonology, Destruction, Subtlety after the
        # leveling re-run) had no current number and its page fell back to a stale record's model (the Affliction steps on Demonology).
        for bid, row in (rec.get("race") or {}).items():
            if bid in ("open winner",) or bid.startswith("finalist") or bid in out or not isinstance(row, dict) or not row.get("levels"):
                continue
            out[bid] = {int(Lv): v for Lv, v in row["levels"].items()}
            LEVEL_MODEL[(cls, bid)] = model
    for bid, info in (GEN.get(cls) or {}).items():
        if info.get("levels") and current_record(info):
            out.setdefault(bid, {int(L): v for L, v in info["levels"].items()})
        if info.get("model"):   # setdefault (2026-10-08): a stale generated record (arcane-leveling from 2026-09-29, the borrowed
            LEVEL_MODEL.setdefault((cls, bid), info["model"])   # frost-leveling model) had overwritten the derived build's own rotation
    for bid, rec in (OWN_ROT.get(cls) or {}).items():   # fightlab/own_rotation_race.py: page builds raced with their spec's own rotation
        if rec.get("levels") and current_record(rec):
            out[bid] = {int(L): v for L, v in rec["levels"].items()}
            LEVEL_MODEL[(cls, bid)] = rec["rotation"]
    return out


_DIRTY = []


def report_date(f):
    """A report's date (YYYY-MM-DD): its last commit, or its file time when it is new or changed since (a regenerated report)."""
    import subprocess
    if not _DIRTY:   # files changed or untracked in the working tree, read once
        try:
            st = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=ROOT, capture_output=True, text=True,
                                encoding="utf-8").stdout
        except OSError:
            st = ""
        _DIRTY.append({(ROOT / ln[3:].strip().strip('"')).resolve() for ln in st.splitlines() if len(ln) > 3})
    mtime = datetime.date.fromtimestamp(f.stat().st_mtime).isoformat()
    if f.resolve() in _DIRTY[0]:
        return mtime
    try:
        cd = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(f)], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        cd = ""
    return cd or mtime


def open_leveling(cls, whole=False):
    """The open leveling search's record (fightlab/open/<class>.json): {rotation: record} (whole=True: the record itself); {} while a
    search is writing it."""
    f = HERE / "fightlab" / "open" / f"{cls}.json"
    try:
        st = json.load(open(f, encoding="utf-8")) if f.exists() else {}
    except ValueError:
        return {}
    return st if whole else (st.get("rotations") or {})


_TALENT_SPELLS = {}


def talent_spells(cls):
    """Names of the class's active spells that a talent grants (Holy Shock, Mortal Strike, Summon Hawk ...): the spellbook's active
    spells whose name is a talent name."""
    if cls not in _TALENT_SPELLS:
        talents = {t["name"] for tr in json.load(open(HERE / "forever-talents" / f"{cls}.json", encoding="utf-8"))["trees"] for t in tr["talents"]}
        out = set()
        sp = HERE / "forever-spells" / f"{cls}.json"
        for tab in (json.load(open(sp, encoding="utf-8")).get("tabs", []) if sp.exists() else []):
            if tab.get("name") == "Pets":
                continue
            for s in tab.get("spells", []):
                ranks = [r for r in s.get("ranks", []) if r.get("id")]
                if s.get("name") in talents and ranks and "Passive" not in (ranks[-1].get("rank") or ""):
                    out.add(s["name"])
        _TALENT_SPELLS[cls] = out
    return _TALENT_SPELLS[cls]


_ENV = {}


def env_info(cls, entry, label):
    """(ladder steps, DPS-over-time windows) of a build in its entry's environments report, or (None, None)."""
    if (cls, entry) not in _ENV:
        f = paths.raidsim_dir(cls) / f"{entry}-environments.json"
        rows = json.load(open(f, encoding="utf-8"))["results"] if f.exists() else []
        R = rr.raidrun()
        _ENV[(cls, entry)] = (R.ladder_steps(rows), R.curve_windows(rows))
    lad, cur = _ENV[(cls, entry)]
    return lad.get(label), cur.get(label)


_CASTS = {}


def casts_of(cls, entry, label):
    """Casts per fight of a build in its entry's race report ({} when missing)."""
    if (cls, entry) not in _CASTS:
        f = paths.raidsim_dir(cls) / f"{entry}.json"
        _CASTS[(cls, entry)] = {x["label"]: x.get("casts") or {} for x in json.load(open(f, encoding="utf-8"))["results"]} if f.exists() else {}
    return _CASTS[(cls, entry)].get(label, {})


_RAID_CASTS = {}


def raid_casts_of(cls, entry, label):
    """Casts per fight of a build in a full raid (the environments run's `raid_casts`, recorded since 2026-10-02; {} when missing)."""
    if (cls, entry) not in _RAID_CASTS:
        f = paths.raidsim_dir(cls) / f"{entry}-environments.json"
        _RAID_CASTS[(cls, entry)] = {x["label"]: x.get("raid_casts") or {} for x in json.load(open(f, encoding="utf-8"))["results"]} if f.exists() else {}
    return _RAID_CASTS[(cls, entry)].get(label, {})


def late_dps(cls, r):
    """Average DPS over a 6-minute fight (the curve's longest) for a raid_numbers row, or None."""
    return (list((env_info(cls, r["entry"], r["row"]["label"])[1] or {}).values()) or [None])[-1] if r else None


LEVEL_MODEL = {}   # (class, build id) -> the fight-lab spec model the build plays
STEPS = {k: v for k, v in json.load(open(HERE / "leveling-steps.json", encoding="utf-8")).items() if not k.startswith("_")}


def healer_numbers(cls):
    return {r["id"]: r for r in rs.healer_rows(cls)}


def weighted(per):
    tot = sum(int(L) / 10 for L in per)
    return sum(v * int(L) / 10 for L, v in per.items()) / tot if tot else None


# ------------------------------------------------------------------------------------------------ picking builds
def rank_builds(cls, mode, builds, nums):
    """Builds of one spec and mode, best first: raid by DPS in a full raid (tanks: tank value; healers: healing capacity), leveling by
    level-weighted time per kill (solo), PvP hand drafts before generated ones."""
    R, L, H = nums

    def key(b):
        bid = b["id"]
        gen = 1 if b.get("generated") else 0
        if mode == "raid":
            if b.get("role") == "healer":
                return (0, -(H.get(bid, {}).get("capacity") or 0), gen)
            r = R.get(bid) or {}
            return (0, -(r.get("group") or 0), gen)
        if mode == "leveling":
            w = weighted(L.get(bid) or {})
            return (0 if w else 1, w or 0, gen)
        return (0 if b.get("replaces") else 1 + gen, b.get("tier") != "primary", bid)
    parse_ids = set() if mode == "raid" else {b["id"] for b in builds if b["id"].endswith("-parse")}   # raid: a parse build is a raid build
    main = sorted([b for b in builds if b["id"] not in parse_ids], key=key)
    # the user's rule (2026-09-30): a derived build is the pick only while it beats the best other build by 2%+ (DERIVED_BAR);
    # a re-race that shrinks the gap (the equal-tier gear: Enhancement +3.1% -> +1.5%) puts that build back on top
    if mode in ("raid", "leveling") and main and main[0].get("derived"):
        def metric(b):
            if mode == "leveling":
                w = weighted(L.get(b["id"]) or {})
                return 1 / w if w else None
            r = R.get(b["id"]) or {}
            return r.get("group")
        others = [b for b in main[1:] if not b.get("generated") and metric(b)]
        if others and metric(main[0]) and metric(main[0]) < metric(others[0]) * (1 + DERIVED_BAR):
            main.remove(others[0])
            main.insert(0, others[0])
    return main + [b for b in builds if b["id"] in parse_ids]


def derived_text(mode, top):
    """Where a derived build comes from, for the page's note."""
    if top.get("preset"):   # the community simulator's own preset talents, raced ahead of our builds (2026-10-09: Feral Cat 9/35/7)
        return (f"the community simulator's own preset talents ({top['preset']}), raced against this project's builds in a full raid, where "
                "they came out ahead")
    if top["id"].endswith("-open-raid"):
        return ("found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, "
                "raced against the rotation's builds)")
    if top["id"].endswith("-open-leveling"):
        return ("found by this project's open leveling search (every legal build, no tree rule, in the fight lab, this project's leveling "
                "simulator; the winner picked by a race at levels 20-60)")
    if top["id"].endswith("-ml-heal"):   # 2026-10-14 page audit: healer builds read "community's raid simulator"
        return ("found by this project's deep search over every legal build of the spec in the healer lab (this project's healing "
                "model; healers are not in the community simulator), then raced against the spec's builds")
    if top["id"].endswith("-ml-tank"):
        return ("found by this project's deep search over every legal build of the spec in the community's raid simulator, on tank value "
                "(threat and damage taken), then raced against the spec's builds")
    return {"leveling": "searched in the fight lab (this project's leveling simulator) from the spec's builds and the stats model's best one",
            "raid": ("found by this project's machine-learning search over every legal build of the spec in the community's raid "
                     "simulator (phase-1 BiS gear, then raced against the spec's builds)" if top["id"].endswith("-ml-raid")
                     else "searched in the community's raid simulator from the spec's best build"),
            "pvp": "the stats model's best PvP build, with the community's most-picked talents where the model rates talents alike"}[mode]


def bname(cls, b):
    """A build's player name; an optimizer build whose name is only a damage breakdown reads "<spec> (optimized)" instead of a tree name."""
    n = rs.display_name(cls, b)
    if b["id"].startswith("opt-"):
        spec = SM.spec_of(cls, b)
        # 2026-10-08: an optimizer build is named after its scorer model ("Raid Combat swords"); when that model is another spec's
        # rotation (its points put it elsewhere: an Assassination page showed "Raid Combat swords") the page names it after its own spec
        rest = b["id"][len("opt-"):]
        lev = SM.leveling_rotation_trees(cls)
        models = [m for m in list(lev) + [e for c, e in SM.RAID_ENTRY_TREES if c == cls] if rest.startswith(m + "-")]
        model = max(models, key=len) if models else None
        trees_ = (lev.get(model) if SM.mode_of(b) == "leveling" else SM.RAID_ENTRY_TREES.get((cls, model))) if model else None
        # 2026-10-09 (the class reviews): always the spec's name, never the scorer model's ("Two-handed Retribution", "Raid Frostbolt with
        # Ice Lance on Fingers of Frost charges" had read as other specs); the weapon variant and the scenario keep two apart
        prof = rest[len(model) + 1:] if model else ""
        if not model:   # a model no rotation map names (the mage's frost-aoe): its profile from the id's end (2026-10-15 page audit B9: the
                        # AoE grinding build read "Frost (optimized)" like the single-target one)
            prof = max((p for p in OPT_PROFILE if rest.endswith("-" + p)), key=len, default="")
        parts = [SM.RAID_ENTRY_VARIANT.get((cls, model), "").lower()] if model and SM.mode_of(b) != "leveling" else []
        parts = [x for x in parts if x and x not in SM.spec_name(cls, spec).lower()]   # "Shadow Bolt hybrid", not "... (optimized, shadow bolt)"
        parts.append(OPT_PROFILE.get(prof, "") or ("tank" if prof == "raid-tank" and "Protection" not in spec else ""))   # the bear beside the cat
        parts = [x for x in parts if x]
        sn = SM.spec_name(cls, spec)
        m = re.fullmatch(r"(.+) \((.+)\)", sn)
        if m:   # "Melee (split, optimized)", not "Melee (split) (optimized)" (2026-10-15 page audit B9)
            sn, parts = m.group(1), [m.group(2) + ", optimized"] + parts
            return f"{sn} ({', '.join(parts)})"
        return f"{sn} (optimized{', ' + ', '.join(parts) if parts else ''})"
    return n


# the scorer profile an optimizer build was exported for, as the pages say it (empty: the mode's main profile)
OPT_PROFILE = {"raid-dps": "", "raid-tank": "", "raid-heal": "", "leveling-st": "", "parse": "parse", "raid-dps-extwc": "another mage's Winter's Chill",
               "leveling-aoe": "AoE pulls", "solo-60": "solo at 60"}


def link(cls, b, src):
    page = paths.build_page_by_id("forever", cls, b["id"])
    name = bname(cls, b)
    return f"[{name}]({paths.rel(src, page)})" if page else name


def tree_link(cls, b):
    return f"[open the talent tree]({rs.tf_link(cls, rs.flat(b))})"


def spec_title(cls, spec):
    return f"{SM.spec_name(cls, spec)} {cls.capitalize()}"


def recommended(cls, g, specs, mode, nums):
    """The specs a new player should pick for a mode: leveling and raid damage within TIE of the best. PvP has no ranking, so none."""
    R, L, H = nums
    tops = {spec: rank_builds(cls, mode, g[spec][mode], nums) for spec in specs}
    if mode == "leveling":
        w = {spec: weighted(L.get(r[0]["id"]) or {}) for spec, r in tops.items() if r}
        w = {k: v for k, v in w.items() if v}
        return {k for k, v in w.items() if v <= min(w.values()) * (1 + TIE)} if w else set()
    if mode == "raid":
        d = {spec: (R.get(r[0]["id"]) or {}).get("group") for spec, r in tops.items() if r and r[0].get("role") != "healer" and not (R.get(r[0]["id"]) or {}).get("tank")}
        d = {k: v for k, v in d.items() if v}
        return {k for k, v in d.items() if v >= max(d.values()) * (1 - TIE)} if d else set()
    return set()


# ------------------------------------------------------------------------------------------------ pages
def variant_best(cls, top, builds, nums):
    """Weapon and stance setups of a spec's raid play (2026-10-08, the improvement log's "weapon variants on the pages"; user: "Do all of
    them"): for each setup of the spec (spec_modes.RAID_ENTRY_VARIANT) other than the pick's, the spec's best build raced in that setup's
    entries, by full-raid DPS (own-rotation rule kept), so a player with swords, a two-hander or no pet sees the build for it."""
    R = nums[0]
    own_var = SM.RAID_ENTRY_VARIANT.get((cls, (R.get(top["id"]) or {}).get("entry")))
    ids = {b["id"]: b for b in builds if not b["id"].endswith("-parse")}
    best = {}
    for x in rs.raid_rows(cls, "raid"):
        v = SM.RAID_ENTRY_VARIANT.get((cls, x["spec"]))
        lab = x["row"]["label"]
        if x["tank"] or not v or v == own_var or lab not in ids:
            continue
        own = SM.RAID_ENTRY_TREES.get((cls, x["spec"]))
        if own and not SM.rotation_allows(SM.spec_of(cls, ids[lab]), own):
            continue
        g = x["row"].get("raid")
        if g and (v not in best or g > best[v][1]):
            best[v] = (lab, g)
    return own_var, best, ids


def variant_lines(cls, top, builds, nums, src):
    """The "Other setups" lines of variant_best."""
    own_var, best, ids = variant_best(cls, top, builds, nums)
    if not best:
        return []
    o = ["**Other setups of this spec.** " + (f"This build is the {own_var} setup. " if own_var else "")
         + "The spec's best build for each other setup, in a full raid:", ""]
    for v, (lab, g) in sorted(best.items(), key=lambda kv: -kv[1][1]):
        b = ids[lab]
        # the same form as "Other builds" (2026-10-15 page audit B9), where these builds are no longer listed a second time
        o.append(f"- {v}: " + (f"this build too ({g:.0f} DPS in a full raid)" if lab == top["id"]
                               else f"{link(cls, b, src)} ({rs.split_of(cls, rs.flat(b))}, {g:.0f} DPS in a full raid)")
                 + f" — {tree_link(cls, b)}")
    return o + [""]


def variant_ids(cls, top, builds, nums):
    """The builds the "Other setups" lines list (kept out of "Other builds", 2026-10-15 page audit B9)."""
    return {lab for lab, _ in variant_best(cls, top, builds, nums)[1].values()}


def mode_section(cls, spec, mode, builds, nums, src):
    """The body of one spec x mode page."""
    R, L, H = nums
    o = []
    ranked = rank_builds(cls, mode, builds, nums)
    # 2026-10-15 page audit B10: a hybrid without a leveling build takes the hybrid branch below (the Smite priest's leveling page had
    # read "No leveling build for this spec yet")
    if mode == "leveling" and not ranked and not spec.startswith("Hybrid "):
        other = SM.LEVEL_AS.get((cls, spec))
        if other:
            o += [f"{spec} is a {'healing' if cls in SM.HEAL_TREES and spec in SM.HEAL_TREES[cls] else 'tanking'} spec: level as **{other}** "
                  f"([{other} leveling](../leveling/{SM.spec_slug(cls, other)}.md)) and switch your talents to {spec} at 60 (a respec at a class trainer).", ""]
        else:
            o += ["No leveling build for this spec yet.", ""]
        return o
    if not ranked:
        if spec.startswith("Hybrid "):   # a split found in one mode only: point to where it has a build and to its two trees (2026-10-09)
            word = SM.MODE_TITLE[mode].split(" (")[0].lower()
            other = next((m for m in PAGE_MODES if m != mode), None)
            own = [t for t in spec[len("Hybrid "):].split("/") if t in SM.trees(cls)]
            o += [f"No {word} build of this split: the searches found {SM.spec_name(cls, spec)} for "
                  f"[{SM.MODE_TITLE[other].split(' (')[0].lower()}](../{other}/{SM.spec_slug(cls, spec)}.md) only. "
                  + (f"For {word}, play one of its trees: " + " or ".join(f"[{t}]({SM.spec_slug(cls, t)}.md)" for t in own) + "." if own else ""), ""]
            return o
        return ["No build for this spec in this mode yet.", ""]
    top = ranked[0]
    o += [f"**{link(cls, top, src)}** ({rs.split_of(cls, rs.flat(top))}) — {tree_link(cls, top)}", ""]
    B = rr.builds(cls)
    if top.get("raid_path"):   # a healer or tank spec levels straight into its raid build (user decision, 2026-09-30)
        dv = (DERIVED["leveling"].get(cls) or {}).get(spec) or {}
        ords = dv.get("orders") or {}
        rp = B.get(top["raid_path"])
        # 2026-10-15 page audit B8: the raid build's player name, not its id; and say so when the raid page now recommends another build
        rtop = rank_builds(cls, "raid", SM.grid(cls, list(B.values())).get(spec, {}).get("raid", []), nums)
        rtop = rtop[0] if rtop else None
        same = rp is not None and (rtop is None or rs.flat(rtop) == rs.flat(rp))
        o += [f"> {DER_MARK} These are " + ("your **raid talents**" if same else "the talents of a **raid build**")
              + f" ([{bname(cls, rtop if same and rtop else rp) if rp else top['raid_path']}](../raid/{SM.spec_slug(cls, spec)}.md)"
              + ("" if same else f"; the raid page now recommends {bname(cls, rtop)}") + "), taken in the order "
              f"that levels fastest: the fight lab raced three orders to them"
              + (" (" + "; ".join(f"{k}: {v['weighted']:.0f} s per kill" for k, v in sorted(ords.items(), key=lambda kv: kv[1]['weighted'])) + ")"
                 if ords else "") + ". A model of the beta, to check at launch.", ""]
    elif top.get("derived"):
        o += [f"> {DER_MARK} Derived build: " + derived_text(mode, top)
              + (f"; it beat the hand-made build ({bname(cls, B[top['replaces']]) if top['replaces'] in B else 'no longer listed'})"
                 + (", which stays below as the alternative" if top["replaces"] in {b["id"] for b in ranked[1:]} else "")
                 if top.get("replaces") else "")   # 2026-10-15 page audit B8: its player name, not its id
              + ". A model of the beta, to check at launch.", ""]
    elif top.get("generated"):
        o += [f"> {GEN_MARK} Generated build: no hand-made {spec} build exists for this mode yet, so this is the stats model's best {spec} build"
              + (", refined in the raid simulator" if mode == "raid" and (GEN.get(cls, {}).get(top["id"], {}).get("entry")) else "")
              + ". A starting point, not a proven build.", ""]
    if mode == "raid":
        o += variant_lines(cls, top, builds, nums, src)
    play, talents, numbers = [], [], []   # the page reads: build, how to play, talents while leveling, the numbers, other builds
    if mode == "leveling":
        if top.get("order"):
            talents += ["## Talents while leveling", "", "One point per level from 10, in this order:", "", "| Levels | Talent | Points |", "|---|---|---|"]
            talents += [f"| {s['levels']} | {s['talent']} ({s['tree']}) | {s['points']} |" for s in top["order"]] + [""]
        spec_model = LEVEL_MODEL.get((cls, top["id"])) or (GEN.get(cls, {}).get(top["id"], {}) or {}).get("model") or rs.leveling_pick(cls)[1]
        st = STEPS.get(cls, {}).get(spec_model)
        if st:
            play += ["## How to play", ""]
            # abilities the steps name that this build cannot have (a talent grants them and the build lacks it): the paladin's Prot-Ret
            # leveling split came out of the Holy rotation's search without Holy Shock (2026-10-07)
            held = {n for items in top["allocation"].values() for n, r in items if r}
            named = {m for x in (st.get("before") or []) + list(st.get("steps") or []) + (st.get("between") or []) for m in re.findall(r"\*\*(.+?)\*\*", x)}
            # 2026-10-15 page audit B11: every talent the steps name, passive ones too (Maelstrom Weapon, Renewed Hope, Missile Barrage
            # had stayed in the steps of builds without them); before, only talents that grant an active spell counted
            lacking = sorted(n for n in named if (n in talent_spells(cls) or n in simple_rotation.talent_names(cls)) and n not in held)
            if lacking:
                play += ["**Not in this build:** " + ", ".join(f"**{n}**" for n in lacking) + (" is a talent this build does not take" if len(lacking) == 1 else " are talents this build does not take")
                         + ": skip the lines that use " + ("it" if len(lacking) == 1 else "them") + ". The fight lab played the build without "
                         + ("it" if len(lacking) == 1 else "them") + ".", ""]
            if st.get("before"):
                play += ["**Before the fight:** " + " ".join(st["before"]), ""]
            play += ["**In the fight**, top to bottom:", ""] + [f"{i}. {x}" for i, x in enumerate(st["steps"], 1)] + [""]
            if st.get("between"):
                play += ["**Between fights:** " + " ".join(st["between"]), ""]
        else:
            try:
                desc = rr.fl_description(cls, spec_model)
            except Exception:   # noqa: BLE001
                desc = ""
            if desc:
                play += ["## How to play", "", " ".join(desc.split()), ""]
        per = L.get(top["id"])
        other = SM.LEVEL_AS.get((cls, spec))
        if per and other:   # a healing or tanking spec's own leveling build, next to the damage spec it could level as instead
            ob = rank_builds(cls, mode, SM.grid(cls, list(rr.builds(cls).values()))[other]["leveling"], nums)
            wo, wm = weighted(L.get(ob[0]["id"]) or {}) if ob else None, weighted(per)
            if wo and wm:
                r = wm / wo
                how = (f"about {r:.1f} times as slow" if r >= 1.5 else f"{r - 1:.0%} slower" if r > 1 else f"{1 - r:.0%} faster")
                job = "heal" if spec in SM.HEAL_TREES.get(cls, ()) else "tank"
                # when the tree's own points arrive in the order (a borrowed damage model orders the talents: damage first)
                own = {n for n, _ in top["allocation"].get(spec, [])}
                first = next((st["levels"].split("-")[0] for st in top.get("order", []) if st["talent"] in own), None)
                o += [f"**Leveling as {spec} or as {other}?** This build takes {wm:.0f} s per kill (level-weighted, 20-60), "
                      f"[{other}](../leveling/{SM.spec_slug(cls, other)}.md) {wo:.0f} s: {spec} is {how}."
                      + (f" The fastest order puts its first point into {spec} at level {first}: the damage talents come first." if first and int(first) >= 25
                         else f" Your first {spec} point comes at level {first}." if first else "")
                      + f" Level this way if you want to {job} dungeons later on the way; otherwise level as {other} and switch at 60 "
                        f"(a respec at a class trainer).", ""]
        if per:
            numbers += ["## The numbers", "", "| Level | Seconds per kill (same-level mobs, eating and drinking included) |", "|---|---|"]
            numbers += [f"| {Lv} | {v:.0f} |" for Lv, v in sorted(per.items())] + [""]
    elif mode == "raid":
        r = R.get(top["id"]) if top.get("role") != "healer" else None
        if top.get("role") == "healer":
            h = H.get(top["id"])
            if h:
                numbers += ["## The numbers", "", f"Healing capacity {h['capacity']:.2f} (the raid damage it heals through in this project's healer lab), "
                            f"{h['hps']:.0f} healing per second. Healers are not in the community simulator.", ""]
            numbers += support_gear(cls, spec, "heal")
        elif r and r.get("tank"):
            numbers += ["## The numbers", "", f"Tank value {r['value']:.3f} (threat and damage taken under a boss, relative to our reference tank build).", ""]
            numbers += support_gear(cls, spec, "tank")
        elif r:
            numbers += ["## The numbers", "", "| Setting | DPS |", "|---|---|"]
            nn = (json.load(open(HERE / "raidsim" / "specs.json", encoding="utf-8")).get(cls, {}).get(r["entry"]) or {}).get("numbers_note")
            if r.get("raid"):
                numbers.append(f"| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | {r['raid']:.0f} |")
            numbers.append("")
            if nn:
                numbers += [f"> Note: {nn}", ""]
            numbers += tier_lines(cls, spec, src, top)
            lad, cur = None, None   # dummy-based (buff ladder, fight-length curve): off the player pages since 2026-10-04
            if lad:
                numbers += ["**Where the raid damage comes from** (the same build, adding the raid's buffs one group at a time; percent of the dummy DPS):", "",
                            f"Dummy {lad['dummy']:.0f} → " + " → ".join(f"{k if k != 'rest' else 'everything else'} {v:+.0%}" for k, v in lad["steps"].items())
                            + f" → raid {lad['raid']:.0f}", "",
                            "(*mana*: Blessing of Wisdom, Mana Spring; *armor*: Sunder Armor, Faerie Fire, Curse of Recklessness; *physical*: Battle Shout, "
                            "Blessing of Might, Windfury, Leader of the Pack, Trueshot Aura; *spell*: Curse of the Elements, Arcane Brilliance, Moonkin Aura; "
                            "*everything else*: Kings, stamina, spirit, auras and the raid rotation.)", ""]
            if cur:
                numbers += ["**DPS by fight length** (training dummy; your average DPS if the fight lasts this long):", "",
                            "| " + " | ".join(cur) + " |", "|" + "---|" * len(cur), "| " + " | ".join(f"{v:.0f}" for v in cur.values()) + " |", "",
                            "Falling numbers mean cooldowns used at the pull, or mana running out in long fights.", ""]
        if r:
            texts = [ln["text"] for ln, pl in zip(r["d"]["lines"], r["row"]["lines"]) if pl["used"]]
            late, twists = [], []   # end-of-fight extras after the filler; seal twisting (simple_rotation.simplify)
            keep, prio = simple_rotation.simplify(cls, texts, late, twists)
            held = {n for items in top["allocation"].values() for n, k in items if k}
            pre = simple_rotation.pre_pull(cls, r["d"]["pre"], held)
            names_kept = [x.split("|")[0] for x in keep]
            # a form or self-buff put up before the pull is kept up all fight (Moonkin Form, Shadowform): said once, not left out
            keep += [x for x in pre if simple_rotation.is_self(x) and not x.startswith("Seal of") and x not in names_kept]
            keep_names = [x.split("|")[0] for x in keep]   # an item may carry "|<how to keep it up>" (Slice and Dice's combo points)
            keep_text = ", ".join(f"**{x.split('|')[0]}**" + (f" ({x.split('|', 1)[1]})" if "|" in x else "") for x in keep)
            play += ["## How to play", ""]
            if pre and set(pre) == set(keep_names):   # totems and self-buffs: one line instead of the same list twice
                play += ["**Before the pull, then keep up all fight:** " + keep_text + ".", ""]
            else:
                if pre:
                    play += ["**Before the pull:** " + ", ".join(f"**{x}**" for x in pre) + ".", ""]
                if keep:
                    play += ["**Keep up all fight:** " + keep_text + ".", ""]
            quiet = [u for u in UNUSED.get((cls, top["id"]), []) if u["kind"] != "wasted"]
            if quiet:   # talents the build takes whose ability has no line in the rotation (2026-10-02, user report on unused abilities)
                play += ["**Talents with no line below:** " + "; ".join(f"**{u['talent']}**: {u['advice']}" for u in quiet) + ".", ""]
            if prio:   # "Then" only after a pre-pull, keep-up or talent line (2026-10-15 page audit B9)
                then = play[-2:] != ["## How to play", ""]
                play += [("**Then press" if then else "**Press") + " the first one that is ready**, top to bottom:", ""] + [f"{i}. {x}" for i, x in enumerate(prio, 1)]
                # the filler: the last line when it has no condition and no cooldown (2026-10-09: Bloodrage, Aimed Shot, Fire Nova had been
                # called fillers); else what fills the gaps on its own (Auto Shot, white swings)
                fill = simple_rotation.filler(cls, prio)
                shown = set(pre) | set(keep_names) | {m for x in prio for m in re.findall(r"\*\*(.+?)\*\*", x)} | {x for x, _, _ in late}
                # the build's casts in the full raid the page ranks on (the dummy race's when the environments run has none)
                casts = raid_casts_of(cls, r["entry"], top["id"]) or casts_of(cls, r["entry"], top["id"])
                extra = [f"**{x}**: in the last {n:g} seconds of the fight, when there is no time left for another **{f}**" for x, n, f in late]
                extra += twists
                extra += simple_rotation.advanced(cls, casts, shown, simple_rotation.mcd_window(texts))
                if fill:
                    play += ["", f"**{fill}** is your filler: cast it whenever nothing above is ready.", ""]
                else:
                    auto = simple_rotation.auto_line(cls, r["d"].get("entry"))
                    play += ["", auto, ""] if auto else [""]
                if extra:
                    play += ["**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:", ""] + [f"- {x}" for x in extra]
                    if any("cooldown" in x or "once a fight" in x for x in extra):
                        play += ["- Use your trinkets and a potion together with your big cooldowns.", ""]
                    else:
                        play += [""]
                play += [f"*The simulator's full rotation for this build, with every condition: [research rotation page]"
                         f"({paths.rel(src, paths.rotation_page(cls, 'raid'))}).*", ""]
        # the build with the most DPS alone (training dummy), when it is not the pick: for players who play without a raid's buffs
        solo = None   # the training dummy build: off the player pages since 2026-10-04 (the user's decision: raid and leveling only)
        if solo and ranked and solo["id"] != ranked[0]["id"] and (R.get(ranked[0]["id"]) or {}).get("dps"):
            gap = R[solo["id"]]["dps"] / R[ranked[0]["id"]]["dps"] - 1
            if gap > 0.005:
                numbers += [f"**Alone instead of in a raid?** {link(cls, solo, src)} ({rs.split_of(cls, rs.flat(solo))}) does {R[solo['id']]['dps']:.0f} DPS on "
                            f"the training dummy with only your own buffs ({gap:+.0%} over this build there) — {tree_link(cls, solo)}.", ""]
    else:
        play += ["## How to play", "", "PvP has no fixed rotation: it depends on who you fight. No simulator plays PvP, so this build rests on the talents' "
                 "descriptions and the community's PvP builds.", "", "**Why these talents:** " + rs.short(top.get("summary"), 400), ""]
        dv = (DERIVED["pvp"].get(cls) or {}).get(spec)
        if dv and top.get("derived"):
            sk = [f"**{x['talent']}** ({x['pick']:.0f}% of {spec} builds take it)" for x in dv["skipped_consensus"]]
            ra = [f"**{x['talent']}** (only {x['pick']:.0f}% take it)" for x in dv["rare"]]
            if sk or ra:
                play += ["**Where this build and the community disagree** (talentsforever.com pick rates of builds leading in "
                         f"{spec}, {dv['builds_behind_picks']} builds, all content):", ""]
                play += ([f"- Most take {', '.join(sk)}: the stats model rates it below this build's weakest point for PvP."] if sk else [])
                play += ([f"- This build takes {', '.join(ra)}: the stats model rates it for PvP (control, survival or burst)."] if ra else [])
                play += [""]
            else:
                play += [f"The community agrees: every talent most {spec} builds take is in this build.", ""]
    gl = []   # the hand-written rotation guide (guides.py, 2026-10-09 user request), under How to play
    if mode == "raid":
        if top.get("role") == "healer":
            gl = guides.render(cls, spec, mode, "healer-policy", guides.healer_fingerprint(cls), title="How to heal")
        else:
            ent = (R.get(top["id"]) or {}).get("entry")
            gl = guides.render(cls, spec, mode, ent, guides.raid_fingerprint(cls, ent) if ent else None)
    elif mode == "leveling":
        mdl = LEVEL_MODEL.get((cls, top["id"])) or (GEN.get(cls, {}).get(top["id"], {}) or {}).get("model") or rs.leveling_pick(cls)[1]
        gl = guides.render(cls, spec, mode, f"leveling:{mdl}", guides.leveling_fingerprint(cls, mdl))
    o += play + gl + talents + numbers
    if mode == "raid" and not (R.get(top["id"]) or {}).get("tank"):
        # a damage spec that also holds the class's tank builds (the druid's bear in Feral Combat, 2026-10-15): the best tank build with
        # its numbers and gear, as on the Protection pages
        tb = [b for b in builds if (R.get(b["id"]) or {}).get("tank")]
        if tb:
            bt = max(tb, key=lambda b: R[b["id"]].get("value") or 0)
            rt = R[bt["id"]]
            o += ["## Tanking", "", f"**{link(cls, bt, src)}** ({rs.split_of(cls, rs.flat(bt))}) — {tree_link(cls, bt)}", "",
                  f"Tank value {rt['value']:.3f} (threat and damage taken under a boss, relative to our reference tank build)"
                  + (f": {rt['row']['threat']:.0f} threat and {rt['row']['dtps']:.0f} damage taken per second in a full raid." if rt["row"].get("threat") else "."), ""]
            o += support_gear(cls, spec, "tank")
    alts = [b for b in ranked[1:] if not b["id"].endswith("-parse")]
    # one entry per talent set (2026-10-09: an optimizer that reproduced a hand draft, or its raid and solo exports, listed twice)
    same = {json.dumps(sorted(rs.flat(top).items()))}
    uniq = []
    shown_setups = variant_ids(cls, top, builds, nums) if mode == "raid" else set()
    for b in alts:
        if b["id"] in shown_setups:   # already under "Other setups of this spec" (2026-10-15 page audit B9)
            continue
        k = json.dumps(sorted(rs.flat(b).items()))
        if k not in same:
            same.add(k)
            uniq.append(b)
    alts = uniq
    if alts:
        o += ["## Other builds of this spec", ""]
        for b in alts:
            extra = ""
            if mode == "raid" and (R.get(b["id"]) or {}).get("group") and not (R.get(b["id"]) or {}).get("tank"):
                extra = f", {R[b['id']]['group']:.0f} DPS in a full raid"   # no dummy number on the pages (user decision, 2026-10-04)
            if mode == "leveling" and weighted(L.get(b["id"]) or {}):
                extra = f", {weighted(L[b['id']]):.0f} s per kill, level-weighted"   # no nested parentheses (2026-10-15 page audit B17)
            o.append(f"- {link(cls, b, src)} ({rs.split_of(cls, rs.flat(b))}{extra}) — {tree_link(cls, b)}")
        o.append("")
    return o


def build_suffix(cls, spec, b, mode):
    """The build's name after its spec's link in a ranking, without repeating the spec (2026-10-15 page audit B17: "Frost — Frost —
    Leveling", "Feral Combat — Feral Combat (optimized)"): " — Arcane Blast", " (optimized)", "" for "<spec> — Leveling"."""
    n, sn = bname(cls, b), SM.spec_name(cls, spec)
    if n == sn:
        return ""
    if n.startswith(sn + " — "):
        rest = n[len(sn) + 3:]
        return "" if rest.lower() in (mode, SM.MODE_TITLE[mode].split(" (")[0].lower()) else f" — {rest}"
    if n.startswith(sn + " ("):
        return n[len(sn):]
    return f" — {n}"


def gap_text(x):
    """A gap behind the best: one decimal under 1% (a 0.3% gap had printed as "-0%")."""
    # rounded before the test (2026-10-15 page audit B9: 0.997% printed "+1.0%" next to "+1%")
    return f"{x:+.1%}" if round(abs(x) * 100, 1) < 1 else f"{x:+.0%}"


def support_picks(cls, g, specs, nums):
    """(tanks [(spec, build)], healers [(-capacity, spec, build)] best first) of a class's raid pages: each spec's raid pick when it is a
    tank or healer build, and a damage spec's tank build (the druid's bear in Feral Combat)."""
    R, L, H = nums
    tanks, heals = [], []
    for spec in specs:
        ranked = rank_builds(cls, "raid", g[spec]["raid"], nums)
        if not ranked:
            continue
        b = ranked[0]
        if b.get("role") == "healer":
            heals.append((-(H.get(b["id"], {}).get("capacity") or 0), spec, b))
        elif (R.get(b["id"]) or {}).get("tank"):
            tanks.append((spec, b))
    for spec in specs:   # a spec whose pick is a damage build can hold the class's tank build too (the druid's bear in Feral Combat)
        if any(s2 == spec for s2, _ in tanks):
            continue
        tb = [b for b in (g.get(spec) or {}).get("raid", []) if (R.get(b["id"]) or {}).get("tank")]
        if tb:
            tanks.append((spec, max(tb, key=lambda b: R[b["id"]].get("value") or 0)))
    heals.sort(key=lambda x: x[0])
    return tanks, heals


def ranking(cls, g, specs, mode, nums, prefix=""):
    """One mode's specs, best first, as markdown lines. Leveling: level-weighted seconds per kill (fight lab, the same simulator for every
    spec, so specs compare). Raid: damage specs by training-dummy DPS, then tanks and healers (other jobs, their own measures). PvP: no
    simulator plays PvP, so it is a list, not a ranking."""
    R, L, H = nums
    rows = []
    for spec in specs:
        ranked = rank_builds(cls, mode, g[spec][mode], nums)
        if ranked:
            rows.append((spec, ranked[0]))
    page = lambda spec: f"{prefix}{SM.spec_slug(cls, spec)}.md"   # noqa: E731
    name = lambda spec, b: f"[{SM.spec_name(cls, spec)}]({page(spec)}){build_suffix(cls, spec, b, mode)}" + mark(b)   # noqa: E731
    o = []
    if mode == "leveling":
        scored = sorted(((weighted(L.get(b["id"]) or {}), spec, b) for spec, b in rows if weighted(L.get(b["id"]) or {})), key=lambda x: x[0])
        if not scored:
            return ["No leveling numbers yet.", ""]
        best = scored[0][0]
        o += ["Ranked by time per kill in the fight lab (levels 20-60, higher levels count more; lower is faster):", "",
              "| # | Spec and build | Seconds per kill | Behind the fastest |", "|---|---|---|---|"]
        o += [f"| {i} | {name(spec, b)} | {w:.0f} | {'fastest' if i == 1 else gap_text(w / best - 1)} |" for i, (w, spec, b) in enumerate(scored, 1)]
        lv = [spec for spec in specs if not g[spec][mode] and SM.LEVEL_AS.get((cls, spec))]
        if lv:
            o += ["", "Healing and tanking specs level as a damage spec and switch at 60: "
                  + ", ".join(f"{spec} levels as {SM.LEVEL_AS[(cls, spec)]}" for spec in lv) + "."]
        o.append("")
    elif mode == "raid":
        dps = []
        for spec, b in rows:
            if b.get("role") != "healer" and not (R.get(b["id"]) or {}).get("tank") and (R.get(b["id"]) or {}).get("group"):
                dps.append((-R[b["id"]]["group"], spec, b))
        tanks, heals = support_picks(cls, g, specs, nums)
        if dps:
            dps.sort(key=lambda x: x[0])
            best = -dps[0][0]
            o += ["**Damage**, ranked by DPS in a full raid over a 3-minute fight (every raid buff and debuff: the group setting).", "",
                  "| # | Spec and build | Full raid DPS | Behind the best |", "|---|---|---|---|"]
            for i, (d, spec, b) in enumerate(dps, 1):
                o.append(f"| {i} | {name(spec, b)} | {-d:.0f} | {'best' if i == 1 else gap_text(-d / best - 1)} |")
            o.append("")
        if tanks:
            o += ["**Tanking**: " + ", ".join(name(spec, b) for spec, b in tanks) + ".", ""]
        if heals:
            o += ["**Healing**" + (" (ranked by the healer lab's capacity: the multiple of the lab's standard raid damage the healer keeps "
                                   "up with)" if len(heals) > 1 else "") + ": "
                  + ", ".join(name(spec, b) + (f" (capacity {-c:.2f})" if len(heals) > 1 and c else "") for c, spec, b in heals) + ".", ""]
    else:
        o += ["Not ranked: no simulator plays PvP, so there is nothing fair to rank on. The builds below rest on the talents' descriptions "
              "and the community's PvP builds.", ""]
        o += [f"- {name(spec, b)}: {rs.split_of(cls, rs.flat(b))}" for spec, b in rows]
        o.append("")
    return o


def cell(cls, spec, mode, builds, nums, src, rec=False):
    R, L, H = nums
    ranked = rank_builds(cls, mode, builds, nums)
    page = f"{mode}/{SM.spec_slug(cls, spec)}.md"
    if not ranked:
        other = SM.LEVEL_AS.get((cls, spec)) if mode == "leveling" else None
        return f"[level as {other}]({page})" if other else "-"
    top = ranked[0]
    note = ""
    if mode == "raid":
        if top.get("role") == "healer":
            note = "healer"
        else:
            r = R.get(top["id"]) or {}
            note = "tank" if r.get("tank") else (f"{r['group']:.0f} DPS (raid)" if r.get("group") else "")
    elif mode == "leveling":
        w = weighted(L.get(top["id"]) or {})
        note = f"{w:.0f} s/kill" if w else ""
    gen = mark(top)
    return (f"**{BADGE}**<br>" if rec else "") + f"[{bname(cls, top)}]({page}){gen}" + (f"<br>{note}" if note else "")


def own_rotation_only(cls, g, nums):
    """Leveling builds whose numbers come from another spec's rotation leave their spec's page (user decision 2026-10-08: "I don't want
    classes specs taking other specs rotations or builds or anything just because it's faster"): kept only with a rotation built for the
    spec's tree (a hybrid: either tree). fightlab/own_rotation_race.py gives such builds their own rotation's numbers first."""
    trees_of = SM.leveling_rotation_trees(cls)
    for spec, modes in g.items():
        keep = []
        for b in modes.get("leveling") or []:
            rot = LEVEL_MODEL.get((cls, b["id"]))
            if not weighted(nums[1].get(b["id"]) or {}) or rot is None or rot not in trees_of or SM.rotation_allows(spec, trees_of[rot]):
                keep.append(b)
        modes["leveling"] = keep
    return g


def class_pages(cls):
    B = rr.builds(cls)
    g = SM.grid(cls, list(B.values()))
    nums = (raid_numbers(cls), leveling_numbers(cls), healer_numbers(cls))
    g = own_rotation_only(cls, g, nums)
    # a hybrid gets pages only with a build in a mode the pages show (2026-10-09: the paladin's Shockadin had pages from its PvP build alone)
    specs = SM.trees(cls) + sorted(s for s in g if s.startswith("Hybrid") and any(g[s].get(m) for m in PAGE_MODES))
    rec = {m: recommended(cls, g, specs, m, nums) for m in SM.MODES}
    readme = ROOT / cls / "README.md"
    import shutil
    for gone in set(SM.MODES) - set(PAGE_MODES):   # player pages of a mode no longer shown
        shutil.rmtree(ROOT / cls / gone, ignore_errors=True)
    for mode in PAGE_MODES:
        d = ROOT / cls / mode
        d.mkdir(parents=True, exist_ok=True)
        for old in d.glob("*.md"):
            old.unlink()   # generated folder: pages of specs that no longer have builds go away
        for spec in specs:
            if spec.startswith("Hybrid") and not g[spec][mode]:
                continue   # 2026-10-15 page audit D7: a hybrid's page in a mode it has no build for was a stub no page linked to
            src = d / f"{SM.spec_slug(cls, spec)}.md"
            o = [f"# {spec_title(cls, spec)} — {SM.MODE_TITLE[mode]}", "",
                 f"[{cls.capitalize()}](../README.md) > [{SM.MODE_TITLE[mode]}](README.md) > {SM.spec_name(cls, spec)}", ""]
            if (cls, spec) in SM.HYBRID_NAMES:
                o += [f"*{SM.hybrid_line(cls, spec, mode)}* (a hybrid: {spec.split(' ', 1)[1]}).", ""]   # a line per mode (2026-10-15, audit C5)
            if spec in rec[mode]:
                o += [f"**{BADGE}** for {SM.MODE_TITLE[mode].split(' (')[0].lower()} (the best {cls} spec here, or within {TIE:.0%} of it).", ""]
            o += mode_section(cls, spec, mode, g[spec][mode], nums, src)
            o += ["---", foot(raid_sims(nums[0], {b["id"] for b in g[spec][mode]}) if mode == "raid" else None), ""]
            src.write_text("\n".join(o) + "\n", encoding="utf-8")
        idx = [f"# {cls.capitalize()} — {SM.MODE_TITLE[mode]}", "", f"[{cls.capitalize()}](../README.md) > {SM.MODE_TITLE[mode]}", ""]
        idx += ranking(cls, g, specs, mode, nums)
        if mode == "raid":
            idx += tier_table(cls, specs, d / "README.md")
        idx += [f"{DER_MARK} = a derived build (searched in a simulator). "
                f"{GEN_MARK} = a generated build (no hand-made build for that spec and mode yet). Differences under 2-3% are within the "
                "simulations' noise and assumptions: treat them as a tie.", "", "---", foot(raid_sims(nums[0]) if mode == "raid" else None), ""]
        (d / "README.md").write_text("\n".join(idx) + "\n", encoding="utf-8")
    # the class README: two generated sections on top, the hand-written overview and the research index below
    o = ["## Pick your spec", "",
         "Pick what you want to do (the columns) and the spec you want to play (the rows). Every link opens a page with the talents "
         "(and a link that shows them in a talent calculator), the talent order while leveling, what to press, and the numbers behind the choice.", "",
         "| Spec | Leveling (solo) | Raid (group: full raid DPS) |", "|---|---|---|"]
    for spec in SM.trees(cls):   # the three specs: every cell filled (spec_builds.py)
        o.append(f"| **{SM.spec_name(cls, spec)}** | " + " | ".join(cell(cls, spec, m, g[spec][m], nums, readme, rec=spec in rec[m]) for m in PAGE_MODES) + " |")
    o += ["", f"**{BADGE}**: the best spec for that column, or within {TIE:.0%} of it (a tie in the simulations). "
          f"{DER_MARK}: a derived build (searched in a simulator). "
          f"{GEN_MARK}: a generated build, a starting point until someone drafts that spec by hand.", ""]
    hyb = [spec for spec in specs if spec.startswith("Hybrid")]
    if hyb:
        # hybrids exist for one purpose each (a raid build, a leveling build...): listed apart with only the modes they are built for,
        # so the grid above never shows empty cells (2026-09-30, user report)
        o += ["### Hybrid builds", "", "Builds that spend their points across two trees, each made for a particular job. They are listed only for the "
              "modes they are built for.", "", "| Hybrid | What it is | Builds |", "|---|---|---|"]
        for h in hyb:
            # the line of each mode it is built for, once when they agree (2026-10-15, audit C5: a hybrid's line may differ by mode)
            lines = {m: SM.hybrid_line(cls, h, m) for m in PAGE_MODES if g[h][m]} if (cls, h) in SM.HYBRID_NAMES else {}
            what = (next(iter(lines.values())) if len(set(lines.values())) == 1
                    else "<br>".join(f"{SM.MODE_TITLE[m].split(' (')[0]}: {x}" for m, x in lines.items()) if lines
                    else f"points split between {h.split(' ', 1)[1]}")
            cells = [f"{SM.MODE_TITLE[m].split(' (')[0]}: " + cell(cls, h, m, g[h][m], nums, readme, rec=h in rec[m]).replace("<br>", " · ")
                     for m in PAGE_MODES if g[h][m]]
            o.append(f"| **{SM.spec_name(cls, h)}** | {what} | " + "<br>".join(cells) + " |")
        o.append("")
    o += [f"*Generated by `_reference/data/render_modes.py` on {TODAY}. Do not hand-edit this section.*"]
    readme_sections.splice_ordered(readme, "class", "## Pick your spec", "\n".join(o))
    o = ["## Which spec is best?", ""]
    for m in PAGE_MODES:
        o += [f"### {SM.MODE_TITLE[m]}", ""] + ranking(cls, g, specs, m, nums, prefix=f"{m}/")
    o += ["Differences under 2-3% are within the simulations' noise and assumptions: treat them as a tie. Everything is a simulation of the "
          "beta, not a measurement in the game.", "", f"*Generated by `_reference/data/render_modes.py` on {TODAY}. Do not hand-edit this section.*"]
    readme_sections.splice_ordered(readme, "class", "## Which spec is best?", "\n".join(o))
    old = ROOT / cls / "START-HERE.md"
    if old.exists():
        old.unlink()   # the class README took its place (2026-09-29)
    R, L, H = nums
    best = lambda m, key: sorted(((key(rank_builds(cls, m, g[sp][m], nums)[0]), sp) for sp in rec[m]), key=lambda x: x[0])   # noqa: E731
    lvl = best("leveling", lambda b: weighted(L.get(b["id"]) or {}))
    raid = best("raid", lambda b: -((R.get(b["id"]) or {}).get("group") or 0))
    roles = ["damage"] + (["tank"] if cls in SM.TANK_TREE else []) + (["healer"] if cls in SM.HEAL_TREES else [])
    solo = lambda sp: (R.get(rank_builds(cls, "raid", g[sp]["raid"], nums)[0]["id"]) or {}).get("dps")   # noqa: E731
    tanks, heals = support_picks(cls, g, specs, nums)
    # the tank and healer picks for the index (2026-10-15 page audit B18): (spec, the build's name when it is not the spec page's pick)
    tank_rows = [(sp, None if rank_builds(cls, "raid", g[sp]["raid"], nums)[0]["id"] == b["id"] else bname(cls, b)) for sp, b in tanks]
    return {"cls": cls, "lvl": [(sp, v) for v, sp in lvl], "raid": [(sp, -v, solo(sp)) for v, sp in raid], "roles": roles,
            "tank": tank_rows, "heal": [(sp, -c) for c, sp, _ in heals], "sims": raid_sims(R)}


def root_page(infos):
    o = ["# WoW: Forever class guides", "",
         "The best talents and the best way to play every class in **World of Warcraft: Forever** (the Classic+ release, launching "
         "2026-11-04), worked out from the beta's talent trees and simulations: the community's combat simulator for raids and this "
         "project's own simulators for leveling and healing.", "",
         "**How to use it:** pick your class below. Its page has a grid of every spec against the two modes (leveling, raid), the "
         "recommended picks marked, and a ranking of the specs for each mode. Every link in the grid opens a build page: the talents (with a "
         "talent calculator link), the order to take them while leveling, and what to press.", "",
         "| Class | Roles | Fastest leveling (solo) | Most raid damage (DPS in a full raid) | Raid healing | Raid tanking |",
         "|---|---|---|---|---|---|"]
    for i in infos:
        cls = i["cls"]
        lvl = ", ".join(f"[{SM.spec_name(cls, sp)}]({cls}/leveling/{SM.spec_slug(cls, sp)}.md) ({v:.0f} s/kill)" for sp, v in i["lvl"]) or "-"
        raid = ", ".join(f"[{SM.spec_name(cls, sp)}]({cls}/raid/{SM.spec_slug(cls, sp)}.md) ({v:.0f} DPS)"
                         for sp, v, pv in i["raid"]) or "-"
        # healer and tank picks, as on the class pages (2026-10-15 page audit B18): healers by the healer lab's capacity, tanks listed
        heal = ", ".join(f"[{SM.spec_name(cls, sp)}]({cls}/raid/{SM.spec_slug(cls, sp)}.md)" + (f" (capacity {c:.2f})" if len(i["heal"]) > 1 and c else "")
                         for sp, c in i["heal"]) or "-"
        tank = ", ".join(f"[{SM.spec_name(cls, sp)}]({cls}/raid/{SM.spec_slug(cls, sp)}.md)" + (f" ({n})" if n else "")
                         for sp, n in i["tank"]) or "-"
        o.append(f"| [**{cls.capitalize()}**]({cls}/README.md) | {', '.join(i['roles'])} | {lvl} | {raid} | {heal} | {tank} |")
    o += ["", "Several specs in one damage or leveling cell share the recommendation: each is within 3% of the class's best spec in that "
          "column, a tie in the simulations. Leveling times compare across classes: every class runs in the same fight simulator, solo "
          "against same-level mobs. Raid numbers assume a group: every raid buff and debuff is up, which is where classes that live on raid "
          "buffs (warriors' rage, hunters' and shamans' mana) do their real damage. Healers are ranked within their class by the healer "
          "lab's capacity (this project's healing model; healers are not in the community simulator); tanks are listed, not ranked.", "",
          "## How to read the numbers", "",
          "- **Full raid DPS** (what raid pages rank and recommend on): your personal damage against a raid boss over a 3-minute fight with "
          "every raid buff and debuff up, as in a real raid group. Each spec's raid page shows where its raid gain comes from (mana, armor "
          "debuffs, physical buffs, spell buffs).",
          "- **Seconds per kill** (leveling): a whole kill cycle against same-level mobs, including eating and drinking.",
          f"- **{BADGE}**: the best spec for that mode in its class, or within 3% of it. **{GEN_MARK}**: a generated build (a starting point).",
          "- Everything is a simulation of the beta, not a measurement in the game. Treat differences under 2-3% as a tie.", "",
          "## Everything else", "",
          "- [Tier list](tier-list.md): every spec of every class in S/A/B/C tiers for raid damage and healing (the tanks listed), from "
          "the same picks and numbers as the class pages.",
          "- [Raid DPS rankings by gear tier](_reference/dps-rankings.md): every raid damage spec in pre-BiS and phase-1 BiS gear, in a "
          "full raid, with its best talents and gear for each.",
          "- [_reference/README.md](_reference/README.md): how the project works, its tools and its rules.",
          "- [_reference/](_reference/): cross-class reports (simulator summaries, the talentsforever.com comparison, launch checklists).",
          "- Each class's `research/` folder: every build, report and simulation behind its pages.", "",
          "---", foot([s for i in infos for s in i.get("sims", [])]), ""]
    (ROOT / "README.md").write_text("\n".join(o) + "\n", encoding="utf-8")
    old = ROOT / "START-HERE.md"
    if old.exists():
        old.unlink()


def main():
    classes = [c for c in sys.argv[1:] if c in SM.CLASSES] or SM.CLASSES
    infos = [class_pages(c) for c in classes]
    for i in infos:
        print(f"{i['cls']}: README.md sections and {len(SM.MODES)} mode folders written")
    if classes == SM.CLASSES:
        root_page(infos)
        print("wrote README.md")


if __name__ == "__main__":
    main()
