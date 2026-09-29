"""Buff / nerf report: what every talent is worth in Classic vs WoW: Forever, per class.

For each Forever talent (and each Classic talent that disappeared) the report lists

* the tree/row/rank change (from the Forever data's `status` and `diff` fields),
* the encoded effects at max rank in both games (parsed from tooltips or hand-entered),
* the model's marginal value of the fully-ranked talent from an empty tree in every spec/profile the class
  has optimizer output for, in both games, and a verdict: **buff** / **nerf** / **reworked** / **new** /
  **removed** / **same** (per-point value ratio Forever/Classic in the talent's best Classic profile; >1.10 buff,
  <0.90 nerf).

It also compares each Forever `opt-<spec>-<profile>` build with the Classic reference build it was calibrated
against, listing the Classic core talents the Forever build drops and the Forever talents it adds - the
"builds that had to change" list.

    python _reference/data/scorer/compare_effects.py [class ...]

Writes `_reference/data/scorer/changes/<class>.md` and `changes/README.md`.
"""
import pathlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))   # _reference/data: paths.py
import paths  # noqa: E402

from effects import CLASSES, load_effects, load_tree  # noqa: E402
from model import Evaluator, effects_for, load_profiles, load_specs  # noqa: E402

# Classic reference build used to calibrate each Forever (spec, profile) pair.
REFERENCE = {
    ("hunter", "bm-leveling", "leveling-st"): "leveling-beast-mastery",
    ("hunter", "bm-leveling", "solo-60"): "leveling-beast-mastery",
    ("hunter", "mm-raid", "raid-dps"): "bm-mm-raid",
    ("hunter", "mm-lonewolf-raid", "raid-dps"): "bm-mm-raid",
    ("mage", "frost-raid", "raid-dps"): "frost-winters-chill-raid",
    ("mage", "frost-raid", "raid-dps-extwc"): "frost-arcane-power-raid",
    ("mage", "fire-raid", "raid-dps"): "fire-raid",
    ("mage", "frost-aoe", "leveling-aoe"): "leveling-frost",
    ("mage", "frost-leveling", "leveling-st"): "leveling-frost",
    ("mage", "fire-leveling", "leveling-st"): "leveling-frost",
    ("warrior", "fury-dw-raid", "raid-dps"): "fury-dw-raid",
    ("warrior", "arms-2h-raid", "raid-dps"): "fury-2h-raid",
    ("warrior", "prot-tank", "raid-tank"): "prot-raid-tank",
    ("warrior", "arms-2h-raid", "leveling-st"): "leveling-arms",
    ("warrior", "fury-dw-raid", "solo-60"): "leveling-arms",
    ("rogue", "combat-swords-raid", "raid-dps"): "combat-swords-raid",
    ("rogue", "combat-daggers-raid", "raid-dps"): "combat-daggers-raid",
    ("rogue", "combat-swords-raid", "leveling-st"): "leveling-combat-swords",
    ("rogue", "combat-daggers-raid", "leveling-st"): "leveling-combat-swords",
    ("rogue", "combat-swords-raid", "solo-60"): "leveling-combat-swords",
    ("priest", "holy-heal", "raid-heal"): "holy-raid-healer",
    ("priest", "shadow-dps", "raid-dps"): "leveling-shadow",
    ("priest", "shadow-dps", "leveling-st"): "leveling-shadow",
    ("priest", "shadow-dps", "solo-60"): "leveling-shadow",
    ("paladin", "holy-heal", "raid-heal"): "holy-raid-healer",
    ("paladin", "ret-dps", "raid-dps"): "ret-raid-dps",
    ("paladin", "prot-tank", "raid-tank"): "prot-tank",
    ("paladin", "ret-dps", "leveling-st"): "leveling-retribution",
    ("paladin", "ret-dps", "solo-60"): "leveling-retribution",
    ("shaman", "resto-heal", "raid-heal"): "resto-raid-healer",
    ("shaman", "elemental-dps", "raid-dps"): "elemental-raid-dps",
    ("shaman", "enhancement-dps", "raid-dps"): "enhancement-raid-support",
    ("shaman", "enhancement-dps", "leveling-st"): "leveling-enhancement",
    ("shaman", "elemental-dps", "leveling-st"): "leveling-enhancement",
    ("shaman", "enhancement-dps", "solo-60"): "leveling-enhancement",
    ("warlock", "sb-raid", "raid-dps"): "ds-ruin-raid",
    ("warlock", "affliction-raid", "raid-dps"): "sm-ruin-raid",
    ("warlock", "fire-destro-raid", "raid-dps"): "ds-ruin-raid",
    ("warlock", "affliction-leveling", "leveling-st"): "leveling-affliction-demo",
    ("warlock", "affliction-leveling", "solo-60"): "leveling-affliction-demo",
    ("druid", "resto-heal", "raid-heal"): "resto-swiftmend-healer",
    ("druid", "feral-cat-dps", "raid-dps"): "feral-cat-dps",
    ("druid", "feral-bear-tank", "raid-tank"): "feral-bear-tank",
    ("druid", "balance-dps", "raid-dps"): "balance-moonkin-raid",
    ("druid", "feral-cat-dps", "leveling-st"): "leveling-feral",
    ("druid", "balance-dps", "leveling-st"): "leveling-feral",
    ("druid", "feral-cat-dps", "solo-60"): "leveling-feral",
}


def pairs_for(cls):
    """(spec, profile) pairs with Forever optimizer output."""
    out = []
    files = sorted(p for sc in paths.SCENARIOS for p in (paths.scenario_dir(cls, sc) / "optimizer").glob("*.md"))
    if not files:
        return out
    specs = load_specs(cls)
    profiles = load_profiles()
    for f in files:
        stem = f.stem
        for spec in sorted(specs, key=len, reverse=True):
            if stem.startswith(spec + "-") and stem[len(spec) + 1:] in profiles:
                out.append((spec, stem[len(spec) + 1:]))
                break
    return out


def fmt_effects(entry):
    """Max-rank encoded effects as a short string."""
    parts = []
    for e in entry["effects"]:
        vals = e.get("values") or []
        if not vals:
            continue
        v = vals[-1]
        scope = ",".join(s for s in e["scope"] if not s.startswith("unknown:")) or e["scope"][0]
        if e["channel"] in ("cast_time", "cooldown", "resource_cost"):
            s = f"{e['channel']} {scope} {v:g}s" if e["channel"] != "resource_cost" else f"{e['channel']} {scope} {v:g}"
        elif e["channel"] in ("disable", "enable"):
            s = f"{e['channel']} {scope}"
        else:
            s = f"{e['channel']} {scope} {v * 100:+.1f}%"
        if e.get("modes"):
            s += f" [{'/'.join(e['modes'])}]"
        if e.get("requires"):
            s += " (needs " + ", ".join(f"{k} {r}" for k, r in e["requires"].items()) + ")"
        parts.append(s)
    return "; ".join(parts) if parts else "-"


def talent_value(ev, merged, name, rank):
    if name not in merged:
        return 0.0
    return ev.score(effects_for({name: rank}, merged))


def build_alloc(build):
    return {t: p for tree in build["allocation"].values() for t, p in tree}


def load_builds(path):
    if not path.exists():
        return {}
    return {b["id"]: b for b in json.load(open(path, encoding="utf-8"))["builds"]}


def report(cls):
    ftree = load_tree("forever", cls)
    ctree = load_tree("classic-era", cls)
    fflat = {n: (tn, x) for tn, d in ftree.items() for n, x in d.items()}
    cflat = {n: (tn, x) for tn, d in ctree.items() for n, x in d.items()}
    fraw = json.load(open(HERE.parent / "forever-talents" / f"{cls}.json", encoding="utf-8"))
    meta = {t["name"]: t for tr in fraw["trees"] for t in tr["talents"]}
    fx = load_effects("forever", cls)
    cx = load_effects("classic-era", cls)
    specs = load_specs(cls)
    profiles = load_profiles()
    pairs = pairs_for(cls)
    evs = {}
    for spec, prof in pairs:
        p = dict(profiles[prof]); p["id"] = prof
        evs[(spec, prof)] = (Evaluator(dict(specs[spec], id=spec), p, 60, "forever"), Evaluator(dict(specs[spec], id=spec), p, 60, "classic-era"))

    rows = []
    counts = {"buff": 0, "nerf": 0, "reworked": 0, "new": 0, "removed": 0, "same": 0, "unscored": 0}
    for name, (tname, x) in sorted(fflat.items(), key=lambda kv: (kv[1][0], kv[1][1]["row"], kv[0])):
        m = meta.get(name, {})
        status = m.get("status", x.get("status", "?"))
        diff = "; ".join(m.get("diff", [])) if m.get("diff") else ""
        fmax = x["max"]
        cmax = cflat[name][1]["max"] if name in cflat else 0
        vals = []
        best_c = (0.0, None)
        for key, (evf, evc) in evs.items():
            vf = talent_value(evf, fx, name, fmax)
            vc = talent_value(evc, cx, name, cmax) if cmax else 0.0
            vals.append((key, vc, vf))
            if vc > best_c[0]:
                best_c = (vc, key)
        if status == "new" or name not in cflat:
            verdict = "new"
        else:
            if best_c[1] is None:
                vf_best = max((vf for _, _, vf in vals), default=0.0)
                verdict = "unscored" if vf_best <= 0.0005 else "reworked"
            else:
                vc = best_c[0]
                vf = dict(((k, f) for k, _, f in vals))[best_c[1]]
                ratio = (vf / fmax) / (vc / cmax) if vc > 0 and fmax and cmax else 0.0
                verdict = "buff" if ratio > 1.10 else "nerf" if ratio < 0.90 else "same"
                chans_c = {e["channel"] for e in cx[name]["effects"]} if name in cx else set()
                chans_f = {e["channel"] for e in fx[name]["effects"]}
                if chans_c and chans_f and not (chans_c & chans_f):
                    verdict = "reworked"
        counts[verdict] += 1
        rows.append((name, tname, x["row"] + 1, fmax, cmax, status, diff, verdict, vals, fmt_effects(cx[name]) if name in cx else "-", fmt_effects(fx[name])))

    removed = [(n, tn, x) for n, (tn, x) in cflat.items() if n not in fflat]
    counts["removed"] = len(removed)

    out = [f"# {cls.capitalize()}: talent buffs and nerfs, Classic -> WoW: Forever", "",
           "> Generated by `_reference/data/scorer/compare_effects.py` from the effect files and spec models in `_reference/data/scorer/`. "
           "Values are the model's marginal gain of the fully-ranked talent from an empty tree at level 60 (raid profiles: % DPS/HPS/threat; leveling: % of time per kill saved); "
           "'per point' = that value divided by the rank count. Synergy effects (`requires`) do not count from an empty tree. Change the inputs, not this file.", "",
           "Verdict rule: per-point value ratio Forever/Classic in the talent's best Classic profile - **buff** > 1.10, **nerf** < 0.90, **same** otherwise; "
           "**reworked** when the encoded effect channels no longer overlap; **new** / **removed** when the talent exists in one game only; **unscored** when neither game's model values it.", "",
           "| Verdict | Count |", "|---|---|"]
    for k in ("buff", "nerf", "same", "reworked", "new", "removed", "unscored"):
        out.append(f"| {k} | {counts[k]} |")
    out += ["", "## Per talent", ""]
    head = "| Talent | Tree | Row | Ranks C->F | Status / layout change | Verdict | " + " | ".join(f"{s} / {p} C->F" for s, p in pairs) + " | Classic encoding (max rank) | Forever encoding (max rank) |"
    out.append(head)
    out.append("|" + "---|" * (7 + len(pairs) + 2))
    for name, tname, row, fmax, cmax, status, diff, verdict, vals, enc_c, enc_f in rows:
        cells = []
        for key, vc, vf in vals:
            cells.append(f"{vc * 100:+.1f}% -> {vf * 100:+.1f}%")
        ranks = f"{cmax}->{fmax}" if cmax else f"-> {fmax}"
        sd = status + (f" ({diff})" if diff else "")
        out.append(f"| {name} | {tname} | {row} | {ranks} | {sd} | **{verdict}** | " + " | ".join(cells) + f" | {enc_c} | {enc_f} |")
    if removed:
        out += ["", "## Removed in Forever (Classic only)", "", "| Talent | Classic tree | Row | Ranks | Classic encoding |", "|---|---|---|---|---|"]
        for n, tn, x in sorted(removed, key=lambda r: (r[1], r[2]["row"], r[0])):
            out.append(f"| {n} | {tn} | {x['row'] + 1} | {x['max']} | {fmt_effects(cx[n]) if n in cx else '-'} |")

    # ---- builds that changed
    fb = load_builds(ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json")
    cb = load_builds(ROOT / cls / "research" / "talents" / "classic-baseline" / "builds.json")
    out += ["", "## Builds that changed (Classic reference vs Forever optimizer)", "",
            "For each Forever `opt-<spec>-<profile>` build: the Classic community build it was calibrated against, the Classic core talents the Forever build no longer takes "
            "(only those that still exist in Forever), and the talents the Forever build adds. A long 'drops' list means the spec had to be rebuilt.", ""]
    for spec, prof in pairs:
        fid = f"opt-{spec}-{prof}"
        cid = REFERENCE.get((cls, spec, prof))
        if fid not in fb or not cid or cid not in cb:
            continue
        fa = build_alloc(fb[fid]); ca = build_alloc(cb[cid])
        fsplit = "/".join(str(sum(p for t, p in fb[fid]["allocation"].get(tn, []))) for tn in ftree)
        csplit = "/".join(str(sum(p for t, p in cb[cid]["allocation"].get(tn, []))) for tn in ctree)
        drops = [f"{t} {r}" for t, r in sorted(ca.items()) if t in fflat and fa.get(t, 0) == 0]
        adds = [f"{t} {r}" + (" (new)" if meta.get(t, {}).get("status") == "new" else "") for t, r in sorted(fa.items()) if ca.get(t, 0) == 0]
        lowered = [f"{t} {ca[t]}->{fa[t]}" for t in sorted(ca) if t in fa and 0 < fa[t] < ca[t]]
        out.append(f"### `{fid}` ({fsplit}) vs Classic `{cid}` ({csplit})")
        out.append("")
        out.append(f"- **Drops:** {', '.join(drops) if drops else 'nothing'}")
        out.append(f"- **Adds:** {', '.join(adds) if adds else 'nothing'}")
        if lowered:
            out.append(f"- **Fewer ranks:** {', '.join(lowered)}")
        out.append("")
    return "\n".join(out) + "\n", counts, rows, pairs


def main():
    classes = [c for c in CLASSES if not sys.argv[1:] or c in sys.argv[1:]]
    outdir = HERE / "changes"
    outdir.mkdir(exist_ok=True)
    index = ["# Talent changes Classic -> WoW: Forever (model view)", "",
             "> Generated by `_reference/data/scorer/compare_effects.py`. One page per class; counts are talents in the Forever tree (removed = Classic talents that no longer exist).", "",
             "| Class | Buffs | Nerfs | Same | Reworked | New | Removed | Unscored | Biggest buffs (per point, in the talent's best Classic profile; full-talent values shown) | Biggest nerfs |", "|---|---|---|---|---|---|---|---|---|---|"]
    for cls in classes:
        text, counts, rows, pairs = report(cls)
        (outdir / f"{cls}.md").write_text(text, encoding="utf-8")
        ranked = []
        for name, tname, row, fmax, cmax, status, diff, verdict, vals, _, _ in rows:
            if verdict not in ("buff", "nerf"):
                continue
            best = max(vals, key=lambda v: v[1])
            key, vc, vf = best
            ranked.append((verdict, (vf / fmax) / (vc / cmax) if vc > 0 else 0, name, vc, vf, key, cmax, fmax))
        buffs = sorted([r for r in ranked if r[0] == "buff"], key=lambda r: -r[1])[:4]
        nerfs = sorted([r for r in ranked if r[0] == "nerf"], key=lambda r: r[1])[:4]

        def cell(r):
            _, _, n, vc, vf, _, cm, fm = r
            ranks = f"{cm}->{fm} ranks, " if cm != fm else ""
            return f"{n} ({ranks}{vc * 100:+.1f}% -> {vf * 100:+.1f}%)"
        fb = ", ".join(cell(r) for r in buffs) or "-"
        fn = ", ".join(cell(r) for r in nerfs) or "-"
        index.append(f"| [{cls.capitalize()}]({cls}.md) | {counts['buff']} | {counts['nerf']} | {counts['same']} | {counts['reworked']} | {counts['new']} | {counts['removed']} | {counts['unscored']} | {fb} | {fn} |")
        print(f"{cls:8s} " + " ".join(f"{k}={v}" for k, v in counts.items()))
    (outdir / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
