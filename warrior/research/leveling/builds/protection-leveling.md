# Protection — Leveling into the raid build — 17/3/31

*[Warrior](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/3/31 (Arms / Fury / Protection) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Protection raid build (protection-ml-tank) so you arrive at 60 ready to tank; the order is the fastest of three the fight lab raced (stats model's order: 28 s per kill over levels 20-60, the prot-leveling rotation).

## Point allocation

### Arms (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Heroic Strike** | 3/3 | changed | Reduces the cost of your Heroic Strike ability by 3 Rage. |
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Improved Rend** | 3/3 | changed | Increases the Bleed damage done by your Rend ability by 35%. |
| **Improved Overpower** | 1/2 | moved | Increases the critical strike chance of your Overpower ability by 25%. |
| **Deep Wounds** | 3/3 | changed | Your critical strikes cause your opponent to Bleed, dealing 60% of your melee weapon's average damage over 12 sec. |
| **Impale** | 2/2 | changed | Increases the critical strike damage bonus of your abilities by 20%. |

### Fury (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Cruelty** | 3/5 | changed | Improves your chance to get a critical strike with melee attacks by 3%. |

### Protection (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shield Specialization** | 5/5 | changed | Increases your chance to Block attacks with your shield by 5% and grants you a 100% chance to generate 5 Rage when you Block. |
| **Anticipation** | 5/5 | changed | Increases your Defense Skill by 20. |
| **Improved Revenge** | 3/3 | changed | Increases damage dealt by your Revenge ability by 60%. |
| **Master of Defense** | 2/2 | **NEW** | Grants you a 100% chance to generate 5 Rage when you Dodge or Parry while a shield is equipped. |
| **Defiance** | 3/3 | changed | Increases all threat generated in Defensive stance by an additional 20% while a shield is equipped. |
| **Improved Sunder Armor** | 3/3 | changed | Reduces the Rage cost of your Sunder Armor ability by 3. |
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
| 23-24 | Protection | Master of Defense | 2 | 0/0/15 |
| 25-27 | Protection | Defiance | 3 | 0/0/18 |
| 28-29 | Protection | Improved Sunder Armor | 2 | 0/0/20 |
| 30-32 | Protection | Focused Rage | 3 | 0/0/23 |
| 33 | Protection | Concussion Blow | 1 | 0/0/24 |
| 34 | Protection | Improved Sunder Armor | 1 | 0/0/25 |
| 35-39 | Protection | Bastion | 5 | 0/0/30 |
| 40 | Protection | Shield Slam | 1 | 0/0/31 |
| 41-43 | Arms | Improved Rend | 3 | 3/0/31 |
| 44-45 | Arms | Deflection | 2 | 5/0/31 |
| 46 | Arms | Improved Overpower | 1 | 6/0/31 |
| 47-49 | Arms | Deflection | 3 | 9/0/31 |
| 50 | Arms | Improved Heroic Strike | 1 | 10/0/31 |
| 51-53 | Arms | Deep Wounds | 3 | 13/0/31 |
| 54 | Fury | Cruelty | 1 | 13/1/31 |
| 55-56 | Arms | Improved Heroic Strike | 2 | 15/1/31 |
| 57-58 | Arms | Impale | 2 | 17/1/31 |
| 59-60 | Fury | Cruelty | 2 | 17/3/31 |

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-07 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): stats model's order 28 s; own tree first 28 s; own tree last 28 s. First Protection point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Check the Protection leveling pace at launch; the raid build's talents may cost speed early.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
