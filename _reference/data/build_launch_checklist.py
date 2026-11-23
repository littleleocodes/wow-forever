"""Aggregate every proposed build's `open_questions` into _reference/launch-checklist.md.

Usage (from anywhere): python _reference/data/build_launch_checklist.py
"""
import sys
import json
import pathlib
import paths  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[2]
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]

GLOBAL = [
    ("Talent system rules", [
        "51 points at 60, 1 per level from 10, and 5-points-per-tier gating — confirm in the live client (fan calculators assume it).",
        "Respec cost curve (Classic: 1g → 50g); decides how freely leveling builds can deviate from the 60 build.",
        "Which abilities are baseline vs. talent: Aimed Shot, Holy Strike, Seal of Fury, Lacerate, Shadow Word: Death, Nature's Grasp, Omen of Clarity, Faerie Fire (Feral), Divine Spirit, Consecration, Blessing of Kings, Mangle (Cat).",
    ]),
    ("Data refresh", [
        "Re-pull the trees from each new beta build (refresh_forever_talents.py --fetch) and at launch from the live client, re-run extract → render_trees → validate → render_builds; fix any build the validator rejects.",
        "Read every talent marked *(est.)* at max rank in game — higher ranks in the demo data are extrapolated.",
        "Level-60 tooltip numbers of every new active ability with gear (the data's beta tooltips are level 60 with no gear).",
    ]),
    ("Raid/combat rules that decide talent value", [
        "Raid debuff cap (Classic: 16) — decides DoT builds, Winter's Chill, Improved Shadow Bolt, Insect Swarm slots.",
        "Weapon skill / glancing blows — decides whether rogues and warriors still need +weapon-skill gear now that Weapon Expertise changed.",
        "Spell hit cap vs. +3-level bosses and whether heals can miss (Holy Precision / Divine Precision).",
        "Fire immunity in The Barrow Deeps / Hyjal Summit (Fire Mage, Fire Warlock viability).",
        "Class books (book-only spell ranks: Tome of Frostbolt XI, Grimoire of Shadow Bolt X ...; Ruins of Ahn'Qiraj in Classic): on "
        "2026-12-09 check whether The Barrow Deeps or Hyjal Summit drop them (or new ones). If they do, `raidsim/trainer_ranks.py "
        "--reverse` and re-tune the raid rotations (the pages assume trainer ranks; the audit's research of 2026-11-20).",
        "Enchants the gear lists leave out (2026-11-22, the audit session; raidsim/gear_tiers.ENCHANTS_OUT): do enchanters have Gloves - "
        "Superior Agility (+15) and Classic's other Ahn'Qiraj formulas (Gloves - Fire, Frost, Shadow and Healing Power, Cloak - Dodge), "
        "which the simulator's database lists as phase 1 with no source, and Forever's sourceless enchants (Chest - Living Stats, Bracer - "
        "Spell Power, the Grand Crusader / Sorcerer / Arcanist / Inquisitor weapon enchants, the off-hand and shield ones)? Each is raced "
        "where it fits and recorded with what it would have gained.",
        "Death Lotus (248822) and Dimensional Transporter - Mt. Hyjal (260823), reagents of Forever crafts (2026-11-23, the audit "
        "session): where do they come from? No tooltip ties them to Hyjal Summit or The Barrow Deeps, so the gear lists count their crafts "
        "as plain crafts (raidsim/gear_lists.WATCH_MATS marks them); if either comes only from the raids or from content that opens with "
        "them, those crafts are True BiS items from 2026-12-09, like the 97 made with Malleable Essence of Nature.",
        "Molten Core's materials for Tarnished Undermine Reals (2026-11-23, the audit session's G14): Pix Xizzix in Booty Bay sells Fiery "
        "Core and Lava Core (15 Reals) and Core Leather (10); can they be traded, and can the Thorium Brotherhood's recipes (Lokhtos "
        "Darkbargainer: Fiery Chain Girdle, Molten Helm, Corehound Boots, Flarecore Gloves, Dark Iron Bracers, Lava Belt and 19 more, "
        "Friendly to Exalted) be made now? The simulator's database dates those crafts phase 2 and the Alliance auction house showed no "
        "core and none of the 31 crafts from 2026-11-05 to 2026-11-22, so the gear lists keep them out (raidsim/gear_lists.MC_MATS); if "
        "the answer is yes, the three cores leave MC_MATS and the crafts join the True lists by the craft rule.",
        "Which honor ranks can a player hold now, and does the rank gear need them? (2026-11-23: the user is not sure.) The gear lists "
        "keep the rank gear the simulator's database dates phase 1 in both True lists, marked PvP, with a non-PvP alternative beside each "
        "piece (raidsim/gear_lists.pvp_alternatives); no rank cap is assumed until this is known.",
        "Threat values of new abilities (Holy Strike, Mangle, Stormstrike, Shield Slam changes).",
        "Hunter's Mark: our beta tooltip gives rank 4 +143 ranged attack power, the simulator's spell data +71 (2026-11-21, the audit "
        "session's C17). Read the rank the trainer teaches at 60 and its bonus in game; until then the hunter raid guides say to take "
        "whichever rank your tooltip shows higher, and the raid numbers are the simulator's.",
    ]),
    ("Performance evidence (needed to promote a draft from 'hypothesis' to 'recommended')", [
        "Combat logs / parses at 60 for the head-to-head questions: BM/MM vs. Lone Wolf, Combat daggers vs. Mutilate, Frost AP vs. Fingers of Frost, DS/Ruin vs. Affliction DoT vs. Destruction fire, Fury DW vs. Arms 2H.",
        "A Forever simulator or spreadsheet once formulas are known (Classic sims do not apply to reworked talents).",
    ]),
]


def main():
    lines = ["# Launch checklist — what talents still need from the live game\n",
             "> Generated by `_reference/data/build_launch_checklist.py` from the `open_questions` of every proposed "
             "Forever build, plus the cross-class items below. Regenerate after editing builds. Tick items off by "
             "editing the builds (remove the resolved `open_questions`) and re-running the script.\n"]
    for title, items in GLOBAL:
        lines.append(f"## {title}\n")
        for it in items:
            lines.append(f"- [ ] {it}")
        lines.append("")
    lines.append("## Per-build open questions\n")
    total = 0
    for cls in CLASSES:
        path = ROOT / cls / "research" / "talents" / "forever" / "proposed-builds.json"
        if not path.exists():
            continue
        data = json.load(open(path, encoding="utf-8"))
        lines.append(f"### {data['class']}\n")
        for b in data["builds"]:
            qs = b.get("open_questions", [])
            if not qs:
                continue
            lines.append(f"**{b['name']}** (`{paths.repo_rel(paths.build_page('forever', cls, b))}`)")
            for q in qs:
                lines.append(f"- [ ] {q}")
                total += 1
            lines.append("")
    out = ROOT / "_reference" / "launch-checklist.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} ({total} per-build questions)")


if __name__ == "__main__":
    main()
