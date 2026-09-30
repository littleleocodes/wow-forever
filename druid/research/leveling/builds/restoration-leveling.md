# Restoration — Leveling (derived) — 0/21/30

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/21/30 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Restoration leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Restoration build, 30+ points kept in Restoration, playing the feral-cat-dps rotation; the talent order is the stats model's (feral-cat-dps). Restoration is a healing spec: this is how to level while keeping it, compared with Feral Combat on the leveling page.

## Point allocation

### Balance (0)

*No points.*

### Feral Combat (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Heart of the Wild** | 3/5 | changed | Increases your Intellect by 6%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 12% and while in Cat Form your Strength is increased by 6%. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **King of the Jungle** | 1/3 | **NEW** | Tiger's Fury now instantly grants you 20 Energy. |

### Restoration (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 2/5 | changed | Gives you a 28% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when you shapeshift into Bear Form or Dire Bear Form. When you shift into Cat Form, you will regain 100% of the Energy you had when you were last in Cat Form, plus 10 Energy for each second you spent not in Bear Form, Cat Form, or Dire Bear Form, up to a maximum of 100 Energy. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Natural Shapeshifter** | 3/3 | moved | Reduces the mana cost of all shapeshifting by 30%. |
| **Tranquil Spirit** | 5/5 | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |
| **Living Spirit** | 3/3 | **NEW** | Increases your Spirit by 15%. |
| **Improved Rejuvenation** | 3/3 | moved | Increases the effect of your Rejuvenation spell by 15%. |
| **Gift of Nature** | 3/5 | changed | Increases the effect of all your healing spells by 6%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Feral Combat | Ferocity | 5 | 0/5/0 |
| 15-17 | Feral Combat | Thick Hide | 3 | 0/8/0 |
| 18-19 | Feral Combat | Feral Swiftness | 2 | 0/10/0 |
| 20-21 | Feral Combat | Savage Fury | 2 | 0/12/0 |
| 22-23 | Feral Combat | Sharpened Claws | 2 | 0/14/0 |
| 24 | Feral Combat | Heart of the Wild | 1 | 0/15/0 |
| 25-27 | Feral Combat | Predatory Strikes | 3 | 0/18/0 |
| 28-29 | Feral Combat | Heart of the Wild | 2 | 0/20/0 |
| 30 | Feral Combat | King of the Jungle | 1 | 0/21/0 |
| 31-32 | Restoration | Nature's Focus | 2 | 0/21/2 |
| 33-35 | Restoration | Furor | 3 | 0/21/5 |
| 36-40 | Restoration | Naturalist | 5 | 0/21/10 |
| 41-43 | Restoration | Natural Shapeshifter | 3 | 0/21/13 |
| 44-45 | Restoration | Furor | 2 | 0/21/15 |
| 46 | Restoration | Swiftmend | 1 | 0/21/16 |
| 47-51 | Restoration | Tranquil Spirit | 5 | 0/21/21 |
| 52-54 | Restoration | Living Spirit | 3 | 0/21/24 |
| 55-57 | Restoration | Improved Rejuvenation | 3 | 0/21/27 |
| 58-60 | Restoration | Gift of Nature | 3 | 0/21/30 |

## Core talents (priority order)

1. **Naturalist** — The scorer's value in this build: +16.2% of its score (model feral-cat-dps).
2. **Sharpened Claws** — The scorer's value in this build: +13.9% of its score (model feral-cat-dps).
3. **Predatory Strikes** — The scorer's value in this build: +12.4% of its score (model feral-cat-dps).
4. **Savage Fury** — The scorer's value in this build: +10.9% of its score (model feral-cat-dps).
5. **King of the Jungle** — The scorer's value in this build: +10.0% of its score (model feral-cat-dps).
6. **Ferocity** — The scorer's value in this build: +7.2% of its score (model feral-cat-dps).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start derived-restoration-scorer, moves: 3 points Nature's Focus -> Improved Rejuvenation; 3 points Subtlety -> Gift of Nature. Race against derived-restoration-scorer over levels 20-60 (seed 3, 3000 fights per level): +0.9% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- A derived Restoration leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
