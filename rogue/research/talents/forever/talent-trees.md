# Rogue — WoW: Forever talent trees (beta client 1.60.1.70291)

> **Data status:** WoW: Forever beta client build 1.60.1.70291, captured 2026-10-08. World of Warcraft: Forever beta client, build 1.60.1.70291: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-10-08, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70291; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.70205, captured 2026-10-04). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Assassination | 17 | 2 | 10 | 2 | 3 | 0 |
| Combat | 17 | 3 | 8 | 0 | 6 | 5 |
| Subtlety | 19 | 5 | 11 | 1 | 2 | 3 |

## Assassination

### Tier 1 — requires 0 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Gouge** | 3 | — | changed | Increases the duration of your Gouge ability by 0.5 sec. | Increases the duration of your Gouge ability by 1.5 sec. |
| **Remorseless Attacks** | 2 | — | changed | After killing a non-trivial enemy, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. | After killing a non-trivial enemy, gives you a 40% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec. |
| **Malice** | 5 | — | changed | Increases your critical strike chance with all attacks and Poisons by 1%. | Increases your critical strike chance with all attacks and Poisons by 5%. |

### Tier 2 — requires 5 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ruthlessness** | 3 | — | unchanged | Gives your finishing moves a 20% chance to add a Combo Point to your target. | Gives your finishing moves a 60% chance to add a Combo Point to your target. |
| **Murder** | 2 | — | changed | Increases all damage dealt by 2% against Humanoid and Giant targets. | Increases all damage dealt by 4% against Humanoid and Giant targets. |
| **Improved Slice and Dice** | 3 | — | unchanged | Increases the duration of your Slice and Dice ability by 15%. | Increases the duration of your Slice and Dice ability by 45%. |

### Tier 3 — requires 10 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Relentless Strikes** | 1 | — | unchanged | Your finishing moves have a 20% chance per Combo Point to restore 25 Energy. | — |
| **Improved Expose Armor** | 2 | — | changed | Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points. | Reduces the Energy cost of your Expose Armor ability by 10, and refunds 2 Combo Points when cast with 5 Combo Points. |
| **Lethality** | 5 | Malice (5) | changed | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%. | Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 20%. |

### Tier 4 — requires 15 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Vile Poisons** | 5 | — | moved | Increases the damage dealt by your poisons by 4% and gives your poisons an additional 8% chance to resist dispel effects. | Increases the damage dealt by your poisons by 20% and gives your poisons an additional 40% chance to resist dispel effects. |
| **Cold Blood** | 1 | — | changed | When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%. | — |
| **Improved Poisons** | 5 | — | changed | Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge. | Increases the chance to apply Poisons to your target by 10%, and gives Poison applications a 50% chance to not consume a charge. |

### Tier 5 — requires 20 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Vigor** | 2 | — | changed | Increases your maximum Energy by 5. | Increases your maximum Energy by 10. |
| **Mutilate** | 1 | — | **NEW** | Instantly attacks with both weapons for 75% weapon damage plus an additional 13 with each weapon. Damage increased by 20% against Poisoned targets. Awards 2 Combo Points. | — |
| **Improved Kidney Shot** | 2 | — | changed | Enemies Stunned by your Kidney Shot ability take 5% increased damage from your poisons and attacks. | Enemies Stunned by your Kidney Shot ability take 10% increased damage from your poisons and attacks. |

### Tier 6 — requires 25 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Seal Fate** | 5 | — | moved | Your critical strikes from abilities that add Combo Points have a 20% chance to add an additional Combo Point. | Your critical strikes from abilities that add Combo Points have a 100% chance to add an additional Combo Point. |

### Tier 7 — requires 30 points in Assassination

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Venom** | 1 | Mutilate (1) | **NEW** | Finishing move that increases the damage of your Poisons by 30% and your chance to apply Poisons by 10%. Lasts longer per combo point:  1 point : 9 sec  2 points: 12 sec  3 points: 15 sec  4 points: 18 sec  5 points: 21 sec | — |

## Combat

### Tier 1 — requires 0 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Eviscerate** | 3 | — | changed | Increases the damage done by your Eviscerate ability by 7%. | Increases the damage done by your Eviscerate ability by 20%. |
| **Improved Sinister Strike** | 2 | — | unchanged | Reduces the Energy cost of your Sinister Strike ability by 3. | Reduces the Energy cost of your Sinister Strike ability by 5. |
| **Lightning Reflexes** | 5 | — | unchanged | Increases your Dodge chance by 1%. | Increases your Dodge chance by 5%. |

### Tier 2 — requires 5 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Puncturing Wounds** | 3 | — | **NEW** | Increases the critical strike chance of your Backstab by 10% and your Mutilate by 5%, and gives Backstab a 15% chance to add an additional Combo Point. | Increases the critical strike chance of your Backstab by 30% and your Mutilate by 15%, and gives Backstab a 45% chance to add an additional Combo Point. |
| **Deflection** | 3 | — | changed | Increases your Parry chance by 2%. | Increases your Parry chance by 6%. |
| **Precision** | 3 | — | changed | Improves your chance to hit by 1%. | Improves your chance to hit by 3%. |

### Tier 3 — requires 10 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Endurance** | 2 | — | changed | Reduces the cooldown of your Sprint and Evasion abilities by 30%. | Reduces the cooldown of your Sprint and Evasion abilities by 60%. |
| **Riposte** | 1 | Deflection (3) | unchanged | A strike that becomes active after parrying an opponent's attack. This attack deals 150% weapon damage and disarms the target for 6 sec. | — |
| **Improved Sprint** | 2 | — | unchanged | Gives a 50% chance to remove all movement impairing effects when you activate your Sprint ability. | Gives a 100% chance to remove all movement impairing effects when you activate your Sprint ability. |

### Tier 4 — requires 15 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Kick** | 2 | — | unchanged | Gives your Kick ability a 50% chance to Silence the target for 2 sec. | Gives your Kick ability a 100% chance to Silence the target for 2 sec. |
| **Flawless Execution** | 1 | — | **NEW** | Reduces the Energy cost of your Eviscerate ability by 10. | — |
| **Dual Wield Specialization** | 5 | Precision (3) | changed | Increases the damage done by your off-hand weapon by 5%. | Increases the damage done by your off-hand weapon by 25%. |

### Tier 5 — requires 20 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Blade Flurry** | 1 | — | changed | Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec. | — |
| **Hack and Slash** | 5 | — | **NEW** | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 1% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 1%.   Mace: Your attacks ignore 3% of  your target's armor. | Gives your melee weapon attacks a benefit depending on the weapon.   Axe/Sword: Your successful  melee attacks have a 5% chance  to trigger an extra attack on the   target.   Dagger/Fist: Increases your  critical strike chance by 5%.   Mace: Your attacks ignore 15% of  your target's armor. |

### Tier 6 — requires 25 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Weapon Expertise** | 2 | Blade Flurry (1) | changed | Reduces the chance for your attacks to be Dodged or Parried by 1%. | Reduces the chance for your attacks to be Dodged or Parried by 2%. |
| **Aggression** | 3 | — | changed | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 2%. | Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 6%. |

### Tier 7 — requires 30 points in Combat

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Adrenaline Rush** | 1 | — | unchanged | Increases your Energy regeneration rate by 100% for 15 sec. | — |

**Removed from Classic Combat:** Improved Backstab, Dagger Specialization, Mace Specialization, Sword Specialization, Fist Weapon Specialization

## Subtlety

### Tier 1 — requires 0 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Camouflage** | 5 | — | changed | Reduces your speed penalty from your Stealth ability by 3% and reduces its cooldown by 2 sec. | Reduces your speed penalty from your Stealth ability by 15% and reduces its cooldown by 6 sec. |
| **Master of Deception** | 3 | — | changed | Reduces the chance enemies have to detect you while in Stealth mode as if you were 1 level higher. | Reduces the chance enemies have to detect you while in Stealth mode as if you were 3 levels higher. |
| **Opportunity** | 2 | — | changed | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 5%. | Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 10%. |

### Tier 2 — requires 5 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Setup** | 3 | — | changed | Gives you a 33% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. | Gives you a 100% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells. |
| **Elusiveness** | 2 | — | unchanged | Reduces the cooldown of your Vanish and Blind abilities by 45 sec. | Reduces the cooldown of your Vanish and Blind abilities by 90 sec. |
| **Dirty Tricks** | 2 | — | **NEW** | Reduces the Energy cost of your Sap and Blind abilities by 25%. | Reduces the Energy cost of your Sap and Blind abilities by 50%. |
| **Improved Ambush** | 3 | — | moved | Increases the critical strike chance of your Ambush ability by 15%. | Increases the critical strike chance of your Ambush ability by 45%. |

### Tier 3 — requires 10 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Initiative** | 3 | — | changed | Gives you a 33% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. | Gives you a 100% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability. |
| **Ghostly Strike** | 1 | — | changed | A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point. | — |
| **Improved Distract** | 2 | — | **NEW** | Increases the radius of your Distract ability by 3 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 1 level lower. | Increases the radius of your Distract ability by 5 yds, and further reduces the Stealth detection of distracted enemies as though they were an additional 2 levels lower. |

### Tier 4 — requires 15 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Heightened Senses** | 2 | — | changed | Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%. | Increases your Stealth detection as if you were 3 levels higher and reduces your chance to be hit by spells and ranged attacks by 4%. |
| **Premeditation** | 1 | — | changed | Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost. | — |
| **Serrated Blades** | 3 | — | changed | Causes your attacks to ignore 3% of your target's Armor and increases the damage dealt by your Rupture ability by 10%. | Causes your attacks to ignore 9% of your target's Armor and increases the damage dealt by your Rupture ability by 30%. |

### Tier 5 — requires 20 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Dirty Deeds** | 2 | — | changed | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10, and your Garrote ability no longer requires you to be behind your target. | Reduces the Energy cost of your Cheap Shot and Garrote abilities by 20, and your Garrote ability no longer requires you to be behind your target. |
| **Preparation** | 1 | — | unchanged | When activated, this ability immediately finishes the cooldown on your other Rogue abilities. | — |
| **Hemorrhage** | 1 | Serrated Blades (3) | changed | An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point. | — |

### Tier 6 — requires 25 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Quietus** | 5 | Dirty Deeds (2) | **NEW** | Your Sinister Strike, Ghostly Strike, and Hemorrhage abilities cause 2% more damage against targets below 35% health. | Your Sinister Strike, Ghostly Strike, and Hemorrhage abilities cause 10% more damage against targets below 35% health. |
| **Cutthroat** | 5 | — | **NEW** | Your Backstab has a 3% chance to cause your next Ambush within 10 sec to not require Stealth. | Your Backstab has a 15% chance to cause your next Ambush within 10 sec to not require Stealth. |

### Tier 7 — requires 30 points in Subtlety

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Thousand Cuts** | 1 | Preparation (1) | **NEW** | When your Rupture ability deals periodic damage, the Energy cost of your next Hemorrhage or Backstab ability within 10 sec is reduced by 3, stacking up to 5 times. | — |

**Removed from Classic Subtlety:** Sleight of Hand, Improved Sap, Deadliness

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Assassination

- **Improved Gouge** (tooltip changed, was Combat row 1, col 1)
  - Classic: Increases the effect duration of your Gouge ability by 1 sec.
  - Forever: Increases the duration of your Gouge ability by 0.5 sec.
- **Remorseless Attacks** (tooltip changed)
  - Classic: After killing an opponent that yields experience or honor, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, or Ghostly Strike. Lasts 20 sec.
  - Forever: After killing a non-trivial enemy, gives you a 20% increased critical strike chance on your next Sinister Strike, Backstab, Ambush, Mutilate, or Ghostly Strike. Lasts 20 sec.
- **Malice** (tooltip changed)
  - Classic: Increases your critical strike chance by 1%.
  - Forever: Increases your critical strike chance with all attacks and Poisons by 1%.
- **Murder** (tooltip changed)
  - Classic: Increases all damage caused against Humanoid, Giant, Beast and Dragonkin targets by 1%.
  - Forever: Increases all damage dealt by 2% against Humanoid and Giant targets.
- **Improved Expose Armor** (tooltip changed)
  - Classic: Increases the armor reduced by your Expose Armor ability by 25%.
  - Forever: Reduces the Energy cost of your Expose Armor ability by 5, and refunds 1 Combo Point when cast with 5 Combo Points.
- **Lethality** (tooltip changed)
  - Classic: Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Ghostly Strike, and Hemorrhage abilities by 6%.
  - Forever: Increases the critical strike damage bonus of your Sinister Strike, Gouge, Backstab, Mutilate, Ghostly Strike, and Hemorrhage abilities by 4%.
- **Cold Blood** (tooltip changed, was Assassination row 5, col 2)
  - Classic: When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, or Eviscerate by 100%.
  - Forever: When activated, increases the critical strike chance of your next Sinister Strike, Backstab, Ambush, Eviscerate, or Mutilate by 100%.
- **Improved Poisons** (tooltip changed)
  - Classic: Increases the chance to apply poisons to your target by 2%.
  - Forever: Increases the chance to apply Poisons to your target by 2%, and gives Poison applications a 10% chance to not consume a charge.
- **Vigor** (max rank 1 → 2, tooltip changed, was Assassination row 7, col 2)
  - Classic: Increases your maximum Energy by 10.
  - Forever: Increases your maximum Energy by 5.
- **Improved Kidney Shot** (max rank 3 → 2, tooltip changed)
  - Classic: While affected by your Kidney Shot ability, the target receives an additional 3% damage from all sources.
  - Forever: Enemies Stunned by your Kidney Shot ability take 5% increased damage from your poisons and attacks.

### Combat

- **Improved Eviscerate** (tooltip changed, was Assassination row 1, col 1)
  - Classic: Increases the damage done by your Eviscerate ability by 5%.
  - Forever: Increases the damage done by your Eviscerate ability by 7%.
- **Deflection** (max rank 5 → 3, tooltip changed)
  - Classic: Increases your Parry chance by 1%.
  - Forever: Increases your Parry chance by 2%.
- **Precision** (max rank 5 → 3, tooltip changed)
  - Classic: Increases your chance to hit with melee weapons by 1%.
  - Forever: Improves your chance to hit by 1%.
- **Endurance** (tooltip changed)
  - Classic: Reduces the cooldown of your Sprint and Evasion abilities by 45 sec.
  - Forever: Reduces the cooldown of your Sprint and Evasion abilities by 30%.
- **Dual Wield Specialization** (tooltip changed)
  - Classic: Increases the damage done by your offhand weapon by 10%.
  - Forever: Increases the damage done by your off-hand weapon by 5%.
- **Blade Flurry** (tooltip changed)
  - Classic: Increases your attack speed by 20%. In addition, attacks strike an additional nearby opponent. Lasts 15 sec.
  - Forever: Increases your melee attack speed by 20% and your melee attacks strike an additional nearby opponent. Lasts 15 sec.
- **Weapon Expertise** (tooltip changed)
  - Classic: Increases your skill with Sword, Fist and Dagger weapons by 3.
  - Forever: Reduces the chance for your attacks to be Dodged or Parried by 1%.
- **Aggression** (tooltip changed)
  - Classic: Increases the damage of your Sinister Strike and Eviscerate abilities by 2%.
  - Forever: Increases the damage of your Sinister Strike, Backstab, and Eviscerate abilities by 2%.

### Subtlety

- **Camouflage** (tooltip changed, was Subtlety row 2, col 3)
  - Classic: Increases your speed while stealthed by 3% and reduces the cooldown of your Stealth ability by 1 sec.
  - Forever: Reduces your speed penalty from your Stealth ability by 3% and reduces its cooldown by 2 sec.
- **Master of Deception** (max rank 5 → 3, tooltip changed)
  - Classic: Reduces the chance enemies have to detect you while in Stealth mode.
  - Forever: Reduces the chance enemies have to detect you while in Stealth mode as if you were 1 level higher.
- **Opportunity** (max rank 5 → 2, tooltip changed)
  - Classic: Increases the damage dealt when striking from behind with your Backstab, Garrote, or Ambush abilities by 4%.
  - Forever: Increases the damage dealt by your Backstab, Garrote, Ambush, and Mutilate abilities by 5%.
- **Setup** (tooltip changed, was Subtlety row 4, col 1)
  - Classic: Gives you a 15% chance to add a combo point to your target after dodging their attack or fully resisting one of their spells.
  - Forever: Gives you a 33% chance to add a Combo Point to your target after Dodging one of their attacks or fully resisting one of their spells.
- **Initiative** (tooltip changed)
  - Classic: Gives you a 25% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
  - Forever: Gives you a 33% chance to add an additional combo point to your target when using your Ambush, Garrote, or Cheap Shot ability.
- **Ghostly Strike** (tooltip changed)
  - Classic: A strike that deals 125% weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point.
  - Forever: A strike that deals 125% (180% if a Dagger is equipped in your Main Hand) weapon damage and increases your chance to dodge by 15% for 7 sec. Awards 1 combo point.
- **Heightened Senses** (tooltip changed, was Subtlety row 5, col 1)
  - Classic: Increases your Stealth detection and reduces the chance you are hit by spells and ranged attacks by 2%.
  - Forever: Increases your Stealth detection as if you were 1 level higher and reduces your chance to be hit by spells and ranged attacks by 2%.
- **Premeditation** (tooltip changed, was Subtlety row 7, col 2)
  - Classic: When used, adds 2 combo points to your target. You must add to or use those combo points within 10 sec or the combo points are lost.
  - Forever: Adds 2 Combo Points to your target. You must add to or use those combo points within 20 sec or the combo points are lost.
- **Serrated Blades** (tooltip changed)
  - Classic: Causes your attacks to ignore 0 of your target's Armor and increases the damage dealt by your Rupture ability by 10%. The amount of Armor reduced increases with your level.
  - Forever: Causes your attacks to ignore 3% of your target's Armor and increases the damage dealt by your Rupture ability by 10%.
- **Dirty Deeds** (tooltip changed, was Subtlety row 5, col 3)
  - Classic: Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10.
  - Forever: Reduces the Energy cost of your Cheap Shot and Garrote abilities by 10, and your Garrote ability no longer requires you to be behind your target.
- **Hemorrhage** (tooltip changed, was Subtlety row 5, col 4)
  - Classic: An instant strike that damages the opponent and causes the target to hemorrhage, increasing any Physical damage dealt to the target by up to 3. Lasts 30 charges or 15 sec. Awards 1 combo point.
  - Forever: An instant strike that deals 100% weapon damage (145% if a Dagger is equipped) and causes the target to take 15% increased Rupture damage from the Rogue. Lasts 15 sec. Awards 1 Combo Point.

---

*Generated from `_reference/data/forever-talents/rogue.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
