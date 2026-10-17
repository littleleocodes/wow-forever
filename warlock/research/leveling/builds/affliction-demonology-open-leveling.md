# Affliction-Demonology — Leveling (open talent search) — 27/24/0

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 27/24/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Affliction-Demonology (an Affliction/Demonology hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the affliction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +6.2% faster per kill than affliction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 50%. Lasts 30 sec. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Soul Siphon** | 1/3 | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 4% per each of your other Affliction effects active on the target, up to a maximum increase of 12%. |
| **Shadow Mastery** | 2/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 4%. |

### Demonology (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 1/5 | changed | Increases your total Stamina by 3%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Fel Vitality** | 1/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 5%, and increases your maximum Mana by 5%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 2/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Decimation** | 1/2 | **NEW** | Reduces the cooldown of your Soul Fire spell by 45%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 3% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 20% and costs no Soul Shards. |
| **Demonic Brand** | 2/3 | **NEW** | Your Searing Pain generates 33% less threat and brands the target for 10 sec. Your pet's next 4 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |

### Destruction (0)

*No points.*

## Core talents (priority order)

1. **Siphon Life** — +3.9 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Voidwalker** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
3. **Demonic Knowledge** — +2.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Demonic Energies** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
5. **Soul Link** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Unholy Power** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Life Tap** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- +2.1% faster than the hand draft leveling-affliction, over the replacement bar: this build is the spec's leveling pick, the hand draft stays as the alternative.
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 39.67; affliction-leveling 42.13. The search simulated 26,128 builds.
- The spec's other leveling builds on the pages: leveling-affliction 40.49 s, opt-affliction-leveling-leveling-st 41.27 s.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 27/24/0 -> 27/24/0; Malediction 5 gone; +1 Improved Corruption (tier gating for Amplify Curse); +1 Suppression (tier gating for Shadow Mastery); +1 Suppression (tier gating for Shadow Mastery); +1 Malevolence (tier gating for Shadow Mastery); +1 Soul Siphon (tier gating for Shadow Mastery); order dropped (order_repair.py) (refill: the affliction-leveling model, leveling-st).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Malediction dropped (not in the allocation; Malediction was replaced by Grim Reach in 70425).

## Open questions (verify in the live game)

- An open-search Affliction-Demonology leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/2345002013400102-00152312012102013--6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
