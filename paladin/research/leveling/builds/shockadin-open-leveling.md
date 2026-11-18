# Shockadin — Leveling (open talent search) — 21/0/30

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shockadin (a Holy/Retribution hybrid) leveling build the open leveling search found on 2026-11-17: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +21.6% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Purifying Power** | 1/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 10% and reduces the cooldown of your Exorcism and Holy Wrath spells by 17%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 1/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 20% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |
| **Oath of Light** | 1/1 | **NEW** | Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229. Only one Oath of Light may be sworn by the Paladin at any one time. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |

### Protection (0)

*No points.*

### Retribution (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 1/5 | moved | Increases your Parry chance by 1%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 5/5 | **NEW** | Increases your spell damage by up to 60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 1.0 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Holy | Divine Strength | 5 | 5/0/0 |
| 15-17 | Holy | Improved Seals | 3 | 8/0/0 |
| 18-19 | Holy | Reverence | 2 | 10/0/0 |
| 20-21 | Holy | Holy Conduit | 2 | 12/0/0 |
| 22 | Holy | Purifying Power | 1 | 13/0/0 |
| 23-24 | Holy | Improved Seals | 2 | 15/0/0 |
| 25-26 | Holy | Divine Precision | 2 | 17/0/0 |
| 27 | Holy | Divine Favor | 1 | 18/0/0 |
| 28 | Holy | Illumination | 1 | 19/0/0 |
| 29 | Holy | Oath of Light | 1 | 20/0/0 |
| 30 | Holy | Holy Shock | 1 | 21/0/0 |
| 31-35 | Retribution | Benediction | 5 | 21/0/5 |
| 36-38 | Retribution | Sanctified Judgement | 3 | 21/0/8 |
| 39-40 | Retribution | Conviction | 2 | 21/0/10 |
| 41 | Retribution | Seal of Command | 1 | 21/0/11 |
| 42 | Retribution | Conviction | 1 | 21/0/12 |
| 43-44 | Retribution | Improved Judgement | 2 | 21/0/14 |
| 45 | Retribution | Vindication | 1 | 21/0/15 |
| 46 | Retribution | Sacred Arbiter | 1 | 21/0/16 |
| 47-49 | Retribution | Two-Handed Weapon Specialization | 3 | 21/0/19 |
| 50 | Retribution | Vindication | 1 | 21/0/20 |
| 51-53 | Retribution | Vengeance | 3 | 21/0/23 |
| 54 | Retribution | Vindication | 1 | 21/0/24 |
| 55 | Retribution | Deflection | 1 | 21/0/25 |
| 56-60 | Retribution | Champion of the Light | 5 | 21/0/30 |

## Core talents (priority order)

1. **Sanctified Judgement** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
2. **Conviction** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Vengeance** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Champion of the Light** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
5. **Two-Handed Weapon Specialization** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Holy Conduit** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Seals** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
8. **Vindication** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-17: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Infusion of Light to Illumination at 28 (gate: -0.1% seed 3, -0.2% seed 4, level-weighted time per kill).
- 2026-11-16: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Consecrated Ground to Champion of the Light at 59 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 28.23; holy-leveling 34.34. The search simulated 38,773 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shockadin leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/05025110221111--1523330100130034-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
