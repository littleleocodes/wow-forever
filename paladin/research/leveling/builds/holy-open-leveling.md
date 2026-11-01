# Holy — Leveling (open talent search) — 30/0/21

*[Paladin](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 30/0/21 (Holy / Protection / Retribution) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Holy leveling build the open leveling search found on 2026-10-23: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the holy-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (ret-dps). +18.8% faster per kill than holy-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Holy (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Spiritual Focus** | 2/5 | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 28% chance to not lose casting time when you take damage. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Purifying Power** | 1/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 10% and reduces the cooldown of your Exorcism and Holy Wrath spells by 17%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Divine Favor** | 1/1 | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Illumination** | 5/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |
| **Consecrated Ground** | 1/2 | **NEW** | Gives your Holy spells 5% increased damage against the first 4 enemies that enter your Consecration. |
| **Holy Shock** | 1/1 | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. |
| **Holy Power** | 5/5 | changed | Increases the critical strike healing bonus of your Holy spells by 50%. |

### Protection (0)

*No points.*

### Retribution (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 3/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 6%. |
| **Deflection** | 2/5 | moved | Increases your Parry chance by 2%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68 for 30 sec. |
| **Eye for an Eye** | 1/2 | changed | All critical strikes against you cause 5% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 1/3 | unchanged | Increases the physical damage you deal by 2%, and reduces all threat you generate by 7% while a two-handed melee weapon is equipped. |
| **Vengeance** | 1/3 | changed | Increases your Physical and Holy damage dealt by 1% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |

## Core talents (priority order)

1. **Sanctified Judgement** — +2.6 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Seals** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Holy Power** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
4. **Conviction** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Judgement** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Holy Conduit** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Sacred Arbiter** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Reverence** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 30.19; holy-leveling 35.88. The search simulated 40,560 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 30/0/21 -> 30/0/21; Divine Intellect 1 gone (moved to Protection); Reverence 3 -> 2 (rank cap); Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); +1 Holy Conduit (tier gating for Holy Power); +1 Holy Conduit (tier gating for Holy Power); refill +2 Pursuit of Justice, +1 Two-Handed Weapon Specialization, +1 Vengeance; order dropped (order_repair.py) (refill: the ret-dps model, leveling-st).

## Open questions (verify in the live game)

- An open-search Holy leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/paladin>
- <https://talentsforever.com/paladin/60/5102300310512115--23225131011-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
