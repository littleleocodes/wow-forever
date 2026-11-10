# Retribution — Raid (open talent search) — 16/4/31

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 16/4/31 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Retribution raid build the open talent search found on 2026-11-10: every legal 51-point build with no tree rule, searched in the community simulator's ret-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +24.6% over ret-raid-dps, the best of our builds in that rotation.

## Point allocation

### Holy (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |
| **Divine Precision** | 1/2 | **NEW** | Improves your chance to hit with Holy spells by 4%, and reduces the duration of Silence effects on you by 10%. |
| **Purifying Power** | 1/2 | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 10% and reduces the cooldown of your Exorcism and Holy Wrath spells by 17%. |

### Protection (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 4/5 | unchanged | Increases your total Intellect by 8%. |

### Retribution (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
| **Benediction** | 4/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 8%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 2/3 | **NEW** | Gives your Judgement ability a 66% chance to return 40% of the Mana cost of the judged seal. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Repentance** | 1/1 | moved | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 5/5 | **NEW** | Increases your spell damage by up to 60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 1.0 sec. |
| **Unsealed Wrath** | 1/1 | **NEW** | Your melee attacks store a copy of your active Seal for 15 sec, stacking up to 3 times. Landing an attack with a different Seal consumes all stacks, giving the stored Seal its normal chance to activate once per stack. |

## Core talents (priority order)

1. **Seal of Command** — 160 DPS lost without it (19% of the build in a full raid; removal, 12,000 fights).
2. **Unsealed Wrath** — 138 DPS lost without it (16% of the build in a full raid; removal, 12,000 fights).
3. **Vengeance** — 64 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Champion of the Light** — 54 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).
5. **Improved Seals** — 44 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
6. **Conviction** — 39 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Two-Handed Weapon Specialization** — 38 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Improved Judgement** — 34 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**3 of 7** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Unsealed Wrath* | community simulator | - | 477 | +0.0% | 874 | -0.5% | 26 s |
| 2 | *Holy Shock* | community simulator | - | 461 | -3.3% | 759 | -13.6% | 0 s |
| 3 | **[`retribution-open-raid`](retribution-open-raid.md)** | ours: derived (open search) | 16/4/31 | 449 | -6.0% | 878 | +0.0% | 47 s |
| 4 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 423 | -11.2% | 703 | -20.0% | 0 s |
| 5 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 422 | -11.6% | 703 | -20.0% | 0 s |
| 6 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 381 | -20.1% | 698 | -20.5% | 16 s |
| 7 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 377 | -21.0% | 699 | -20.4% | 18 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation (no rotation search recorded).
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 5 passes, the last 2026-11-10, 1 changes to the base rotation; third-seed check: retribution-open-raid 867 -> 876 DPS (+1.0%), sim preset: Unsealed Wrath 865 -> 875 DPS (+1.1%), ret-raid-dps 691 -> 702 DPS (+1.7%), ret-full-buffs-raid 690 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 691 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 701 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to variableRef yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`retribution-open-raid`](retribution-open-raid.md) casts/min |
|---|---|---|
| 1 | if not spellInRange: groupReference | as ready |
| 2 | if variableRef: cast Judgement | 7.0 |
| 3 | if time into the fight ≥ variableRef: use every other cooldown when ready | as ready |
| 4 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.9 |
| 5 | if variableRef and not Judgement is ready and variableRef: cast Holy Strike | 5.8 |
| 6 | if variableRef: cast Seal of Command | 3.1 |
| 7 | if variableRef: cast Seal of Righteousness | 2.9 |
| 8 | groupReference | as ready |
| 9 | groupReference | as ready |

Damage by ability:

| Ability | [`retribution-open-raid`](retribution-open-raid.md) |
|---|---|
| Auto Attack | 22% |
| Seal of Command | 21% |
| Holy Strike | 15% |
| Judgement of Command | 12% |
| Consecration | 10% |
| Seal of Righteousness | 8% |
| Judgement of Righteousness | 6% |
| Hammer of Wrath | 4% |
| Demonic Rune | 2% |
| spell 16614 | 0% |

## Notes

- Open search result (ret-dps, full raid): 16/4/31 (Retribution) at 839.0 DPS; ret-raid-dps 673.5, opt-ret-dps-raid-dps 673.5, ret-full-buffs-raid 671.4, retribution-ml-raid 671.3 in the same fights; 2,050 builds simulated, 1 independent runs reached the top.
- The ret-dps raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): shockadin-raid -17.8%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Illumination, Deflection, Sanctified Judgement, Unyielding Faith, Repentance.
- Simulator numbers are the community's model of the beta (wowsims/forever 16e8542 (client 70790) with this project's patches), not in-game measurements.
- 2026-11-10 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Illumination -> Purifying Power (mana); Deflection -> Benediction (mana); Deflection -> Benediction (mana); Unyielding Faith -> Deflection (survival); Unyielding Faith -> Deflection (survival). Net -0.02% on a third seed.

## Open questions (verify in the live game)

- An open-search Retribution build: check it against the community's Retribution builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/paladin/60/0502500121-4-32232021201301351-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
