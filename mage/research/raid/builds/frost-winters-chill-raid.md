# Frost — Winter's Chill (raid support) — 21/0/30

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `frost-winters-chill-raid` |

## Summary

Winter's Chill now buffs Frostbolt and Ice Lance crit (demo text says it stacks once — likely a transcription artefact; Classic stacked to 5), Ice Block moved to tier 4 and Cold Snap to tier 5, Shatter is 3 ranks. The 17/0/34 shape still fits with Elemental Precision at 5 ranks.

## Point allocation

### Arcane (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 1/3 | changed | Increases your Armor by an amount equal to 25% of your Intellect. |
| **Improved Channeling** | 4/5 | **NEW** | Gives your Arcane Missiles spell a 80% chance and your Arcane Blast and Arcane Wrath spells a 56% chance to not lose casting time when you take damage. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 1/2 | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 2/3 | changed | Allows 33% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |

### Fire (0)

*No points.*

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Frostbite** | 3/3 | moved | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Winter's Chill** | 5/5 | changed | Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 100% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times. |

## Core talents (priority order)

1. **Winter's Chill** — 100% chance at max rank to apply the crit debuff for Frostbolt/Ice Lance — the raid-support reason for the build.
2. **Ice Shards** — Frostbolt crit damage.
3. **Improved Frostbolt** — Cast time.
4. **Ice Block** — Now the 16-point Frost talent — cheap immunity.
5. **Frost Channeling** — Mana and threat.
6. **Arcane Meditation** — Regen while casting (2/3).

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 2 | Arcane Meditation 2 | Arcane Meditation 3 with Arcane Blast 0 | Regen vs. filler. |

## Rank among our builds and the community simulator's

**8 of 14** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 17/2/32 | 670 | +0.0% | 800 | +0.0% | 0 s |
| 2 | [`frost-med-raid`](frost-med-raid.md) | ours: derived (simulator preset) | 18/0/33 | 648 | -3.3% | 796 | -0.4% | 6 s |
| 3 | *Frost Med* | community simulator | - | 648 | -3.3% | 796 | -0.4% | 6 s |
| 4 | *Frost Incin* | community simulator | - | 627 | -6.4% | 781 | -2.3% | 12 s |
| 5 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 530 | -20.8% | 598 | -25.2% | 0 s |
| 6 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 528 | -21.1% | 623 | -22.2% | 0 s |
| 7 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 514 | -23.3% | 599 | -25.2% | 0 s |
| 8 | **[`frost-winters-chill-raid`](frost-winters-chill-raid.md)** | ours: hand draft | 21/0/30 | 452 | -32.5% | 505 | -36.9% | 0 s |
| 9 | *FFB* | community simulator | - | 409 | -38.9% | 466 | -41.7% | 0 s |
| 10 | *Arcane* | community simulator | - | 357 | -46.8% | 374 | -53.3% | 0 s |
| 11 | *Arcane Fire* | community simulator | - | 357 | -46.8% | 374 | -53.3% | 0 s |
| 12 | *Fire Skyborne GT 180* | community simulator | - | 325 | -51.5% | 357 | -55.4% | 0 s |
| 13 | *Fire* | community simulator | - | 325 | -51.5% | 357 | -55.4% | 0 s |
| 14 | *Fire Skyborne LT 180* | community simulator | - | 325 | -51.5% | 357 | -55.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 6 passes, the last 2026-11-20, 13 changes to the base rotation; third-seed check: ml: Frost 680 -> 686 DPS (+1.0%), opt-frost-raid-raid-dps-extwc 521 -> 530 DPS (+1.6%), sim preset: Frost Incin 573 -> 626 DPS (+9.3%), frost-winters-chill-raid 358 -> 452 DPS (+26.3%), frost-fingers-of-frost-raid 525 -> 529 DPS (+0.7%), opt-frost-raid-raid-dps 507 -> 514 DPS (+1.2%), frost-ml-raid 583 -> 601 DPS (+3.2%)):
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
  13. drop the condition: if Fingers of Frost is up: use every other cooldown when ready (+1.0%, pass 6)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 12 passes, the last 2026-11-20, 6 changes to the base rotation; third-seed check: ml: Frost 816 -> 816 DPS (+0.0%), opt-frost-raid-raid-dps 598 -> 598 DPS (+0.0%), sim preset: Arcane 374 -> 374 DPS (+0.0%), frost-winters-chill-raid 504 -> 504 DPS (+0.0%), frost-fingers-of-frost-raid 622 -> 622 DPS (+0.0%), opt-frost-raid-raid-dps-extwc 599 -> 599 DPS (+0.0%), frost-ml-raid 718 -> 718 DPS (+0.0%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%, pass 1)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%, pass 1)
  3. spell probe: insert in the middle: cast Arcane Wrath (+1.0%, pass 6)
  4. insert at the top: if (time left on Arcane Blast < cast time of Arcane Blast or stacks of Arcane Blast < 2): cast Arcane Blast (+6.1%, pass 7)
  5. move to the top: if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles (rank 7) (+2.2%, pass 7)
  6. only with 20s or more of the fight left: cast Arcane Wrath (+0.4%, pass 7)

Before the pull: cast Ice Barrier; cast Frostbolt (rank 10).

| # | Priority (the first line whose condition holds is cast) | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 5%: channel Evocation (stop it when mana % ≥ 99%) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if number of targets ≥ 3 and stacks of Fingers of Frost on you ≥ 1: cast Cone of Cold | 3.9 |
| 4 | if number of targets ≥ 3 and time until Cone of Cold is ready ≥ 5: cast Cold Snap | 0.3 |
| 5 | if time until Cone of Cold is ready ≥ 7: cast Cold Snap | 0.3 |
| 6 | if stacks of Winter's Chill on the target = 5: cast Cone of Cold | 3.9 |
| 7 | cast Frostbolt (rank 10) | 20.9 |

Lines of the simulator's rotation these builds never cast: cast Read Leyline, cast Blizzard (its condition never held in these fights); cast Ice Lance (needs the Ice Lance talent); cast Ice Barrier (needs the Ice Barrier talent).

Damage by ability:

| Ability | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) |
|---|---|
| Frostbolt | 78% |
| Cone of Cold | 21% |
| Demonic Rune | 1% |

## Notes

- Ice Lance + Fingers of Frost are not taken here; they need 3 more Frost points (see the Fingers of Frost build).
- 2026-09-27 scenario audit: Improved Frost Nova 2 -> Arctic Reach 2. Improved Frost Nova shortens a root's cooldown: control a raid boss ignores (simulator 0.0%). Arctic Reach 2/2 adds range. This draft is superseded in Forever: the beta Winter's Chill raises only your own Frostbolt and Ice Lance crit, so the raid-support reason for skipping Fingers of Frost is gone, and frost-fingers-of-frost-raid simulates about 14% higher (645 vs 559 DPS).
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arctic Reach -> Missile Barrage (+7.6% DPS); Arcane Geometry -> Arcane Impact (+0.2% DPS); Arcane Geometry -> Arcane Impact (+0.2% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Arctic Reach -> Arcane Impact (+0.2% DPS); Shatter -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Shatter -> Arctic Reach (range); Shatter -> Arctic Reach (range). Net +8.80% on a third seed.
- 2026-10-02 filler audit (raidsim/filler_audit.py, user question on zero-value fillers; 2026-10-02 user report on talents whose ability the rotation never casts: Arcane Blast, Ice Barrier was never cast here): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Ice Barrier -> Presence of Mind (+1.1% DPS); Arcane Blast -> Improved Channeling (interrupt). Net +1.11% on a third seed.
- 2026-10-22 (repair_builds.py, client build 70425 trees): 21/0/30 -> 21/0/30; Elemental Precision 5 -> 3 (rank cap); Piercing Ice 3 gone; +1 Frost Warding (tier gating for Cold Snap); +1 Frost Warding (tier gating for Winter's Chill); +1 Frostbite (tier gating for Winter's Chill); +1 Frostbite (tier gating for Winter's Chill); +1 Frostbite (tier gating for Winter's Chill) (refill: the frost-raid model, raid-dps).
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 21/0/30 -> 21/0/30; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Missile Barrage (tier gating for Arcane Meditation); +1 Arcane Subtlety (tier gating for Presence of Mind); +1 Arcane Subtlety (tier gating for Presence of Mind); +1 Magic Absorption (tier gating for Presence of Mind) (refill: the frost-raid model, raid-dps).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Elemental Precision, Piercing Ice; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Winter's Chill stack count (demo says 1; Classic was 5) — decides whether one dedicated WC mage is still worth it.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
