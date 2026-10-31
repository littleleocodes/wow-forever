# Druid — WoW: Forever talent trees (beta client 1.60.1.70707)

> **Data status:** WoW: Forever beta client build 1.60.1.70707, captured 2026-10-30. World of Warcraft: Forever beta client, build 1.60.1.70707: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-10-29, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70532; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.70205, captured 2026-10-04). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Tree structure (positions, rank caps, prerequisites) from the official wowsims/forever simulator's trees (extracted from the live client 1.60.1.70707 with its hotfix caches); talents the export lacks take Wowhead's tooltip. Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Balance | 16 | 5 | 11 | 0 | 0 | 5 |
| Feral Combat | 20 | 9 | 11 | 0 | 0 | 5 |
| Restoration | 16 | 4 | 7 | 2 | 3 | 3 |

## Balance

### Tier 1 — requires 0 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Wrath** | 5 | — | changed | Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%. | Reduces the cast time of your Wrath spell by 0.5 sec and its Mana cost by 50%. |
| **Genesis** | 5 | — | **NEW** | Increases the periodic damage and healing done by your spells and abilities by 1%. | Increases the periodic damage and healing done by your spells and abilities by 5%. |

### Tier 2 — requires 5 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Moonglow** | 3 | — | changed | Reduces the Mana cost of your damaging spells by 8%. | Reduces the Mana cost of your damaging spells by 25%. |
| **Improved Moonfire** | 2 | — | changed | Increases the damage and critical strike chance of your Moonfire spell by 5%. | Increases the damage and critical strike chance of your Moonfire spell by 10%. |
| **Nature's Majesty** | 2 | — | **NEW** | Increases your critical strike chance with spells and melee attacks by 2%. | Increases your critical strike chance with spells and melee attacks by 4%. |
| **Nature's Reach** | 2 | — | changed | Increases the range of your offensive Balance spells by 10% and improves your chance to hit by 2%. | Increases the range of your offensive Balance spells by 20% and improves your chance to hit by 4%. |

### Tier 3 — requires 10 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Entangling Roots** | 3 | — | changed | Increases the damage done by your Entangling Roots spell by 25%, and its victims can take up to 25% more damage without interrupting the effect. | Increases the damage done by your Entangling Roots spell by 75%, and its victims can take up to 75% more damage without interrupting the effect. |
| **Nature's Splendor** | 1 | Nature's Majesty (2) | **NEW** | Increases the duration of your Moonfire and Rejuvenation spells by 3 sec, your Regrowth spell by 6 sec, and your Insect Swarm spell by 2 sec. | — |

### Tier 4 — requires 15 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Insect Swarm** | 1 | — | changed | The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec. | — |
| **Vengeance** | 5 | Improved Moonfire (2) | changed | Increases the critical strike damage bonus of your Arcane and Nature spells by 20%. | Increases the critical strike damage bonus of your Arcane and Nature spells by 100%. |
| **Improved Starfire** | 5 | — | changed | Reduces the cast time of Starfire by 0.1 sec and Starfire has a 3% chance to stun its target for 3 sec. | Reduces the cast time of Starfire by 0.5 sec and Starfire has a 15% chance to stun its target for 3 sec. |

### Tier 5 — requires 20 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Overgrowth** | 2 | — | **NEW** | Increases the maximum number of targets you may have affected by Entangling Roots by 1. | Increases the maximum number of targets you may have affected by Entangling Roots by 2. |
| **Nature's Grace** | 1 | — | changed | All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec. | — |
| **Eclipse** | 3 | — | **NEW** | Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.17 sec. Stores up to 4 charges. Lasts 15 sec. | Your Wrath spell reduces the cast time of your next 2 Starfire spells by 0.50 sec. Stores up to 4 charges. Lasts 15 sec. |

### Tier 6 — requires 25 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Moonfury** | 5 | — | changed | Increases the damage done by your Arcane and Nature spells by 2%. | Increases the damage done by your Arcane and Nature spells by 10%. |

### Tier 7 — requires 30 points in Balance

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Moonkin Form** | 1 | — | changed | Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their spell Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects. | — |

**Removed from Classic Balance:** Nature's Grasp, Improved Nature's Grasp, Natural Weapons, Improved Thorns, Omen of Clarity

## Feral Combat

### Tier 1 — requires 0 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ferocity** | 5 | — | changed | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 1 Rage or Energy. | Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 5 Rage or Energy. |
| **Furor** | 5 | — | changed | Gives you a 20% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20% of the Energy you had when last in Cat Form, plus 2 Energy per second spent outside Bear Form or Dire Bear Form, up to 20 Energy. | Gives you a 100% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 100% of the Energy you had when last in Cat Form, plus 10 Energy per second spent outside Bear Form or Dire Bear Form, up to 100 Energy. |

### Tier 2 — requires 5 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Feral Swiftness** | 2 | — | **NEW** | Increases your movement speed while in Cat Form by 15%, and increases your chance to Dodge by 2%. | Increases your movement speed while in Cat Form by 30%, and increases your chance to Dodge by 4%. |
| **Feral Instinct** | 3 | — | changed | Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 level higher. | Increases damage done by your Swipe ability by 30% and reduces the chance enemies have to detect you while Prowling as if you were 3 levels higher. |
| **Brutal Impact** | 2 | — | changed | Increases the stun duration of your Bash and Pounce abilities by 0.5 sec and reduces the cooldown of Bash by 15 sec. | Increases the stun duration of your Bash and Pounce abilities by 1 sec and reduces the cooldown of Bash by 30 sec. |
| **Thick Hide** | 3 | — | changed | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1 additional base Armor per level and another 0.67 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. | While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 3 additional base Armor per level and another 2.00 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms. |

### Tier 3 — requires 10 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Shredding Attacks** | 3 | — | **NEW** | Reduces the Energy cost of your Shred ability by 6 and reduces the Rage cost of your Lacerate ability by 1. | Reduces the Energy cost of your Shred ability by 18 and reduces the Rage cost of your Lacerate ability by 3. |
| **Savage Fury** | 2 | — | changed | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 5%. | Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 10%. |
| **Feral Charge** | 1 | — | changed | Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy. | — |
| **Sharpened Claws** | 2 | — | changed | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 3%. | Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 6%. |

### Tier 4 — requires 15 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Predatory Strikes** | 3 | — | changed | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 50% of your level. | Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 150% of your level. |
| **Lacerate** | 1 | Savage Fury (2) | **NEW** | Lacerates the enemy target, making them bleed for 20 damage over 15 sec plus 10% weapon damage per existing application of Lacerate on the target. Causes a high amount of threat. This effect stacks up to 5 times on the same target. | — |
| **Predatory Discipline** | 1 | — | **NEW** | Your Ferocious Bite ability no longer converts extra Energy into damage, but still deals extra damage based on your excess Energy. | — |
| **Blood Frenzy** | 2 | Sharpened Claws (2) | changed | Gives you a 50% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50% chance to add an additional Combo Point. | Gives you a 100% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 100% chance to add an additional Combo Point. |

### Tier 5 — requires 20 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Leader of the Pack** | 1 | — | changed | While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the melee and ranged Critical Strike chance of all party or raid members within 45 yards by 3%. | — |
| **Natural Instinct** | 2 | — | **NEW** | Increases the critical strike damage bonus of your melee abilities by 10% and increases your spell healing by 12% of your Intellect. | Increases the critical strike damage bonus of your melee abilities by 20% and increases your spell healing by 25% of your Intellect. |

### Tier 6 — requires 25 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Rend and Tear** | 5 | Predatory Strikes (3) | **NEW** | Increases damage done by your melee abilities on Bleeding targets by 2%. | Increases damage done by your melee abilities on Bleeding targets by 10%. |
| **Natural Reaction** | 5 | — | **NEW** | Increases your dodge chance by 1%, and gives you a 20% chance to gain 5 Rage each time you dodge. | Increases your dodge chance by 5%, and gives you a 100% chance to gain 5 Rage each time you dodge. |

### Tier 7 — requires 30 points in Feral Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Primal Bite** | 1 | Leader of the Pack (1) | **NEW** | Bite the target, dealing 100% normal damage plus 26 and generating a high amount of threat. | — |
| **Shifting Power** | 1 | Predatory Discipline (1) | **NEW** | Instantly convert 55% of base Mana into 40 Energy. Shifting Power's cost is reduced by effects that reduce the cost of Shapeshifting. | — |

**Removed from Classic Feral Combat:** Feral Aggression, Feline Swiftness, Improved Shred, Primal Fury, Faerie Fire (Feral)

## Restoration

### Tier 1 — requires 0 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Nature's Focus** | 5 | — | changed | Gives your Arcane and Nature spells a 14% chance to not lose casting time when you take damage. | Gives your Arcane and Nature spells a 70% chance to not lose casting time when you take damage. |
| **Heart of the Wild** | 5 | — | changed | Increases your Intellect by 2%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 4% and while in Cat Form your Strength is increased by 2%. | Increases your Intellect by 10%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 20% and while in Cat Form your Strength is increased by 10%. |

### Tier 2 — requires 5 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Naturalist** | 5 | — | **NEW** | Reduces the cast time of your Healing Touch spell by 0.1 sec and increases all damage you deal by 1%. | Reduces the cast time of your Healing Touch spell by 0.5 sec and increases all damage you deal by 5%. |
| **Reflection** | 3 | — | changed | Allows 17% of your Mana regeneration to continue while casting. | Allows 50% of your Mana regeneration to continue while casting. |
| **Natural Shapeshifter** | 3 | — | moved | Reduces the mana cost of all shapeshifting by 10%. | Reduces the mana cost of all shapeshifting by 30%. |

### Tier 3 — requires 10 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Subtlety** | 3 | — | changed | Reduces the threat generated by your Nature and Arcane spells by 10%. | Reduces the threat generated by your Nature and Arcane spells by 30%. |
| **Gift of Nature** | 5 | — | changed | Increases the effect of all your healing spells by 2%. | Increases the effect of all your healing spells by 10%. |
| **Bloom** | 1 | — | **NEW** | When your Rejuvenation or Regrowth spell expires due to its duration, the target is instantly healed for an amount equal to 100% of your Spirit. If either spell expires due to being dispelled, the target is healed for 50% of your Spirit instead. | — |

### Tier 4 — requires 15 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Tranquil Spirit** | 5 | — | unchanged | Reduces the mana cost of your Healing Touch and Tranquility spells by 2%. | Reduces the mana cost of your Healing Touch and Tranquility spells by 10%. |
| **Improved Rejuvenation** | 3 | — | moved | Increases the effect of your Rejuvenation spell by 5%. | Increases the effect of your Rejuvenation spell by 15%. |
| **Swiftmend** | 1 | — | changed | Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells. | — |

### Tier 5 — requires 20 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Nature's Swiftness** | 1 | Naturalist (5) | unchanged | When activated, your next Nature spell becomes an instant cast spell. | — |
| **Living Spirit** | 3 | — | **NEW** | Increases your Spirit by 5%. | Increases your Spirit by 15%. |
| **Improved Tranquility** | 2 | — | changed | Reduces threat caused by Tranquility by 50% and its cooldown by 30%. | Reduces threat caused by Tranquility by 100% and its cooldown by 60%. |

### Tier 6 — requires 25 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Regrowth** | 5 | Improved Rejuvenation (3) | unchanged | Increases the critical effect chance of your Regrowth spell by 10%. | Increases the critical effect chance of your Regrowth spell by 50%. |

### Tier 7 — requires 30 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Wild Growth** | 1 | Living Spirit (3) | **NEW** | Heals the target and their party for 336 over 7 sec. Party members must be within 43 yards of target. The amount healed is applied quickly at first, and slows down as Wild Growth reaches its full duration. | — |

**Removed from Classic Restoration:** Improved Mark of the Wild, Improved Healing Touch, Improved Enrage

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Balance

- **Improved Wrath** (tooltip changed, was Balance row 1, col 1)
  - Classic: Reduces the cast time of your Wrath spell by 0 sec.
  - Forever: Reduces the cast time of your Wrath spell by 0.1 sec and its Mana cost by 10%.
- **Moonglow** (tooltip changed, was Balance row 5, col 3)
  - Classic: Reduces the Mana cost of your Moonfire, Starfire, Wrath, Healing Touch, Regrowth and Rejuvenation spells by 3%.
  - Forever: Reduces the Mana cost of your damaging spells by 8%.
- **Improved Moonfire** (max rank 5 → 2, tooltip changed)
  - Classic: Increases the damage and critical strike chance of your Moonfire spell by 2%.
  - Forever: Increases the damage and critical strike chance of your Moonfire spell by 5%.
- **Nature's Reach** (tooltip changed, was Balance row 3, col 4)
  - Classic: Increases the range of your Wrath, Entangling Roots, Faerie Fire, Moonfire, Starfire, and Hurricane spells by 10%.
  - Forever: Increases the range of your offensive Balance spells by 10% and improves your chance to hit by 2%.
- **Improved Entangling Roots** (tooltip changed, was Balance row 2, col 1)
  - Classic: Gives you a 40% chance to avoid interruption caused by damage while casting Entangling Roots.
  - Forever: Increases the damage done by your Entangling Roots spell by 25%, and its victims can take up to 25% more damage without interrupting the effect.
- **Insect Swarm** (tooltip changed, was Restoration row 3, col 3)
  - Classic: The enemy target is swarmed by insects, decreasing their chance to hit by 2% and causing 66 Nature damage over 12 sec.
  - Forever: The enemy target is swarmed by insects, decreasing their chance to hit with attacks by 2% and causing 48 Nature damage over 12 sec.
- **Vengeance** (tooltip changed)
  - Classic: Increases the critical strike damage bonus of your Starfire, Moonfire, and Wrath spells by 20%.
  - Forever: Increases the critical strike damage bonus of your Arcane and Nature spells by 20%.
- **Improved Starfire** (tooltip changed)
  - Classic: Reduces the cast time of Starfire by 0 sec and has a 3% chance to stun the target for 3 sec.
  - Forever: Reduces the cast time of Starfire by 0.1 sec and Starfire has a 3% chance to stun its target for 3 sec.
- **Nature's Grace** (tooltip changed)
  - Classic: All spell criticals grace you with a blessing of nature, reducing the casting time of your next spell by 1 sec.
  - Forever: All non-periodic spell criticals grace you with a blessing of nature, increasing your spellcasting speed and reducing your global cooldown by 10% for 3 sec.
- **Moonfury** (tooltip changed)
  - Classic: Increases the damage done by your Starfire, Moonfire and Wrath spells by 2%. .
  - Forever: Increases the damage done by your Arcane and Nature spells by 2%.
- **Moonkin Form** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1))
  - Classic: Transforms the Druid into Moonkin Form. While in this form the armor contribution from items is increased by 360% and all party members within 0 yards have their spell critical chance increased by 3%. The Moonkin can only cast Balance spells while shapeshifted.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects.
  - Forever: Shapeshift into Moonkin Form, increasing Omen of Clarity's chance to trigger by 100%, Armor contribution from items by 360%, and all party or raid members within 45 yards have their spell Critical Strike chance increased by 3%. Also protects the caster from Polymorph effects and prevents the use of healing spells.  The act of shapeshifting frees the caster of Polymorph and Movement Impairing effects.

### Feral Combat

- **Ferocity** (tooltip changed)
  - Classic: Reduces the cost of your Maul, Swipe, Claw, and Rake abilities by 1 Rage or Energy.
  - Forever: Reduces the cost of your Maul, Primal Bite, Swipe, Claw, and Rake abilities by 1 Rage or Energy.
- **Furor** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5))
  - Classic: Gives you 20% chance to gain 10 Rage when you shapeshift into Bear and Dire Bear Form or 40 Energy when you shapeshift into Cat Form.
  - Forever: Gives you a 20% chance to gain 10 Rage when shapeshifting into Bear Form or Dire Bear Form. Shapeshifting into Cat Form restores 20% of the Energy you had when last in Cat Form, plus 2 Energy per second spent outside Bear Form or Dire Bear Form, up to 20 Energy.
- **Feral Instinct** (max rank 5 → 3, tooltip changed, was Feral Combat row 2, col 1)
  - Classic: Increases threat caused in Bear and Dire Bear Form by 3% and reduces the chance enemies have to detect you while Prowling.
  - Forever: Increases damage done by your Swipe ability by 10% and reduces the chance enemies have to detect you while Prowling as if you were 1 level higher.
- **Brutal Impact** (tooltip changed, was Feral Combat row 2, col 2)
  - Classic: Increases the stun duration of your Bash and Pounce abilities by 1 sec.
  - Forever: Increases the stun duration of your Bash and Pounce abilities by 0.5 sec and reduces the cooldown of Bash by 15 sec.
- **Thick Hide** (max rank 5 → 3, tooltip changed, was Feral Combat row 2, col 3)
  - Classic: Increases your Armor contribution from items by 2%.
  - Forever: While in Bear Form, Cat Form, Dire Bear Form, or Moonkin Form, you gain 1 additional base Armor per level and another 0.67 base Armor for each point of defense skill beyond five times your level. This amount can be further increased by multipliers from those forms.
- **Savage Fury** (tooltip changed, was Feral Combat row 5, col 1)
  - Classic: Increases the damage caused by your Claw, Rake, Maul and Swipe abilities by 10%.
  - Forever: Increases the damage caused by your Claw, Rake, Shred, Maul, and Swipe abilities by 5%.
- **Feral Charge** (tooltip changed, was Feral Combat row 3, col 2, tooltip changed in build 1.60.1.70707 (ranks 1))
  - Classic: Causes you to charge an enemy, immobilizing and interrupting any spell being cast for 4 sec.
  - Forever: Charge an enemy, immobilizing them and interrupting any spell they are casting for 4 sec.  Feral Charge (Cat): 8-25 yd range, Instant, 30 sec cooldown, Requires Cat Form. Leap behind an enemy.
- **Sharpened Claws** (max rank 3 → 2, tooltip changed, was Feral Combat row 3, col 3)
  - Classic: Increases your critical strike chance while in Bear, Dire Bear or Cat Form by 2%.
  - Forever: Increases your critical strike chance while in Bear Form, Dire Bear Form, or Cat Form by 3%.
- **Predatory Strikes** (tooltip changed, was Feral Combat row 4, col 2, moved in build 1.60.1.70707: was row 4, col 3)
  - Classic: Increases your melee attack power in Cat, Bear and Dire Bear Forms by 50% of your level.
  - Forever: Increases your melee Attack Power in Cat Form, Bear Form, and Dire Bear Form by 50% of your level.
- **Blood Frenzy** (tooltip changed, was Feral Combat row 4, col 3)
  - Classic: Your critical strikes from Cat Form abilities that add combo points have a 50% chance to add an additional combo point.
  - Forever: Gives you a 50% chance to gain an additional 5 Rage any time you get a critical strike while in Bear Form or Dire Bear Form. In addition, your non-periodic critical strikes from Cat Form abilities that generate Combo Points have a 50% chance to add an additional Combo Point.
- **Leader of the Pack** (tooltip changed, was Feral Combat row 7, col 2, tooltip changed in build 1.60.1.70707 (ranks 1))
  - Classic: While in Cat, Bear or Dire Bear Form, the Leader of the Pack increases ranged and melee critical chance of all party members within 0 yards by 3%.
  - Forever: While in Cat Form, Bear Form, or Dire Bear Form, the Leader of the Pack increases the melee and ranged Critical Strike chance of all party or raid members within 45 yards by 3%.

### Restoration

- **Nature's Focus** (tooltip changed, was Restoration row 2, col 2, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5))
  - Classic: Gives you a 14% chance to avoid interruption caused by damage while casting the Healing Touch, Regrowth and Tranquility spells.
  - Forever: Gives your Arcane and Nature spells a 14% chance to not lose casting time when you take damage.
- **Heart of the Wild** (tooltip changed, was Feral Combat row 6, col 2)
  - Classic: Increases your Intellect by 4%. In addition, while in Bear or Dire Bear Form your Stamina is increased by 4% and while in Cat Form your Strength is increased by 4%.
  - Forever: Increases your Intellect by 2%. In addition, while in Bear Form or Dire Bear Form your Stamina is increased by 4% and while in Cat Form your Strength is increased by 2%.
- **Reflection** (tooltip changed, moved in build 1.60.1.70707: was row 3, col 2)
  - Classic: Allows 5% of your Mana regeneration to continue while casting.
  - Forever: Allows 17% of your Mana regeneration to continue while casting.
- **Subtlety** (max rank 5 → 3, tooltip changed, was Restoration row 3, col 4, moved in build 1.60.1.70707: was row 2, col 2)
  - Classic: Reduces the threat generated by your Healing spells by 4%.
  - Forever: Reduces the threat generated by your Nature and Arcane spells by 10%.
- **Gift of Nature** (tooltip changed, was Restoration row 5, col 3)
  - Classic: Increases the effect of all healing spells by 2%.
  - Forever: Increases the effect of all your healing spells by 2%.
- **Swiftmend** (tooltip changed, was Restoration row 7, col 2)
  - Classic: Consumes a Rejuvenation or Regrowth effect on a friendly target to instantly heal them. an amount equal to 12 sec. of Rejuvenation or 18 sec. of Regrowth.
  - Forever: Instantly heals a target with an active Rejuvenation or Regrowth effect for an amount equal to the full duration of the periodic effect of one of those spells.
- **Improved Tranquility** (tooltip changed)
  - Classic: Reduces threat caused by Tranquility by 50%.
  - Forever: Reduces threat caused by Tranquility by 50% and its cooldown by 30%.

---

*Generated from `_reference/data/forever-talents/druid.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
