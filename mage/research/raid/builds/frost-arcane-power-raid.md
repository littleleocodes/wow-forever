# Frost — Arcane Power / Frostbolt (raid DPS) — 33/0/18

*[Mage](../../../README.md) · [Raids: training dummy, raid and parse](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/0/18 (Arcane / Fire / Frost) |
| **Role** | DPS — Raid |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |
| **Based on** | Classic baseline `frost-arcane-power-raid` |

## Summary

The Classic 31/0/20 survives: Arcane Power (+30% damage, now +30% mana cost), Presence of Mind, Arcane Instability and a stronger Arcane Mind (+10% Intellect and +100% Arcane crit damage) with Arcane Concentration and Arcane Meditation, plus Improved Frostbolt, Ice Shards, Piercing Ice and Elemental Precision — which is now 5 ranks, so Frost Channeling drops to 2.

## Point allocation

### Arcane (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Arcane Focus** | 5/5 | changed | Improves your chance to hit with Arcane spells by 5%. |
| **Arcane Concentration** | 5/5 | unchanged | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Blast** | 1/1 | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. |
| **Arcane Meditation** | 3/3 | changed | Allows 50% of your Mana regeneration to continue while casting. |
| **Missile Barrage** | 1/1 | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. |
| **Presence of Mind** | 1/1 | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. |
| **Arcane Mind** | 5/5 | changed | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |
| **Arcane Instability** | 3/3 | changed | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |
| **Arcane Power** | 1/1 | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. |
| **Arcane Impact** | 3/3 | **NEW** | Increases the critical strike chance of your Arcane spells by 6%. |
| **Improved Channeling** | 5/5 | **NEW** | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast. |

### Fire (0)

*No points.*

### Frost (18)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Frostbolt** | 5/5 | changed | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5/5 | changed | Improves your chance to hit with Frost and Fire spells by 5%. |
| **Ice Shards** | 5/5 | unchanged | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Piercing Ice** | 3/3 | unchanged | Increases the damage done by your Frost spells by 6%. |

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

**3 of 11** for `frost-raid` by training-dummy DPS in the community simulator (ElliotWood/Forever 40be98e); full ranking and the other builds' rotations: [raid README](../README.md), [raid rotations](../rotation.md).

| Rank | Build | By | Split | Dummy DPS | vs best | Raid DPS | vs best in a raid | Out of mana on the dummy |
|---|---|---|---|---|---|---|---|---|
| 1 | [`frost-fingers-of-frost-raid`](frost-fingers-of-frost-raid.md) | ours: hand draft | 22/0/29 | 640 | +0.0% | 728 | +0.0% | 0 s |
| 2 | [`opt-frost-raid-raid-dps`](opt-frost-raid-raid-dps.md) | ours: optimizer | 22/0/29 | 637 | -0.5% | 728 | -0.0% | 0 s |
| 3 | **[`frost-arcane-power-raid`](frost-arcane-power-raid.md)** | ours: hand draft | 33/0/18 | 600 | -6.2% | 690 | -5.3% | 0 s |
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

| # | Priority (the first line whose condition holds is cast) | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) casts/min |
|---|---|---|
| 1 | if mana % ≤ 80%: cast Mana Ruby (mana gem) | as ready |
| 2 | use every other cooldown when ready | as ready |
| 3 | if Missile Barrage is known and Missile Barrage is up: cast Arcane Missiles | 4.0 |
| 4 | cast Frostbolt | 20.0 |

Lines of the simulator's rotation these builds never cast: cast Evocation (its condition never held in these fights); cast Ice Lance (needs the Ice Lance talent).

Damage by ability:

| Ability | [`frost-arcane-power-raid`](frost-arcane-power-raid.md) |
|---|---|
| Frostbolt | 74% |
| Arcane Missiles | 26% |

## Notes

- Missile Barrage (Frostbolt 20% chance to make the next Arcane Missiles fast and free) could add a filler cast; treat it as a curiosity until tested.
- 2026-09-29 filler audit (raidsim/filler_audit.py, user question on zero-value fillers): points the simulator measures at 0 moved, one at a time, to talents that help in a real raid (interrupt protection, threat, mana, range, survival; the simulator cannot see these, so the order is our judgment) or that gain DPS: Arcane Geometry -> Arcane Impact (+0.4% DPS); Arcane Geometry -> Arcane Impact (+0.4% DPS); Arcane Subtlety -> Arcane Impact (+0.4% DPS); Arcane Subtlety -> Arcane Focus (+0.3% DPS); Improved Counterspell -> Arcane Focus (+0.3% DPS); Improved Counterspell -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Wand Specialization -> Improved Channeling (interrupt); Frost Channeling -> Improved Channeling (interrupt); Frost Channeling -> Improved Channeling (interrupt). Net +1.80% on a third seed.

## Open questions (verify in the live game)

- Is Arcane Instability's crit 'with all attacks' also spell crit? Demo wording is ambiguous.
- Whether the deep Frost Fingers of Frost build out-damages this — see frost-fingers-of-frost-raid.

## Sources

- <https://warcraftforever.games/talents/mage>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
