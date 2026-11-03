# Affliction-Demonology — Leveling (open talent search) — 27/24/0

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 27/24/0 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Affliction-Demonology (an Affliction/Demonology hybrid) leveling build the open leveling search found on 2026-11-02: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the demonology-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +2.4% faster per kill than demonology-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (27)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Grim Reach** | 1/2 | **NEW** | Increases the range of your Affliction spells by 10%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Shadow Mastery** | 2/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 4%. |

### Demonology (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Health Funnel** | 1/2 | changed | Increases the amount of health transferred by your Health Funnel spell by 20%, reduces its health cost by 15%, and reduces all threat your Health Funnel generates by 50%. Allows Health Funnel to be used regardless of your demon's health. |
| **Demonic Embrace** | 4/5 | changed | Increases your total Stamina by 12%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 1/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 2 sec and the Mana cost by 20%. |
| **Demonic Brand** | 3/3 | **NEW** | Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |

### Destruction (0)

*No points.*

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Demonology | Unholy Power | 5 | 0/5/0 |
| 15 | Demonology | Demonic Energies | 1 | 0/6/0 |
| 16-18 | Demonology | Improved Voidwalker | 3 | 0/9/0 |
| 19 | Demonology | Demonic Energies | 1 | 0/10/0 |
| 20 | Demonology | Improved Health Funnel | 1 | 0/11/0 |
| 21-24 | Demonology | Demonic Embrace | 4 | 0/15/0 |
| 25 | Demonology | Demonic Sacrifice | 1 | 0/16/0 |
| 26 | Demonology | Master Summoner | 1 | 0/17/0 |
| 27-29 | Demonology | Demonic Brand | 3 | 0/20/0 |
| 30 | Demonology | Soul Link | 1 | 0/21/0 |
| 31-33 | Demonology | Demonic Knowledge | 3 | 0/24/0 |
| 34-35 | Affliction | Improved Life Tap | 2 | 2/24/0 |
| 36 | Affliction | Suppression | 1 | 3/24/0 |
| 37-40 | Affliction | Improved Corruption | 4 | 7/24/0 |
| 41-43 | Affliction | Suppression | 3 | 10/24/0 |
| 44 | Affliction | Amplify Curse | 1 | 11/24/0 |
| 45-46 | Affliction | Improved Bane of Agony | 2 | 13/24/0 |
| 47 | Affliction | Improved Corruption | 1 | 14/24/0 |
| 48 | Affliction | Pandemic | 1 | 15/24/0 |
| 49-51 | Affliction | Malevolence | 3 | 18/24/0 |
| 52 | Affliction | Pandemic | 1 | 19/24/0 |
| 53 | Affliction | Malevolence | 1 | 20/24/0 |
| 54 | Affliction | Siphon Life | 1 | 21/24/0 |
| 55 | Affliction | Pandemic | 1 | 22/24/0 |
| 56 | Affliction | Malevolence | 1 | 23/24/0 |
| 57 | Affliction | Suppression | 1 | 24/24/0 |
| 58 | Affliction | Grim Reach | 1 | 25/24/0 |
| 59-60 | Affliction | Shadow Mastery | 2 | 27/24/0 |

## Core talents (priority order)

1. **Siphon Life** — +2.1 s per kill at level 60 without it (removal, 3,000 fights).
2. **Suppression** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
3. **Demonic Knowledge** — +1.5 s per kill at level 60 without it (removal, 3,000 fights).
4. **Demonic Brand** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
5. **Demonic Energies** — +1.0 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Corruption** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
7. **Improved Life Tap** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).
8. **Improved Voidwalker** — +0.7 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 30.42; demonology-leveling 31.15. The search simulated 34,237 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Affliction-Demonology leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/2551002013500102-10450302011003013--7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
