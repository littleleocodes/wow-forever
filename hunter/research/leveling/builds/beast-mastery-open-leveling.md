# Beast Mastery — Leveling (open talent search) — 31/16/4

*[Hunter](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/16/4 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Beast Mastery leveling build the open leveling search found on 2026-11-06: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the bm-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (bm-leveling). -0.7% faster per kill than beast-mastery-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Beast Mastery (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 3/5 | changed | Increases the Health and Armor of your pets by 9%. |
| **Focused Fire** | 2/2 | **NEW** | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Bestial Swiftness** | 1/1 | changed | Increases the movement speed of your pets by 30%. |
| **Unleashed Fury** | 5/5 | changed | Increases the damage done by your pets and hawks by 15%. |
| **Ferocity** | 5/5 | changed | Increases the critical strike chance of your pets and hawks by 10%. |
| **Spirit Bond** | 1/2 | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. |
| **Intimidation** | 1/1 | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. |
| **Bestial Discipline** | 2/2 | changed | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |
| **Frenzy** | 5/5 | unchanged | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |
| **Bestial Wrath** | 1/1 | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. |

### Marksmanship (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Improved Stings** | 3/3 | **NEW** | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 2/5 | **NEW** | Increases your Attack Power by 40% of your Intellect. |
| **Trueshot Aura** | 1/1 | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. |

### Survival (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Tracking** | 4/5 | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 4%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Beast Mastery | Deadly Aspects | 5 | 5/0/0 |
| 15-16 | Beast Mastery | Focused Fire | 2 | 7/0/0 |
| 17-19 | Beast Mastery | Endurance Training | 3 | 10/0/0 |
| 20-24 | Beast Mastery | Unleashed Fury | 5 | 15/0/0 |
| 25-29 | Beast Mastery | Ferocity | 5 | 20/0/0 |
| 30-31 | Beast Mastery | Bestial Discipline | 2 | 22/0/0 |
| 32 | Beast Mastery | Spirit Bond | 1 | 23/0/0 |
| 33 | Beast Mastery | Bestial Swiftness | 1 | 24/0/0 |
| 34 | Beast Mastery | Intimidation | 1 | 25/0/0 |
| 35-39 | Beast Mastery | Frenzy | 5 | 30/0/0 |
| 40 | Beast Mastery | Bestial Wrath | 1 | 31/0/0 |
| 41-45 | Marksmanship | Lethal Attacks | 5 | 31/5/0 |
| 46-50 | Marksmanship | Efficiency | 5 | 31/10/0 |
| 51-53 | Marksmanship | Improved Stings | 3 | 31/13/0 |
| 54-55 | Marksmanship | Careful Aim | 2 | 31/15/0 |
| 56 | Marksmanship | Trueshot Aura | 1 | 31/16/0 |
| 57-60 | Survival | Improved Tracking | 4 | 31/16/4 |

## Core talents (priority order)

1. **Unleashed Fury** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Bestial Discipline** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Efficiency** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Ferocity** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Lethal Attacks** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Stings** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
7. **Frenzy** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).
8. **Trueshot Aura** — +0.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +5.1% faster than the hand draft bm-solo-farm, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 23.12; beast-mastery-leveling 22.95, beast-mastery-open-leveling 23.06, bm-solo-farm 24.30. The search simulated 22,683 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Beast Mastery leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/hunter>
- <https://talentsforever.com/hunter/60/5320001505011251-0053520001-4-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
