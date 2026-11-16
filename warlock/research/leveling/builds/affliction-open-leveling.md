# Affliction — Leveling (open talent search) — 40/10/1

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 40/10/1 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70753 (2026-11-03 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Affliction leveling build the open leveling search found on 2026-11-16: every legal 51-point build with no tree rule, searched at level 60 in the fight lab (this project's solo leveling simulator: same-level mobs, eating, drinking and deaths included) playing the affliction-leveling rotation, the winner picked by a race at levels 20-60 among the level-60 finalists (fightlab/fl_open_search.py); the talent order is the stats model's (affliction-leveling). 

## Point allocation

### Affliction (40)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Life Tap** | 2/2 | moved | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Grim Reach** | 2/2 | **NEW** | Increases the range of your Affliction spells by 20%. |
| **Improved Drains** | 3/3 | **NEW** | Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 20%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |
| **Fel Concentration** | 2/3 | changed | Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 47% chance to not lose casting time when you take damage. |
| **Amplify Curse** | 1/1 | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. |
| **Pandemic** | 3/3 | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |
| **Malevolence** | 5/5 | **NEW** | Increases the critical effect chance of your Shadow spells by 5%. |
| **Siphon Life** | 1/1 | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. |
| **Soul Siphon** | 3/3 | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 12% per each of your other Affliction effects active on the target, up to a maximum increase of 36%. |
| **Shadow Mastery** | 5/5 | changed | Increases the damage dealt or life drained by your Shadow spells by 10%. |
| **Wrack** | 1/1 | **NEW** | Tears the target apart from within for 6 sec, inflicting 60 Shadow damage every 1 sec. While channeling, your Siphon Life, Corruption, and Bane of Agony effects on the target deal their periodic damage 100% faster. |

### Demonology (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 2/2 | **NEW** | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |

### Destruction (1)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Destructive Reach** | 1/2 | changed | Increases the range of your Destruction spells by 10%. |

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
| 42-43 | Affliction | Improved Drains | 2 | 34/0/0 |
| 44 | Affliction | Malevolence | 1 | 35/0/0 |
| 45-49 | Demonology | Unholy Power | 5 | 35/5/0 |
| 50 | Demonology | Demonic Energies | 1 | 35/6/0 |
| 51-52 | Affliction | Fel Concentration | 2 | 37/6/0 |
| 53-55 | Demonology | Improved Voidwalker | 3 | 37/9/0 |
| 56 | Destruction | Destructive Reach | 1 | 37/9/1 |
| 57 | Affliction | Grim Reach | 1 | 38/9/1 |
| 58 | Affliction | Improved Drains | 1 | 39/9/1 |
| 59 | Affliction | Grim Reach | 1 | 40/9/1 |
| 60 | Demonology | Demonic Energies | 1 | 40/10/1 |

## Core talents (priority order)

1. **Wrack** — +3.5 s per kill at level 60 without it (removal, 3,000 fights).
2. **Siphon Life** — +3.4 s per kill at level 60 without it (removal, 3,000 fights).
3. **Suppression** — +1.8 s per kill at level 60 without it (removal, 3,000 fights).
4. **Shadow Mastery** — +1.6 s per kill at level 60 without it (removal, 3,000 fights).
5. **Improved Life Tap** — +1.3 s per kill at level 60 without it (removal, 3,000 fights).
6. **Improved Voidwalker** — +0.9 s per kill at level 60 without it (removal, 3,000 fights).
7. **Pandemic** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).
8. **Malevolence** — +0.8 s per kill at level 60 without it (removal, 3,000 fights).

## Leveling rotation

Not simulated in the fight lab; the class's leveling priority is on the [leveling rotation page](../rotation.md).

## Notes

- 2026-11-16: leveling filler pass (fightlab/fl_filler_pass.py, 1500 fights a level): points that measured nothing, or held a tier open, moved: Improved Shadow Bolt to Demonic Energies at 60 (no loss: -0.0% seed 3, -0.0% seed 4, level-weighted time per kill); Demonic Aegis to Curse of Exhaustion at 58 (no loss: -0.0% seed 3, +0.0% seed 4, level-weighted time per kill); Curse of Exhaustion to Improved Drains at 58 (tie-break: -0.1% seed 3, -0.1% seed 4, level-weighted time per kill); Fel Concentration to Destructive Reach at 56 (no loss: +0.0% seed 3, +0.1% seed 4, level-weighted time per kill); Demonic Embrace to Grim Reach at 57 (no loss: +0.0% seed 3, -0.1% seed 4, level-weighted time per kill).
- Race at levels 20-60 (seed 3, 3,000 fights per level; level-weighted seconds per kill, lower is faster): this build 30.61; affliction-leveling 33.49. The search simulated 21,543 builds.
- Fight-lab numbers are a model of the beta (the assumptions in fightlab/tables.py), not in-game measurements.

## Open questions (verify in the live game)

- An open-search Affliction leveling build: check it while leveling at launch.

## Sources

- <https://talentsforever.com/warlock>
- <https://talentsforever.com/warlock/60/25510223135001351-00151301-01-12>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
