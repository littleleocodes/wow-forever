# Hunter — WoW: Forever talent trees (beta client 1.60.1.70753)

> **Data status:** WoW: Forever beta client build 1.60.1.70753, captured 2026-11-03. World of Warcraft: Forever beta client, build 1.60.1.70753: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-11-03, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70532; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.70205, captured 2026-10-04). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Beast Mastery | 16 | 3 | 8 | 1 | 4 | 3 |
| Marksmanship | 16 | 7 | 5 | 2 | 2 | 5 |
| Survival | 18 | 8 | 7 | 0 | 3 | 6 |

## Beast Mastery

### Tier 1 — requires 0 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Deadly Aspects** | 5 | — | **NEW** | While Aspect of the Hawk is active, Auto Shot has a 2% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 2% chance of increasing melee attack speed by 30% for 12 sec. | While Aspect of the Hawk is active, Auto Shot has a 10% chance of increasing ranged attack speed by 30% for 12 sec. While Aspect of the Beast is active, all melee auto attacks have a 10% chance of increasing melee attack speed by 30% for 12 sec. |
| **Endurance Training** | 5 | — | changed | Increases the Health and Armor of your pets by 3%. | Increases the Health and Armor of your pets by 15%. |

### Tier 2 — requires 5 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Focused Fire** | 2 | — | **NEW** | Increases all damage you and your pet deal by 1% while your pet is active. | Increases all damage you and your pet deal by 2% while your pet is active. |
| **Improved Aspect of the Monkey** | 3 | — | changed | Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. | Increases the Dodge bonus of your Aspect of the Monkey by 6%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability. |
| **Improved Revive Pet** | 2 | — | unchanged | Revive Pet's casting time is reduced by 3 sec, mana cost is reduced by 20%, and increases the health your pet returns with by an additional 15%. | Revive Pet's casting time is reduced by 6 sec, mana cost is reduced by 40%, and increases the health your pet returns with by an additional 30%. |

### Tier 3 — requires 10 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Pathfinding** | 2 | — | moved | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 3%. | Increases the speed bonus of your Aspect of the Cheetah and Aspect of the Pack by 6%. |
| **Bestial Swiftness** | 1 | — | changed | Increases the movement speed of your pets by 30%. | — |
| **Unleashed Fury** | 5 | — | changed | Increases the damage done by your pets and hawks by 3%. | Increases the damage done by your pets and hawks by 15%. |

### Tier 4 — requires 15 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Mend Pet** | 2 | — | changed | Gives your Mend Pet spell a 15% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 10%. | Gives your Mend Pet spell a 50% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 20%. |
| **Ferocity** | 5 | — | changed | Increases the critical strike chance of your pets and hawks by 2%. | Increases the critical strike chance of your pets and hawks by 10%. |
| **Summon Hawk** | 1 | — | **NEW** | Command a hawk to dive-bomb your targeted enemy, dealing 32 plus 5% of your Ranged Attack Power Physical damage and continuing its assault for 18 sec. Only 2 hawks can be active at once. Summon Hawk shares its cooldown with Arcane Shot. | — |

### Tier 5 — requires 20 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Spirit Bond** | 2 | — | unchanged | While your pet is active, you and your pet will regenerate 1% of total health every 10 sec. | While your pet is active, you and your pet will regenerate 1% of total health every 5 sec. |
| **Intimidation** | 1 | Bestial Swiftness (1) | changed | Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat. | — |
| **Bestial Discipline** | 2 | — | changed | Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting. | Increases the Focus regeneration of your pets by 20% and allows 50% of your Mana regeneration to continue while casting. |

### Tier 6 — requires 25 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Frenzy** | 5 | Ferocity (5) | unchanged | Gives your pet a 20% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. | Gives your pet a 100% chance to gain a 30% attack speed increase for 8 sec after dealing a critical strike. |

### Tier 7 — requires 30 points in Beast Mastery

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Bestial Wrath** | 1 | Intimidation (1) | unchanged | Send your pet into a rage causing 50% additional damage for 18 sec. While enraged, the beast does not feel pity or remorse or fear and it cannot be stopped unless killed. | — |

**Removed from Classic Beast Mastery:** Improved Aspect of the Hawk, Improved Eyes of the Beast, Thick Hide

## Marksmanship

### Tier 1 — requires 0 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Hawk Eye** | 3 | — | moved | Increases the range of your ranged weapons by 2 yards. | Increases the range of your ranged weapons by 6 yards. |
| **Improved Concussive Shot** | 5 | — | unchanged | Gives your Concussive Shot a 4% chance to stun the target for 3 sec. | Gives your Concussive Shot a 20% chance to stun the target for 3 sec. |
| **Lethal Attacks** | 5 | — | **NEW** | Increases your critical strike chance with all attacks by 1%. | Increases your critical strike chance with all attacks by 5%. |

### Tier 2 — requires 5 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Stings** | 3 | — | **NEW** | Increases the damage of your Serpent Sting ability by 6%, reduces the cooldown of your Viper Sting ability by 2 sec, and increases the duration of your Scorpid Sting ability by 15 sec. | Increases the damage of your Serpent Sting ability by 20%, reduces the cooldown of your Viper Sting ability by 6 sec, and increases the duration of your Scorpid Sting ability by 45 sec. |
| **Efficiency** | 5 | — | changed | Reduces the Mana cost of your Shots, Stings, and melee abilities by 3%. | Reduces the Mana cost of your Shots, Stings, and melee abilities by 15%. |
| **Careful Aim** | 5 | — | **NEW** | Increases your Attack Power by 20% of your Intellect. | Increases your Attack Power by 100% of your Intellect. |

### Tier 3 — requires 10 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Rapid Killing** | 2 | — | **NEW** | Reduces the cooldown on your Rapid Fire ability by 1 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 10%. | Reduces the cooldown on your Rapid Fire ability by 2 min. In addition, when you kill a non-trivial enemy or it dies while afflicted by your Serpent Sting, you gain Rapid Killing, increasing the damage of your next Shot ability within 20 sec by 20%. |
| **Improved Arcane Shot** | 5 | — | changed | Reduces the cooldown of your Arcane Shot by 0.3 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. | Reduces the cooldown of your Arcane Shot by 1.5 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot. |
| **Lone Wolf** | 1 | — | **NEW** | You deal 20% increased damage with all attacks while you do not have an active pet. | — |

### Tier 4 — requires 15 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Trueshot Aura** | 1 | — | changed | Increases the Ranged Attack Power of party or raid members within 45 yds by 20. | — |
| **Mortal Shots** | 5 | Careful Aim (5) | changed | Increases the critical strike damage bonus on all ranged abilities by 6%. | Increases the critical strike damage bonus on all ranged abilities by 30%. |

### Tier 5 — requires 20 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Rapid Recuperation** | 2 | Rapid Killing (2) | **NEW** | Afflicting a target with Serpent Sting allows 25% of your Mana Regeneration to continue while casting for 15 sec, increased to 50% when Rapid Killing is consumed. | Afflicting a target with Serpent Sting allows 50% of your Mana Regeneration to continue while casting for 15 sec, increased to 100% when Rapid Killing is consumed. |
| **Barrage** | 3 | — | changed | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 5%. | Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 15%. |
| **Scatter Shot** | 1 | — | moved | A short-range shot that deals 50% weapon damage and disorients the target for 4 sec. Any damage caused will remove the effect. Turns off your attack when used. | — |

### Tier 6 — requires 25 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ranged Weapon Specialization** | 5 | — | unchanged | Increases the damage you deal with ranged weapons by 1%. | Increases the damage you deal with ranged weapons by 5%. |

### Tier 7 — requires 30 points in Marksmanship

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Sniper Shot** | 1 | Trueshot Aura (1) | **NEW** | A long-range shot that deals ranged damage plus 160 and increases the range of your next 3 Shots by 10 yards for 10 sec. | — |

**Removed from Classic Marksmanship:** Improved Hunter's Mark, Lethal Shots, Aimed Shot, Improved Serpent Sting, Improved Scorpid Sting

## Survival

### Tier 1 — requires 0 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Tracking** | 5 | — | **NEW** | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 1%. | While tracking Beasts, Demons, Dragonkin, Elementals, Giants, Humanoids, or Undead, all damage you deal to the tracked creature type is increased by 5%. |
| **Deflection** | 5 | — | unchanged | Increases your Parry chance by 1%. | Increases your Parry chance by 5%. |

### Tier 2 — requires 5 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Entrapment** | 5 | — | changed | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec. | When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 5 sec. |
| **Savage Strikes** | 2 | — | changed | Increases the critical strike chance of all your melee abilities by 2%. | Increases the critical strike chance of all your melee abilities by 4%. |
| **Survivalist** | 5 | — | changed | Increases your total Health by 2%. | Increases your total Health by 10%. |
| **Improved Wing Clip** | 3 | — | changed | Gives your Wing Clip ability a 7% chance to immobilize the target for 5 sec. | Gives your Wing Clip ability a 20% chance to immobilize the target for 5 sec. |

### Tier 3 — requires 10 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Clever Traps** | 2 | — | unchanged | Increases the duration of Freezing and Frost trap effects by 15% and the damage of Immolation and Explosive trap effects by 15%. | Increases the duration of Freezing and Frost trap effects by 30% and the damage of Immolation and Explosive trap effects by 30%. |
| **Surefooted** | 3 | — | changed | Increases your hit chance by 1% and reduces the duration of movement impairing effects on you by 10%. | Increases your hit chance by 3% and reduces the duration of movement impairing effects on you by 30%. |
| **Deterrence** | 1 | — | unchanged | When activated, increases your Dodge and Parry chance by 25% for 10 sec. | — |

### Tier 4 — requires 15 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Survival Tactics** | 2 | — | **NEW** | Increases your chance to hit with your Trap and Feign Death abilities by 5%. | Increases your chance to hit with your Trap and Feign Death abilities by 10%. |
| **Predator's Edge** | 5 | — | **NEW** | Increases your melee ability critical strike damage by 6% and your Off Hand weapon damage by 10%. | Increases your melee ability critical strike damage by 30% and your Off Hand weapon damage by 50%. |
| **Counterattack** | 1 | Deterrence (1) | changed | A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried. | — |

### Tier 5 — requires 20 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Resourcefulness** | 2 | — | **NEW** | Reduces the Mana cost of your Trap and melee abilities by 30%, and grants your melee and ranged ability Critical Strikes a 50% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. | Reduces the Mana cost of your Trap and melee abilities by 60%, and grants your melee and ranged ability Critical Strikes a 100% chance to allow 50% of your Mana Regeneration to continue while casting for 30 sec. |
| **Expose Prey** | 2 | — | **NEW** | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 5% chance to allow an activation of Mongoose Bite. Lasts 10 sec. | Grants your melee and ranged attacks against enemies afflicted by Hunter's Mark a 10% chance to allow an activation of Mongoose Bite. Lasts 10 sec. |
| **Survivalist's Discipline** | 2 | — | **NEW** | Reduces the cooldown of your Trap and Deterrence abilities by 20%. | Reduces the cooldown of your Trap and Deterrence abilities by 40%. |
| **Strider Kick** | 1 | — | **NEW** | A powerful kick that deals 100% melee weapon damage and increases movement speed by 30% for 3 sec. | — |

### Tier 6 — requires 25 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Lightning Reflexes** | 5 | — | changed | Increases your Agility by 3%. | Increases your Agility by 15%. |

### Tier 7 — requires 30 points in Survival

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Lacerating Strikes** | 1 | Expose Prey (2) | **NEW** | Your Mongoose Bite also causes the target to Bleed for damage equal to 40% of the damage done by Mongoose Bite over 21 sec | — |

**Removed from Classic Survival:** Monster Slaying, Humanoid Slaying, Trap Mastery, Improved Feign Death, Killer Instinct, Wyvern Sting

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Beast Mastery

- **Endurance Training** (tooltip changed)
  - Classic: Increases the Health of your pets by 3%.
  - Forever: Increases the Health and Armor of your pets by 3%.
- **Improved Aspect of the Monkey** (max rank 5 → 3, tooltip changed)
  - Classic: Increases the Dodge bonus of your Aspect of the Monkey by 1%.
  - Forever: Increases the Dodge bonus of your Aspect of the Monkey by 2%. Additionally, your pet gains 50% of the effect of your Aspect of the Monkey ability.
- **Bestial Swiftness** (tooltip changed)
  - Classic: Increases the outdoor movement speed of your pets by 30%.
  - Forever: Increases the movement speed of your pets by 30%.
- **Unleashed Fury** (tooltip changed)
  - Classic: Increases the damage done by your pets by 4%.
  - Forever: Increases the damage done by your pets and hawks by 3%.
- **Improved Mend Pet** (tooltip changed, was Beast Mastery row 4, col 2)
  - Classic: Gives the Mend Pet spell a 15% chance of cleansing 1 Curse, Disease, Magic or Poison effect from the pet each tick.
  - Forever: Gives your Mend Pet spell a 15% chance of cleansing 1 Curse, Disease, Magic, or Poison effect from your pet each time it heals and reduces the Mana cost by 10%.
- **Ferocity** (tooltip changed)
  - Classic: Increases the critical strike chance of your pets by 3%.
  - Forever: Increases the critical strike chance of your pets and hawks by 2%.
- **Intimidation** (tooltip changed)
  - Classic: Command your pet to intimidate the target on the next successful melee attack, causing a high amount of threat and stunning the target for 3 sec.
  - Forever: Command your pet to Stun the target for 3 sec on its next successful attack, which also gains 100% increased critical strike chance. Generates high threat.
- **Bestial Discipline** (tooltip changed)
  - Classic: Increases the Focus regeneration of your pets by 10%.
  - Forever: Increases the Focus regeneration of your pets by 10% and allows 25% of your Mana regeneration to continue while casting.

### Marksmanship

- **Efficiency** (tooltip changed, was Marksmanship row 1, col 3)
  - Classic: Reduces the Mana cost of your Shots and Stings by 2%.
  - Forever: Reduces the Mana cost of your Shots, Stings, and melee abilities by 3%.
- **Improved Arcane Shot** (tooltip changed)
  - Classic: Reduces the cooldown of your Arcane Shot by 0 sec.
  - Forever: Reduces the cooldown of your Arcane Shot by 0.3 sec. Does not affect the cooldown of abilities which share a cooldown with Arcane Shot.
- **Trueshot Aura** (tooltip changed, was Marksmanship row 7, col 2, tooltip changed in build 1.60.1.70753 (ranks 1))
  - Classic: Increases the attack power of party members within 0 yards by 50. Lasts 30 min.
  - Forever: Increases the Ranged Attack Power of party or raid members within 45 yds by 20.
- **Mortal Shots** (tooltip changed)
  - Classic: Increases your ranged weapon critical strike damage bonus by 6%.
  - Forever: Increases the critical strike damage bonus on all ranged abilities by 6%.
- **Barrage** (tooltip changed, was Marksmanship row 5, col 2, tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3))
  - Classic: Increases the damage done by your Multi-Shot and Volley spells by 5%.
  - Forever: Increases the damage done by your Multi-Shot, Aimed Shot, and Volley abilities by 5%.

### Survival

- **Entrapment** (tooltip changed)
  - Classic: Gives your Immolation Trap, Frost Trap, and Explosive Trap a 5% chance to entrap the target, preventing them from moving for 5 sec.
  - Forever: When your traps are triggered, all affected targets are Entrapped, preventing them from moving for 1 sec.
- **Savage Strikes** (tooltip changed)
  - Classic: Increases the critical strike chance of Raptor Strike and Mongoose Bite by 10%.
  - Forever: Increases the critical strike chance of all your melee abilities by 2%.
- **Survivalist** (tooltip changed, was Survival row 3, col 2)
  - Classic: Increases total health by 2%.
  - Forever: Increases your total Health by 2%.
- **Improved Wing Clip** (max rank 5 → 3, tooltip changed, was Survival row 2, col 3)
  - Classic: Gives your Wing Clip ability a 4% chance to immobilize the target for 5 sec.
  - Forever: Gives your Wing Clip ability a 7% chance to immobilize the target for 5 sec.
- **Surefooted** (tooltip changed, was Survival row 4, col 2)
  - Classic: Increases hit chance by 1% and increases the chance movement impairing effects will be resisted by an additional 5%.
  - Forever: Increases your hit chance by 1% and reduces the duration of movement impairing effects on you by 10%.
- **Counterattack** (tooltip changed, was Survival row 5, col 3, tooltip changed in build 1.60.1.70753 (ranks 1))
  - Classic: A strike that becomes active after parrying an opponent's attack. This attack deals 40 damage and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried.
  - Forever: A strike that becomes active after parrying an opponent's attack. This attack deals 50% weapon damage plus 13 and immobilizes the target for 5 sec. Counterattack cannot be blocked, dodged, or parried.
- **Lightning Reflexes** (tooltip changed, tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5))
  - Classic: Increases your Agility by 3%.
  - Forever: Increases your Agility by 3%.

---

*Generated from `_reference/data/forever-talents/hunter.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
