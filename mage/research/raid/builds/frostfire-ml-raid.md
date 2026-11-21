# Frostfire — Raid (machine-learning search) — 0/29/22

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/29/22 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frostfire build the machine-learning talent search found in a full raid (every raid buff and debuff: the group setting) on 2026-10-29 in the community simulator, in the spec's phase-1 BiS gear and the raid rotation of the entry frostfire-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Arcane (0)

*No points.*

### Fire (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Accelerant** | 5/5 | changed | Reduces the casting time of your Fireball, Frostfire Bolt, and Arcane Wrath spells by 0.5 sec. |
| **Incineration** | 3/5 | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Ignite** | 5/5 | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Improved Fire Blast** | 2/2 | **NEW** | Reduces the cooldown of your Fire Blast spell by 2 sec and increases its range by 15 yards. |
| **Pyroblast** | 1/1 | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. |
| **Heating Up** | 1/1 | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. Fire Blast grants an additional stack every time it deals damage. |
| **Improved Scorch** | 3/3 | changed | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Master of Elements** | 3/3 | changed | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |
| **Critical Mass** | 3/3 | unchanged | Increases the critical strike chance of your Fire spells by 6%. |
| **Fire Power** | 3/3 | unchanged | Increases the damage done by your Fire spells by 3% per your Fire effects on the target, up to a maximum increase of 12%. Effects which mix multiple schools of magic do not qualify. |

### Frost (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Frost Warding** | 2/2 | changed | Increases the Armor and resistances granted by your Frost Armor and Ice Armor spells by 30%, gives your Frost Ward a 20% chance to negate the warded damage spell, and increases the amount absorbed by your Ice Barrier and Frost Ward by 20%. |
| **Improved Frostbolt** | 1/5 | changed | Reduces the casting time of your Frostbolt spell by 0.1 sec. |
| **Precision** | 3/3 | changed | Improves your chance to hit with all spells by 6%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Frost Channeling** | 3/3 | moved | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Arctic Reach** | 1/2 | unchanged | Increases the range of your Frostbolt, Ice Lance, and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. |
| **Ice Block** | 1/1 | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

## Rank among our builds and the community simulator's

**2 of 5** for `frostfire-raid` by training-dummy DPS in the community simulator (wowsims/forever 2e6e77d (client 70938)); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frostfire-fingers-of-frost-raid`](frostfire-fingers-of-frost-raid.md) | ours: hand draft | 0/29/22 | 532 | +0.0% | 768 | -1.8% | 38 s |
| 2 | **[`frostfire-ml-raid`](frostfire-ml-raid.md)** | ours: derived (ML search) | 0/29/22 | 527 | -0.9% | 778 | -0.4% | 42 s |
| 3 | [`frostfire-raid`](frostfire-raid.md) | ours: hand draft | 7/31/13 | 505 | -5.1% | 704 | -9.9% | 35 s |
| 4 | [`frostfire-ffb-raid`](frostfire-ffb-raid.md) | ours: derived (simulator preset) | 0/29/22 | 501 | -5.9% | 781 | +0.0% | 50 s |
| 5 | *FFB* | community simulator | - | 501 | -5.9% | 781 | +0.0% | 50 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** the entry's base rotation (`_reference/data/raidsim/apls/mage/upstream/ffb.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-24 (18 changes, `frostfire-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.
- **A fully buffed raid:** the entry's base rotation (`_reference/data/raidsim/apls/mage/upstream/ffb.apl.json`), untuned. The rotation search of 2026-09-28 to 2026-10-31 (37 changes, `frostfire-raid-rotation-search.json`) tuned an earlier base that this entry no longer plays.

Before the pull: cast Pyroblast.

| # | Priority (the first line whose condition holds is cast) | [`frostfire-ml-raid`](frostfire-ml-raid.md) casts/min |
|---|---|---|
| 1 | if mana < current cost and (not Read Leyline is known or not Read Leyline is ready or Energized is up): channel Evocation (stop it when mana % ≥ 99%) | as ready |
| 2 | if (stacks of Fire Vulnerability on the target < 5 or time left on Fire Vulnerability < 5) and (stacks of Fire Vulnerability on the target < 4 or not Scorch is being cast): cast Scorch | 4.3 |
| 3 | if stacks of Fire Vulnerability on the target = 5: use every other cooldown when ready | as ready |
| 4 | if stacks of Heating Up on you = 3 and not Pyroblast is being cast: cast Pyroblast | 3.1 |
| 5 | if stacks of Fingers of Frost on you < 2: cast Fire Blast | 5.4 |
| 6 | cast Frostfire Bolt | 10.4 |

Lines of the simulator's rotation these builds never cast: strict sequence: cast Read Leyline; channel Evocation (stop it when mana % ≥ 99%) (its condition never held in these fights).

Damage by ability:

| Ability | [`frostfire-ml-raid`](frostfire-ml-raid.md) |
|---|---|
| Frostfire Bolt | 40% |
| Pyroblast | 22% |
| Fire Blast | 17% |
| Ignite | 12% |
| Scorch | 8% |
| Demonic Rune | 1% |

## Notes

- Against the best hand draft frostfire-fingers-of-frost-raid in a full raid, same gear and fights (100,000, one seed): +6.4% (over the replacement bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Where the simulator measured no difference, the points follow frostfire-fingers-of-frost-raid: Permafrost → Frost Warding, Improved Blizzard → Arctic Reach, Improved Blizzard → Ice Block (the same DPS as the search winner 0/29/22 on one seed, 30,000 fights).
- Search result (full raid): 0/29/22 at 793.4 ± 0.17 DPS over 100,000 fights; runner-up 0/29/22 (+0.15%; the winner takes Permafrost 1; the runner-up Frostbite 1); 2,324 builds simulated; certificate: 1 confirmed move first, then none of its 347 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (wowsims/forever 30f67f5 (client 70450) with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 0/29/22 at 789.2 DPS in a full raid (other talents: _reference/dps-rankings.md).
- Alone on the training dummy (only your own buffs) the search's best is 10/28/13 at 497.0 DPS.
- 2026-10-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Improved Fire Blast -> Master of Elements (+0.7% DPS). Net +0.65% on a third seed.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 0/29/22 -> 0/29/22; Improved Fireball -> Accelerant (renamed); Critical Mass 5 -> 3 (rank cap); Elemental Precision -> Precision (renamed); +1 Master of Elements (tier gating for Fire Power); refill +1 Improved Fire Blast (refill: the fire-raid model, raid-dps).

## Open questions (verify in the live game)

- A machine-searched Frostfire build: check it against the community's Frostfire builds at launch.

## Sources

- <https://github.com/wowsims/forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
