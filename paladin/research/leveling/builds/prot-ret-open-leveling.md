# Prot-Ret — Leveling (open talent search) — 12/16/23

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 12/16/23 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Prot-Ret (a Protection/Retribution hybrid) leveling build the open leveling search found on 2026-11-17: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the ret-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +2.6% faster per kill than leveling-retribution, the fastest of our leveling builds in that race.

## Point allocation

### Holy (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Improved Hammer of Justice** | 1/3 | moved | Decreases the cooldown of your Hammer of Justice spell by 5 sec. |
| **Toughness** | 3/5 | moved | Increases your armor value from items by 6%. |
| **Swift Judgement** | 1/1 | **NEW** | Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |

### Retribution (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
| **Benediction** | 2/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 4%. |
| **Improved Judgement** | 1/2 | changed | Decreases the cooldown of your Judgement ability by 1 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Retribution | Benediction | 2 | 0/0/2 |
| 12-14 | Retribution | Deflection | 3 | 0/0/5 |
| 15-17 | Retribution | Sanctified Judgement | 3 | 0/0/8 |
| 18-19 | Retribution | Conviction | 2 | 0/0/10 |
| 20 | Retribution | Seal of Command | 1 | 0/0/11 |
| 21 | Retribution | Conviction | 1 | 0/0/12 |
| 22 | Retribution | Improved Judgement | 1 | 0/0/13 |
| 23-24 | Retribution | Vindication | 2 | 0/0/15 |
| 25 | Retribution | Sacred Arbiter | 1 | 0/0/16 |
| 26-28 | Retribution | Two-Handed Weapon Specialization | 3 | 0/0/19 |
| 29 | Retribution | Vindication | 1 | 0/0/20 |
| 30-32 | Retribution | Vengeance | 3 | 0/0/23 |
| 33-37 | Holy | Divine Strength | 5 | 5/0/23 |
| 38-40 | Holy | Improved Seals | 3 | 8/0/23 |
| 41-45 | Protection | Divine Intellect | 5 | 8/5/23 |
| 46-48 | Protection | Precision | 3 | 8/8/23 |
| 49-50 | Protection | Sacred Duty | 2 | 8/10/23 |
| 51 | Protection | Templar's Bulwark | 1 | 8/11/23 |
| 52 | Protection | Improved Hammer of Justice | 1 | 8/12/23 |
| 53-55 | Protection | Toughness | 3 | 8/15/23 |
| 56 | Protection | Swift Judgement | 1 | 8/16/23 |
| 57-58 | Holy | Reverence | 2 | 10/16/23 |
| 59-60 | Holy | Improved Seals | 2 | 12/16/23 |

## Core talents (priority order)

1. **Sanctified Judgement** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Conviction** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Vengeance** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Swift Judgement** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
5. **Two-Handed Weapon Specialization** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Seals** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Seal of Command** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Vindication** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-15: by hand, Redoubt to Sacred Duty at 49, 50: Redoubt only adds block, which needs a shield, and this build fights with a two-hander; Sacred Duty holds the row to Templar's Bulwark open as well and takes 30 seconds a point off Divine Shield, Divine Protection and Templar's Bulwark (the fight lab measures the swap at 0.00%). Earlier: 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Deflection to Improved Seals at 59 (tie-break: -0.3% seed 3, -0.2% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 25.89; leveling-retribution 26.57, opt-ret-dps-leveling-st 26.77. The search simulated 47,144 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Prot-Ret leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/05024-5230011031-421333010013003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
