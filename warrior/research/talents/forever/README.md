# Warrior — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [../../spells/README.md](../../spells/README.md). Point-by-point audit of every
Classic build: [baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), rendered under
[../../leveling/builds/](../../leveling/builds/), [../../raid/builds/](../../raid/builds/) and [../../pvp/builds/](../../pvp/builds/).
What to play: the player pages, [leveling](../../../leveling/README.md) and [raid](../../../raid/README.md).

## What broke

| Classic talent | Forever | Impact on Classic builds |
|---|---|---|
| Tactical Mastery (Arms) | **Removed**: a baseline passive at 14 keeps 10 rage; Improved Tactical Mastery (5 ranks, up to 15 more) takes the slot and is the prerequisite for Anger Management | Arms dips keep their shape with the new talent |
| Axe, Mace, Sword and Polearm Specialization | **Removed**: Weaponmaster (Arms, 5 ranks): axe or polearm crit, mace or staff armor ignored, sword extra attacks | Arms builds take Weaponmaster |
| Improved Battle Shout, Improved Demoralizing Shout (Fury) | **Removed** | Classic Fury builds lose 5 points of tier-3 filler |
| Improved Cleave (Fury) | Now **Furious Precision**: +10% off-hand hit | A dual-wield talent |
| Classic Iron Will | Its Fury slot is now **Lingering Rage** (slower rage decay out of combat); a new Iron Will in Protection shortens stuns and fears | |
| Improved Slam | Fury → **Arms** row 6, 2 ranks: 0.5 sec off the cast and global cooldown, 3 sec off the cooldown, no swing delay | The two-handed raid build becomes an Arms build |
| Improved Thunder Clap | Arms → **Protection** | A tank talent |
| Toughness, Improved Shield Block, Improved Taunt, One-Handed Weapon Specialization (Protection) | **Removed** | Bastion (+10% damage with a shield) is the new tank multiplier |

## What's new and matters

- **Arms:** Bloodthrill (main-hand hits on a target with your Rend light up Overpower), Weaponmaster, Spearing Strike (+80% weapon damage
  against Giants, Dragonkin and mounted targets).
- **Fury:** Raging Blows (3 rage off Cleave and Whirlwind), Gore Drinker; Whirlwind hits with both weapons, Flurry needs Death Wish.
- **Protection:** Master of Defense (rage from dodges and parries), Vanguard (Charge in Defensive Stance), Focused Rage, Bastion, Iron Will.

## To verify at launch

- Sunder Armor's threat and the attack power shares Forever adds to Rend, Revenge and Thunder Clap.
- Whether a Bloodthrill window and a dodge window for Overpower stack.
