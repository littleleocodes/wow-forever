# Protection — Leveling into the raid build — 14/5/32

*[Warrior](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/5/32 (Arms / Fury / Protection) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Protection raid build (opt-prot-tank-raid-tank) so you arrive at 60 ready to tank; the order is the fastest of three the fight lab raced (own tree first: 28 s per kill over levels 20-60, the prot-leveling rotation).

## Point allocation

### Arms (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |

### Fury (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |

### Protection (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shield Specialization** | 5/5 | changed | Increases your chance to Block attacks with your shield by 5% and grants you a 100% chance to generate 5 Rage when you Block. |
| **Improved Revenge** | 3/3 | changed | Increases damage dealt by your Revenge ability by 60%. |
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Improved Thunder Clap** | 3/3 | changed | Reduces the Rage cost of your Thunder Clap ability by 6. |
| **Defiance** | 3/3 | changed | Increases all threat generated in Defensive stance by an additional 15% while a shield is equipped. |
| **Master of Defense** | 2/2 | **NEW** | Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. |
| **Vanguard** | 1/1 | **NEW** | Your Charge ability is now usable while in Defensive Stance. |
| **Concussion Blow** | 1/1 | changed | Stuns the target for 5 sec. |
| **Focused Rage** | 3/3 | **NEW** | Reduces the Rage cost of your offensive abilities by 3. |
| **Bastion** | 5/5 | **NEW** | Increases all damage you deal by 10% while a shield is equipped. |
| **Shield Slam** | 1/1 | changed | Slam the target with your shield, causing 421 to 439 damage, increased by your Block Value, and has a 50% chance of dispelling 1 magic effect on the target. Causes a very high amount of threat. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Protection | Shield Specialization | 5 | 0/0/5 |
| 15-19 | Protection | Anticipation | 5 | 0/0/10 |
| 20-22 | Protection | Improved Revenge | 3 | 0/0/13 |
| 23-25 | Protection | Improved Thunder Clap | 3 | 0/0/16 |
| 26-28 | Protection | Defiance | 3 | 0/0/19 |
| 29 | Protection | Master of Defense | 1 | 0/0/20 |
| 30-32 | Protection | Focused Rage | 3 | 0/0/23 |
| 33 | Protection | Concussion Blow | 1 | 0/0/24 |
| 34 | Protection | Master of Defense | 1 | 0/0/25 |
| 35 | Protection | Vanguard | 1 | 0/0/26 |
| 36-40 | Protection | Bastion | 5 | 0/0/31 |
| 41 | Protection | Shield Slam | 1 | 0/0/32 |
| 42-44 | Arms | Improved Rend | 3 | 3/0/32 |
| 45-46 | Fury | Cruelty | 2 | 3/2/32 |
| 47-50 | Arms | Deflection | 4 | 7/2/32 |
| 51-53 | Fury | Cruelty | 3 | 7/5/32 |
| 54 | Arms | Deflection | 1 | 8/5/32 |
| 55-56 | Arms | Improved Heroic Strike | 2 | 10/5/32 |
| 57-59 | Arms | Deep Wounds | 3 | 13/5/32 |
| 60 | Arms | Improved Heroic Strike | 1 | 14/5/32 |

## Core talents (priority order)

1. **Shield Slam** — Removing it costs 22.7 points of score in this model.
2. **Defiance** — Removing it costs 10.9 points of score in this model.
3. **Deflection** — Removing it costs 5.9 points of score in this model.
4. **Bastion** — Removing it costs 5.4 points of score in this model.
5. **Improved Revenge** — Removing it costs 4.8 points of score in this model.
6. **Focused Rage** — Removing it costs 4.2 points of score in this model.
7. **Anticipation** — Removing it costs 3.0 points of score in this model.
8. **Shield Specialization** — Removing it costs 2.9 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-10-15 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): own tree first 28 s; stats model's order 30 s; own tree last 31 s. First Protection point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Check the Protection leveling pace at launch; the raid build's talents may cost speed early.

## Sources

- <https://warcraftforever.games/talents/warrior>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
