# Smite — Leveling (open talent search) — 21/23/7

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/23/7 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Smite (a Discipline/Holy hybrid) leveling build the open leveling search found on 2026-10-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +12.0% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Twin Disciplines** | 4/5 | **NEW** | Increases the damage and healing of your instant cast spells by 4%. |
| **Holy Precision** | 1/3 | **NEW** | Improves your chance to hit with Holy spells by 6%. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Improved Inner Fire** | 1/3 | changed | Increases the Armor bonus of your Inner Fire spell by 15% and increases its total charges by 4. |
| **Mental Strength** | 1/5 | changed | Increases your total Intellect by 3%. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |
| **Penance** | 1/1 | **NEW** | Launches a volley of holy light at the target, causing 44 Holy damage to an enemy, or 133 healing to an ally, instantly and every 1 sec for 2 sec. |

### Holy (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 1/3 | **NEW** | Gives you a 23% chance to avoid interruption caused by damage while casting any spell. |
| **Improved Renew** | 3/3 | unchanged | Increases the amount healed by your Renew spell by 15%. |
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Inspiration** | 1/3 | changed | Your non-periodic critical heals increase your target's Armor by 8% for 15 sec. |
| **Improved Healing** | 3/3 | changed | Reduces the Mana cost of your Lesser Heal, Heal, Greater Heal, Penance, and Prayer of Mending spells by 15%. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |
| **Spiritual Guidance** | 3/5 | changed | Increases your spell healing by up to 15% of your total Spirit and your spell damage by up to 5% of your total Spirit. |

### Shadow (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Shadow Reach** | 2/2 | changed | Increases the range of your offensive Shadow spells by 20%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Shadow | Spirit Tap | 5 | 0/0/5 |
| 15-16 | Shadow | Shadow Reach | 2 | 0/0/7 |
| 17-20 | Discipline | Twin Disciplines | 4 | 4/0/7 |
| 21 | Discipline | Wand Specialization | 1 | 5/0/7 |
| 22-24 | Discipline | Improved Power Word: Shield | 3 | 8/0/7 |
| 25 | Discipline | Wand Specialization | 1 | 9/0/7 |
| 26 | Discipline | Holy Precision | 1 | 10/0/7 |
| 27 | Discipline | Meditation | 1 | 11/0/7 |
| 28 | Discipline | Inner Focus | 1 | 12/0/7 |
| 29-30 | Discipline | Meditation | 2 | 14/0/7 |
| 31-33 | Discipline | Mental Agility | 3 | 17/0/7 |
| 34 | Discipline | Mental Strength | 1 | 18/0/7 |
| 35 | Discipline | Improved Inner Fire | 1 | 19/0/7 |
| 36 | Discipline | Soul Warding | 1 | 20/0/7 |
| 37 | Discipline | Penance | 1 | 21/0/7 |
| 38 | Holy | Twilight Focus | 1 | 21/1/7 |
| 39-41 | Holy | Improved Renew | 3 | 21/4/7 |
| 42-46 | Holy | Holy Specialization | 5 | 21/9/7 |
| 47-51 | Holy | Divine Fury | 5 | 21/14/7 |
| 52 | Holy | Inspiration | 1 | 21/15/7 |
| 53-55 | Holy | Improved Healing | 3 | 21/18/7 |
| 56-57 | Holy | Searing Light | 2 | 21/20/7 |
| 58-60 | Holy | Spiritual Guidance | 3 | 21/23/7 |

## Core talents (priority order)

1. **Penance** — +6.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Spirit Tap** — +2.3 s per kill at level 60 without it (removal, 3,000 fights).
3. **Meditation** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Mental Agility** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Wand Specialization** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Searing Light** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Healing** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Soul Warding** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 40.28; holy-leveling 45.10. The search simulated 39,186 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Smite leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/024013031311101-135050010320003-005002-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
