# Frostfire — Fingers of Frost / Ice Lance (user build) — 0/29/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/29/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

A Frostfire Bolt build the user brought on 2026-10-06 (talentsforever.com link): 29 Fire points for Ignite, Heating Up, Pyroblast, Master of Elements, Critical Mass and Fire Power, 22 Frost points for Elemental Precision, Ice Shards, Piercing Ice, Frost Channeling, Shatter, Ice Lance and Fingers of Frost. In the Frostfire rotation in a full raid it beat the open search's 0/34/17 winner by 2.1% (698 against 684 DPS, 30,000 fights, seed 2), which that search had missed; an Ice Lance line on Fingers of Frost procs adds about 0.9% more.

## Point allocation

### Arcane (0)

*No points.*

### Fire (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 1/2 | unchanged | Increases the range of your Fire spells by 3 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 4/5 | unchanged | Increases the damage done by your Fire spells by 8%. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Fingers of Frost** — Frostfire Bolt chills, so its procs let Ice Lance and Shatter crit; the 22 Frost points exist for this.
2. **Shatter** — Crit against frozen targets for Frostfire Bolt, Ice Lance and the Fire spells alike.
3. **Ignite** — The Fire half: crits burn for 40% more.
4. **Heating Up** — Instant Pyroblasts off crit streaks.
5. **Master of Elements** — Mana back from crits; the build has no Arcane mana talents.

## Rank among our builds and the community simulator's

**2 of 3** for `frostfire-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frostfire-raid`](frostfire-raid.md) | ours: hand draft | 4/31/16 | 476 | +0.0% | 628 | -5.4% | 0 s |
| 2 | **[`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md)** | ours: hand draft | 0/29/22 | 476 | -0.0% | 665 | +0.0% | 0 s |
| 3 | [`frostfire-ml-raid`](frostfire-ml-raid.md) | ours: hand draft | 4/31/16 | 439 | -7.7% | 592 | -10.9% | 1 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-09, 20 changes to the base rotation; third-seed check: frostfire-open-raid 671 -> 637 DPS (-5.1%), frostfire-raid 613 -> 629 DPS (+2.5%), frostfire-ml-raid 623 -> 593 DPS (-4.8%), frostfire-fingers-of-frost-raid 678 -> 664 DPS (-2.1%)):
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

| # | Priority (the first line whose condition holds is cast) | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch | 4.2 |
| 2 | cast Fire Blast | 6.4 |
| 3 | cast Berserking | 0.3 |
| 4 | if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s) and time left in the fight ≥ 20s: cast Scorch | 4.2 |
| 5 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 6 | use every other cooldown when ready | as ready |
| 7 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 8 | if stacks of Heating Up = 2: cast Pyroblast | 2.6 |
| 9 | if stacks of Heating Up = 3: cast Pyroblast | 2.6 |
| 10 | cast Mana Citrine | as ready |
| 11 | if mana % ≥ 10% and time left in the fight ≥ 6s and mana % ≥ 25%: cast Frostfire Bolt | 8.5 |
| 12 | if time left in the fight ≥ 3s: cast Fireball | 8.6 |
| 13 | cast Robe of the Archmage | as ready |
| 14 | cast Scorch | 0.2 |

Lines of the simulator's rotation these builds never cast: cast Combustion (needs the Combustion talent); cast Arcane Missiles (its condition never held in these fights).

Damage by ability:

| Ability | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) |
|---|---|
| Frostfire Bolt | 35% |
| Fire Blast | 21% |
| Pyroblast | 20% |
| Ignite | 12% |
| Scorch | 8% |
| Fireball | 3% |

## Notes

- Added 2026-10-06 from the user's link; the open talent search of the same day found 0/34/17 at 684 DPS in the Frostfire rotation and missed this build (698): recorded in raidsim/known-positives.json so later searches start from it.
- Alone on a training dummy (own buffs only) it is 2% behind the 0/34/17 build; in a full raid 2% ahead. Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.

## Open questions (verify in the live game)

- Does Frostfire Bolt's chill proc Fingers of Frost in the live game as the simulator assumes?

## Sources

- <https://talentsforever.com/mage/60/-0355100013013304-00550003310003002-TUV4WaVbdeflmqrswzh-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
