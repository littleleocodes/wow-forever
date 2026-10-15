# Druid — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08 (`_reference/data/data_build.py`; trees in
[talent-trees.md](talent-trees.md)). Spellbook numbers: [../../spells/README.md](../../spells/README.md). Point-by-point audit of every
Classic build: [baseline-audit.md](baseline-audit.md). Builds: [proposed-builds.json](proposed-builds.json), rendered under
[../../leveling/builds/](../../leveling/builds/), [../../raid/builds/](../../raid/builds/) and [../../pvp/builds/](../../pvp/builds/).
What to play: the player pages, [leveling](../../../leveling/README.md) and [raid](../../../raid/README.md).

## What broke

| Classic talent | Forever | Impact on Classic builds |
|---|---|---|
| Omen of Clarity (Balance) | **Removed**: a baseline passive at 20 that also procs from spells | The Feral Balance dip loses its main reason |
| Natural Weapons (Balance) | **Removed** | Feral loses +10% physical damage; Naturalist (Restoration, +5% all damage) is the nearest replacement |
| Nature's Grasp, Improved Nature's Grasp, Improved Thorns | **Removed** (Nature's Grasp is a baseline spell at 10) | Balance tier-1 fillers gone |
| Improved Healing Touch, Improved Mark of the Wild, Improved Enrage (Restoration) | **Removed**; Naturalist (-0.1 sec Healing Touch and +1% damage a rank) takes Improved Healing Touch's cast-time job | Healer points freed |
| Feral Aggression, Feline Swiftness, Improved Shred, Primal Fury, Faerie Fire (Feral) | **Removed**; Feral Swiftness, Shredding Attacks (18 energy off Shred) and Blood Frenzy (now also Primal Fury's rage) cover them; Faerie Fire is free in forms | Cat build rebuilt |
| Heart of the Wild | Feral tier 6 → **tier 1** (Intellect, bear Stamina, cat Strength) | Every Feral build takes it first |
| Insect Swarm | Restoration → **Balance tier 4** | |
| Swiftmend | Capstone → **Restoration tier 4**; its tooltip no longer says it uses up the heal over time | Every healer takes it |
| Nature's Swiftness, Improved Regrowth | Require 5 points in Naturalist / 3 in Improved Rejuvenation | |
| Nature's Grace | Classic's -0.5 sec on the next cast → 10% faster casts and global cooldown for 3 sec | The Classic Regrowth build loses its engine |
| Sharpened Claws | 3 ranks → 2 ranks (3% a rank) | Cheaper |
| Furor | A chance at 40 energy → keeps 20% a rank of the Cat Form energy you left with, plus 2 a rank per second out of form | Powershifting for energy is gone |

## What's new and matters

- **Balance:** Genesis (periodic damage and healing), Nature's Majesty (spell and melee crit), Nature's Splendor, Eclipse (each Wrath
  shortens the next two Starfires), Overgrowth.
- **Feral Combat:** Shifting Power and Improved Shifting Power (mana into energy: the raid cat's main talent in the simulator),
  Shredding Attacks, Primal Bite (bear only), Natural Instinct, Natural Reaction, Rend and Tear, Berserk.
- **Restoration:** Naturalist, Gift of the Earthmother, Living Spirit, Wild Growth.

## To verify at launch

- Furor's energy retention and the Wolfshead Helm.
- Tiger's Fury: not in the trainer list; the community simulator reads it from the client as granted.
- Swiftmend not consuming the heal over time; Wild Growth's numbers and target cap.
- Eclipse's charge mechanics.
