# Feral — Cat DPS / Powershift (14/32/5) — 14/32/5

*Druid · Classic baseline*

| | |
|---|---|
| **Build** | 14/32/5 (Balance / Feral Combat / Restoration) |
| **Role** | DPS — Raid |
| **Status** | Alternative |
| **Data** | Classic Era 1.12-era trees (validated against `_reference/data/classic-era-talents.json`) |
| **Forever** | This is the *baseline*; see the Forever status table below and `../forever/` for the adapted build |

## Summary

The classic 14/32/5 feral: Heart of the Wild, Leader of the Pack, Blood Frenzy, Improved Shred, Predatory Strikes and Savage Fury in Feral; Natural Weapons, Omen of Clarity and Natural Shapeshifter in Balance; Furor in Restoration for powershifting (shift out and back in for 40 energy with Wolfshead Helm).

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
| **Thick Hide** | 5/5 | Increases your Armor contribution from items by 10%. |
| **Feline Swiftness** | 2/2 | Increases your movement speed by 30% while outdoors in Cat Form and increases your chance to dodge while in Cat Form by 4%. |
| **Sharpened Claws** | 3/3 | Increases your critical strike chance while in Bear, Dire Bear or Cat Form by 6%. |
| **Improved Shred** | 2/2 | Reduces the Energy cost of your Shred ability by 12. |
| **Predatory Strikes** | 3/3 | Increases your melee attack power in Cat, Bear and Dire Bear Forms by 150% of your level. |
| **Blood Frenzy** | 2/2 | Your critical strikes from Cat Form abilities that add combo points have a 100% chance to add an additional combo point. |
| **Primal Fury** | 2/2 | Gives you a 100% chance to gain an additional 5 Rage anytime you get a critical strike while in Bear and Dire Bear Form. |
| **Savage Fury** | 2/2 | Increases the damage caused by your Claw, Rake, Maul and Swipe abilities by 20%. |
| **Heart of the Wild** | 5/5 | Increases your Intellect by 20%. In addition, while in Bear or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 20%. |
| **Leader of the Pack** | 1/1 | While in Cat, Bear or Dire Bear Form, the Leader of the Pack increases ranged and melee critical chance of all party members within 45 yards by 3%. |

### Restoration (5)

| Talent | Pts | Effect at this rank |
|---|---|---|
| **Furor** | 5/5 | Gives you 100% chance to gain 10 Rage when you shapeshift into Bear and Dire Bear Form or 40 Energy when you shapeshift into Cat Form. |

## Core talents (priority order)

1. **Furor** — 40 energy on entering Cat Form — powershifting lives on this.
2. **Heart of the Wild** — +20% Strength in Cat Form (+25% Stamina in Bear).
3. **Leader of the Pack** — +3% crit for the whole melee group.
4. **Omen of Clarity** — Clearcasting procs on melee hits — free Shreds.
5. **Natural Weapons** — +10% physical damage.
6. **Natural Shapeshifter** — -30% shapeshift mana cost — more powershifts per mana bar.
7. **Improved Shred** — -12 energy on Shred.
8. **Blood Frenzy** — Extra combo point on crits.
9. **Predatory Strikes** — +150 attack power at 60.
10. **Sharpened Claws** — +6% crit in forms.
11. **Savage Fury** — +20% Claw/Rake/Maul/Swipe damage.
12. **Ferocity** — -5 energy on Claw/Rake/Maul/Swipe.

## Flex points

| Pts | Default | Alternatives | Why |
|---|---|---|---|
| 5 | Thick Hide | Feral Instinct, Brutal Impact 2 + Feral Instinct 3 | Tier-2 Feral filler; Thick Hide also helps when you have to bear up. |
| 5 | Nature's Grasp 1 + Improved Nature's Grasp 4 | Improved Wrath | Tier-1 Balance filler on the way to Natural Weapons. |
| 2 | Feline Swiftness | Feral Charge 1 + Primal Fury (bear variant) | Movement speed and dodge in Cat Form. |

## Notes

- Shred from behind (or Claw if not possible), Rip/Ferocious Bite at 5 points, powershift whenever energy is low and Clearcasting is not up.
- Requires Wolfshead Helm (Leatherworking) and Manual Crowd Pummeler charges to reach rogue-level DPS.

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
| Feral Combat | Thick Hide | 5 | changed | tier 2, max 3 — max rank 5 → 3; tooltip changed; was Feral Combat row 2, col 3 |
| Feral Combat | Feline Swiftness | 2 | **REMOVED** | removed from Classic |
| Feral Combat | Sharpened Claws | 3 | changed | tier 3, max 2 — max rank 3 → 2; tooltip changed; was Feral Combat row 3, col 3 |
| Feral Combat | Improved Shred | 2 | **REMOVED** | removed from Classic |
| Feral Combat | Predatory Strikes | 3 | changed | tier 4, max 3 — tooltip changed; was Feral Combat row 4, col 2 |
| Feral Combat | Blood Frenzy | 2 | changed | tier 4, max 2 — tooltip changed; was Feral Combat row 4, col 3 |
| Feral Combat | Primal Fury | 2 | **REMOVED** | removed from Classic |
| Feral Combat | Savage Fury | 2 | changed | tier 3, max 2 — tooltip changed; was Feral Combat row 5, col 1 |
| Feral Combat | Heart of the Wild | 5 | changed | tier 1, max 5 — tooltip changed; was Feral Combat row 6, col 2 |
| Feral Combat | Leader of the Pack | 1 | changed | tier 5, max 1 — tooltip changed; was Feral Combat row 7, col 2 |
| Restoration | Furor | 5 | changed | tier 1, max 5 — tooltip changed; tooltip changed in build 1.60.1.70291 (ranks 1, 2, 3, 4, 5) |

**17 point(s) of this build no longer exist in Forever** and must be re-spent; see `../forever/README.md` for how they were re-spent.

## Sources

- <https://www.wowhead.com/classic/guide/classes/druid/feral/dps-talent-builds-pve>

---
*Generated from `builds.json` by `_reference/data/render_builds.py` — edit the JSON, not this file.*
