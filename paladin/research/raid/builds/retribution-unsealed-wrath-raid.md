# Retribution — Unsealed Wrath (the simulator's own build) — 14/6/31

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 14/6/31 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own Retribution build (Unsealed Wrath, 14/6/31): Seal of Command and Seal of Righteousness twisted for Unsealed Wrath's stored seals, Holy Strike, Consecration, judgements. In a full raid under our raid rotation (2026-11-20, 10,000 fights, seeds 1 / 2): 767.4 / 767.6 against our open-search build's 769.3 / 769.3, within 0.3%; Unsealed Wrath is worth 14.9% of it there (667.7 without the talent).

## Point allocation

### Holy (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Reverence** | 2/2 | **NEW** | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |
| **Holy Conduit** | 2/2 | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |

### Protection (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Precision** | 1/3 | changed | Improves your chance to hit by 1%. |

### Retribution (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Unyielding Faith** | 1/2 | changed | Reduces the duration of Fear and Disorient effects on you by 15%. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Pursuit of Justice** | 2/2 | changed | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Repentance** | 1/1 | moved | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 5/5 | **NEW** | Increases your spell damage by up to 60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 1.0 sec. |
| **Unsealed Wrath** | 1/1 | **NEW** | Your melee attacks store a copy of your active Seal for 15 sec, stacking up to 3 times. Landing an attack with a different Seal consumes all stacks, giving the stored Seal its normal chance to activate once per stack. |

## Core talents (priority order)

1. **Unsealed Wrath** — Your melee attacks store a copy of your active Seal for 15 sec, stacking up to 3 times
2. **Champion of the Light** — Increases your spell damage by up to 60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 1.0 sec
3. **Repentance** — Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec
4. **Vengeance** — Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike
5. **Sacred Arbiter** — Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target

## Rank among our builds and the community simulator's

**1 of 9** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`retribution-unsealed-wrath-raid`](retribution-unsealed-wrath-raid.md)** | ours: derived (simulator preset) | 14/6/31 | 442 | +0.0% | 768 | -0.2% | 32 s |
| 2 | *Unsealed Wrath* | community simulator | - | 442 | +0.0% | 768 | -0.2% | 32 s |
| 3 | *Holy Shock* | community simulator | - | 431 | -2.6% | 680 | -11.6% | 0 s |
| 4 | [`retribution-open-raid`](retribution-open-raid.md) | ours: derived (open search) | 16/4/31 | 426 | -3.7% | 769 | +0.0% | 45 s |
| 5 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 396 | -10.4% | 632 | -17.8% | 0 s |
| 6 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 396 | -10.4% | 632 | -17.8% | 0 s |
| 7 | [`prot-ret-ml-raid`](prot-ret-ml-raid.md) | ours: derived (ML search) | 10/12/29 | 366 | -17.1% | 655 | -14.9% | 9 s |
| 8 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 351 | -20.7% | 629 | -18.3% | 9 s |
| 9 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 348 | -21.2% | 628 | -18.3% | 12 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-11-13, 1 changes to the base rotation; third-seed check: ):
  1. spell probe: insert at the end: cast Divine Favor (+0.2%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 5 passes, the last 2026-11-10, 1 changes to the base rotation; third-seed check: retribution-open-raid 867 -> 876 DPS (+1.0%), sim preset: Unsealed Wrath 865 -> 875 DPS (+1.1%), ret-raid-dps 691 -> 702 DPS (+1.7%), ret-full-buffs-raid 690 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 691 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 701 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to “Pull range” yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`retribution-unsealed-wrath-raid`](retribution-unsealed-wrath-raid.md) casts/min |
|---|---|---|
| 1 | if not Holy Strike is in range and “Has assigned judgement” and Seal of Command is taken and (“Use Seal of Command” or not “Use Seal of Righteousness” or Unsealed Wrath is taken) and not the sequence is complete: sequence 'move1': move to “Melee range” yd; wait until Judgement is in range; cast Judgement; wait inputDelay; cast Seal of Command; wait until Holy Strike is in range | 12.8 |
| 2 | if not Holy Strike is in range and “Has assigned judgement” and (not Unsealed Wrath is taken or not Seal of Command is taken or not “Use Seal of Command”) and not the sequence is complete: sequence 'move2': move to “Melee range” yd; wait until Judgement is in range; cast Judgement; wait inputDelay; cast Seal of Righteousness; wait until Holy Strike is in range | 12.6 |
| 3 | if “WF guard”: cast Judgement | 7.2 |
| 4 | if time into the fight ≥ “Delay Major CDs”: use every other cooldown when ready | as ready |
| 5 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 1.2 |
| 6 | if “WF guard” and not Judgement is ready and “Judge realism protection”: cast Holy Strike | 5.8 |
| 7 | if “Should refresh SoC”: cast Seal of Command | 5.6 |
| 8 | if “Should refresh SoR”: cast Seal of Righteousness | 5.4 |
| 9 | if time to the next auto attack > 1.5s and mana % ≥ 10% and not Judgement is ready and not Holy Strike is ready: cast Consecration | 4.7 |

Lines of the simulator's rotation these builds never cast: sequence 'move3': move to “Melee range” yd; wait until Judgement is in range; cast Judgement; wait until Holy Strike is in range (a switch this rotation keeps off); cast Exorcism (its condition never held in these fights); cast Divine Favor (needs the Divine Favor talent).

Damage by ability:

| Ability | [`retribution-unsealed-wrath-raid`](retribution-unsealed-wrath-raid.md) |
|---|---|
| Auto Attack | 22% |
| Seal of Command | 16% |
| Holy Strike | 14% |
| Judgement of Command | 13% |
| Consecration | 12% |
| Seal of Righteousness | 11% |
| Judgement of Righteousness | 6% |
| Hammer of Wrath | 5% |
| Demonic Rune | 2% |

## Notes

- The simulator's own build, credited (Simulator build first, 2026-11-20): the page starts from it; ours replaces it only when 0.5% ahead on two seeds and passing the spec's rules.
- Within 0.3% of our open-search build (769.3) under the same rotation: Retribution's full search of the optimality pass, with the seal-twist knob in the rotation search, settles which leads.
- Simulator numbers are the community's model of the game, not in-game measurements.

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d844dc4d6790f984b9a1817fc583f7ca2e/ui/specs/paladin/retribution/builds/unsealed_wrath.siml>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
