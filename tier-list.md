# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off. The community's combat simulator (the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Warrior: Fury](warrior/raid/fury.md) | 18/31/2 | 925 | best |
| **A** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 870 | 5.9% |
| **A** | [Mage: Fire](mage/raid/fire.md) | 17/31/3 | 850 | 8.1% |
| **A** | [Warlock: Affliction](warlock/raid/affliction.md) | 30/0/21 | 836 | 9.5% |
| **A** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 835 | 9.7% |
| **B** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 799 | 13.6% |
| **B** | [Warrior: Arms](warrior/raid/arms.md) | 34/17/0 | 799 | 13.6% |
| **B** | [Priest: Shadow](priest/raid/shadow.md) | 20/0/31 | 796 | 13.9% |
| **B** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 21/11/19 | 795 | 14.1% |
| **B** | [Paladin: Retribution](paladin/raid/retribution.md) | 17/0/34 | 785 | 15.2% |
| **B** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 7/39/5 | 781 | 15.5% |
| **B** | [Warlock: Destruction](warlock/raid/destruction.md) | 9/11/31 | 770 | 16.7% |
| **B** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 768 | 17.0% |
| **B** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 28/20/3 | 759 | 17.9% |
| **B** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/33/9 | 754 | 18.4% |
| **C** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 17/31/3 | 734 | 20.6% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 35/13/3 | 717 | 22.5% |
| **C** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 17/29/5 | 695 | 24.8% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 29/0/22 | 693 | 25.1% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 16/33/2 | 683 | 26.1% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 28/21/2 | 664 | 28.2% |
| **C** | [Rogue: Assassination](rogue/raid/assassination.md) | 30/21/0 | 662 | 28.4% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/5/13 | 624 | 32.5% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 29/22/0 | 619 | 33.0% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 17/17/17 | 611 | 33.9% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 20/0/31 | 609 | 34.1% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 588 | 36.4% |

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
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/35/7 | 4045 | 364 | 1.06 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/35/16 | 826 | 321 | 1.07 |
| [Warrior: Protection](warrior/raid/protection.md) | 17/3/31 | 1261 | 277 | 1.02 |

## Race

The tiers above run with racials off. With them on, the race matters by this much in a full raid (the community simulator's Forever racials, the spec's simulator entry with its best build, two seeds; [every race and setting](_reference/race-sweep.md)). Weapon racials count only with the weapon type of the spec's gear set.

| Spec | Best race | Worst race behind it |
|---|---|---|
| [Warrior: Fury](warrior/raid/fury.md) | Skyborne (Windshaper) | 6.7% (Dwarf) |
| [Warlock: Demonology](warlock/raid/demonology.md) | Human | 1.8% (Troll) |
| [Mage: Fire](mage/raid/fire.md) | Skyborne (High Order) | 6.8% (Troll) |
| [Warlock: Affliction](warlock/raid/affliction.md) | Human | 2.0% (Troll) |
| [Hunter: Survival](hunter/raid/survival.md) | Skyborne (Windshaper) | 6.6% (Dwarf) |
| [Mage: Frostfire](mage/raid/frostfire.md) | Skyborne (High Order) | 4.8% (Troll) |
| [Warrior: Arms](warrior/raid/arms.md) | Skyborne (Windshaper) | 6.1% (Gnome) |
| [Priest: Shadow](priest/raid/shadow.md) | Human | 1.7% (Dwarf) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | Human | 2.0% (Troll) |
| [Paladin: Retribution](paladin/raid/retribution.md) | Human | 0.7% (Undead) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | Skyborne (Windshaper) | 4.5% (Dwarf) |
| [Warlock: Destruction](warlock/raid/destruction.md) | Human | 2.0% (Troll) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | Skyborne (Windshaper) | 5.0% (Night Elf) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Mage: Arcane](mage/raid/arcane.md) | Skyborne (High Order) | 5.6% (Troll) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | Skyborne (High Order) | 7.1% (Troll) |
| [Rogue: Combat](rogue/raid/combat.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | Skyborne (Windshaper) | 6.3% (Dwarf) |
| [Rogue: Assassination](rogue/raid/assassination.md) | Skyborne (Windshaper) | 6.3% (Dwarf) |
| [Druid: Balance](druid/raid/balance.md) | Skyborne (Windshaper) | 6.2% (Night Elf) |
| [Shaman: Elemental](shaman/raid/elemental.md) | Skyborne (Windshaper) | 6.8% (Dwarf) |
| [Priest: Smite](priest/raid/smite.md) | Undead | 1.1% (Dwarf) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Mage: Frost](mage/raid/frost.md) | Skyborne (High Order) | 7.1% (Troll) |

## Trinkets

The trinket pair in each spec's own gear sets (damage specs and tanks: raced in the community simulator; healers: by the healer lab's stat weights). Each opens its Wowhead page.

| Spec | Pre-BiS | Phase 1 BiS |
|---|---|---|
| [Druid: Balance](druid/raid/balance.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Molten Heart of the Mountain](https://www.wowhead.com/forever/item=249470) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) (tank) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |
| [Druid: Restoration](druid/raid/restoration.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Ankh of Life](https://www.wowhead.com/forever/item=1713) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | [Everlook Delivery Bot](https://www.wowhead.com/forever/item=274760), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Everlook Delivery Bot](https://www.wowhead.com/forever/item=274760) |
| [Hunter: Survival](hunter/raid/survival.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Mage: Arcane](mage/raid/arcane.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Fire](mage/raid/fire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Frost](mage/raid/frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Frostfire](mage/raid/frostfire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Alchemist's Stone](https://www.wowhead.com/forever/item=13503) | [Alchemist's Stone](https://www.wowhead.com/forever/item=13503), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Paladin: Holy](paladin/raid/holy.md) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Serenity Field](https://www.wowhead.com/forever/item=272439) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Paladin: Protection](paladin/raid/protection.md) (tank) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) |
| [Paladin: Retribution](paladin/raid/retribution.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Priest: Discipline](priest/raid/discipline.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Holy](priest/raid/holy.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Smite](priest/raid/smite.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Priest: Shadow](priest/raid/shadow.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Rogue: Assassination](rogue/raid/assassination.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Combat](rogue/raid/combat.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Shaman: Elemental](shaman/raid/elemental.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Shaman: Restoration](shaman/raid/restoration.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Warlock: Affliction](warlock/raid/affliction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warlock: Demonology](warlock/raid/demonology.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Destruction](warlock/raid/destruction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warrior: Arms](warrior/raid/arms.md) | [Everlook Pathcarver](https://www.wowhead.com/forever/item=274759), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Everlook Delivery Bot](https://www.wowhead.com/forever/item=274760), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| [Warrior: Fury](warrior/raid/fury.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Warrior: Protection](warrior/raid/protection.md) (tank) | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |

---
*Generated by `_reference/data/render_tier_list.py` on 2026-10-30 from the pages' own picks and numbers (talent and spell data: client build 1.60.1.70425; raid numbers: wowsims/forever at 30f67f5 (client 70450)). Simulations, not in-game measurements. Do not hand-edit.*

