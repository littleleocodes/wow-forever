# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off. The community's combat simulator (the official wowsims/forever simulator at bac92db (client 1.60.1.70707), 7c3453f (client 1.60.1.70755), 5ad0894 (client 1.60.1.70707), d97252f (client 1.60.1.70707), 92c4c35 (client 1.60.1.70755) and 02bd77c (client 1.60.1.70707)) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 7/39/5 | 1004 | best |
| **S** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 995 | 0.9% |
| **S** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 28/21/2 | 986 | 1.8% |
| **A** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 17/31/3 | 969 | 3.5% |
| **B** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 17/29/5 | 893 | 11.1% |
| **B** | [Warrior: Fury](warrior/raid/fury.md) | 18/33/0 | 887 | 11.6% |
| **B** | [Paladin: Retribution](paladin/raid/retribution.md) | 16/4/31 | 876 | 12.7% |
| **B** | [Paladin: Shockadin](paladin/raid/shockadin.md) | 23/0/28 | 839 | 16.4% |
| **B** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 838 | 16.5% |
| **B** | [Mage: Fire](mage/raid/fire.md) | 17/31/3 | 828 | 17.5% |
| **B** | [Warrior: Arms](warrior/raid/arms.md) | 34/17/0 | 813 | 19.0% |
| **B** | [Warlock: Affliction](warlock/raid/affliction.md) | 30/0/21 | 812 | 19.1% |
| **C** | [Warlock: Destruction](warlock/raid/destruction.md) | 9/11/31 | 795 | 20.8% |
| **C** | [Priest: Shadow](priest/raid/shadow.md) | 16/0/35 | 788 | 21.5% |
| **C** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 21/11/19 | 770 | 23.3% |
| **C** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 759 | 24.4% |
| **C** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/32/10 | 758 | 24.5% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 31/17/3 | 756 | 24.7% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 31/11/9 | 746 | 25.7% |
| **C** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 734 | 26.9% |
| **C** | [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | 8/15/28 | 697 | 30.5% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 28/10/13 | 671 | 33.2% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 21/30/0 | 666 | 33.6% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/0/18 | 647 | 35.6% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 21/0/30 | 607 | 39.5% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 29/22/0 | 603 | 40.0% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 17/17/17 | 602 | 40.1% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 520 | 48.2% |

## Healing

Healing capacity in this project's healer lab: how much of the lab's standard raid damage the healer keeps one group (a tank and four raid members) alive through for five minutes, in 90% of the runs. Healers are in no community simulator; the lab is a model of stated assumptions (`_reference/data/heallab/tables.py`), the same group, damage and fight for every class. Real raids spread damage differently and value utility (dispels, buffs, battle resurrection) the lab does not count.

| Tier | Spec | Build | Capacity | Behind the best |
|---|---|---|---|---|
| **S** | [Shaman: Restoration](shaman/raid/restoration.md) | 0/10/41 | 0.69 | best |
| **S** | [Priest: Holy](priest/raid/holy.md) | 22/29/0 | 0.69 | 0.5% |
| **A** | [Druid: Restoration](druid/raid/restoration.md) | 12/1/38 | 0.66 | 4.7% |
| **A** | [Paladin: Holy](paladin/raid/holy.md) | 32/5/14 | 0.63 | 9.3% |
| **A** | [Priest: Discipline](priest/raid/discipline.md) | 30/21/0 | 0.63 | 9.5% |

## Tanking

Not tiered: each tank's tank value is measured against its own class's hand-made build, and each tank plays in its own gear set, so the numbers do not compare across classes. Threat and damage taken per second below are in a full raid against a raid boss (the community simulator, with this project's patches: Bear Form's threat is our +50% patch).

| Spec | Build | Threat per second | Damage taken per second | Tank value (own class's hand draft = 1.00) |
|---|---|---|---|---|
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/37/5 | 3705 | 376 | 1.16 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/35/16 | 1241 | 292 | 1.02 |
| [Warrior: Protection](warrior/raid/protection.md) | 17/3/31 | 1115 | 277 | 1.01 |

## Race

The tiers above run with racials off. With them on, the race matters by this much in a full raid (the community simulator's Forever racials, the spec's simulator entry with its best build, two seeds; [every race and setting](_reference/race-sweep.md)). Weapon racials count only with the weapon type of the spec's gear set.

| Spec | Best race | Worst race behind it |
|---|---|---|
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | Skyborne (Windshaper) | 4.5% (Dwarf) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Warrior: Fury](warrior/raid/fury.md) | Skyborne (Windshaper) | 6.7% (Dwarf) |
| [Paladin: Retribution](paladin/raid/retribution.md) | Human | 0.7% (Undead) |
| [Paladin: Shockadin](paladin/raid/shockadin.md) | Human | 0.6% (Dwarf) |
| [Warlock: Demonology](warlock/raid/demonology.md) | Human | 1.8% (Troll) |
| [Mage: Fire](mage/raid/fire.md) | Skyborne (High Order) | 6.8% (Troll) |
| [Warrior: Arms](warrior/raid/arms.md) | Skyborne (Windshaper) | 6.1% (Gnome) |
| [Warlock: Affliction](warlock/raid/affliction.md) | Human | 2.0% (Troll) |
| [Warlock: Destruction](warlock/raid/destruction.md) | Human | 2.0% (Troll) |
| [Priest: Shadow](priest/raid/shadow.md) | Human | 1.7% (Dwarf) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | Human | 2.0% (Troll) |
| [Mage: Frostfire](mage/raid/frostfire.md) | Skyborne (High Order) | 4.8% (Troll) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | Skyborne (Windshaper) | 5.0% (Night Elf) |
| [Mage: Arcane](mage/raid/arcane.md) | Skyborne (High Order) | 5.6% (Troll) |
| [Shaman: Elemental](shaman/raid/elemental.md) | Skyborne (Windshaper) | 6.8% (Dwarf) |
| [Hunter: Survival](hunter/raid/survival.md) | Skyborne (Windshaper) | 6.6% (Dwarf) |
| [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | Human | 0.7% (Undead) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | Skyborne (High Order) | 7.1% (Troll) |
| [Rogue: Combat](rogue/raid/combat.md) | Skyborne (Windshaper) | 6.7% (Dwarf) |
| [Druid: Balance](druid/raid/balance.md) | Skyborne (Windshaper) | 6.2% (Night Elf) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | Skyborne (Windshaper) | 6.3% (Dwarf) |
| [Priest: Smite](priest/raid/smite.md) | Undead | 1.1% (Dwarf) |
| [Mage: Frost](mage/raid/frost.md) | Skyborne (High Order) | 7.1% (Troll) |

## Trinkets

The trinket pair in each spec's own gear sets (damage specs and tanks: raced in the community simulator; healers: by the healer lab's stat weights). Each opens its Wowhead page.

| Spec | Pre-BiS | Phase 1 BiS |
|---|---|---|
| [Druid: Balance](druid/raid/balance.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) (tank) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |
| [Druid: Restoration](druid/raid/restoration.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [item 1713](https://www.wowhead.com/forever/item=1713) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120), [Cleansed Vilebranch Medallion](https://www.wowhead.com/forever/item=270275) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Enriched Seal](https://www.wowhead.com/forever/item=271903) |
| [Hunter: Survival](hunter/raid/survival.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Mage: Arcane](mage/raid/arcane.md) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Mage: Fire](mage/raid/fire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Frost](mage/raid/frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Mage: Frostfire](mage/raid/frostfire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Paladin: Holy](paladin/raid/holy.md) | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659), [Serenity Field](https://www.wowhead.com/forever/item=272439) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Paladin: Protection](paladin/raid/protection.md) (tank) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904) |
| [Paladin: Retribution](paladin/raid/retribution.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678) |
| [Priest: Discipline](priest/raid/discipline.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Holy](priest/raid/holy.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Smite](priest/raid/smite.md) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Zandalarian Hero Charm](https://www.wowhead.com/forever/item=19950) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Priest: Shadow](priest/raid/shadow.md) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ascendance](https://www.wowhead.com/forever/item=22678), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Rogue: Combat](rogue/raid/combat.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Shaman: Elemental](shaman/raid/elemental.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Shaman: Restoration](shaman/raid/restoration.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Warlock: Affliction](warlock/raid/affliction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warlock: Demonology](warlock/raid/demonology.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warlock: Destruction](warlock/raid/destruction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Warrior: Arms](warrior/raid/arms.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| [Warrior: Fury](warrior/raid/fury.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Warrior: Protection](warrior/raid/protection.md) (tank) | [Stormpike Insignia Rank 6](https://www.wowhead.com/forever/item=17904), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |

---
*Generated by `_reference/data/render_tier_list.py` on 2026-11-04 from the pages' own picks and numbers (talent and spell data: client build 1.60.1.70753; raid numbers: wowsims/forever at bac92db (client 70707), 7c3453f (client 70755), 5ad0894 (client 70707), d97252f (client 70707), 92c4c35 (client 70755) and 02bd77c (client 70707)). Simulations, not in-game measurements. Do not hand-edit.*

