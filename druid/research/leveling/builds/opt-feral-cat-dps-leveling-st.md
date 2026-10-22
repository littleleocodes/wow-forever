# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (leveling-st) — 9/31/11

*[Druid](../../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/31/11 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70425 (2026-10-16 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `leveling-st`: score +28.2% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

## Point allocation

### Balance (9)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Genesis** | 5/5 | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 5%. |
| **Nature's Reach** | 2/2 | changed | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |
| **Nature's Majesty** | 2/2 | **NEW** | Increases your critical strike chance with spells and melee attacks by 4%. |

### Feral Combat (31)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 5/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Thick Hide** | 1/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1 additional base Armor per level and another 0.67 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the melee and ranged Critical Strike chance of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 5/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Berserk** | 1/1 | **NEW** | Causes your Primal Bite ability to strike up to 3 targets, removes its cooldown, and increases the critical strike chance of your Combo Point-generating abilities by 100%. Clears and grants immunity to Fear effects for the duration. Lasts 15 sec. |

### Restoration (11)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Nature's Focus** | 5/5 | changed | Gives you a 70% chance to avoid interruption caused by damage while casting Arcane and Nature spells. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Natural Shapeshifter** | 1/3 | moved | Reduces the mana cost of all shapeshifting by 10%. |

## Leveling order

| Levels | Tree | Talent | Pts | Running total |
|---|---|---|---|---|
| 10-14 | Feral Combat | Ferocity | 5 | 0/5/0 |
| 15-16 | Feral Combat | Feral Swiftness | 2 | 0/7/0 |
| 17-19 | Feral Combat | Heart of the Wild | 3 | 0/10/0 |
| 20-21 | Feral Combat | Sharpened Claws | 2 | 0/12/0 |
| 22-23 | Feral Combat | Savage Fury | 2 | 0/14/0 |
| 24 | Feral Combat | Heart of the Wild | 1 | 0/15/0 |
| 25-27 | Feral Combat | Predatory Strikes | 3 | 0/18/0 |
| 28-29 | Feral Combat | Blood Frenzy | 2 | 0/20/0 |
| 30 | Feral Combat | Leader of the Pack | 1 | 0/21/0 |
| 31-32 | Feral Combat | Natural Instinct | 2 | 0/23/0 |
| 33 | Feral Combat | Heart of the Wild | 1 | 0/24/0 |
| 34 | Feral Combat | Thick Hide | 1 | 0/25/0 |
| 35-39 | Feral Combat | Rend and Tear | 5 | 0/30/0 |
| 40 | Feral Combat | Berserk | 1 | 0/31/0 |
| 41-45 | Balance | Genesis | 5 | 5/31/0 |
| 46-47 | Balance | Nature's Reach | 2 | 7/31/0 |
| 48-49 | Balance | Nature's Majesty | 2 | 9/31/0 |
| 50-54 | Restoration | Nature's Focus | 5 | 9/31/5 |
| 55-59 | Restoration | Naturalist | 5 | 9/31/10 |
| 60 | Restoration | Natural Shapeshifter | 1 | 9/31/11 |

## Core talents (priority order)

1. **Blood Frenzy** — Removing it costs 2.8 points of score in this model.
2. **Sharpened Claws** — Removing it costs 2.5 points of score in this model.
3. **Predatory Strikes** — Removing it costs 2.4 points of score in this model.
4. **Naturalist** — Removing it costs 2.3 points of score in this model.
5. **Nature's Reach** — Removing it costs 2.2 points of score in this model.
6. **Berserk** — Removing it costs 2.1 points of score in this model.
7. **Rend and Tear** — Removing it costs 1.8 points of score in this model.
8. **Nature's Majesty** — Removing it costs 1.7 points of score in this model.

## Leveling rotation (fight lab)

Single-target leveling fights against normal mobs of your level. Levels 10-19 in Bear Form: walk up, Enrage, Demoralizing Roar, Maul on every swing the rage allows, Bash when low or against a casting mob. From 20 in Cat Form: prowl up behind the mob and open with Ravage from 32 (Shred from 22, Claw before; Pounce comes at 36, after Ravage), Rake once, Claw to five points (the mob faces you, so Shred is only for the opener), Ferocious Bite whenever it kills (from 32), Rip at five points on a mob above half health (before Ferocious Bite: Rip at 2 points on a mob above 40% of its health), Berserk on the pull; when low, shift out for a Regrowth (Nature's Swiftness + Healing Touch in an emergency) and shift back at 55% of base mana, Furor carrying the energy. Between fights: 2 s loot, 6 s travel, Rejuvenation / Regrowth in caster form when hurt (only with the mana to shift back) then Cat Form again, water below 35% mana (the tuned rule drinks lower).

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-10-19, on top of the priority below): drink below 15% mana; never cast Shred. Together +1.0% time per kill saved for `leveling-feral` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/feral-cat-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L15 casts/kill | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|---|
| Melee | 5.0 | 11.8 | 14.6 | 17.3 | 17.0 | 18.6 | 30% |
| Claw | 0.0 | 4.6 | 3.8 | 3.1 | 3.1 | 3.3 | 18% |
| Rake | 0.0 | 0.0 | 1.9 | 1.7 | 1.6 | 1.8 | 8% |
| Ravage | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 | 14% |
| Ferocious Bite | 0.0 | 0.0 | 0.0 | 1.0 | 1.1 | 0.9 | 15% |
| Rip | 0.0 | 0.9 | 1.1 | 0.1 | 0.2 | 0.4 | 11% |
| Enrage | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Demoralizing Roar | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Maul | 3.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Bash | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: druid/research/talents/forever/optimizer/feral-cat-dps-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
