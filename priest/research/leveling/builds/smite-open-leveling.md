# Smite — Leveling (open talent search) — 22/22/7

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/22/7 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Smite (a Discipline/Holy hybrid) leveling build the open leveling search found on 2026-11-17: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +12.7% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Twin Disciplines** | 3/5 | **NEW** | Increases the damage and healing of your instant cast spells by 3%. |
| **Holy Precision** | 1/3 | **NEW** | Improves your chance to hit with Holy spells by 6%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |

### Holy (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives your spells a 70% chance to not lose casting time when you take damage. |
| **Improved Renew** | 1/3 | unchanged | Increases the amount healed by your Renew spell by 5%. |
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |
| **Improved Healing** | 3/3 | changed | Reduces the Mana cost of your Lesser Heal, Heal, Greater Heal, Penance, and Prayer of Mending spells by 15%. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |
| **Spiritual Guidance** | 2/5 | changed | Increases your spell healing by up to 10% of your total Spirit and your spell damage by up to 3% of your total Spirit. |

### Shadow (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 1/5 | changed | Reduces the cooldown of your Mind Blast spell by 0.5 sec. |
| **Improved Shadow Word: Pain** | 1/2 | moved | Increases the duration of your Shadow Word: Pain spell by 3 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Discipline | Wand Specialization | 2 | 2/0/0 |
| 12-13 | Discipline | Twin Disciplines | 2 | 4/0/0 |
| 14-18 | Discipline | Power in Light | 5 | 9/0/0 |
| 19 | Discipline | Holy Precision | 1 | 10/0/0 |
| 20-21 | Discipline | Mental Agility | 2 | 12/0/0 |
| 22-24 | Discipline | Meditation | 3 | 15/0/0 |
| 25 | Discipline | Mental Agility | 1 | 16/0/0 |
| 26 | Discipline | Inner Focus | 1 | 17/0/0 |
| 27-29 | Discipline | Improved Power Word: Shield | 3 | 20/0/0 |
| 30 | Discipline | Twin Disciplines | 1 | 21/0/0 |
| 31 | Discipline | Soul Warding | 1 | 22/0/0 |
| 32-36 | Shadow | Spirit Tap | 5 | 22/0/5 |
| 37-39 | Holy | Twilight Focus | 3 | 22/3/5 |
| 40 | Shadow | Improved Mind Blast | 1 | 22/3/6 |
| 41 | Holy | Improved Renew | 1 | 22/4/6 |
| 42-46 | Holy | Holy Specialization | 5 | 22/9/6 |
| 47 | Holy | Divine Fury | 1 | 22/10/6 |
| 48 | Holy | Holy Nova | 1 | 22/11/6 |
| 49-52 | Holy | Divine Fury | 4 | 22/15/6 |
| 53-55 | Holy | Improved Healing | 3 | 22/18/6 |
| 56-57 | Holy | Searing Light | 2 | 22/20/6 |
| 58 | Shadow | Improved Shadow Word: Pain | 1 | 22/20/7 |
| 59-60 | Holy | Spiritual Guidance | 2 | 22/22/7 |

## Core talents (priority order)

1. **Meditation** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Mental Agility** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Divine Fury** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Spirit Tap** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Power in Light** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Searing Light** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
7. **Holy Precision** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Soul Warding** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-17: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Shadow Word: Pain to Shadow Focus at 59 (no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill); Shadow Focus to Spiritual Guidance at 59 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Improved Inner Fire to Twin Disciplines at 30 (no loss: +0.1% seed 3, +0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 49.96; holy-leveling 56.32. The search simulated 40,040 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Smite leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/52201003133101-315051000320001-00512-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
