# Prot-Ret — Raid (machine-learning search) — 10/12/29

*[Paladin](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 10/12/29 (Holy / Protection / Retribution) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Prot-Ret build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-11-13 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry ret-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Holy (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Strength** | 5/5 | unchanged | Increases your Strength by 10%. |
| **Improved Seals** | 5/5 | **NEW** | Increases the damage done by your Seals and Judgements by 15%. |

### Protection (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Divine Intellect** | 5/5 | unchanged | Increases your total Intellect by 10%. |
| **Redoubt** | 3/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 18%. Lasts 10 sec or 5 blocks. |
| **Precision** | 2/3 | changed | Improves your chance to hit by 2%. |
| **Templar's Bulwark** | 1/1 | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. |
| **Toughness** | 1/5 | moved | Increases your armor value from items by 2%. |

### Retribution (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 1/5 | moved | Increases your Parry chance by 1%. |
| **Benediction** | 5/5 | changed | Reduces the Mana cost of all instant cast spells and abilities by 10%. |
| **Improved Judgement** | 2/2 | changed | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3/3 | changed | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3/3 | **NEW** | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |
| **Vindication** | 1/3 | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68 for 30 sec. |
| **Seal of Command** | 1/1 | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. |
| **Sacred Arbiter** | 1/1 | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. |
| **Two-Handed Weapon Specialization** | 3/3 | unchanged | Increases the Holy and Physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |
| **Vengeance** | 3/3 | changed | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 5 times. |
| **Champion of the Light** | 4/5 | **NEW** | Increases your spell damage by up to 48% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.8 sec. |
| **Unyielding Faith** | 2/2 | changed | Reduces the duration of Fear and Disorient effects on you by 30%. |

## Rank among our builds and the community simulator's

**7 of 9** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`retribution-unsealed-wrath-raid`](retribution-unsealed-wrath-raid.md) | ours: derived (simulator preset) | 14/6/31 | 442 | +0.0% | 768 | -0.2% | 32 s |
| 2 | *Unsealed Wrath* | community simulator | - | 442 | +0.0% | 768 | -0.2% | 32 s |
| 3 | *Holy Shock* | community simulator | - | 431 | -2.6% | 680 | -11.6% | 0 s |
| 4 | [`retribution-open-raid`](retribution-open-raid.md) | ours: derived (open search) | 16/4/31 | 426 | -3.7% | 769 | +0.0% | 45 s |
| 5 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 396 | -10.4% | 632 | -17.8% | 0 s |
| 6 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 396 | -10.4% | 632 | -17.8% | 0 s |
| 7 | **[`prot-ret-ml-raid`](prot-ret-ml-raid.md)** | ours: derived (ML search) | 10/12/29 | 366 | -17.1% | 655 | -14.9% | 9 s |
| 8 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 351 | -20.7% | 629 | -18.3% | 9 s |
| 9 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 348 | -21.2% | 628 | -18.3% | 12 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-11-13, 1 changes to the base rotation; third-seed check: ):
  1. spell probe: insert at the end: cast Divine Favor (+0.2%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 5 passes, the last 2026-11-10, 1 changes to the base rotation; third-seed check: retribution-open-raid 867 -> 876 DPS (+1.0%), sim preset: Unsealed Wrath 865 -> 875 DPS (+1.1%), ret-raid-dps 691 -> 702 DPS (+1.7%), ret-full-buffs-raid 690 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 691 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 701 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to “Pull range” yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`prot-ret-ml-raid`](prot-ret-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not Holy Strike is in range and “Has assigned judgement” and Seal of Command is taken and (“Use Seal of Command” or not “Use Seal of Righteousness” or Unsealed Wrath is taken) and not the sequence is complete: sequence 'move1': move to “Melee range” yd; wait until Judgement is in range; cast Judgement; wait inputDelay; cast Seal of Command; wait until Holy Strike is in range | 9.4 |
| 2 | if not Holy Strike is in range and “Has assigned judgement” and (not Unsealed Wrath is taken or not Seal of Command is taken or not “Use Seal of Command”) and not the sequence is complete: sequence 'move2': move to “Melee range” yd; wait until Judgement is in range; cast Judgement; wait inputDelay; cast Seal of Righteousness; wait until Holy Strike is in range | 7.3 |
| 3 | if “WF guard”: cast Judgement | 7.3 |
| 4 | if time into the fight ≥ “Delay Major CDs”: use every other cooldown when ready | as ready |
| 5 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.9 |
| 6 | if “WF guard” and not Judgement is ready and “Judge realism protection”: cast Holy Strike | 5.8 |
| 7 | if “Should refresh SoC”: cast Seal of Command | 2.1 |
| 8 | if time to the next auto attack > 1.5s and mana % ≥ 10% and not Judgement is ready and not Holy Strike is ready: cast Consecration | 5.1 |

Lines of the simulator's rotation these builds never cast: sequence 'move3': move to “Melee range” yd; wait until Judgement is in range; cast Judgement; wait until Holy Strike is in range (a switch this rotation keeps off); cast Seal of Righteousness, cast Exorcism (its condition never held in these fights); cast Divine Favor (needs the Divine Favor talent).

Damage by ability:

| Ability | [`prot-ret-ml-raid`](prot-ret-ml-raid.md) |
|---|---|
| Auto Attack | 25% |
| Judgement of Command | 22% |
| Holy Strike | 16% |
| Consecration | 15% |
| Seal of Command | 15% |
| Hammer of Wrath | 4% |
| Demonic Rune | 3% |

## Notes

- Against the best hand draft ret-full-buffs-raid in a full raid, same gear and fights (100,000, one seed): +3.5% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow ret-full-buffs-raid: Pursuit of Justice → Deflection, Guardian's Favor → Redoubt (2 points), Templar's Bulwark → Redoubt (within 0.00% of the search winner 10/12/29 on one seed, 30,000 fights).
- Search result (full raid): 10/12/29 at 682.0 ± 0.13 DPS over 100,000 fights; runner-up 10/12/29 (+0.00%; the winner takes Templar's Bulwark 1, Vindication 3; the runner-up Deflection 1, Sacred Duty 1, Vindication 2); 1,616 builds simulated; certificate: none of its 216 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever ff9babb (client 70888) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 10/12/29 at 676.9 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 13/14/24 at 410.2 DPS.
- 2026-11-13 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Vindication -> Deflection (survival); Vindication -> Deflection (survival). Net +0.00% on a third seed.
- 2026-11-20: filler points moved (1 point from Redoubt to Templar's Bulwark; 1 point from Redoubt to Toughness): the same DPS bit for bit in a full raid and on the training dummy. The new talents follow the utility order (interrupt protection, threat, mana, range, survival; dodge, parry and block count for nothing in a damage dealer's raid), which the simulator cannot measure (deep-runs/credited_fillers_1120.py; the user's rule of 2026-11-08 that a page pick holds no talent that does nothing).
- 2026-11-20: filler points moved (2 points from Deflection to Unyielding Faith): the same DPS bit for bit in a full raid and on the training dummy. The new talents follow the utility order (interrupt protection, threat, mana, range, survival; dodge, parry and block count for nothing in a damage dealer's raid), which the simulator cannot measure (deep-runs/credited_fillers_1120.py; the user's rule of 2026-11-08 that a page pick holds no talent that does nothing).

## Open questions (verify in the live game)

- A machine-searched Prot-Ret build: check it against the community's Prot-Ret builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
