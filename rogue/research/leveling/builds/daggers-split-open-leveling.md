# Daggers (split) — Leveling (open talent search) — 22/16/13

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/16/13 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (a Assassination/Combat hybrid) leveling build the open leveling search found on 2026-10-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-swords-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +1.7% faster per kill than opt-combat-swords-raid-leveling-aoe, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 2/3 | unchanged | Gives your finishing moves a 40% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 3/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 12%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Vigor** | 1/2 | changed | Increases your maximum Energy by 5. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |

### Subtlety (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Camouflage** | 1/5 | changed | Reduces your speed penalty from your Stealth ability by 3% and reduces its cooldown by 2 sec. |
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 1/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 5%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 2/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Combat | Improved Sinister Strike | 2 | 0/2/0 |
| 12-14 | Combat | Improved Eviscerate | 3 | 0/5/0 |
| 15 | Combat | Deflection | 1 | 0/6/0 |
| 16-17 | Combat | Precision | 2 | 0/8/0 |
| 18-19 | Combat | Deflection | 2 | 0/10/0 |
| 20 | Combat | Riposte | 1 | 0/11/0 |
| 21 | Combat | Precision | 1 | 0/12/0 |
| 22-24 | Combat | Lightning Reflexes | 3 | 0/15/0 |
| 25 | Combat | Flawless Execution | 1 | 0/16/0 |
| 26 | Subtlety | Opportunity | 1 | 0/16/1 |
| 27-29 | Subtlety | Master of Deception | 3 | 0/16/4 |
| 30 | Subtlety | Camouflage | 1 | 0/16/5 |
| 31-33 | Subtlety | Setup | 3 | 0/16/8 |
| 34-35 | Subtlety | Elusiveness | 2 | 0/16/10 |
| 36-38 | Subtlety | Initiative | 3 | 0/16/13 |
| 39-40 | Assassination | Remorseless Attacks | 2 | 2/16/13 |
| 41-45 | Assassination | Malice | 5 | 7/16/13 |
| 46-47 | Assassination | Murder | 2 | 9/16/13 |
| 48 | Assassination | Ruthlessness | 1 | 10/16/13 |
| 49 | Assassination | Relentless Strikes | 1 | 11/16/13 |
| 50-52 | Assassination | Lethality | 3 | 14/16/13 |
| 53 | Assassination | Ruthlessness | 1 | 15/16/13 |
| 54 | Assassination | Cold Blood | 1 | 16/16/13 |
| 55-58 | Assassination | Improved Poisons | 4 | 20/16/13 |
| 59 | Assassination | Vigor | 1 | 21/16/13 |
| 60 | Assassination | Improved Poisons | 1 | 22/16/13 |

## Core talents (priority order)

1. **Setup** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Sinister Strike** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Eviscerate** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Precision** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Relentless Strikes** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Flawless Execution** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malice** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.13; opt-combat-swords-raid-leveling-aoe 25.56, combat-leveling 25.57. The search simulated 94,682 builds.
- The spec's other leveling builds on the pages: opt-combat-daggers-raid-leveling-st 29.55 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Daggers (split) leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/0252201030151-32303301001-13132003-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
