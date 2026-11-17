# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off. The community's combat simulator (the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 1028 | best |
| **S** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 28/21/2 | 1017 | 1.1% |
| **S** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 7/39/5 | 1015 | 1.3% |
| **A** | [Warrior: Fury](warrior/raid/fury.md) | 17/32/2 | 937 | 8.8% |
| **A** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/32/10 | 927 | 9.9% |
| **B** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 18/31/2 | 909 | 11.6% |
| **B** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 17/29/5 | 892 | 13.2% |
| **B** | [Mage: Fire](mage/raid/fire.md) | 17/31/3 | 887 | 13.7% |
| **B** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 867 | 15.7% |
| **B** | [Warrior: Arms](warrior/raid/arms.md) | 34/17/0 | 864 | 16.0% |
| **B** | [Rogue: Assassination](rogue/raid/assassination.md) | 31/19/1 | 844 | 17.9% |
| **B** | [Paladin: Retribution](paladin/raid/retribution.md) | 16/4/31 | 843 | 18.0% |
| **B** | [Warlock: Affliction](warlock/raid/affliction.md) | 30/0/21 | 838 | 18.4% |
| **B** | [Warlock: Destruction](warlock/raid/destruction.md) | 9/11/31 | 826 | 19.6% |
| **C** | [Rogue: Assassination/Subtlety hybrid](rogue/raid/hybrid-assassination-subtlety.md) | 27/2/22 | 822 | 20.1% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 12/8/31 | 817 | 20.5% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 29/22/0 | 808 | 21.4% |
| **C** | [Paladin: Shockadin](paladin/raid/shockadin.md) | 23/0/28 | 804 | 21.8% |
| **C** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 9/11/31 | 802 | 21.9% |
| **C** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 798 | 22.4% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 31/17/3 | 797 | 22.4% |
| **C** | [Priest: Shadow](priest/raid/shadow.md) | 20/0/31 | 788 | 23.4% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 13/33/5 | 781 | 24.0% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 31/11/9 | 771 | 25.0% |
| **C** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 738 | 28.2% |
| **C** | [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | 10/12/29 | 727 | 29.3% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/0/18 | 725 | 29.4% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 28/10/13 | 704 | 31.5% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 17/17/17 | 623 | 39.4% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 533 | 48.2% |

## Healing

Healing capacity in this project's healer lab: how much of the lab's standard raid damage the healer keeps one group (a tank and four raid members) alive through for five minutes, in 90% of the runs. Healers are in no community simulator; the lab is a model of stated assumptions (`_reference/data/heallab/tables.py`), the same group, damage and fight for every class. Real raids spread damage differently and value utility (dispels, buffs, battle resurrection) the lab does not count.

| Tier | Spec | Build | Capacity | Behind the best |
|---|---|---|---|---|
| **S** | [Druid: Restoration](druid/raid/restoration.md) | 11/0/40 | 0.70 | best |
| **S** | [Priest: Holy](priest/raid/holy.md) | 22/29/0 | 0.69 | 1.2% |
| **S** | [Shaman: Restoration](shaman/raid/restoration.md) | 0/10/41 | 0.69 | 1.7% |
| **A** | [Priest: Discipline](priest/raid/discipline.md) | 29/22/0 | 0.65 | 7.6% |
| **A** | [Paladin: Holy](paladin/raid/holy.md) | 32/5/14 | 0.64 | 9.1% |

## Tanking

Not tiered: each tank's tank value is measured against its own class's hand-made build, and each tank plays in its own gear set, so the numbers do not compare across classes. Threat and damage taken per second below are in a full raid against a raid boss (the community simulator, with this project's patches: Bear Form's threat is our +50% patch).

| Spec | Build | Threat per second | Damage taken per second | Tank value (own class's hand draft = 1.00) |
|---|---|---|---|---|
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/37/5 | 8055 | 376 | 1.16 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/35/16 | 1210 | 280 | 1.02 |
| [Warrior: Protection](warrior/raid/protection.md) | 17/3/31 | 1990 | 287 | 1.01 |

## Race

The tiers above run with racials off. With them on, the race matters by this much in a full raid (the community simulator's Forever racials, the spec's simulator entry with its best build, two seeds; [every race and setting](_reference/race-sweep.md)). Weapon racials count only with the weapon type of the spec's gear set.

| Spec | Best race | Worst race behind it |
|---|---|---|
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | Skyborne (Windshaper) | 4.9% (Dwarf) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | Skyborne (Windshaper) | 4.5% (Dwarf) |
| [Warrior: Fury](warrior/raid/fury.md) | Skyborne (Windshaper) | 6.7% (Dwarf) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | Skyborne (Windshaper) | 5.0% (Night Elf) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | Skyborne (Windshaper) | 6.2% (Troll) |
| [Mage: Fire](mage/raid/fire.md) | Skyborne (High Order) | 6.8% (Troll) |
| [Warlock: Demonology](warlock/raid/demonology.md) | Human | 1.8% (Troll) |
| [Warrior: Arms](warrior/raid/arms.md) | Skyborne (Windshaper) | 6.1% (Gnome) |
| [Rogue: Assassination](rogue/raid/assassination.md) | Skyborne (Windshaper) | 6.3% (Dwarf) |
| [Paladin: Retribution](paladin/raid/retribution.md) | Human | 0.7% (Undead) |
| [Warlock: Affliction](warlock/raid/affliction.md) | Human | 2.0% (Troll) |
| [Warlock: Destruction](warlock/raid/destruction.md) | Human | 2.0% (Troll) |
| [Rogue: Assassination/Subtlety hybrid](rogue/raid/hybrid-assassination-subtlety.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Paladin: Shockadin](paladin/raid/shockadin.md) | Human | 0.6% (Dwarf) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | Human | 1.8% (Troll) |
| [Mage: Frostfire](mage/raid/frostfire.md) | Skyborne (High Order) | 4.8% (Troll) |
| [Mage: Arcane](mage/raid/arcane.md) | Skyborne (High Order) | 5.6% (Troll) |
| [Priest: Shadow](priest/raid/shadow.md) | Human | 1.7% (Dwarf) |
| [Rogue: Combat](rogue/raid/combat.md) | Skyborne (Windshaper) | 6.4% (Dwarf) |
| [Shaman: Elemental](shaman/raid/elemental.md) | Skyborne (Windshaper) | 6.8% (Dwarf) |
| [Hunter: Survival](hunter/raid/survival.md) | Skyborne (Windshaper) | 6.6% (Dwarf) |
| [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | Human | 0.7% (Undead) |
| [Druid: Balance](druid/raid/balance.md) | Skyborne (Windshaper) | 6.2% (Night Elf) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | Skyborne (High Order) | 7.1% (Troll) |
| [Priest: Smite](priest/raid/smite.md) | Undead | 1.1% (Dwarf) |
| [Mage: Frost](mage/raid/frost.md) | Skyborne (High Order) | 7.1% (Troll) |

## Trinkets

The trinket pair in each spec's own gear sets (damage specs and tanks: raced in the community simulator; healers: by the healer lab's stat weights). Each opens its Wowhead page.

| Spec | Pre-BiS | Phase 1 BiS |
|---|---|---|
| [Druid: Balance](druid/raid/balance.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) |
| [Druid: Feral Combat](druid/raid/feral-combat.md) (tank) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| [Druid: Restoration](druid/raid/restoration.md) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) |
| [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) |
| [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) |
| [Hunter: Marksmanship](hunter/raid/marksmanship.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) |
| [Hunter: Survival](hunter/raid/survival.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Mage: Arcane](mage/raid/arcane.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Fire](mage/raid/fire.md) | [Eye of the Beast](https://www.wowhead.com/forever/item=13968), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Mage: Frost](mage/raid/frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Draconic Infused Emblem](https://www.wowhead.com/forever/item=22268) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Mage: Frostfire](mage/raid/frostfire.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Second Wind](https://www.wowhead.com/forever/item=11819) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Paladin: Holy](paladin/raid/holy.md) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) |
| [Paladin: Prot-Ret](paladin/raid/prot-ret.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Paladin: Protection](paladin/raid/protection.md) (tank) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) | [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440), [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557) |
| [Paladin: Retribution](paladin/raid/retribution.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Priest: Discipline](priest/raid/discipline.md) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) |
| [Priest: Holy](priest/raid/holy.md) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) |
| [Priest: Smite](priest/raid/smite.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Briarwood Reed](https://www.wowhead.com/forever/item=12930) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| [Priest: Shadow](priest/raid/shadow.md) | [Eye of the Beast](https://www.wowhead.com/forever/item=13968), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Rogue: Assassination](rogue/raid/assassination.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) |
| [Rogue: Combat](rogue/raid/combat.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) |
| [Rogue: Assassination/Subtlety hybrid](rogue/raid/hybrid-assassination-subtlety.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) |
| [Rogue: Subtlety](rogue/raid/subtlety.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) |
| [Shaman: Elemental](shaman/raid/elemental.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) |
| [Shaman: Enhancement](shaman/raid/enhancement.md) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965), [Hand of Justice](https://www.wowhead.com/forever/item=11815) | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213), [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| [Shaman: Restoration](shaman/raid/restoration.md) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) | [Burst of Knowledge](https://www.wowhead.com/forever/item=11832), [Mindtap Talisman](https://www.wowhead.com/forever/item=18371) |
| [Warlock: Affliction](warlock/raid/affliction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Demonology](warlock/raid/demonology.md) | [Eye of the Beast](https://www.wowhead.com/forever/item=13968), [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Destruction](warlock/raid/destruction.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Eye of the Beast](https://www.wowhead.com/forever/item=13968) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438), [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) |
| [Warrior: Arms](warrior/raid/arms.md) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Hand of Justice](https://www.wowhead.com/forever/item=11815), [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) |
| [Warrior: Fury](warrior/raid/fury.md) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Hand of Justice](https://www.wowhead.com/forever/item=11815) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437), [Hand of Justice](https://www.wowhead.com/forever/item=11815) |
| [Warrior: Protection](warrior/raid/protection.md) (tank) | [The Lion Horn of Stormwind](https://www.wowhead.com/forever/item=14557), [Defender's Grip Stabilizer](https://www.wowhead.com/forever/item=272440) | [Arena Grand Master](https://www.wowhead.com/forever/item=19024), [Vigilance Charm](https://www.wowhead.com/forever/item=18370) |

---
*Generated by `_reference/data/render_tier_list.py` on 2026-11-17 from the pages' own picks and numbers (talent and spell data: client build 1.60.1.70753; raid numbers: wowsims/forever at 2e6e77d (client 70938)). Simulations, not in-game measurements. Do not hand-edit.*

