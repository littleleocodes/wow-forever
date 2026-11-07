# Feral Combat — Leveling (open talent search) — 11/29/11

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/29/11 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the feral-cat-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (feral-cat-dps). +0.5% faster per kill than opt-feral-cat-dps-solo-60, the fastest of our leveling builds in that race.

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 1/5 | changed | Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%. |
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 10%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Furor** | 1/5 | changed | Gives you a 20% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20% of the Energy you had when last in Cat Form, plus 2 Energy per second spent outside Bear Form or Dire Bear Form, up to 20 Energy. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Brutal Impact** | 1/2 | changed | Increases the stun duration of your Bash and Pounce abilities by 0.5 sec and reduces the cooldown of Bash by 15 sec. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 4/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 12%. |

### Restoration (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Natural Shapeshifter** | 1/3 | moved | Reduces the mana cost of all shapeshifting by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Feral Combat | Ferocity | 5 | 0/5/0 |
| 15-16 | Feral Combat | Feral Swiftness | 2 | 0/7/0 |
| 17-19 | Feral Combat | Thick Hide | 3 | 0/10/0 |
| 20-21 | Feral Combat | Sharpened Claws | 2 | 0/12/0 |
| 22-23 | Feral Combat | Savage Fury | 2 | 0/14/0 |
| 24 | Feral Combat | Furor | 1 | 0/15/0 |
| 25-27 | Feral Combat | Predatory Strikes | 3 | 0/18/0 |
| 28-29 | Feral Combat | Blood Frenzy | 2 | 0/20/0 |
| 30 | Feral Combat | Leader of the Pack | 1 | 0/21/0 |
| 31-35 | Balance | Genesis | 5 | 5/21/0 |
| 36-37 | Balance | Nature's Reach | 2 | 7/21/0 |
| 38-39 | Balance | Nature's Majesty | 2 | 9/21/0 |
| 40-41 | Feral Combat | Natural Instinct | 2 | 9/23/0 |
| 42-46 | Restoration | Heart of the Wild | 5 | 9/23/5 |
| 47-51 | Restoration | Naturalist | 5 | 9/23/10 |
| 52 | Restoration | Natural Shapeshifter | 1 | 9/23/11 |
| 53 | Feral Combat | Brutal Impact | 1 | 9/24/11 |
| 54 | Feral Combat | Feral Charge | 1 | 9/25/11 |
| 55-58 | Feral Combat | Rend and Tear | 4 | 9/29/11 |
| 59 | Balance | Improved Wrath | 1 | 10/29/11 |
| 60 | Balance | Nature's Splendor | 1 | 11/29/11 |

## Core talents (priority order)

1. **Naturalist** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
2. **Sharpened Claws** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Ferocity** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Blood Frenzy** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Nature's Reach** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Predatory Strikes** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
7. **Nature's Majesty** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Savage Fury** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +0.9% faster than the hand draft leveling-feral, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.86; opt-feral-cat-dps-solo-60 22.98, opt-feral-cat-dps-leveling-st 23.00, leveling-feral 23.06, restoration-leveling 28.49. The search simulated 46,777 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Feral Combat leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/druid/60/15002201-51201302123002124-05501-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
