# Shadow Bolt hybrid — Leveling (open talent search) — 29/10/12

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/10/12 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) leveling build the open leveling search found on 2026-10-20: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the destruction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +7.5% faster per kill than destruction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 50%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Curse of Exhaustion** | 1/1 | changed | Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Shadow Mastery** | 4/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 8%. |

### Demonology (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |

### Destruction (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 4/5 | changed | Increases the initial damage of your Immolate spell by 40% and your Conflagrate spell has a 80% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-11 | Affliction | Improved Life Tap | 2 | 2/0/0 |
| 12-15 | Affliction | Suppression | 4 | 6/0/0 |
| 16-19 | Affliction | Improved Corruption | 4 | 10/0/0 |
| 20 | Affliction | Amplify Curse | 1 | 11/0/0 |
| 21-22 | Affliction | Improved Bane of Agony | 2 | 13/0/0 |
| 23 | Affliction | Improved Corruption | 1 | 14/0/0 |
| 24 | Affliction | Pandemic | 1 | 15/0/0 |
| 25-27 | Affliction | Malevolence | 3 | 18/0/0 |
| 28-29 | Affliction | Pandemic | 2 | 20/0/0 |
| 30 | Affliction | Malevolence | 1 | 21/0/0 |
| 31 | Affliction | Siphon Life | 1 | 22/0/0 |
| 32 | Affliction | Malevolence | 1 | 23/0/0 |
| 33 | Affliction | Suppression | 1 | 24/0/0 |
| 34 | Affliction | Curse of Exhaustion | 1 | 25/0/0 |
| 35-38 | Affliction | Shadow Mastery | 4 | 29/0/0 |
| 39-43 | Demonology | Unholy Power | 5 | 29/5/0 |
| 44 | Demonology | Demonic Energies | 1 | 29/6/0 |
| 45-47 | Demonology | Improved Voidwalker | 3 | 29/9/0 |
| 48 | Demonology | Demonic Energies | 1 | 29/10/0 |
| 49-53 | Destruction | Bane | 5 | 29/10/5 |
| 54-57 | Destruction | Aftermath | 4 | 29/10/9 |
| 58-60 | Destruction | Cataclysm | 3 | 29/10/12 |

## Core talents (priority order)

1. **Siphon Life** — +2.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Suppression** — +2.2 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Voidwalker** — +1.7 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Mastery** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
5. **Demonic Energies** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Life Tap** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
7. **Malevolence** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
8. **Pandemic** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 32.18; destruction-leveling 34.60. The search simulated 33,042 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/2550002013501104-00050302-005034-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
