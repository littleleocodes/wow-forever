# Optimizer — White 40%, Shred 30% (60 energy), Ferocious Bite 15%, Rip 10%, Claw/Rake 5% (leveling-st) — 9/31/11

*[Druid](../../README.md) · [Leveling and solo play](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 9/31/11 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Leveling |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70009 (2026-09-25 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

Produced by the stats model (`_reference/data/scorer/`) for spec model `feral-cat-dps` and profile `leveling-st`: score +33.9% (time-per-kill saved vs. no talents). Every number behind it is in the effect files (tooltip-parsed or hand-entered with its arithmetic); change those, not this build.

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
| **Heart of the Wild** | 3/5 | changed | Increases your Intellect by 6%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 12% and while in Cat Form your Strength is increased by 6%. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **King of the Jungle** | 3/3 | **NEW** | Tiger's Fury now instantly grants you 60 Energy. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the critical strike chance of all party members within 45 yards by 3%, exclusive with Moonkin Aura. |
| **Predatory Instincts** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20%. |
| **Rend and Tear** | 4/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 8%. |
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
| 15-17 | Feral Combat | Thick Hide | 3 | 0/8/0 |
| 18-19 | Feral Combat | Feral Swiftness | 2 | 0/10/0 |
| 20-21 | Feral Combat | Savage Fury | 2 | 0/12/0 |
| 22-23 | Feral Combat | Sharpened Claws | 2 | 0/14/0 |
| 24 | Feral Combat | Heart of the Wild | 1 | 0/15/0 |
| 25-27 | Feral Combat | Predatory Strikes | 3 | 0/18/0 |
| 28-29 | Feral Combat | Heart of the Wild | 2 | 0/20/0 |
| 30-32 | Feral Combat | King of the Jungle | 3 | 0/23/0 |
| 33 | Feral Combat | Leader of the Pack | 1 | 0/24/0 |
| 34-35 | Feral Combat | Predatory Instincts | 2 | 0/26/0 |
| 36-39 | Feral Combat | Rend and Tear | 4 | 0/30/0 |
| 40 | Feral Combat | Berserk | 1 | 0/31/0 |
| 41-45 | Balance | Genesis | 5 | 5/31/0 |
| 46-47 | Balance | Nature's Reach | 2 | 7/31/0 |
| 48-49 | Balance | Nature's Majesty | 2 | 9/31/0 |
| 50-54 | Restoration | Nature's Focus | 5 | 9/31/5 |
| 55-59 | Restoration | Naturalist | 5 | 9/31/10 |
| 60 | Restoration | Natural Shapeshifter | 1 | 9/31/11 |

## Core talents (priority order)

1. **King of the Jungle** — Removing it costs 5.0 points of score in this model.
2. **Naturalist** — Removing it costs 2.9 points of score in this model.
3. **Sharpened Claws** — Removing it costs 2.6 points of score in this model.
4. **Predatory Strikes** — Removing it costs 2.2 points of score in this model.
5. **Nature's Reach** — Removing it costs 2.0 points of score in this model.
6. **Savage Fury** — Removing it costs 1.9 points of score in this model.
7. **Berserk** — Removing it costs 1.9 points of score in this model.
8. **Nature's Majesty** — Removing it costs 1.7 points of score in this model.

## Leveling rotation (fight lab)

Balance: Moonfire and Insect Swarm up, Wrath while the mob walks in (Eclipse charges), Starfire on Eclipse charges or when the mob is rooted / stunned, Wrath otherwise (pushback in melee), Regrowth below 35% health with Nature's Swiftness when it is up; Entangling Roots when low and the mob is not rooted.

**Tuned rules** (`fightlab/rotation_opt.py`, 2026-09-28, on top of the priority below): drink below 45% mana; eat below 80% health. Together +1.7% time per kill saved for `opt-balance-dps-leveling-st` (level-weighted, a third seed of 3000 fights per level).

What this build casts per kill ([report](../fightlab/balance-dps.md), all leveling builds: [leveling rotations](../rotation.md)):

| Ability | L15 casts/kill | L20 casts/kill | L30 casts/kill | L40 casts/kill | L50 casts/kill | L60 casts/kill | Damage at L60 |
|---|---|---|---|---|---|---|---|
| Melee | 4.3 | 9.6 | 13.3 | 14.5 | 14.7 | 16.4 | 31% |
| Claw | 0.0 | 5.2 | 3.9 | 3.7 | 3.7 | 4.2 | 24% |
| Rake | 0.0 | 0.0 | 1.3 | 1.5 | 1.4 | 1.6 | 7% |
| Ferocious Bite | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.1 | 20% |
| Ravage | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 | 15% |
| Tiger's Fury | 0.0 | 0.0 | 0.6 | 0.7 | 0.7 | 0.8 | 0% |
| Rip | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 3% |
| Enrage | 0.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Demoralizing Roar | 1.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Maul | 3.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Bash | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0% |
| Shred | 0.0 | 0.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0% |

## Notes

- Report: druid/talents/forever/optimizer/feral-cat-dps-leveling-st.md

## Open questions (verify in the live game)

- Hand-entered effect values (see the manual effect file) are the weakest inputs — verify the ones this build leans on.

## Sources

- <https://warcraftforever.games/talents/druid>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
