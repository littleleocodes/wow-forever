# Frostfire — Raid (machine-learning search) — 4/31/16

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 4/31/16 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-03 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry frostfire-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Arcane (4)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 4/5 | **NEW** | Gives you a 80% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 56% chance while casting Arcane Blast. |

### Fire (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wake of Fire** | 1/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 25%. |
| **Improved Fireball** | 4/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.4 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 2/2 | unchanged | Increases the range of your Fire spells by 6 yards. |
| **Impact** | 1/3 | changed | Gives your Fire spells a 3% chance to stun the target for 2 sec. |
| **Burning Soul** | 3/3 | changed | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Flamestrike** | 1/3 | unchanged | Increases the critical strike chance of your Flamestrike spell by 5%. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 5/5 | unchanged | Increases the damage done by your Fire spells by 10%. |
| **Combustion** | 1/1 | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. |

### Frost (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |

## Rank among our builds and the community simulator's

**1 of 2** for `frostfire-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`frostfire-ml-raid`](frostfire-ml-raid.md)** | ours: hand draft | 4/31/16 | 499 | +0.0% | 614 | +0.0% | 2 s |
| 2 | [`frostfire-raid`](frostfire-raid.md) | ours: hand draft | 4/31/16 | 479 | -4.0% | 589 | -4.2% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 4 passes, the last 2026-10-02, 13 changes to the base rotation; third-seed check: ml: Hybrid Fire/Frost 557 -> 612 DPS (+10.0%), frostfire-raid 552 -> 616 DPS (+11.7%)):
  1. insert before the filler: cast Fireball (+0.7%, pass 1)
  2. threshold 20% -> 10%: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.5%, pass 1)
  3. only with 3s or more of the fight left: cast Fireball (+0.3%, pass 1)
  4. insert before the filler: cast Robe of the Archmage (+0.6%, pass 2)
  5. threshold 5s -> 6s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.4%, pass 2)
  6. insert at the top: cast Berserking (+0.2%, pass 2)
  7. move down below 'if mana % ≥ 10%: cast Frostfire Bolt': cast Fire Blast (+6.4%, pass 4)
  8. only with 6s or more of the fight left: if mana % ≥ 10%: cast Frostfire Bolt (+1.1%, pass 4)
  9. insert in the middle: cast Mana Citrine (+0.5%, pass 4)
  10. threshold 3 -> 2: if stacks of Hot Streak = 3: cast Pyroblast (+0.3%, pass 4)
  11. insert in the middle: if stacks of Hot Streak = 3: cast Pyroblast (+0.6%, pass 4)
  12. only with 20s or more of the fight left: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s): cast Scorch (+0.3%, pass 4)
  13. insert in the middle: cast Combustion (+0.3%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 10 changes to the base rotation; third-seed check: ml: Hybrid Fire/Frost 670 -> 727 DPS (+8.5%), frostfire-raid 664 -> 723 DPS (+8.9%)):
  1. insert at the top: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  2. threshold 110 -> 82.5: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  3. insert at the top: cast Berserking (+0.3%, pass 3)
  4. drop: cast Fire Blast (+2.5%, pass 5)
  5. threshold 5s -> 10s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+2.2%, pass 5)
  6. threshold 82.5 -> 165: if mana ≥ (time left in the fight × 82.5): cast Fire Blast (+1.6%, pass 5)
  7. threshold 10s -> 7.5s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 10s): cast Scorch (+1.0%, pass 5)
  8. threshold 165 -> 330: if mana ≥ (time left in the fight × 165): cast Fire Blast (+0.5%, pass 5)
  9. threshold 3 -> 2: if stacks of Hot Streak = 3: cast Pyroblast (+0.3%, pass 5)
  10. insert in the middle: if stacks of Hot Streak = 3: cast Pyroblast (+0.6%, pass 5)

| # | Priority (the first line whose condition holds is cast) | [`frostfire-ml-raid`](frostfire-ml-raid.md) casts/min |
|---|---|---|
| 1 | cast Berserking | 0.3 |
| 2 | if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s) and time left in the fight ≥ 20s: cast Scorch | 4.3 |
| 3 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 4 | use every other cooldown when ready | as ready |
| 5 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 6 | if stacks of Heating Up = 2: cast Pyroblast | 1.7 |
| 7 | if stacks of Heating Up = 3: cast Pyroblast | 1.7 |
| 8 | cast Combustion | 0.3 |
| 9 | cast Mana Citrine | as ready |
| 10 | if mana % ≥ 10% and time left in the fight ≥ 6s: cast Frostfire Bolt | 15.1 |
| 11 | cast Fire Blast | 1.0 |
| 12 | if time left in the fight ≥ 3s: cast Fireball | 3.0 |
| 13 | cast Robe of the Archmage | as ready |
| 14 | cast Scorch | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Arcane Missiles (its condition never held in these fights).

Damage by ability:

| Ability | [`frostfire-ml-raid`](frostfire-ml-raid.md) |
|---|---|
| Frostfire Bolt | 59% |
| Pyroblast | 13% |
| Ignite | 12% |
| Scorch | 8% |
| Fireball | 5% |
| Fire Blast | 3% |

## Notes

- Against the best hand draft frostfire-raid in a full raid, same gear and fights (100,000, one seed): +1.6% (under the 2% bar: the hand draft stays the pick).
- Where the simulator measured no difference, the points follow frostfire-raid: Improved Fireball → Burning Soul, Flame Throwing → Burning Soul, Impact → Burning Soul, Frostbite → Improved Channeling, Ice Lance → Improved Channeling, Arctic Reach → Improved Channeling (the same DPS as the search winner 1/31/19 on one seed, 30,000 fights).
- Search result (full raid): 1/31/19 at 739.6 ± 0.23 DPS over 100,000 fights; runner-up 3/31/17 (+0.00%; the winner takes Flame Throwing 2, Frostbite 1, Ice Lance 1, Impact 3, Improved Channeling 1, Improved Flamestrike 1; the runner-up Blast Wave 1, Burning Soul 1, Improved Channeling 3, Improved Fire Ward 2, Improved Flamestrike 2); 1,942 builds simulated; certificate: none of its 311 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 3/31/17 at 721.6 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 1/34/16 at 627.1 DPS.
- 2026-10-03 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Impact -> Flame Throwing (range). Net +0.00% on a third seed.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): Hot Streak 1 out; Heating Up 1 in; to be re-optimized.

## Open questions (verify in the live game)

- A machine-searched Frostfire build: check it against the community's Frostfire builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
