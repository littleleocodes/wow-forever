# Frost — Raid (machine-learning search) — 21/0/30

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost build the machine-learning talent search found on the training dummy (only your own buffs) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry frost-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Arcane (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 3/5 | **NEW** | Gives you a 60% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 42% chance while casting Arcane Blast or Arcane Wrath. |
| **Missile Barrage** | 1/2 | **NEW** | Gives your Arcane Blast spell a 20% chance, your Arcane Missile hits a 5% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 10% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |

### Fire (0)

*No points.*

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Elemental Precision** | 3/3 | changed | Improves your chance to hit with Frost and Fire spells by 6%. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt and Frost Blast spells by 0.5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 200% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Frost Blast, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 5/5 | changed | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the damage done by your Cone of Cold spell to the target by 40%, stacking up to 5 times. |

## Rank among our builds and the community simulator's

**8 of 11** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 30f67f5 (client 70450)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 587 | +0.0% | 680 | -1.8% | 9 s |
| 2 | *Arcane Frost* | community simulator | - | 582 | -0.9% | 693 | +0.0% | 8 s |
| 3 | [`arcane-frost-open-raid`](arcane-frost-open-raid.md) | ours: derived (open search) | 29/0/22 | 577 | -1.7% | 693 | -0.0% | 7 s |
| 4 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 35/0/16 | 577 | -1.7% | 676 | -2.4% | 5 s |
| 5 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 549 | -6.4% | 628 | -9.3% | 4 s |
| 6 | *Arcane Fire* | community simulator | - | 521 | -11.2% | 645 | -6.8% | 2 s |
| 7 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 484 | -17.5% | 547 | -21.0% | 0 s |
| 8 | **[`frost-ml-raid`](frost-ml-raid.md)** | ours: derived (ML search) | 21/0/30 | 482 | -17.9% | 544 | -21.4% | 0 s |
| 9 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 441 | -24.8% | 501 | -27.7% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`frost-ml-raid`](frost-ml-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 60% and mana % ≥ 60%: cast Mana Ruby | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Fingers of Frost is up: cast Ice Lance | 2.9 |
| 4 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) | 2.0 |
| 5 | if Arcane Wrath is ready: cast Presence of Mind | 0.3 |
| 6 | if time left in the fight ≥ 3s: cast Frostbolt (rank 10) | 20.2 |
| 7 | if (Clearcasting is up or mana % ≥ 10%): cast Fire Blast | 0.3 |
| 8 | cast Robe of the Archmage | as ready |
| 9 | cast Frost Blast | 0.1 |

Lines of the simulator's rotation these builds never cast: cast Arcane Blast (needs the Arcane Blast talent); cast Evocation (its condition never held in these fights).

Damage by ability:

| Ability | [`frost-ml-raid`](frost-ml-raid.md) |
|---|---|
| Frostbolt | 74% |
| Arcane Missiles | 13% |
| Ice Lance | 11% |
| Demonic Rune | 2% |
| Fire Blast | 1% |
| Frost Blast | 0% |

## Notes

- Against the best hand draft frost-winters-chill-raid in the same gear and fights (100,000, one seed): +13.7% (over the 2% bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Search result: 21/0/30 at 647.4 ± 0.12 DPS over 100,000 fights; runner-up 21/0/30 (+0.00%; the winner takes Improved Channeling 2; the runner-up Arcane Resilience 1, Improved Channeling 1); 1,483 builds simulated; certificate: none of its 270 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 21/0/30 at 627.1 DPS on the dummy (other talents: _reference/dps-rankings.md).
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Arcane Blast was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Blast -> Improved Channeling (interrupt). Net +0.00% on a third seed.
- 2026-10-15: the 70291 machine-learning search (ElliotWood/Forever 2ce8265 with this project's patches, ml_pipeline.py --fresh) confirms this build for Frost: its full-raid winner is +0.15% against it, under the 0.5% bar for a new build.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 21/0/30 -> 21/0/30; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; +1 Ice Block (tier gating for Fingers of Frost); +1 Frost Channeling (tier gating for Fingers of Frost); +1 Frost Channeling (tier gating for Winter's Chill); +1 Arctic Reach (tier gating for Winter's Chill); +1 Arctic Reach (tier gating for Winter's Chill) (refill: the frost-raid model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Frost build: check it against the community's Frost builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
