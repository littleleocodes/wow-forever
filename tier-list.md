# Tier list: raid damage, healing and tanking

Every spec of every class, by the build its raid page recommends. Tiers by how far each spec is behind the best of its role: **S** within 3% of the best, **A** within 10% of the best, **B** within 20% of the best, **C** more than 20% behind. Differences under 2-3% are a tie in these simulations, so the order inside a tier means little. Leveling is not tiered here: each class page ranks its specs for leveling.

## Damage

DPS in a full raid: a 3-minute fight against a raid boss with every raid buff and debuff up, phase-1 gear from one item pool for every spec, racials off. The community's combat simulator (ElliotWood/Forever, commit 2ce8265) with this project's patches and tuned rotations: a model of the beta, not a measurement in the game. Patches that move whole classes (from Forever's client and community numbers, `_reference/data/raidsim/patches/README.md`): hunter pets scale with the hunter's gear (a Beast Mastery build +8.5%), warlock demons with the warlock's (+3.6-4.2%), pets hit with a 2.0 s base (+3.0-3.9% for hunters with a pet); the boss is an Elemental, which hunters' Improved Tracking counts (+5%). Pet scaling is the largest difference from MythicSim's tier list (its engine gives pets nothing from the hunter; [our comparison](_reference/mythicsim-comparison.md)), which also ranks in dungeon gear without trinkets.

| Tier | Spec | Build | Full raid DPS | Behind the best |
|---|---|---|---|---|
| **S** | [Hunter: Beast-Survival](hunter/raid/beast-survival.md) | 16/11/24 | 1004 | best |
| **S** | [Hunter: Survival](hunter/raid/survival.md) | 5/11/35 | 996 | 0.8% |
| **S** | [Paladin: Retribution](paladin/raid/retribution.md) | 10/8/33 | 979 | 2.5% |
| **A** | [Warrior: Arms](warrior/raid/arms.md) | 37/14/0 | 964 | 4.0% |
| **B** | [Hunter: Marksmanship](hunter/raid/marksmanship.md) | 5/41/5 | 893 | 11.1% |
| **B** | [Warrior: Fury](warrior/raid/fury.md) | 20/31/0 | 881 | 12.3% |
| **B** | [Hunter: Beast-Marks](hunter/raid/beast-marks.md) | 27/21/3 | 852 | 15.1% |
| **B** | [Hunter: Beast Mastery](hunter/raid/beast-mastery.md) | 31/20/0 | 847 | 15.7% |
| **B** | [Warlock: Demonology](warlock/raid/demonology.md) | 2/31/18 | 822 | 18.1% |
| **C** | [Warlock: Affliction](warlock/raid/affliction.md) | 30/0/21 | 752 | 25.1% |
| **C** | [Shaman: Enhancement](shaman/raid/enhancement.md) | 19/32/0 | 727 | 27.6% |
| **C** | [Warlock: Shadow Bolt hybrid](warlock/raid/shadow-bolt-hybrid.md) | 20/11/20 | 723 | 28.0% |
| **C** | [Warlock: Destruction](warlock/raid/destruction.md) | 10/11/30 | 705 | 29.8% |
| **C** | [Priest: Shadow](priest/raid/shadow.md) | 18/0/33 | 699 | 30.4% |
| **C** | [Rogue: Combat](rogue/raid/combat.md) | 16/33/2 | 695 | 30.8% |
| **C** | [Druid: Feral Combat](druid/raid/feral-combat.md) | 9/33/9 | 694 | 30.9% |
| **C** | [Shaman: Elemental-Enhancement](shaman/raid/elemental-enhancement.md) | 17/26/8 | 690 | 31.3% |
| **C** | [Mage: Arcane](mage/raid/arcane.md) | 35/11/5 | 689 | 31.4% |
| **C** | [Mage: Arcane-Frost](mage/raid/arcane-frost.md) | 28/0/23 | 687 | 31.6% |
| **C** | [Mage: Fire](mage/raid/fire.md) | 12/34/5 | 685 | 31.8% |
| **C** | [Mage: Frost](mage/raid/frost.md) | 21/0/30 | 680 | 32.2% |
| **C** | [Mage: Frostfire](mage/raid/frostfire.md) | 0/29/22 | 675 | 32.8% |
| **C** | [Rogue: Assassination](rogue/raid/assassination.md) | 30/19/2 | 672 | 33.1% |
| **C** | [Rogue: Daggers (split)](rogue/raid/daggers-split.md) | 21/28/2 | 669 | 33.4% |
| **C** | [Rogue: Subtlety](rogue/raid/subtlety.md) | 20/0/31 | 640 | 36.3% |
| **C** | [Priest: Smite](priest/raid/smite.md) | 31/17/3 | 597 | 40.6% |
| **C** | [Druid: Balance](druid/raid/balance.md) | 33/5/13 | 586 | 41.6% |
| **C** | [Shaman: Elemental](shaman/raid/elemental.md) | 29/22/0 | 515 | 48.7% |

## Healing

Healing capacity in this project's healer lab: how much of the lab's standard raid damage the healer keeps one group (a tank and four raid members) alive through for five minutes, in 90% of the runs. Healers are in no community simulator; the lab is a model of stated assumptions (`_reference/data/heallab/tables.py`), the same group, damage and fight for every class. Real raids spread damage differently and value utility (dispels, buffs, battle resurrection) the lab does not count.

| Tier | Spec | Build | Capacity | Behind the best |
|---|---|---|---|---|
| **S** | [Shaman: Restoration](shaman/raid/restoration.md) | 0/10/41 | 0.69 | best |
| **S** | [Priest: Holy](priest/raid/holy.md) | 21/30/0 | 0.69 | 0.3% |
| **B** | [Priest: Discipline](priest/raid/discipline.md) | 30/21/0 | 0.61 | 11.5% |
| **B** | [Druid: Restoration](druid/raid/restoration.md) | 11/5/35 | 0.60 | 13.7% |
| **B** | [Paladin: Holy](paladin/raid/holy.md) | 34/11/6 | 0.58 | 15.9% |

## Tanking

Not tiered: each tank's tank value is measured against its own class's hand-made build, and each tank plays in its own gear set, so the numbers do not compare across classes. Threat and damage taken per second below are in a full raid against a raid boss (the community simulator, with this project's patches: Bear Form's threat is our +50% patch).

| Spec | Build | Threat per second | Damage taken per second | Tank value (own class's hand draft = 1.00) |
|---|---|---|---|---|
| [Druid: Feral Combat](druid/raid/feral-combat.md) | 7/35/9 | 1221 | 989 | 1.00 |
| [Paladin: Protection](paladin/raid/protection.md) | 0/32/19 | 504 | 912 | 1.04 |
| [Warrior: Protection](warrior/raid/protection.md) | 14/5/32 | 686 | 1162 | 1.01 |

---
*Generated by `_reference/data/render_tier_list.py` on 2026-10-15 from the pages' own picks and numbers (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

