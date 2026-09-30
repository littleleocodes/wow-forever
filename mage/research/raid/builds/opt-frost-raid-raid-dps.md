# Optimizer — Raid Frostbolt with Ice Lance on Fingers of Frost charges (the ice_lance source, 2026-09-27) (raid-dps) — 22/0/29

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 22/0/29 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `frost-raid` and profile `raid-dps`: score +75.7% (DPS gain vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Arcane (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Wand Specialization** | 1/2 | moved | Increases your damage with Wands by 13%. |
| **Arcane Subtlety** | 2/2 | changed | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 1/5 | changed | Increases your Intellect by 2% and increases the critical strike damage bonus of your Arcane spells by 20%. |

### Fire (0)

*No points.*

### Frost (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Improved Cone of Cold** | 1/3 | changed | Increases the damage dealt by your Cone of Cold spell by 12%. |
| **Winter's Chill** | 4/5 | changed | Gives your Frost damage spells a 80% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 4 times. |

## Core talents (priority order)

1. **Improved Frostbolt** — Removing it costs 22.3 points of score in this model.
2. **Ice Shards** — Removing it costs 20.1 points of score in this model.
3. **Fingers of Frost** — Removing it costs 19.5 points of score in this model.
4. **Ice Lance** — Removing it costs 12.3 points of score in this model.
5. **Winter's Chill** — Removing it costs 11.4 points of score in this model.
6. **Shatter** — Removing it costs 11.1 points of score in this model.
7. **Piercing Ice** — Removing it costs 8.7 points of score in this model.
8. **Elemental Precision** — Removing it costs 8.6 points of score in this model.

## Rank among our builds and the community simulator's

**2 of 11** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 640 | +0.0% | 728 | +0.0% | 0 s |
| 2 | **[`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md)** | ours: optimizer | 22/0/29 | 637 | -0.5% | 728 | -0.0% | 0 s |
| 3 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 33/0/18 | 600 | -6.2% | 690 | -5.3% | 0 s |
| 4 | *Frost DPS* | community simulator | - | 597 | -6.8% | 688 | -5.5% | 0 s |
| 5 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 1/13/37 | 591 | -7.7% | 705 | -3.2% | 0 s |
| 6 | *Frost 14/0/37* | community simulator | - | 585 | -8.6% | 697 | -4.2% | 0 s |
| 7 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 20/0/31 | 569 | -11.2% | 647 | -11.1% | 0 s |
| 8 | *Arcane 35/0/16* | community simulator | - | 517 | -19.2% | 592 | -18.7% | 0 s |
| 9 | *Arcane DPS* | community simulator | - | 451 | -29.5% | 510 | -30.0% | 0 s |
| 10 | *Fire 0/35/16* | community simulator | - | 402 | -37.2% | 467 | -35.9% | 0 s |
| 11 | *Fire DPS* | community simulator | - | 340 | -46.9% | 383 | -47.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-29).
- **A fully buffed raid:** the simulator's own rotation: no single change (and no pair of changes) beat it on two seeds (`raidsim/apl_opt.py`, 2026-09-29).

| # | Priority (the first line whose condition holds is cast) | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Fingers of Frost is up: cast Ice Lance | 4.5 |
| 4 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles | 3.5 |
| 5 | cast Frostbolt | 17.7 |

Lines of the simulator's rotation these builds never cast: cast Evocation (its condition never held in these fights).

Damage by ability:

| Ability | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) |
|---|---|
| Frostbolt | 60% |
| Ice Lance | 20% |
| Arcane Missiles | 19% |

## Notes

- Allocation taken from cand-frost-raid-r1 on 2026-09-30: the optimizer's earlier round beat its last export in the community simulator (637 vs 607 DPS; the calibration moved the model past the better build).
- Report: mage/research/talents/forever/optimizer/frost-raid-raid-dps.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
