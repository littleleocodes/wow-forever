# Frostfire — Raid (open talent search) — 3/32/16

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 3/32/16 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire (a Fire/Frost hybrid) raid build the open talent search found on 2026-10-06: every legal 51-point build with no tree rule, searched in the community simulator's frostfire-raid rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +5.6% over frostfire-raid, the best of our builds in that rotation.

## Point allocation

### Arcane (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 3/5 | **NEW** | Gives you a 60% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 42% chance while casting Arcane Blast. |

### Fire (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wake of Fire** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 50%. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
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

## Core talents (priority order)

1. **Ignite** — 94 DPS lost without it (14% of the build in a full raid; removal, 12,000 fights).
2. **Improved Scorch** — 85 DPS lost without it (12% of the build in a full raid; removal, 12,000 fights).
3. **Fire Power** — 60 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
4. **Critical Mass** — 53 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
5. **Pyroblast** — 49 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
6. **Heating Up** — 49 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
7. **Ice Shards** — 46 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
8. **Improved Fireball** — 41 DPS lost without it (6% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**1 of 4** for `frostfire-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever b0f0df3); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`frostfire-open-raid`](frostfire-open-raid.md)** | ours: hand draft | 3/32/16 | 551 | +0.0% | 691 | -2.3% | 1 s |
| 2 | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) | ours: hand draft | 0/29/22 | 539 | -2.1% | 707 | +0.0% | 0 s |
| 3 | [`frostfire-raid`](frostfire-raid.md) | ours: hand draft | 4/31/16 | 516 | -6.3% | 648 | -8.4% | 0 s |
| 4 | [`frostfire-ml-raid`](frostfire-ml-raid.md) | ours: hand draft | 4/31/16 | 513 | -6.9% | 644 | -9.0% | 1 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-06, 16 changes to the base rotation; third-seed check: open winner 533 -> 540 DPS (+1.4%), frostfire-open-raid 527 -> 550 DPS (+4.4%), frostfire-raid 514 -> 514 DPS (+0.0%), frostfire-ml-raid 482 -> 513 DPS (+6.4%), frostfire-fingers-of-frost-raid 535 -> 539 DPS (+0.8%)):
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
  14. only above 25% mana: if mana % ≥ 10% and time left in the fight ≥ 6s: cast Frostfire Bolt (+0.7%, pass 5)
  15. move to the top: cast Fire Blast (+3.8%, pass 5)
  16. insert at the top: if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch (+0.5%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-06, 20 changes to the base rotation; third-seed check: open winner 687 -> 705 DPS (+2.7%), frostfire-open-raid 679 -> 692 DPS (+1.9%), frostfire-raid 625 -> 648 DPS (+3.7%), frostfire-ml-raid 630 -> 646 DPS (+2.5%), frostfire-fingers-of-frost-raid 686 -> 707 DPS (+3.0%)):
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
  11. drop the condition: if mana ≥ (time left in the fight × 330): cast Fire Blast (+4.9%, pass 6)
  12. threshold 25s -> 50s: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.6%, pass 6)
  13. drop: if stacks of Heating Up = 2: cast Pyroblast (+0.3%, pass 6)
  14. drop: cast Berserking (+0.3%, pass 6)
  15. move down below 'if mana % ≥ 10%: cast Frostfire Bolt': if mana % < 20% and time left in the fight > 50s: cast Evocation (+0.2%, pass 6)
  16. move to the top: if stacks of Heating Up = 3: cast Pyroblast (+0.2%, pass 6)
  17. insert at the top: if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 8)
  18. threshold 7.5s -> 15s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 7.5s): cast Scorch + insert before the filler: cast Fireball (+0.2%, pass 8)
  19. drop: if mana % < 20% and time left in the fight > 50s: cast Evocation (+0.4%, pass 8)
  20. insert in the middle: cast Mana Citrine (+0.2%, pass 8)

| # | Priority (the first line whose condition holds is cast) | [`frostfire-open-raid`](frostfire-open-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch | 4.5 |
| 2 | cast Fire Blast | 8.1 |
| 3 | cast Berserking | 0.3 |
| 4 | if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s) and time left in the fight ≥ 20s: cast Scorch | 4.5 |
| 5 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 6 | use every other cooldown when ready | as ready |
| 7 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 8 | if stacks of Heating Up = 2: cast Pyroblast | 2.6 |
| 9 | if stacks of Heating Up = 3: cast Pyroblast | 2.6 |
| 10 | cast Combustion | 0.3 |
| 11 | cast Mana Citrine | as ready |
| 12 | if mana % ≥ 10% and time left in the fight ≥ 6s and mana % ≥ 25%: cast Frostfire Bolt | 6.8 |
| 13 | if time left in the fight ≥ 3s: cast Fireball | 9.5 |
| 14 | cast Robe of the Archmage | as ready |
| 15 | cast Scorch | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Arcane Missiles (its condition never held in these fights).

Damage by ability:

| Ability | [`frostfire-open-raid`](frostfire-open-raid.md) |
|---|---|
| Frostfire Bolt | 25% |
| Fire Blast | 23% |
| Pyroblast | 17% |
| Fireball | 15% |
| Ignite | 12% |
| Scorch | 8% |

## Notes

- +5.6% over the best hand draft of the spec, frostfire-raid, over the 2% replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (frostfire-raid, full raid): 0/34/17 (Frostfire (a Fire/Frost hybrid)) at 683.9 DPS; frostfire-raid 647.6, frostfire-ml-raid 636.4 in the same fights; 4,515 builds simulated, 2 independent runs reached the top.
- The frostfire-raid raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): frost-raid -33.0%, fire-raid -0.4%, arcane-dps -73.4%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Fire Ward, Improved Frostbolt.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.
- 2026-10-06 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Fire Ward -> Improved Channeling (interrupt); Improved Fire Ward -> Improved Channeling (interrupt); Improved Frostbolt -> Improved Channeling (interrupt). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Frostfire build: check it against the community's Frostfire builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/mage/60/-23550000132133051-015500033-4>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
