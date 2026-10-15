# Shadow Bolt hybrid — Leveling (open talent search) — 29/10/12

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 29/10/12 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Shadow Bolt hybrid (an Affliction/Destruction hybrid) leveling build the open leveling search found on 2026-10-15: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the destruction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +5.2% faster per kill than destruction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (29)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 3/5 | changed | Improves your chance to hit by 3% and reduces all threat you generate by 12%. |
| **Improved Corruption** | 4/5 | changed | Reduces the casting time of your Corruption spell by 1.6 sec and increases the damage it deals by 8%. |
| **Malediction** | 4/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 4%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Shadow Mastery** | 4/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 4%. |

### Demonology (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |

### Destruction (12)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 1/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec. |
| **Bane** | 4/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.4 sec and your Soul Fire spell by 1.6 sec. |
| **Molten Skin** | 2/5 | **NEW** | Reduces all damage taken by 4%. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 2/5 | changed | Increases the initial damage of your Immolate spell by 20% and your Conflagrate spell has a 40% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-13 | Affliction | Improved Corruption | 4 | 4/0/0 |
| 14 | Affliction | Suppression | 1 | 5/0/0 |
| 15-18 | Affliction | Malediction | 4 | 9/0/0 |
| 19 | Affliction | Suppression | 1 | 10/0/0 |
| 20 | Affliction | Amplify Curse | 1 | 11/0/0 |
| 21-22 | Affliction | Improved Bane of Agony | 2 | 13/0/0 |
| 23-25 | Affliction | Pandemic | 3 | 16/0/0 |
| 26 | Affliction | Malevolence | 1 | 17/0/0 |
| 27 | Affliction | Suppression | 1 | 18/0/0 |
| 28-31 | Affliction | Malevolence | 4 | 22/0/0 |
| 32-33 | Affliction | Improved Life Tap | 2 | 24/0/0 |
| 34 | Affliction | Siphon Life | 1 | 25/0/0 |
| 35-38 | Affliction | Shadow Mastery | 4 | 29/0/0 |
| 39-43 | Demonology | Unholy Power | 5 | 29/5/0 |
| 44-47 | Destruction | Bane | 4 | 29/5/4 |
| 48 | Destruction | Improved Shadow Bolt | 1 | 29/5/5 |
| 49-50 | Demonology | Demonic Energies | 2 | 29/7/5 |
| 51-52 | Destruction | Molten Skin | 2 | 29/7/7 |
| 53-54 | Destruction | Aftermath | 2 | 29/7/9 |
| 55-57 | Demonology | Improved Voidwalker | 3 | 29/10/9 |
| 58-60 | Destruction | Cataclysm | 3 | 29/10/12 |

## Core talents (priority order)

1. **Siphon Life** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Voidwalker** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Demonic Energies** — +1.1 s per kill at level 60 without it (removal, 3,000 fights).
4. **Malevolence** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
5. **Pandemic** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Malediction** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Shadow Mastery** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Life Tap** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 35.93; destruction-leveling 37.80. The search simulated 31,035 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Shadow Bolt hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/2344002013500104-00050302-014232-6>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
