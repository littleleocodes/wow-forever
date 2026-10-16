# Survival — Full raid (parse) (machine-learning search) — 5/14/32

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/14/32 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival build the machine-learning talent search found in a full raid (every raid buff and debuff) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry melee-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |
| **Efficiency** | 3/5 | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 9%. |

### Survival (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | unchanged | Increases your Parry chance by 5%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Survival Tactics** | 1/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 10 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 10%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec |

## Rank among our builds and the community simulator's

**5 of 5** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: derived (simulator search) | 5/16/30 | 488 | +0.0% | 987 | -2.9% | 9 s |
| 2 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 466 | -4.5% | 1007 | -1.0% | 44 s |
| 3 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 465 | -4.8% | 975 | -4.1% | 8 s |
| 4 | [`beast-survival-open-raid`](beast-survival-open-raid.md) | ours: derived (open search) | 16/11/24 | 360 | -26.3% | 1017 | +0.0% | 127 s |
| 5 | **[`survival-ml-parse`](survival-ml-parse.md)** | ours: derived (ML search) | 5/14/32 | 360 | -26.3% | 959 | -5.7% | 117 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 8 passes, the last 2026-10-05, 9 changes to the base rotation; third-seed check: open winner 298 -> 363 DPS (+21.9%), survival-raid 313 -> 445 DPS (+42.1%), melee-survival-raid 319 -> 423 DPS (+32.5%), opt-melee-dps-raid-dps 319 -> 426 DPS (+33.2%)):
  1. insert before the filler: cast Wing Clip (+7.4%, pass 1)
  2. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+14.3%, pass 2)
  3. insert in the middle: cast Major Mana Potion (+0.4%, pass 3)
  4. move to the top: cast Immolation Trap (+0.5%, pass 3)
  5. move to the top: cast Raptor Strike (+0.3%, pass 3)
  6. move down below 'cast Strider Kick': cast Major Mana Potion (+0.4%, pass 4)
  7. move to the top: cast Mongoose Bite (+0.2%, pass 4)
  8. move to the top: cast Aspect of the Beast (+0.2%, pass 4)
  9. move to the top: if auraIsInactive: cast Summon Hawk (+0.3%, pass 7)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 10 passes, the last 2026-10-09, 4 changes to the base rotation; third-seed check: beast-survival-open-raid 736 -> 1057 DPS (+43.6%), melee-survival-raid 764 -> 1048 DPS (+37.1%), opt-melee-dps-raid-dps 764 -> 1017 DPS (+33.1%), survival-raid 749 -> 1028 DPS (+37.3%), survival-ml-parse 729 -> 999 DPS (+37.1%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)
  3. move down below 'cast Strider Kick': if auraIsInactive: cast Summon Hawk (+0.3%, pass 10)
  4. move to the top: cast Raptor Strike (+0.3%, pass 10)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`survival-ml-parse`](survival-ml-parse.md) casts/min |
|---|---|---|
| 1 | cast Aspect of the Beast | 0.3 |
| 2 | cast Mongoose Bite | 8.2 |
| 3 | cast Raptor Strike | 13.5 |
| 4 | cast Immolation Trap | 1.7 |
| 5 | use every other cooldown when ready | as ready |
| 6 | cast Strider Kick | 2.8 |
| 7 | cast Major Mana Potion | as ready |
| 8 | cast Wing Clip | 9.6 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Counterattack (needs the Counterattack talent); cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`survival-ml-parse`](survival-ml-parse.md) |
|---|---|
| Auto Attack | 55% |
| Raptor Strike | 14% |
| Mongoose Bite | 12% |
| Immolation Trap | 9% |
| Strider Kick | 4% |
| Wing Clip | 3% |
| Dragonbreath Chili | 3% |

## Notes

- In a full raid it does +2.3% over the training-dummy winner (990.2 vs 967.7 DPS, 100,000 fights, one seed, BiS gear).
- Search result: 5/11/35 at 990.3 ± 0.15 DPS over 100,000 fights; runner-up 5/11/35 (+0.00%; the winner takes Counterattack 1, Deflection 5, Deterrence 1, Survivalist 3; the runner-up Entrapment 5, Improved Tracking 5); 1,559 builds simulated; certificate: the neighbours ahead on the short run (of 340) did not hold on the longer one.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Counterattack, Deterrence was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Counterattack -> Efficiency (mana); Deterrence -> Efficiency (mana); Survival Tactics -> Efficiency (mana). Net -0.00% on a third seed.

## Open questions (verify in the live game)

- A machine-searched Survival build: check it against the community's Survival builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
