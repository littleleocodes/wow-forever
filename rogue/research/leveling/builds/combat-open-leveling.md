# Combat — Leveling (open talent search) — 12/31/8

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/31/8 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the combat-swords-raid rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +0.6% faster per kill than opt-combat-swords-raid-leveling-aoe, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Gouge** | 1/3 | changed | Increases the duration of your Gouge ability by 0.5 sec. |
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5/5 | changed | Increases your critical strike chance with all attacks and Poisons by 5%. |
| **Murder** | 2/2 | changed | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Relentless Strikes** | 1/1 | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. |
| **Lethality** | 1/5 | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%. |

### Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Eviscerate** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2/2 | unchanged | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Deflection** | 3/3 | changed | Increases your Parry chance by 6%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Riposte** | 1/1 | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. |
| **Dual Wield Specialization** | 5/5 | changed | Increases the damage done by your off-hand weapon by 25%. |
| **Blade Flurry** | 1/1 | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. |
| **Hack and Slash** | 3/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 3% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 3%.   Mace: Your attacks ignore 9% of  your target's armor. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |
| **Adrenaline Rush** | 1/1 | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. |

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
| 10-11 | Combat | Improved Sinister Strike | 2 | 0/2/0 |
| 12-14 | Combat | Improved Eviscerate | 3 | 0/5/0 |
| 15 | Combat | Deflection | 1 | 0/6/0 |
| 16-17 | Combat | Precision | 2 | 0/8/0 |
| 18-19 | Combat | Deflection | 2 | 0/10/0 |
| 20 | Combat | Riposte | 1 | 0/11/0 |
| 21 | Combat | Precision | 1 | 0/12/0 |
| 22-24 | Combat | Lightning Reflexes | 3 | 0/15/0 |
| 25 | Combat | Flawless Execution | 1 | 0/16/0 |
| 26-30 | Combat | Dual Wield Specialization | 5 | 0/21/0 |
| 31-33 | Combat | Hack and Slash | 3 | 0/24/0 |
| 34 | Combat | Blade Flurry | 1 | 0/25/0 |
| 35-36 | Combat | Weapon Expertise | 2 | 0/27/0 |
| 37-39 | Combat | Aggression | 3 | 0/30/0 |
| 40 | Combat | Adrenaline Rush | 1 | 0/31/0 |
| 41-42 | Assassination | Remorseless Attacks | 2 | 2/31/0 |
| 43-44 | Subtlety | Opportunity | 2 | 2/31/2 |
| 45-49 | Assassination | Malice | 5 | 7/31/2 |
| 50-51 | Assassination | Murder | 2 | 9/31/2 |
| 52 | Assassination | Improved Gouge | 1 | 10/31/2 |
| 53 | Assassination | Relentless Strikes | 1 | 11/31/2 |
| 54-55 | Subtlety | Master of Deception | 2 | 11/31/4 |
| 56 | Subtlety | Camouflage | 1 | 11/31/5 |
| 57-59 | Subtlety | Setup | 3 | 11/31/8 |
| 60 | Assassination | Lethality | 1 | 12/31/8 |

## Core talents (priority order)

1. **Setup** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Flawless Execution** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Sinister Strike** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Improved Eviscerate** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Malice** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Precision** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
7. **Weapon Expertise** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Relentless Strikes** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 24.63; opt-combat-swords-raid-leveling-aoe 24.78, combat-leveling 25.35. The search simulated 37,275 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Combat leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/125020101-32303301001513231-1223-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
