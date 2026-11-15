# Holy-Prot — Leveling (open talent search) — 21/16/14

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/16/14 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy-Prot (a Holy/Protection hybrid) leveling build the open leveling search found on 2026-11-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +15.6% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Illumination** | 4/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 80% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 1/2 | **NEW** | Improves your chance to hit with Holy spells by 4%, and reduces the duration of Silence effects on you by 10%. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |

### Protection (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Guardian's Favor** | 1/2 | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Toughness** | 4/5 | moved | Increases your armor value from items by 8%. |
| **Swift Judgement** | 1/1 | **NEW** | Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. |
| **Sacred Duty** | 1/2 | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec, and reduces the duration of Forbearance by 5 sec. |

### Retribution (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Holy | Divine Strength | 5 | 5/0/0 |
| 15-17 | Holy | Improved Seals | 3 | 8/0/0 |
| 18-19 | Holy | Reverence | 2 | 10/0/0 |
| 20-21 | Holy | Holy Conduit | 2 | 12/0/0 |
| 22-24 | Holy | Illumination | 3 | 15/0/0 |
| 25 | Holy | Divine Precision | 1 | 16/0/0 |
| 26 | Holy | Illumination | 1 | 17/0/0 |
| 27-28 | Holy | Improved Seals | 2 | 19/0/0 |
| 29 | Holy | Divine Favor | 1 | 20/0/0 |
| 30 | Holy | Holy Shock | 1 | 21/0/0 |
| 31-35 | Retribution | Benediction | 5 | 21/0/5 |
| 36-38 | Retribution | Sanctified Judgement | 3 | 21/0/8 |
| 39-40 | Retribution | Conviction | 2 | 21/0/10 |
| 41 | Retribution | Seal of Command | 1 | 21/0/11 |
| 42 | Retribution | Conviction | 1 | 21/0/12 |
| 43-44 | Retribution | Improved Judgement | 2 | 21/0/14 |
| 45-49 | Protection | Divine Intellect | 5 | 21/5/14 |
| 50-52 | Protection | Precision | 3 | 21/8/14 |
| 53 | Protection | Sacred Duty | 1 | 21/9/14 |
| 54 | Protection | Guardian's Favor | 1 | 21/10/14 |
| 55 | Protection | Templar's Bulwark | 1 | 21/11/14 |
| 56-59 | Protection | Toughness | 4 | 21/15/14 |
| 60 | Protection | Swift Judgement | 1 | 21/16/14 |

## Core talents (priority order)

1. **Swift Judgement** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Sanctified Judgement** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Seals** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Conviction** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
5. **Seal of Command** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Holy Conduit** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Judgement** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Precision** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-15: by hand, Redoubt to Sacred Duty at 53: Redoubt only adds block, which needs a shield, and this build fights with a two-hander; Sacred Duty holds the row to Templar's Bulwark open as well and takes 30 seconds a point off Divine Shield, Divine Protection and Templar's Bulwark (the fight lab measures the swap at 0.00%).
- 2026-11-15: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Deflection to Benediction at 35 (gate: -0.2% seed 3, -0.2% seed 4, level-weighted time per kill); Deflection to Benediction at 34 (gate: -0.3% seed 3, -0.2% seed 4, level-weighted time per kill); Improved Hammer of Justice to Toughness at 56 (gate: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.16; holy-leveling 37.18. The search simulated 38,773 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Holy-Prot leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/05025014210001-5131011031-23233001-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
