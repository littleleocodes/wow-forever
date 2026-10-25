# Frostfire — Fingers of Frost / Ice Lance (user build) — 0/29/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/29/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

A Frostfire Bolt build the user brought on 2026-10-06 (talentsforever.com link): 29 Fire points for Ignite, Heating Up, Pyroblast, Master of Elements, Critical Mass and Fire Power, 22 Frost points for Elemental Precision, Ice Shards, Piercing Ice, Frost Channeling, Shatter, Ice Lance and Fingers of Frost. In the Frostfire rotation in a full raid it beat the open search's 0/34/17 winner by 2.1% (698 against 684 DPS, 30,000 fights, seed 2), which that search had missed; an Ice Lance line on Fingers of Frost procs adds about 0.9% more.

## Point allocation

### Arcane (0)

*No points.*

### Fire (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Fire Blast** | 1/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec and increases its range by 8 yards. |
| **Improved Fireball** | 5/5 | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Flame Throwing** | 1/2 | unchanged | Increases the range of your Fire spells by 3 yards. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/5 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Improved Frostbolt** | 1/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.1 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Fingers of Frost** — Frostfire Bolt chills, so its procs let Ice Lance and Shatter crit; the 22 Frost points exist for this.
2. **Shatter** — Crit against frozen targets for Frostfire Bolt, Ice Lance and the Fire spells alike.
3. **Ignite** — The Fire half: crits burn for 40% more.
4. **Heating Up** — Instant Pyroblasts off crit streaks.
5. **Master of Elements** — Mana back from crits; the build has no Arcane mana talents.

## Rank among our builds and the community simulator's

**5 of 5** for `frostfire-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frostfire-raid`](frostfire-raid.md) | ours: hand draft | 5/33/13 | 516 | +0.0% | 743 | -7.4% | 52 s |
| 2 | [`frostfire-ml-raid`](frostfire-ml-raid.md) | ours: derived (ML search) | 6/32/13 | 489 | -5.2% | 760 | -5.3% | 62 s |
| 3 | [`frostfire-open-raid`](frostfire-open-raid.md) | ours: derived (open search) | 0/29/22 | 470 | -8.9% | 802 | +0.0% | 64 s |
| 4 | *FFB* | community simulator | - | 464 | -10.1% | 792 | -1.3% | 67 s |
| 5 | **[`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md)** | ours: hand draft | 0/29/22 | 464 | -10.1% | 764 | -4.8% | 58 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 10 passes, the last 2026-10-24, 18 changes to the base rotation; third-seed check: open winner 496 -> 469 DPS (-5.4%), frostfire-raid 506 -> 515 DPS (+1.8%), sim preset: FFB 485 -> 463 DPS (-4.5%), frostfire-ml-raid 477 -> 488 DPS (+2.3%), frostfire-fingers-of-frost-raid 494 -> 463 DPS (-6.3%)):
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
  17. spell probe: insert in the middle: cast Arcane Blast (+1.8%, pass 9)
  18. spell probe: insert at the top: cast Arcane Power (+1.2%, pass 9)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 15 passes, the last 2026-10-24, 27 changes to the base rotation; third-seed check: open winner 779 -> 801 DPS (+2.8%), frostfire-fingers-of-frost-raid 749 -> 763 DPS (+1.9%), sim preset: FFB 766 -> 794 DPS (+3.7%), frostfire-raid 726 -> 743 DPS (+2.4%), frostfire-ml-raid 732 -> 758 DPS (+3.5%)):
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
  21. rank 2 below 30% mana, above: if mana % ≥ 10%: cast Frostfire Bolt (+1.4%, pass 12)
  22. drop 'mana % ≥ 10%' from the condition: if mana % ≥ 10% and mana % < 30%: cast Frostfire Bolt (+0.9%, pass 12)
  23. spell probe: insert at the top: cast Arcane Power (+0.3%, pass 13)
  24. drop: if Fingers of Frost is up: cast Ice Lance (+217.8%, pass 14)
  25. insert at the top: cast Demonic Rune (+0.4%, pass 14)
  26. insert before the filler: cast Robe of the Archmage (+0.3%, pass 14)
  27. threshold 15s -> 7.5s: if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 15s): cast Scorch (+0.4%, pass 15)

| # | Priority (the first line whose condition holds is cast) | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) casts/min |
|---|---|---|
| 1 | if (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 5s): cast Scorch | 6.0 |
| 2 | cast Fire Blast | 5.0 |
| 3 | if Fire Vulnerability is known and (stacks of Fire Vulnerability < 5 or time left on Fire Vulnerability ≤ 6s) and time left in the fight ≥ 20s: cast Scorch | 6.0 |
| 4 | if mana % ≤ 80%: cast Mana Ruby | as ready |
| 5 | use every other cooldown when ready | as ready |
| 6 | if mana % < 10% and time left in the fight > 25s: cast Evocation | 0.3 |
| 7 | if stacks of Heating Up = 2: cast Pyroblast | 3.0 |
| 8 | if stacks of Heating Up = 3: cast Pyroblast | 3.0 |
| 9 | cast Mana Citrine | as ready |
| 10 | if mana % ≥ 10% and time left in the fight ≥ 6s and mana % ≥ 25%: cast Frostfire Bolt | 5.5 |
| 11 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 1.4 |
| 12 | if time left in the fight ≥ 3s: cast Fireball (rank 11) | 0.4 |
| 13 | cast Robe of the Archmage | as ready |
| 14 | cast Scorch | 6.0 |

Lines of the simulator's rotation these builds never cast: cast Arcane Power (needs the Arcane Power talent); cast Berserking (its condition never held in these fights); cast Arcane Blast (needs the Arcane Blast talent); cast Combustion (needs the Combustion talent).

Damage by ability:

| Ability | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) |
|---|---|
| Frostfire Bolt | 25% |
| Pyroblast | 25% |
| Fire Blast | 17% |
| Scorch | 12% |
| Ignite | 10% |
| Arcane Missiles | 8% |
| Fireball | 2% |
| Demonic Rune | 0% |

## Notes

- Added 2026-10-06 from the user's link; the open talent search of the same day found 0/34/17 at 684 DPS in the Frostfire rotation and missed this build (698): recorded in raidsim/known-positives.json so later searches start from it.
- Alone on a training dummy (own buffs only) it is 2% behind the 0/34/17 build; in a full raid 2% ahead. Simulator numbers are the community's model of the beta (ElliotWood/Forever b0f0df3 with this project's patches), not in-game measurements.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Hybrid Fire/Frost: its full-raid winner is +0.07% against it, under the 0.5% bar for a new build.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 0/29/22 -> 0/29/22; Fire Power 4 -> 3 (rank cap); refill +1 Improved Fire Blast (refill: the fire-raid model, raid-dps).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 0/29/22 -> 0/29/22; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; +1 Frost Warding (tier gating for Ice Shards); +1 Frost Warding (tier gating for Ice Shards); +1 Improved Frostbolt (tier gating for Shatter); +1 Ice Block (tier gating for Fingers of Frost); +1 Arctic Reach (tier gating for Fingers of Frost) (refill: the fire-raid model, raid-dps).

## Open questions (verify in the live game)

- Does Frostfire Bolt's chill proc Fingers of Frost in the live game as the simulator assumes?

## Sources

- <https://talentsforever.com/mage/60/-0355100013013304-00550003310003002-TUV4WaVbdeflmqrswzh-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
