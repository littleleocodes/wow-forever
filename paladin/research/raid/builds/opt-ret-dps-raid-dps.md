# Optimizer — Two-handed Retribution: white 45%, seal procs 25% (Seal of Command via talent, Seal of Righteousness otherwise), Judgements 15%, Consecration 8%, Holy Strike 7% (Forever baseline ability; absent in Classic) (raid-dps) — 17/6/28

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/6/28 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `ret-dps` and profile `raid-dps`: score +139.4% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Holy (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 3/5 | **NEW** | Increases the damage done by your Seals and Judgements by 9%. |
| **Purifying Power** | 2/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Illumination** | 1/5 | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 20% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Divine Precision** | 2/2 | **NEW** | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |

### Protection (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 1/3 | changed | Improves your chance to hit by 1%. |

### Retribution (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Deflection** | 1/5 | moved | Increases your Parry chance by 1%. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Vindication** | 3/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 3/5 | **NEW** | Increases your spell damage by up to 36% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.6 sec. |

## Core talents (priority order)

1. **Seal of Command** — Removing it costs 86.0 points of score in this model.
2. **Divine Precision** — Removing it costs 20.4 points of score in this model.
3. **Sanctified Judgement** — Removing it costs 17.5 points of score in this model.
4. **Holy Conduit** — Removing it costs 17.5 points of score in this model.
5. **Vengeance** — Removing it costs 16.1 points of score in this model.
6. **Improved Seals** — Removing it costs 12.6 points of score in this model.
7. **Two-Handed Weapon Specialization** — Removing it costs 11.1 points of score in this model.
8. **Reverence** — Removing it costs 9.3 points of score in this model.

## Rank among our builds and the community simulator's

**5 of 7** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Unsealed Wrath* | community simulator | - | 477 | +0.0% | 874 | -0.5% | 26 s |
| 2 | *Holy Shock* | community simulator | - | 461 | -3.3% | 759 | -13.6% | 0 s |
| 3 | [`retribution-open-raid`](retribution-open-raid.md) | ours: derived (open search) | 16/4/31 | 449 | -6.0% | 878 | +0.0% | 47 s |
| 4 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 423 | -11.2% | 703 | -20.0% | 0 s |
| 5 | **[`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md)** | ours: optimizer | 17/6/28 | 422 | -11.6% | 703 | -20.0% | 0 s |
| 6 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 381 | -20.1% | 698 | -20.5% | 16 s |
| 7 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 377 | -21.0% | 699 | -20.4% | 18 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 5 passes, the last 2026-11-10, 1 changes to the base rotation; third-seed check: retribution-open-raid 867 -> 876 DPS (+1.0%), sim preset: Unsealed Wrath 865 -> 875 DPS (+1.1%), ret-raid-dps 691 -> 702 DPS (+1.7%), ret-full-buffs-raid 690 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 691 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 701 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to variableRef yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) casts/min |
|---|---|---|
| 1 | if not spellInRange: groupReference | as ready |
| 2 | if variableRef: cast Judgement | 7.6 |
| 3 | if time into the fight ≥ variableRef: use every other cooldown when ready | as ready |
| 4 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 1.3 |
| 5 | if variableRef and not Judgement is ready and variableRef: cast Holy Strike | 6.0 |
| 6 | if variableRef: cast Seal of Command | 2.3 |
| 7 | groupReference | as ready |
| 8 | groupReference | as ready |

Lines of the simulator's rotation these builds never cast: cast Seal of Righteousness (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) |
|---|---|
| Auto Attack | 23% |
| Judgement of Command | 19% |
| Seal of Command | 17% |
| Consecration | 17% |
| Holy Strike | 16% |
| Hammer of Wrath | 5% |
| Demonic Rune | 2% |
| spell 16614 | 0% |

## Notes

- Allocation taken from cand-ret-dps-r4 on 2026-10-26: the optimizer's earlier round beat its last export in the community simulator (383 vs 349 DPS; the calibration moved the model past the better build).
- Report: paladin/research/talents/forever/optimizer/ret-dps-raid-dps.md
- 2026-10-31 (repair_builds.py, client build 1.60.1.70707 trees): 17/0/34 -> 17/6/28; Divine Intellect 5 gone (moved to Protection); Reverence 3 -> 2 (rank cap); Holy Conduit 2 gone (moved to Holy); Conviction 5 -> 3 (rank cap); Instrument of Law 2 gone; Twist of Light 1 gone; +1 Deflection (tier gating for Champion of the Light); refill +2 Holy Conduit, +2 Purifying Power, +2 Divine Precision, +5 Redoubt, +1 Precision (refill: the ret-dps model, raid-dps).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/paladin>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
