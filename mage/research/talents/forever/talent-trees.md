# Mage — WoW: Forever talent trees (beta client 1.60.1.70170)

> **Data status:** WoW: Forever beta client build 1.60.1.70170, captured 2026-10-03. World of Warcraft: Forever beta client, build 1.60.1.70170: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-10-03, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70009; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.69893, captured 2026-09-18). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Arcane | 18 | 6 | 9 | 1 | 2 | 4 |
| Fire | 17 | 3 | 8 | 0 | 6 | 2 |
| Frost | 19 | 2 | 10 | 3 | 4 | 0 |

## Arcane

### Tier 1 — requires 0 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Wand Specialization** | 2 | — | moved | Increases your damage with Wands by 13%. | Increases your damage with Wands by 25%. |
| **Arcane Focus** | 5 | — | changed | Improves your chance to hit with Arcane spells by 1%. | Improves your chance to hit with Arcane spells by 5%. |
| **Improved Channeling** | 5 | — | **NEW** | Gives you a 20% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 14% chance while casting Arcane Blast. | Gives you a 100% chance to avoid interruption caused by damage while channeling Arcane Missiles and a 70% chance while casting Arcane Blast. |

### Tier 2 — requires 5 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Arcane Subtlety** | 2 | — | changed | Reduces your target's resistance to all your spells by 8 and reduces the threat caused by your Arcane spells by 15%. | Reduces your target's resistance to all your spells by 15 and reduces the threat caused by your Arcane spells by 30%. |
| **Magic Absorption** | 2 | — | changed | Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec. | Increases all your resistances by 10 and causes all spells you fully resist to restore 2% of your total mana. Cannot trigger more often than 1 time per sec. |
| **Arcane Concentration** | 5 | — | unchanged | Gives you a 2% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. | Gives you a 10% chance of entering a Clearcasting state after any damage spell hits a target. The Clearcasting state reduces the mana cost of your next damage spell by 100%. |
| **Arcane Resilience** | 2 | — | changed | Increases your Armor by an amount equal to 25% of your Intellect. | Increases your Armor by an amount equal to 50% of your Intellect. |

### Tier 3 — requires 10 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Arcane Geometry** | 2 | — | **NEW** | Increases the range of your Arcane spells by 3 yards. | Increases the range of your Arcane spells by 6 yards. |
| **Arcane Impact** | 3 | — | **NEW** | Increases the critical strike chance of your Arcane spells by 2%. | Increases the critical strike chance of your Arcane spells by 6%. |
| **Arcane Blast** | 1 | — | **NEW** | Blasts the target with energy, dealing 57 to 65 Arcane damage. Each time you cast Arcane Blast, the damage of all your other spells is increased by 10% and the mana cost of Arcane Blast is increased by 175%. Effect stacks up to 4 times and lasts 8 sec or until any other damage spell is cast. | — |

### Tier 4 — requires 15 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Arcane Shielding** | 2 | — | **NEW** | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 17% and increases the resistances granted by your Mage Armor spell by 25%. | Decreases the Mana lost per point of damage taken when your Mana Shield spell is active by 33% and increases the resistances granted by your Mage Armor spell by 50%. |
| **Improved Counterspell** | 2 | — | changed | Your Counterspell also Silences the target for 2 sec. | Your Counterspell also Silences the target for 4 sec. |
| **Arcane Meditation** | 3 | Arcane Concentration (5) | changed | Allows 17% of your Mana regeneration to continue while casting. | Allows 50% of your Mana regeneration to continue while casting. |
| **Missile Barrage** | 1 | — | **NEW** | Gives your Arcane Blast spell a 40% chance, and your Fireball, Frostbolt, and Frostfire Bolt spells a 20% chance to reduce the channeled duration of your next Arcane Missiles spell by 50%, reduce the Mana cost by 100%, and missiles fire every 0.5 sec. | — |

### Tier 5 — requires 20 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Presence of Mind** | 1 | — | unchanged | When activated, your next Mage spell with a casting time less than 10 sec becomes an instant cast spell. | — |
| **Arcane Mind** | 5 | — | changed | Increases your Intellect by 2% and increases the critical strike damage bonus of your Arcane spells by 20%. | Increases your Intellect by 10% and increases the critical strike damage bonus of your Arcane spells by 100%. |

### Tier 6 — requires 25 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Arcane Instability** | 3 | — | changed | Increases the damage done by your spells by 1% and your critical strike chance by 1%. | Increases the damage done by your spells by 3% and your critical strike chance by 3%. |

### Tier 7 — requires 30 points in Arcane

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Arcane Power** | 1 | Presence of Mind (1) | changed | For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast. | — |

**Removed from Classic Arcane:** Improved Arcane Missiles, Magic Attunement, Improved Arcane Explosion, Improved Mana Shield

## Fire

### Tier 1 — requires 0 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Wake of Fire** | 2 | — | **NEW** | Reduces the cooldown of your Fire Blast spell by 1 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 25%. | Reduces the cooldown of your Fire Blast spell by 2 sec. Killing a non-trivial target increases the critical strike chance of your next Fire Blast cast within 30 sec by 50%. |
| **Incineration** | 3 | — | **NEW** | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 2%. | Increases the critical strike chance of your Fire Blast, Ice Lance, Arcane Blast, and Scorch spells by 6%. |
| **Improved Fireball** | 5 | — | changed | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.1 sec. | Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.5 sec. |

### Tier 2 — requires 5 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ignite** | 5 | — | unchanged | Your critical strikes from Fire damage spells cause the target to burn for an additional 8% of your spell's damage over 4 sec. | Your critical strikes from Fire damage spells cause the target to burn for an additional 40% of your spell's damage over 4 sec. |
| **Flame Throwing** | 2 | — | unchanged | Increases the range of your Fire spells by 3 yards. | Increases the range of your Fire spells by 6 yards. |
| **Impact** | 3 | — | changed | Gives your Fire spells a 3% chance to stun the target for 2 sec. | Gives your Fire spells a 10% chance to stun the target for 2 sec. |

### Tier 3 — requires 10 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Burning Soul** | 3 | — | changed | Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%. | Gives your Fire spells a 70% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 30%. |
| **Improved Flamestrike** | 3 | — | unchanged | Increases the critical strike chance of your Flamestrike spell by 5%. | Increases the critical strike chance of your Flamestrike spell by 15%. |
| **Pyroblast** | 1 | — | changed | Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec. | — |

### Tier 4 — requires 15 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Scorch** | 3 | — | changed | Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. | Your Scorch spell has a 100% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times. |
| **Improved Fire Ward** | 2 | — | unchanged | Causes your Fire Ward to have a 10% chance to reflect Fire spells while active. | Causes your Fire Ward to have a 20% chance to reflect Fire spells while active. |
| **Heating Up** | 1 | Pyroblast (1) | **NEW** | Non-periodic critical strikes with Fireball, Frostfire Bolt, Fire Blast, and Scorch reduce the cast time of your next Pyroblast cast within 20 sec by 25%, stacking up to 3 times. | — |
| **Master of Elements** | 3 | — | changed | Your Fire and Frost critical strikes will refund 10% of their base mana cost. | Your Fire and Frost critical strikes will refund 30% of their base mana cost. |

### Tier 5 — requires 20 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Critical Mass** | 3 | — | unchanged | Increases the critical strike chance of your Fire spells by 2%. | Increases the critical strike chance of your Fire spells by 6%. |
| **Blast Wave** | 1 | — | changed | A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec. | — |

### Tier 6 — requires 25 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Fire Power** | 5 | — | unchanged | Increases the damage done by your Fire spells by 2%. | Increases the damage done by your Fire spells by 10%. |

### Tier 7 — requires 30 points in Fire

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Combustion** | 1 | Critical Mass (3) | changed | When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells. | — |

**Removed from Classic Fire:** Improved Fire Blast, Incinerate

## Frost

### Tier 1 — requires 0 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Frost Warding** | 2 | — | changed | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active. | Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 30%. In addition, gives your Frost Ward a 20% chance to reflect Frost spells and effects while active. |
| **Improved Frostbolt** | 5 | — | changed | Reduces the casting time of your Frostbolt spell by 0.1 sec. | Reduces the casting time of your Frostbolt spell by 0.5 sec. |
| **Elemental Precision** | 5 | — | changed | Improves your chance to hit with Frost and Fire spells by 1%. | Improves your chance to hit with Frost and Fire spells by 5%. |

### Tier 2 — requires 5 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ice Shards** | 5 | — | unchanged | Increases the critical strike damage bonus of your Frost spells by 20%. | Increases the critical strike damage bonus of your Frost spells by 100%. |
| **Permafrost** | 3 | — | changed | Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%. | Increases the duration of your Chill effects by 33% and reduces the target's speed by an additional 10%. |
| **Improved Frost Nova** | 2 | — | unchanged | Reduces the cooldown of your Frost Nova spell by 2 sec. | Reduces the cooldown of your Frost Nova spell by 4 sec. |
| **Frostbite** | 3 | — | moved | Gives your Chill effects a 5% chance to Freeze the target for 5 sec. | Gives your Chill effects a 15% chance to Freeze the target for 5 sec. |

### Tier 3 — requires 10 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Piercing Ice** | 3 | — | unchanged | Increases the damage done by your Frost spells by 2%. | Increases the damage done by your Frost spells by 6%. |
| **Frost Channeling** | 3 | — | moved | Reduces the mana cost of your Frost spells by 5% and reduces the threat caused by your Frost spells by 10%. | Reduces the mana cost of your Frost spells by 15% and reduces the threat caused by your Frost spells by 30%. |
| **Ice Lance** | 1 | — | **NEW** | Deals 28 to 32 Frost damage to an enemy target. Deals 300% increased damage to Frozen targets. | — |
| **Improved Blizzard** | 3 | — | changed | Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 15% for 1.5 sec. | Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 40% for 1.5 sec. |

### Tier 4 — requires 15 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Arctic Reach** | 2 | — | unchanged | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 10%. | Increases the range of your Frostbolt and Blizzard spells and the radius of your Frost Nova and Cone of Cold spells by 20%. |
| **Ice Block** | 1 | — | moved | You become encased in a block of ice, protecting you from all physical attacks and spells for 10 sec, but during that time you cannot attack, move, or cast spells. | — |
| **Shatter** | 3 | — | changed | Increases the critical strike chance of all your spells against Frozen targets by 17%. | Increases the critical strike chance of all your spells against Frozen targets by 50%. |

### Tier 5 — requires 20 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Cone of Cold** | 3 | — | changed | Increases the damage dealt by your Cone of Cold spell by 12%. | Increases the damage dealt by your Cone of Cold spell by 35%. |
| **Cold Snap** | 1 | — | changed | Finishes the remaining cooldown on all your other Frost spells. | — |
| **Fingers of Frost** | 2 | Ice Lance (1) | **NEW** | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 1 spell cast as if the target were Frozen. Lasts 15 sec. | Gives your Chill effects a 15% chance to grant you the Fingers of Frost effect, which treats your next 2 spells cast as if the target were Frozen. Lasts 15 sec. |

### Tier 6 — requires 25 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Winter's Chill** | 5 | — | changed | Gives your Frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times. | Gives your Frost damage spells a 100% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 5 times. |

### Tier 7 — requires 30 points in Frost

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ice Barrier** | 1 | Cold Snap (1) | changed | Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage. | — |

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Arcane

- **Arcane Focus** (tooltip changed)
  - Classic: Reduces the chance that the opponent can resist your Arcane spells by 2%.
  - Forever: Improves your chance to hit with Arcane spells by 1%.
- **Arcane Subtlety** (tooltip changed, was Arcane row 1, col 1)
  - Classic: Reduces your target's resistance to all your spells by 5 and reduces the threat caused by your Arcane spells by 20%.
  - Forever: Reduces your target's resistance to all your spells by 8 and reduces the threat caused by your Arcane spells by 15%.
- **Magic Absorption** (max rank 5 → 2, tooltip changed)
  - Classic: Increases all resistances by 2 and causes all spells you fully resist to restore 1% of your total mana. 1 sec. cooldown.
  - Forever: Increases all your resistances by 5 and causes all spells you fully resist to restore 1% of your total mana. Cannot trigger more often than 1 time per sec.
- **Arcane Resilience** (max rank 1 → 2, tooltip changed, was Arcane row 3, col 3)
  - Classic: Increases your armor by an amount equal to 50% of your Intellect.
  - Forever: Increases your Armor by an amount equal to 25% of your Intellect.
- **Improved Counterspell** (tooltip changed)
  - Classic: Gives your Counterspell a 50% chance to silence the target for 4 sec.
  - Forever: Your Counterspell also Silences the target for 2 sec.
- **Arcane Meditation** (tooltip changed, was Arcane row 4, col 4)
  - Classic: Allows 5% of your Mana regeneration to continue while casting.
  - Forever: Allows 17% of your Mana regeneration to continue while casting.
- **Arcane Mind** (tooltip changed)
  - Classic: Increases your maximum Mana by 2%.
  - Forever: Increases your Intellect by 2% and increases the critical strike damage bonus of your Arcane spells by 20%.
- **Arcane Instability** (tooltip changed, was Arcane row 6, col 2)
  - Classic: Increases your spell damage and critical strike chance by 1%.
  - Forever: Increases the damage done by your spells by 1% and your critical strike chance by 1%.
- **Arcane Power** (tooltip changed)
  - Classic: When activated, your spells deal 30% more damage while costing 30% more mana to cast. This effect lasts 15 sec.
  - Forever: For the next 15 sec, your spells deal 30% more damage while costing 30% more mana to cast.

### Fire

- **Improved Fireball** (tooltip changed, was Fire row 1, col 2)
  - Classic: Reduces the casting time of your Fireball spell by 0 sec.
  - Forever: Reduces the casting time of your Fireball and Frostfire Bolt spells by 0.1 sec.
- **Impact** (max rank 5 → 3, tooltip changed, was Fire row 1, col 3)
  - Classic: Gives your Fire spells a 2% chance to stun the target for 2 sec.
  - Forever: Gives your Fire spells a 3% chance to stun the target for 2 sec.
- **Burning Soul** (max rank 2 → 3, tooltip changed, was Fire row 3, col 4)
  - Classic: Gives your Fire spells a 35% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 15%.
  - Forever: Gives your Fire spells a 23% chance to not lose casting time when you take damage and reduces the threat caused by your Fire spells by 10%.
- **Pyroblast** (tooltip changed, tooltip changed in build 1.60.1.70170 (ranks 1))
  - Classic: Hurls an immense fiery boulder that causes 187 Fire damage and an additional 56 Fire damage over 12 sec.
  - Forever: Hurls an immense fiery boulder that causes 101 to 131 Fire damage and an additional 44 Fire damage over 12 sec.
- **Improved Scorch** (tooltip changed)
  - Classic: Your Scorch spells have a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases the Fire damage dealt to your target by 3% and lasts 30 sec. Stacks up to 5 times.
  - Forever: Your Scorch spell has a 33% chance to cause your target to be vulnerable to Fire damage. This vulnerability increases all Fire damage you deal to your target by 3% and lasts 30 sec, stacking up to 5 times.
- **Master of Elements** (tooltip changed)
  - Classic: Your Fire and Frost spell criticals will refund 10% of their base mana cost.
  - Forever: Your Fire and Frost critical strikes will refund 10% of their base mana cost.
- **Blast Wave** (tooltip changed, tooltip changed in build 1.60.1.70170 (ranks 1))
  - Classic: A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 186 Fire damage, and dazing them for 6 sec.
  - Forever: A wave of flame radiates outward from the caster, damaging all enemies caught within the blast for 154 to 184 Fire damage, and Dazing them for 50% reduced movement speed for 6 sec.
- **Combustion** (tooltip changed, tooltip changed in build 1.60.1.70170 (ranks 1))
  - Classic: When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 critical strikes with Fire spells.
  - Forever: When activated, this spell causes each of your Fire damage spell hits to increase your critical strike chance with Fire damage spells by 10%. This effect lasts until you have caused 3 non-periodic critical strikes with Fire spells.

### Frost

- **Frost Warding** (tooltip changed)
  - Classic: Increases the armor and resistances given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active.
  - Forever: Increases the Armor and resistance given by your Frost Armor and Ice Armor spells by 15%. In addition, gives your Frost Ward a 10% chance to reflect Frost spells and effects while active.
- **Improved Frostbolt** (tooltip changed)
  - Classic: Reduces the casting time of your Frostbolt spell by 0 sec.
  - Forever: Reduces the casting time of your Frostbolt spell by 0.1 sec.
- **Elemental Precision** (max rank 3 → 5, tooltip changed)
  - Classic: Reduces the chance that the opponent can resist your Frost and Fire spells by 2%.
  - Forever: Improves your chance to hit with Frost and Fire spells by 1%.
- **Permafrost** (tooltip changed, was Frost row 2, col 4)
  - Classic: Increases the duration of your Chill effects by 1 sec and reduces the target's speed by an additional 4%.
  - Forever: Increases the duration of your Chill effects by 11% and reduces the target's speed by an additional 3%.
- **Improved Blizzard** (tooltip changed)
  - Classic: Adds a chill effect to your Blizzard spell. This effect lowers the target's movement speed by 30%. Lasts 1.5 sec.
  - Forever: Adds a Chill effect to your Blizzard spell. This effect lowers the target's movement speed by 15% for 1.5 sec.
- **Shatter** (max rank 5 → 3, tooltip changed, was Frost row 4, col 3)
  - Classic: Increases the critical strike chance of all your spells against frozen targets by 10%.
  - Forever: Increases the critical strike chance of all your spells against Frozen targets by 17%.
- **Improved Cone of Cold** (tooltip changed, was Frost row 5, col 3)
  - Classic: Increases the damage dealt by your Cone of Cold spell by 15%.
  - Forever: Increases the damage dealt by your Cone of Cold spell by 12%.
- **Cold Snap** (tooltip changed, was Frost row 3, col 2)
  - Classic: When activated, this spell finishes the cooldown on all of your Frost spells.
  - Forever: Finishes the remaining cooldown on all your other Frost spells.
- **Winter's Chill** (tooltip changed)
  - Classic: Gives your Frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the chance a Frost spell will critically hit the target by 2% for 15 sec. Stacks up to 5 times.
  - Forever: Gives your Frost damage spells a 20% chance to apply the Winter's Chill effect, which increases the chance your Ice Lance and Frostbolt spells will critically hit the target by 2% for 15 sec. Stacks up to 1 times.
- **Ice Barrier** (tooltip changed, tooltip changed in build 1.60.1.70170 (ranks 1))
  - Classic: Instantly shields you, absorbing 438 damage. Lasts 1 min. While the shield holds, spells will not be interrupted.
  - Forever: Instantly shields you, absorbing 447 damage. Lasts 1 min. While the shield holds, your spellcasts will not be interrupted or delayed from taking damage.

---

*Generated from `_reference/data/forever-talents/mage.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
