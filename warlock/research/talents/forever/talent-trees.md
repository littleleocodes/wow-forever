# Warlock — WoW: Forever talent trees (beta client 1.60.1.70753)

> **Data status:** WoW: Forever beta client build 1.60.1.70753, captured 2026-11-03. World of Warcraft: Forever beta client, build 1.60.1.70753: per-rank tooltips (level 60, no gear), rank caps and positions from talentsforever.com's data export (generated 2026-11-03, CC BY 4.0); positions and prerequisite arrows cross-checked against thewowdb.com's Trait-table snapshot of build 1.60.1.70532; talent ids, Classic status/diff/tooltips and removed-Classic-talent lists from warcraftforever.games (beta client 1.60.1.70205, captured 2026-10-04). Earlier snapshot: BlizzCon 2026 demo transcription captured 2026-09-13 (archived under raw/2026-09-13-demo). Every rank's tooltip is the client's (level-60 values, no gear); talents whose text changed between beta builds keep the older text in the JSON (`ranks_prev`). **Everything here can change before the November 4, 2026 launch** — re-verify against the live game or the [Wowhead Forever calculator](https://www.wowhead.com/forever/talent-calc) before locking a build.

> Tier rule (same as Classic): tier *n* unlocks after 5 × (*n* − 1) points in that tree. 51 points total at level 60. Prerequisites are listed where the calculator shows an arrow.

## At a glance

| Tree | Talents | New | Changed | Moved | Unchanged | Removed from Classic |
|---|---|---|---|---|---|---|
| Affliction | 17 | 8 | 8 | 1 | 0 | 7 |
| Demonology | 19 | 8 | 8 | 1 | 2 | 6 |
| Destruction | 16 | 6 | 10 | 0 | 0 | 6 |

## Affliction

### Tier 1 — requires 0 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Life Tap** | 2 | — | moved | Increases the amount of Mana awarded by your Life Tap spell by 10%. | Increases the amount of Mana awarded by your Life Tap spell by 20%. |
| **Suppression** | 5 | — | changed | Improves your chance to hit by 1% and reduces all threat you generate by 4%. | Improves your chance to hit by 5% and reduces all threat you generate by 20%. |
| **Improved Corruption** | 5 | — | changed | Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%. | Reduces the casting time of your Corruption spell by 2 sec and increases the damage it deals by 10%. |

### Tier 2 — requires 5 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Grim Reach** | 2 | — | **NEW** | Increases the range of your Affliction spells by 10%. | Increases the range of your Affliction spells by 20%. |
| **Soul Harvest** | 2 | — | **NEW** | Killing a non-trivial target afflicted by your Drain Soul increases your Mana regeneration by 50% for 10 sec and allows 50% of normal Mana regeneration to continue while casting. | Killing a non-trivial target afflicted by your Drain Soul increases your Mana regeneration by 100% for 10 sec and allows 100% of normal Mana regeneration to continue while casting. |
| **Improved Drains** | 3 | — | **NEW** | Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 7%. | Increases Health drained, damage done, or Mana drained by your Drain Life, Drain Soul, and Drain Mana spells by 20%. |

### Tier 3 — requires 10 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Bane of Agony** | 2 | — | **NEW** | Increases the damage done by your Bane of Agony by 5%. | Increases the damage done by your Bane of Agony by 10%. |
| **Fel Concentration** | 3 | — | changed | Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 23% chance to not lose casting time when you take damage. | Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 70% chance to not lose casting time when you take damage. |
| **Amplify Curse** | 1 | — | changed | Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec. | — |
| **Pandemic** | 3 | — | **NEW** | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 33%. | Increases the critical strike damage bonus of your Corruption, Bane of Agony, Bane of Doom, Drain Soul, Drain Life, Siphon Life, and Wrack spells by 100%. |

### Tier 4 — requires 15 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Malevolence** | 5 | — | **NEW** | Increases the critical effect chance of your Shadow spells by 1%. | Increases the critical effect chance of your Shadow spells by 5%. |
| **Nightfall** | 2 | — | changed | Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 2% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. | Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 4% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%. |
| **Curse of Exhaustion** | 1 | Amplify Curse (1) | changed | Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target. | — |

### Tier 5 — requires 20 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Siphon Life** | 1 | — | changed | Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec. | — |
| **Soul Siphon** | 3 | — | **NEW** | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 4% per each of your other Affliction effects active on the target, up to a maximum increase of 12%. | Increases the damage done or health drained by your Drain Life, Drain Soul, and Wrack spells by 12% per each of your other Affliction effects active on the target, up to a maximum increase of 36%. |

### Tier 6 — requires 25 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Shadow Mastery** | 5 | — | changed | Increases the damage dealt or life drained by your Shadow spells by 2%. | Increases the damage dealt or life drained by your Shadow spells by 10%. |

### Tier 7 — requires 30 points in Affliction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Wrack** | 1 | Siphon Life (1) | **NEW** | Tears the target apart from within, inflicting 86 Shadow damage every 1 sec and increasing the damage they take from your other Shadow damage over time effects by 10% for 6 sec. | — |

**Removed from Classic Affliction:** Improved Curse of Weakness, Improved Drain Soul, Improved Drain Life, Improved Curse of Agony, Improved Drain Mana, Improved Curse of Exhaustion, Dark Pact

## Demonology

### Tier 1 — requires 0 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Health Funnel** | 2 | — | changed | Increases the amount of health transferred by your Health Funnel spell by 20%, reduces its health cost by 15%, and reduces all threat your Health Funnel generates by 50%. Allows Health Funnel to be used regardless of your demon's health. | Increases the amount of health transferred by your Health Funnel spell by 40%, reduces its health cost by 30%, and reduces all threat your Health Funnel generates by 100%. Allows Health Funnel to be used regardless of your demon's health. |
| **Improved Imp** | 3 | — | changed | Increases the damage of your Imp's Firebolt spell by 10% and the effect of its Fire Shield spell by 10%. | Increases the damage of your Imp's Firebolt spell by 30% and the effect of its Fire Shield spell by 30%. |
| **Demonic Embrace** | 5 | — | changed | Increases your total Stamina by 3%. | Increases your total Stamina by 15%. |
| **Unholy Power** | 5 | — | changed | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 2%. | Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 10%. |

### Tier 2 — requires 5 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Demonic Aegis** | 2 | — | **NEW** | Increases the effectiveness of your Demon Skin and Demon Armor spells by 15%. | Increases the effectiveness of your Demon Skin and Demon Armor spells by 30%. |
| **Improved Voidwalker** | 3 | — | unchanged | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 10%. | Increases the effectiveness of your Voidwalker's Torment, Consume Shadows, Sacrifice, and Suffering spells by 30%. |
| **Fel Vitality** | 3 | — | **NEW** | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 5%, and increases your maximum Mana by 5%. | Increases the maximum health and Mana of your Imp, Voidwalker, Succubus, Incubus, and Felhunter by 15%, and increases your maximum Mana by 15%. |
| **Demonic Energies** | 2 | — | **NEW** | You heal your pet for 8% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 50% of the Mana you gain. | You heal your pet for 15% of all spell damage you deal. When you gain Mana from Life Tap, your summoned demon gains 100% of the Mana you gain. |

### Tier 3 — requires 10 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Sayaad** | 3 | — | unchanged | Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 10%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 10%. | Increases the effect of your Succubus' and Incubus' Lash of Pain and Soothing Kiss spells by 30%, and increases the duration of your Succubus' and Incubus' Seduction and Lesser Invisibility spells by 30%. |
| **Demonic Sacrifice** | 1 | — | changed | When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec. | — |
| **Master Summoner** | 2 | — | moved | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 2 sec and the Mana cost by 20%. | Reduces the casting time of your Imp, Voidwalker, Succubus, Incubus, and Felhunter Summoning spells by 4 sec and the Mana cost by 40%. |

### Tier 4 — requires 15 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Decimation** | 2 | — | **NEW** | Reduces the cooldown of your Soul Fire spell by 45%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 3% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 20% and costs no Soul Shards. | Reduces the cooldown of your Soul Fire spell by 90%. When you cast Shadow Bolt or Searing Pain on an enemy below 35% health, they deal 6% increased damage, and for the next 10 sec your Soul Fire spell has its cast time reduced by 40% and costs no Soul Shards. |
| **Fel Domination** | 1 | Master Summoner (2) | changed | Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%. | — |
| **Demonic Brand** | 3 | — | **NEW** | Your Searing Pain generates 17% less threat and brands the target for 10 sec. Your pet's next 2 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. | Your Searing Pain generates 50% less threat and brands the target for 10 sec. Your pet's next 6 attacks against the target deal 65 to 68 Fire or Shadow damage based on the pet. If Shadow damage is dealt, it has high threat. |

### Tier 5 — requires 20 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Improved Felhunter** | 3 | — | **NEW** | Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 10%, and reduces the cooldown of its Spell Lock by 2 sec. | Increases the Attack Power reduction of your Felhunter's Tainted Blood, the healing of its Devour Magic, and the detection level of its Paranoia by 30%, and reduces the cooldown of its Spell Lock by 6 sec. |
| **Soul Link** | 1 | Demonic Sacrifice (1) | changed | When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active. | — |
| **Demonic Knowledge** | 3 | — | **NEW** | Increases your spell damage and your Demon pet's spell damage by up to 33% of your level while you have a summoned Demon pet active. | Increases your spell damage and your Demon pet's spell damage by up to 100% of your level while you have a summoned Demon pet active. |

### Tier 6 — requires 25 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Master Demonologist** | 5 | — | changed | Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 2%.  Voidwalker - Reduces Physical damage taken by 2%.  Succubus/Incubus - Increases Shadow damage done by 2%.  Felhunter - Reduces Magic damage taken by 2%. | Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 10%.  Voidwalker - Reduces Physical damage taken by 10%.  Succubus/Incubus - Increases Shadow damage done by 10%.  Felhunter - Reduces Magic damage taken by 10%. |

### Tier 7 — requires 30 points in Demonology

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Demonic Pact** | 1 | Soul Link (1) | **NEW** | Your Demonic Sacrifice effect is no longer cancelled by summoning a different Demon pet. Resummoning the sacrificed pet will still cancel the effect. | — |

**Removed from Classic Demonology:** Improved Healthstone, Fel Intellect, Fel Stamina, Improved Subjugate Demon, Improved Firestone, Improved Spellstone

## Destruction

### Tier 1 — requires 0 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Destructive Reach** | 2 | — | changed | Increases the range of your Destruction spells by 10%. | Increases the range of your Destruction spells by 20%. |
| **Improved Shadow Bolt** | 5 | — | changed | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec. | Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 20% for 12 sec. |
| **Bane** | 5 | — | changed | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.1 sec and your Soul Fire spell by 0.4 sec. | Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.5 sec and your Soul Fire spell by 2 sec. |

### Tier 2 — requires 5 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Molten Skin** | 5 | — | **NEW** | Reduces all damage taken by 2%. | Reduces all damage taken by 10%. |
| **Cataclysm** | 3 | — | changed | Reduces the Mana cost of your Destruction spells by 3%. | Reduces the Mana cost of your Destruction spells by 10%. |
| **Aftermath** | 5 | — | changed | Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. | Increases the initial damage of your Immolate spell by 50% and your Conflagrate spell has a 100% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec. |

### Tier 3 — requires 10 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Ruin** | 5 | — | changed | Increases the critical strike damage bonus of your Destruction spells by 20%. | Increases the critical strike damage bonus of your Destruction spells by 100%. |
| **Shadowburn** | 1 | — | changed | Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard. | — |

### Tier 4 — requires 15 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Intensity** | 3 | — | changed | Gives your Destruction spells a 23% chance to not lose casting time when you take damage. | Gives your Destruction spells a 70% chance to not lose casting time when you take damage. |
| **Agonizing Flames** | 3 | — | **NEW** | Increases the critical strike chance of your Searing Pain spell by 3% and the damage done by all your Destruction spells by 3%. | Increases the critical strike chance of your Searing Pain spell by 10% and the damage done by all your Destruction spells by 10%. |
| **Conflagrate** | 1 | — | changed | Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect. | — |

### Tier 5 — requires 20 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Pyroclasm** | 2 | Intensity (3) | changed | Gives your Soul Fire spell a 13% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13% chance over their duration to Stun targets they damage for 3 sec. | Gives your Soul Fire spell a 26% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 26% chance over their duration to Stun targets they damage for 3 sec. |
| **Bane of Havoc** | 1 | — | **NEW** | Afflicts the target for 5 min, causing 15% of all damage done by the Warlock to other targets to also be dealt to the cursed target. Bane of Havoc is limited to 1 target, and only one Bane per Warlock can be active on any one target. | — |
| **Fire and Brimstone** | 3 | Conflagrate (1) | **NEW** | Increases the critical strike chance of your Conflagrate spell by 8%. | Increases the critical strike chance of your Conflagrate spell by 25%. |

### Tier 6 — requires 25 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Shadow and Flame** | 5 | — | **NEW** | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 4% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 4% for 20 sec. In addition, Conflagrate has a 20% chance not to consume Immolate, and Shadowburn has a 20% chance to instantly refund a Soul Shard. | Hitting an enemy with Conflagrate increases all Shadow damage you deal by 20% for 20 sec, and hitting an enemy with Shadowburn increases all Fire damage you deal by 20% for 20 sec. In addition, Conflagrate has a 100% chance not to consume Immolate, and Shadowburn has a 100% chance to instantly refund a Soul Shard. |

### Tier 7 — requires 30 points in Destruction

| Talent | Pts | Requires | vs Classic | Rank 1 | Max rank |
|---|---|---|---|---|---|
| **Incinerate** | 1 | Bane of Havoc (1) | **NEW** | Deals 99 to 113 Fire damage to your target and an additional 25% damage if the target is afflicted by Immolate. | — |

**Removed from Classic Destruction:** Improved Firebolt, Improved Lash of Pain, Devastation, Improved Searing Pain, Improved Immolate, Emberstorm

## Changes vs Classic Era (talent by talent)

Only talents whose tooltip differs from Classic are listed. Text is rank 1 unless noted.

### Affliction

- **Suppression** (tooltip changed)
  - Classic: Reduces the chance for enemies to resist your Affliction spells by 2%.
  - Forever: Improves your chance to hit by 1% and reduces all threat you generate by 4%.
- **Improved Corruption** (tooltip changed)
  - Classic: Reduces the casting time of your Corruption spell by 0 sec.
  - Forever: Reduces the casting time of your Corruption spell by 0.4 sec and increases the damage it deals by 2%.
- **Fel Concentration** (max rank 5 → 3, tooltip changed, tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3))
  - Classic: Gives you a 14% chance to avoid interruption caused by damage while channeling the Drain Life, Drain Mana, or Drain Soul spell.
  - Forever: Gives your Drain Life, Drain Mana, Drain Soul, and Wrack spells a 23% chance to not lose casting time when you take damage.
- **Amplify Curse** (tooltip changed)
  - Classic: Increases the effect of your next Curse of Weakness or Curse of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec.
  - Forever: Increases the effect of your next Curse of Weakness or Bane of Agony by 50%, or your next Curse of Exhaustion by 20%. Lasts 30 sec.
- **Nightfall** (tooltip changed)
  - Classic: Gives your Corruption and Drain Life spells a 2% chance to cause you to enter a Shadow Trance state after damaging the opponent. The Shadow Trance state reduces the casting time of your next Shadow Bolt spell by 100%.
  - Forever: Gives your Corruption, Drain Soul, Drain Life, and Wrack spells a 2% chance to cause you to enter a Shadow Trance after damaging the opponent. The Shadow Trance reduces the casting time of your next Shadow Bolt spell by 100%.
- **Curse of Exhaustion** (tooltip changed, was Affliction row 5, col 3)
  - Classic: Reduces the target's movement speed by 10% for 12 sec. Only one Curse per Warlock can be active on any one target.
  - Forever: Reduces the target's movement speed by 30% for 12 sec. Only one Curse per Warlock can be active on any one target.
- **Siphon Life** (tooltip changed)
  - Classic: Transfers 15 health from the target to the caster every 3 sec. Lasts 30 sec.
  - Forever: Transfers 11 health from the target to the caster every 3 sec. Lasts 30 sec.
- **Shadow Mastery** (tooltip changed, was Affliction row 6, col 2, tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3, 4, 5))
  - Classic: Increases the damage dealt or life drained by your Shadow spells by 2%.
  - Forever: Increases the damage dealt or life drained by your Shadow spells by 2%.

### Demonology

- **Improved Health Funnel** (tooltip changed, was Demonology row 2, col 1)
  - Classic: Increases the amount of Health transferred by your Health Funnel spell by 10%.
  - Forever: Increases the amount of health transferred by your Health Funnel spell by 20%, reduces its health cost by 15%, and reduces all threat your Health Funnel generates by 50%. Allows Health Funnel to be used regardless of your demon's health.
- **Improved Imp** (tooltip changed)
  - Classic: Increases the effect of your Imp's Firebolt, Fire Shield, and Blood Pact spells by 10%.
  - Forever: Increases the damage of your Imp's Firebolt spell by 10% and the effect of its Fire Shield spell by 10%.
- **Demonic Embrace** (tooltip changed)
  - Classic: Increases your total Stamina by 3% but reduces your total Spirit by 1%.
  - Forever: Increases your total Stamina by 3%.
- **Unholy Power** (tooltip changed, was Demonology row 4, col 3)
  - Classic: Increases the damage done by your Voidwalker, Succubus, Incubus, and Felhunter's melee attacks by 4%.
  - Forever: Increases all damage done by your Imp, Voidwalker, Succubus, Incubus, and Felhunter pets by 2%.
- **Demonic Sacrifice** (tooltip changed, was Demonology row 5, col 2, tooltip changed in build 1.60.1.70753 (ranks 1))
  - Classic: When activated, sacrifices your summoned demon to grant you an effect that lasts 30 min. The effect is canceled if any Demon is summoned.  Imp: Increases your Fire damage by 15%.  Voidwalker: Restores 3% of total Health every 4 sec.  Succubus/Incubus: Increases your Shadow damage by 15%.  Felhunter: Restores 2% of total Mana every 4 sec.
  - Forever: When activated, sacrifices your summoned Demon to enhance the opposing aspect of your power, granting you an effect that lasts 2 hrs. The effect is canceled if any Demon is summoned.  Imp: Increases your Shadow damage by 15%.  Voidwalker: Restores 2% of your total Mana every 4 sec.  Succubus/Incubus: Increases your Fire damage by 15%.  Felhunter: Restores 3% of your total Health every 4 sec.
- **Fel Domination** (tooltip changed, was Demonology row 3, col 2)
  - Classic: Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 6 sec and its Mana cost reduced by 50%.
  - Forever: Your next Imp, Voidwalker, Succubus, Incubus, or Felhunter Summon spell has its casting time reduced by 5.5 sec and its Mana cost reduced by 50%.
- **Soul Link** (tooltip changed, was Demonology row 7, col 2)
  - Classic: When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter demon instead. In addition, both the demon and master will inflict 3% more damage. Lasts as long as the demon is active.
  - Forever: When active, 30% of all damage taken by the caster is taken by your Imp, Voidwalker, Succubus, Incubus, or Felhunter Demon instead. In addition, both the Demon and the master will inflict 3% more damage. Lasts as long as the Demon is active.
- **Master Demonologist** (tooltip changed)
  - Classic: Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Reduces. threat caused by 4%.  Voidwalker - Reduces physical damage taken by 2%.  Succubus/Incubus - Increases all damage caused by 2%.  Felhunter - Increases all resistances by .2 per level.
  - Forever: Grants both the Warlock and the summoned demon an effect as long as that demon is active.  Imp - Increases Fire damage done by 2%.  Voidwalker - Reduces Physical damage taken by 2%.  Succubus/Incubus - Increases Shadow damage done by 2%.  Felhunter - Reduces Magic damage taken by 2%.

### Destruction

- **Destructive Reach** (tooltip changed, was Destruction row 4, col 2, tooltip changed in build 1.60.1.70753 (ranks 1, 2))
  - Classic: Increases the range of your Destruction spells by 10%.
  - Forever: Increases the range of your Destruction spells by 10%.
- **Improved Shadow Bolt** (tooltip changed)
  - Classic: Your Shadow Bolt critical strikes increase Shadow damage dealt to the target by 4% until 4 non-periodic damage sources are applied. Effect lasts a maximum of 12 sec.
  - Forever: Your Shadow Bolt critical strikes increase Shadow damage taken by the target from your attacks by 4% for 12 sec.
- **Bane** (tooltip changed, was Destruction row 2, col 2)
  - Classic: Reduces the casting time of your Shadow Bolt and Immolate spells by 0 sec and your Soul Fire spell by 0 sec.
  - Forever: Reduces the casting time of your Shadow Bolt, Immolate, and Incinerate spells by 0.1 sec and your Soul Fire spell by 0.4 sec.
- **Cataclysm** (max rank 5 → 3, tooltip changed, was Destruction row 1, col 3)
  - Classic: Reduces the Mana cost of your Destruction spells by 1%.
  - Forever: Reduces the Mana cost of your Destruction spells by 3%.
- **Aftermath** (tooltip changed)
  - Classic: Gives your Destruction spells a 2% chance to daze the target for 5 sec.
  - Forever: Increases the initial damage of your Immolate spell by 10% and your Conflagrate spell has a 20% chance to Daze the target, reducing the target's movement speed by 50% for 5 sec.
- **Ruin** (max rank 1 → 5, tooltip changed, was Destruction row 5, col 3)
  - Classic: Increases the critical strike damage bonus of your Destruction spells by 100%.
  - Forever: Increases the critical strike damage bonus of your Destruction spells by 20%.
- **Shadowburn** (tooltip changed, was Destruction row 3, col 4, tooltip changed in build 1.60.1.70753 (ranks 1))
  - Classic: Instantly blasts the target for 99 Shadow damage. If the target dies within 5 sec of Shadowburn, and yields experience or honor, the caster gains a Soul Shard.
  - Forever: Instantly blasts the target for 65 to 73 Shadow damage. If a non-trivial target dies within 8 sec of being hit with Shadowburn, the caster gains a Soul Shard.
- **Intensity** (max rank 2 → 3, tooltip changed, tooltip changed in build 1.60.1.70753 (ranks 1, 2, 3))
  - Classic: Gives you a 35% chance to resist interruption caused by damage while channeling the Rain of Fire, Hellfire or Soul Fire spell.
  - Forever: Gives your Destruction spells a 23% chance to not lose casting time when you take damage.
- **Conflagrate** (tooltip changed, was Destruction row 7, col 2, tooltip changed in build 1.60.1.70753 (ranks 1))
  - Classic: Ignites a target that is already afflicted by Immolate, dealing 306 Fire damage and consuming the Immolate spell.
  - Forever: Ignites a target that is already afflicted by your Immolate spell, dealing 88 to 110 Fire damage and consuming your Immolate effect.
- **Pyroclasm** (tooltip changed)
  - Classic: Gives your Rain of Fire, Hellfire, and Soul Fire spells a 13% chance to stun the target for 3 sec.
  - Forever: Gives your Soul Fire spell a 13% chance to Stun the target for 3 sec, and your Rain of Fire and Hellfire spells a 13% chance over their duration to Stun targets they damage for 3 sec.

---

*Generated from `_reference/data/forever-talents/warlock.json` by `_reference/data/render_trees.py`. Do not hand-edit; regenerate after refreshing the data.*
