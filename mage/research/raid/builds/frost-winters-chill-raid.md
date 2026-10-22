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
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Meditation** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, your Arcane Missile hits a 5% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Improved Channeling** | 4/5 | **NEW** | Gives you a 80% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 56% chance while casting Arcane Blast or Arcane Wrath. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |

### Fire (0)

*No points.*

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Winter's Chill** | 5/5 | changed | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the damage done by your Cone of Cold spell to the target by 40%, stacking up to 5 times. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |

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

**8 of 13** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 2ce8265); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 21/0/30 | 602 | +0.0% | 680 | -1.0% | 0 s |
| 2 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 598 | -0.5% | 676 | -1.6% | 0 s |
| 3 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 22/0/29 | 597 | -0.8% | 676 | -1.6% | 1 s |
| 4 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 28/0/23 | 589 | -2.1% | 687 | +0.0% | 5 s |
| 5 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 32/0/19 | 566 | -5.9% | 643 | -6.4% | 0 s |
| 6 | *Frost DPS* | community simulator | - | 557 | -7.5% | 632 | -8.0% | 0 s |
| 7 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 1/13/37 | 546 | -9.3% | 646 | -6.0% | 7 s |
| 8 | **[`frost-winters-chill-raid`](frost-winters-chill-raid.md)** | ours: hand draft | 21/0/30 | 541 | -10.0% | 612 | -10.9% | 0 s |
| 9 | *Frost 14/0/37* | community simulator | - | 540 | -10.2% | 641 | -6.7% | 8 s |
| 10 | *Arcane 35/0/16* | community simulator | - | 487 | -19.1% | 553 | -19.5% | 0 s |
| 11 | *Arcane DPS* | community simulator | - | 420 | -30.1% | 472 | -31.2% | 0 s |
| 12 | *Fire 0/35/16* | community simulator | - | 385 | -36.0% | 438 | -36.2% | 0 s |
| 13 | *Fire DPS* | community simulator | - | 323 | -46.3% | 362 | -47.3% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 4 passes, the last 2026-10-09, 7 changes to the base rotation; third-seed check: open winner 576 -> 605 DPS (+5.1%), frost-ml-raid 591 -> 604 DPS (+2.2%), sim preset: Frost DPS 551 -> 561 DPS (+1.7%), frost-arcane-power-raid 567 -> 572 DPS (+0.8%), frost-winters-chill-raid 544 -> 547 DPS (+0.6%), frost-fingers-of-frost-raid 588 -> 602 DPS (+2.4%), opt-frost-raid-raid-dps 580 -> 600 DPS (+3.4%), opt-frost-raid-raid-dps-extwc 545 -> 549 DPS (+0.8%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%, pass 1)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  3. repair: insert before the filler: if mana % < 5% and time left in the fight > 25s: cast Evocation (every frost-raid build raced, 20,000 fights, seed 3: opt-frost-raid-raid-dps-extwc +6.6%, the others -0.02% to +0.00%) (+6.6%, pass 2)
  4. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast (+0.6%, pass 3)
  5. threshold 80% -> 60%: if mana % ≤ 80%: cast Mana Ruby (mana gem) (+0.2%, pass 4)
  6. threshold 25s -> 50s: if mana % < 5% and time left in the fight > 25s: cast Evocation (+0.2%, pass 4)
  7. insert at the end: cast Arcane Blast (+0.2%, pass 4)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 4 passes, the last 2026-10-09, 2 changes to the base rotation; third-seed check: open winner 676 -> 693 DPS (+2.4%), frost-ml-raid 673 -> 683 DPS (+1.5%), sim preset: Frost DPS 631 -> 635 DPS (+0.7%), frost-arcane-power-raid 646 -> 650 DPS (+0.6%), frost-winters-chill-raid 616 -> 620 DPS (+0.6%), frost-fingers-of-frost-raid 669 -> 680 DPS (+1.7%), opt-frost-raid-raid-dps 669 -> 680 DPS (+1.7%), opt-frost-raid-raid-dps-extwc 645 -> 650 DPS (+0.7%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)

| # | Priority (the first line whose condition holds is cast) | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.3 |

Lines of the simulator's rotation these builds never cast: cast Arcane Missiles (rank 7), cast Evocation, cast Frostbolt (rank 10) (its condition never held in these fights); cast Ice Lance (needs the Ice Lance talent); cast Arcane Blast (needs the Arcane Blast talent).

Damage by ability:

| Ability | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) |
|---|---|
| Frostbolt | 78% |
| Arcane Missiles | 22% |
| Fire Blast | 1% |

## Notes

- Ice Lance + Fingers of Frost are not taken here; they need 3 more Frost points (see the Fingers of Frost build).
- 2026-09-27 scenario audit: Improved Frost Nova 2 -> Arctic Reach 2. Improved Frost Nova shortens a root's cooldown: control a raid boss ignores (simulator 0.0%). Arctic Reach 2/2 adds range. This draft is superseded in Forever: the beta Winter's Chill raises only your own Frostbolt and Ice Lance crit, so the raid-support reason for skipping Fingers of Frost is gone, and frost-fingers-of-frost-raid simulates about 14% higher (645 vs 559 DPS).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arctic Reach -> Missile Barrage (+7.6% DPS); Arcane Geometry -> Arcane Impact (+0.2% DPS); Arcane Geometry -> Arcane Impact (+0.2% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Arctic Reach -> Arcane Impact (+0.2% DPS); Shatter -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Shatter -> Arctic Reach (range); Shatter -> Arctic Reach (range). Net +8.80% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Arcane Blast, Ice Barrier was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Ice Barrier -> Presence of Mind (+1.1% DPS); Arcane Blast -> Improved Channeling (interrupt). Net +1.11% on a third seed.

## Open questions (verify in the live game)

- Winter's Chill stack count (demo says 1; Classic was 5) — decides whether one dedicated WC mage is still worth it.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
