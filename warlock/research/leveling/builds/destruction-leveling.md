# Destruction — Leveling (derived) — 21/0/30

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/0/30 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Destruction leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Destruction build, 30+ points kept in Destruction, playing the destruction-leveling rotation; the talent order is the stats model's (affliction-leveling).

## Point allocation

### Affliction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 4/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 4%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |

### Demonology (0)

*No points.*

### Destruction (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Destructive Reach** | 2/2 | changed | Increases the range of your Destruction spells by 20%. |
| **Aftermath** | 5/5 | changed | Increases the initial damage of your Immolate spell by 50% and your Conflagrate spell has a 100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Molten Skin** | 5/5 | **NEW** | Reduces all damage taken by 10%. |
| **Ruin** | 5/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1/1 | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. |
| **Intensity** | 3/3 | changed | Gives your Destruction spells a 70% chance to not lose casting time when you take damage. |
| **Fire and Brimstone** | 1/3 | **NEW** | Increases the critical strike chance of your Conflagrate spell by 8%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Affliction | Improved Corruption | 5 | 5/0/0 |
| 15-19 | Affliction | Suppression | 5 | 10/0/0 |
| 20 | Affliction | Amplify Curse | 1 | 11/0/0 |
| 21-22 | Affliction | Improved Bane of Agony | 2 | 13/0/0 |
| 23-25 | Affliction | Pandemic | 3 | 16/0/0 |
| 26-29 | Affliction | Malevolence | 4 | 20/0/0 |
| 30 | Affliction | Siphon Life | 1 | 21/0/0 |
| 31-35 | Destruction | Bane | 5 | 21/0/5 |
| 36-40 | Destruction | Molten Skin | 5 | 21/0/10 |
| 41-45 | Destruction | Aftermath | 5 | 21/0/15 |
| 46-48 | Destruction | Agonizing Flames | 3 | 21/0/18 |
| 49-53 | Destruction | Ruin | 5 | 21/0/23 |
| 54-55 | Destruction | Destructive Reach | 2 | 21/0/25 |
| 56 | Destruction | Conflagrate | 1 | 21/0/26 |
| 57-59 | Destruction | Intensity | 3 | 21/0/29 |
| 60 | Destruction | Fire and Brimstone | 1 | 21/0/30 |

## Core talents (priority order)

1. **Siphon Life** — The scorer's value in this build: +42.7% of its score (model affliction-leveling).
2. **Improved Corruption** — The scorer's value in this build: +8.7% of its score (model affliction-leveling).
3. **Molten Skin** — The scorer's value in this build: +7.9% of its score (model affliction-leveling).
4. **Pandemic** — The scorer's value in this build: +6.9% of its score (model affliction-leveling).
5. **Malevolence** — The scorer's value in this build: +5.2% of its score (model affliction-leveling).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start destruction-leveling, moves: 1 point Shadowburn -> Fire and Brimstone. Race against destruction-leveling over levels 20-60 (seed 3, 3000 fights per level): +0.4% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 21/0/30 -> 21/0/30; Malediction 5 gone; +1 Suppression (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); order dropped (order_repair.py) (refill: the affliction-leveling model, leveling-st).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Malediction dropped (not in the allocation; Malediction was replaced by Grim Reach in 70425).
- 2026-10-18 (order_repair.py, page audit C1): the order lost in the 2026-10-03 repair is the fastest of three the fight lab raced (the destruction-leveling rotation, seed 3, 3000 fights per level, levels 20-60 weighted by level): stats model 37.8 s per kill; own tree first 39.0 s; own tree last 37.8 s.

## Open questions (verify in the live game)

- A derived Destruction leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
