# Warlock — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; the trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [../../spells/README.md](../../spells/README.md). Point-by-point audit of
every Classic build: [baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), one page each under
[../../leveling/builds/](../../leveling/builds/), [../../raid/builds/](../../raid/builds/) and [../../pvp/builds/](../../pvp/builds/).

The warlock changed most of any class: 21 new talents, 2 renamed, 19 Classic talents gone. The Classic shapes (7/21/23,
30/0/21) no longer mean the same builds.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Fel Intellect, Fel Stamina, Improved Healthstone, Improved Firestone, Improved Spellstone, Improved Enslave Demon | **Removed** | DS/Ruin's Demonology fillers are gone; tier 2 is Demonic Aegis, Improved Voidwalker, Fel Vitality (+15% to your mana and your demon's) and Demonic Energies |
| Demonic Sacrifice | Tier 5 → **tier 3**, lasts 2 hours; the Imp gives +15% Shadow and the Succubus +15% Fire damage (the reverse of Classic) | Sacrificing is cheap |
| Ruin | 1 rank at tier 5 → **5 ranks at tier 3** (+100% crit damage at 5) | Same effect, 4 more points, 10 Destruction points to reach it |
| Devastation, Improved Immolate, Emberstorm, Improved Searing Pain, Improved Firebolt, Improved Lash of Pain | **Removed** | Destruction's fillers are now Molten Skin, Agonizing Flames, Fire and Brimstone and Shadow and Flame |
| Grim Reach, Dark Pact, Improved Curse of Weakness, Improved Curse of Exhaustion, Improved Drain Life, Drain Soul and Drain Mana | **Removed**; Improved Curse of Agony is *Improved Bane of Agony* (2 ranks) | Affliction is rebuilt around Malediction, Pandemic and Malevolence |
| Suppression | Affliction hit → **hit with every spell** (5% at 5 ranks) and 20% less threat | Every build takes it |
| Improved Life Tap, Unholy Power | Moved to tier 1 (Affliction, Demonology) | Cheaper |
| Soul Link | Tier 7 → **tier 5**, requires Demonic Sacrifice | Soul Link builds gain 10 points |
| Shadow Mastery | 2% → 1% a rank (5% at 5) | Half its Classic value |

## What's new and matters

- **Demonic Pact** (Demonology capstone): keeps a Demonic Sacrifice buff while a different demon is out. The best warlock raid build
  (Demonology, 2026-10-15) sacrifices the Imp and fights with a Succubus.
- **Wrack** (Affliction capstone: a 6-second Shadow channel that raises your other Shadow dots by 10%; it replaced Drain Hope in beta
  build 69893), **Pandemic**, **Malediction**, **Malevolence**: a damage-over-time spec with critting dots.
- **Conflagrate** (16-point), **Shadow and Flame**, **Fire and Brimstone**, **Agonizing Flames**, **Bane of Havoc** and the **Incinerate**
  capstone: the Shadow Bolt spec gets stronger, and a fire spec exists (it loses to Shadow Bolt in the simulator).
- **Demonic Knowledge** (spell damage while a demon is out) and **Decimation** (Soul Fire below 35% health): pet-keeping damage options.
- Curse of Agony and Curse of Doom are Banes (**Bane of Agony**, **Bane of Doom**, plus **Bane of Havoc**): one Bane and one Curse per target.

## Builds

The current picks per spec and mode are on the player pages: [leveling](../../../leveling/README.md) and
[raid](../../../raid/README.md); the research behind them is under [../../leveling/](../../leveling/) and [../../raid/](../../raid/).

## To verify at launch

- Demon scaling from your stats (the 70291 client's numbers; this project's simulator patch uses them): a beta tester's pet pane would confirm them.
- Raid debuff cap (Affliction's dots and curses).
- Demonic Pact: which demon's bonuses stack with which sacrifice.
