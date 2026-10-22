# Smite — Leveling (open talent search) — 25/13/13

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 25/13/13 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Smite (a Discipline/Holy hybrid) leveling build the open leveling search found on 2026-10-21: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +18.0% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (25)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 4/5 | **NEW** | Your Smite and Penance spells deal 8% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Improved Inner Fire** | 3/3 | changed | Increases the Armor bonus of your Inner Fire spell by 45% and increases its total charges by 12. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |

### Holy (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 2/3 | **NEW** | Gives you a 47% chance to avoid interruption caused by damage while casting any spell. |
| **Improved Renew** | 3/3 | unchanged | Increases the amount healed by your Renew spell by 15%. |
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Divine Fury** | 3/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.3 sec. |

### Shadow (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 4/5 | changed | Improves your chance to hit with Shadow spells by 4%. |
| **Blackout** | 2/5 | moved | Gives your Shadow damage spells a 4% chance to stun the target for 3 sec. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Discipline | Wand Specialization | 2 | 2/0/0 |
| 12-16 | Discipline | Twin Disciplines | 5 | 7/0/0 |
| 17-19 | Discipline | Power in Light | 3 | 10/0/0 |
| 20-21 | Discipline | Mental Agility | 2 | 12/0/0 |
| 22-24 | Discipline | Meditation | 3 | 15/0/0 |
| 25 | Discipline | Mental Agility | 1 | 16/0/0 |
| 26 | Discipline | Inner Focus | 1 | 17/0/0 |
| 27-29 | Discipline | Improved Power Word: Shield | 3 | 20/0/0 |
| 30-32 | Discipline | Improved Inner Fire | 3 | 23/0/0 |
| 33 | Discipline | Power in Light | 1 | 24/0/0 |
| 34 | Discipline | Soul Warding | 1 | 25/0/0 |
| 35-39 | Shadow | Spirit Tap | 5 | 25/0/5 |
| 40-43 | Shadow | Shadow Focus | 4 | 25/0/9 |
| 44-45 | Holy | Twilight Focus | 2 | 25/2/9 |
| 46-47 | Shadow | Blackout | 2 | 25/2/11 |
| 48-50 | Holy | Improved Renew | 3 | 25/5/11 |
| 51-55 | Holy | Holy Specialization | 5 | 25/10/11 |
| 56-58 | Holy | Divine Fury | 3 | 25/13/11 |
| 59-60 | Shadow | Improved Shadow Word: Pain | 2 | 25/13/13 |

## Core talents (priority order)

1. **Wand Specialization** — +4.4 s per kill at level 60 without it (removal, 3,000 fights).
2. **Spirit Tap** — +3.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Shadow Word: Pain** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Meditation** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Mental Agility** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Twin Disciplines** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Shadow Focus** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Inner Fire** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 35.27; holy-leveling 41.63. The search simulated 35,735 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Smite leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/42500003133301-23503-42502-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
