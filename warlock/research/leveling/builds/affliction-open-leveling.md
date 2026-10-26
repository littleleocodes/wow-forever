# Affliction — Leveling (open talent search) — 37/14/0

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 37/14/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Affliction leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the affliction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +5.1% faster per kill than affliction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (37)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Improved Drains** | 3/3 | **NEW** | Increases health drained or damage done by your Drain Life, Drain Soul, and Wrack spells by 20%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Fel Concentration** | 2/3 | changed | Gives you a 47% chance to avoid interruption caused by damage while channeling or casting your Drain Life, Drain Mana, Drain Soul, or Wrack spells. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 50%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 4/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 4%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Soul Siphon** | 3/3 | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 12% per each of your other Affliction effects active on the target, up to a maximum increase of 36%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 10%. |
| **Wrack** | 1/1 | **NEW** | Tears the target apart from within, inflicting 36 Shadow damage every 1 sec and increasing the damage they take from your other Shadow damage over time effects by 10% for 6 sec. |

### Demonology (14)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 2/5 | changed | Increases your total Stamina by 6%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Improved Sayaad** | 1/3 | unchanged | Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 10%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 10%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |

### Destruction (0)

*No points.*

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
| 28 | Affliction | Pandemic | 1 | 19/0/0 |
| 29 | Affliction | Malevolence | 1 | 20/0/0 |
| 30 | Affliction | Pandemic | 1 | 21/0/0 |
| 31 | Affliction | Suppression | 1 | 22/0/0 |
| 32-33 | Affliction | Soul Siphon | 2 | 24/0/0 |
| 34 | Affliction | Siphon Life | 1 | 25/0/0 |
| 35-39 | Affliction | Shadow Mastery | 5 | 30/0/0 |
| 40 | Affliction | Wrack | 1 | 31/0/0 |
| 41 | Affliction | Soul Siphon | 1 | 32/0/0 |
| 42-44 | Affliction | Improved Drains | 3 | 35/0/0 |
| 45-49 | Demonology | Unholy Power | 5 | 35/5/0 |
| 50 | Demonology | Demonic Energies | 1 | 35/6/0 |
| 51-52 | Affliction | Fel Concentration | 2 | 37/6/0 |
| 53-55 | Demonology | Improved Voidwalker | 3 | 37/9/0 |
| 56 | Demonology | Demonic Energies | 1 | 37/10/0 |
| 57-58 | Demonology | Demonic Embrace | 2 | 37/12/0 |
| 59 | Demonology | Demonic Sacrifice | 1 | 37/13/0 |
| 60 | Demonology | Improved Sayaad | 1 | 37/14/0 |

## Core talents (priority order)

1. **Suppression** — +2.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Siphon Life** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
3. **Improved Voidwalker** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Mastery** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
5. **Soul Siphon** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Life Tap** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
7. **Wrack** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Drains** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 37.38; affliction-leveling 39.30. The search simulated 19,476 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Affliction leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/25500322134001351-0025030211--7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
