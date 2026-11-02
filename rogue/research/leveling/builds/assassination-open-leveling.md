# Assassination — Leveling (open talent search) — 30/19/2

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/19/2 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Assassination leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). +0.9% faster per kill than opt-combat-swords-raid-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 2/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 8%. |
| **Vile Poisons** | 1/5 | moved | Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 5/5 | changed | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |
| **Vigor** | 2/2 | changed | Increases your maximum Energy by 10. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |
| **Seal Fate** | 5/5 | moved | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Combat (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Improved Sprint** | 2/2 | unchanged | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 3/5 | changed | Increases the damage done by your off-hand weapon by 15%. |

### Subtlety (2)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12-16 | Assassination | Malice | 5 | 5/0/2 |
| 17-18 | Assassination | Ruthlessness | 2 | 7/0/2 |
| 19 | Assassination | Murder | 1 | 8/0/2 |
| 20 | Assassination | Ruthlessness | 1 | 9/0/2 |
| 21 | Assassination | Murder | 1 | 10/0/2 |
| 22 | Assassination | Relentless Strikes | 1 | 11/0/2 |
| 23-24 | Assassination | Remorseless Attacks | 2 | 13/0/2 |
| 25-26 | Assassination | Lethality | 2 | 15/0/2 |
| 27 | Assassination | Cold Blood | 1 | 16/0/2 |
| 28 | Assassination | Vile Poisons | 1 | 17/0/2 |
| 29-31 | Assassination | Improved Poisons | 3 | 20/0/2 |
| 32 | Assassination | Mutilate | 1 | 21/0/2 |
| 33-35 | Combat | Lightning Reflexes | 3 | 21/3/2 |
| 36-37 | Combat | Improved Eviscerate | 2 | 21/5/2 |
| 38-40 | Combat | Precision | 3 | 21/8/2 |
| 41-43 | Combat | Deflection | 3 | 21/11/2 |
| 44 | Combat | Riposte | 1 | 21/12/2 |
| 45 | Combat | Improved Eviscerate | 1 | 21/13/2 |
| 46-47 | Combat | Improved Sprint | 2 | 21/15/2 |
| 48 | Combat | Flawless Execution | 1 | 21/16/2 |
| 49-51 | Combat | Dual Wield Specialization | 3 | 21/19/2 |
| 52-53 | Assassination | Vigor | 2 | 23/19/2 |
| 54-55 | Assassination | Improved Poisons | 2 | 25/19/2 |
| 56-60 | Assassination | Seal Fate | 5 | 30/19/2 |

## Core talents (priority order)

1. **Mutilate** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Eviscerate** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Malice** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Improved Poisons** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Flawless Execution** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Remorseless Attacks** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Relentless Strikes** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 26.31; opt-combat-swords-raid-leveling-st 26.55, opt-combat-swords-raid-solo-60 26.55, leveling-combat-swords 26.89. The search simulated 47,680 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Assassination leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/0253201021152105-303033012013-002-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
