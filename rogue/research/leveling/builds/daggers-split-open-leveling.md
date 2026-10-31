# Daggers (split) — Leveling (open talent search) — 22/16/13

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/16/13 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Daggers (split) (an Assassination/Combat hybrid) leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-daggers-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-daggers-raid). +2.4% faster per kill than opt-combat-swords-raid-leveling-st, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Ruthlessness** | 3/3 | unchanged | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Improved Expose Armor** | 1/2 | changed | Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points. |
| **Lethality** | 1/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%. |
| **Cold Blood** | 1/1 | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. |
| **Improved Poisons** | 4/5 | changed | Increases the chance to apply Poisons to your target by 8%, and gives Poison applications a 40% chance to not consume a charge. |
| **Vigor** | 1/2 | changed | Increases your maximum Energy by 5. |
| **Mutilate** | 1/1 | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. |

### Combat (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |

### Subtlety (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Master of Deception** | 3/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2/2 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |
| **Setup** | 3/3 | changed | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 1/2 | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 45 sec. |
| **Improved Ambush** | 1/3 | moved | Increases the critical strike chance of your Ambush ability by 15%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Assassination | Malice | 5 | 5/0/0 |
| 15-16 | Assassination | Ruthlessness | 2 | 7/0/0 |
| 17 | Assassination | Murder | 1 | 8/0/0 |
| 18 | Assassination | Ruthlessness | 1 | 9/0/0 |
| 19 | Assassination | Murder | 1 | 10/0/0 |
| 20 | Assassination | Relentless Strikes | 1 | 11/0/0 |
| 21-22 | Assassination | Remorseless Attacks | 2 | 13/0/0 |
| 23 | Assassination | Lethality | 1 | 14/0/0 |
| 24 | Assassination | Improved Expose Armor | 1 | 15/0/0 |
| 25 | Assassination | Cold Blood | 1 | 16/0/0 |
| 26-29 | Assassination | Improved Poisons | 4 | 20/0/0 |
| 30 | Assassination | Mutilate | 1 | 21/0/0 |
| 31 | Assassination | Vigor | 1 | 22/0/0 |
| 32-33 | Subtlety | Opportunity | 2 | 22/0/2 |
| 34-38 | Combat | Lightning Reflexes | 5 | 22/5/2 |
| 39-41 | Combat | Precision | 3 | 22/8/2 |
| 42-44 | Combat | Deflection | 3 | 22/11/2 |
| 45 | Combat | Riposte | 1 | 22/12/2 |
| 46-48 | Combat | Improved Eviscerate | 3 | 22/15/2 |
| 49 | Combat | Flawless Execution | 1 | 22/16/2 |
| 50-52 | Subtlety | Master of Deception | 3 | 22/16/5 |
| 53 | Subtlety | Improved Ambush | 1 | 22/16/6 |
| 54-56 | Subtlety | Setup | 3 | 22/16/9 |
| 57 | Subtlety | Elusiveness | 1 | 22/16/10 |
| 58-60 | Subtlety | Initiative | 3 | 22/16/13 |

## Core talents (priority order)

1. **Setup** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Eviscerate** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Mutilate** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Relentless Strikes** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Flawless Execution** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Precision** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malice** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.94; opt-combat-swords-raid-leveling-st 26.55, opt-combat-swords-raid-solo-60 26.55, leveling-combat-swords 26.89. The search simulated 75,937 builds.
- The spec's other leveling builds on the pages: opt-combat-daggers-raid-leveling-st 28.17 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Daggers (split) leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/02532011101411-30503301001-03231013-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
