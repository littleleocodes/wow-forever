# Hunter — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [../../spells/README.md](../../spells/README.md). Point-by-point audit of every
Classic build: [baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), rendered under
[../../leveling/builds/](../../leveling/builds/), [../../raid/builds/](../../raid/builds/) and [../../pvp/builds/](../../pvp/builds/).

## What broke

| Classic talent | Forever (build 70291) | Impact on Classic builds |
|---|---|---|
| Improved Aspect of the Hawk (Beast Mastery tier 1) | **Removed** → *Deadly Aspects* (5 ranks, 2% a rank): the Hawk proc, plus a melee version under Aspect of the Beast | Direct replacement |
| Lethal Shots (Marksmanship tier 2) | **Removed** → *Lethal Attacks* (tier 1, crit with all attacks) | Direct replacement, one tier earlier |
| Aimed Shot (Marksmanship tier 3) | **Removed** as a talent: trained from level 20 (6 ranks, 2 s cast, +166 at 60, 6 s cooldown shared with Multi-Shot) | Sniper Shot is the new capstone shot |
| Improved Hunter's Mark | **Removed** | 5 points freed in every raid build |
| Improved Serpent Sting / Improved Scorpid Sting | **Removed** → *Improved Stings* (3 ranks) | |
| Mortal Shots | Requires 5 points in **Careful Aim** (attack power from Intellect) | Careful Aim is mandatory for Marksmanship |
| Trueshot Aura | Tier 7 → **tier 4**, one rank, a party buff you cast | Cheaper |
| Monster Slaying / Humanoid Slaying | **Removed** → *Improved Tracking* (5 ranks, +1% a rank against the tracked type) | Works on every tracked type |
| Killer Instinct, Trap Mastery, Improved Feign Death, Wyvern Sting | **Removed** | Survival is now a melee tree |
| Thick Hide, Improved Eyes of the Beast | **Removed** | |
| Intimidation | Requires Bestial Swiftness | Beast Mastery builds take Bestial Swiftness |
| Efficiency | 3% a rank (Classic 2%) | Better |

## What's new and matters

- **Lone Wolf** (Marksmanship tier 3): +20% damage with no pet out.
- **Careful Aim**, **Lethal Attacks**, **Sniper Shot**, **Rapid Killing** and **Rapid Recuperation** (Rapid Fire and mana).
- **Focused Fire** (+2% damage with a pet), **Summon Hawk** (Beast Mastery tier 4, shares Arcane Shot's cooldown), **Deadly Aspects**.
- **Predator's Edge**, **Expose Prey**, **Strider Kick**, **Lacerating Strikes**, **Resourcefulness**, **Survivalist's Discipline**: melee
  Survival.

Which builds won: the player pages, [leveling](../../../leveling/README.md) and [raid](../../../raid/README.md).

## To verify at launch

- Trueshot Aura's spell ranks: the 70291 tooltip reads rank 5 at +50, below rank 4's +75.
- Lone Wolf against a pet in raid conditions, and whether hawks count as pets for Lone Wolf.
- Pet scaling (this project uses the 70291 client's numbers: 10% of the higher attack power, all of the crit).
