# Holy-Shadow — Leveling (open talent search) — 16/17/18

*[Priest](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/17/18 (Discipline / Holy / Shadow) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy-Shadow (a Holy/Shadow hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (shadow-dps). +20.5% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Discipline (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Wand Specialization** | 2/2 | changed | Increases your damage with Wands by 25%. |
| **Mental Strength** | 3/5 | changed | Increases your total Intellect by 6%. |
| **Improved Power Word: Shield** | 3/3 | changed | Increases the damage absorbed by your Power Word: Shield by 20%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 1/3 | changed | Allows 17% of your Mana regeneration to continue while casting. |
| **Soul Warding** | 1/1 | **NEW** | Reduces the cooldown on your Power Word: Shield spell by 4 sec and reduces its mana cost by 15%. |

### Holy (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Holy Specialization** | 4/5 | unchanged | Increases the critical effect chance of your Holy spells by 4%. |
| **Improved Renew** | 3/3 | unchanged | Increases the amount healed by your Renew spell by 15%. |
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |

### Shadow (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 3/5 | changed | Improves your chance to hit with Shadow spells by 3%. |
| **Spirit Tap** | 5/5 | changed | Gives you a 100% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |
| **Improved Mind Blast** | 4/5 | changed | Reduces the cooldown of your Mind Blast spell by 2 sec. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Shadow Weaving** | 3/3 | changed | Your Shadow damage spells have a 100% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |

## Core talents (priority order)

1. **Meditation** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Shadow Word: Pain** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Spirit Tap** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Weaving** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Mind Blast** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Wand Specialization** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Shadow Focus** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Soul Warding** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 43.14; holy-leveling 51.98. The search simulated 41,544 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 16/17/18 -> 16/17/18; +1 Mental Strength (tier gating for Improved Power Word: Shield); +1 Mental Strength (tier gating for Improved Power Word: Shield); +1 Mental Strength (tier gating for Improved Power Word: Shield); -1 Mental Agility (over 51); -1 Meditation (over 51); -1 Meditation (over 51); order dropped (order_repair.py) (refill: the shadow-dps model, leveling-st).

## Open questions (verify in the live game)

- An open-search Holy-Shadow leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/priest>
- <https://talentsforever.com/priest/60/0250030113001-33405000002-3050204010003-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
