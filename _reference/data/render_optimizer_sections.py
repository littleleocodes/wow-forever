"""Write the "Optimizer (stats model)" section of every class README from the optimizer outputs.

Reads `<class>/research/talents/forever/proposed-builds.json` (the `opt-*` builds) and the optimizer reports, and writes the
`## Optimizer (stats model)` section of each scenario README: the leveling and solo rows into `<class>/research/leveling/README.md`, the
raid, tank and healer rows into `<class>/research/raid/README.md` (2026-09-27 layout, paths.py). The use-case rows and the findings
prose live in this file (they are editorial); the splits and scores are read from the data.

    python _reference/data/render_optimizer_sections.py [class ...]
"""
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

# Model claims with no community precedent - to be tested in the beta (level cap 30) or at launch.
HYPOTHESES = {
    "hunter": "Lone Wolf's +20% (the raid comparison rests on it); Deadly Aspects' proc rate; pet threat scaling (pet_dmg_to_surv 0.3).",
    "mage": "The AoE build keeping Shatter 3 + Fingers of Frost 2 and dropping Improved Cone of Cold; the ~9 h Frost-over-Fire leveling gap assumes equal talentless baselines; Arcane Meditation at 17%/rank.",
    "warrior": "Values of the new talents (Bloodthrill, Spearing Strike, Weaponmaster, Bastion, Vitality); dual-wield vs two-hander leveling assumes equal talentless baselines; Unbridled Wrath at 60%.",
    "rogue": "The Mutilate-over-swords margin (+92% vs +57%) and Restless Blades' cooldown maths; daggers vs swords leveling assumes equal talentless baselines.",
    "priest": "Penance, Renewed Hope and Devouring Contagion numbers; Blackout's stun value while leveling; Meditation at its Forever value.",
    "paladin": "Twist of Light's seal-twisting proc (valued at +6% pending mechanics); Holy Strike and Seal of Fury numbers; whether Forever paladins get a taunt; Champion of the Light's Intellect scaling.",
    "shaman": "Water Shield's globe rate (encoded as ~+18% healer mana); Maelstrom Weapon's stack chance; Enhancement vs Elemental leveling assumes equal talentless baselines.",
    "warlock": "Fire Destruction's +164% is against its own baseline, not comparable to Shadow; Drain Hope and Soul Siphon numbers; Demonic Pact keeping Demonic Sacrifice.",
    "druid": "Balance vs Cat leveling assumes equal talentless baselines (Classic favours Cat); King of the Jungle, Berserk and Rend and Tear values; Wild Growth and Gift of the Earthmother throughput.",
}

FINDINGS = {
    "hunter": "Improved Tracking beats Ferocity per point everywhere; Endurance Training is worth ~0.2%/rank of leveling time; with the raid mana weight raised for hunters (they run dry on long fights), Efficiency is back in the raid build (12/34/5); Lone Wolf edges the pet build in raids (absolute DPS index 1.96 vs 1.88) if its +20% is real.",
    "mage": "Arcane Meditation (17%/rank) pulls every build 15+ points into Arcane; raid Frost is Shatter + Fingers of Frost with no Winter's Chill; Frost still out-levels Fire (+43% vs +31% time saved). The AoE build now follows the Classic AoE loop (Improved Frost Nova 15-16, Permafrost, Improved Blizzard 20-22, Arctic Reach, Cold Snap, Ice Block, Ice Barrier at 40, no Frostbite) and keeps Shatter/Fingers of Frost because Forever's versions are stronger.",
    "warrior": "Dual-wield Fury 18/33/0 and two-hander Fury 19/32/0 score within 2% of each other and both beat the Arms draft; Bloodthirst, Flurry, Enrage, Unbridled Wrath and Anger Management are the raid core in every DPS build. Protection 6/5/40 takes the deep Protection rows (Vitality, Focused Rage, Bastion, Shield Slam) plus Anticipation/Improved Shield Wall now that defense and armor are priced from their arithmetic.",
    "rogue": "Mutilate daggers 33/16/2 (+92%) beat Combat swords 19/32/0 (+57%) by a wide margin: Seal Fate, Lethality, Improved Poisons and Cold Blood all feed Mutilate. Dagger leveling is 21/28/2 (Combat's Hack and Slash, Restless Blades and Riposte); Adrenaline Rush stays core for swords.",
    "priest": "Healer 22/29/0: Discipline's Twin Disciplines, Mental Strength and Penance pair with Holy's Divine Fury, Inspiration, Holy Specialization and Spiritual Healing. Shadow raid 20/0/31 leans on Shadow Weaving, Darkness and Devouring Contagion; leveling Shadow 14/0/37 keeps Spirit Tap and Blackout (now priced as a leveling stun).",
    "paladin": "Retribution raid 10/8/33 matches the hand draft's split (Seal of Command, Vengeance, Champion of the Light, Twist of Light, Two-Handed Weapon Specialization). The healer 23/0/28 spends its second half in Retribution (Champion of the Light, Conviction, Benediction, Sanctified Judgement) rather than Protection. Protection 2/31/18 is Holy Shield, Iron Creed and Templar's Bulwark plus Retribution threat (Conviction, Deflection, Crusade).",
    "shaman": "Restoration 0/10/41: Water Shield and Riptide are the new core and Enhancement's Thundering Strikes crits heals. Elemental 31/6/14 adds Lava Burst, Lightning Overload and Elemental Alacrity with Tidal Focus/Water Shield for mana. Enhancement 19/32/0 (Stormstrike, Maelstrom Weapon, Flurry, Elemental Weapons) takes Elemental's shock talents; leveling Enhancement goes 0/34/17 for Water Shield.",
    "warlock": "The Shadow Bolt raid build is 10/11/30: Demonic Sacrifice plus 30 Destruction for Conflagrate → Shadow and Flame (+10% Shadow), so DS/Ruin survives in a new shape. Affliction 31/11/9 is a real DoT spec (Malevolence, Pandemic, Soul Siphon, Drain Hope) with Demonic Sacrifice. Fire Destruction 9/11/31 (Aftermath, Conflagrate, Fire and Brimstone, Incinerate) scores +164% against its own baseline; leveling stays Affliction with a Voidwalker (31/16/4).",
    "druid": "Restoration 11/5/35 keeps Swiftmend and adds Wild Growth, Gift of the Earthmother and Genesis. Cat 9/35/7 (Rend and Tear, King of the Jungle, Berserk, Natural Instinct) and Bear 9/40/2 (Mangle, Natural Reaction) share Heart of the Wild, Predatory Strikes and Leader of the Pack. Balance 38/0/13 gets Eclipse, Nature's Grace and Vengeance; Cat leveling goes 0/35/16.",
}


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
    lines += ["", "Model findings: " + FINDINGS[cls], "",
              "Beta hypotheses (model claims without community precedent, unverified): " + HYPOTHESES[cls]
              + f" Level-30 checks: [`_reference/beta-checklist.md`]({paths.rel(readme, paths.ROOT / '_reference/beta-checklist.md')}).", ""]
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
