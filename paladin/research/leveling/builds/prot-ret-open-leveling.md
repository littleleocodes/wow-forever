# Prot-Ret — Leveling (open talent search) — 0/22/29

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/22/29 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Prot-Ret (a Protection/Retribution hybrid) leveling build the open leveling search found on 2026-10-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the prot-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +9.6% faster per kill than protection-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (0)

*No points.*

### Protection (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 20%. Lasts 10 sec or 5 blocks. |
| **Precision** | 3/3 | changed | Improves your chance to hit by 3%. |
| **Anticipation** | 3/5 | changed | Increases your Defense Skill by 12. |
| **Improved Seal of Fury** | 1/1 | **NEW** | When Seal of Fury's shield is fully absorbed, restore 60 Mana, increased by 15% per level the attacker is above you, up to 45%. |
| **Shield Specialization** | 3/3 | changed | Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 6% of your maximum Mana. May only occur once every 3 sec. |
| **Swift Judgement** | 1/1 | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. |
| **One-Handed Weapon Specialization** | 3/3 | changed | Increases the damage you deal with one-handed melee weapons by 10%. |
| **Reckoning** | 2/5 | changed | Gives you a 16% chance to gain an extra attack after Blocking a melee attack and a 40% chance to gain an extra attack after being the victim of a non-periodic critical strike. Cannot occur more often than once every 1.5 sec. |

### Retribution (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 1/2 | changed | Decreases the cooldown of your Judgement ability by 1 sec. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Conviction** | 5/5 | changed | Improves your chance to get a critical strike with melee attacks by 5%. |
| **Vindication** | 2/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 136, and increase your Attack Power by 2% for 30 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 1/2 | changed | Increases movement speed and mounted movement speed by 8%. This does not stack with other movement speed increasing effects. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |
| **Champion of the Light** | 3/3 | **NEW** | Increases your spell damage by up to 60% of your Intellect. |
| **Instrument of Law** | 1/2 | **NEW** | Reduces the cast time of your Hammer of Wrath by 0.5 sec, and reduces all threat you generate by 10% while Righteous Fury is not active. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Protection | Redoubt | 5 | 0/5/0 |
| 15-17 | Protection | Precision | 3 | 0/8/0 |
| 18-19 | Protection | Anticipation | 2 | 0/10/0 |
| 20-22 | Protection | Shield Specialization | 3 | 0/13/0 |
| 23 | Protection | Anticipation | 1 | 0/14/0 |
| 24 | Protection | Improved Seal of Fury | 1 | 0/15/0 |
| 25 | Protection | Swift Judgement | 1 | 0/16/0 |
| 26 | Protection | Toughness | 1 | 0/17/0 |
| 27-29 | Protection | One-Handed Weapon Specialization | 3 | 0/20/0 |
| 30-31 | Protection | Reckoning | 2 | 0/22/0 |
| 32-36 | Retribution | Benediction | 5 | 0/22/5 |
| 37-38 | Retribution | Holy Conduit | 2 | 0/22/7 |
| 39 | Retribution | Improved Judgement | 1 | 0/22/8 |
| 40-41 | Retribution | Conviction | 2 | 0/22/10 |
| 42-43 | Retribution | Sanctified Judgement | 2 | 0/22/12 |
| 44 | Retribution | Pursuit of Justice | 1 | 0/22/13 |
| 45 | Retribution | Sanctified Judgement | 1 | 0/22/14 |
| 46 | Retribution | Conviction | 1 | 0/22/15 |
| 47 | Retribution | Sacred Arbiter | 1 | 0/22/16 |
| 48-49 | Retribution | Conviction | 2 | 0/22/18 |
| 50-51 | Retribution | Vindication | 2 | 0/22/20 |
| 52-54 | Retribution | Vengeance | 3 | 0/22/23 |
| 55-56 | Retribution | Deflection | 2 | 0/22/25 |
| 57 | Retribution | Instrument of Law | 1 | 0/22/26 |
| 58-60 | Retribution | Champion of the Light | 3 | 0/22/29 |

## Core talents (priority order)

1. **Holy Conduit** — +3.3 s per kill at level 60 without it (removal, 3,000 fights).
2. **Sanctified Judgement** — +3.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Seal of Fury** — +3.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **One-Handed Weapon Specialization** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
5. **Conviction** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
6. **Vengeance** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
7. **Champion of the Light** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
8. **Sacred Arbiter** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.52; protection-leveling 35.64. The search simulated 72,124 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Prot-Ret leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/-15303103013002-2512523010103031-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
