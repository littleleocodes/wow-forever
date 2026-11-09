# Holy/Protection hybrid — Leveling (open talent search) — 11/26/14

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 11/26/14 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy/Protection hybrid (a Holy/Protection hybrid) leveling build the open leveling search found on 2026-11-09: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the prot-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +2.0% faster per kill than protection-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 4/5 | **NEW** | Increases the damage done by your Seals and Judgements by 12%. |

### Protection (26)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 3/5 | unchanged | Increases your total Intellect by 6%. |
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Shield Specialization** | 2/2 | changed | Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 4% of your maximum Mana. May only occur once every 3 sec. |
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Swift Judgement** | 1/1 | **NEW** | Unleash the energy of a Seal spell upon an enemy. Does not consume the Seal. Refer to individual Seals for Judgement effect. Does not share a cooldown with your Judgement ability. |
| **Improved Righteous Fury** | 1/3 | changed | While Righteous Fury is active, all damage taken is reduced by 3%. |
| **Anticipation** | 3/5 | changed | Increases your Defense Skill by 12. |
| **Holy Shield** | 1/1 | changed | Increases chance to block by 30% for 10 sec, and deals 75 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges. |
| **Reckoning** | 5/5 | changed | Gives you a 40% chance after Blocking and a 100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec. |

### Retribution (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68 for 30 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-12 | Protection | Divine Intellect | 3 | 0/3/0 |
| 13-14 | Protection | Redoubt | 2 | 0/5/0 |
| 15-17 | Protection | Precision | 3 | 0/8/0 |
| 18-19 | Protection | Redoubt | 2 | 0/10/0 |
| 20 | Protection | Templar's Bulwark | 1 | 0/11/0 |
| 21 | Protection | Redoubt | 1 | 0/12/0 |
| 22-23 | Protection | Shield Specialization | 2 | 0/14/0 |
| 24 | Protection | Toughness | 1 | 0/15/0 |
| 25 | Protection | Swift Judgement | 1 | 0/16/0 |
| 26-28 | Protection | Anticipation | 3 | 0/19/0 |
| 29 | Protection | Improved Righteous Fury | 1 | 0/20/0 |
| 30 | Protection | Holy Shield | 1 | 0/21/0 |
| 31-35 | Retribution | Benediction | 5 | 0/21/5 |
| 36-38 | Retribution | Sanctified Judgement | 3 | 0/21/8 |
| 39-41 | Retribution | Conviction | 3 | 0/21/11 |
| 42 | Retribution | Improved Judgement | 1 | 0/21/12 |
| 43-44 | Holy | Divine Strength | 2 | 2/21/12 |
| 45 | Retribution | Improved Judgement | 1 | 2/21/13 |
| 46-48 | Holy | Divine Strength | 3 | 5/21/13 |
| 49-50 | Holy | Reverence | 2 | 7/21/13 |
| 51-53 | Holy | Improved Seals | 3 | 10/21/13 |
| 54 | Retribution | Vindication | 1 | 10/21/14 |
| 55 | Protection | Reckoning | 1 | 10/22/14 |
| 56 | Holy | Improved Seals | 1 | 11/22/14 |
| 57-60 | Protection | Reckoning | 4 | 11/26/14 |

## Core talents (priority order)

1. **Holy Shield** — +6.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Sanctified Judgement** — +3.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Shield Specialization** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Redoubt** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
5. **Reckoning** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Conviction** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Swift Judgement** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Seals** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-09: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing moved: Holy Conduit to Reckoning at 55 (measured: -0.4% seed 3, -0.3% seed 4, level-weighted time per kill); Holy Conduit to Vindication at 54 (tie-break: -0.2% seed 3, -0.2% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 30.70; protection-leveling 31.30. The search simulated 32,236 builds.
- The talent order takes the spec's signature talents at the earliest level their tree allows (the signature rule since 2026-11-06, fl_signature.sig_order), then follows the order the fight lab raced fastest.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Holy/Protection hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/050240002-353001021113014-05233-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
