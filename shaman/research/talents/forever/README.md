# Shaman — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; the trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [../../spells/README.md](../../spells/README.md). Point-by-point audit of
every Classic build: [baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), one page each under
[../../leveling/builds/](../../leveling/builds/), [../../raid/builds/](../../raid/builds/) and [../../pvp/builds/](../../pvp/builds/).

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Lightning Mastery (Elemental, -1.0 s) | **Renamed** *Elemental Alacrity* (3 ranks, tier 3, -0.5 s on Lightning Bolt, Chain Lightning and Lava Burst) | Lightning Bolt is a 2.5-second cast at high ranks, so 2.0 seconds with Alacrity |
| Elemental Mastery (Elemental capstone) | **Removed**; *Lava Burst* is the capstone | No burst cooldown: a rotational Fire nuke instead |
| Storm Reach, Improved Fire Totems | **Renamed** *Elemental Reach* (also Fire Nova, Lava Burst and +15 yards on Flame Shock) and *Improved Fire Nova* | |
| Call of Thunder | 5 ranks → **1 rank (+3% crit)**, requires Elemental Alacrity 3 | 4 points freed |
| Elemental Fury | 1 rank → **5 ranks** at tier 6, requires Call of Thunder | 4 points dearer; nets out with Call of Thunder |
| Improved Weapon Totems, Enhancing Totems, Weapon Mastery, Two-Handed Axes and Maces | **Removed** (baseline now) | The Windfury-support Enhancement build no longer exists |
| Shield Specialization, Parry | **Removed**; Parry's place is *Spirit Weapons* | Enhancement is rebuilt around Stormstrike, Maelstrom Weapon and Rage of the Farseer |
| Stormstrike | Capstone → **16-point talent** | |
| Flurry | Requires **Mental Dexterity 3** (attack power from Intellect) | |
| Nature's Guidance | **Removed**; hit is on *Tidal Focus* (5% at 5 ranks, tier 2) | Casters and melee alike take Tidal Focus |
| Totemic Mastery, Healing Grace | **Removed**; Healing Grace's place is *Natural Grace* (15% less spell threat) | Buff totems reach 30 yards without it |
| Mana Tide Totem | Capstone → **16-point talent** | |
| Tidal Mastery | Heal crit only, tier 4 | No longer buffs lightning crit |

## What's new and matters

- **Lava Burst**, **Lightning Overload**, **Earthbound** (Elemental); **Maelstrom Weapon**, **Rage of the Farseer**, **Mental Dexterity**,
  **Mental Quickness**, **Improved Stormstrike**, **Shamanistic Focus** (Enhancement); **Riptide**, **Water Shield**, **Mindfulness**
  (Restoration).
- **Thundering Strikes** is crit with all spells and attacks: Elemental's raid pick takes it, and healers can.

## Builds

The current picks per spec and mode are on the player pages: [leveling](../../../leveling/README.md) and
[raid](../../../raid/README.md); the research behind them is under [../../leveling/](../../leveling/) and [../../raid/](../../raid/).

## To verify at launch

- Lava Burst 192-248 and Riptide 799-883 plus 805 over 15 seconds at 60 (70291 spellbook).
- Maelstrom Weapon's proc rate (not in the tooltip).
- Windfury Totem's 246 attack power at 60 (Classic 315).
