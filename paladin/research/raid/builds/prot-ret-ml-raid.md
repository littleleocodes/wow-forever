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
| **Redoubt** | 5/5 | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |
| **Precision** | 2/3 | changed | Improves your chance to hit by 2%. |

### Retribution (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 3/5 | moved | Increases your Parry chance by 3%. |
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

## Rank among our builds and the community simulator's

**6 of 8** for `ret-dps` by training-dummy DPS in the community simulator (wowsims/forever ff9babb (client 70888)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Unsealed Wrath* | community simulator | - | 504 | +0.0% | 815 | -0.3% | 13 s |
| 2 | [`retribution-open-raid`](retribution-open-raid.md) | ours: derived (open search) | 16/4/31 | 477 | -5.4% | 817 | +0.0% | 33 s |
| 3 | *Holy Shock* | community simulator | - | 460 | -8.7% | 709 | -13.3% | 0 s |
| 4 | [`ret-raid-dps`](ret-raid-dps.md) | ours: hand draft | 17/6/28 | 422 | -16.3% | 654 | -20.0% | 0 s |
| 5 | [`opt-ret-dps-raid-dps`](opt-ret-dps-raid-dps.md) | ours: optimizer | 17/6/28 | 422 | -16.3% | 654 | -20.0% | 0 s |
| 6 | **[`prot-ret-ml-raid`](prot-ret-ml-raid.md)** | ours: derived (ML search) | 10/12/29 | 403 | -20.2% | 682 | -16.5% | 8 s |
| 7 | [`retribution-ml-raid`](retribution-ml-raid.md) | ours: derived (ML search) | 9/14/28 | 389 | -22.9% | 652 | -20.2% | 8 s |
| 8 | [`ret-full-buffs-raid`](ret-full-buffs-raid.md) | ours: hand draft | 8/15/28 | 387 | -23.2% | 652 | -20.2% | 8 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-11-13, 1 changes to the base rotation; third-seed check: ):
  1. spell probe: insert at the end: cast Divine Favor (+0.2%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-31, 5 passes, the last 2026-11-10, 1 changes to the base rotation; third-seed check: retribution-open-raid 867 -> 876 DPS (+1.0%), sim preset: Unsealed Wrath 865 -> 875 DPS (+1.1%), ret-raid-dps 691 -> 702 DPS (+1.7%), ret-full-buffs-raid 690 -> 700 DPS (+1.6%), opt-ret-dps-raid-dps 691 -> 702 DPS (+1.7%), retribution-ml-raid 689 -> 701 DPS (+1.7%)):
  1. insert in the middle: cast Consecration (+1.2%, pass 1)

Before the pull: at -20s: groupReference; at -20s: move to “Pull range” yd; at -3s: groupReference; at -1.5s: groupReference; at -1.5s: groupReference.

| # | Priority (the first line whose condition holds is cast) | [`prot-ret-ml-raid`](prot-ret-ml-raid.md) casts/min |
|---|---|---|
| 1 | if not spellInRange: groupReference | as ready |
| 2 | if “WF guard”: cast Judgement | 7.4 |
| 3 | if time into the fight ≥ “Delay Major CDs”: use every other cooldown when ready | as ready |
| 4 | if (cast time of Hammer of Wrath = 0s or autoTimeSinceLast < 0.2s): cast Hammer of Wrath | 0.7 |
| 5 | if “WF guard” and not Judgement is ready and “Judge realism protection”: cast Holy Strike | 5.9 |
| 6 | if “Should refresh SoC”: cast Seal of Command | 2.2 |
| 7 | groupReference | as ready |
| 8 | groupReference | as ready |

Lines of the simulator's rotation these builds never cast: cast Seal of Righteousness (its condition never held in these fights); cast Divine Favor (needs the Divine Favor talent).

Damage by ability:

| Ability | [`prot-ret-ml-raid`](prot-ret-ml-raid.md) |
|---|---|
| Auto Attack | 24% |
| Judgement of Command | 21% |
| Seal of Command | 19% |
| Holy Strike | 17% |
| Consecration | 14% |
| Hammer of Wrath | 3% |
| Demonic Rune | 2% |

## Notes

- Against the best hand draft ret-full-buffs-raid in a full raid, same gear and fights (100,000, one seed): +3.5% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow ret-full-buffs-raid: Pursuit of Justice → Deflection, Guardian's Favor → Redoubt (2 points), Templar's Bulwark → Redoubt (within 0.00% of the search winner 10/12/29 on one seed, 30,000 fights).
- Search result (full raid): 10/12/29 at 682.0 ± 0.13 DPS over 100,000 fights; runner-up 10/12/29 (+0.00%; the winner takes Templar's Bulwark 1, Vindication 3; the runner-up Deflection 1, Sacred Duty 1, Vindication 2); 1,616 builds simulated; certificate: none of its 216 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever ff9babb (client 70888) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 10/12/29 at 676.9 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 13/14/24 at 410.2 DPS.
- 2026-11-13 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Vindication -> Deflection (survival); Vindication -> Deflection (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- A machine-searched Prot-Ret build: check it against the community's Prot-Ret builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
