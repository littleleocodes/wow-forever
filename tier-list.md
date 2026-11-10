# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off. The community's combat simulator (the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 17/31/3 | 998 | best |
| **A** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 966 | 3.2% |
| **A** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 5/41/5 | 966 | 3.2% |
| **A** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 28/21/2 | 957 | 4.1% |
| **A** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 17/29/5 | 928 | 7.0% |
| **A** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/32/10 | 927 | 7.1% |
| **A** | [Warrior: Fury](warrior/raid/fury.md) | 20/31/0 | 909 | 8.9% |
| **B** | [Paladin: Retribution](paladin/raid/retribution.md) | 16/4/31 | 878 | 12.0% |
| **B** | [Mage: Fire](mage/raid/fire.md) | 17/31/3 | 869 | 12.9% |
| **B** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 857 | 14.1% |
| **B** | [Warrior: Arms](warrior/raid/arms.md) | 34/17/0 | 845 | 15.3% |
| **B** | [Paladin: Shockadin](paladin/raid/shockadin.md) | 23/0/28 | 834 | 16.4% |
| **B** | [Warlock: Affliction](warlock/raid/affliction.md) | 30/0/21 | 828 | 17.0% |
| **B** | [Rogue: Assassination](rogue/raid/assassination.md) | 31/19/1 | 813 | 18.6% |
| **B** | [Warlock: Destruction](warlock/raid/destruction.md) | 9/11/31 | 811 | 18.7% |
| **C** | [Rogue: Assassination/Subtlety hybrid](rogue/raid/hybrid-assassination-subtlety.md) | 27/2/22 | 796 | 20.2% |
| **C** | [Priest: Shadow](priest/raid/shadow.md) | 16/0/35 | 796 | 20.2% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 31/17/3 | 790 | 20.8% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 12/8/31 | 789 | 20.9% |
| **C** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 9/11/31 | 789 | 21.0% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 29/22/0 | 788 | 21.0% |
| **C** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 785 | 21.3% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 13/33/5 | 764 | 23.4% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 31/11/9 | 757 | 24.2% |
| **C** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 753 | 24.6% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/0/18 | 722 | 27.6% |
| **C** | [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | 8/15/28 | 699 | 29.9% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 28/10/13 | 693 | 30.6% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 17/17/17 | 616 | 38.3% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 526 | 47.3% |

## Healing

Healing capacity in this project's healer lab: how much of the lab's standard raid damage the healer keeps one group (a tank and four raid members) alive through for five minutes, in 90% of the runs. Healers are in no community simulator; the lab is a model of stated assumptions (`_reference/data/heallab/tables.py`), the same group, damage and fight for every class. Real raids spread damage differently and value utility (dispels, buffs, battle resurrection) the lab does not count.

| Tier | Spec | Build | Capacity | Behind the best |
|---|---|---|---|---|
| **S** | [Druid: Restoration](druid/raid/restoration.md) | 11/0/40 | 0.70 | best |
| **S** | [Priest: Holy](priest/raid/holy.md) | 22/29/0 | 0.69 | 0.8% |
| **S** | [Shaman: Restoration](shaman/raid/restoration.md) | 0/10/41 | 0.69 | 1.3% |
| **A** | [Priest: Discipline](priest/raid/discipline.md) | 29/22/0 | 0.65 | 7.2% |
| **A** | [Paladin: Holy](paladin/raid/holy.md) | 32/5/14 | 0.64 | 8.7% |

## Tanking

Not tiered: each tank's tank value is measured against its own class's hand-made build, and each tank plays in its own gear set, so the numbers do not compare across classes. Threat and damage taken per second below are in a full raid against a raid boss (the community simulator, with this project's patches: Bear Form's threat is our +50% patch).

| Spec | Build | Threat per second | Damage taken per second | Tank value (own class's hand draft = 1.00) |
|---|---|---|---|---|
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/37/5 | 8525 | 376 | 1.16 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/35/16 | 1241 | 292 | 1.02 |
| [Warrior: Protection](warrior/raid/protection.md) | 17/3/31 | 1604 | 277 | 1.01 |

## Race

The tiers above run with racials off. With them on, the race matters by this much in a full raid (the community simulator's Forever racials, the spec's simulator entry with its best build, two seeds; [every race and setting](_reference/race-sweep.md)). Weapon racials count only with the weapon type of the spec's gear set.

| Spec | Best race | Worst race behind it |
|---|---|---|
| [Shaman: Enhancement](shaman/raid/enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | Skyborne (Windshaper) | 7.1% (Dwarf) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | Skyborne (Windshaper) | 5.0% (Night Elf) |
| [Warrior: Fury](warrior/raid/fury.md) | Skyborne (Windshaper) | 6.3% (Night Elf) |
| [Paladin: Retribution](paladin/raid/retribution.md) | Human | 0.7% (Undead) |
| [Mage: Fire](mage/raid/fire.md) | Skyborne (High Order) | 6.8% (Troll) |
| [Warlock: Demonology](warlock/raid/demonology.md) | Human | 1.8% (Troll) |
| [Warrior: Arms](warrior/raid/arms.md) | Skyborne (Windshaper) | 6.1% (Gnome) |
| [Paladin: Shockadin](paladin/raid/shockadin.md) | Human | 0.6% (Dwarf) |
| [Warlock: Affliction](warlock/raid/affliction.md) | Human | 2.0% (Troll) |
| [Rogue: Assassination](rogue/raid/assassination.md) | Skyborne (Windshaper) | 6.3% (Dwarf) |
| [Warlock: Destruction](warlock/raid/destruction.md) | Human | 2.0% (Troll) |
| [Rogue: Assassination/Subtlety hybrid](rogue/raid/hybrid-assassination-subtlety.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Priest: Shadow](priest/raid/shadow.md) | Human | 1.7% (Dwarf) |
| [Mage: Arcane](mage/raid/arcane.md) | Skyborne (High Order) | 5.6% (Troll) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | Human | 1.8% (Troll) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Mage: Frostfire](mage/raid/frostfire.md) | Skyborne (High Order) | 4.8% (Troll) |
| [Rogue: Combat](rogue/raid/combat.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Shaman: Elemental](shaman/raid/elemental.md) | Skyborne (Windshaper) | 6.8% (Dwarf) |
| [Hunter: Survival](hunter/raid/survival.md) | Skyborne (Windshaper) | 6.6% (Dwarf) |
| [Druid: Balance](druid/raid/balance.md) | Skyborne (Windshaper) | 6.2% (Night Elf) |
| [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | Human | 0.7% (Undead) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | Skyborne (High Order) | 7.1% (Troll) |
| [Priest: Smite](priest/raid/smite.md) | Undead | 1.1% (Dwarf) |
| [Mage: Frost](mage/raid/frost.md) | Skyborne (High Order) | 7.1% (Troll) |

## Trinkets

The trinket pair in each spec's own gear sets (damage specs and tanks: raced in the community simulator; healers: by the healer lab's stat weights). Each opens its Wowhead page.

| Spec | Pre-BiS | Phase 1 BiS |
|---|---|---|
| [Druid: Balance](druid/raid/balance.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) (tank) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |
| [Druid: Restoration](druid/raid/restoration.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Hunter: Survival](hunter/raid/survival.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Mage: Arcane](mage/raid/arcane.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Fire](mage/raid/fire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Frost](mage/raid/frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Frostfire](mage/raid/frostfire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Paladin: Holy](paladin/raid/holy.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Paladin: Protection](paladin/raid/protection.md) (tank) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Paladin: Retribution](paladin/raid/retribution.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Priest: Discipline](priest/raid/discipline.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Holy](priest/raid/holy.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Priest: Smite](priest/raid/smite.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Priest: Shadow](priest/raid/shadow.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Rogue: Assassination](rogue/raid/assassination.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Combat](rogue/raid/combat.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Shaman: Elemental](shaman/raid/elemental.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Shaman: Restoration](shaman/raid/restoration.md) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Serenity Field](https://www.wowhead.com/forever/item=272439), [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) |
| [Warlock: Affliction](warlock/raid/affliction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Demonology](warlock/raid/demonology.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Destruction](warlock/raid/destruction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warrior: Arms](warrior/raid/arms.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| [Warrior: Fury](warrior/raid/fury.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Warrior: Protection](warrior/raid/protection.md) (tank) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Talisman of Arathor](https://www.wowhead.com/forever/item=20071) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Arena Grand Master](https://www.wowhead.com/forever/item=19024) |

---
*Generated by `_reference/data/render_tier_list.py` on 2026-11-10 from the pages' own picks and numbers (talent and spell data: client build 1.60.1.70753; raid numbers: wowsims/forever at 16e8542 (client 70790)). Simulations, not in-game measurements. Do not hand-edit.*

