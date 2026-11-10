# Subtlety — Leveling (open talent search) — 0/20/31

*[Rogue](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/20/31 (Assassination / Combat / Subtlety) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Subtlety leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the subtlety-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (combat-swords-raid). 

## Point allocation

### Assassination (0)

*No points.*

### Combat (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Coup de Grace** | 3/3 | changed | Increases the damage done by your Eviscerate ability by 20%, and the damage and storage rate of your Death Mark ability by 20%. |
| **Efficient Strikes** | 2/2 | unchanged | Reduces the Energy costs of Sinister Strike and Hemorrhage by 5. |
| **Lightning Reflexes** | 3/5 | unchanged | Increases your Dodge chance by 3%. |
| **Puncturing Wounds** | 2/3 | **NEW** | Increases the critical strike chance of your Backstab by 20% and your Mutilate by 10%, and gives Backstab a 30% chance to add an additional Combo Point. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Composure** | 2/2 | **NEW** | Increases the Energy cost reduction of your Poised ability by 10. |
| **Flawless Execution** | 1/1 | **NEW** | Reduces the Energy cost of your Eviscerate ability by 15. |
| **Weapon Expertise** | 2/2 | changed | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 2/3 | changed | Increases the damage of Sinister Strike and Eviscerate by 10%. |

### Subtlety (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Setup** | 3/3 | changed | Gives you a 45% chance to add a Combo Point to your target after Dodging their attack or fully resisting one of their spells. |
| **Master of Deception** | 1/3 | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 1 level higher. |
| **Opportunity** | 5/5 | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 20%. |
| **Dirty Deeds** | 2/2 | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Improved Ambush** | 3/3 | moved | Increases the critical strike chance of your Ambush ability by 45%. |
| **Dirty Tricks** | 1/2 | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 25%. |
| **Initiative** | 3/3 | changed | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Premeditation** | 1/1 | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. |
| **Serrated Blades** | 3/3 | changed | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |
| **Ghostly Strike** | 1/1 | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. Also causes your next Ambush or Garrote cast within 7 seconds to not require Stealth. |
| **Preparation** | 1/1 | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. |
| **Hemorrhage** | 1/1 | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and increases the damage of the caster's Rupture and Garrote abilities by 15%. Lasts 15 sec. Awards 1 Combo Point. |
| **Boot Knife** | 5/5 | **NEW** | Gives your Shank ability a 100% chance to add 2 Combo Points to the target. |
| **Death Mark** | 1/1 | **NEW** | Finishing move that marks the target, storing a portion of the damage dealt by your attacks per Combo Point. Garrote and Rupture damage is stored at twice the rate. After 6 sec, the stored damage is dealt up to a maximum increased by Attack Power and Critical Strike chance. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Subtlety | Opportunity | 2 | 0/0/2 |
| 12-14 | Subtlety | Setup | 3 | 0/0/5 |
| 15-16 | Subtlety | Dirty Deeds | 2 | 0/0/7 |
| 17 | Subtlety | Master of Deception | 1 | 0/0/8 |
| 18-19 | Subtlety | Improved Ambush | 2 | 0/0/10 |
| 20-22 | Subtlety | Serrated Blades | 3 | 0/0/13 |
| 23 | Subtlety | Initiative | 1 | 0/0/14 |
| 24 | Subtlety | Premeditation | 1 | 0/0/15 |
| 25 | Subtlety | Ghostly Strike | 1 | 0/0/16 |
| 26-27 | Subtlety | Initiative | 2 | 0/0/18 |
| 28-29 | Subtlety | Opportunity | 2 | 0/0/20 |
| 30 | Subtlety | Hemorrhage | 1 | 0/0/21 |
| 31 | Subtlety | Preparation | 1 | 0/0/22 |
| 32 | Subtlety | Opportunity | 1 | 0/0/23 |
| 33 | Subtlety | Improved Ambush | 1 | 0/0/24 |
| 34 | Subtlety | Dirty Tricks | 1 | 0/0/25 |
| 35-39 | Subtlety | Boot Knife | 5 | 0/0/30 |
| 40 | Subtlety | Death Mark | 1 | 0/0/31 |
| 41-43 | Combat | Coup de Grace | 3 | 0/3/31 |
| 44-45 | Combat | Lightning Reflexes | 2 | 0/5/31 |
| 46-48 | Combat | Precision | 3 | 0/8/31 |
| 49-50 | Combat | Efficient Strikes | 2 | 0/10/31 |
| 51-52 | Combat | Puncturing Wounds | 2 | 0/12/31 |
| 53 | Combat | Lightning Reflexes | 1 | 0/13/31 |
| 54-55 | Combat | Composure | 2 | 0/15/31 |
| 56 | Combat | Flawless Execution | 1 | 0/16/31 |
| 57-58 | Combat | Weapon Expertise | 2 | 0/18/31 |
| 59-60 | Combat | Aggression | 2 | 0/20/31 |

## Core talents (priority order)

1. **Boot Knife** — +2.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Coup de Grace** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Flawless Execution** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Dirty Deeds** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Initiative** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Efficient Strikes** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Hemorrhage** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Weapon Expertise** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-09: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Master of Deception to Improved Ambush at 19 (gate: -0.5% seed 3, -0.5% seed 4, level-weighted time per kill); Master of Deception to Improved Ambush at 18 (gate: -0.7% seed 3, -0.8% seed 4, level-weighted time per kill); Improved Sprint to Composure at 54 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Puncturing Wounds to Lightning Reflexes at 53 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 22.41; subtlety-leveling 23.33. The search simulated 32,176 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Subtlety leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/rogue>
- <https://talentsforever.com/rogue/60/-32230310010122-335201131301001151-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
