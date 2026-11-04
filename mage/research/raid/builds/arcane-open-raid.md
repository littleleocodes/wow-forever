# Arcane — Raid (open talent search) — 31/17/3

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/17/3 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Arcane raid build the open talent search found on 2026-11-03: every legal 51-point build with no tree rule, searched in the community simulator's arcane-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +2.9% over arcane-open-raid, the best of our builds in that rotation.

## Point allocation

### Arcane (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 2/5 | **NEW** | Gives your Arcane Missiles spell a 40% chance and your Arcane Blast and Arcane Wrath spells a 28% chance to not lose casting time when you take damage. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Meditation** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Ignite** | 4/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 32% of your spell's damage over 4 sec. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Improved Fire Blast** | 1/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec and increases its range by 8 yards. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |

### Frost (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |

## Core talents (priority order)

1. **Missile Barrage** — 178 DPS lost without it (24% of the build in a full raid; removal, 12,000 fights).
2. **Arcane Mind** — 78 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
3. **Arcane Blast** — 63 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
4. **Arcane Wrath** — 54 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
5. **Precision** — 53 DPS lost without it (7% of the build in a full raid; removal, 12,000 fights).
6. **Arcane Instability** — 39 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
7. **Accelerant** — 37 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
8. **Arcane Impact** — 28 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**2 of 3** for `arcane-dps` by training-dummy DPS in the community simulator (wowsims/forever 5ad0894 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Arcane Fire* | community simulator | - | 554 | +0.0% | 742 | -1.8% | 6 s |
| 2 | **[`arcane-open-raid`](arcane-open-raid.md)** | ours: derived (open search) | 31/17/3 | 552 | -0.3% | 756 | +0.0% | 10 s |
| 3 | [`arcane-blast-raid`](arcane-blast-raid.md) | ours: hand draft | 31/13/7 | 536 | -3.2% | 683 | -9.7% | 8 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 6 passes, the last 2026-10-24, 14 changes to the base rotation; third-seed check: open winner 519 -> 562 DPS (+8.3%), arcane-blast-raid 524 -> 539 DPS (+2.9%), sim preset: Arcane Frost 546 -> 565 DPS (+3.5%)):
  1. threshold 3 -> 1.5: if (stacks of Arcane Blast ≥ 3 or mana % < 40%): cast Frostbolt (+2.2%, pass 1)
  2. drop 'mana % < 40%' from the condition: if (stacks of Arcane Blast ≥ 1.5 or mana % < 40%): cast Frostbolt (+0.4%, pass 1)
  3. insert at the top: if mana ≥ (time left in the fight × 110): cast Fire Blast + threshold 110 -> 220: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  4. drop the condition: if mana ≥ (time left in the fight × 220): cast Fire Blast (+2.9%, pass 2)
  5. move down below 'use every other cooldown when ready': cast Fire Blast (+0.4%, pass 2)
  6. drop: if mana % < 15% and time left in the fight > 20s: cast Evocation (+0.9%, pass 5)
  7. insert at the end: cast Fireball (+0.6%, pass 5)
  8. insert in the middle: cast Arcane Wrath (+4.8%, pass 6)
  9. insert in the middle: if Arcane Blast is up and time left on Arcane Blast < cast time of Arcane Blast: cast Arcane Blast (+1.0%, pass 6)
  10. insert at the end: cast Frost Blast (+0.9%, pass 6)
  11. insert before the filler: cast Robe of the Archmage (+0.5%, pass 6)
  12. move down below 'if Missile Barrage is up: cast Arcane Missiles (rank 7)': cast Fire Blast (+0.2%, pass 6)
  13. only with 10s or more of the fight left: if stacks of Arcane Blast ≥ 1.5: cast Frostbolt (rank 10) (+0.2%, pass 6)
  14. insert before the filler: cast Mana Citrine (+0.3%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 13 passes, the last 2026-11-03, 29 changes to the base rotation; third-seed check: arcane-open-raid 734 -> 755 DPS (+2.8%), sim preset: Arcane Fire 722 -> 742 DPS (+2.7%), arcane-blast-raid 613 -> 682 DPS (+11.3%)):
  1. threshold 3 -> 1.5: if (stacks of Arcane Blast ≥ 3 or mana % < 40%): cast Frostbolt (+0.2%, pass 1)
  2. insert in the middle: if mana ≥ (time left in the fight × 110): cast Fire Blast (+2.3%, pass 2)
  3. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+2.4%, pass 2)
  4. move down below 'if Missile Barrage is up: cast Arcane Missiles': cast Fire Blast (+3.3%, pass 6)
  5. drop: if (stacks of Arcane Blast ≥ 1.5 or mana % < 40%): cast Frostbolt (+0.3%, pass 6)
  6. only with 20s or more of the fight left: cast Fire Blast (+0.2%, pass 6)
  7. threshold 20s -> 40s: if time left in the fight ≥ 20s: cast Fire Blast (+0.2%, pass 6)
  8. insert at the end: if stacks of Arcane Blast ≥ 2: cast Fire Blast (+0.2%, pass 6)
  9. only with 3s or more of the fight left: cast Arcane Blast (+0.2%, pass 6)
  10. drop the condition: if stacks of Arcane Blast ≥ 2: cast Fire Blast (+0.3%, pass 6)
  11. insert at the end: cast Fireball (rank 11) (+207.8%, pass 8)
  12. insert before the filler: cast Arcane Wrath (+7.4%, pass 8)
  13. insert at the end: cast Mana Citrine (+0.2%, pass 8)
  14. move to the top: cast Arcane Wrath (+8.9%, pass 9)
  15. insert in the middle: if (auraIsInactive or time left on Arcane Blast < cast time of Arcane Blast): cast Arcane Blast (+1.5%, pass 9)
  16. move to the top: if Missile Barrage is up: cast Arcane Missiles (rank 7) (+1.1%, pass 9)
  17. move to the top: use every other cooldown when ready (+1.4%, pass 9)
  18. insert before the filler: cast Frost Blast (+0.4%, pass 9)
  19. only with 10s or more of the fight left: cast Arcane Wrath (+0.3%, pass 9)
  20. threshold 20s -> 40s: if mana % < 15% and time left in the fight > 20s: cast Evocation (+0.2%, pass 9)
  21. threshold 40s -> 80s: if mana % < 15% and time left in the fight > 40s: cast Evocation (+0.3%, pass 9)
  22. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+0.2%, pass 9)
  23. only above 25% mana: if time left in the fight ≥ 3s: cast Arcane Blast (+0.2%, pass 9)
  24. drop: if mana % < 15% and time left in the fight > 80s: cast Evocation (+3.8%, pass 10)
  25. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast ≤ 2) and not spellIsCasting: cast Arcane Blast (+0.2%, pass 11)
  26. drop 'stacks of Arcane Blast < 2' from the condition: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+0.5%, pass 11)
  27. insert in the middle: if stacks of Heating Up = 3 and not spellIsCasting: cast Pyroblast (+1.9%, pass 12)
  28. drop the condition: if time left in the fight ≥ 40s: cast Fire Blast (+0.5%, pass 13)
  29. drop: cast Mana Citrine (+0.2%, pass 13)

| # | Priority (the first line whose condition holds is cast) | [`arcane-open-raid`](arcane-open-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 3.6 |
| 3 | cast Fire Blast | 7.1 |
| 4 | if Arcane Blast is up and time left on Arcane Blast < cast time of Arcane Blast: cast Arcane Blast | 6.4 |
| 5 | cast Arcane Wrath | 5.1 |
| 6 | if stacks of Arcane Blast ≥ 1.5 and time left in the fight ≥ 10s: cast Frostbolt (rank 10) | 3.6 |
| 7 | cast Arcane Blast | 6.4 |
| 8 | cast Robe of the Archmage | as ready |
| 9 | cast Mana Citrine | as ready |

Lines of the simulator's rotation these builds never cast: cast Fireball (rank 11), cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`arcane-open-raid`](arcane-open-raid.md) |
|---|---|
| Arcane Wrath | 28% |
| Arcane Missiles | 25% |
| Fire Blast | 19% |
| Arcane Blast | 14% |
| Frostbolt | 12% |
| Ignite | 2% |
| Demonic Rune | 1% |
| Fireball | 0% |

## Notes

- +12.7% over the best hand draft of the spec, arcane-blast-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (arcane-dps, full raid): 31/17/3 (Arcane) at 741.8 DPS; arcane-open-raid 720.8, arcane-blast-raid 658.0 in the same fights; 2,385 builds simulated, 1 independent runs reached the top.
- The arcane-dps raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): frost-raid -12.3%, fire-raid -29.8%, frostfire-raid -35.0%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Improved Channeling, Arcane Resilience.
- Simulator numbers are the community's model of the beta (wowsims/forever 5ad0894 (client 70707) with this project's patches), not in-game measurements.
- 2026-11-03 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Channeling -> Arcane Resilience (survival); Improved Channeling -> Arcane Resilience (survival). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Arcane build: check it against the community's Arcane builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/mage/60/041205203100211531-554000011001-003-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
