# Smite — Raid (open talent search) — 21/23/7

*[Priest](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/23/7 (Discipline / Holy / Shadow) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Smite (a Discipline/Holy hybrid) raid build the open talent search found on 2026-10-11: every legal 51-point build with no tree rule, searched in the community simulator's smite-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +0.6% over smite-discipline-raid, the best of our builds in that rotation.

## Point allocation

### Discipline (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Holy Precision** | 3/3 | **NEW** | Improves your chance to hit with Holy spells by 18%. |
| **Mental Agility** | 2/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 7%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Mental Strength** | 1/5 | changed | Increases your total Intellect by 3%. |
| **Penance** | 1/1 | **NEW** | Launches a volley of holy light at the target, causing 44 Holy damage to an enemy, or 133 healing to an ally, instantly and every 1 sec for 2 sec. |

### Holy (23)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Twilight Focus** | 3/3 | **NEW** | Gives you a 70% chance to avoid interruption caused by damage while casting any spell. |
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Spell Warding** | 1/5 | unchanged | Reduces all spell damage taken by 2%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |
| **Improved Healing** | 2/3 | changed | Reduces the Mana cost of your Lesser Heal, Heal, Greater Heal, Penance, and Prayer of Mending spells by 10%. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |
| **Spiritual Guidance** | 3/5 | changed | Increases your spell healing by up to 15% of your total Spirit and your spell damage by up to 5% of your total Spirit. |
| **Binding Heal** | 1/1 | **NEW** | Heals a friendly target and the caster for 236 to 284. Low threat. |

### Shadow (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |

## Core talents (priority order)

1. **Divine Fury** — 60 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
2. **Holy Precision** — 56 DPS lost without it (10% of the build in a full raid; removal, 12,000 fights).
3. **Meditation** — 56 DPS lost without it (9% of the build in a full raid; removal, 12,000 fights).
4. **Penance** — 48 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
5. **Power in Light** — 29 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
6. **Searing Light** — 21 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
7. **Mental Agility** — 16 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
8. **Improved Shadow Word: Pain** — 15 DPS lost without it (2% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**2 of 4** for `smite-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`smite-discipline-raid`](smite-discipline-raid.md) | ours: hand draft | 31/17/3 | 350 | +0.0% | 584 | -0.6% | 7 s |
| 2 | **[`smite-open-raid`](smite-open-raid.md)** | ours: hand draft | 21/23/7 | 350 | -0.0% | 588 | +0.0% | 6 s |
| 3 | *Smite* | community simulator | - | 346 | -1.0% | 580 | -1.3% | 8 s |
| 4 | *Smite 31/17/3* | community simulator | - | 346 | -1.0% | 580 | -1.3% | 8 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 8 passes, the last 2026-10-11, 20 changes to the base rotation; third-seed check: open winner 315 -> 350 DPS (+11.1%), smite-open-raid 320 -> 338 DPS (+5.9%), sim preset: Smite 329 -> 346 DPS (+5.2%), smite-discipline-raid 331 -> 350 DPS (+5.8%)):
  1. insert before the filler: cast Smite (+42.9%, pass 1)
  2. drop: if mana % ≥ 20%: cast Smite (+6.8%, pass 1)
  3. insert at the top: strict sequence: cast Inner Focus; cast Devouring Plague (+1.9%, pass 1)
  4. insert in the middle: if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain (+2.2%, pass 1)
  5. only above 40% mana: cast Penance (+2.4%, pass 1)
  6. threshold 3s -> 2.5s: if time left on Holy Fire < 3s: cast Holy Fire (+0.8%, pass 1)
  7. move down below 'use every other cooldown when ready': strict sequence: cast Inner Focus; cast Devouring Plague (+0.7%, pass 1)
  8. threshold 40% -> 50%: if mana % ≥ 40%: cast Penance (+0.2%, pass 1)
  9. threshold 2.5s -> 1.25s: if time left on Holy Fire < 2.5s: cast Holy Fire (+0.3%, pass 1)
  10. drop the condition: if mana % ≥ 50%: cast Penance (+3.2%, pass 2)
  11. threshold 10 -> 5: if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain (+0.2%, pass 3)
  12. spell probe: insert at the end: cast Shadowform (+6.8%, pass 5)
  13. insert at the top: if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain + move down below 'use every other cooldown when ready': if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain (+0.4%, pass 6)
  14. rank 4 below 15% mana, above: if not Shadow Word: Pain is on the target and time left in the fight ≥ 5: cast Shadow Word: Pain (+0.2%, pass 6)
  15. insert in the middle: if execute phase (E20): cast Shadow Word: Death (+1.0%, pass 7)
  16. threshold 1.25s -> 1.875s: if time left on Holy Fire < 1.25s: cast Holy Fire (+0.6%, pass 7)
  17. always rank 3 instead of rank 4: cast Penance (+4.8%, pass 8)
  18. only above 60% mana: cast Smite (+7.3%, pass 8)
  19. always rank 3 instead of rank 4: if execute phase (E20): cast Shadow Word: Death (+0.6%, pass 8)
  20. rank 5 below 15% mana, above: cast Smite (+0.2%, pass 8)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 11 passes, the last 2026-10-11, 26 changes to the base rotation; third-seed check: open winner 561 -> 588 DPS (+4.8%), smite-discipline-raid 561 -> 584 DPS (+4.2%), sim preset: Smite 559 -> 580 DPS (+3.9%), smite-open-raid 562 -> 583 DPS (+3.7%)):
  1. rank 4 below 50% mana, above: if mana % ≥ 20%: cast Smite (+8.7%, pass 1)
  2. insert at the top: if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain (+2.1%, pass 1)
  3. always rank 2 instead of rank 4: if mana % ≥ 20% and mana % < 50%: cast Smite (+1.2%, pass 1)
  4. insert at the top: strict sequence: cast Inner Focus; cast Devouring Plague (+1.0%, pass 1)
  5. move down below 'use every other cooldown when ready': if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain (+1.0%, pass 1)
  6. threshold 3s -> 1.5s: if time left on Holy Fire < 3s: cast Holy Fire (+0.5%, pass 1)
  7. only with 20s or more of the fight left: if mana % ≥ 20% and mana % < 50%: cast Smite (+0.6%, pass 1)
  8. insert before the filler: cast Mind Blast (+0.2%, pass 1)
  9. move down below 'cast Mind Blast': if mana % ≥ 20%: cast Smite (+0.6%, pass 1)
  10. insert before the filler: cast Smite (+0.8%, pass 1)
  11. move down below 'use every other cooldown when ready': strict sequence: cast Inner Focus; cast Devouring Plague (+0.4%, pass 1)
  12. threshold 20s -> 30s: if mana % ≥ 20% and mana % < 50% and time left in the fight ≥ 20s: cast Smite (+0.3%, pass 1)
  13. insert in the middle: cast Shadow Word: Death (+0.3%, pass 2)
  14. always rank 3 instead of rank 4: cast Shadow Word: Death (+0.5%, pass 2)
  15. spell probe: insert at the end: cast Shadowform (+1.2%, pass 5)
  16. insert in the middle: if mana % ≥ 40%: cast Smite (+0.7%, pass 6)
  17. move down below 'if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain': strict sequence: cast Inner Focus; cast Devouring Plague (+0.2%, pass 6)
  18. insert before the filler: cast Dark Sacrifice (+0.3%, pass 7)
  19. insert at the top: cast Penance (+3.1%, pass 8)
  20. insert in the middle: cast Devouring Plague (+0.8%, pass 8)
  21. insert in the middle: cast Power Infusion (+0.2%, pass 8)
  22. threshold 40% -> 60%: if mana % ≥ 40%: cast Smite (+0.2%, pass 8)
  23. threshold 60% -> 80%: if mana % ≥ 60%: cast Smite (+0.2%, pass 8)
  24. drop: cast Smite (+3.4%, pass 9)
  25. drop the condition: if mana % ≥ 80%: cast Smite (+4.9%, pass 9)
  26. drop: cast Devouring Plague (+2.0%, pass 9)

Before the pull: at -3s: cast Holy Fire.

| # | Priority (the first line whose condition holds is cast) | [`smite-open-raid`](smite-open-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain | 2.8 |
| 3 | strict sequence: cast Inner Focus; cast Devouring Plague | 0.7 |
| 4 | if time left on Holy Fire < 1.875s: cast Holy Fire | 4.9 |
| 5 | strict sequence: cast Inner Focus; cast Smite | 0.3 |
| 6 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 5 and mana % < 15%: cast Shadow Word: Pain | 0.1 |
| 7 | if execute phase (E20): cast Shadow Word: Death | 0.9 |
| 8 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 5: cast Shadow Word: Pain | 2.8 |
| 9 | cast Penance | 4.8 |
| 10 | if not Shadow Word: Pain is on the target and mana % ≥ 30%: cast Shadow Word: Pain | 2.8 |
| 11 | if mana % ≥ 60%: cast Smite | 14.0 |
| 12 | if mana % < 15%: cast Smite | 0.7 |
| 13 | cast Smite | 3.4 |

Lines of the simulator's rotation these builds never cast: cast Shadowform (needs the Shadowform talent).

Damage by ability:

| Ability | [`smite-open-raid`](smite-open-raid.md) |
|---|---|
| Penance | 29% |
| Shadow Word: Pain | 26% |
| Holy Fire | 22% |
| Smite | 18% |
| Shadow Word: Death | 3% |
| Devouring Plague | 2% |

## Notes

- +0.6% over the best hand draft of the spec, smite-discipline-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (smite-dps, full raid): 21/23/7 (Smite (a Discipline/Holy hybrid)) at 587.6 DPS; smite-discipline-raid 584.1, smite-open-raid 583.2 in the same fights; 3,922 builds simulated, 2 independent runs reached the top.
- The smite-dps raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): shadow-dps -54.8%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Twilight Focus, Improved Renew, Spell Warding, Holy Nova.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 2ce8265 with this project's patches), not in-game measurements.
- 2026-10-11 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Renew -> Binding Heal (threat). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Smite build: check it against the community's Smite builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/priest/60/505030021301001-315151000220003-50002-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
