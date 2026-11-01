# Holy — Leveling into the raid build — 30/16/5

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/16/5 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Level with the talents of the Holy raid build (holy-ml-heal) so you arrive at 60 ready to heal; the order is the fastest of three the fight lab raced (own tree first: 36 s per kill over levels 20-60, the holy-leveling rotation).

## Point allocation

### Holy (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Spiritual Focus** | 1/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 14% chance to not lose casting time when you take damage. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Infusion of Light** | 1/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 3/5 | unchanged | Increases your total Intellect by 6%. |
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Guardian's Favor** | 1/2 | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Sacred Duty** | 1/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec, and reduces the duration of Forbearance by 5 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Anticipation** | 1/5 | changed | Increases your Defense Skill by 4. |

### Retribution (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-10-25 (raid_path_leveling.py, user decision): healer and tank specs level into their raid build. Orders raced (fight lab, seed 3, 3000 fights per level, level-weighted): own tree first 36 s; stats model's order 36 s; own tree last 36 s. First Holy point at level 10.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 33/12/6 -> 30/16/5; Divine Intellect 5 gone (moved to Protection); Unyielding Faith 2 gone (moved to Retribution); Reverence 3 -> 2 (rank cap); Holy Conduit 1 gone (moved to Holy); +1 Precision (tier gating for Toughness); +1 Precision (tier gating for Toughness); +1 Precision (tier gating for Toughness); +1 Templar's Bulwark (tier gating for Anticipation); +1 Divine Intellect (tier gating for Anticipation); +1 Divine Intellect (tier gating for Anticipation); +1 Divine Intellect (tier gating for Anticipation); +1 Improved Seals (tier gating for Holy Power); +1 Improved Seals (tier gating for Holy Power); +1 Improved Seals (tier gating for Holy Power); +1 Holy Conduit (tier gating for Holy Power); +1 Holy Conduit (tier gating for Holy Power); -1 Improved Righteous Fury (over 51); -1 Anticipation (over 51); -1 Anticipation (over 51); order dropped (order_repair.py) (refill: the ret-dps model, leveling-st).

## Open questions (verify in the live game)

- Check the Holy leveling pace at launch; the raid build's talents may cost speed early.

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
