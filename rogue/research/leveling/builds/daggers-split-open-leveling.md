# Daggers (split) — Leveling (open talent search) — 16/27/8

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/27/8 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (an Assassination/Combat hybrid) leveling build the open leveling search found on 2026-10-24: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). +3.8% faster per kill than opt-combat-swords-raid-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Improved Slice and Dice** | 2/3 | unchanged | Increases the duration of your Slice and Dice ability by 30%. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |

### Combat (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 4/5 | changed | Increases the damage done by your off-hand weapon by 20%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 4/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 4% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 4%.   Mace: Your attacks ignore 12% of  your target's armor. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |

### Subtlety (8)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Camouflage** | 1/5 | changed | Reduces your speed penalty from your Stealth ability by 3% and reduces its cooldown by 2 sec. |
| **Master of Deception** | 2/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 2 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12-16 | Assassination | Malice | 5 | 5/0/2 |
| 17-18 | Assassination | Ruthlessness | 2 | 7/0/2 |
| 19-20 | Assassination | Murder | 2 | 9/0/2 |
| 21 | Assassination | Ruthlessness | 1 | 10/0/2 |
| 22 | Assassination | Relentless Strikes | 1 | 11/0/2 |
| 23 | Subtlety | Camouflage | 1 | 11/0/3 |
| 24-25 | Subtlety | Master of Deception | 2 | 11/0/5 |
| 26-27 | Assassination | Remorseless Attacks | 2 | 13/0/5 |
| 28-30 | Subtlety | Setup | 3 | 13/0/8 |
| 31-32 | Assassination | Improved Slice and Dice | 2 | 15/0/8 |
| 33 | Assassination | Cold Blood | 1 | 16/0/8 |
| 34-36 | Combat | Lightning Reflexes | 3 | 16/3/8 |
| 37-38 | Combat | Improved Eviscerate | 2 | 16/5/8 |
| 39-41 | Combat | Precision | 3 | 16/8/8 |
| 42-44 | Combat | Deflection | 3 | 16/11/8 |
| 45 | Combat | Riposte | 1 | 16/12/8 |
| 46 | Combat | Improved Eviscerate | 1 | 16/13/8 |
| 47-48 | Combat | Improved Sinister Strike | 2 | 16/15/8 |
| 49 | Combat | Flawless Execution | 1 | 16/16/8 |
| 50-53 | Combat | Dual Wield Specialization | 4 | 16/20/8 |
| 54 | Combat | Blade Flurry | 1 | 16/21/8 |
| 55-58 | Combat | Hack and Slash | 4 | 16/25/8 |
| 59-60 | Combat | Weapon Expertise | 2 | 16/27/8 |

## Core talents (priority order)

1. **Setup** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Flawless Execution** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Relentless Strikes** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ruthlessness** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Sinister Strike** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Weapon Expertise** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malice** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 26.66; opt-combat-swords-raid-leveling-st 27.67, opt-combat-swords-raid-solo-60 27.67, leveling-combat-swords 27.68. The search simulated 85,534 builds.
- The spec's other leveling builds on the pages: opt-combat-daggers-raid-leveling-st 29.67 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Daggers (split) leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/02532210001-323033010014142-1223-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
