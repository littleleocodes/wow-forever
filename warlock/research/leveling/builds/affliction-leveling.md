# Affliction — Leveling (derived) — 33/6/12

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 33/6/12 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Affliction leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Affliction build, 30+ points kept in Affliction, playing the affliction-leveling rotation; the talent order is the stats model's (affliction-leveling).

## Point allocation

### Affliction (33)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Drains** | 3/3 | **NEW** | Increases health drained or damage done by your Drain Life, Drain Soul, and Wrack spells by 20%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 50%. Lasts 30 sec. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Soul Siphon** | 3/3 | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 12% per each of your other Affliction effects active on the target, up to a maximum increase of 36%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 10%. |

### Demonology (6)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Energies** | 1/2 | **NEW** | You heal your pet for 8% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 50% of the Mana you gain. |

### Destruction (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Molten Skin** | 5/5 | **NEW** | Reduces all damage taken by 10%. |
| **Ruin** | 2/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 40%. |

## Core talents (priority order)

1. **Siphon Life** — The scorer's value in this build: +33.8% of its score (model affliction-leveling).
2. **Shadow Mastery** — The scorer's value in this build: +8.4% of its score (model affliction-leveling).
3. **Improved Corruption** — The scorer's value in this build: +7.2% of its score (model affliction-leveling).
4. **Molten Skin** — The scorer's value in this build: +6.2% of its score (model affliction-leveling).
5. **Pandemic** — The scorer's value in this build: +5.9% of its score (model affliction-leveling).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start derived-affliction-scorer, moves: 1 point Aftermath -> Demonic Energies. Race against affliction-leveling over levels 20-60 (seed 3, 3000 fights per level): +0.4% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 35/6/10 -> 33/6/12; Malediction 5 gone; refill +3 Improved Drains, +2 Ruin; order dropped (order_repair.py) (refill: the affliction-leveling model, leveling-st).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Malediction dropped (not in the allocation; Malediction was replaced by Grim Reach in 70425).

## Open questions (verify in the live game)

- A derived Affliction leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
