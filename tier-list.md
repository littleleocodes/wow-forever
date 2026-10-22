# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off. The community's combat simulator (ElliotWood/Forever, commit 09e7398) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Hunter: Beast-Survival](hunter/raid/beast-survival.md) | 16/11/24 | 1017 | best |
| **S** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 1007 | 1.0% |
| **A** | [Paladin: Retribution](paladin/raid/retribution.md) | 10/8/33 | 979 | 3.7% |
| **A** | [Warrior: Arms](warrior/raid/arms.md) | 37/14/0 | 964 | 5.2% |
| **B** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 5/41/5 | 893 | 12.2% |
| **B** | [Warrior: Fury](warrior/raid/fury.md) | 20/31/0 | 881 | 13.4% |
| **B** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 27/21/3 | 852 | 16.2% |
| **B** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 847 | 16.7% |
| **B** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 822 | 19.2% |
| **C** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 17/32/0 | 754 | 25.9% |
| **C** | [Warlock: Affliction](warlock/raid/affliction.md) | 28/0/21 | 752 | 26.0% |
| **C** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 19/11/20 | 723 | 28.9% |
| **C** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 15/26/8 | 713 | 29.9% |
| **C** | [Warlock: Destruction](warlock/raid/destruction.md) | 10/11/30 | 705 | 30.7% |
| **C** | [Priest: Shadow](priest/raid/shadow.md) | 18/0/30 | 699 | 31.3% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 16/33/2 | 695 | 31.6% |
| **C** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/33/9 | 694 | 31.7% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 35/9/5 | 689 | 32.2% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 28/0/23 | 687 | 32.4% |
| **C** | [Mage: Fire](mage/raid/fire.md) | 12/32/5 | 685 | 32.7% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 680 | 33.1% |
| **C** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 675 | 33.6% |
| **C** | [Rogue: Assassination](rogue/raid/assassination.md) | 30/19/2 | 672 | 33.9% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 21/28/2 | 669 | 34.2% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 20/0/31 | 640 | 37.1% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 31/17/3 | 597 | 41.3% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/5/13 | 586 | 42.4% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 28/22/0 | 515 | 49.3% |

## Healing

Healing capacity in this project's healer lab: how much of the lab's standard raid damage the healer keeps one group (a tank and four raid members) alive through for five minutes, in 90% of the runs. Healers are in no community simulator; the lab is a model of stated assumptions (`_reference/data/heallab/tables.py`), the same group, damage and fight for every class. Real raids spread damage differently and value utility (dispels, buffs, battle resurrection) the lab does not count.

| Tier | Spec | Build | Capacity | Behind the best |
|---|---|---|---|---|
| **S** | [Shaman: Restoration](shaman/raid/restoration.md) | 0/10/41 | 0.69 | best |
| **S** | [Priest: Holy](priest/raid/holy.md) | 22/29/0 | 0.69 | 0.5% |
| **A** | [Druid: Restoration](druid/raid/restoration.md) | 11/5/35 | 0.65 | 6.1% |
| **A** | [Priest: Discipline](priest/raid/discipline.md) | 30/21/0 | 0.63 | 9.5% |
| **B** | [Paladin: Holy](paladin/raid/holy.md) | 33/12/6 | 0.59 | 14.9% |

## Tanking

Not tiered: each tank's tank value is measured against its own class's hand-made build, and each tank plays in its own gear set, so the numbers do not compare across classes. Threat and damage taken per second below are in a full raid against a raid boss (the community simulator, with this project's patches: Bear Form's threat is our +50% patch).

| Spec | Build | Threat per second | Damage taken per second | Tank value (own class's hand draft = 1.00) |
|---|---|---|---|---|
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 7/35/9 | 1221 | 636 | 1.00 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/33/18 | 503 | 516 | 1.05 |
| [Warrior: Protection](warrior/raid/protection.md) | 17/3/31 | 700 | 672 | 1.01 |

## Race

The tiers above run with racials off. With them on, the race matters by this much in a full raid (the community simulator's Forever racials, the spec's simulator entry with its best build, two seeds; [every race and setting](_reference/race-sweep.md)). Weapon racials count only with the weapon type of the spec's gear set.

| Spec | Best race | Worst race behind it |
|---|---|---|
| [Hunter: Beast-Survival](hunter/raid/beast-survival.md) | Skyborne (Windshaper) | 5.4% (Dwarf) |
| [Hunter: Survival](hunter/raid/survival.md) | Skyborne (Windshaper) | 5.4% (Dwarf) |
| [Paladin: Retribution](paladin/raid/retribution.md) | Human | 1.9% (Dwarf) |
| [Warrior: Arms](warrior/raid/arms.md) | Skyborne (Windshaper) | 5.0% (Gnome) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | Skyborne (Windshaper) | 5.9% (Tauren) |
| [Warrior: Fury](warrior/raid/fury.md) | Skyborne (Windshaper) | 5.1% (Dwarf) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | Skyborne (Windshaper) | 4.6% (Tauren) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | Skyborne (Windshaper) | 4.6% (Tauren) |
| [Warlock: Demonology](warlock/raid/demonology.md) | Human | 1.7% (Troll) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | Skyborne (Windshaper) | 5.3% (Tauren) |
| [Warlock: Affliction](warlock/raid/affliction.md) | Human | 1.7% (Troll) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | Human | 2.0% (Troll) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | Skyborne (Windshaper) | 5.3% (Tauren) |
| [Warlock: Destruction](warlock/raid/destruction.md) | Human | 2.0% (Troll) |
| [Priest: Shadow](priest/raid/shadow.md) | Undead | 1.1% (Human) |
| [Rogue: Combat](rogue/raid/combat.md) | Skyborne (Windshaper) | 5.5% (Dwarf) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | Skyborne (Windshaper) | 4.4% (Night Elf) |
| [Mage: Arcane](mage/raid/arcane.md) | Skyborne (High Order) | 5.0% (Troll) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | Skyborne (High Order) | 5.2% (Troll) |
| [Mage: Fire](mage/raid/fire.md) | Skyborne (High Order) | 4.1% (Troll) |
| [Mage: Frost](mage/raid/frost.md) | Skyborne (High Order) | 5.2% (Troll) |
| [Mage: Frostfire](mage/raid/frostfire.md) | Skyborne (High Order) | 5.2% (Troll) |
| [Rogue: Assassination](rogue/raid/assassination.md) | Skyborne (Windshaper) | 5.4% (Dwarf) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | Skyborne (Windshaper) | 5.4% (Dwarf) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | Skyborne (Windshaper) | 5.3% (Dwarf) |
| [Priest: Smite](priest/raid/smite.md) | Undead | 1.5% (Human) |
| [Druid: Balance](druid/raid/balance.md) | Skyborne (Windshaper) | 4.6% (Night Elf) |
| [Shaman: Elemental](shaman/raid/elemental.md) | Skyborne (Windshaper) | 5.7% (Dwarf) |

## Trinkets

The trinket pair in each spec's own gear sets (damage specs and tanks: raced in the community simulator; healers: by the healer lab's stat weights). Each opens its Wowhead page.

| Spec | Pre-BiS | Phase 1 BiS |
|---|---|---|
| [Druid: Balance](druid/raid/balance.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) (tank) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) |
| [Druid: Restoration](druid/raid/restoration.md) | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18470), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18470), [Serenity Field](https://www.wowhead.com/forever/item=272439) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) |
| [Hunter: Beast-Survival](hunter/raid/beast-survival.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) |
| [Hunter: Survival](hunter/raid/survival.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Mage: Arcane](mage/raid/arcane.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Mage: Fire](mage/raid/fire.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Mage: Frost](mage/raid/frost.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Mage: Frostfire](mage/raid/frostfire.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Eye of the Beast](https://www.wowhead.com/forever/item=13968), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Paladin: Holy](paladin/raid/holy.md) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Serenity Field](https://www.wowhead.com/forever/item=272439) |
| [Paladin: Protection](paladin/raid/protection.md) (tank) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Arena Grand Master](https://www.wowhead.com/forever/item=19024), [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) |
| [Paladin: Retribution](paladin/raid/retribution.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Priest: Discipline](priest/raid/discipline.md) | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469) |
| [Priest: Holy](priest/raid/holy.md) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Smite](priest/raid/smite.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Priest: Shadow](priest/raid/shadow.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Rogue: Assassination](rogue/raid/assassination.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) |
| [Rogue: Combat](rogue/raid/combat.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) |
| [Shaman: Elemental](shaman/raid/elemental.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Shaman: Restoration](shaman/raid/restoration.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| [Warlock: Affliction](warlock/raid/affliction.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Warlock: Demonology](warlock/raid/demonology.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Warlock: Destruction](warlock/raid/destruction.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18467) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) |
| [Warrior: Arms](warrior/raid/arms.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| [Warrior: Fury](warrior/raid/fury.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Warrior: Protection](warrior/raid/protection.md) (tank) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Demon's Blood](https://www.wowhead.com/forever/item=10779), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |

---
*Generated by `_reference/data/render_tier_list.py` on 2026-10-22 from the pages' own picks and numbers (client build 1.60.1.70425). Simulations, not in-game measurements. Do not hand-edit.*

