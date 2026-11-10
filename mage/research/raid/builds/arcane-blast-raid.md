# Arcane — Arcane Blast (raid) — 31/13/7

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 31/13/7 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Arcane Blast, a Forever Arcane talent whose damage and cost grow with each cast, as the core of an Arcane build: Arcane Blast stacks, Arcane Missiles on Missile Barrage procs, Frostbolt while the stacks fall off, Arcane Power and Presence of Mind. Talents from the simulator talent search from the simulator's Arcane presets, keeping Arcane Blast.

## Point allocation

### Arcane (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (13)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 5/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 10%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 1/3 | changed | Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |

### Frost (7)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 4/5 | changed | Reduces the casting time of your Frostbolt spell by 0.4 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |

## Core talents (priority order)

1. **Missile Barrage** — Procs a fast, free Arcane Missiles. Simulator (2026-09-28): the rotation reads this talent's own spell or proc (or casts it in a sequence), so its removal run breaks the rotation rather than measuring it.
2. **Arcane Blast** — The build's nuke. Simulator (2026-09-28): the rotation reads this talent's own spell or proc (or casts it in a sequence), so its removal run breaks the rotation rather than measuring it.
3. **Arcane Mind** — Intellect. Simulator removal run (2026-09-28): the build loses 8.3% of its DPS on the training dummy without it.
4. **Arcane Instability** — +damage and crit. Simulator removal run (2026-09-28): the build loses 5.4% of its DPS on the training dummy without it.
5. **Arcane Power** — +damage cooldown. Simulator removal run (2026-09-28): the build loses 4.1% of its DPS on the training dummy without it.
6. **Arcane Impact** — Simulator removal run (2026-09-28): the build loses 3.6% of its DPS on the training dummy without it.
7. **Incineration** — Simulator removal run (2026-09-28): the build loses 3.3% of its DPS on the training dummy without it.
8. **Ignite** — Simulator removal run (2026-09-28): the build loses 2.7% of its DPS on the training dummy without it.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Arcane Meditation | any talent legal at that tier | Worth 0.5% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Arcane Subtlety | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 1 | Burning Soul | Magic Absorption, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 3 | Burning Soul | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Arcane Subtlety | Improved Flamestrike, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |

## Rank among our builds and the community simulator's

**3 of 3** for `arcane-dps` by training-dummy DPS in the community simulator (wowsims/forever 16e8542 (client 70790)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | *Arcane Fire* | community simulator | - | 580 | +0.0% | 778 | -1.4% | 3 s |
| 2 | [`arcane-open-raid`](arcane-open-raid.md) | ours: derived (open search) | 31/17/3 | 579 | -0.1% | 790 | +0.0% | 5 s |
| 3 | **[`arcane-blast-raid`](arcane-blast-raid.md)** | ours: hand draft | 31/13/7 | 558 | -3.8% | 711 | -10.0% | 4 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 14 passes, the last 2026-11-10, 29 changes to the base rotation; third-seed check: arcane-open-raid 766 -> 790 DPS (+3.1%), sim preset: Arcane Fire 754 -> 777 DPS (+3.1%), arcane-blast-raid 655 -> 710 DPS (+8.4%)):
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

| # | Priority (the first line whose condition holds is cast) | [`arcane-blast-raid`](arcane-blast-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | if Missile Barrage is up: cast Arcane Missiles (rank 7) | 4.0 |
| 3 | cast Fire Blast | 8.2 |
| 4 | if Arcane Blast is up and time left on Arcane Blast < cast time of Arcane Blast: cast Arcane Blast | 7.9 |
| 5 | if stacks of Arcane Blast ≥ 1.5 and time left in the fight ≥ 10s: cast Frostbolt (rank 10) | 8.3 |
| 6 | cast Arcane Blast | 7.9 |
| 7 | cast Robe of the Archmage | as ready |
| 8 | cast Mana Citrine | as ready |

Lines of the simulator's rotation these builds never cast: cast Arcane Wrath (needs the Arcane Wrath talent); cast Fireball (rank 11), cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`arcane-blast-raid`](arcane-blast-raid.md) |
|---|---|
| Arcane Missiles | 28% |
| Frostbolt | 28% |
| Fire Blast | 22% |
| Arcane Blast | 17% |
| Ignite | 3% |
| Demonic Rune | 1% |
| Fireball | 0% |

## Notes

- Talents from the simulator talent search (raidsim/talent_opt.py, 2026-09-28) from `sim preset: Arcane DPS`: 3 points Master of Elements -> Elemental Precision, 2 points Improved Scorch -> Elemental Precision.
- New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Subtlety -> Improved Channeling (interrupt); Arcane Subtlety -> Improved Channeling (interrupt); Burning Soul -> Improved Channeling (interrupt); Burning Soul -> Improved Channeling (interrupt); Burning Soul -> Improved Channeling (interrupt); Improved Flamestrike -> Arcane Subtlety (threat); Improved Flamestrike -> Arcane Subtlety (threat); Magic Absorption -> Burning Soul (threat). Net +0.00% on a third seed.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Arcane: its full-raid winner is +0.36% against it, under the 0.5% bar for a new build.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 35/11/5 -> 35/11/5; Wake of Fire -> Improved Fire Blast (renamed) (refill: the frost-raid model, raid-dps).
- 2026-10-22 (repair_builds.py, client build 70425 trees): 35/11/5 -> 36/11/4; Elemental Precision 5 -> 3 (rank cap); refill +1 Missile Barrage, +1 Improved Frostbolt (refill: the frost-raid model, raid-dps).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 36/11/4 -> 31/13/7; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Incineration (tier gating for Ignite); +1 Incineration (tier gating for Ignite); refill +3 Improved Frostbolt (refill: the frost-raid model, raid-dps).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Arcane Focus; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Arcane Blast's stacking cost against a mage's mana in long fights (the simulator's fights last 120 s).

## Sources

- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/mage/dps/presets.ts>
- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
