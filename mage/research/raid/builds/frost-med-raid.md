# Frost — Winter's Chill and Cone of Cold (the simulator's own build) — 18/0/33

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 18/0/33 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The official wowsims/forever simulator's own Frost build (Frost Med, 18/0/33) for its frost rotation: Frostbolt and Fingers of Frost's Ice Lance stack Winter's Chill on the boss, Cone of Cold spends the stacks (with Improved Cone of Cold), Ice Barrier keeps Frigid Power up, Arcane Meditation holds the mana. Stand within 10 yards of the boss: Cone of Cold is a 10-yard cone (12 with Arctic Reach).

## Point allocation

### Arcane (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Wand Specialization** | 2/2 | moved | Increases your damage with Wands by 25%. |
| **Arcane Resilience** | 3/3 | changed | Increases your Armor by an amount equal to 75% of your Intellect. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2/2 | changed | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Geometry** | 1/2 | **NEW** | Increases the range of your Arcane spells by 3 yards. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |

### Fire (0)

*No points.*

### Frost (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Improved Blizzard** | 1/3 | changed | Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 15% for 1.5 sec. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 2/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Improved Cone of Cold** | 3/3 | changed | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Cold Snap** | 1/1 | changed | Finishes the remaining cooldown on all your other Frost spells. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 5/5 | changed | Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 100% chance to apply Winter's Chill, increasing the target's damage taken from your next Cone of Cold by 20% and it gains an additional 7% of your spell damage, stacking up to 5 times. |
| **Ice Barrier** | 1/1 | changed | Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min. While shielded, your Frost damage is increased by an additional 5% and you do not lose casting time when you take damage. |

## Core talents (priority order)

1. **Ice Barrier** — Shield yourself, absorbing 447 damage and increasing your Frost damage by 15% for 1 min
2. **Winter's Chill** — Gives your Frostbolt and Fingers of Frost empowered Ice Lance spells a 100% chance to apply Winter's Chill, increasing the target's damage taken from 
3. **Improved Cone of Cold** — Increases the damage dealt by your Cone of Cold spell by 35%
4. **Fingers of Frost** — Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen
5. **Cold Snap** — Finishes the remaining cooldown on all your other Frost spells

## Rank among our builds and the community simulator's

**2 of 14** for `frost-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-ml-raid`](frost-ml-raid.md) | ours: derived (ML search) | 17/2/32 | 670 | +0.0% | 800 | +0.0% | 0 s |
| 2 | **[`frost-med-raid`](frost-med-raid.md)** | ours: derived (simulator preset) | 18/0/33 | 648 | -3.3% | 796 | -0.4% | 6 s |
| 3 | *Frost Med* | community simulator | - | 648 | -3.3% | 796 | -0.4% | 6 s |
| 4 | *Frost Incin* | community simulator | - | 627 | -6.4% | 781 | -2.3% | 12 s |
| 5 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 28/1/22 | 530 | -20.8% | 598 | -25.2% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`frost-med-raid`](frost-med-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 5%: channel Evocation (interrupt it when a higher line is ready) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if number of targets ≥ 3 and stacks of Fingers of Frost ≥ 1: cast Cone of Cold | 3.6 |
| 4 | if number of targets ≥ 3 and stacks of Fingers of Frost ≥ 1: cast Ice Lance | 1.7 |
| 5 | if number of targets ≥ 3 and time until Cone of Cold is ready ≥ 5: cast Cold Snap | 0.3 |
| 6 | if number of targets ≥ 3 and auraIsInactive: cast Ice Barrier | 1.3 |
| 7 | if time until Cone of Cold is ready ≥ 7: cast Cold Snap | 0.3 |
| 8 | if stacks of Winter's Chill = 5: cast Cone of Cold | 3.6 |
| 9 | if stacks of Fingers of Frost = 1 and spellIsCasting: cast Ice Lance | 1.7 |
| 10 | if time left on Frigid Power ≤ 3: cast Ice Barrier | 1.3 |
| 11 | cast Frostbolt (rank 10) | 18.7 |

Lines of the simulator's rotation these builds never cast: cast Read Leyline, cast Blizzard (its condition never held in these fights).

Damage by ability:

| Ability | [`frost-med-raid`](frost-med-raid.md) |
|---|---|
| Frostbolt | 67% |
| Cone of Cold | 25% |
| Ice Lance | 8% |
| Demonic Rune | 0% |

## Notes

- The simulator's own build, credited (Simulator build first, 2026-11-20): the page starts from it; ours replaces it only when 0.5% ahead on two seeds and passing the spec's rules.
- Simulator numbers are the community's model of the game, not in-game measurements.

## Sources

- <https://github.com/wowsims/forever/blob/2e6e77d84/ui/specs/mage/dps/presets.ts>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
