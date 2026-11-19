# WoW: Forever class guides

The best talents and the best way to play every class in **World of Warcraft: Forever** (the Classic+ release, launching 2026-11-04), worked out from the beta's talent trees and simulations: the community's combat simulator for raids and this project's own simulators for leveling and healing.

**How to use it:** pick your class below. Its page has a grid of every spec against leveling, raid and PvP, the recommended picks marked, and a ranking of the specs for each. Every link in the grid opens a build page: the talents (with a talent calculator link), the order to take them while leveling, and what to press.

| Class | Roles | Fastest leveling (solo) | Most raid damage (DPS in a full raid) | Raid healing | Raid tanking | Most duels won (PvP) |
|---|---|---|---|---|---|---|
| [**Druid**](druid/README.md) | damage, tank, healer | [Feral Combat](druid/leveling/feral-combat.md) (26 s/kill) | [Feral Combat](druid/raid/feral-combat.md) (927 DPS) | [Restoration](druid/raid/restoration.md) | [Feral Combat](druid/raid/feral-combat.md) (Feral Combat (optimized, tank)) | [Restoration](druid/pvp/restoration.md) (44% of duels), [Feral Combat](druid/pvp/feral-combat.md) (42% of duels) |
| [**Hunter**](hunter/README.md) | damage | [Survival](hunter/leveling/survival.md) (21 s/kill), [Beast-Survival](hunter/leveling/beast-survival.md) (21 s/kill) | [Beast Mastery](hunter/raid/beast-mastery.md) (1028 DPS), [Beast-Marks](hunter/raid/beast-marks.md) (1017 DPS), [Marksmanship](hunter/raid/marksmanship.md) (1015 DPS) | - | - | [Beast Mastery](hunter/pvp/beast-mastery.md) (96% of duels) |
| [**Mage**](mage/README.md) | damage | [Arcane-Frost](mage/leveling/arcane-frost.md) (27 s/kill), [Arcane](mage/leveling/arcane.md) (27 s/kill) | [Fire](mage/raid/fire.md) (887 DPS) | - | - | [Arcane](mage/pvp/arcane.md) (52% of duels) |
| [**Paladin**](paladin/README.md) | damage, tank, healer | [Prot-Ret](paladin/leveling/prot-ret.md) (26 s/kill) | [Retribution](paladin/raid/retribution.md) (843 DPS) | [Holy](paladin/raid/holy.md) | [Protection](paladin/raid/protection.md) | [Retribution](paladin/pvp/retribution.md) (83% of duels) |
| [**Priest**](priest/README.md) | damage, healer | [Shadow](priest/leveling/shadow.md) (24 s/kill) | [Shadow](priest/raid/shadow.md) (788 DPS) | [Holy](priest/raid/holy.md) (capacity 0.69), [Discipline](priest/raid/discipline.md) (capacity 0.65) | - | [Shadow](priest/pvp/shadow.md) (84% of duels) |
| [**Rogue**](rogue/README.md) | damage | [Combat](rogue/leveling/combat.md) (20 s/kill), [Combat-Subtlety](rogue/leveling/combat-subtlety.md) (21 s/kill) | [Assassination](rogue/raid/assassination.md) (844 DPS), [Assassination/Subtlety hybrid](rogue/raid/hybrid-assassination-subtlety.md) (822 DPS) | - | - | [Assassination](rogue/pvp/assassination.md) (54% of duels) |
| [**Shaman**](shaman/README.md) | damage, healer | [Enhancement](shaman/leveling/enhancement.md) (26 s/kill) | [Enhancement](shaman/raid/enhancement.md) (797 DPS), [Elemental-Enhancement](shaman/raid/elemental-enhancement.md) (784 DPS) | [Restoration](shaman/raid/restoration.md) | - | [Restoration](shaman/pvp/restoration.md) (73% of duels) |
| [**Warlock**](warlock/README.md) | damage | [Affliction](warlock/leveling/affliction.md) (31 s/kill), [Affliction-Demonology](warlock/leveling/affliction-demonology.md) (31 s/kill), [Demonology](warlock/leveling/demonology.md) (31 s/kill) | [Demonology](warlock/raid/demonology.md) (867 DPS) | - | - | [Demonology](warlock/pvp/demonology.md) (72% of duels) |
| [**Warrior**](warrior/README.md) | damage, tank | [Fury](warrior/leveling/fury.md) (24 s/kill), [Arms](warrior/leveling/arms.md) (25 s/kill) | [Fury](warrior/raid/fury.md) (937 DPS) | - | [Protection](warrior/raid/protection.md) | [Protection](warrior/pvp/protection.md) (56% of duels) |

Several specs in one damage or leveling cell share the recommendation: each is within 3% of the class's best spec in that column, a tie in the simulations. Leveling times compare across classes: every class runs in the same fight simulator, solo against same-level mobs. Raid numbers assume a group: every raid buff and debuff is up, which is where classes that live on raid buffs (warriors' rage, hunters' and shamans' mana) do their real damage. Healers are ranked within their class by the healer lab's capacity (this project's healing model; healers are not in the community simulator); tanks are listed, not ranked.

## How to read the numbers

- **Full raid DPS** (what raid pages rank and recommend on): your personal damage against a raid boss over a 3-minute fight with every raid buff and debuff up, as in a real raid group. Each spec's raid page shows where its raid gain comes from (mana, armor debuffs, physical buffs, spell buffs).
- **Seconds per kill** (leveling): a whole kill cycle against same-level mobs, including eating and drinking.
- **Duels won** (PvP): the share of level-60 one-against-one duels a build wins in this project's duel lab against nine opponents, each class's most-tagged PvP build on talentsforever.com. The lab's AI against itself in an open field: a model of PvP, so no PvP pick is marked recommended; the cell lists the class's best spec and any within 3 points of it.
- **✅ Recommended**: the best spec for that mode in its class, or within 3% of it. **⚗**: a generated build (a starting point).
- Everything is a simulation of the beta, not a measurement in the game. Treat differences under 2-3% as a tie.

## Everything else

- [Tier list](tier-list.md): every spec of every class in S/A/B/C tiers for raid damage and healing (the tanks listed), from the same picks and numbers as the class pages.
- [Raid DPS rankings by gear tier](_reference/dps-rankings.md): every raid damage spec in pre-BiS and raid BiS gear, in a full raid, with its best talents and gear for each.
- [_reference/README.md](_reference/README.md): how the project works, its tools and its rules.
- [_reference/](_reference/): cross-class reports (simulator summaries, the talentsforever.com comparison, launch checklists).
- Each class's `research/` folder: every build, report and simulation behind its pages.

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

