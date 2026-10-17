# Optimizer — Voidwalker tank: Corruption 24%, Agony 14%, Drain Life 16%, Shadow Bolt 14%, Immolate 6%, wand 6%, Voidwalker 20% (solo-60) — 27/24/0

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 27/24/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Solo/farming |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `affliction-leveling` and profile `solo-60`: score +26.3% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 50%. Lasts 30 sec. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Soul Siphon** | 3/3 | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 12% per each of your other Affliction effects active on the target, up to a maximum increase of 36%. |
| **Shadow Mastery** | 2/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 4%. |

### Demonology (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Improved Imp** | 3/3 | changed | Increases the damage of your Imp's Firebolt spell by 30% and the effect of its Fire Shield spell by 30%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Fel Vitality** | 1/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 5%, and increases your maximum Mana by 5%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |

### Destruction (0)

*No points.*

## Core talents (priority order)

1. **Siphon Life** — Removing it costs 7.7 points of score in this model.
2. **Demonic Knowledge** — Removing it costs 3.5 points of score in this model.
3. **Pandemic** — Removing it costs 2.8 points of score in this model.
4. **Improved Corruption** — Removing it costs 1.6 points of score in this model.
5. **Soul Link** — Removing it costs 1.6 points of score in this model.
6. **Suppression** — Removing it costs 1.2 points of score in this model.
7. **Unholy Power** — Removing it costs 1.0 points of score in this model.

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Report: warlock/research/talents/forever/optimizer/affliction-leveling-solo-60.md
- 2026-10-16 (repair_builds.py, client build 70425 trees): 27/24/0 -> 27/24/0; Malediction 5 gone; +1 Malevolence (tier gating for Siphon Life); +1 Malevolence (tier gating for Shadow Mastery); +1 Soul Siphon (tier gating for Shadow Mastery); +1 Soul Siphon (tier gating for Shadow Mastery); +1 Soul Siphon (tier gating for Shadow Mastery); order dropped (order_repair.py) (refill: the affliction-leveling model, solo-60).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Malediction dropped (not in the allocation; Malediction was replaced by Grim Reach in 70425).

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
