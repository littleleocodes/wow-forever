# Protection — Leveling (open talent search) — 0/20/31

*[Warrior](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/20/31 (Arms / Fury / Protection) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Protection leveling build the open leveling search found on 2026-10-11: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the prot-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (arms-2h-raid). +0.6% faster per kill than protection-open-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Arms (0)

*No points.*

### Fury (20)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Booming Voice** | 3/5 | changed | Increases the area of effect of your Shouts by 30% and reduces their Rage cost by 15%. |
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Unbridled Wrath** | 5/5 | changed | Gives you a 60% chance to generate 1 additional Rage when you deal melee damage with a weapon. |
| **Furious Precision** | 2/3 | changed | Increases your chance to hit with off-hand attacks by 7%. |
| **Enrage** | 5/5 | changed | Gives you a 30% chance to deal 10% increased Physical damage for 12 sec after being the victim of any damaging attack. |

### Protection (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shield Specialization** | 5/5 | changed | Increases your chance to Block attacks with your shield by 5% and grants you a 100% chance to generate 5 Rage when you Block. |
| **Anticipation** | 3/5 | changed | Increases your Defense Skill by 12. |
| **Improved Revenge** | 3/3 | changed | Increases damage dealt by your Revenge ability by 60%. |
| **Improved Thunder Clap** | 1/3 | changed | Reduces the Rage cost of your Thunder Clap ability by 2. |
| **Master of Defense** | 2/2 | **NEW** | Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. |
| **Improved Disarm** | 2/3 | changed | Reduces the cooldown of your Disarm ability by 13 secs. |
| **Improved Sunder Armor** | 2/3 | changed | Reduces the Rage cost of your Sunder Armor ability by 2. |
| **Vanguard** | 1/1 | **NEW** | Your Charge ability is now usable while in Defensive Stance. |
| **Improved Shield Bash** | 1/2 | unchanged | Gives your Shield Bash ability a 50% chance to Silence the target for 3 sec. |
| **Improved Shield Wall** | 1/2 | changed | Reduces the cooldown of your Shield Wall ability by 5.5 min. |
| **Concussion Blow** | 1/1 | changed | Stuns the target for 5 sec. |
| **Focused Rage** | 3/3 | **NEW** | Reduces the Rage cost of your offensive abilities by 3. |
| **Bastion** | 5/5 | **NEW** | Increases all damage you deal by 10% while a shield is equipped. |
| **Shield Slam** | 1/1 | changed | Slam the target with your shield, causing 421 to 439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Protection | Shield Specialization | 5 | 0/0/5 |
| 15-17 | Protection | Anticipation | 3 | 0/0/8 |
| 18-20 | Protection | Improved Revenge | 3 | 0/0/11 |
| 21 | Protection | Improved Thunder Clap | 1 | 0/0/12 |
| 22-23 | Protection | Master of Defense | 2 | 0/0/14 |
| 24 | Protection | Improved Disarm | 1 | 0/0/15 |
| 25-26 | Protection | Improved Sunder Armor | 2 | 0/0/17 |
| 27 | Protection | Vanguard | 1 | 0/0/18 |
| 28 | Protection | Improved Shield Bash | 1 | 0/0/19 |
| 29 | Protection | Improved Disarm | 1 | 0/0/20 |
| 30-32 | Protection | Focused Rage | 3 | 0/0/23 |
| 33 | Protection | Concussion Blow | 1 | 0/0/24 |
| 34 | Protection | Improved Shield Wall | 1 | 0/0/25 |
| 35-39 | Protection | Bastion | 5 | 0/0/30 |
| 40 | Protection | Shield Slam | 1 | 0/0/31 |
| 41-45 | Fury | Cruelty | 5 | 0/5/31 |
| 46-50 | Fury | Unbridled Wrath | 5 | 0/10/31 |
| 51-53 | Fury | Booming Voice | 3 | 0/13/31 |
| 54-55 | Fury | Furious Precision | 2 | 0/15/31 |
| 56-60 | Fury | Enrage | 5 | 0/20/31 |

## Core talents (priority order)

1. **Shield Slam** — +5.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Revenge** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Shield Specialization** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Bastion** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Focused Rage** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Cruelty** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Enrage** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Master of Defense** — +0.3 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 26.19; protection-open-leveling 26.34, protection-leveling 30.64. The search simulated 29,703 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Protection leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warrior>
- <https://talentsforever.com/warrior/60/-3505200005-050331022021111351-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
