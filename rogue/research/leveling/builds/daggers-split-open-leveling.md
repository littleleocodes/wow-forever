# Daggers (split) — Leveling (open talent search) — 22/16/13

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/16/13 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (an Assassination/Combat hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). +3.1% faster per kill than opt-combat-swords-raid-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 2/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 8%. |
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
| **Camouflage** | 3/5 | changed | Reduces your speed penalty from your Stealth ability by 9% and reduces its cooldown by 4 sec. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Improved Ambush** | 2/3 | moved | Increases the critical strike chance of your Ambush ability by 30%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12-14 | Combat | Lightning Reflexes | 3 | 0/3/2 |
| 15-16 | Combat | Improved Eviscerate | 2 | 0/5/2 |
| 17-19 | Combat | Precision | 3 | 0/8/2 |
| 20-22 | Combat | Deflection | 3 | 0/11/2 |
| 23 | Combat | Riposte | 1 | 0/12/2 |
| 24 | Combat | Improved Eviscerate | 1 | 0/13/2 |
| 25-26 | Combat | Improved Sinister Strike | 2 | 0/15/2 |
| 27 | Combat | Flawless Execution | 1 | 0/16/2 |
| 28-30 | Subtlety | Camouflage | 3 | 0/16/5 |
| 31-32 | Subtlety | Improved Ambush | 2 | 0/16/7 |
| 33-35 | Subtlety | Setup | 3 | 0/16/10 |
| 36-38 | Subtlety | Initiative | 3 | 0/16/13 |
| 39-43 | Assassination | Malice | 5 | 5/16/13 |
| 44-45 | Assassination | Murder | 2 | 7/16/13 |
| 46-48 | Assassination | Ruthlessness | 3 | 10/16/13 |
| 49 | Assassination | Relentless Strikes | 1 | 11/16/13 |
| 50-51 | Assassination | Remorseless Attacks | 2 | 13/16/13 |
| 52-53 | Assassination | Lethality | 2 | 15/16/13 |
| 54-58 | Assassination | Improved Poisons | 5 | 20/16/13 |
| 59 | Assassination | Cold Blood | 1 | 21/16/13 |
| 60 | Assassination | Vigor | 1 | 22/16/13 |

## Core talents (priority order)

1. **Setup** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Eviscerate** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Flawless Execution** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Relentless Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Initiative** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Sinister Strike** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
7. **Precision** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Poisons** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.85; opt-combat-swords-raid-leveling-st 26.65, opt-combat-swords-raid-solo-60 26.65, leveling-combat-swords 27.10. The search simulated 90,763 builds.
- The spec's other leveling builds on the pages: opt-combat-daggers-raid-leveling-st 28.90 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Daggers (split) leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/0253201020151-32303301001-30230023-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
