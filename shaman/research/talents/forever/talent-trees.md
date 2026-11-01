# Shaman — WoW: Forever talent trees (beta client 1.60.1.70707)

> **Data status:** WoW: Forever beta client build 1.60.1.70707, captured 2026-10-31. World of Warcraft: Forever beta client, build 1.60.1.70707: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-10-30, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70532; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.70205, captured 2026-10-04). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Tree structure (positions, rank caps, prerequisites) from the official wowsims/forever simulator's trees (extracted from the live client 1.60.1.70707 with its hotfix caches); talents the export lacks take Wowhead's tooltip. Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Elemental | 16 | 7 | 8 | 1 | 0 | 3 |
| Enhancement | 18 | 7 | 7 | 2 | 2 | 6 |
| Restoration | 16 | 4 | 9 | 1 | 2 | 3 |

## Elemental

### Tier 1 — requires 0 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Convection** | 5 | — | changed | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 2%. | Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 10%. |
| **Concussion** | 5 | — | changed | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 1%. | Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 5%. |

### Tier 2 — requires 5 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Elemental Devastation** | 3 | — | changed | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3% for 10 sec. | Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 9% for 10 sec. |
| **Reverberation** | 5 | — | changed | Reduces the cooldown of your Shock spells by 0.2 sec. | Reduces the cooldown of your Shock spells by 1.0 sec. |
| **Elemental Alacrity** | 3 | — | **NEW** | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.17 sec. | Reduces the cast time of your Lightning Bolt, Chain Lightning, and Lava Burst spells by 0.50 sec. |
| **Call of Flame** | 3 | — | changed | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 5%, as well as increases the duration of your Flame Shock spell by 3 sec. | Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 15%, as well as increases the duration of your Flame Shock spell by 9 sec. |

### Tier 3 — requires 10 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Elemental Focus** | 1 | — | moved | Gives you a 10% chance to enter a Clearcasting state after casting any Fire, Frost, or Nature damage spell. The Clearcasting state reduces the mana cost of your next damage spell by 100%. | — |
| **Elemental Warding** | 3 | — | changed | Reduces damage taken from Fire, Frost, and Nature effects by 3%. | Reduces damage taken from Fire, Frost, and Nature effects by 10%. |

### Tier 4 — requires 15 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Trial by Fire** | 2 | — | **NEW** | Increases the damage done by your Fire Nova spell by 10% and reduces its cooldown by 2 sec, and increases the duration of your Magma Totem by 10 sec. | Increases the damage done by your Fire Nova spell by 20% and reduces its cooldown by 4 sec, and increases the duration of your Magma Totem by 20 sec. |
| **Eye of the Storm** | 3 | — | changed | Gives your Lightning Bolt, Chain Lightning, and Lava Burst spells a 23% chance to not lose casting time when you take damage. | Gives your Lightning Bolt, Chain Lightning, and Lava Burst spells a 70% chance to not lose casting time when you take damage. |
| **Earthbound** | 1 | — | **NEW** | Your Earthbind Totem Immobilizes nearby targets for 5 sec when cast. | — |

### Tier 5 — requires 20 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Elemental Reach** | 2 | — | **NEW** | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 3 yards and reduces the cooldown of Totemic Projection by 10 sec. | Increases the range of your Lightning Bolt, Chain Lightning, Fire Nova, and Lava Burst spells by 6 yards and reduces the cooldown of Totemic Projection by 20 sec. |
| **Lava Burst** | 1 | — | **NEW** | You hurl molten lava at the target, dealing 113 to 145 Fire damage. If your Flame Shock is on the target, Lava Burst deals 20% increased damage. | — |
| **Lightning Overload** | 3 | Elemental Alacrity (3) | **NEW** | Gives your Lightning Bolt and Chain Lightning spells a 3% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. | Gives your Lightning Bolt and Chain Lightning spells a 10% chance to cast a second, similar spell on the same target at no additional cost that causes half damage and no threat. |

### Tier 6 — requires 25 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Elemental Fury** | 5 | Lightning Overload (3) | changed | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20%. | Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 100%. |

### Tier 7 — requires 30 points in Elemental

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Elemental Mastery** | 1 | Lava Burst (1) | **NEW** | Gain mastery over Fire and Lightning, reducing the cast time of Lightning Bolt and Lava Burst by 0.5 sec, and removing the cooldown from Chain Lightning. Lasts 15 sec. | — |

**Removed from Classic Elemental:** Improved Fire Totems, Storm Reach, Lightning Mastery

## Enhancement

### Tier 1 — requires 0 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Earth's Grasp** | 2 | — | moved | Increases the health of your Stoneclaw Totem by 25% and the radius of your Earthbind Totem by 10%. | Increases the health of your Stoneclaw Totem by 50% and the radius of your Earthbind Totem by 20%. |
| **Thundering Strikes** | 5 | — | changed | Improves your chance to get a critical strike with all spells and attacks by 1%. | Improves your chance to get a critical strike with all spells and attacks by 5%. |
| **Ancestral Knowledge** | 5 | — | changed | Increases your Intellect by 2%. | Increases your Intellect by 10%. |

### Tier 2 — requires 5 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Guardian Totems** | 2 | — | unchanged | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 10% and reduces the cooldown of your Grounding Totem by 1 sec. | Increases the amount of damage reduced by your Stoneskin Totem and Windwall Totem by 20% and reduces the cooldown of your Grounding Totem by 2 sec. |
| **Mental Dexterity** | 3 | — | **NEW** | Increases your Attack Power by an amount equal to 33% of your Intellect. | Increases your Attack Power by an amount equal to 100% of your Intellect. |
| **Improved Ghost Wolf** | 2 | — | changed | Reduces the cast time of your Ghost Wolf spell by 1.0 sec, and Ghost Wolf may be used indoors. | Reduces the cast time of your Ghost Wolf spell by 3.0 sec, and Ghost Wolf may be used indoors. |
| **Improved Lightning Shield** | 3 | — | unchanged | Increases the damage done by your Lightning Shield orbs by 5%. | Increases the damage done by your Lightning Shield orbs by 15%. |

### Tier 3 — requires 10 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Elemental Weapons** | 3 | — | moved | Increases the melee attack power bonus of your Rockbiter Weapon by 7%, your Windfury Weapon effect by 13% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 5%. | Increases the melee attack power bonus of your Rockbiter Weapon by 20%, your Windfury Weapon effect by 40% and increases the damage caused by your Flametongue Weapon and Frostbrand Weapon by 15%. |
| **Shamanistic Focus** | 1 | — | **NEW** | Reduces the mana cost of your Shock and Lightning Shield spells by 45%. | — |
| **Anticipation** | 3 | — | changed | Increases your chance to dodge by an additional 2%. | Increases your chance to dodge by an additional 6%. |

### Tier 4 — requires 15 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Toughness** | 5 | — | changed | Increases your Stamina by 2%. | Increases your Stamina by 10%. |
| **Flurry** | 5 | Mental Dexterity (3) | changed | Increases your attack speed by 5% for your next 3 swings after dealing a melee critical strike. | Increases your attack speed by 25% for your next 3 swings after dealing a melee critical strike. |
| **Stormstrike** | 1 | — | changed | Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec. | — |

### Tier 5 — requires 20 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Spirit Weapons** | 1 | — | **NEW** | Gives a chance to parry enemy melee attacks, reduces all threat generated by your attacks by 30% while Rockbiter Weapon is not active, and increases all threat generated by 30% while Rockbiter Weapon is active. | — |
| **Mental Quickness** | 2 | — | **NEW** | Increases your spell damage and healing by up to 15% of your Intellect. | Increases your spell damage and healing by up to 30% of your Intellect. |
| **Improved Stormstrike** | 2 | Stormstrike (1) | **NEW** | When you Stormstrike, you have a 50% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 50% chance to reset each time you Dodge or Parry. | When you Stormstrike, you have a 100% chance to gain 50% mana regeneration while casting spells for 15 sec, and Stormstrike's cooldown has a 100% chance to reset each time you Dodge or Parry. |

### Tier 6 — requires 25 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Maelstrom Weapon** | 5 | — | **NEW** | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 4%. Stacks up to 5 times. Lasts 30 sec. | When you deal damage with a melee attack, you have a chance to reduce the cast time and Mana cost of your next Lightning Bolt spell by 20%. Stacks up to 5 times. Lasts 30 sec. |

### Tier 7 — requires 30 points in Enhancement

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Rage of the Farseer** | 1 | Mental Quickness (2) | **NEW** | Increases your attack speed by 30% for 25 sec. | — |

**Removed from Classic Enhancement:** Shield Specialization, Enhancing Totems, Two-Handed Axes and Maces, Improved Weapon Totems, Parry, Weapon Mastery

## Restoration

### Tier 1 — requires 0 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Healing Wave** | 5 | — | changed | Reduces the casting time of your Healing Wave spell by 0.1 sec. | Reduces the casting time of your Healing Wave spell by 0.5 sec. |
| **Tidal Focus** | 5 | — | changed | Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%. | Reduces the Mana cost of your healing spells by 5% and improves your chance to hit by 5%. |

### Tier 2 — requires 5 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Mindfulness** | 3 | — | **NEW** | Allows 17% of your Mana regeneration to continue while casting. | Allows 50% of your Mana regeneration to continue while casting. |
| **Natural Grace** | 3 | — | **NEW** | Reduces the threat generated by your spells by 5%. | Reduces the threat generated by your spells by 15%. |
| **Totemic Focus** | 5 | — | changed | Reduces the Mana cost of your totems and any spells that summon or move them by 5%. | Reduces the Mana cost of your totems and any spells that summon or move them by 25%. |
| **Improved Reincarnation** | 2 | — | changed | Reduces the cooldown of your Reincarnation spell by 10 min, increases your maximum health by 2%, and increases the amount of health and Mana you reincarnate with by an additional 10%. | Reduces the cooldown of your Reincarnation spell by 20 min, increases your maximum health by 4%, and increases the amount of health and Mana you reincarnate with by an additional 20%. |

### Tier 3 — requires 10 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ancestral Healing** | 3 | — | moved | Increases your target's armor value by 8% for 15 sec after getting a critical effect from one of your healing spells. | Increases your target's armor value by 25% for 15 sec after getting a critical effect from one of your healing spells. |
| **Healing Focus** | 3 | — | changed | Gives your healing spells a 23% chance to not lose casting time when you take damage. | Gives your healing spells a 70% chance to not lose casting time when you take damage. |
| **Water Shield** | 1 | — | **NEW** | The caster is surrounded by 3 globes of water. When a spell, melee, or ranged attack hits the caster or when one of the caster's spells gets a critical result, 2% of maximum mana is restored to the caster, expending one water globe. Only one globe will activate every few seconds. Lasts 10 min.  Only one Elemental Shield can be active on the Shaman at any one time. | — |

### Tier 4 — requires 15 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Tidal Mastery** | 5 | — | changed | Increases the critical effect chance of your healing spells by 1%. | Increases the critical effect chance of your healing spells by 5%. |
| **Restorative Totems** | 5 | — | changed | Increases the effect of your Mana Spring Totem by 5% and increases the effect of your Healing Stream Totem by 10%. | Increases the effect of your Mana Spring Totem by 25% and increases the effect of your Healing Stream Totem by 50%. |
| **Mana Tide Totem** | 1 | — | changed | Summons a Mana Tide Totem with 5 health at the feet of the caster for 12 sec that restores 88 mana every 3 seconds to group members within 30 yards. | — |

### Tier 5 — requires 20 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Healing Way** | 3 | — | changed | Increases the amount healed by your Healing Wave spell by 8%. | Increases the amount healed by your Healing Wave spell by 25%. |
| **Nature's Swiftness** | 1 | — | unchanged | When activated, your next Nature spell with a casting time less than 10 sec. becomes an instant cast spell. | — |

### Tier 6 — requires 25 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Purification** | 5 | — | unchanged | Increases the effectiveness of your healing spells by 2%. | Increases the effectiveness of your healing spells by 10%. |

### Tier 7 — requires 30 points in Restoration

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Riptide** | 1 | Healing Way (3) | **NEW** | Heals a friendly target for 485 to 533, an additional 445 over 15 sec, and increases the effectiveness of your Chain Heal casts directly on that target by 25%. | — |

**Removed from Classic Restoration:** Nature's Guidance, Totemic Mastery, Healing Grace

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Elemental

- **Convection** (tooltip changed)
  - Classic: Reduces the mana cost of your Shock, Lightning Bolt and Chain Lightning spells by 2%.
  - Forever: Reduces the mana cost of your Shock, Lightning Bolt, Lava Burst, and Chain Lightning spells by 2%.
- **Concussion** (tooltip changed)
  - Classic: Increases the damage done by your Lightning Bolt, Chain Lightning and Shock spells by 1%.
  - Forever: Increases the damage done by your Lightning Bolt, Chain Lightning, and Earth Shock spells by 1%.
- **Elemental Devastation** (tooltip changed, was Elemental row 4, col 4, moved in build 1.60.1.70707: was row 2, col 4, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Your offensive spell crits will increase your chance to get a critical strike with melee attacks by 3% for 10 sec.
  - Forever: Your Critical Strikes with direct damage spells increase your chance to get a Critical Strike with melee attacks by 3% for 10 sec.
- **Reverberation** (tooltip changed, was Elemental row 3, col 2)
  - Classic: Reduces the cooldown of your Shock spells by 0 sec.
  - Forever: Reduces the cooldown of your Shock spells by 0.2 sec.
- **Call of Flame** (tooltip changed, moved in build 1.60.1.70707: was row 2, col 3, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Increases the damage done by your Fire Totems by 5%.
  - Forever: Increases the damage done by your Fire Totems and by your Flame Shock, Fire Nova, and Lava Burst spells by 5%, as well as increases the duration of your Flame Shock spell by 3 sec.
- **Elemental Warding** (tooltip changed, was Elemental row 2, col 2, moved in build 1.60.1.70707: was row 2, col 1)
  - Classic: Reduces damage taken from Fire, Frost and Nature effects by 4%.
  - Forever: Reduces damage taken from Fire, Frost, and Nature effects by 3%.
- **Eye of the Storm** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Gives you a 33% chance to gain the Focused Casting effect that lasts for 6 sec after being the victim of a melee or ranged critical strike. The Focused Casting effect prevents you from losing casting time when taking damage.
  - Forever: Gives your Lightning Bolt, Chain Lightning, and Lava Burst spells a 23% chance to not lose casting time when you take damage.
- **Elemental Fury** (max rank 1 → 5, tooltip changed, was Elemental row 5, col 2, prerequisite changed in build 1.60.1.70707: was call of thunder)
  - Classic: Increases the critical strike damage bonus of your Searing, Magma, and Fire Nova Totems and your Fire, Frost, and Nature spells by 100%.
  - Forever: Increases the critical strike damage bonus of your Searing and Magma Totems and your Fire, Frost, and Nature spells by 20%.

### Enhancement

- **Thundering Strikes** (tooltip changed, was Enhancement row 2, col 2)
  - Classic: Improves your chance to get a critical strike with your weapon attacks by 1%.
  - Forever: Improves your chance to get a critical strike with all spells and attacks by 1%.
- **Ancestral Knowledge** (tooltip changed, was Enhancement row 1, col 2)
  - Classic: Increases your maximum Mana by 1%.
  - Forever: Increases your Intellect by 2%.
- **Improved Ghost Wolf** (tooltip changed)
  - Classic: Reduces the cast time of your Ghost Wolf spell by 1 sec.
  - Forever: Reduces the cast time of your Ghost Wolf spell by 1.0 sec, and Ghost Wolf may be used indoors.
- **Anticipation** (max rank 5 → 3, tooltip changed)
  - Classic: Increases your chance to dodge by an additional 1%.
  - Forever: Increases your chance to dodge by an additional 2%.
- **Toughness** (tooltip changed, was Enhancement row 4, col 3)
  - Classic: Increases your armor value from items by 2%.
  - Forever: Increases your Stamina by 2%.
- **Flurry** (tooltip changed)
  - Classic: Increases your attack speed by 10% for your next 3 swings after dealing a critical strike.
  - Forever: Increases your attack speed by 5% for your next 3 swings after dealing a melee critical strike.
- **Stormstrike** (tooltip changed, was Enhancement row 7, col 2)
  - Classic: Gives you an extra attack. In addition, the next 2 sources of Nature damage dealt to the target are increased by 20%. Lasts 12 sec.
  - Forever: Instantly strike for normal weapon damage and increase the damage you deal to the target with your next Lightning Bolt, Chain Lightning, or Earth Shock spell by 20% for 12 sec.

### Restoration

- **Improved Healing Wave** (tooltip changed)
  - Classic: Reduces the casting time of your Healing Wave spell by 0 sec.
  - Forever: Reduces the casting time of your Healing Wave spell by 0.1 sec.
- **Tidal Focus** (tooltip changed, was Restoration row 1, col 3, moved in build 1.60.1.70707: was row 2, col 3)
  - Classic: Reduces the Mana cost of your healing spells by 1%.
  - Forever: Reduces the Mana cost of your healing spells by 1% and improves your chance to hit by 1%.
- **Totemic Focus** (tooltip changed, was Restoration row 2, col 3, moved in build 1.60.1.70707: was row 1, col 3)
  - Classic: Reduces the Mana cost of your totems by 5%.
  - Forever: Reduces the Mana cost of your totems and any spells that summon or move them by 5%.
- **Improved Reincarnation** (tooltip changed, was Restoration row 2, col 1)
  - Classic: Reduces the cooldown of your Reincarnation spell by 10 min and increases the amount of health and mana you reincarnate with by an additional 10%.
  - Forever: Reduces the cooldown of your Reincarnation spell by 10 min, increases your maximum health by 2%, and increases the amount of health and Mana you reincarnate with by an additional 10%.
- **Healing Focus** (max rank 5 → 3, tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Gives you a 14% chance to avoid interruption caused by damage while casting any healing spell.
  - Forever: Gives your healing spells a 23% chance to not lose casting time when you take damage.
- **Tidal Mastery** (tooltip changed, was Restoration row 4, col 3)
  - Classic: Increases the critical effect chance of your healing and lightning spells by 1%.
  - Forever: Increases the critical effect chance of your healing spells by 1%.
- **Restorative Totems** (tooltip changed)
  - Classic: Increases the effect of your Mana Spring and Healing Stream Totems by 5%.
  - Forever: Increases the effect of your Mana Spring Totem by 5% and increases the effect of your Healing Stream Totem by 10%.
- **Mana Tide Totem** (tooltip changed, was Restoration row 7, col 2, tooltip changed in build 1.60.1.70707 (ranks 1))
  - Classic: Summons a Mana Tide Totem with 5 health at the feet of the caster for 13 sec-1 sec that restores 170 mana every 3 seconds to group members within 0 yards.
  - Forever: Summons a Mana Tide Totem with 5 health at the feet of the caster for 12 sec that restores 88 mana every 3 seconds to group members within 30 yards.
- **Healing Way** (tooltip changed, was Restoration row 5, col 1)
  - Classic: Your Healing Wave spells have a 33% chance to increase the effect of subsequent Healing Wave spells on that target by 6% for 15 sec. This effect will stack up to 3 times.
  - Forever: Increases the amount healed by your Healing Wave spell by 8%.

---

*Generated from `_reference/data/forever-talents/shaman.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
