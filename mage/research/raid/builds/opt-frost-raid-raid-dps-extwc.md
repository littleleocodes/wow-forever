# Optimizer — Raid Frostbolt with Ice Lance on Fingers of Frost charges (the ice_lance source, 2026-09-27) (raid-dps-extwc) — 28/1/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 28/1/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-raid` and profile `raid-dps-extwc`: score +87.5% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (28)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Missile Barrage** | 2/2 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Arcane Wrath, Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 34 to 38 Arcane damage. Each time you cast Arcane Blast, you gain 12% of your Intellect as Spell Damage and the mana cost of Arcane Blast is increased by 100%. Effect stacks up to 4 times and lasts 18 sec from time of initial application. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Meditation** | 1/3 | changed | Allows 17% of your Mana regeneration to continue while casting. |
| **Arcane Wrath** | 1/1 | **NEW** | Launches a projectile of pure Arcane energy at the enemy target, causing 122 to 146 Arcane damage. This spell gains additional Spell Damage equal to 5% of your maximum Mana. |
| **Arcane Mind** | 4/5 | changed | Increases your Intellect by 8% and increases the critical strike damage bonus of your Arcane spells by 80%. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Fire (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Incineration** | 1/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 2%. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Core talents (priority order)

1. **Improved Frostbolt** — Removing it costs 22.1 points of score in this model.
2. **Fingers of Frost** — Removing it costs 19.4 points of score in this model.
3. **Ice Shards** — Removing it costs 16.7 points of score in this model.
4. **Ice Lance** — Removing it costs 12.5 points of score in this model.
5. **Missile Barrage** — Removing it costs 12.0 points of score in this model.
6. **Shatter** — Removing it costs 11.3 points of score in this model.
7. **Arcane Instability** — Removing it costs 9.5 points of score in this model.

## Rank among our builds and the community simulator's

**5 of 14** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 17/2/32 | 670 | +0.0% | 800 | +0.0% | 0 s |
| 2 | [`frost-med-raid`](frost-med-raid.md) | ours: derived (simulator preset) | 18/0/33 | 648 | -3.3% | 796 | -0.4% | 6 s |
| 3 | *Frost Med* | community simulator | - | 648 | -3.3% | 796 | -0.4% | 6 s |
| 4 | *Frost Incin* | community simulator | - | 627 | -6.4% | 781 | -2.3% | 12 s |
| 5 | **[`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md)** | ours: optimizer | 28/1/22 | 530 | -20.8% | 598 | -25.2% | 0 s |
| 6 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 528 | -21.1% | 623 | -22.2% | 0 s |
| 7 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 29/0/22 | 514 | -23.3% | 599 | -25.2% | 0 s |
| 8 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 21/0/30 | 452 | -32.5% | 505 | -36.9% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 5%: channel Evocation (interrupt it when a higher line is ready) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if number of targets ≥ 3 and stacks of Fingers of Frost ≥ 1: cast Ice Lance | 2.5 |
| 4 | if stacks of Fingers of Frost = 1 and spellIsCasting: cast Ice Lance | 2.5 |
| 5 | cast Frostbolt (rank 10) | 22.9 |

Lines of the simulator's rotation these builds never cast: cast Read Leyline, cast Cone of Cold, cast Blizzard (its condition never held in these fights); cast Cold Snap (needs the Cold Snap talent); cast Ice Barrier (needs the Ice Barrier talent).

Damage by ability:

| Ability | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) |
|---|---|
| Frostbolt | 86% |
| Ice Lance | 13% |
| Demonic Rune | 1% |

## Notes

- Report: mage/research/talents/forever/optimizer/frost-raid-raid-dps-extwc.md
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 28/1/22 -> 28/1/22; Arcane Focus 5 gone; Elemental Precision -> Precision (renamed); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Arcane Resilience (tier gating for Arcane Concentration); +1 Wand Specialization (tier gating for Arcane Concentration); +1 Wand Specialization (tier gating for Arcane Concentration) (refill: the frost-raid model, raid-dps-extwc).
- 2026-11-09 page audit: core entries for talents the allocation no longer holds removed (Elemental Precision; a tree change or a repair took them out).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
