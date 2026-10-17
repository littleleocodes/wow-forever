# Demonology — Leveling (derived) — 21/30/0

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Demonology leveling build derived on 2026-09-30 (derive_leveling.py): searched in the fight lab at level 60 from the fastest of the spec's builds and the stats model's best Demonology build, 30+ points kept in Demonology, playing the demonology-leveling rotation; the talent order is the stats model's (affliction-leveling).

## Point allocation

### Affliction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 3/5 | changed | Improves your chance to hit by 3% and reduces all threat you generate by 12%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 50%. Lasts 30 sec. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 4/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 4%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |

### Demonology (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 2/5 | changed | Increases your total Stamina by 6%. |
| **Improved Imp** | 3/3 | changed | Increases the damage of your Imp's Firebolt spell by 30% and the effect of its Fire Shield spell by 30%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Demonic Brand** | 3/3 | **NEW** | Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Master Demonologist** | 5/5 | changed | Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 10%.  Voidwalker - Reduces Physical damage taken by 10%.  Succubus/Incubus - Increases Shadow damage done by 10%.  Felhunter - Reduces Magic damage taken by 10%. |

### Destruction (0)

*No points.*

## Core talents (priority order)

1. **Siphon Life** — The scorer's value in this build: +35.1% of its score (model affliction-leveling).
2. **Demonic Knowledge** — The scorer's value in this build: +16.1% of its score (model affliction-leveling).
3. **Soul Link** — The scorer's value in this build: +6.8% of its score (model affliction-leveling).
4. **Pandemic** — The scorer's value in this build: +5.7% of its score (model affliction-leveling).
5. **Unholy Power** — The scorer's value in this build: +4.6% of its score (model affliction-leveling).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Fight-lab talent search (fightlab/fl_talent_opt.py): start demonology-leveling, moves: 2 points Improved Health Funnel -> Demonic Energies; 3 points Demonic Embrace -> Demonic Brand; 2 points Improved Bane of Agony -> Improved Life Tap; 2 points Improved Corruption -> Improved Bane of Agony. Race against demonology-leveling over levels 20-60 (seed 3, 3000 fights per level): +5.3% faster per kill.
- Fight-lab numbers are a model of the beta, not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 21/30/0 -> 21/30/0; Malediction 5 gone; +1 Improved Corruption (tier gating for Amplify Curse); +1 Improved Corruption (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); +1 Suppression (tier gating for Amplify Curse); order dropped (order_repair.py) (refill: the affliction-leveling model, leveling-st).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Malediction dropped (not in the allocation; Malediction was replaced by Grim Reach in 70425).

## Open questions (verify in the live game)

- A derived Demonology leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
