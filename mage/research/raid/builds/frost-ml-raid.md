# Frost — Raid (machine-learning search) — 21/0/30

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Frost build the machine-learning talent search found on the training dummy (only your own buffs) on 2026-10-02 in the community simulator, in the spec's phase-1 BiS gear and the rotation of the entry frost-raid (raidsim/ml_talents.py: a random forest trained on simulated builds guides a genetic search over every legal build of the spec; the finalists are raced on fresh seeds and the winner is checked against all its one-move and prerequisite-chain neighbours).

## Point allocation

### Arcane (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 2/5 | **NEW** | Gives you a 40% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 28% chance while casting Arcane Blast. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |

### Fire (0)

*No points.*

### Frost (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 1/3 | moved | Reduces the mana cost of your Frost spells by 5% and reduces the threat caused by your Frost spells by 10%. |
| **Ice Lance** | 1/1 | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. |
| **Shatter** | 3/3 | changed | Increases the critical strike chance of all your spells against Frozen targets by 50%. |
| **Fingers of Frost** | 2/2 | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |
| **Winter's Chill** | 5/5 | changed | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 5 times. |

## Rank among our builds and the community simulator's

**1 of 12** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | **[`frost-ml-raid`](frost-ml-raid.md)** | ours: hand draft | 21/0/30 | 647 | +0.0% | 739 | +0.0% | 0 s |
| 2 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 643 | -0.7% | 735 | -0.5% | 0 s |
| 3 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 22/0/29 | 643 | -0.7% | 735 | -0.5% | 0 s |
| 4 | *Frost DPS* | community simulator | - | 603 | -6.8% | 692 | -6.3% | 0 s |
| 5 | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) | ours: hand draft | 33/0/18 | 602 | -7.0% | 694 | -6.1% | 0 s |
| 6 | [`frost-winters-chill-raid`](frost-winters-chill-raid.md) | ours: hand draft | 20/0/31 | 569 | -12.2% | 651 | -11.8% | 0 s |
| 7 | [`opt-frost-raid-raid-dps-extwc`](opt-frost-raid-raid-dps-extwc.md) | ours: optimizer | 1/13/37 | 554 | -14.4% | 709 | -4.0% | 21 s |
| 8 | *Frost 14/0/37* | community simulator | - | 530 | -18.2% | 702 | -5.0% | 29 s |
| 9 | *Arcane 35/0/16* | community simulator | - | 517 | -20.2% | 596 | -19.3% | 0 s |
| 10 | *Arcane DPS* | community simulator | - | 451 | -30.3% | 514 | -30.5% | 0 s |
| 11 | *Fire 0/35/16* | community simulator | - | 408 | -37.0% | 472 | -36.1% | 0 s |
| 12 | *Fire DPS* | community simulator | - | 341 | -47.4% | 388 | -47.4% | 0 s |

## Rotation (community simulator, training dummy)

- **The training dummy:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 2 changes to the base rotation; third-seed check: ml: Frost 644 -> 647 DPS (+0.5%), ml: Hybrid Arcane/Frost 640 -> 643 DPS (+0.5%), frost-fingers-of-frost-raid 640 -> 643 DPS (+0.5%), sim preset: Frost DPS 597 -> 603 DPS (+1.1%), frost-arcane-power-raid 602 -> 603 DPS (+0.2%)):
  1. drop: if mana % < 20% and time left in the fight > 25s: cast Evocation (+0.3%)
  2. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%)
- **A fully buffed raid:** our tuned rotation (`raidsim/apl_opt.py`, 2026-10-02, 2 changes to the base rotation; third-seed check: ml: Frost 731 -> 737 DPS (+0.8%), ml: Hybrid Arcane/Frost 728 -> 735 DPS (+1.0%), frost-fingers-of-frost-raid 728 -> 735 DPS (+1.0%), sim preset: Frost DPS 687 -> 691 DPS (+0.6%), frost-arcane-power-raid 689 -> 693 DPS (+0.6%)):
  1. move down below 'if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles': if Fingers of Frost is up: cast Ice Lance (+0.2%)
  2. only with 3s or more of the fight left: cast Frostbolt + insert at the end: if mana ≥ (time left in the fight × 110): cast Fire Blast (+0.5%)

| # | Priority (the first line whose condition holds is cast) | [`frost-ml-raid`](frost-ml-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles | 3.6 |
| 4 | if Fingers of Frost is up: cast Ice Lance | 4.5 |
| 5 | cast Frostbolt | 17.8 |

Damage by ability:

| Ability | [`frost-ml-raid`](frost-ml-raid.md) |
|---|---|
| Frostbolt | 61% |
| Ice Lance | 20% |
| Arcane Missiles | 19% |

## Notes

- Against the best hand draft frost-winters-chill-raid in the same gear and fights (100,000, one seed): +13.7% (over the 2% bar: this build is the spec's raid pick, the hand draft stays as the alternative).
- Search result: 21/0/30 at 647.4 ± 0.12 DPS over 100,000 fights; runner-up 21/0/30 (+0.00%; the winner takes Improved Channeling 2; the runner-up Arcane Resilience 1, Improved Channeling 1); 1,483 builds simulated; certificate: none of its 270 one-move and chain-move neighbours was 0.1% ahead.
- Simulator numbers are the community's model of the beta (ElliotWood/Forever 40be98e with this project's patches), not in-game measurements; the talents are the simulator's answer for this gear and rotation.
- Pre-BiS gear: 21/0/30 at 627.1 DPS on the dummy (other talents: _reference/dps-rankings.md).

## Open questions (verify in the live game)

- A machine-searched Frost build: check it against the community's Frost builds at launch.

## Sources

- <https://github.com/ElliotWood/Forever>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
