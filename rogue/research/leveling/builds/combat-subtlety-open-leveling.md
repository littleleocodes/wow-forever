# Combat-Subtlety — Leveling (open talent search) — 5/25/21

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/25/21 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Combat-Subtlety (a Combat/Subtlety hybrid) leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the subtlety-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). +7.3% faster per kill than subtlety-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Assassination (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Remorseless Attacks** | 2/2 | changed | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 3/5 | changed | Increases your critical strike chance with all attacks and Poisons by 3%. |

### Combat (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 5/5 | unchanged | Increases your Dodge chance by 5%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Composure** | 2/2 | **NEW** | Increases the Energy cost reduction of your Poised ability by 10. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 15%. |
| **Dual Wield Specialization** | 2/2 | changed | Increases the damage done by your off-hand weapon by 50%. |
| **Hack and Slash** | 2/5 | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 2% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 2%.   Mace: Your attacks ignore 6% of  your target's armor. |

### Subtlety (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Opportunity** | 5/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 20%. |
| **Dirty Deeds** | 1/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10, and your Garrote ability no longer requires you to be behind your target. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec. Awards 1 Combo Point. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12 | Subtlety | Setup | 1 | 0/0/3 |
| 13-14 | Subtlety | Opportunity | 2 | 0/0/5 |
| 15 | Subtlety | Dirty Deeds | 1 | 0/0/6 |
| 16 | Subtlety | Opportunity | 1 | 0/0/7 |
| 17-19 | Subtlety | Improved Ambush | 3 | 0/0/10 |
| 20-22 | Subtlety | Serrated Blades | 3 | 0/0/13 |
| 23 | Subtlety | Initiative | 1 | 0/0/14 |
| 24 | Subtlety | Premeditation | 1 | 0/0/15 |
| 25 | Subtlety | Ghostly Strike | 1 | 0/0/16 |
| 26-28 | Combat | Coup de Grace | 3 | 0/3/16 |
| 29-30 | Assassination | Remorseless Attacks | 2 | 2/3/16 |
| 31-33 | Assassination | Malice | 3 | 5/3/16 |
| 34-35 | Combat | Efficient Strikes | 2 | 5/5/16 |
| 36-37 | Combat | Lightning Reflexes | 2 | 5/7/16 |
| 38-40 | Combat | Precision | 3 | 5/10/16 |
| 41-43 | Combat | Lightning Reflexes | 3 | 5/13/16 |
| 44-45 | Combat | Composure | 2 | 5/15/16 |
| 46 | Combat | Flawless Execution | 1 | 5/16/16 |
| 47-48 | Combat | Weapon Expertise | 2 | 5/18/16 |
| 49-51 | Combat | Aggression | 3 | 5/21/16 |
| 52-53 | Subtlety | Initiative | 2 | 5/21/18 |
| 54-55 | Combat | Dual Wield Specialization | 2 | 5/23/18 |
| 56-57 | Combat | Hack and Slash | 2 | 5/25/18 |
| 58-59 | Subtlety | Setup | 2 | 5/25/20 |
| 60 | Subtlety | Hemorrhage | 1 | 5/25/21 |

## Core talents (priority order)

1. **Remorseless Attacks** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Ambush** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Flawless Execution** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Coup de Grace** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Aggression** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Initiative** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Opportunity** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Hemorrhage** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-09: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Elusiveness to Setup at 59 (gate: -0.2% seed 3, -0.1% seed 4, level-weighted time per kill); Elusiveness to Setup at 58 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 20.89; subtlety-open-leveling 22.41, subtlety-leveling 23.33. The search simulated 54,137 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Combat-Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/023-32500300020123202-1051030313210001-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
