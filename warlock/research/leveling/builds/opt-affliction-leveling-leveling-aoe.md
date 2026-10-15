# Optimizer — Voidwalker tank: Corruption 24%, Agony 14%, Drain Life 16%, Shadow Bolt 14%, Immolate 6%, wand 6%, Voidwalker 20% (leveling-aoe) — 17/24/10

*[Warlock](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 17/24/10 (Affliction / Demonology / Destruction) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70291 (2026-10-08 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `affliction-leveling` and profile `leveling-aoe`: score +54.8% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Affliction (17)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Improved Corruption** | 5/5 | changed | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |
| **Suppression** | 5/5 | changed | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Malediction** | 5/5 | **NEW** | Increases all periodic damage done by your Warlock spells by 5%. |
| **Improved Bane of Agony** | 2/2 | **NEW** | Increases the damage done by your Bane of Agony by 10%. |

### Demonology (24)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Demonic Embrace** | 5/5 | changed | Increases your total Stamina by 15%. |
| **Unholy Power** | 5/5 | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |
| **Demonic Aegis** | 2/2 | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Improved Voidwalker** | 3/3 | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Demonic Energies** | 1/2 | **NEW** | You heal your pet for 8% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 50% of the Mana you gain. |
| **Demonic Sacrifice** | 1/1 | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. |
| **Master Summoner** | 2/2 | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |
| **Fel Domination** | 1/1 | changed | Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. |
| **Soul Link** | 1/1 | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. |
| **Demonic Knowledge** | 3/3 | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |

### Destruction (10)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Bane** | 2/5 | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.2 sec and your Soul Fire spell by 0.8 sec. |
| **Improved Shadow Bolt** | 3/5 | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 12% for 12 sec. |
| **Molten Skin** | 5/5 | **NEW** | Reduces all damage taken by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Demonology | Demonic Embrace | 5 | 0/5/0 |
| 15-16 | Demonology | Demonic Aegis | 2 | 0/7/0 |
| 17-19 | Demonology | Unholy Power | 3 | 0/10/0 |
| 20 | Demonology | Demonic Sacrifice | 1 | 0/11/0 |
| 21-22 | Demonology | Unholy Power | 2 | 0/13/0 |
| 23 | Demonology | Demonic Energies | 1 | 0/14/0 |
| 24-26 | Demonology | Improved Voidwalker | 3 | 0/17/0 |
| 27-28 | Demonology | Master Summoner | 2 | 0/19/0 |
| 29 | Demonology | Fel Domination | 1 | 0/20/0 |
| 30 | Demonology | Soul Link | 1 | 0/21/0 |
| 31-33 | Demonology | Demonic Knowledge | 3 | 0/24/0 |
| 34-38 | Affliction | Improved Corruption | 5 | 5/24/0 |
| 39-43 | Affliction | Suppression | 5 | 10/24/0 |
| 44-45 | Affliction | Improved Bane of Agony | 2 | 12/24/0 |
| 46-47 | Destruction | Bane | 2 | 12/24/2 |
| 48-52 | Affliction | Malediction | 5 | 17/24/2 |
| 53-55 | Destruction | Improved Shadow Bolt | 3 | 17/24/5 |
| 56-60 | Destruction | Molten Skin | 5 | 17/24/10 |

## Core talents (priority order)

1. **Soul Link** — Removing it costs 19.4 points of score in this model.
2. **Improved Corruption** — Removing it costs 4.8 points of score in this model.
3. **Demonic Knowledge** — Removing it costs 3.5 points of score in this model.
4. **Malediction** — Removing it costs 1.8 points of score in this model.
5. **Improved Bane of Agony** — Removing it costs 1.7 points of score in this model.
6. **Demonic Embrace** — Removing it costs 1.4 points of score in this model.
7. **Shadow Mastery** — Removing it costs 1.0 points of score in this model.
8. **Suppression** — Removing it costs 0.9 points of score in this model.

## Leveling rotation (fight lab)

Pulls of several mobs: area attacks when enough mobs stand in reach, then damage over time spread over the pull, else the single-target priority below. Single-target leveling fights against normal mobs of your level with a Voidwalker: the pet runs in and meets the mob halfway, Torments it every 5 s, and holds it until your threat passes 130% of its own (it takes the mob back once its threat passes yours by 10%). You cast Corruption, Bane of Agony, Siphon Life and Immolate, channel Wrack once the DoTs are up, fill with Shadow Bolt while mana is plentiful and the wand otherwise, Drain Life when hurt, Life Tap when low on mana, Fear or Death Coil a mob that reaches you. Between fights: 2 s loot, 6 s travel, Life Tap back to 70% mana, Consume Shadows or Health Funnel for the pet, food only below 55% health, a 10-12 s re-summon after a pet death; a death costs 90 s.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-09, on top of the priority below): Shadow Bolt only while the mob has more than 35% health; Corruption only while the mob has more than 35% health; Life Tap only when the mob is below 35% health; Curse of the Elements only above 30% mana. Together +10.8% time per kill saved for `leveling-affliction` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/affliction-leveling-aoe.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|
| Torment | 4.4 | 4.0 | 4.3 | 3.1 | 0% |
| Wand | 4.5 | 3.9 | 5.6 | 1.9 | 2% |
| Rain of Fire | 1.3 | 1.3 | 1.1 | 1.6 | 70% |
| Corruption | 1.1 | 1.1 | 1.5 | 0.6 | 8% |
| Bane of Agony | 1.3 | 1.4 | 1.7 | 0.6 | 6% |
| Immolate | 0.7 | 0.7 | 0.8 | 0.4 | 4% |
| Drain Life | 0.1 | 0.2 | 0.2 | 0.1 | 1% |
| Create Healthstone | 0.2 | 0.3 | 0.3 | 0.1 | 0% |
| Death Coil | 0.0 | 0.0 | 0.1 | 0.0 | 1% |
| Fear | 0.1 | 0.1 | 0.2 | 0.0 | 0% |
| Life Tap | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Shadow Bolt | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Curse of the Elements | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Allocation and order taken from cand-aoe-r8 on 2026-10-15: an earlier optimizer round beat the last export in the fight lab (44.6s vs 46.4s per kill, level-weighted).
- Report: warlock/research/talents/forever/optimizer/affliction-leveling-leveling-aoe.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/warlock>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
