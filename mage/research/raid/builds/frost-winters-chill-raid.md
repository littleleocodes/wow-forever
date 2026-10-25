# Frost — Winter's Chill (raid support) — 21/0/30

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `frost-winters-chill-raid` |

## Summary

Winter's Chill now buffs Frostbolt and Ice Lance crit (demo text says it stacks once — likely a transcription artefact; Classic stacked to 5), Ice Block moved to tier 4 and Cold Snap to tier 5, Shatter is 3 ranks. The 17/0/34 shape still fits with Elemental Precision at 5 ranks.

## Point allocation

### Arcane (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 4/5 | **NEW** | Gives you a 80% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 56% chance while casting Arcane Blast or Arcane Wrath. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, your Arcane Missile hits a 5% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |

### Fire (0)

*No points.*

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Winter's Chill** | 5/5 | changed | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the damage done by your Cone of Cold spell to the target by 40%, stacking up to 5 times. |

## Core talents (priority order)

1. **Winter's Chill** — 100% chance at max rank to apply the crit debuff for Frostbolt/Ice Lance — the raid-support reason for the build.
2. **Ice Shards** — Frostbolt crit damage.
3. **Elemental Precision** — 5% hit.
4. **Improved Frostbolt** — Cast time.
5. **Piercing Ice** — Frost damage.
6. **Ice Block** — Now the 16-point Frost talent — cheap immunity.
7. **Frost Channeling** — Mana and threat.
8. **Arcane Meditation** — Regen while casting (2/3).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Arcane Meditation 2 | Arcane Meditation 3 with Arcane Blast 0 | Regen vs. filler. |

## Rank among our builds and the community simulator's

**9 of 11** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 587 | +0.0% | 680 | -1.8% | 9 s |
| 2 | *Arcane Frost* | community simulator | - | 582 | -0.9% | 693 | +0.0% | 8 s |
| 3 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 29/0/22 | 577 | -1.7% | 693 | -0.0% | 7 s |
| 4 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 35/0/16 | 577 | -1.7% | 676 | -2.4% | 5 s |
| 5 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 549 | -6.4% | 628 | -9.3% | 4 s |
| 6 | *Arcane Fire* | community simulator | - | 521 | -11.2% | 645 | -6.8% | 2 s |
| 7 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 484 | -17.5% | 547 | -21.0% | 0 s |
| 8 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 482 | -17.9% | 544 | -21.4% | 0 s |
| 9 | **[`frost-winters-chill-raid`](frost-winters-chill-raid.md)** | ours: hand draft | 21/0/30 | 441 | -24.8% | 501 | -27.7% | 0 s |
| 10 | *Fire* | community simulator | - | 439 | -25.2% | 504 | -27.2% | 8 s |
| 11 | *FFB* | community simulator | - | 387 | -34.1% | 443 | -36.1% | 2 s |

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
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 7 passes, the last 2026-10-23, 6 changes to the base rotation; third-seed check: open winner 626 -> 691 DPS (+10.4%), opt-frost-raid-raid-dps-extwc 623 -> 680 DPS (+9.3%), sim preset: Arcane Frost 586 -> 693 DPS (+18.1%), frost-arcane-power-raid 585 -> 676 DPS (+15.6%), frost-winters-chill-raid 497 -> 501 DPS (+0.8%), frost-fingers-of-frost-raid 544 -> 547 DPS (+0.5%), opt-frost-raid-raid-dps 606 -> 663 DPS (+9.3%), frost-ml-raid 542 -> 545 DPS (+0.5%), arcane-frost-open-raid 622 -> 687 DPS (+10.5%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)
  3. spell probe: insert in the middle: cast Arcane Wrath (+1.0%, pass 6)
  4. insert at the top: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+6.1%, pass 7)
  5. move to the top: if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+2.2%, pass 7)
  6. only with 20s or more of the fight left: cast Arcane Wrath (+0.4%, pass 7)

| # | Priority (the first line whose condition holds is cast) | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 2.2 |
| 4 | if Arcane Wrath is ready: cast Presence of Mind | 0.3 |
| 5 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 21.8 |
| 6 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.3 |
| 7 | cast Robe of the Archmage | as ready |

Lines of the simulator's rotation these builds never cast: cast Ice Lance (needs the Ice Lance talent); cast Arcane Blast (needs the Arcane Blast talent); cast Evocation, cast Frost Blast (its condition never held in these fights).

Damage by ability:

| Ability | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) |
|---|---|
| Frostbolt | 82% |
| Arcane Missiles | 15% |
| Demonic Rune | 2% |
| Fire Blast | 1% |
| Frost Blast | 0% |

## Notes

- Ice Lance + Fingers of Frost are not taken here; they need 3 more Frost points (see the Fingers of Frost build).
- 2026-09-27 scenario audit: Improved Frost Nova 2 -> Arctic Reach 2. Improved Frost Nova shortens a root's cooldown: control a raid boss ignores (simulator 0.0%). Arctic Reach 2/2 adds range. This draft is superseded in Forever: the beta Winter's Chill raises only your own Frostbolt and Ice Lance crit, so the raid-support reason for skipping Fingers of Frost is gone, and frost-fingers-of-frost-raid simulates about 14% higher (645 vs 559 DPS).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arctic Reach -> Missile Barrage (+7.6% DPS); Arcane Geometry -> Arcane Impact (+0.2% DPS); Arcane Geometry -> Arcane Impact (+0.2% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Arctic Reach -> Arcane Impact (+0.2% DPS); Shatter -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Shatter -> Arctic Reach (range); Shatter -> Arctic Reach (range). Net +8.80% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Arcane Blast, Ice Barrier was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Ice Barrier -> Presence of Mind (+1.1% DPS); Arcane Blast -> Improved Channeling (interrupt). Net +1.11% on a third seed.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 21/0/30 -> 21/0/30; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; +1 Frost Warding (tier gating for Cold Snap); +1 Frost Warding (tier gating for Winter's Chill); +1 Frostbite (tier gating for Winter's Chill); +1 Frostbite (tier gating for Winter's Chill); +1 Frostbite (tier gating for Winter's Chill) (refill: the frost-raid model, raid-dps).

## Open questions (verify in the live game)

- Winter's Chill stack count (demo says 1; Classic was 5) — decides whether one dedicated WC mage is still worth it.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
