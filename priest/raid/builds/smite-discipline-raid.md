# Discipline/Holy — Smite (raid) — 31/17/3

*[Priest](../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/17/3 (Discipline / Holy / Shadow) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

A Smite damage build: Discipline to Penance and Power Infusion (Power in Light: +10% Smite and Penance on targets with Holy Fire; Twin Disciplines on instants; Mental Strength), Holy for Divine Fury, Holy Specialization and Searing Light. From the simulator's Smite preset, tuned by the simulator talent search and its own rotation (Holy Fire up, Penance on cooldown, Smite). For a priest who wants to deal Holy damage; its rank against Shadow is on the survey page.

## Point allocation

### Discipline (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Power in Light** | 5/5 | **NEW** | Your Smite and Penance spells deal 10% increased damage to targets afflicted with your Holy Fire. |
| **Wand Specialization** | 1/2 | changed | Increases your damage with Wands by 13%. |
| **Twin Disciplines** | 5/5 | **NEW** | Increases the damage and healing of your instant cast spells by 5%. |
| **Holy Precision** | 3/3 | **NEW** | Improves your chance to hit with Holy spells by 18%. |
| **Mental Agility** | 3/3 | changed | Reduces the mana cost of your Smite, Holy Fire, and instant cast spells by 10%. |
| **Inner Focus** | 1/1 | unchanged | When activated, reduces the Mana cost of your next spell by 100% and increases its critical effect chance by 25% if it is capable of a critical effect. |
| **Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Mental Strength** | 5/5 | changed | Increases your total Intellect by 15%. |
| **Penance** | 1/1 | **NEW** | Launches a volley of holy light at the target, causing 81 Holy damage to an enemy, or 184 healing to an ally, instantly and every 1 sec for 2 sec. |
| **Divine Aegis** | 3/3 | **NEW** | Your critical heals create a protective shield on the target, absorbing 15% of the amount healed. Lasts 12 sec. |
| **Power Infusion** | 1/1 | changed | Infuses the target with power, increasing their spell damage and healing done by 20% for 15 sec. |

### Holy (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Holy Specialization** | 5/5 | unchanged | Increases the critical effect chance of your Holy spells by 5%. |
| **Divine Fury** | 5/5 | changed | Reduces the casting time of your Smite, Holy Fire, Heal, and Greater Heal spells by 0.5 sec. |
| **Blessed Recovery** | 2/3 | changed | After being struck by a melee or ranged critical hit, or suffering more than 30% of your maximum Health from a single attack, heal 17% of the damage taken over 6 sec. Refreshing this effect carries over any remaining healing. |
| **Inspiration** | 3/3 | changed | Your non-periodic critical heals increase your target's Armor by 25% for 15 sec. |
| **Searing Light** | 2/2 | changed | Increases your Holy damage done by 5%, and gives a 10% chance each time your Holy Fire spell deals periodic damage for your next Holy Nova to cost no Mana. |

### Shadow (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Shadow Focus** | 3/5 | changed | Improves your chance to hit with Shadow spells by 3%. |

## Core talents (priority order)

1. **Inner Focus** — A free, +25% crit spell on its cooldown; the rotation opens a strict sequence with it. Simulator (2026-09-28): the rotation reads this talent's own spell or proc (or casts it in a sequence), so its removal run breaks the rotation rather than measuring it.
2. **Penance** — Holy damage on a 12 s cooldown, cast on cooldown. Simulator removal run (2026-09-28): the build loses 13.0% of its DPS on the training dummy without it.
3. **Divine Fury** — -0.5 s on Smite and Holy Fire. Simulator removal run (2026-09-28): the build loses 12.9% of its DPS on the training dummy without it.
4. **Holy Precision** — Simulator removal run (2026-09-28): the build loses 11.7% of its DPS on the training dummy without it.
5. **Meditation** — Simulator removal run (2026-09-28): the build loses 10.1% of its DPS on the training dummy without it.
6. **Power in Light** — +10% Smite and Penance on targets with Holy Fire. Simulator removal run (2026-09-28): the build loses 4.9% of its DPS on the training dummy without it.
7. **Searing Light** — +5% Holy damage. Simulator removal run (2026-09-28): the build loses 3.3% of its DPS on the training dummy without it.
8. **Power Infusion** — +20% spell damage for 15 s. Simulator removal run (2026-09-28): the build loses 3.2% of its DPS on the training dummy without it.
9. **Mental Agility** — Simulator removal run (2026-09-28): the build loses 2.0% of its DPS on the training dummy without it.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Shadow Focus | any talent legal at that tier | Worth 0.6% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 1 | Wand Specialization | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 3 | Divine Aegis | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Blessed Recovery | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 3 | Inspiration | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |

## Rank among our builds and the community simulator's

**1 of 3** for `smite-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`smite-discipline-raid`](smite-discipline-raid.md)** | ours: hand draft | 31/17/3 | 315 | +0.0% | 477 | +0.0% | 3 s |
| 2 | *Smite* | community simulator | - | 313 | -0.6% | 471 | -1.2% | 3 s |
| 3 | *Smite 31/17/3* | community simulator | - | 313 | -0.6% | 471 | -1.2% | 3 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-28, 11 changes to the base rotation; third-seed check: smite-discipline-raid 223 -> 315 DPS (+41.1%), sim preset: Smite 222 -> 313 DPS (+40.8%)):
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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 3 passes, the last 2026-09-28, 14 changes to the base rotation; third-seed check: smite-discipline-raid 441 -> 477 DPS (+8.1%), sim preset: Smite 439 -> 471 DPS (+7.2%)):
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

Before the pull: at -3s: cast Holy Fire.

| # | Priority (the first line whose condition holds is cast) | [`smite-discipline-raid`](smite-discipline-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | strict sequence: cast Inner Focus; cast Devouring Plague | 1.0 |
| 3 | if time left on Holy Fire < 1.25s: cast Holy Fire | 5.0 |
| 4 | strict sequence: cast Inner Focus; cast Smite | 0.5 |
| 5 | if not Shadow Word: Pain is on the target and time left in the fight ≥ 5: cast Shadow Word: Pain | 3.6 |
| 6 | cast Penance | 4.9 |
| 7 | if not Shadow Word: Pain is on the target and mana % ≥ 30%: cast Shadow Word: Pain | 3.6 |
| 8 | cast Smite | 20.1 |

Lines of the simulator's rotation these builds never cast: cast Smite (its condition never held in these fights).

Damage by ability:

| Ability | [`smite-discipline-raid`](smite-discipline-raid.md) |
|---|---|
| Smite | 30% |
| Shadow Word: Pain | 27% |
| Penance | 22% |
| Holy Fire | 18% |
| Devouring Plague | 4% |

## Notes

- Talents from the simulator talent search (raidsim/talent_opt.py, 2026-09-28) from `sim preset: Smite 31/17/3`: 3 points Spirit Tap -> Shadow Focus.
- New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited.

## Open questions (verify in the live game)

- Penance's damage rank (131 a bolt at rank 4) and whether Power in Light counts Penance's bolts.

## Sources

- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/priest/dps/presets.ts>
- <https://warcraftforever.games/talents/priest>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
