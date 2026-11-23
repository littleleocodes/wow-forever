# Smite — Leveling (open talent search) — 21/21/9

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/21/9 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Smite (a Discipline/Holy hybrid) leveling build the open leveling search found on 2026-11-22: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). 

## Point allocation

### Discipline (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Twin Disciplines** | 2/5 | **NEW** | Increases the damage and healing of your instant cast spells by 2%. |
| **Holy Precision** | 1/3 | **NEW** | Improves your chance to hit with Holy spells by 6%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |

### Holy (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives your spells a 70% chance to not lose casting time when you take damage. |
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Spell Warding** | 2/5 | unchanged | Reduces all spell damage taken by 4%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Inspiration** | 3/3 | changed | Your non-periodic critical heals increase your target's Armor by 25% for 15 sec. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |
| **Spiritual Guidance** | 1/5 | changed | Increases your spell healing by up to 5% of your total Spirit and your spell damage by up to 1% of your total Spirit. |

### Shadow (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 1/5 | changed | Improves your chance to hit with Shadow spells by 1%. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 1/5 | changed | Reduces the cooldown of your Mind Blast spell by 0.5 sec. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Discipline | Wand Specialization | 2 | 2/0/0 |
| 12-13 | Discipline | Twin Disciplines | 2 | 4/0/0 |
| 14-18 | Discipline | Power in Light | 5 | 9/0/0 |
| 19 | Discipline | Holy Precision | 1 | 10/0/0 |
| 20-21 | Discipline | Mental Agility | 2 | 12/0/0 |
| 22-24 | Discipline | Meditation | 3 | 15/0/0 |
| 25-27 | Shadow | Spirit Tap | 3 | 15/0/3 |
| 28 | Discipline | Mental Agility | 1 | 16/0/3 |
| 29 | Shadow | Spirit Tap | 1 | 16/0/4 |
| 30 | Discipline | Inner Focus | 1 | 17/0/4 |
| 31 | Shadow | Spirit Tap | 1 | 17/0/5 |
| 32 | Shadow | Improved Mind Blast | 1 | 17/0/6 |
| 33 | Discipline | Improved Power Word: Shield | 1 | 18/0/6 |
| 34 | Holy | Twilight Focus | 1 | 18/1/6 |
| 35-39 | Holy | Holy Specialization | 5 | 18/6/6 |
| 40-43 | Holy | Divine Fury | 4 | 18/10/6 |
| 44 | Holy | Twilight Focus | 1 | 18/11/6 |
| 45-46 | Discipline | Improved Power Word: Shield | 2 | 20/11/6 |
| 47 | Shadow | Shadow Focus | 1 | 20/11/7 |
| 48 | Discipline | Soul Warding | 1 | 21/11/7 |
| 49 | Holy | Divine Fury | 1 | 21/12/7 |
| 50-52 | Holy | Inspiration | 3 | 21/15/7 |
| 53-54 | Holy | Spell Warding | 2 | 21/17/7 |
| 55 | Holy | Twilight Focus | 1 | 21/18/7 |
| 56-57 | Holy | Searing Light | 2 | 21/20/7 |
| 58 | Holy | Spiritual Guidance | 1 | 21/21/7 |
| 59-60 | Shadow | Improved Shadow Word: Pain | 2 | 21/21/9 |

## Core talents (priority order)

1. **Spirit Tap** — +3.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Meditation** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Mental Agility** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Divine Fury** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Power in Light** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
6. **Searing Light** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
7. **Holy Precision** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Shadow Word: Pain** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-21: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Healing to Spell Warding at 54 (gate that did nothing, tie-break by utility (survival): +0.0% seed 3, +0.0% seed 4, level-weighted time per kill); Improved Healing to Spell Warding at 53 (gate that did nothing, tie-break by utility (survival): +0.0% seed 3, +0.0% seed 4, level-weighted time per kill). Earlier: 2026-11-21: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Healing to Twilight Focus at 55 (gate that did nothing, no loss: -0.0% seed 3, +0.0% seed 4, level-weighted time per kill). Earlier: 2026-11-20: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Inner Fire to Shadow Focus at 47 (no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill); Improved Renew to Twilight Focus at 34 (gate: -0.2% seed 3, -0.2% seed 4, level-weighted time per kill); Holy Nova to Twilight Focus at 44 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 42.37; holy-leveling 50.01. The search simulated 40,040 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Smite leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/52201003133001-305250030020001-10512-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
