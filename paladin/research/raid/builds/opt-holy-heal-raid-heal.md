# Optimizer — Raid healing: Flash of Light 55%, Holy Light 35%, Holy Shock 5% (talent/instant), Lay on Hands 5% (raid-heal) — 31/7/13

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/7/13 (Holy / Protection / Retribution) |
| **Role** | HEALER — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `holy-heal` and profile `raid-heal`: score +94.6% (healing score: 0.6 x HPS gain + 0.5 x mana gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Divine Strength** | 1/5 | unchanged | Increases your Strength by 2%. |
| **Healing Light** | 3/3 | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Spiritual Focus** | 2/2 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Reverence** | 3/3 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Infusion of Light** | 2/2 | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Holy Power** | 5/5 | changed | Increases the critical strike chance of your Holy Shock and Holy Strike spells by 15%, and all other spells by 5%. |
| **Light's Vigil** | 1/1 | **NEW** | Applies Light's Vigil to the target for 30 sec. Your next Holy Shock cast on them triggers no cooldown and causes enemy targets to suffer 175 to 189 Holy damage and refund 75% of Light's Vigil's Mana cost, or allied targets to heal their party for 325 to 343. You may only have one Light's Vigil active per party. |

### Protection (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 5/5 | moved | Increases your armor value from items by 10%. |
| **Guardian's Favor** | 2/2 | changed | Reduces the cooldown of your Blessing of Protection by 2 min and increases the duration of your Blessing of Freedom by 6 sec. |

### Retribution (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Deflection** | 5/5 | moved | Increases your Parry chance by 5%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |

## Core talents (priority order)

1. **Illumination** — Removing it costs 24.0 points of score in this model.
2. **Reverence** — Removing it costs 20.3 points of score in this model.
3. **Healing Light** — Removing it costs 11.7 points of score in this model.
4. **Divine Intellect** — Removing it costs 8.0 points of score in this model.
5. **Divine Favor** — Removing it costs 7.6 points of score in this model.
6. **Holy Power** — Removing it costs 6.3 points of score in this model.
7. **Light's Vigil** — Removing it costs 6.2 points of score in this model.
8. **Sanctified Judgement** — Removing it costs 6.0 points of score in this model.

## Rotation

A healer: not in the community simulator, see the healer lab section of the [raid README](../README.md).

## Notes

- Report: paladin/research/talents/forever/optimizer/holy-heal-raid-heal.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
