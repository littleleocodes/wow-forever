# Holy — Leveling into the raid build — 33/12/6

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/12/6 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Holy raid build (holy-ml-heal) so you arrive at 60 ready to heal; the order is the fastest of three the fight lab raced (own tree first: 37 s per kill over levels 20-60, the holy-leveling rotation).

## Point allocation

### Holy (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Spiritual Focus** | 1/2 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 35% chance to not lose casting time when you take damage. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Power** | 5/5 | changed | Increases the critical strike chance of your Holy Shock and Holy Strike spells by 15%, and all other spells by 5%. |

### Protection (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 20%. Lasts 10 sec or 5 blocks. |
| **Guardian's Favor** | 1/2 | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. |
| **Anticipation** | 3/5 | changed | Increases your Defense Skill by 12. |
| **Improved Righteous Fury** | 1/3 | changed | While Righteous Fury is active, all damage taken is reduced by 2%. |
| **Sacred Duty** | 1/2 | **NEW** | Increases your total Stamina by 2% and reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec. |

### Retribution (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Holy Conduit** | 1/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 20%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Holy | Divine Strength | 5 | 5/0/0 |
| 15-19 | Holy | Divine Intellect | 5 | 10/0/0 |
| 20-22 | Holy | Reverence | 3 | 13/0/0 |
| 23-24 | Holy | Purifying Power | 2 | 15/0/0 |
| 25-29 | Holy | Illumination | 5 | 20/0/0 |
| 30-31 | Holy | Unyielding Faith | 2 | 22/0/0 |
| 32-34 | Holy | Healing Light | 3 | 25/0/0 |
| 35-39 | Holy | Holy Power | 5 | 30/0/0 |
| 40 | Holy | Spiritual Focus | 1 | 31/0/0 |
| 41 | Holy | Infusion of Light | 1 | 32/0/0 |
| 42 | Holy | Divine Favor | 1 | 33/0/0 |
| 43-47 | Retribution | Benediction | 5 | 33/0/5 |
| 48 | Retribution | Holy Conduit | 1 | 33/0/6 |
| 49 | Protection | Toughness | 1 | 33/1/6 |
| 50-53 | Protection | Redoubt | 4 | 33/5/6 |
| 54-56 | Protection | Anticipation | 3 | 33/8/6 |
| 57 | Protection | Redoubt | 1 | 33/9/6 |
| 58 | Protection | Guardian's Favor | 1 | 33/10/6 |
| 59 | Protection | Sacred Duty | 1 | 33/11/6 |
| 60 | Protection | Improved Righteous Fury | 1 | 33/12/6 |

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-10-22 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): own tree first 37 s; stats model's order 37 s; own tree last 37 s. First Holy point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Check the Holy leveling pace at launch; the raid build's talents may cost speed early.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
