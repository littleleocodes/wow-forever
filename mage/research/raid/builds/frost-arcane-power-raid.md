# Frost — Arcane Power / Frostbolt (raid DPS) — 32/3/16

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 32/3/16 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `frost-arcane-power-raid` |

## Summary

The Classic 31/0/20 survives: Arcane Power (+30% damage, now +30% mana cost), Presence of Mind, Arcane Instability and a stronger Arcane Mind (+10% Intellect and +100% Arcane crit damage) with Arcane Concentration and Arcane Meditation, plus Improved Frostbolt, Ice Shards, Piercing Ice and Elemental Precision — which is now 5 ranks, so Frost Channeling drops to 2.

## Point allocation

### Arcane (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Channeling** | 5/5 | **NEW** | Gives your Arcane Missiles spell a 100% chance and your Arcane Blast and Arcane Wrath spells a 70% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, Frost Blast, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |

### Fire (3)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |

### Frost (16)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 2/3 | moved | Reduces the mana cost of your Frost spells by 10% and reduces the threat caused by your Frost spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |

## Core talents (priority order)

1. **Arcane Power** — +30% damage for 15s; now costs 30% more mana during the window and requires Presence of Mind.
2. **Presence of Mind** — Instant Frostbolt for the burst window.
3. **Arcane Instability** — +3% damage, +3% crit (est.).
4. **Arcane Mind** — +10% Intellect at max rank (est.) — mana and crit.
5. **Ice Shards** — +100% Frostbolt crit damage (unchanged).
6. **Improved Frostbolt** — -0.5s Frostbolt (unchanged).
7. **Elemental Precision** — Now 1% hit per rank over 5 ranks — 5% hit for 5 points.
8. **Piercing Ice** — +6% Frost damage.
9. **Arcane Concentration** — Clearcasting (unchanged); prerequisite for Arcane Meditation.
10. **Arcane Meditation** — Reworked: 17% of regen per rank continues while casting (est. 51% at 3/3) — much stronger than Classic.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Wand Specialization 2 + Arcane Focus 3 | Improved Channeling | Tier-1 Arcane is all filler for a Frost mage (Arcane Focus is Arcane-only hit now). |
| 3 | Arcane Geometry 2 + Arcane Blast 1 | Arcane Impact | Tier-3 Arcane filler to reach 15 points; Improved Arcane Explosion no longer exists. |
| 3 | Improved Counterspell 2 + Missile Barrage 1 | Magic Absorption 2, Arcane Shielding | Gating fillers to reach 20 and 30 points. |
| 2 | Improved Channeling | Frost Channeling, Frost Channeling 3 with Elemental Precision 4 | Mana/threat vs. the fifth point of hit. |

## Rank among our builds and the community simulator's

**3 of 13** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 54ceac6 (client 70707)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 552 | +0.0% | 661 | -1.5% | 5 s |
| 2 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 546 | -1.0% | 650 | -3.0% | 9 s |
| 3 | **[`frost-arcane-power-raid`](frost-arcane-power-raid.md)** | ours: hand draft | 32/3/16 | 544 | -1.4% | 659 | -1.7% | 7 s |
| 4 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 28/10/13 | 525 | -4.9% | 671 | +0.0% | 4 s |
| 5 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 506 | -8.4% | 572 | -14.7% | 0 s |
| 6 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 502 | -9.1% | 597 | -11.0% | 5 s |
| 7 | *Arcane Fire* | community simulator | - | 482 | -12.7% | 619 | -7.7% | 6 s |
| 8 | *Arcane* | community simulator | - | 482 | -12.7% | 631 | -5.9% | 6 s |
| 9 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 457 | -17.2% | 519 | -22.6% | 0 s |
| 10 | *Frost Incin* | community simulator | - | 454 | -17.9% | 544 | -18.9% | 4 s |
| 11 | *Frost Med* | community simulator | - | 444 | -19.6% | 539 | -19.5% | 9 s |
| 12 | *Fire* | community simulator | - | 408 | -26.0% | 487 | -27.4% | 8 s |
| 13 | *FFB* | community simulator | - | 387 | -30.0% | 447 | -33.4% | 2 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 5 passes, the last 2026-10-23, 12 changes to the base rotation; third-seed check: open winner 528 -> 577 DPS (+9.3%), opt-frost-raid-raid-dps-extwc 549 -> 586 DPS (+6.8%), sim preset: Arcane Frost 516 -> 582 DPS (+12.8%), frost-arcane-power-raid 515 -> 577 DPS (+12.2%), frost-winters-chill-raid 436 -> 441 DPS (+1.1%), frost-fingers-of-frost-raid 480 -> 484 DPS (+0.8%), opt-frost-raid-raid-dps 532 -> 566 DPS (+6.4%), frost-ml-raid 478 -> 482 DPS (+0.8%), arcane-frost-open-raid 543 -> 576 DPS (+6.2%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
  4. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast (+0.6%, pass 3)
  5. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 4)
  6. threshold 25s -> 50s: if mana % < 5% and time left in the fight > 25s: cast Evocation (+0.2%, pass 4)
  7. insert at the end: cast Arcane Blast (+0.2%, pass 4)
  8. insert in the middle: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+10.2%, pass 5)
  9. insert at the end: cast Robe of the Archmage (+0.9%, pass 5)
  10. insert in the middle: if Arcane Wrath is ready: cast Presence of Mind (+0.7%, pass 5)
  11. move down below 'if Fingers of Frost is up: cast Ice Lance': if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+0.2%, pass 5)
  12. only above 60% mana: if mana % ≤ 60%: cast Mana Ruby + insert at the end: cast Frost Blast (+0.2%, pass 5)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 10 passes, the last 2026-10-31, 6 changes to the base rotation; third-seed check: arcane-frost-open-raid 558 -> 671 DPS (+20.3%), sim preset: Arcane 464 -> 632 DPS (+36.3%), frost-arcane-power-raid 575 -> 660 DPS (+14.7%), frost-winters-chill-raid 515 -> 520 DPS (+0.8%), frost-fingers-of-frost-raid 574 -> 573 DPS (-0.3%), opt-frost-raid-raid-dps 618 -> 661 DPS (+6.9%), opt-frost-raid-raid-dps-extwc 616 -> 650 DPS (+5.5%), frost-ml-raid 569 -> 597 DPS (+5.0%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)
  3. spell probe: insert in the middle: cast Arcane Wrath (+1.0%, pass 6)
  4. insert at the top: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+6.1%, pass 7)
  5. move to the top: if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+2.2%, pass 7)
  6. only with 20s or more of the fight left: cast Arcane Wrath (+0.4%, pass 7)

| # | Priority (the first line whose condition holds is cast) | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 4.6 |
| 4 | if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast | 8.1 |
| 5 | if Arcane Wrath is ready: cast Presence of Mind | 0.3 |
| 6 | if mana % < 5% and time left in the fight > 50s: cast Evocation | 0.1 |
| 7 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 13.4 |
| 8 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.1 |
| 9 | cast Arcane Blast | 8.1 |
| 10 | cast Robe of the Archmage | as ready |

Lines of the simulator's rotation these builds never cast: cast Ice Lance (needs the Ice Lance talent); cast spell 1326055 (its condition never held in these fights).

Damage by ability:

| Ability | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) |
|---|---|
| Frostbolt | 49% |
| Arcane Missiles | 33% |
| Arcane Blast | 17% |
| Demonic Rune | 2% |
| Fire Blast | 0% |

## Notes

- Missile Barrage (Frostbolt 20% chance to make the next Arcane Missiles fast and free) could add a filler cast; treat it as a curiosity until tested.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Geometry -> Arcane Impact (+0.4% DPS); Arcane Geometry -> Arcane Impact (+0.4% DPS); Arcane Subtlety -> Arcane Impact (+0.4% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Improved Counterspell -> Arcane Focus (+0.3% DPS); Improved Counterspell -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Frost Channeling -> Improved Channeling (interrupt); Frost Channeling -> Improved Channeling (interrupt). Net +1.80% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Arcane Blast was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Blast -> Frost Channeling (threat). Net -0.01% on a third seed.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 32/0/19 -> 35/0/16; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; refill +1 Missile Barrage, +1 Frost Channeling, +1 Arcane Blast, +1 Arcane Wrath, +1 Ice Block (refill: the frost-raid model, raid-dps).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 35/0/16 -> 32/3/16; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Arcane Subtlety (tier gating for Arcane Power); refill +1 Arcane Subtlety, +3 Incineration (refill: the frost-raid model, raid-dps).

## Open questions (verify in the live game)

- Is Arcane Instability's crit 'with all attacks' also spell crit? Demo wording is ambiguous.
- Whether the deep Frost Fingers of Frost build out-damages this — see frost-fingers-of-frost-raid.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
