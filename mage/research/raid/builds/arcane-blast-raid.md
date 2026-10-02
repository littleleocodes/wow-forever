# Arcane — Arcane Blast (raid) — 35/11/5

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 35/11/5 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Arcane Blast, a Forever Arcane talent whose damage and cost grow with each cast, as the core of an Arcane build: Arcane Blast stacks, Arcane Missiles on Missile Barrage procs, Frostbolt while the stacks fall off, Arcane Power and Presence of Mind. Talents from the simulator talent search from the simulator's Arcane presets, keeping Arcane Blast.

## Point allocation

### Arcane (35)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |

### Fire (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wake of Fire** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 50%. |
| **Incineration** | 3/3 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Burning Soul** | 1/3 | changed | Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%. |

### Frost (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |

## Core talents (priority order)

1. **Missile Barrage** — Procs a fast, free Arcane Missiles. Simulator (2026-09-28): the rotation reads this talent's own spell or proc (or casts it in a sequence), so its removal run breaks the rotation rather than measuring it.
2. **Arcane Blast** — The build's nuke. Simulator (2026-09-28): the rotation reads this talent's own spell or proc (or casts it in a sequence), so its removal run breaks the rotation rather than measuring it.
3. **Arcane Mind** — Intellect. Simulator removal run (2026-09-28): the build loses 8.3% of its DPS on the training dummy without it.
4. **Arcane Instability** — +damage and crit. Simulator removal run (2026-09-28): the build loses 5.4% of its DPS on the training dummy without it.
5. **Arcane Focus** — Simulator removal run (2026-09-28): the build loses 4.2% of its DPS on the training dummy without it.
6. **Arcane Power** — +damage cooldown. Simulator removal run (2026-09-28): the build loses 4.1% of its DPS on the training dummy without it.
7. **Arcane Impact** — Simulator removal run (2026-09-28): the build loses 3.6% of its DPS on the training dummy without it.
8. **Incineration** — Simulator removal run (2026-09-28): the build loses 3.3% of its DPS on the training dummy without it.
9. **Ignite** — Simulator removal run (2026-09-28): the build loses 2.7% of its DPS on the training dummy without it.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 3 | Arcane Meditation | any talent legal at that tier | Worth 0.5% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Arcane Subtlety | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 1 | Burning Soul | Magic Absorption, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 3 | Burning Soul | any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |
| 2 | Arcane Subtlety | Improved Flamestrike, any talent legal at that tier | Worth 0.0% of the DPS on the training dummy in the simulator: free points (a tier filler, or noise). |

## Rank among our builds and the community simulator's

**1 of 3** for `arcane-dps` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`arcane-blast-raid`](arcane-blast-raid.md)** | ours: hand draft | 35/11/5 | 602 | +0.0% | 690 | +0.0% | 0 s |
| 2 | *Arcane DPS* | community simulator | - | 594 | -1.3% | 681 | -1.3% | 0 s |
| 3 | *Arcane 35/0/16* | community simulator | - | 569 | -5.5% | 649 | -6.0% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 7 changes to the base rotation; third-seed check: ml: Arcane 575 -> 603 DPS (+4.8%), arcane-blast-raid 561 -> 602 DPS (+7.3%), sim preset: Arcane DPS 558 -> 594 DPS (+6.6%)):
  1. threshold 3 -> 1.5: if (stacks of Arcane Blast ≥ 3 or mana % < 40%): cast Frostbolt (+2.2%, pass 1)
  2. drop 'mana % < 40%' from the condition: if (stacks of Arcane Blast ≥ 1.5 or mana % < 40%): cast Frostbolt (+0.4%, pass 1)
  3. insert at the top: if mana ≥ (time left in the fight × 110): cast Fire Blast + threshold 110 -> 220: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.2%, pass 1)
  4. drop the condition: if mana ≥ (time left in the fight × 220): cast Fire Blast (+2.9%, pass 2)
  5. move down below 'use every other cooldown when ready': cast Fire Blast (+0.4%, pass 2)
  6. drop: if mana % < 15% and time left in the fight > 20s: cast Evocation (+0.9%, pass 5)
  7. insert at the end: cast Fireball (+0.6%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-09-28, 5 passes, the last 2026-10-02, 3 changes to the base rotation; third-seed check: ml: Arcane 675 -> 691 DPS (+2.3%), arcane-blast-raid 667 -> 691 DPS (+3.6%), sim preset: Arcane DPS 664 -> 681 DPS (+2.5%)):
  1. threshold 3 -> 1.5: if (stacks of Arcane Blast ≥ 3 or mana % < 40%): cast Frostbolt (+0.2%, pass 1)
  2. insert in the middle: if mana ≥ (time left in the fight × 110): cast Fire Blast (+2.3%, pass 2)
  3. drop the condition: if mana ≥ (time left in the fight × 110): cast Fire Blast (+2.4%, pass 2)

| # | Priority (the first line whose condition holds is cast) | [`arcane-blast-raid`](arcane-blast-raid.md) casts/min |
|---|---|---|
| 1 | use every other cooldown when ready | as ready |
| 2 | cast Fire Blast | 9.2 |
| 3 | if Missile Barrage is up: cast Arcane Missiles | 5.2 |
| 4 | if stacks of Arcane Blast ≥ 1.5: cast Frostbolt | 0.1 |
| 5 | cast Arcane Blast | 12.9 |
| 6 | cast Fireball | 0.4 |

Damage by ability:

| Ability | [`arcane-blast-raid`](arcane-blast-raid.md) |
|---|---|
| Arcane Blast | 39% |
| Arcane Missiles | 34% |
| Fire Blast | 22% |
| Ignite | 3% |
| Frostbolt | 1% |
| Fireball | 0% |

## Notes

- Talents from the simulator talent search (raidsim/talent_opt.py, 2026-09-28) from `sim preset: Arcane DPS`: 3 points Master of Elements -> Elemental Precision, 2 points Improved Scorch -> Elemental Precision.
- New-builds survey (2026-09-28, user request): see _reference/new-builds-survey.md. A simulator-searched build: no scorer model covers it, so it is raced and ranked, not optimized or audited.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Subtlety -> Improved Channeling (interrupt); Arcane Subtlety -> Improved Channeling (interrupt); Burning Soul -> Improved Channeling (interrupt); Burning Soul -> Improved Channeling (interrupt); Burning Soul -> Improved Channeling (interrupt); Improved Flamestrike -> Arcane Subtlety (threat); Improved Flamestrike -> Arcane Subtlety (threat); Magic Absorption -> Burning Soul (threat). Net +0.00% on a third seed.

## Open questions (verify in the live game)

- Arcane Blast's stacking cost against a mage's mana in long fights (the simulator's fights last 120 s).

## Sources

- <https://github.com/ElliotWood/Forever/blob/master/ui/specs/mage/dps/presets.ts>
- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
