"""The cross-class tier list (2026-10-15, user request of 2026-10-14: "I want to create a tier list for the DPS as well Healers and Tanks
after the testing is done"). Writes `tier-list.md` at the project root.

    python _reference/data/render_tier_list.py

Each spec is represented by the build its raid page shows (render_modes.rank_builds: the pages' own pick and numbers, so the tier list
never disagrees with them). User decisions of 2026-10-14:
- Damage: tiers by full-raid DPS (every raid buff and debuff, 3-minute fight, phase-1 gear from one item pool), the number the pages
  rank on; healers: tiers by the healer lab's capacity (one group, the same damage and fight for every class).
- Tiers by percentage of the role's best spec ("S/A/B/C by % of best"): S within 3% (TIER_CUTS; 3% is the pages' tie), A within 10%,
  B within 20%, C further behind.
- Tanks: no tiers ("No tank tiers"): tank value is relative to each class's own hand draft and each tank plays in its own gear set, so
  the three tanks are listed with their numbers and not ranked.
"""
import datetime
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
import render_modes as RM  # noqa: E402
import render_rotations as rr  # noqa: E402
import render_start_here as rs  # noqa: E402
import spec_modes as SM  # noqa: E402
sys.path.insert(0, str(HERE / "raidsim"))
import setup as RS  # noqa: E402  (raidsim/setup.py: the pinned simulator commit)

TODAY = datetime.date.today().isoformat()
TIER_CUTS = [("S", 0.03), ("A", 0.10), ("B", 0.20)]   # behind the role's best by at most this share; C below
OUT = ROOT / "tier-list.md"


def tier_of(gap):
    return next((t for t, cut in TIER_CUTS if gap <= cut + 1e-9), "C")


def picks():
    """[(cls, spec, build, raid number row, healer row)] for every spec with a raid page pick."""
    out = []
    for cls in SM.CLASSES:
        B = rr.builds(cls)
        g = SM.grid(cls, list(B.values()))
        nums = (RM.raid_numbers(cls), RM.leveling_numbers(cls), RM.healer_numbers(cls))
        g = RM.own_rotation_only(cls, g, nums)
        R, _L, H = nums
        for spec in g:
            ranked = RM.rank_builds(cls, "raid", g[spec].get("raid", []), nums)
            # the druid's bear sits in Feral Combat next to the cat: the tank build is listed with the tanks as well
            tanks = [b for b in g[spec].get("raid", []) if (R.get(b["id"]) or {}).get("tank")]
            if ranked:
                out.append((cls, spec, ranked[0], R.get(ranked[0]["id"]) or {}, H.get(ranked[0]["id"]) or {}))
            if tanks and not (ranked and (R.get(ranked[0]["id"]) or {}).get("tank")):
                t = max(tanks, key=lambda b: R[b["id"]].get("value") or 0)
                out.append((cls, spec, t, R[t["id"]], {}))
    return out


def name(cls, spec, b):
    return f"[{cls.capitalize()}: {SM.spec_name(cls, spec)}]({cls}/raid/{SM.spec_slug(cls, spec)}.md)"


def tiers(rows, unit, fmt):
    """rows: [(value, cls, spec, build)], higher is better. Markdown lines grouped by tier."""
    rows = sorted(rows, key=lambda x: -x[0])
    best = rows[0][0]
    o = [f"| Tier | Spec | Build | {unit} | Behind the best |", "|---|---|---|---|---|"]
    for v, cls, spec, b in rows:
        gap = 1 - v / best
        o.append(f"| **{tier_of(gap)}** | {name(cls, spec, b)} | {rs.split_of(cls, rs.flat(b))} | {fmt(v)} | "
                 f"{'best' if gap <= 0 else f'{gap:.1%}'} |")
    return o


def main():
    P = picks()
    dps = [(r["group"], cls, spec, b) for cls, spec, b, r, h in P if b.get("role") != "healer" and not r.get("tank") and r.get("group")]
    heal = [(h["capacity"], cls, spec, b) for cls, spec, b, r, h in P if b.get("role") == "healer" and h.get("capacity")]
    tank = [(cls, spec, b, r) for cls, spec, b, r, h in P if r.get("tank")]
    commit = RS.GAMES["forever"]["commit"][:7]
    cuts = ", ".join(f"**{t}** within {c:.0%} of the best" for t, c in TIER_CUTS) + f", **C** more than {TIER_CUTS[-1][1]:.0%} behind"
    o = ["# Tier list: raid damage, healing and tanking", "",
         f"Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: {cuts}. "
         "Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: "
         "each class page ranks its specs for leveling.", ""]
    o += ["## Damage", "",
          f"DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for "
          f"every spec, racials off. The community's combat simulator (ElliotWood/Forever, commit {commit}) with this project's patches and "
          "tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and "
          "community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build "
          "+8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is "
          "an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list "
          "(its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in "
          "dungeon gear without trinkets.", ""]
    o += tiers(dps, "Full raid DPS", lambda v: f"{v:.0f}") + [""]
    o += ["## Healing", "",
          "Healing capacity in this project's healer lab: how much of the lab's standard raid damage the healer keeps one group (a tank and "
          "four raid members) alive through for five minutes, in 90% of the runs. Healers are in no community simulator; the lab is a model "
          "of stated assumptions (`_reference/data/heallab/tables.py`), the same group, damage and fight for every class. Real raids spread "
          "damage differently and value utility (dispels, buffs, battle resurrection) the lab does not count.", ""]
    o += tiers(heal, "Capacity", lambda v: f"{v:.2f}") + [""]
    o += ["## Tanking", "",
          "Not tiered: each tank's tank value is measured against its own class's hand-made build, and each tank plays in its own gear "
          "set, so the numbers do not compare across classes. Threat and damage taken per second below are in a full raid against a "
          "raid boss (the community simulator, with this project's patches: Bear Form's threat is our +50% patch).", "",
          "| Spec | Build | Threat per second | Damage taken per second | Tank value (own class's hand draft = 1.00) |", "|---|---|---|---|---|"]
    for cls, spec, b, r in sorted(tank):
        th, dt = r["row"].get("threat"), r["row"].get("dtps")
        o.append(f"| {name(cls, spec, b)} | {rs.split_of(cls, rs.flat(b))} | {th:.0f} | {dt:.0f} | {r.get('value') or 0:.2f} |"
                 if th and dt else f"| {name(cls, spec, b)} | {rs.split_of(cls, rs.flat(b))} | - | - | {r.get('value') or 0:.2f} |")
    o += ["", "---", f"*Generated by `_reference/data/render_tier_list.py` on {TODAY} from the pages' own picks and numbers (client build "
          f"{RM.BUILD}). Simulations, not in-game measurements. Do not hand-edit.*", ""]
    OUT.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(dps)} damage specs, {len(heal)} healers, {len(tank)} tanks")


if __name__ == "__main__":
    main()
