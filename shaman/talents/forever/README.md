# Shaman — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Lightning Mastery (Ele T6, -1.0s) | **Removed** → *Elemental Alacrity* (3, -0.17/0.33/0.5s; tier 3 since build 70009) | Lightning Bolt is 2.5s baseline in the beta, so 2.0s with Alacrity: as fast as Classic Elemental |
| Elemental Mastery (Ele capstone) | **Removed** → *Lava Burst* capstone | Burst cooldown replaced by a rotational Fire nuke |
| Storm Reach, Improved Fire Totems | **Removed** → Elemental Reach / Improved Fire Nova | |
| Call of Thunder | 5 ranks (+6%) → **1 rank (+3%)**, requires Elemental Alacrity 3 (build 70009) | 4 points freed |
| Elemental Fury | 1 rank → **5 ranks** (20%/rank) at tier 6 (build 70009), requires Call of Thunder | 4 points more expensive — nets out with Call of Thunder |
| Improved Weapon Totems, Enhancing Totems | **Removed** | The Windfury-support Enhancement build no longer exists |
| Weapon Mastery, Shield Specialization, Parry, Two-Handed Axes and Maces | **Removed** | Enhancement rebuilt around Stormstrike (16-pt), Maelstrom Weapon, Rage of the Farseer |
| Stormstrike | Capstone → **16-point talent** | |
| Flurry | Requires **Mental Dexterity 3** (new AP-from-Intellect talent) | |
| Nature's Guidance | **Removed** → hit is now on *Tidal Focus* (1%/rank) | Every caster/melee build takes Tidal Focus |
| Totemic Mastery, Healing Grace | **Removed** | Natural Grace (threat) replaces Healing Grace; totem range unknown |
| Mana Tide Totem | Capstone → **16-point talent** | Elemental can reach it |
| Tidal Mastery | Now heal crit only; tier 4 in the beta (Totemic Focus took the tier-1 slot) | No longer buffs lightning crit, and no longer a cheap filler |

## What's new and matters

- **Lava Burst**, **Lightning Overload**, **Elemental Alacrity**, **Elemental Reach**, **Earthbound**, **Improved Fire Nova** (Elemental).
- **Maelstrom Weapon**, **Rage of the Farseer**, **Mental Dexterity**, **Mental Quickness**, **Spirit Weapons**, **Improved Stormstrike**, **Shamanistic Focus** (Enhancement).
- **Riptide** (capstone), **Water Shield**, **Mindfulness**, **Natural Grace** (Restoration).
- **Thundering Strikes** is now crit with all spells and attacks — interesting for healers and Elemental too.

## Decisions made in the proposed builds

1. **Resto 0/5/46** keeps its shape; Riptide capstone, Mana Tide at 16.
2. **Elemental 31/0/20**: Lava Burst + Lightning Overload + Alacrity, Mana Tide from Restoration.
3. **Enhancement 7/34/10**: rebuilt as a melee DPS (the support build is obsolete).
4. **PvP Elemental 30/0/21**: Reverberation + Earthbound + Nature's Swiftness.

## To verify at launch

- Two-handers / dual wield for shamans (Two-Handed Axes and Maces is gone).
- Totem radius without Totemic Mastery.
- Lava Burst 192-248 at 60 (buffed in 70009), Riptide 485-533 plus 445, Maelstrom Weapon 4%/point confirmed; Elemental Alacrity 0.5s.
- Windfury Totem was lowered (95/179/246 AP vs Classic 122/229/315).
