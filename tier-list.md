# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off for hunter, mage, priest, rogue, shaman, warlock, warrior; on for druid, paladin. The community's combat simulator (the ElliotWood/Forever fork (deleted 2026-10-18) at b7083fa (client 1.60.1.70425, its spell data of 14-15 Oct) and 2ce8265 (client 1.60.1.70291); the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Warrior: Arms](warrior/raid/arms.md) | 37/14/0 | 964 | best |
| **S** | [Paladin: Retribution](paladin/raid/retribution.md) | 10/8/33 | 952 | 1.3% |
| **A** | [Warrior: Fury](warrior/raid/fury.md) | 20/31/0 | 881 | 8.6% |
| **B** | [Mage: Fire](mage/raid/fire.md) | 17/31/3 | 850 | 11.8% |
| **B** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 835 | 13.3% |
| **B** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 822 | 14.7% |
| **B** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 802 | 16.8% |
| **B** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 7/39/5 | 781 | 18.9% |
| **C** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 768 | 20.3% |
| **C** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/33/9 | 766 | 20.5% |
| **C** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 19/32/0 | 754 | 21.8% |
| **C** | [Warlock: Affliction](warlock/raid/affliction.md) | 30/0/21 | 752 | 22.0% |
| **C** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 20/11/20 | 723 | 25.0% |
| **C** | [Warlock: Destruction](warlock/raid/destruction.md) | 10/11/30 | 718 | 25.5% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 35/13/3 | 717 | 25.6% |
| **C** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 22/29/0 | 715 | 25.8% |
| **C** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 15/24/12 | 713 | 26.0% |
| **C** | [Priest: Shadow](priest/raid/shadow.md) | 17/0/34 | 699 | 27.5% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 29/0/22 | 693 | 28.2% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 16/33/2 | 683 | 29.1% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 21/28/2 | 657 | 31.9% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 20/0/31 | 609 | 36.8% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 31/17/3 | 597 | 38.1% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/5/13 | 594 | 38.4% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 544 | 43.5% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 29/22/0 | 515 | 46.6% |

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
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 7/35/9 | 1224 | 636 | 1.00 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/35/16 | 490 | 518 | 1.07 |
| [Warrior: Protection](warrior/raid/protection.md) | 17/3/31 | 700 | 672 | 1.01 |

## Race

The tiers above run with racials off for hunter, mage, priest, rogue, shaman, warlock, warrior; on for druid, paladin. With them on, the race matters by this much in a full raid (the community simulator's Forever racials, the spec's simulator entry with its best build, two seeds; [every race and setting](_reference/race-sweep.md)). Weapon racials count only with the weapon type of the spec's gear set.

| Spec | Best race | Worst race behind it |
|---|---|---|
| [Warrior: Arms](warrior/raid/arms.md) | Skyborne (Windshaper) | 5.0% (Gnome) |
| [Paladin: Retribution](paladin/raid/retribution.md) | Human | 1.9% (Dwarf) |
| [Warrior: Fury](warrior/raid/fury.md) | Skyborne (Windshaper) | 5.1% (Dwarf) |
| [Mage: Fire](mage/raid/fire.md) | Skyborne (High Order) | 4.1% (Troll) |
| [Hunter: Survival](hunter/raid/survival.md) | Skyborne (Windshaper) | 5.4% (Dwarf) |
| [Warlock: Demonology](warlock/raid/demonology.md) | Human | 1.7% (Troll) |
| [Mage: Frostfire](mage/raid/frostfire.md) | Skyborne (High Order) | 5.2% (Troll) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | Skyborne (Windshaper) | 4.9% (Tauren) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | Skyborne (Windshaper) | 4.6% (Tauren) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | Skyborne (Windshaper) | 4.4% (Night Elf) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | Skyborne (Windshaper) | 5.3% (Tauren) |
| [Warlock: Affliction](warlock/raid/affliction.md) | Human | 1.7% (Troll) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | Human | 2.0% (Troll) |
| [Warlock: Destruction](warlock/raid/destruction.md) | Human | 2.0% (Troll) |
| [Mage: Arcane](mage/raid/arcane.md) | Skyborne (High Order) | 5.0% (Troll) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | Skyborne (Windshaper) | 4.6% (Tauren) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | Skyborne (Windshaper) | 5.3% (Tauren) |
| [Priest: Shadow](priest/raid/shadow.md) | Undead | 1.1% (Human) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | Skyborne (High Order) | 5.2% (Troll) |
| [Rogue: Combat](rogue/raid/combat.md) | Skyborne (Windshaper) | 5.5% (Dwarf) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | Skyborne (Windshaper) | 5.4% (Dwarf) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | Skyborne (Windshaper) | 5.3% (Dwarf) |
| [Priest: Smite](priest/raid/smite.md) | Undead | 1.5% (Human) |
| [Druid: Balance](druid/raid/balance.md) | Skyborne (Windshaper) | 4.6% (Night Elf) |
| [Mage: Frost](mage/raid/frost.md) | Skyborne (High Order) | 5.2% (Troll) |
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
*Generated by `_reference/data/render_tier_list.py` on 2026-10-25 from the pages' own picks and numbers (talent and spell data: client build 1.60.1.70425; raid numbers: ElliotWood/Forever fork at b7083fa (client 70425) and 2ce8265 (client 70291); wowsims/forever at 30f67f5 (client 70450)). Simulations, not in-game measurements. Do not hand-edit.*

