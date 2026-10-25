# Discipline — Leveling (open talent search) — 30/0/21

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Discipline leveling build the open leveling search found on 2026-10-23: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the discipline-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +17.0% faster per kill than discipline-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Holy Precision** | 2/3 | **NEW** | Improves your chance to hit with Holy spells by 12%. |
| **Martyrdom** | 2/2 | changed | Gives you a 100% chance to gain Focused Casting for 6 sec after being the victim of a melee or ranged critical strike. The Focused Casting effect prevents you from losing casting time when taking damage and increases your resistance to Interrupt effects by 20%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Improved Power Word: Shield** | 1/3 | changed | Increases the damage absorbed by your Power Word: Shield by 7%. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Improved Inner Fire** | 3/3 | changed | Increases the Armor bonus of your Inner Fire spell by 45% and increases its total charges by 12. |
| **Improved Mana Burn** | 2/2 | changed | Reduces the casting time of your Mana Burn spell by 1.0 sec. |
| **Penance** | 1/1 | **NEW** | Launches a volley of holy light at the target, causing 44 Holy damage to an enemy, or 133 healing to an ally, instantly and every 1 sec for 2 sec. |

### Holy (0)

*No points.*

### Shadow (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 4/5 | changed | Improves your chance to hit with Shadow spells by 4%. |
| **Blackout** | 2/5 | moved | Gives your Shadow damage spells a 4% chance to stun the target for 3 sec. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 2/5 | changed | Reduces the cooldown of your Mind Blast spell by 1 sec. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Dark Inspiration** | 2/5 | moved | Your Mind Blast and fully channeled Mind Flay causes Dark Inspiration, increasing yours and your party's Spirit by 6% for 10 sec. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Devouring Contagion** | 1/2 | **NEW** | Reduces the mana cost of your Devouring Plague by 25%.  Targets that die while Devouring Plague is active spreads it, jumping to 2 nearby enemies within 5 yds for the remaining duration. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Discipline | Wand Specialization | 2 | 2/0/0 |
| 12-16 | Discipline | Twin Disciplines | 5 | 7/0/0 |
| 17 | Discipline | Power in Light | 1 | 8/0/0 |
| 18 | Discipline | Holy Precision | 1 | 9/0/0 |
| 19 | Discipline | Power in Light | 1 | 10/0/0 |
| 20-21 | Discipline | Mental Agility | 2 | 12/0/0 |
| 22-24 | Discipline | Meditation | 3 | 15/0/0 |
| 25-27 | Shadow | Spirit Tap | 3 | 15/0/3 |
| 28 | Discipline | Mental Agility | 1 | 16/0/3 |
| 29 | Shadow | Spirit Tap | 1 | 16/0/4 |
| 30 | Discipline | Inner Focus | 1 | 17/0/4 |
| 31 | Shadow | Spirit Tap | 1 | 17/0/5 |
| 32-35 | Shadow | Shadow Focus | 4 | 17/0/9 |
| 36-37 | Shadow | Blackout | 2 | 17/0/11 |
| 38-39 | Shadow | Improved Mind Blast | 2 | 17/0/13 |
| 40-41 | Shadow | Improved Shadow Word: Pain | 2 | 17/0/15 |
| 42-44 | Shadow | Shadow Weaving | 3 | 17/0/18 |
| 45-46 | Shadow | Dark Inspiration | 2 | 17/0/20 |
| 47 | Discipline | Improved Power Word: Shield | 1 | 18/0/20 |
| 48-49 | Discipline | Improved Inner Fire | 2 | 20/0/20 |
| 50 | Shadow | Devouring Contagion | 1 | 20/0/21 |
| 51 | Discipline | Penance | 1 | 21/0/21 |
| 52 | Discipline | Improved Inner Fire | 1 | 22/0/21 |
| 53-55 | Discipline | Power in Light | 3 | 25/0/21 |
| 56 | Discipline | Holy Precision | 1 | 26/0/21 |
| 57-58 | Discipline | Martyrdom | 2 | 28/0/21 |
| 59-60 | Discipline | Improved Mana Burn | 2 | 30/0/21 |

## Core talents (priority order)

1. **Spirit Tap** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Meditation** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Devouring Contagion** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Focus** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Mental Agility** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Twin Disciplines** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
7. **Wand Specialization** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Shadow Word: Pain** — +0.4 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 39.52; discipline-leveling 46.22. The search simulated 23,417 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Discipline leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/525020231133201--42522000020301-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
