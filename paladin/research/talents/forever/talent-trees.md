# Paladin — WoW: Forever talent trees (beta client 1.60.1.70707)

> **Data status:** WoW: Forever beta client build 1.60.1.70707, captured 2026-10-30. World of Warcraft: Forever beta client, build 1.60.1.70707: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-10-29, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70532; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.70205, captured 2026-10-04). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Tree structure (positions, rank caps, prerequisites) from the official wowsims/forever simulator's trees (extracted from the live client 1.60.1.70707 with its hotfix caches); talents the export lacks take Wowhead's tooltip. Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Holy | 17 | 10 | 5 | 1 | 1 | 5 |
| Protection | 17 | 6 | 8 | 2 | 1 | 4 |
| Retribution | 17 | 5 | 9 | 2 | 1 | 4 |

## Holy

### Tier 1 — requires 0 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Spiritual Focus** | 5 | — | changed | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 14% chance to not lose casting time when you take damage. | Gives your Flash of Light, Holy Light, and Light's Vigil spells a 70% chance to not lose casting time when you take damage. |
| **Divine Strength** | 5 | — | unchanged | Increases your Strength by 2%. | Increases your Strength by 10%. |

### Tier 2 — requires 5 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Healing Light** | 3 | — | changed | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 4%. | Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 12%. |
| **Reverence** | 2 | — | **NEW** | Allows 15% of your Mana regeneration to continue while casting. | Allows 30% of your Mana regeneration to continue while casting. |
| **Improved Seals** | 5 | — | **NEW** | Increases the damage done by your Seals and Judgements by 3%. | Increases the damage done by your Seals and Judgements by 15%. |
| **Purifying Power** | 2 | — | **NEW** | Reduces the mana cost of your Cleanse and Purify spells by 10% and reduces the cooldown of your Exorcism and Holy Wrath spells by 17%. | Reduces the mana cost of your Cleanse and Purify spells by 20% and reduces the cooldown of your Exorcism and Holy Wrath spells by 33%. |

### Tier 3 — requires 10 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Divine Favor** | 1 | — | moved | When activated, gives your next Flash of Light, Holy Light, or Holy Shock spell a 100% critical effect chance. | — |
| **Illumination** | 5 | Reverence (2) | changed | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 20% chance to gain Mana equal to 50% of the base cost of the spell. | After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 100% chance to gain Mana equal to 50% of the base cost of the spell. |
| **Holy Conduit** | 2 | — | **NEW** | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 20%. | Reduces the mana cost of your Consecration, Holy Wrath, Exorcism, and Hammer of Wrath spells by 40%. |

### Tier 4 — requires 15 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Divine Precision** | 2 | — | **NEW** | Improves your chance to hit with Holy spells by 4%, and reduces the duration of Silence effects on you by 10%. | Improves your chance to hit with Holy spells by 8%, and reduces the duration of Silence effects on you by 20%. |
| **Infusion of Light** | 2 | — | **NEW** | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 0.5 sec. | Your Holy Shock and Flash of Light critical hits reduce the cast time of your next Holy Light cast within 15 sec by 1.0 sec. |
| **Oath of Light** | 1 | — | **NEW** | Swear an Oath to protect target ally for 5 min, increasing the healing of your Holy Light on them by up to 400, your Flash of Light by up to 115, and your Holy Shock by up to 229. Only one Oath of Light may be sworn by the Paladin at any one time. | — |

### Tier 5 — requires 20 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Consecrated Ground** | 2 | — | **NEW** | Gives your Holy spells 5% increased damage against the first 4 enemies that enter your Consecration. | Gives your Holy spells 10% increased damage against the first 4 enemies that enter your Consecration. |
| **Holy Shock** | 1 | — | changed | Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally. | — |
| **Boundless Light** | 2 | Holy Shock (1) | **NEW** | Increases the critical strike chance of your Holy Shock spell by 15% when cast on allies not affected by your Oath of Light. | Increases the critical strike chance of your Holy Shock spell by 30% when cast on allies not affected by your Oath of Light. *(est.)* |

### Tier 6 — requires 25 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Holy Power** | 5 | — | changed | Increases the critical strike healing bonus of your Holy spells by 10%. | Increases the critical strike healing bonus of your Holy spells by 50%. |

### Tier 7 — requires 30 points in Holy

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Light's Vigil** | 1 | Holy Shock (1) | **NEW** | Applies Light's Vigil to the target for 30 sec. Your next Holy Shock cast on them triggers no cooldown and causes enemy targets to suffer 175 to 189 Holy damage and refund 75% of Light's Vigil's Mana cost, or allied targets to heal their party for 325 to 343. You may only have one Light's Vigil active per party. | — |

**Removed from Classic Holy:** Improved Seal of Righteousness, Consecration, Improved Lay on Hands, Improved Blessing of Wisdom, Lasting Judgement

## Protection

### Tier 1 — requires 0 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Divine Intellect** | 5 | — | unchanged | Increases your total Intellect by 2%. | Increases your total Intellect by 10%. |
| **Redoubt** | 5 | — | changed | Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks. | Damaging melee attacks against you have a 10% chance to increase your chance to block by 30%. Lasts 10 sec or 5 blocks. |

### Tier 2 — requires 5 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Precision** | 3 | — | changed | Improves your chance to hit by 1%. | Improves your chance to hit by 3%. |
| **Guardian's Favor** | 2 | — | changed | Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec. | Reduces the cooldown of your Blessing of Protection by 2 min and increases the duration of your Blessing of Freedom by 6 sec. |
| **Sacred Duty** | 2 | — | **NEW** | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 30 sec, and reduces the duration of Forbearance by 5 sec. | Reduces the cooldown of your Divine Shield, Divine Protection, and Templar's Bulwark spells by 60 sec, and reduces the duration of Forbearance by 10 sec. |

### Tier 3 — requires 10 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Templar's Bulwark** | 1 | — | **NEW** | When activated, this ability grants you an absorb shield equal to 100% of your maximum health for 8 sec. Applies Forbearance for 1 min. Cannot be cast while Forbearance is active. | — |
| **Improved Hammer of Justice** | 3 | — | moved | Decreases the cooldown of your Hammer of Justice spell by 5 sec. | Decreases the cooldown of your Hammer of Justice spell by 15 sec. |
| **Shield Specialization** | 2 | Redoubt (5) | changed | Increases the amount of damage absorbed by your shield by 15%, and gives your blocks a 50% chance to restore 4% of your maximum Mana. May only occur once every 3 sec. With Shieldsworn, a Holy Strike that lands with a shield rolls the same chance without the cooldown. | Increases the amount of damage absorbed by your shield by 30%, and gives your blocks a 100% chance to restore 4% of your maximum Mana. May only occur once every 3 sec. With Shieldsworn, a Holy Strike that lands with a shield rolls the same chance without the cooldown. |
| **Toughness** | 5 | — | moved | Increases your armor value from items by 2%. | Increases your armor value from items by 10%. |

### Tier 4 — requires 15 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Swift Judgement** | 1 | Templar's Bulwark (1) | **NEW** | Finishes the remaining cooldown on your Judgement ability and reduces the Mana cost of your next Judgement by 100%. | — |
| **Improved Righteous Fury** | 3 | — | changed | While Righteous Fury is active, all damage taken is reduced by 3%. | While Righteous Fury is active, all damage taken is reduced by 9%. |
| **Anticipation** | 5 | — | changed | Increases your Defense Skill by 4. | Increases your Defense Skill by 20. |

### Tier 5 — requires 20 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Stoicism** | 2 | — | **NEW** | Reduces the duration of Stun and Charm effects on you by 20%. | Reduces the duration of Stun and Charm effects on you by 40%. *(est.)* |
| **Holy Shield** | 1 | — | changed | Increases chance to block by 30% for 10 sec, and deals 110 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges. | — |
| **Reckoning** | 5 | — | changed | Gives you a 8% chance after Blocking and a 20% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec. | Gives you a 40% chance after Blocking and a 100% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec. |

### Tier 6 — requires 25 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Iron Creed** | 3 | — | **NEW** | Increases the threat generated by your Holy Strike ability by 10%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 2% for 6 sec. | Increases the threat generated by your Holy Strike ability by 30%. While Righteous Fury is active, Holy Strike also reduces your damage taken by 6% for 6 sec. |

### Tier 7 — requires 30 points in Protection

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Shieldsworn** | 1 | Holy Shield (1) | **NEW** | Reduces the cooldown of your Holy Strike ability by 4 sec. Additionally, Holy Strike now strikes with your shield, triggering your active Holy Shield and Shield Specialization talents without consuming their charges or triggering their cooldowns, and allowing you to Block spells for 6 sec. | — |

**Removed from Classic Protection:** Improved Devotion Aura, Blessing of Kings, Improved Concentration Aura, Blessing of Sanctuary

## Retribution

### Tier 1 — requires 0 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Deflection** | 5 | — | moved | Increases your Parry chance by 1%. | Increases your Parry chance by 5%. |
| **Benediction** | 5 | — | changed | Reduces the Mana cost of all instant cast spells and abilities by 2%. | Reduces the Mana cost of all instant cast spells and abilities by 10%. |

### Tier 2 — requires 5 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Judgement** | 2 | — | changed | Decreases the cooldown of your Judgement ability by 1 sec. | Decreases the cooldown of your Judgement ability by 2 sec. |
| **Conviction** | 3 | — | changed | Improves your chance to get a critical strike with all spells and attacks by 2%. | Improves your chance to get a critical strike with all spells and attacks by 6%. |
| **Sanctified Judgement** | 3 | — | **NEW** | Gives your Judgement ability a 33% chance to return 20% of the Mana cost of the judged seal. | Gives your Judgement ability a 100% chance to return 60% of the Mana cost of the judged seal. |

### Tier 3 — requires 10 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Vindication** | 3 | — | changed | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68 for 30 sec. | Gives your damaging melee attacks a chance to reduce the target's Attack Power by 204 for 30 sec. |
| **Unyielding Faith** | 2 | — | changed | Reduces the duration of Fear and Disorient effects on you by 15%. | Reduces the duration of Fear and Disorient effects on you by 30%. |
| **Seal of Command** | 1 | — | changed | Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated. | — |
| **Pursuit of Justice** | 2 | — | changed | Increases movement speed and mounted movement speed by 8%. This does not stack with other movement speed increasing effects. | Increases movement speed and mounted movement speed by 15%. This does not stack with other movement speed increasing effects. |

### Tier 4 — requires 15 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Eye for an Eye** | 2 | — | changed | All critical strikes against you cause 5% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health. | All critical strikes against you cause 10% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health. |
| **Sacred Arbiter** | 1 | — | **NEW** | Increases the damage of your Holy Strike ability by 20% and causes it to refresh all Judgement effects on the target. | — |
| **Two-Handed Weapon Specialization** | 3 | — | unchanged | Increases the physical damage you deal by 2%, and reduces all threat you generate by 7% while a two-handed melee weapon is equipped. | Increases the physical damage you deal by 6%, and reduces all threat you generate by 20% while a two-handed melee weapon is equipped. |

### Tier 5 — requires 20 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Turn Evil** | 2 | — | **NEW** | Reduces the cast time of your Turn Undead spell by 1.5 sec, its cooldown by 2 sec, and allows it to affect Demons. | Reduces the cast time of your Turn Undead spell by 3 sec, its cooldown by 4 sec, and allows it to affect Demons. *(est.)* |
| **Repentance** | 1 | — | moved | Puts the enemy target in a state of meditation, incapacitating them for up to 6 sec. Any damage caused will awaken the target. Only works against Humanoids. | — |
| **Vengeance** | 3 | Seal of Command (1) | changed | Increases your Physical and Holy damage dealt by 1% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. | Increases your Physical and Holy damage dealt by 3% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times. |

### Tier 6 — requires 25 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Champion of the Light** | 5 | — | **NEW** | Increases your spell damage by up to 12% of your Intellect, and reduces the cast time of your Hammer of Wrath by 0.2 sec. | Increases your spell damage by up to 60% of your Intellect, and reduces the cast time of your Hammer of Wrath by 1.0 sec. |

### Tier 7 — requires 30 points in Retribution

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Unsealed Wrath** | 1 | Repentance (1) | **NEW** | Your melee attacks store a copy of your active Seal for 15 sec, stacking up to 3 times. Landing an attack with a different Seal consumes all stacks, giving the stored Seal its normal chance to activate once per stack. | — |

**Removed from Classic Retribution:** Improved Blessing of Might, Improved Seal of the Crusader, Improved Retribution Aura, Sanctity Aura

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Holy

- **Spiritual Focus** (max rank 5 → 2, tooltip changed, moved in build 1.60.1.70707: was row 2, col 2, max rank 2 -> 5 in build 1.60.1.70707, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5))
  - Classic: Gives your Flash of Light and Holy Light spells a 14% chance to not lose casting time when you take damage.
  - Forever: Gives your Flash of Light, Holy Light, and Light's Vigil spells a 14% chance to not lose casting time when you take damage.
- **Healing Light** (tooltip changed, was Holy row 3, col 1)
  - Classic: Increases the amount healed by your Holy Light and Flash of Light spells by 4%.
  - Forever: Increases the amount healed by your Holy Light, Flash of Light, and Holy Shock spells by 4%.
- **Illumination** (tooltip changed, moved in build 1.60.1.70707: was row 4, col 2)
  - Classic: After getting a critical effect from your Flash of Light, Holy Light, or Holy Shock heal spell, gives you a 20% chance to gain Mana equal to the base cost of the spell.
  - Forever: After getting a critical effect from your Flash of Light, Holy Light, Light's Vigil, or Holy Shock heal spell you have a 20% chance to gain Mana equal to 50% of the base cost of the spell.
- **Holy Shock** (tooltip changed, was Holy row 7, col 2)
  - Classic: Blasts the target with Holy energy, causing 220 Holy damage to an enemy, or 220 healing to an ally.
  - Forever: Blasts the target with Holy energy, causing 129 to 139 Holy damage to an enemy, or 110 to 118 healing to an ally.
- **Holy Power** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5))
  - Classic: Increases the critical effect chance of your Holy spells by 1%.
  - Forever: Increases the critical strike healing bonus of your Holy spells by 10%.

### Protection

- **Redoubt** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5))
  - Classic: Increases your chance to block attacks with your shield by 6% after being the victim of a critical strike. Lasts 10 sec or 5 blocks.
  - Forever: Damaging melee attacks against you have a 10% chance to increase your chance to block by 6%. Lasts 10 sec or 5 blocks.
- **Precision** (tooltip changed)
  - Classic: Increases your chance to hit with melee weapons by 1%.
  - Forever: Improves your chance to hit by 1%.
- **Guardian's Favor** (tooltip changed)
  - Classic: Reduces the cooldown of your Blessing of Protection by 60 sec and increases the duration of your Blessing of Freedom by 3 sec.
  - Forever: Reduces the cooldown of your Blessing of Protection by 1 min and increases the duration of your Blessing of Freedom by 3 sec.
- **Shield Specialization** (tooltip changed, max rank 3 -> 2 in build 1.60.1.70707, tooltip changed in build 1.60.1.70707 (ranks 1, 2))
  - Classic: Increases the amount of damage absorbed by your shield by 10%.
  - Forever: Increases the amount of damage absorbed by your shield by 15%, and gives your blocks a 50% chance to restore 4% of your maximum Mana. May only occur once every 3 sec. With Shieldsworn, a Holy Strike that lands with a shield rolls the same chance without the cooldown.
- **Improved Righteous Fury** (tooltip changed, moved in build 1.60.1.70707: was row 3, col 2, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Increases the amount of threat generated by your Righteous Fury spell by 16%.
  - Forever: While Righteous Fury is active, all damage taken is reduced by 3%.
- **Anticipation** (tooltip changed, was Protection row 3, col 4, moved in build 1.60.1.70707: was row 2, col 4)
  - Classic: Increases your Defense skill by 2.
  - Forever: Increases your Defense Skill by 4.
- **Holy Shield** (tooltip changed, moved in build 1.60.1.70707: was row 7, col 2, prerequisite changed in build 1.60.1.70707: was templar s bulwark)
  - Classic: Increases chance to block by 30% for 10 sec, and deals 65 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges.
  - Forever: Increases chance to block by 30% for 10 sec, and deals 110 Holy damage for each attack blocked while active. Damage caused by Holy Shield causes 20% additional threat. Each block expends a charge. 4 charges.
- **Reckoning** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3, 4, 5))
  - Classic: Gives you a 20% chance to gain an extra attack after being the victim of a critical strike.
  - Forever: Gives you a 8% chance after Blocking and a 20% chance after receiving a non-periodic critical strike to gain an extra attack. Stores up to 4 extra attacks. Cannot occur from Blocks more than once every 1.5 sec.

### Retribution

- **Benediction** (tooltip changed)
  - Classic: Reduces the Mana cost of your Judgement and Seal spells by 3%.
  - Forever: Reduces the Mana cost of all instant cast spells and abilities by 2%.
- **Improved Judgement** (tooltip changed)
  - Classic: Decreases the cooldown of your Judgement spell by 1 sec.
  - Forever: Decreases the cooldown of your Judgement ability by 1 sec.
- **Conviction** (tooltip changed, was Retribution row 3, col 2, moved in build 1.60.1.70707: was row 2, col 3, max rank 5 -> 3 in build 1.60.1.70707, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Increases your chance to get a critical strike with melee weapons by 1%.
  - Forever: Improves your chance to get a critical strike with all spells and attacks by 2%.
- **Vindication** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1, 2, 3))
  - Classic: Gives the Paladin's damaging melee attacks a chance to reduce the target's Strength and Agility by 5%10 sec.
  - Forever: Gives your damaging melee attacks a chance to reduce the target's Attack Power by 68 for 30 sec.
- **Unyielding Faith** (tooltip changed, was Holy row 3, col 4, moved in build 1.60.1.70707: was row 2, col 4)
  - Classic: Increases your chance to resist Fear and Disorient effects by an additional 5%.
  - Forever: Reduces the duration of Fear and Disorient effects on you by 15%.
- **Seal of Command** (tooltip changed, tooltip changed in build 1.60.1.70707 (ranks 1))
  - Classic: Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 51 Holy damage, 101 if the target is stunned or incapacitated.
  - Forever: Gives the Paladin a chance to deal additional Holy damage equal to 70% of normal weapon damage. Only one Seal can be active on the Paladin at any one time. Lasts 30 sec.  Unleashing this Seal's energy will judge an enemy, instantly causing 68 to 73 Holy damage, 137 to 145 if the target is stunned or incapacitated.
- **Pursuit of Justice** (tooltip changed)
  - Classic: Increases movement and mounted movement speed by 4%. This does not stack with other movement speed increasing effects.
  - Forever: Increases movement speed and mounted movement speed by 8%. This does not stack with other movement speed increasing effects.
- **Eye for an Eye** (tooltip changed)
  - Classic: All spell criticals against you cause 15% of the damage taken to the caster as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health.
  - Forever: All critical strikes against you cause 5% of the damage taken to the attacker as well. The damage caused by Eye for an Eye will not exceed 50% of the Paladin's total health.
- **Vengeance** (max rank 5 → 3, tooltip changed, was Retribution row 6, col 2, moved in build 1.60.1.70707: was row 5, col 2, prerequisite changed in build 1.60.1.70707: was sanctified judgement)
  - Classic: Gives you a 3% bonus to Physical and Holy damage you deal for 8 sec after dealing a critical strike from a weapon swing, spell, or ability.
  - Forever: Increases your Physical and Holy damage dealt by 1% for 30 sec after landing a non-periodic critical strike. Stacks up to 3 times.

---

*Generated from `_reference/data/forever-talents/paladin.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
