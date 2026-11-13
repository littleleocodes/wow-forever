# WoW: Forever class guides

The best talents and the best way to play every class in **World of Warcraft: Forever** (the Classic+ release, launching 2026-11-04), worked out from the beta's talent trees and simulations: the community's combat simulator for raids and this project's own simulators for leveling and healing.

**How to use it:** pick your class below. Its page has a grid of every spec against the two modes (leveling, raid), the recommended picks marked, and a ranking of the specs for each mode. Every link in the grid opens a build page: the talents (with a talent calculator link), the order to take them while leveling, and what to press.

| Class | Roles | Fastest leveling (solo) | Most raid damage (DPS in a full raid) | Raid healing | Raid tanking |
|---|---|---|---|---|---|
| [**Druid**](druid/README.md) | damage, tank, healer | [Feral Combat](druid/leveling/feral-combat.md) (23 s/kill) | [Feral Combat](druid/raid/feral-combat.md) (914 DPS) | [Restoration](druid/raid/restoration.md) | [Feral Combat](druid/raid/feral-combat.md) (Feral Combat (optimized, tank)) |
| [**Hunter**](hunter/README.md) | damage | [Beast-Survival](hunter/leveling/beast-survival.md) (21 s/kill), [Survival](hunter/leveling/survival.md) (22 s/kill) | [Beast Mastery](hunter/raid/beast-mastery.md) (1003 DPS), [Marksmanship](hunter/raid/marksmanship.md) (997 DPS), [Beast-Marks](hunter/raid/beast-marks.md) (992 DPS) | - | - |
| [**Mage**](mage/README.md) | damage | [Arcane-Frost](mage/leveling/arcane-frost.md) (29 s/kill) | [Fire](mage/raid/fire.md) (855 DPS) | - | - |
| [**Paladin**](paladin/README.md) | damage, tank, healer | [Retribution](paladin/leveling/retribution.md) (26 s/kill), [Prot-Ret](paladin/leveling/prot-ret.md) (26 s/kill) | [Retribution](paladin/raid/retribution.md) (817 DPS), [Shockadin](paladin/raid/shockadin.md) (805 DPS) | [Holy](paladin/raid/holy.md) | [Protection](paladin/raid/protection.md) |
| [**Priest**](priest/README.md) | damage, healer | [Shadow](priest/leveling/shadow.md) (24 s/kill) | [Shadow](priest/raid/shadow.md) (761 DPS) | [Holy](priest/raid/holy.md) (capacity 0.69), [Discipline](priest/raid/discipline.md) (capacity 0.65) | - |
| [**Rogue**](rogue/README.md) | damage | [Combat](rogue/leveling/combat.md) (21 s/kill), [Combat-Subtlety](rogue/leveling/combat-subtlety.md) (21 s/kill) | [Assassination](rogue/raid/assassination.md) (833 DPS) | - | - |
| [**Shaman**](shaman/README.md) | damage, healer | [Enhancement](shaman/leveling/enhancement.md) (25 s/kill) | [Enhancement](shaman/raid/enhancement.md) (985 DPS) | [Restoration](shaman/raid/restoration.md) | - |
| [**Warlock**](warlock/README.md) | damage | [Affliction-Demonology](warlock/leveling/affliction-demonology.md) (30 s/kill), [Demonology](warlock/leveling/demonology.md) (31 s/kill) | [Demonology](warlock/raid/demonology.md) (851 DPS) | - | - |
| [**Warrior**](warrior/README.md) | damage, tank | [Fury](warrior/leveling/fury.md) (25 s/kill), [Arms](warrior/leveling/arms.md) (25 s/kill) | [Fury](warrior/raid/fury.md) (858 DPS), [Arms](warrior/raid/arms.md) (852 DPS) | - | [Protection](warrior/raid/protection.md) |

Several specs in one damage or leveling cell share the recommendation: each is within 3% of the class's best spec in that column, a tie in the simulations. Leveling times compare across classes: every class runs in the same fight simulator, solo against same-level mobs. Raid numbers assume a group: every raid buff and debuff is up, which is where classes that live on raid buffs (warriors' rage, hunters' and shamans' mana) do their real damage. Healers are ranked within their class by the healer lab's capacity (this project's healing model; healers are not in the community simulator); tanks are listed, not ranked.

## How to read the numbers

- **Full raid DPS** (what raid pages rank and recommend on): your personal damage against a raid boss over a 3-minute fight with every raid buff and debuff up, as in a real raid group. Each spec's raid page shows where its raid gain comes from (mana, armor debuffs, physical buffs, spell buffs).
- **Seconds per kill** (leveling): a whole kill cycle against same-level mobs, including eating and drinking.
- **✅ Recommended**: the best spec for that mode in its class, or within 3% of it. **⚗**: a generated build (a starting point).
- Everything is a simulation of the beta, not a measurement in the game. Treat differences under 2-3% as a tie.

## Everything else

- [Tier list](tier-list.md): every spec of every class in S/A/B/C tiers for raid damage and healing (the tanks listed), from the same picks and numbers as the class pages.
- [Raid DPS rankings by gear tier](_reference/dps-rankings.md): every raid damage spec in pre-BiS and phase-1 BiS gear, in a full raid, with its best talents and gear for each.
- [_reference/README.md](_reference/README.md): how the project works, its tools and its rules.
- [_reference/](_reference/): cross-class reports (simulator summaries, the talentsforever.com comparison, launch checklists).
- Each class's `research/` folder: every build, report and simulation behind its pages.

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

