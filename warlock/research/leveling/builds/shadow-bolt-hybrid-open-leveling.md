# Shadow Bolt hybrid — Leveling (open talent search) — 29/10/12

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/10/12 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the destruction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +5.2% faster per kill than destruction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (29)

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
| **Shadow Mastery** | 4/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 8%. |

### Demonology (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |

### Destruction (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 4/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.4 sec and your Soul Fire spell by 1.6 sec. |
| **Improved Shadow Bolt** | 1/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec. |
| **Aftermath** | 2/5 | changed | Increases the initial damage of your Immolate spell by 20% and your Conflagrate spell has a 40% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Molten Skin** | 2/5 | **NEW** | Reduces all damage taken by 4%. |

## Core talents (priority order)

1. **Siphon Life** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Voidwalker** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Demonic Energies** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Malevolence** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
5. **Pandemic** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Shadow Mastery** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Life Tap** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 35.93; destruction-leveling 37.80. The search simulated 31,035 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.
- 2026-10-16 (repair_builds.py, client build 70425 trees): 29/10/12 -> 29/10/12; Malediction 4 gone; +1 Improved Corruption (tier gating for Amplify Curse); +1 Suppression (tier gating for Shadow Mastery); +1 Suppression (tier gating for Shadow Mastery); +1 Soul Siphon (tier gating for Shadow Mastery); order dropped (order_repair.py) (refill: the affliction-leveling model, leveling-st).
- 2026-10-17 (audit of 2026-10-17, finding 26): core Malediction dropped (not in the allocation; Malediction was replaced by Grim Reach in 70425).

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/2344002013500104-00050302-014232-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
