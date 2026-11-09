# Demonology — Leveling (open talent search) — 21/30/0

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 21/30/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Demonology leveling build the open leveling search found on 2026-11-08: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the demonology-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +0.7% faster per kill than demonology-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (21)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 4/5 | changed | Improves your chance to hit by 4% and reduces all threat you generate by 16%. |
| **Improved Corruption** | 3/5 | changed | Reduces the casting time of your Corruption spell by 1.2 sec and increases the damage it deals by 6%. |
| **Grim Reach** | 1/2 | **NEW** | Increases the range of your Affliction spells by 10%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 4/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 4%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |

### Demonology (30)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Imp** | 2/3 | changed | Increases the damage of your Imp's Firebolt spell by 20% and the effect of its Fire Shield spell by 20%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Improved Sayaad** | 1/3 | unchanged | Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 10%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 10%. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 1/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 2 sec and the Mana cost by 20%. |
| **Demonic Brand** | 3/3 | **NEW** | Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. |
| **Improved Felhunter** | 1/3 | **NEW** | Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 10%, and reduces the cooldown of its Spell Lock by 2 sec. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |
| **Master Demonologist** | 5/5 | changed | Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 10%.  Voidwalker - Reduces Physical damage taken by 10%.  Succubus/Incubus - Increases Shadow damage done by 10%.  Felhunter - Reduces Magic damage taken by 10%. |

### Destruction (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Demonology | Unholy Power | 5 | 0/5/0 |
| 15 | Demonology | Demonic Energies | 1 | 0/6/0 |
| 16-18 | Demonology | Improved Voidwalker | 3 | 0/9/0 |
| 19 | Demonology | Demonic Energies | 1 | 0/10/0 |
| 20-21 | Demonology | Improved Imp | 2 | 0/12/0 |
| 22-23 | Demonology | Demonic Aegis | 2 | 0/14/0 |
| 24 | Demonology | Improved Sayaad | 1 | 0/15/0 |
| 25 | Demonology | Demonic Sacrifice | 1 | 0/16/0 |
| 26 | Demonology | Master Summoner | 1 | 0/17/0 |
| 27-29 | Demonology | Demonic Brand | 3 | 0/20/0 |
| 30 | Demonology | Soul Link | 1 | 0/21/0 |
| 31-33 | Demonology | Demonic Knowledge | 3 | 0/24/0 |
| 34 | Demonology | Improved Felhunter | 1 | 0/25/0 |
| 35-37 | Affliction | Improved Corruption | 3 | 3/25/0 |
| 38-42 | Demonology | Master Demonologist | 5 | 3/30/0 |
| 43-44 | Affliction | Improved Life Tap | 2 | 5/30/0 |
| 45-48 | Affliction | Suppression | 4 | 9/30/0 |
| 49 | Affliction | Grim Reach | 1 | 10/30/0 |
| 50 | Affliction | Amplify Curse | 1 | 11/30/0 |
| 51-52 | Affliction | Improved Bane of Agony | 2 | 13/30/0 |
| 53-54 | Affliction | Pandemic | 2 | 15/30/0 |
| 55-58 | Affliction | Malevolence | 4 | 19/30/0 |
| 59 | Affliction | Pandemic | 1 | 20/30/0 |
| 60 | Affliction | Siphon Life | 1 | 21/30/0 |

## Core talents (priority order)

1. **Siphon Life** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
2. **Demonic Brand** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Demonic Knowledge** — +1.4 s per kill at level 60 without it (removal, 3,000 fights).
4. **Demonic Energies** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
5. **Suppression** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Life Tap** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Corruption** — +0.6 s per kill at level 60 without it (removal, 3,000 fights).
8. **Pandemic** — +0.5 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 30.92; demonology-leveling 31.14. The search simulated 25,765 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Demonology leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/24310020134001-020523021110031135--12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
