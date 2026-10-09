# Feral — Bear Tank (14/32/5) — 14/32/5

*Druid · Classic baseline*

| | |
|---|---|
| **Build** | 14/32/5 (Balance / Feral Combat / Restoration) |
| **Role** | TANK — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The tank version of 14/32/5: Feral Instinct (threat), Thick Hide (armor), Feral Charge, Faerie Fire (Feral), Heart of the Wild (+25% Stamina), Leader of the Pack, Savage Fury and Primal Fury, with Natural Weapons/Omen of Clarity/Natural Shapeshifter and Furor. Excellent off-tank and dungeon tank; main-tanks with the right gear.

## Point allocation

### Balance (14)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Nature's Grasp** | 1/1 | While active, any time an enemy strikes the caster they have a 35% chance to become afflicted by Entangling Roots (Rank 1). Only useable outdoors. 1 charge. Lasts 45 sec. |
| **Improved Nature's Grasp** | 4/4 | Increases the chance for your Nature's Grasp to entangle an enemy by 65%. |
| **Natural Weapons** | 5/5 | Increases the damage you deal with physical attacks in all forms by 10%. |
| **Natural Shapeshifter** | 3/3 | Reduces the mana cost of all shapeshifting by 30%. |
| **Omen of Clarity** | 1/1 | Imbues the Druid with natural energy. Each of the Druid's melee attacks has a chance of causing the caster to enter a Clearcasting state. The Clearcasting state reduces the Mana, Rage or Energy cost of your next damage or healing spell or offensive ability by 100%. Lasts 10 min. |

### Feral Combat (32)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Ferocity** | 5/5 | Reduces the cost of your Maul, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Feral Instinct** | 5/5 | Increases threat caused in Bear and Dire Bear Form by 15% and reduces the chance enemies have to detect you while Prowling. |
| **Thick Hide** | 5/5 | Increases your Armor contribution from items by 10%. |
| **Feral Charge** | 1/1 | Causes you to charge an enemy, immobilizing and interrupting any spell being cast for 4 sec. |
| **Sharpened Claws** | 3/3 | Increases your critical strike chance while in Bear, Dire Bear or Cat Form by 6%. |
| **Predatory Strikes** | 3/3 | Increases your melee attack power in Cat, Bear and Dire Bear Forms by 150% of your level. |
| **Primal Fury** | 1/2 | Gives you a 50% chance to gain an additional 5 Rage anytime you get a critical strike while in Bear and Dire Bear Form. |
| **Savage Fury** | 2/2 | Increases the damage caused by your Claw, Rake, Maul and Swipe abilities by 20%. |
| **Faerie Fire (Feral)** | 1/1 | Decrease the armor of the target by 175 for 40 sec. While affected, the target cannot stealth or turn invisible. |
| **Heart of the Wild** | 5/5 | Increases your Intellect by 20%. In addition, while in Bear or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 20%. |
| **Leader of the Pack** | 1/1 | While in Cat, Bear or Dire Bear Form, the Leader of the Pack increases ranged and melee critical chance of all party members within 45 yards by 3%. |

### Restoration (5)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Furor** | 5/5 | Gives you 100% chance to gain 10 Rage when you shapeshift into Bear and Dire Bear Form or 40 Energy when you shapeshift into Cat Form. |

## Core talents (priority order)

1. **Heart of the Wild** — +25% Stamina in Bear Form.
2. **Thick Hide** — +10% armor — Dire Bear multiplies it.
3. **Feral Instinct** — +15% threat in bear forms.
4. **Natural Weapons** — +10% damage = threat.
5. **Omen of Clarity** — Free Mauls/Swipes.
6. **Furor** — 10 rage on shifting into Bear Form — instant Maul/Growl on the pull.
7. **Savage Fury** — +20% Maul/Swipe.
8. **Faerie Fire (Feral)** — Armor debuff without leaving form.
9. **Feral Charge** — Charge + interrupt in Bear Form.
10. **Leader of the Pack** — Group crit.
11. **Sharpened Claws** — Crit in forms.
12. **Ferocity** — Cheaper Maul/Swipe.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 1 | Primal Fury | Primal Fury 2 by dropping Feral Charge, Brutal Impact | Rage on crit; one rank is the compromise to fit Feral Charge and Faerie Fire. |
| 3 | Predatory Strikes | Improved Shred (hybrid cat/bear) | Attack power in forms; prerequisite for Heart of the Wild. |

## Notes

- Maul is the rotation (queue it on every swing), Swipe on packs, Demoralizing Roar and Faerie Fire on the pull; Feral Charge to open.
- Icy Veins: prioritize tank talents over cat talents in a hybrid build — losing threat wipes raids, losing a little DPS does not.

## Forever status of every point in this build

Talent-by-talent check against the Forever beta-client trees (`../forever/talent-trees.md`).

| Tree | Talent | Pts | In Forever | Detail |
|---|---|---|---|---|
| Balance | Nature's Grasp | 1 | **REMOVED** | removed from Classic |
| Balance | Improved Nature's Grasp | 4 | **REMOVED** | removed from Classic |
| Balance | Natural Weapons | 5 | **REMOVED** | removed from Classic |
| Balance | Natural Shapeshifter | 3 | moved-tree | now in Restoration, tier 2 |
| Balance | Omen of Clarity | 1 | **REMOVED** | removed from Classic |
| Feral Combat | Ferocity | 5 | changed | tier 1, max 5 — tooltip changed |
| Feral Combat | Feral Instinct | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed; was Feral Combat row 2, col 1 |
| Feral Combat | Thick Hide | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed; was Feral Combat row 2, col 3 |
| Feral Combat | Feral Charge | 1 | changed | tier 3, max 1 — tooltip changed; was Feral Combat row 3, col 2; tooltip changed in build 1.60.1.70291 (ranks 1) |
| Feral Combat | Sharpened Claws | 3 | changed | tier 3, max 2 — max rank 3 → 2; tooltip changed; was Feral Combat row 3, col 3 |
| Feral Combat | Predatory Strikes | 3 | changed | tier 4, max 3 — tooltip changed; was Feral Combat row 4, col 2 |
| Feral Combat | Primal Fury | 1 | **REMOVED** | removed from Classic |
| Feral Combat | Savage Fury | 2 | changed | tier 3, max 2 — tooltip changed; was Feral Combat row 5, col 1 |
| Feral Combat | Faerie Fire (Feral) | 1 | **REMOVED** | removed from Classic |
| Feral Combat | Heart of the Wild | 5 | changed | tier 1, max 5 — tooltip changed; was Feral Combat row 6, col 2 |
| Feral Combat | Leader of the Pack | 1 | changed | tier 5, max 1 — tooltip changed; was Feral Combat row 7, col 2 |
| Restoration | Furor | 5 | changed | tier 1, max 5 — tooltip changed; tooltip changed in build 1.60.1.70291 (ranks 1, 2, 3, 4, 5) |

**13 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.icy-veins.com/wow-classic/feral-druid-tank-pve-spec-builds-talents>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
