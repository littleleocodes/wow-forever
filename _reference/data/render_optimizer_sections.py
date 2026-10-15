"""Write the "Optimizer (stats model)" section of every class README from the optimizer outputs.

Reads `<class>/research/talents/forever/proposed-builds.json` (the `opt-*` builds) and the optimizer reports, and writes the
`## Optimizer (stats model)` section of each scenario README: the leveling and solo rows into `<class>/research/leveling/README.md`, the
raid, tank and healer rows into `<class>/research/raid/README.md` (2026-09-27 layout, paths.py). The use-case rows live in this file
(they are editorial); the splits, scores and findings are read from the data (findings generated since 2026-10-15).

    python _reference/data/render_optimizer_sections.py [class ...]
"""
import functools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import paths  # noqa: E402
import readme_sections as rs  # noqa: E402

# (use-case label, spec model, profile, hand-draft build id to compare with)
ROWS = {
    "hunter": [
        ("Leveling (single target)", "bm-leveling", "leveling-st", "leveling-beast-mastery"),
        ("Solo / farming at 60", "bm-leveling", "solo-60", "bm-solo-farm"),
        ("Raid DPS with pet", "mm-raid", "raid-dps", "bm-mm-raid"),
        ("Raid DPS, Lone Wolf", "mm-lonewolf-raid", "raid-dps", "mm-lone-wolf-raid"),
    ],
    "mage": [
        ("Leveling, Frost single target", "frost-leveling", "leveling-st", "leveling-frost"),
        ("Leveling, Fire single target", "fire-leveling", "leveling-st", "leveling-frost"),
        ("AoE grinding", "frost-aoe", "leveling-aoe", "leveling-frost"),
        ("Raid DPS, Frost (lone frost mage)", "frost-raid", "raid-dps", "frost-winters-chill-raid"),
        ("Raid DPS, Frost (another mage keeps Winter's Chill)", "frost-raid", "raid-dps-extwc", "frost-arcane-power-raid"),
        ("Raid DPS, Fire", "fire-raid", "raid-dps", "fire-raid"),
    ],
    "warrior": [
        ("Raid DPS, dual wield Fury", "fury-dw-raid", "raid-dps", "fury-dw-raid"),
        ("Raid DPS, two-hander", "arms-2h-raid", "raid-dps", "arms-2h-raid"),
        ("Raid main tank", "prot-tank", "raid-tank", "prot-raid-tank"),
        ("Leveling, two-hander", "arms-2h-raid", "leveling-st", "leveling-arms"),
        ("Solo / farming at 60, dual wield", "fury-dw-raid", "solo-60", "leveling-arms"),
    ],
    "rogue": [
        ("Raid DPS, swords", "combat-swords-raid", "raid-dps", "combat-swords-raid"),
        ("Raid DPS, daggers", "combat-daggers-raid", "raid-dps", "combat-daggers-raid"),
        ("Leveling, swords", "combat-swords-raid", "leveling-st", "leveling-combat-swords"),
        ("Leveling, daggers", "combat-daggers-raid", "leveling-st", "leveling-combat-swords"),
        ("Solo / farming at 60", "combat-swords-raid", "solo-60", "leveling-combat-swords"),
    ],
    "priest": [
        ("Raid healer", "holy-heal", "raid-heal", "holy-raid-healer"),
        ("Raid DPS, Shadow", "shadow-dps", "raid-dps", "leveling-shadow"),
        ("Leveling, Shadow", "shadow-dps", "leveling-st", "leveling-shadow"),
        ("Solo / farming at 60", "shadow-dps", "solo-60", "leveling-shadow"),
    ],
    "paladin": [
        ("Raid healer", "holy-heal", "raid-heal", "holy-raid-healer"),
        ("Raid DPS, Retribution", "ret-dps", "raid-dps", "ret-raid-dps"),
        ("Raid main tank", "prot-tank", "raid-tank", "prot-tank"),
        ("Leveling, Retribution", "ret-dps", "leveling-st", "leveling-retribution"),
        ("Solo / farming at 60", "ret-dps", "solo-60", "leveling-retribution"),
    ],
    "shaman": [
        ("Raid healer", "resto-heal", "raid-heal", "resto-raid-healer"),
        ("Raid DPS, Elemental", "elemental-dps", "raid-dps", "elemental-raid-dps"),
        ("Raid DPS, Enhancement", "enhancement-dps", "raid-dps", "enhancement-raid-dps"),
        ("Leveling, Enhancement", "enhancement-dps", "leveling-st", "leveling-enhancement"),
        ("Leveling, Elemental", "elemental-dps", "leveling-st", "leveling-enhancement"),
        ("Solo / farming at 60", "enhancement-dps", "solo-60", "leveling-enhancement"),
    ],
    "warlock": [
        ("Raid DPS, Shadow Bolt", "sb-raid", "raid-dps", "ds-ruin-raid"),
        ("Raid DPS, Affliction DoTs", "affliction-raid", "raid-dps", "affliction-dot-raid"),
        ("Raid DPS, Fire Destruction", "fire-destro-raid", "raid-dps", "destruction-fire-raid"),
        ("Leveling, Affliction + Voidwalker", "affliction-leveling", "leveling-st", "leveling-affliction"),
        ("Solo / farming at 60", "affliction-leveling", "solo-60", "leveling-affliction"),
    ],
    "druid": [
        ("Raid healer", "resto-heal", "raid-heal", "resto-raid-healer"),
        ("Raid DPS, Cat", "feral-cat-dps", "raid-dps", "feral-cat-dps"),
        ("Raid main tank, Bear", "feral-bear-tank", "raid-tank", "feral-bear-tank"),
        ("Raid DPS, Balance", "balance-dps", "raid-dps", "balance-moonkin-raid"),
        ("Leveling, Cat", "feral-cat-dps", "leveling-st", "leveling-feral"),
        ("Leveling, Balance", "balance-dps", "leveling-st", "leveling-feral"),
        ("Solo / farming at 60, Cat", "feral-cat-dps", "solo-60", "leveling-feral"),
    ],
}

# 2026-10-15 page audit B6: the "Model findings" and "Beta hypotheses" prose was hand-written in September (HYPOTHESES, FINDINGS) and
# named builds, splits and talents the trees no longer have (Vitality, King of the Jungle, Restless Blades, Drain Hope). The findings
# are now generated from each optimizer build (its split and the talents whose removal costs the most score, as written into its `core`
# by scorer/run.py --export) and the hand draft's split; the hypotheses point to the builds' open questions (launch checklist).


@functools.lru_cache(maxsize=None)
def current_talents(cls):
    """Every talent name of the class's current Forever trees (forever-talents/<class>.json)."""
    d = json.load(open(paths.ROOT / "_reference/data/forever-talents" / f"{cls}.json", encoding="utf-8"))
    return {t["name"] for tr in d["trees"] for t in tr["talents"]}


def split_of(b, trees):
    return "/".join(str(sum(p for t, p in b["allocation"].get(t, []))) for t in trees)


def findings(cls, rows, fb, trees):
    """One generated line per use-case row: the optimizer build's split, its biggest talents by score lost when removed, the hand draft."""
    out = []
    have = current_talents(cls)
    for label, spec, prof, draft in rows:
        b = fb.get(f"opt-{spec}-{prof}")
        if not b:
            continue
        top = []
        for c in b.get("core") or []:
            name = c.get("talent") if isinstance(c, dict) else None
            m = re.search(r"costs ([\d.]+) points", (c.get("why") or "") if isinstance(c, dict) else "")
            if name in have and m:
                top.append(f"{name} ({m.group(1)})")
        d = fb.get(draft)
        out.append(f"- **{label}:** {split_of(b, trees)}" + (f"; biggest talents by score lost when removed: {', '.join(top[:5])}" if top else "")
                   + (f"; the hand draft `{draft}` is {split_of(d, trees)}" if d else "") + ".")
    return out


def section(cls, scenario):
    """The Optimizer section of one scenario README, or None when the class has no use-case row for it."""
    fb = {b["id"]: b for b in json.load(open(paths.builds_json("forever", cls), encoding="utf-8"))["builds"]}
    trees = list(next(iter(fb.values()))["allocation"].keys())
    readme = paths.scenario_readme(cls, scenario)
    rows = [r for r in ROWS[cls] if paths.scenario_of_profile(r[2]) == scenario]
    if not rows:
        return None
    changes = paths.ROOT / "_reference/data/scorer/changes" / f"{cls}.md"
    lines = ["## Optimizer (stats model) — builds derived from talent numbers", "",
             "Produced by `_reference/data/scorer/` (see its README for the method and Classic calibration). Reports with every "
             f"talent's marginal value: [`optimizer/`]({paths.rel(readme, paths.scenario_dir(cls, scenario) / 'optimizer')}/). What changed from Classic "
             f"(buffs, nerfs, talents each build drops or adds): [`changes/{cls}.md`]({paths.rel(readme, changes)})."]
    if scenario == "leveling":
        lines += [f"When to respec while leveling, with the best point-by-point path: [respec plan]({paths.rel(readme, paths.respec_plan(cls))}) "
                  "(its level-30/40 plans usually out-level the `opt-*-leveling-st` order, which plays toward the 60 build from level 10)."]
    lines += ["", "| Use-case | Spec model | Optimized build | Hand draft it competes with |", "|---|---|---|---|"]
    for label, spec, prof, draft in rows:
        bid = f"opt-{spec}-{prof}"
        if bid not in fb:
            continue
        b = fb[bid]
        split = "/".join(str(sum(p for t, p in b["allocation"].get(t, []))) for t in trees)
        m = re.search(r"score ([+-][\d.]+%)", b["summary"])
        score = m.group(1) if m else ""
        order = " with order" if b.get("order") else ""
        draft_cell = f"[{draft}]({paths.rel(readme, paths.build_page('forever', cls, fb[draft]))})" if draft in fb else "—"
        lines.append(f"| {label} | {spec} | [{split}{order}]({paths.rel(readme, paths.build_page('forever', cls, b))}) ({score}) | {draft_cell} |")
    lines += ["", "Model findings (generated from the optimizer builds; scores are within each spec model, never across models):", ""]
    lines += findings(cls, rows, fb, trees)
    lines += ["", "Beta hypotheses: every build's unverified claims are its `open_questions`, collected in "
              f"[`_reference/launch-checklist.md`]({paths.rel(readme, paths.ROOT / '_reference/launch-checklist.md')}); level-30 checks: "
              f"[`_reference/beta-checklist.md`]({paths.rel(readme, paths.ROOT / '_reference/beta-checklist.md')}).", ""]
    return "\n".join(lines)


def main():
    classes = [c for c in ROWS if not sys.argv[1:] or c in sys.argv[1:]]
    for cls in classes:
        for sc in ("leveling", "raid"):
            text = section(cls, sc)
            if text:
                rs.splice_ordered(paths.scenario_readme(cls, sc), sc, "## Optimizer", text)
        rs.drop(paths.ROOT / cls / "README.md", "## Optimizer")   # moved to the scenario READMEs (2026-09-27 layout)
        print(f"updated {cls}/leveling/README.md and {cls}/raid/README.md")


if __name__ == "__main__":
    main()
