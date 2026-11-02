# Feral Combat/Restoration hybrid — Leveling (open talent search) — 11/31/9

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/31/9 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat/Restoration hybrid (a Feral Combat/Restoration hybrid) leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the feral-cat-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (feral-cat-dps). +0.1% faster per kill than feral-combat-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 1/5 | changed | Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%. |
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Heart of the Wild** | 5/? | ? |  |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Thick Hide** | 1/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1 additional base Armor per level and another 0.67 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/? | ? |  |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Naturalist** | 2/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.2 sec and increases all damage you deal by 4%. |
| **Natural Shapeshifter** | 2/3 | moved | Reduces the mana cost of all shapeshifting by 20%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Feral Combat | Ferocity | 5 | 0/5/0 |
| 15-16 | Feral Combat | Feral Swiftness | 2 | 0/7/0 |
| 17-19 | Feral Combat | Heart of the Wild | 3 | 0/10/0 |
| 20-21 | Feral Combat | Sharpened Claws | 2 | 0/12/0 |
| 22-23 | Feral Combat | Savage Fury | 2 | 0/14/0 |
| 24 | Feral Combat | Heart of the Wild | 1 | 0/15/0 |
| 25-27 | Feral Combat | Predatory Strikes | 3 | 0/18/0 |
| 28-29 | Feral Combat | Blood Frenzy | 2 | 0/20/0 |
| 30 | Feral Combat | Leader of the Pack | 1 | 0/21/0 |
| 31-32 | Feral Combat | Natural Instinct | 2 | 0/23/0 |
| 33 | Feral Combat | Heart of the Wild | 1 | 0/24/0 |
| 34 | Feral Combat | Thick Hide | 1 | 0/25/0 |
| 35-39 | Feral Combat | Rend and Tear | 5 | 0/30/0 |
| 40 | Feral Combat | Berserk | 1 | 0/31/0 |
| 41-45 | Balance | Genesis | 5 | 5/31/0 |
| 46-47 | Balance | Nature's Reach | 2 | 7/31/0 |
| 48-49 | Balance | Nature's Majesty | 2 | 9/31/0 |
| 50-54 | Restoration | Nature's Focus | 5 | 9/31/5 |
| 55-56 | Restoration | Naturalist | 2 | 9/31/7 |
| 57-58 | Restoration | Natural Shapeshifter | 2 | 9/31/9 |
| 59 | Balance | Improved Wrath | 1 | 10/31/9 |
| 60 | Balance | Nature's Splendor | 1 | 11/31/9 |

## Core talents (priority order)

1. **Sharpened Claws** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Blood Frenzy** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Nature's Reach** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ferocity** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Nature's Majesty** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Berserk** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Predatory Strikes** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Leader of the Pack** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 27.80; feral-combat-open-leveling 27.84, opt-feral-cat-dps-leveling-st 27.91, opt-feral-cat-dps-solo-60 27.91, leveling-feral 28.76, restoration-leveling 34.37. The search simulated 54,698 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Feral Combat/Restoration hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/druid/60/15002201-55200102020032012051-50202-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
