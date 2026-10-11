# Feral Combat — Leveling (open talent search) — 11/31/9

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/31/9 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat leveling build the open leveling search found on 2026-10-11: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the feral-cat-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (feral-cat-dps). +3.8% faster per kill than leveling-feral, the fastest of our leveling builds in that race.

## Point allocation

### Balance (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Wrath** | 1/5 | changed | Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%. |
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Nature's Splendor** | 1/1 | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. |

### Feral Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Thick Hide** | 1/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1 additional base Armor per level and another 0.67 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/1 | **NEW** | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec. |

### Restoration (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 1/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%. |
| **Natural Shapeshifter** | 3/3 | moved | Reduces the mana cost of all shapeshifting by 30%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Feral Combat | Ferocity | 5 | 0/5/0 |
| 15 | Feral Combat | Thick Hide | 1 | 0/6/0 |
| 16-17 | Feral Combat | Feral Swiftness | 2 | 0/8/0 |
| 18-19 | Feral Combat | Heart of the Wild | 2 | 0/10/0 |
| 20-21 | Feral Combat | Sharpened Claws | 2 | 0/12/0 |
| 22-23 | Feral Combat | Savage Fury | 2 | 0/14/0 |
| 24 | Feral Combat | Heart of the Wild | 1 | 0/15/0 |
| 25-27 | Feral Combat | Predatory Strikes | 3 | 0/18/0 |
| 28-29 | Feral Combat | Heart of the Wild | 2 | 0/20/0 |
| 30 | Feral Combat | Leader of the Pack | 1 | 0/21/0 |
| 31-32 | Feral Combat | Natural Instinct | 2 | 0/23/0 |
| 33-34 | Feral Combat | Blood Frenzy | 2 | 0/25/0 |
| 35-39 | Feral Combat | Rend and Tear | 5 | 0/30/0 |
| 40 | Feral Combat | Berserk | 1 | 0/31/0 |
| 41-45 | Balance | Genesis | 5 | 5/31/0 |
| 46-47 | Balance | Nature's Reach | 2 | 7/31/0 |
| 48-49 | Balance | Nature's Majesty | 2 | 9/31/0 |
| 50-54 | Restoration | Nature's Focus | 5 | 9/31/5 |
| 55 | Restoration | Naturalist | 1 | 9/31/6 |
| 56-58 | Restoration | Natural Shapeshifter | 3 | 9/31/9 |
| 59 | Balance | Improved Wrath | 1 | 10/31/9 |
| 60 | Balance | Nature's Splendor | 1 | 11/31/9 |

## Core talents (priority order)

1. **Blood Frenzy** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Ferocity** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Sharpened Claws** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Natural Shapeshifter** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
5. **Nature's Reach** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Berserk** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Nature's Splendor** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Nature's Majesty** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +3.8% faster than the hand draft leveling-feral, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 28.55; leveling-feral 29.64, opt-feral-cat-dps-leveling-st 29.71, opt-feral-cat-dps-solo-60 29.71, restoration-leveling 36.04. The search simulated 52,802 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Feral Combat leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/druid/60/15002201-55200102020032012051-50103-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
