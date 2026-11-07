# Smite — Raid (open talent search) — 17/17/17

*[Priest](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/17/17 (Discipline / Holy / Shadow) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Smite (a Discipline/Holy hybrid) raid build the open talent search found on 2026-11-03: every legal 51-point build with no tree rule, searched in the community simulator's smite-dps rotation in a full raid (every raid buff and debuff: the group setting; raidsim/family_search.py: every pair of keystones polished by a short hill climb first, then the machine-learning search, the winner raced against the rotation's builds over 30,000 fights). +1.0% over smite-open-raid, the best of our builds in that rotation.

## Point allocation

### Discipline (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire or Shadow Word: Pain. |
| **Twin Disciplines** | 2/5 | **NEW** | Increases the damage and healing of your instant cast spells by 2%. |
| **Holy Precision** | 3/3 | **NEW** | Improves your chance to hit with Holy spells by 18%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | changed | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is a non-periodic spell and capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Holy (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Holy Nova** | 1/1 | changed | Causes an explosion of holy light around the caster, causing 26 to 30 Holy damage to all enemy targets within 10 yards and healing all party members within 10 yards for 49 to 57. These effects cause no threat. |
| **Blessed Recovery** | 2/3 | changed | After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 17% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing. |
| **Inspiration** | 1/3 | changed | Your non-periodic critical heals increase your target's Armor by 8% for 15 sec. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |
| **Spell Warding** | 1/5 | unchanged | Reduces all spell damage taken by 2%. |

### Shadow (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 5/5 | changed | Improves your chance to hit with Shadow spells by 5%. |
| **Improved Mind Blast** | 5/5 | changed | Reduces the cooldown of your Mind Blast spell by 2.5 sec. |
| **Improved Shadow Word: Pain** | 2/2 | moved | Increases the duration of your Shadow Word: Pain spell by 6 sec. |
| **Mind Flay** | 1/1 | changed | Assault the target's mind with Shadow energy, causing 63 Shadow damage over 3 sec and slowing their movement speed by 50%. |
| **Shadow Weaving** | 2/3 | changed | Your Shadow damage spells have a 67% chance to increase the Shadow damage the target takes from you by 2% for 15 sec, stacking up to 5 times. |
| **Spirit Tap** | 2/5 | changed | Gives you a 40% chance to increase your Spirit by 100% for 15 sec after killing a non-trivial target or when an enemy afflicted by your Vampiric Embrace dies. For the duration, 50% of your Mana regeneration will continue while casting. |

## Core talents (priority order)

1. **Divine Fury** — 67 DPS lost without it (11% of the build in a full raid; removal, 12,000 fights).
2. **Holy Precision** — 51 DPS lost without it (8% of the build in a full raid; removal, 12,000 fights).
3. **Inner Focus** — 29 DPS lost without it (5% of the build in a full raid; removal, 12,000 fights).
4. **Power in Light** — 23 DPS lost without it (4% of the build in a full raid; removal, 12,000 fights).
5. **Meditation** — 21 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
6. **Shadow Weaving** — 17 DPS lost without it (3% of the build in a full raid; removal, 12,000 fights).
7. **Shadow Focus** — 13 DPS lost without it (2% of the build in a full raid; removal, 12,000 fights).
8. **Searing Light** — 13 DPS lost without it (2% of the build in a full raid; removal, 12,000 fights).

## Rank among our builds and the community simulator's

**3 of 3** for `smite-dps` by training-dummy DPS in the community simulator (wowsims/forever bac92db (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`smite-discipline-raid`](smite-discipline-raid.md) | ours: hand draft | 31/17/3 | 363 | +0.0% | 582 | -3.3% | 42 s |
| 2 | *Smite* | community simulator | - | 363 | +0.0% | 582 | -3.3% | 42 s |
| 3 | **[`smite-open-raid`](smite-open-raid.md)** | ours: derived (open search) | 17/17/17 | 343 | -5.6% | 602 | +0.0% | 40 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 9 passes, the last 2026-10-14, 22 changes to the base rotation; third-seed check: ):
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
  21. spell probe: insert in the middle: if auraIsInactive: cast Power Infusion (+0.6%, pass 9)
  22. spell probe: insert in the middle: if not Mind Flay is on the target: cast Mind Flay (+14.5%, pass 9)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 15 passes, the last 2026-11-03, 39 changes to the base rotation; third-seed check: smite-open-raid 539 -> 602 DPS (+11.6%), sim preset: Smite 526 -> 582 DPS (+10.7%), smite-discipline-raid 526 -> 582 DPS (+10.7%)):
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
  27. spell probe: insert at the end: if not Mind Flay is on the target: cast Mind Flay (+0.2%, pass 12)
  28. drop the condition: if mana % ≥ 20% and mana % < 50% and time left in the fight ≥ 30s: cast Smite (rank 2) (+14.6%, pass 13)
  29. drop: cast Penance (rank 3) (+0.6%, pass 13)
  30. drop: cast Penance (+0.8%, pass 13)
  31. only above 25% mana: cast Smite (+0.6%, pass 13)
  32. only above 40% mana: if time left on Holy Fire < 1.5s: cast Holy Fire (+0.5%, pass 13)
  33. only with 10s or more of the fight left: cast Smite (rank 2) (+0.3%, pass 13)
  34. move down below 'if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain': use every other cooldown when ready (+0.3%, pass 13)
  35. move down below 'strict sequence: cast Inner Focus; cast Devouring Plague': use every other cooldown when ready (+0.2%, pass 13)
  36. move to the top: cast Mind Blast (+0.8%, pass 14)
  37. threshold 1.5s -> 0.5s: if time left on Holy Fire < 1.5s and mana % ≥ 40%: cast Holy Fire (+0.2%, pass 14)
  38. move down below 'if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain': cast Mind Blast (+0.2%, pass 14)
  39. insert before the filler: cast Demonic Rune (+0.4%, pass 15)

Before the pull: at -3s: cast Holy Fire.

| # | Priority (the first line whose condition holds is cast) | [`smite-open-raid`](smite-open-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 10: cast Shadow Word: Pain | 2.3 |
| 3 | strict sequence: cast Inner Focus; cast Devouring Plague | 0.7 |
| 4 | if time left on Holy Fire < 1.875s: cast Holy Fire | 4.0 |
| 5 | strict sequence: cast Inner Focus; cast Smite | 0.3 |
| 6 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 5 and mana % < 15%: cast Shadow Word: Pain (rank 4) | 0.1 |
| 7 | if execute phase (E20): cast Shadow Word: Death (rank 3) | 0.6 |
| 8 | if not Mind Flay is on the target: cast Mind Flay | 10.8 |
| 9 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 5: cast Shadow Word: Pain | 2.3 |
| 10 | if not Shadow Word: Pain is on the target and mana % ≥ 30%: cast Shadow Word: Pain | 2.3 |
| 11 | if mana % < 15%: cast Smite (rank 5) | 2.4 |

Lines of the simulator's rotation these builds never cast: cast Power Infusion (needs the Power Infusion talent); cast Penance (rank 3) (needs the Penance talent); cast Smite (rank 2), cast Smite (rank 7) (its condition never held in these fights); cast Shadowform (needs the Shadowform talent).

Damage by ability:

| Ability | [`smite-open-raid`](smite-open-raid.md) |
|---|---|
| Mind Flay | 41% |
| Shadow Word: Pain | 26% |
| Holy Fire | 19% |
| Smite | 7% |
| Demonic Rune | 3% |
| Devouring Plague | 2% |
| Shadow Word: Death | 2% |

## Notes

- +2.9% over the best hand draft of the spec, smite-discipline-raid, over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative.
- Open search result (smite-dps, full raid): 17/17/17 (Smite (a Discipline/Holy hybrid)) at 611.1 DPS; smite-open-raid 605.0, smite-discipline-raid 593.7 in the same fights; 2,354 builds simulated, 1 independent runs reached the top.
- The smite-dps raid rotation was re-tuned on this build (a pass in its rotation-search record); the numbers use it.
- Sibling rotations tried on it (10,000 fights): shadow-dps -18.3%; none adopted.
- Talents the simulator measures at 0 DPS in this build (tier fillers; the filler audit may move them): Twilight Focus, Holy Nova, Blessed Recovery, Inspiration, Mind Flay, Improved Mind Flay.
- Simulator numbers are the community's model of the beta (wowsims/forever bac92db (client 70707) with this project's patches), not in-game measurements.
- 2026-11-03 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Mind Flay -> Spirit Tap (mana); Improved Mind Flay -> Spirit Tap (mana); Twilight Focus -> Spell Warding (survival). Net -0.00% on a third seed.

## Open questions (verify in the live game)

- An open-search Smite build: check it against the community's Smite builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>
- <https://talentsforever.com/priest/60/50203003103-10505121002-500520012002-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
