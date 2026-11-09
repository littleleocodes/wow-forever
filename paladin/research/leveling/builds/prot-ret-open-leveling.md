# Prot-Ret — Leveling (open talent search) — 10/16/25

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/16/25 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Prot-Ret (a Protection/Retribution hybrid) leveling build the open leveling search found on 2026-11-09: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the ret-dps rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +2.8% faster per kill than leveling-retribution, the fastest of our leveling builds in that race.

## Point allocation

### Holy (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Sacred Duty** | 2/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Improved Hammer of Justice** | 3/3 | moved | Decreases the cooldown of your Hammer of Justice spell by 15 sec. |
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Swift Judgement** | 1/1 | **NEW** | Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. |

### Retribution (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Benediction** | 1/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 2%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
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
| 10 | Retribution | Benediction | 1 | 0/0/1 |
| 11-14 | Retribution | Deflection | 4 | 0/0/5 |
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
| 33 | Retribution | Deflection | 1 | 0/0/24 |
| 34-38 | Holy | Divine Strength | 5 | 5/0/24 |
| 39-41 | Holy | Improved Seals | 3 | 8/0/24 |
| 42-46 | Protection | Divine Intellect | 5 | 8/5/24 |
| 47-49 | Protection | Precision | 3 | 8/8/24 |
| 50-51 | Protection | Sacred Duty | 2 | 8/10/24 |
| 52 | Protection | Templar's Bulwark | 1 | 8/11/24 |
| 53 | Protection | Improved Hammer of Justice | 1 | 8/12/24 |
| 54 | Protection | Toughness | 1 | 8/13/24 |
| 55-56 | Protection | Improved Hammer of Justice | 2 | 8/15/24 |
| 57 | Protection | Swift Judgement | 1 | 8/16/24 |
| 58-59 | Holy | Reverence | 2 | 10/16/24 |
| 60 | Retribution | Improved Judgement | 1 | 10/16/25 |

## Core talents (priority order)

1. **Sanctified Judgement** — +3.2 s per kill at level 60 without it (removal, 3,000 fights).
2. **Conviction** — +2.6 s per kill at level 60 without it (removal, 3,000 fights).
3. **Swift Judgement** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Vengeance** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Two-Handed Weapon Specialization** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Seals** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Precision** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Seal of Command** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-09: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing moved: Improved Seals to Improved Judgement at 60 (no loss: -0.0% seed 3, +0.0% seed 4, level-weighted time per kill). 2026-11-09: tier-gate swap by hand (the filler pass reads only points the build can drop): Redoubt to Sacred Duty at 50-51. Redoubt adds block, which needs a shield, and this build fights with a two-hander; Protection's deeper talents need the two points in rows 1-2, where Redoubt, Guardian's Favor and Sacred Duty are left. The fight lab measures the swap at exactly 0.00% on seeds 3 and 4 (26.490 and 26.713 s level-weighted); Sacred Duty takes 60 s off Divine Shield, Divine Protection and Templar's Bulwark. Then 2 of the 3 Toughness points (55-56, also a gate for Swift Judgement) to Improved Hammer of Justice 3/3: faster on both seeds (-0.17% seed 3, -0.15% seed 4, level-weighted; 30.27 to 30.17 s at 60 on seed 3), the stun combo ready 10 s sooner.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 26.46; leveling-retribution 27.19, opt-ret-dps-leveling-st 27.19. The search simulated 47,144 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Prot-Ret leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/05024-5230011031-511333010013003-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
