# Holy — Leveling into the raid build — 32/5/14

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 32/5/14 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Holy raid build (holy-ml-heal) so you arrive at 60 ready to heal; the order is the fastest of three the fight lab raced (stats model's order: 39 s per kill over levels 20-60, the holy-leveling rotation).

## Point allocation

### Holy (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Spiritual Focus** | 5/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Divine Strength** | 4/5 | unchanged | Increases your Strength by 8%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Oath of Light** | 1/1 | **NEW** | Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229. Only one Oath of Light may be sworn by the Paladin at any one time. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Boundless Light** | 1/2 | **NEW** | Increases the critical strike chance of your Holy Shock spell by 15% when cast on allies not affected by your Oath of Light. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to a friendly target for 30 sec. The caster's next Holy Shock on the target incurs no cooldown and heals the target and their party for 325 to 343. Only one Vigil per Paladin may be active in each party. |

### Protection (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |

### Retribution (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-13 | Holy | Divine Strength | 4 | 4/0/0 |
| 14 | Holy | Spiritual Focus | 1 | 5/0/0 |
| 15-16 | Holy | Reverence | 2 | 7/0/0 |
| 17-18 | Holy | Purifying Power | 2 | 9/0/0 |
| 19 | Holy | Spiritual Focus | 1 | 10/0/0 |
| 20-24 | Holy | Illumination | 5 | 15/0/0 |
| 25-27 | Holy | Spiritual Focus | 3 | 18/0/0 |
| 28-29 | Holy | Healing Light | 2 | 20/0/0 |
| 30 | Holy | Holy Shock | 1 | 21/0/0 |
| 31-35 | Retribution | Benediction | 5 | 21/0/5 |
| 36-38 | Retribution | Conviction | 3 | 21/0/8 |
| 39-40 | Retribution | Deflection | 2 | 21/0/10 |
| 41-42 | Retribution | Pursuit of Justice | 2 | 21/0/12 |
| 43-47 | Protection | Divine Intellect | 5 | 21/5/12 |
| 48-49 | Retribution | Unyielding Faith | 2 | 21/5/14 |
| 50 | Holy | Healing Light | 1 | 22/5/14 |
| 51 | Holy | Divine Favor | 1 | 23/5/14 |
| 52 | Holy | Infusion of Light | 1 | 24/5/14 |
| 53 | Holy | Oath of Light | 1 | 25/5/14 |
| 54-58 | Holy | Holy Power | 5 | 30/5/14 |
| 59 | Holy | Boundless Light | 1 | 31/5/14 |
| 60 | Holy | Light's Vigil | 1 | 32/5/14 |

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-09 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): stats model's order 39 s; own tree first 40 s; own tree last 39 s. First Holy point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.

## Open questions (verify in the live game)

- Check the Holy leveling pace at launch; the raid build's talents may cost speed early.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
