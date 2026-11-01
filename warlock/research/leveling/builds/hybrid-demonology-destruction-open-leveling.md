# Demonology/Destruction hybrid — Leveling (open talent search) — 5/24/22

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 5/24/22 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-31 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Demonology/Destruction hybrid (a Demonology/Destruction hybrid) leveling build the open leveling search found on 2026-10-26: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the destruction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). +14.0% faster per kill than destruction-leveling, the fastest of our leveling builds in that race.

## Point allocation

### Affliction (5)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |

### Demonology (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Health Funnel** | 1/2 | changed | Increases the amount of health transferred by your Health Funnel spell by 20%, reduces its health cost by 15%, and reduces all threat your Health Funnel generates by 50%. Allows Health Funnel to be used regardless of your demon's health. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Fel Vitality** | 3/3 | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 2/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Decimation** | 2/2 | **NEW** | Reduces the cooldown of your Soul Fire spell by 90%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 6% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 40% and costs no Soul Shards. |
| **Fel Domination** | 1/1 | changed | Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |

### Destruction (22)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Shadow Bolt** | 4/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 16% for 12 sec. |
| **Bane** | 5/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |
| **Cataclysm** | 3/3 | changed | Reduces the Mana cost of your Destruction spells by 10%. |
| **Ruin** | 4/5 | changed | Increases the critical strike damage bonus of your Destruction spells by 80%. |
| **Shadowburn** | 1/1 | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. |
| **Intensity** | 2/3 | changed | Gives your Destruction spells a 47% chance to not lose casting time when you take damage. |
| **Agonizing Flames** | 3/3 | **NEW** | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-13 | Affliction | Suppression | 4 | 4/0/0 |
| 14-18 | Demonology | Unholy Power | 5 | 4/5/0 |
| 19 | Demonology | Demonic Energies | 1 | 4/6/0 |
| 20-22 | Demonology | Improved Voidwalker | 3 | 4/9/0 |
| 23 | Demonology | Demonic Energies | 1 | 4/10/0 |
| 24 | Demonology | Improved Health Funnel | 1 | 4/11/0 |
| 25-27 | Demonology | Fel Vitality | 3 | 4/14/0 |
| 28 | Demonology | Demonic Sacrifice | 1 | 4/15/0 |
| 29-30 | Demonology | Decimation | 2 | 4/17/0 |
| 31-32 | Demonology | Master Summoner | 2 | 4/19/0 |
| 33 | Demonology | Fel Domination | 1 | 4/20/0 |
| 34 | Demonology | Soul Link | 1 | 4/21/0 |
| 35-37 | Demonology | Demonic Knowledge | 3 | 4/24/0 |
| 38 | Affliction | Suppression | 1 | 5/24/0 |
| 39-43 | Destruction | Bane | 5 | 5/24/5 |
| 44-46 | Destruction | Cataclysm | 3 | 5/24/8 |
| 47-48 | Destruction | Improved Shadow Bolt | 2 | 5/24/10 |
| 49-52 | Destruction | Ruin | 4 | 5/24/14 |
| 53 | Destruction | Improved Shadow Bolt | 1 | 5/24/15 |
| 54-56 | Destruction | Agonizing Flames | 3 | 5/24/18 |
| 57 | Destruction | Improved Shadow Bolt | 1 | 5/24/19 |
| 58 | Destruction | Shadowburn | 1 | 5/24/20 |
| 59-60 | Destruction | Intensity | 2 | 5/24/22 |

## Core talents (priority order)

1. **Suppression** — +3.7 s per kill at level 60 without it (removal, 3,000 fights).
2. **Improved Voidwalker** — +2.9 s per kill at level 60 without it (removal, 3,000 fights).
3. **Demonic Knowledge** — +2.0 s per kill at level 60 without it (removal, 3,000 fights).
4. **Cataclysm** — +1.9 s per kill at level 60 without it (removal, 3,000 fights).
5. **Agonizing Flames** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
6. **Decimation** — +1.2 s per kill at level 60 without it (removal, 3,000 fights).
7. **Soul Link** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Bane** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 44.56; destruction-leveling 50.82. The search simulated 40,901 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Demonology/Destruction hybrid leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/05-10050332012210013-0450304123-7>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
