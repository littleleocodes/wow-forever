# Feral Combat — PvP (derived) — 0/32/19

*[Druid](../../../README.md) · [PvP](../README.md) · WoW: Forever — proposed*

| | |
|---|---|
| **Build** | 0/32/19 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — PvP |
| **Status** | Draft |
| **Data** | WoW: Forever beta client build 1.60.1.70707 (2026-10-30 snapshot in `_reference/data/forever-talents/`) — **subject to change before launch** |

## Summary

The Feral Combat PvP build derived on 2026-09-30 (derive_pvp.py): the stats model's PvP optimum with 30+ points in Feral Combat (model feral-cat-dps, profile pvp), then, among builds the model scores within 1% of that, the one the most talentsforever.com Feral Combat builds agree with (3220 builds).

## Point allocation

### Balance (0)

*No points.*

### Feral Combat (32)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Ferocity** | 2/5 | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 2 Rage or Energy. |
| **Furor** | 5/5 | changed | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |
| **Brutal Impact** | 2/2 | changed | Increases the stun duration of your Bash and Pounce abilities by 1 sec and reduces the cooldown of Bash by 30 sec. |
| **Feral Instinct** | 3/3 | changed | Increases damage done by your Swipe ability by 30% and reduces the chance enemies have to detect you while Prowling as if you were 3 levels higher. |
| **Feral Swiftness** | 2/2 | **NEW** | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Thick Hide** | 3/3 | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |
| **Feral Charge** | 1/1 | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. |
| **Savage Fury** | 2/2 | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Sharpened Claws** | 2/2 | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |
| **Blood Frenzy** | 2/2 | changed | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |
| **Predatory Strikes** | 3/3 | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Leader of the Pack** | 1/1 | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the Critical Strike chance (melee, ranged and spell) of all party or raid members within 45 yards by 3%. |
| **Natural Instinct** | 2/2 | **NEW** | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |
| **Rend and Tear** | 1/5 | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 2%. |
| **Primal Bite** | 1/1 | **NEW** | Bite the target, dealing 100% normal damage plus 26 and generating a high amount of threat. |

### Restoration (19)

| Talent | Pts | vs Classic | Effect at this rank |
|---|---|---|---|
| **Heart of the Wild** | 5/5 | changed | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |
| **Nature's Focus** | 5/5 | changed | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Natural Shapeshifter** | 3/3 | moved | Reduces the mana cost of all shapeshifting by 30%. |
| **Naturalist** | 5/5 | **NEW** | Reduces the cast time of your Healing Touch and Wild Growth spells by 0.5 sec and increases all damage you deal by 10%. |
| **Swiftmend** | 1/1 | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. |

## Core talents (priority order)

1. **Natural Shapeshifter** — The scorer's value in this build: +11.8% of its score (model feral-cat-dps).
2. **Berserk** — The scorer's value in this build: +9.9% of its score (model feral-cat-dps).
3. **Feral Swiftness** — The scorer's value in this build: +9.3% of its score (model feral-cat-dps).
4. **Thick Hide** — The scorer's value in this build: +8.9% of its score (model feral-cat-dps).
5. **Feral Charge** — The scorer's value in this build: +7.9% of its score (model feral-cat-dps).
6. **Brutal Impact** — The scorer's value in this build: +7.9% of its score (model feral-cat-dps).

## Notes

- Community tie-break moves: 1 point Naturalist -> Primal Bite; 1 point Rend and Tear -> Blood Frenzy.
- Where we disagree with the community: most Feral Combat builds take Rend and Tear (86% take it), Ferocity (83% take it), which the model values below this build's weakest point; this build takes Gift of the Earthmother (8%), Nature's Focus (3%), Swiftmend (9%), which few Feral Combat builds take (the model values them). Pick rates cover every level-60 build on the site, not PvP builds only.
- PvP values are assumptions: no simulator plays PvP.
- 2026-10-03: repaired for beta build 1.60.1.70170 (talents removed, renamed or moved): King of the Jungle 3 out; Blood Frenzy 2, Ferocity 2 in; to be re-optimized.
- 2026-10-30 (repair_builds.py, client build 1.60.1.70707 trees): 0/32/19 -> 0/32/19; Berserk 1 gone; Gift of the Earthmother 1 gone; refill +1 Naturalist, +1 Rend and Tear (refill: the feral-cat-dps model, pvp).

## Open questions (verify in the live game)

- A derived Feral Combat PvP build: check it in duels and battlegrounds at launch.

## Sources

- <https://talentsforever.com/druid>
- <https://talentsforever.com/popular.js>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
