# Survival — Full raid (parse) (machine-learning search) — 5/11/35

*[Hunter](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/11/35 (Beast Mastery / Marksmanship / Survival) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Survival build the machine-learning talent search found in a full raid (every raid buff and debuff) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry melee-dps (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Beast Mastery (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deadly Aspects** | 5/5 | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |

### Marksmanship (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Lethal Attacks** | 5/5 | **NEW** | Increases your critical strike chance with all attacks by 5%. |
| **Careful Aim** | 5/5 | **NEW** | Increases your Attack Power by 100% of your Intellect. |
| **Lone Wolf** | 1/1 | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. |

### Survival (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Deflection** | 5/5 | changed | Increases your Parry chance by 10%. |
| **Savage Strikes** | 2/2 | changed | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 3/5 | changed | Increases your total Health by 6%. |
| **Clever Traps** | 2/2 | unchanged | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3/3 | changed | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1/1 | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. |
| **Survival Tactics** | 2/2 | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Predator's Edge** | 5/5 | **NEW** | Increases your melee critical strike damage by 30% and your offhand weapon damage by 50%. |
| **Counterattack** | 1/1 | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. |
| **Expose Prey** | 2/2 | **NEW** | Your attacks against targets with Hunter's Mark have a 10% chance to activate your Mongoose Bite for 5 sec. |
| **Survivalist's Discipline** | 2/2 | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1/1 | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. |
| **Lightning Reflexes** | 5/5 | changed | Increases your Agility by 15%. |
| **Lacerating Strikes** | 1/1 | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage over 21 sec equal to 40% of the damage done by Mongoose Bite. |

## Rank among our builds and the community simulator's

**4 of 4** for `melee-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`survival-raid`](survival-raid.md) | ours: hand draft | 5/16/30 | 450 | +0.0% | 967 | -2.4% | 12 s |
| 2 | [`opt-melee-dps-raid-dps`](opt-melee-dps-raid-dps.md) | ours: optimizer | 5/15/31 | 430 | -4.5% | 965 | -2.6% | 9 s |
| 3 | [`melee-survival-raid`](melee-survival-raid.md) | ours: hand draft | 5/11/35 | 426 | -5.3% | 991 | -0.0% | 47 s |
| 4 | **[`survival-ml-parse`](survival-ml-parse.md)** | ours: parse build | 5/11/35 | 336 | -25.3% | 991 | +0.0% | 124 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 3 passes, the last 2026-10-02, 5 changes to the base rotation; third-seed check: ml: Survival 318 -> 449 DPS (+41.5%)):
  1. insert before the filler: cast Wing Clip (+7.4%, pass 1)
  2. spell probe: insert at the top: if auraIsInactive: cast Summon Hawk (+14.3%, pass 2)
  3. insert in the middle: cast Major Mana Potion (+0.4%, pass 3)
  4. move to the top: cast Immolation Trap (+0.5%, pass 3)
  5. move to the top: cast Raptor Strike (+0.3%, pass 3)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-29, 3 passes, the last 2026-10-02, 2 changes to the base rotation; third-seed check: ml: Survival 713 -> 968 DPS (+35.9%)):
  1. insert before the filler: cast Wing Clip (+10.3%, pass 1)
  2. spell probe: insert in the middle: if auraIsInactive: cast Summon Hawk (+15.0%, pass 2)

Before the pull: at -3s: cast Hunter's Mark.

| # | Priority (the first line whose condition holds is cast) | [`survival-ml-parse`](survival-ml-parse.md) casts/min |
|---|---|---|
| 1 | cast Raptor Strike | 12.5 |
| 2 | cast Immolation Trap | 1.7 |
| 3 | cast Aspect of the Beast | 0.3 |
| 4 | use every other cooldown when ready | as ready |
| 5 | cast Mongoose Bite | 6.8 |
| 6 | cast Major Mana Potion | as ready |
| 7 | cast Strider Kick | 2.6 |
| 8 | cast Wing Clip | 9.2 |

Lines of the simulator's rotation these builds never cast: cast Summon Hawk (needs the Summon Hawk talent); cast Counterattack, cast Explosive Trap (its condition never held in these fights).

Damage by ability:

| Ability | [`survival-ml-parse`](survival-ml-parse.md) |
|---|---|
| Auto Attack | 57% |
| Raptor Strike | 13% |
| Mongoose Bite | 11% |
| Immolation Trap | 8% |
| Strider Kick | 4% |
| Dragonbreath Chili | 3% |
| Wing Clip | 3% |

## Notes

- In a full raid it does +2.3% over the training-dummy winner (990.2 vs 967.7 DPS, 100,000 fights, one seed, BiS gear).
- Search result: 5/11/35 at 990.3 ± 0.15 DPS over 100,000 fights; runner-up 5/11/35 (+0.00%; the winner takes Counterattack 1, Deflection 5, Deterrence 1, Survivalist 3; the runner-up Entrapment 5, Improved Tracking 5); 1,559 builds simulated; certificate: the neighbours ahead on the short run (of 340) did not hold on the longer one.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.

## Open questions (verify in the live game)

- A machine-searched Survival build: check it against the community's Survival builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
