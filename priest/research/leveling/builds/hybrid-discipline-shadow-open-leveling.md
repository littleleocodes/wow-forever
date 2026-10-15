# Discipline-Shadow — Leveling (open talent search) — 22/0/29

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/0/29 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Discipline-Shadow (a Discipline/Shadow hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the discipline-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +19.8% faster per kill than discipline-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (22)

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
| **Mental Strength** | 3/5 | changed | Increases your total Intellect by 9%. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |

### Holy (0)

*No points.*

### Shadow (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 4/5 | changed | Improves your chance to hit with Shadow spells by 4%. |
| **Blackout** | 1/5 | moved | Gives your Shadow damage spells a 2% chance to stun the target for 3 sec. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Improved Fade** | 1/2 | moved | Decreases the cooldown of your Fade ability by 3 sec. |
| **Vampiric Embrace** | 1/1 | changed | Afflicts your target with Shadow energy that causes all party members to be healed for 20% of any Shadow spell damage you deal for 30 sec. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage you deal by 2% for 15 sec, stacking up to 5 times. |
| **Silence** | 1/1 | changed | Silences the target, preventing them from casting spells for 5 sec and interrupting their spellcasts for 3 sec. |
| **Devouring Contagion** | 2/2 | **NEW** | Reduces the mana cost of your Devouring Plague by 50%.  Targets that die while Devouring Plague is active spreads it, jumping to a nearby enemy within 10 yds for the remaining duration. |
| **Darkness** | 4/5 | changed | Increases your Shadow damage done by 8%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-13 | Discipline | Twin Disciplines | 4 | 4/0/0 |
| 14 | Discipline | Wand Specialization | 1 | 5/0/0 |
| 15-17 | Discipline | Improved Power Word: Shield | 3 | 8/0/0 |
| 18 | Discipline | Wand Specialization | 1 | 9/0/0 |
| 19 | Discipline | Holy Precision | 1 | 10/0/0 |
| 20 | Discipline | Inner Focus | 1 | 11/0/0 |
| 21-23 | Discipline | Mental Agility | 3 | 14/0/0 |
| 24 | Discipline | Meditation | 1 | 15/0/0 |
| 25-27 | Discipline | Mental Strength | 3 | 18/0/0 |
| 28 | Discipline | Improved Inner Fire | 1 | 19/0/0 |
| 29-30 | Discipline | Meditation | 2 | 21/0/0 |
| 31 | Discipline | Soul Warding | 1 | 22/0/0 |
| 32 | Shadow | Blackout | 1 | 22/0/1 |
| 33-36 | Shadow | Shadow Focus | 4 | 22/0/5 |
| 37 | Shadow | Improved Shadow Word: Pain | 1 | 22/0/6 |
| 38-42 | Shadow | Spirit Tap | 5 | 22/0/11 |
| 43-46 | Shadow | Improved Mind Blast | 4 | 22/0/15 |
| 47-49 | Shadow | Shadow Weaving | 3 | 22/0/18 |
| 50 | Shadow | Improved Shadow Word: Pain | 1 | 22/0/19 |
| 51 | Shadow | Improved Mind Blast | 1 | 22/0/20 |
| 52 | Shadow | Improved Fade | 1 | 22/0/21 |
| 53 | Shadow | Vampiric Embrace | 1 | 22/0/22 |
| 54 | Shadow | Silence | 1 | 22/0/23 |
| 55-56 | Shadow | Devouring Contagion | 2 | 22/0/25 |
| 57-60 | Shadow | Darkness | 4 | 22/0/29 |

## Core talents (priority order)

1. **Meditation** — +2.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Spirit Tap** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Darkness** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Weaving** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Shadow Word: Pain** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Mental Agility** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
7. **Shadow Focus** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Mind Blast** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 42.66; discipline-leveling 51.10. The search simulated 51,696 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Discipline-Shadow leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/0240130313131--41502050001131204-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
