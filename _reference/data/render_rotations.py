"""Rotations per build and the raid DPS ranking (2026-09-27).

    python _reference/data/render_rotations.py [classes...]

Writes, per class (paths.py):
  <class>/research/raid/rotation.md       per raid spec model: the community simulator's rotation (its APL) filtered to what each build
                                 casts, builds that cast the same lines grouped, with the casts per minute the simulator measured
                                 on the training dummy (tanks: the raid setting). Our builds and the simulator's own builds.
  <class>/research/leveling/rotation.md   per fight-lab report: the priority the fight lab plays and what each leveling build casts per
                                 kill at every level bracket, with damage shares.
  "## DPS ranking" of <class>/research/raid/README.md and "## Raid DPS ranking" of <class>/README.md: our builds and the simulator's own
                                 builds per spec model, by training-dummy DPS with the raid-setting DPS next to it (tanks: tank value).
It also gives render_builds.py the rotation and rank sections of the build pages (build_sections()). Reads the raid-sim reports
(`raidsim/run.py --write`: casts per build), the environments reports and the fight-lab reports; changes nothing else.
"""
import argparse
import datetime
import functools
import importlib.util
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import paths  # noqa: E402
import readme_sections as rs  # noqa: E402

CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
MIN_CPM = 0.05   # a line cast less than once in 20 minutes counts as not cast


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@functools.lru_cache(maxsize=None)
def raidrun():
    sys.path.insert(0, str(HERE / "scorer"))
    m = _load("raidrun", HERE / "raidsim" / "run.py")
    m.set_game("forever")
    return m


@functools.lru_cache(maxsize=None)
def presets_mod():
    return _load("render_sim_presets_mod", HERE / "render_sim_presets.py")


@functools.lru_cache(maxsize=None)
def repo():
    return raidrun().repo_path(argparse.Namespace(repo=None))


@functools.lru_cache(maxsize=None)
def names():
    return presets_mod().Names(repo())


def raid_specs(cls):
    specs = json.load(open(HERE / "raidsim" / "specs.json", encoding="utf-8"))
    return [(s, e) for s, e in (specs.get(cls) or {}).items() if isinstance(e, dict) and "apl" in e]


def _json(p):
    return json.load(open(p, encoding="utf-8")) if p.exists() else None


@functools.lru_cache(maxsize=None)
def builds(cls):
    p = paths.builds_json("forever", cls)
    return {b["id"]: b for b in json.load(open(p, encoding="utf-8"))["builds"]} if p.exists() else {}


def made_by(cls, label):
    if label.startswith("sim preset: "):
        return "community simulator"
    if label.endswith("-parse"):
        return "ours: parse build"
    if label.startswith("opt-"):
        return "ours: optimizer"
    return "ours: hand draft" if label in builds(cls) else "ours"


def label_md(cls, label, src=None):
    """A build's name in a table: a link to its page for ours, the simulator's name for theirs."""
    if label.startswith("sim preset: "):
        return f"*{label[len('sim preset: '):]}*"
    page = paths.build_page_by_id("forever", cls, label)
    return f"[`{label}`]({paths.rel(src, page)})" if (page and src) else f"`{label}`"


# ------------------------------------------------------------------------------------------------ raid: the simulator's data
@functools.lru_cache(maxsize=None)
def trees(cls):
    return raidrun().load_trees(repo(), cls)


def decode(cls, talents):
    """The simulator's talent string -> {talent: rank} (both ours and the presets use the same trees)."""
    out = {}
    for tr, part in zip(trees(cls), (talents or "").split("-")):
        for t, ch in zip(tr["talents"], part):
            if ch != "0":
                out[t.get("fancyName") or t["fieldName"]] = int(ch)
    return out


def talent_of_spell(cls, entry):
    """{spell id: the talent that grants it} from the simulator's spell data (a talent's ability or proc aura carries its name)."""
    sd = raidrun().spelldata_names(repo(), entry)
    pascal = {}
    for tr in trees(cls):
        for t in tr["talents"]:
            f = t.get("fieldName") or ""
            pascal[f[:1].upper() + f[1:]] = t.get("fancyName") or f
    out = {}
    for sid, nm in sd.items():
        if nm in pascal:
            out[sid] = pascal[nm]
        else:
            for suf in raidrun().AURA_SUFFIXES:
                if nm.endswith(suf) and nm[: -len(suf)] in pascal:
                    out[sid] = pascal[nm[: -len(suf)]]
    return out


def spell_ids(x):
    """Spell ids an APL action casts (its castSpell / multidot / sequence contents; conditions are not casts)."""
    ids = []
    if isinstance(x, dict):
        for k, v in x.items():
            if k == "condition":
                continue
            if k in ("castSpell", "castFriendlySpell", "multidot", "multishield") and isinstance(v, dict):
                sid = (v.get("spellId") or {}).get("spellId")
                if sid:
                    ids.append(int(sid))
            ids += spell_ids(v)
    elif isinstance(x, list):
        for v in x:
            ids += spell_ids(v)
    return ids


@functools.lru_cache(maxsize=None)
def spec_data(cls, spec, setting="dummy"):
    """Everything the raid pages need for one spec model: the rotation lines and, per build, its lines, casts and damage.
    setting "raid" (2026-10-02, user decision: raid pages are about the group setting): the entry's raid rotation, each line's use from
    the build's casts in the environments run's raid column (falls back to the dummy race's casts for a report without them), rows ranked
    by full-raid DPS. Tanks always use the race (their race runs in the raid setting)."""
    entry = dict(raid_specs(cls))[spec]
    rep = _json(paths.raidsim_dir(cls) / f"{spec}.json")
    if not rep:
        return None
    env = _json(paths.raidsim_dir(cls) / f"{spec}-environments.json") or {"results": []}
    env_by = {x["label"]: x["dps"] for x in env["results"]}
    env_casts = {x["label"]: x.get("raid_spell_casts") for x in env["results"] if x.get("raid_spell_casts")}
    raid_view = setting == "raid" and not entry.get("tank") and bool(env_casts)
    apl = json.load(open(raidrun().apl_path(entry, repo(), "raid" if raid_view else None), encoding="utf-8"))   # ours when apl_opt.py found a better one
    N = names()
    pm = presets_mod()
    lines = [{"text": pm.action(it.get("action", {}), N), "ids": spell_ids(it.get("action", {})),
              "kind": next(iter(k for k in it.get("action", {}) if k != "condition"), "")}
             for it in apl.get("priorityList", []) if not it.get("hide")]
    pre = [(p.get("doAtValue", {}).get("const", {}).get("val"), pm.action(p.get("action", {}), N)) for p in apl.get("prepullActions") or []]
    grant = talent_of_spell(cls, entry)
    dur = float(rep["sim"].get("duration") or 120.0)
    tank = any(x.get("value") is not None for x in rep["results"])
    rows = []
    for x in rep["results"]:
        if x.get("removal") or x["label"].startswith("cand-") or not x.get("dps"):
            continue
        casts = {int(k): v for k, v in ((env_casts.get(x["label"]) if raid_view else None) or x.get("spell_casts") or {}).items()}
        alloc = decode(cls, x.get("talents"))
        per_line = []
        for ln in lines:
            if not ln["ids"]:
                per_line.append({"used": True, "cpm": None, "why": ""})
                continue
            cpm = sum(casts.get(i, 0.0) for i in ln["ids"]) / dur * 60
            need = [grant[i] for i in ln["ids"] if i in grant and grant[i] not in alloc]
            per_line.append({"used": cpm >= MIN_CPM, "cpm": cpm, "why": f"needs the {need[0]} talent" if need else "its condition never held in these fights"})
        rows.append({"label": x["label"], "by": made_by(cls, x["label"]), "split": x.get("split") or "", "dps": x["dps"], "value": x.get("value"),
                     "threat": x.get("threat"), "dtps": x.get("dtps"), "oom": x.get("oom_seconds"), "shares": x.get("shares") or {},
                     "raid": (env_by.get(x["label"]) or {}).get("raid"), "lines": per_line})
    key = (lambda r: -(r["value"] or 0)) if tank else ((lambda r: -(r["raid"] or r["dps"] or 0)) if raid_view else (lambda r: -(r["dps"] or 0)))
    rows.sort(key=key)
    return {"spec": spec, "entry": entry, "apl": raidrun().apl_label(entry, repo(), "raid" if raid_view else None), "lines": lines, "pre": pre, "rows": rows,
            "tank": tank, "view": "raid" if raid_view else "dummy",
            "setting": rep["sim"].get("setting", "raid"), "commit": rep["sim"].get("commit", "?"), "iterations": rep["sim"].get("iterations"), "duration": dur}


# ------------------------------------------------------------------------------------------------ rotation searches
def raid_search(cls, spec):
    """{setting: record} from raidsim/apl_opt.py (the raid rotation search), or {}."""
    rec = _json(paths.raidsim_dir(cls) / f"{spec}-rotation-search.json") or {}
    return {rec.get("setting", "dummy"): rec} if "changes" in rec else rec


def raid_tuning_lines(cls, spec, setting):
    """What the rotation search did to a spec's rotation in one kind of setting, for a page."""
    rec = raid_search(cls, spec).get(setting)
    where = "the training dummy" if setting == "dummy" else "a fully buffed raid"
    if not rec:
        return [f"- **{where.capitalize()}:** the simulator's own rotation (no rotation search recorded)."]
    fin = rec.get("final", {}).get(setting, {})
    gains = ", ".join(f"{b} {v['before']:.0f} -> {v['after']:.0f} DPS ({v['after'] / v['before'] - 1:+.1%})" for b, v in fin.items() if v.get("before") and v.get("after"))
    if not rec.get("changes"):
        return [f"- **{where.capitalize()}:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds "
                f"(`raidsim/apl_opt.py`, {rec.get('date', '?')})."]
    passes = rec.get("passes", 1)
    when = f"{rec.get('first_date', rec.get('date', '?'))}, {passes} passes, the last {rec.get('date', '?')}" if passes > 1 else rec.get("date", "?")
    o = [f"- **{where.capitalize()}:** our tuned rotation (`raidsim/apl_opt.py`, {when}, {len(rec['changes'])} changes to the base rotation; "
         f"third-seed check: {gains}):"]
    for c in rec["changes"]:
        g2, g1 = c.get("gain_seed2"), c.get("gain_seed1")   # a rotation adopted whole (the open search's cross-race) records one seed only
        gain = f"{g2:+.1%}" if isinstance(g2, (int, float)) else (f"{g1:+.1%} on one seed" if isinstance(g1, (int, float)) else "gain not re-measured")
        o.append(f"  {c['round']}. {c['change']} ({gain}" + (f", pass {c['pass']}" if passes > 1 else "") + ")")
    return o


def fl_rotation(cls, spec):
    p = HERE / "fightlab" / "rotations" / f"{cls}-{spec}.json"
    return _json(p) if p.exists() else None


def fl_tuning_text(cls, spec):
    r = fl_rotation(cls, spec)
    if not r or not r.get("changes"):
        return None
    rules = "; ".join(c["change"] for c in r["changes"])
    return (f"**Tuned rules** (`fightlab/rotation_opt.py`, {r.get('date', '?')}, on top of the priority below): {rules}. Together "
            f"{1 - r['weighted_after'] / r['weighted_before']:+.1%} time per kill saved for `{r['build']}` (level-weighted, a third seed "
            f"of {r.get('confirm', '?')} fights per level).")


# ------------------------------------------------------------------------------------------------ raid: ranking tables
def ranking_table(cls, d, src, highlight=None):
    rows = d["rows"]
    o = []
    if d["tank"]:
        best = rows[0]["value"] or 1.0
        o += ["| Rank | Build | By | Split | Tank value | vs best | Threat/s | Damage taken/s |", "|---|---|---|---|---|---|---|---|"]
        for i, r in enumerate(rows, 1):
            name = label_md(cls, r["label"], src)
            name = f"**{name}**" if r["label"] == highlight else name
            o.append(f"| {i} | {name} | {r['by']} | {r['split'] or '-'} | {(r['value'] or 0):.3f} | {((r['value'] or 0) - best) / best * 100:+.1f}% | "
                     f"{(r['threat'] or 0):.0f} | {(r['dtps'] or 0):.0f} |")
        return o
    best = rows[0]["dps"] or 1.0
    best_raid = max((r["raid"] or 0 for r in rows), default=0) or 1.0
    o += ["| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |", "|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        name = label_md(cls, r["label"], src)
        name = f"**{name}**" if r["label"] == highlight else name
        raid = f"{r['raid']:.0f} | {(r['raid'] - best_raid) / best_raid * 100:+.1f}%" if r["raid"] else "- | -"
        oom = f"{r['oom']:.0f} s" if r.get("oom") is not None else "-"
        o.append(f"| {i} | {name} | {r['by']} | {r['split'] or '-'} | {r['dps']:.0f} | {(r['dps'] - best) / best * 100:+.1f}% | {raid} | {oom} |")
    return o


def ranking_section(cls):
    readme = paths.scenario_readme(cls, "raid")
    o = ["## DPS ranking", "",
         "Our builds and the community simulator's own builds, run through the same simulator with the same gear and rotation "
         "(ElliotWood/Forever). DPS specs are ranked on the boss-level training dummy with only your own buffs; the raid column is the same "
         "build in a fully buffed raid. Tanks are ranked by tank value in the raid setting (threat and damage taken, relative to our tank draft). "
         "The rotation each build plays is on the [rotation page](rotation.md). Simulations of the community's model of the beta, not "
         f"measurements. Generated by `_reference/data/render_rotations.py` on {datetime.date.today().isoformat()}.", ""]
    n = 0
    for spec, _ in raid_specs(cls):
        d = spec_data(cls, spec)
        if not d or not d["rows"]:
            continue
        n += 1
        o += [f"**{spec}**" + (" (tank)" if d["tank"] else ""), ""] + ranking_table(cls, d, readme) + [""]
    if not n:
        o += ["No raid spec of this class runs in the community simulator (healers are measured in the healer lab).", ""]
    return "\n".join(o)


def class_ranking_section(cls):
    readme = ROOT / cls / "README.md"
    o = ["## Raid DPS ranking", "",
         "The top build of every raid spec on the training dummy and in a fully buffed raid, ours or the community simulator's "
         f"([full ranking]({paths.rel(readme, paths.scenario_readme(cls, 'raid'))}), generated by `_reference/data/render_rotations.py`).", "",
         "| Spec model | Best on the training dummy | DPS | Best in a raid | DPS |", "|---|---|---|---|---|"]
    n = 0
    for spec, _ in raid_specs(cls):
        d = spec_data(cls, spec)
        if not d or not d["rows"] or d["tank"]:
            continue
        n += 1
        b = d["rows"][0]
        br = max(d["rows"], key=lambda r: r["raid"] or 0)
        o.append(f"| {spec} | {label_md(cls, b['label'], readme)} ({b['by']}) | {b['dps']:.0f} | {label_md(cls, br['label'], readme)} ({br['by']}) | "
                 + (f"{br['raid']:.0f}" if br["raid"] else "-") + " |")
    if not n:
        return None
    return "\n".join(o)


# ------------------------------------------------------------------------------------------------ raid: rotations
def _groups(d):
    groups = {}
    for r in d["rows"]:
        k = tuple(i for i, pl in enumerate(r["lines"]) if pl["used"])
        groups.setdefault(k, []).append(r)
    return list(groups.items())


def rotation_block(cls, d, rows, src, heading="###"):
    """The priority lines a group of builds casts, with each build's casts per minute; the lines they skip and why; damage shares."""
    used = [i for i, pl in enumerate(rows[0]["lines"]) if pl["used"]]
    o = []
    if d["pre"]:
        o.append("Before the pull: " + "; ".join((f"at {t}: " if t else "") + a for t, a in d["pre"]) + ".")
        o.append("")
    head = "| # | Priority (the first line whose condition holds is cast) | " + " | ".join(label_md(cls, r["label"], src) + " casts/min" for r in rows) + " |"
    o += [head, "|---|---|" + "---|" * len(rows)]
    for n, i in enumerate(used, 1):
        cells = []
        for r in rows:
            c = r["lines"][i]["cpm"]
            cells.append(f"{c:.1f}" if c is not None else "as ready")
        o.append(f"| {n} | {d['lines'][i]['text']} | " + " | ".join(cells) + " |")
    skipped = {}
    for i, pl in enumerate(rows[0]["lines"]):
        if not pl["used"]:
            skipped.setdefault(pl["why"], []).append(d["lines"][i]["text"])
    if skipped:
        o.append("")
        o.append("Lines of the simulator's rotation these builds never cast: " + "; ".join(
            f"{', '.join(dict.fromkeys(t.split(': ', 1)[-1] for t in texts))} ({why})" for why, texts in skipped.items()) + ".")
    abil = []
    for r in rows:
        for k in r["shares"]:
            if k not in abil:
                abil.append(k)
    top = sorted(abil, key=lambda k: -max(r["shares"].get(k, 0) for r in rows))[:10]
    if top:
        o += ["", "Damage by ability" + (" (threat for tanks)" if d["tank"] else "") + ":", "",
              "| Ability | " + " | ".join(label_md(cls, r["label"], src) for r in rows) + " |", "|---|" + "---|" * len(rows)]
        for k in top:
            o.append(f"| {k} | " + " | ".join(f"{r['shares'].get(k, 0) * 100:.0f}%" for r in rows) + " |")
    return o


def raid_rotation_page(cls):
    page = paths.rotation_page(cls, "raid")
    o = [f"# {cls.title()} — raid rotations (generated)", "",
         f"> Generated by `_reference/data/render_rotations.py` on {datetime.date.today().isoformat()} from the ElliotWood/Forever simulator's "
         "rotation files and its runs of every build: each build's rotation is the simulator's priority list with the lines that build never "
         "casts removed, and the casts per minute measured on the training dummy (tanks: in the raid setting). Our builds and the simulator's own "
         "builds; builds that cast the same lines share a table. A line's condition reads left to right (spell names from the simulator's "
         "database). The leveling priority the fight lab plays is on the [leveling rotation page](../leveling/rotation.md). Models of the beta, "
         "not measurements. Do not hand-edit.", ""]
    n = 0
    for spec, entry in raid_specs(cls):
        d = spec_data(cls, spec)
        if not d or not d["rows"]:
            continue
        n += 1
        ours = d["apl"].startswith("_reference/")
        base_ours = entry["apl"].startswith("_reference/")   # our own base rotation (the note below says what it adds)
        o += [f"## {spec}" + (" (tank)" if d["tank"] else ""), "",
              (f"Our rotation `{pathlib.Path(d['apl']).name}`" + (f" (our base rotation `{pathlib.Path(entry['apl']).name}` with the changes below)"
                                                                  if pathlib.Path(d["apl"]).name != pathlib.Path(entry["apl"]).name else "") if base_ours
               else f"Our tuned rotation `{pathlib.Path(d['apl']).name}` (the simulator's `{pathlib.Path(entry['apl']).name}` with the changes below)" if ours
               else f"The simulator's rotation file `{pathlib.Path(d['apl']).name}`")
              + f" (commit {d['commit']}), {d['iterations']} fights of {d['duration']:.0f} s per build "
              + ("on the training dummy." if d["setting"] == "dummy" else "in the raid setting.") + " Ranking: [raid README](README.md).", ""]
        if entry.get("rotation_note"):
            o += [entry["rotation_note"], ""]
        o += ["**Rotation search** (every change kept had to win on two random seeds and cost none of the tuning builds more than 0.1%):", ""]
        o += (raid_tuning_lines(cls, spec, "raid") if d["tank"] else raid_tuning_lines(cls, spec, "dummy") + raid_tuning_lines(cls, spec, "raid")) + [""]
        raid_apl = raidrun().apl_path(entry, repo(), "raid")
        if not d["tank"] and raid_apl != raidrun().apl_path(entry, repo(), "dummy"):
            pm = presets_mod()
            N = names()
            ra = json.load(open(raid_apl, encoding="utf-8"))
            o += ["The raid rotation (a fully buffed raid: Blessing of Wisdom and Mana Spring change what mana is worth), top priority first:", ""]
            o += [f"{i}. {pm.action(it.get('action', {}), N)}" for i, it in enumerate([x for x in ra.get("priorityList", []) if not x.get("hide")], start=1)] + [""]
            o += ["The tables below are the training-dummy rotation, filtered per build:", ""]
        for k, rows in _groups(d):
            o += [f"### " + ", ".join(label_md(cls, r["label"], page) + f" ({r['by']}, {r['dps']:.0f} DPS)" for r in rows), ""]
            o += rotation_block(cls, d, rows, page) + [""]
    if not n:
        o += ["No raid spec of this class runs in the community simulator: healers are measured in the healer lab, whose priorities are in "
              "`_reference/data/heallab/`.", ""]
    return "\n".join(o).rstrip("\n") + "\n"


# ------------------------------------------------------------------------------------------------ leveling
@functools.lru_cache(maxsize=None)
def fl_module(cls):
    sys.path.insert(0, str(HERE / "fightlab"))
    fr = _load("fightlab_run_for_rotations", HERE / "fightlab" / "run.py")
    return __import__(fr.MODULES[cls][0])


SPECIAL = {("shaman", "elemental-dps"): "decide_elemental", ("druid", "balance-dps"): "decide_balance", ("hunter", "melee-dps"): "decide_melee"}


def fl_description(cls, spec, aoe=False):
    cm = fl_module(cls)
    fn = SPECIAL.get((cls, spec))
    txt = None
    if fn:
        for c in [v for v in vars(cm).values() if isinstance(v, type)]:
            if hasattr(c, fn) and getattr(c, fn).__doc__:
                txt = " ".join(getattr(c, fn).__doc__.split())
                break
    txt = txt or cm.DESCRIPTION
    if aoe:
        txt = ("Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the "
               "single-target priority below. " + txt)
    return txt


def fl_reports(cls):
    out = []
    for p in sorted(paths.fightlab_dir(cls).glob("*.json")):
        if p.name.endswith("-calibration.json"):
            continue
        r = _json(p)
        if r and r.get("levels"):
            out.append((p, r))
    return out


def fl_build_table(r, bid, per):
    levels = sorted(per, key=int)
    abil = []
    for L in levels:
        for k in per[L].get("casts") or {}:
            if k not in abil:
                abil.append(k)
    top = levels[-1]
    kills = {L: max(per[L].get("kills") or 1, 1) for L in levels}
    abil.sort(key=lambda k: -(per[top].get("casts") or {}).get(k, 0))
    o = ["| Ability | " + " | ".join(f"L{L} casts/kill" for L in levels) + f" | Damage at L{top} |", "|---|" + "---|" * (len(levels) + 1)]
    for k in abil:
        cells = [f"{(per[L].get('casts') or {}).get(k, 0) / kills[L]:.1f}" for L in levels]
        o.append(f"| {k} | " + " | ".join(cells) + f" | {(per[top].get('shares') or {}).get(k, 0) * 100:.0f}% |")
    return o


def leveling_rotation_page(cls):
    page = paths.rotation_page(cls, "leveling")
    o = [f"# {cls.title()} — leveling rotations (generated)", "",
         f"> Generated by `_reference/data/render_rotations.py` on {datetime.date.today().isoformat()} from the fight lab (`_reference/data/fightlab/`): "
         "the priority each class module plays against same-level mobs, and what every simulated leveling build casts per kill at each level "
         "bracket (talent abilities appear from the level the build takes them). A model of the beta, not a measurement. Do not hand-edit.", ""]
    for p, r in fl_reports(cls):
        spec = r["spec"]
        aoe = p.stem.endswith("-aoe")
        o += [f"## {spec}" + (" in pulls of several mobs" if aoe else ""), "", fl_description(cls, spec, aoe), ""]
        if fl_tuning_text(cls, spec):
            o += [fl_tuning_text(cls, spec), ""]
        o += [f"Report: [fightlab/{p.stem}.md](fightlab/{p.stem}.md).", ""]
        for bid, per in [(r["build"], r["levels"])] + list(r.get("compare", {}).items()):
            if not per:
                continue
            o += [f"### {label_md(cls, bid, page)}", ""] + fl_build_table(r, bid, per) + [""]
    return "\n".join(o).rstrip("\n") + "\n"


# ------------------------------------------------------------------------------------------------ build pages
@functools.lru_cache(maxsize=None)
def build_index(cls):
    """build id -> ('raid', spec) for builds in a raid report, and -> ('leveling', report path) for builds in a fight-lab report."""
    idx = {}
    for spec, _ in raid_specs(cls):
        d = spec_data(cls, spec)
        for r in (d or {}).get("rows", []):
            idx.setdefault(("raid", r["label"]), spec)
    for p, r in fl_reports(cls):
        for bid in [r["build"]] + list(r.get("compare", {})):
            idx.setdefault(("leveling", bid), p)
    return idx


def build_sections(cls, build):
    """Markdown sections for a Forever build page: its DPS rank and rotation (raid) or its leveling rotation."""
    page = paths.build_page("forever", cls, build)
    bid = build["id"]
    idx = build_index(cls)
    o = []
    spec = idx.get(("raid", bid))
    if spec:
        d = spec_data(cls, spec)
        r = next(x for x in d["rows"] if x["label"] == bid)
        rank = [x["label"] for x in d["rows"]].index(bid) + 1
        what = "tank value" if d["tank"] else "training-dummy DPS"
        o += ["## Rank among our builds and the community simulator's", "",
              f"**{rank} of {len(d['rows'])}** for `{spec}` by {what} in the community simulator (ElliotWood/Forever {d['commit']}); "
              f"full ranking and the other builds' rotations: [raid README]({paths.rel(page, paths.scenario_readme(cls, 'raid'))}), "
              f"[raid rotations]({paths.rel(page, paths.rotation_page(cls, 'raid'))}).", ""] + ranking_table(cls, d, page, highlight=bid) + [""]
        o += ["## Rotation (community simulator, " + ("training dummy" if d["setting"] == "dummy" else "raid setting") + ")", ""]
        o += (raid_tuning_lines(cls, spec, "raid") if d["tank"] else raid_tuning_lines(cls, spec, "dummy") + raid_tuning_lines(cls, spec, "raid")) + [""]
        o += rotation_block(cls, d, [r], page) + [""]
    lp = idx.get(("leveling", bid))
    if lp:
        r = _json(lp)
        per = r["levels"] if r["build"] == bid else r["compare"][bid]
        o += ["## Leveling rotation (fight lab)", "", fl_description(cls, r["spec"], lp.stem.endswith("-aoe")), ""]
        if fl_tuning_text(cls, r["spec"]):
            o += [fl_tuning_text(cls, r["spec"]), ""]
        o += [
              f"What this build casts per kill ([report]({paths.rel(page, lp.with_suffix('.md'))}), all leveling builds: "
              f"[leveling rotations]({paths.rel(page, paths.rotation_page(cls, 'leveling'))})):", ""] + fl_build_table(r, bid, per) + [""]
    if not o and paths.scenario_of(build) == "leveling":
        o += ["## Leveling rotation", "", "Not simulated in the fight lab; the class's leveling priority is on the "
              f"[leveling rotation page]({paths.rel(page, paths.rotation_page(cls, 'leveling'))}).", ""]
    if not o and paths.scenario_of(build) == "raid":
        o += ["## Rotation", "", ("A healer: not in the community simulator, see the healer lab section of the "
                                  if build.get("role") == "healer" else "Not simulated in the community simulator (no spec model of this playstyle there); see the ")
              + f"[raid README]({paths.rel(page, paths.scenario_readme(cls, 'raid'))}).", ""]
    return "\n".join(o)


# ------------------------------------------------------------------------------------------------ main
def main():
    classes = [c for c in (sys.argv[1:] or CLASSES) if c in CLASSES]
    for cls in classes:
        rp = paths.rotation_page(cls, "raid")
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text(raid_rotation_page(cls), encoding="utf-8")
        lp = paths.rotation_page(cls, "leveling")
        lp.parent.mkdir(parents=True, exist_ok=True)
        lp.write_text(leveling_rotation_page(cls), encoding="utf-8")
        rs.splice_ordered(paths.scenario_readme(cls, "raid"), "raid", "## DPS ranking", ranking_section(cls))
        # the class README's ranking is render_modes.py's "Which spec is best?" since 2026-09-29
        rs.drop(ROOT / cls / "README.md", "## Raid DPS ranking")
        print(f"{cls}: raid and leveling rotations, DPS ranking written")


if __name__ == "__main__":
    main()
