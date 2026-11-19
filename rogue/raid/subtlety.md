# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Raid](../research/raid/builds/subtlety-ml-raid.md)** (12/8/31) — [open the talent tree](https://talentsforever.com/rogue/60/00530301-320003-325230031301001151-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Subtlety — Hemorrhage), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Premeditation**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target (timing: see below)
2. **Vanish** (timing: see below); no global cooldown, so press it alongside the others
3. **Preparation**
4. **Shank** (timing: see below)
5. **Premeditation** when you have 3 or fewer combo points; no global cooldown, so press it alongside the others
6. **Death Mark** when you have 4 or more combo points
7. **Rupture**: keep it on the target, when you have 3 or more combo points (timing: see below)
8. **Ghostly Strike** when Garrote has under 4 seconds left (timing: see below)
9. **Hemorrhage**

**Hemorrhage** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Subtlety in a raid is a Death Mark rotation: **Hemorrhage** and **Shank** build combo points, **Garrote** and **Rupture** stay on the boss, **Slice and Dice** stays up, and 4 or more points go into **Death Mark**, which stores part of your damage and deals it a second time. The list never casts **Eviscerate**.

**Why it works**

- **Death Mark** is your main finisher: 25 energy, a 10-second cooldown, at 4 or more points. For 6 seconds it stores a portion of the damage you deal the target per combo point, **Garrote** and **Rupture** damage at twice the rate, then deals what it stored, up to a maximum your attack power and crit chance raise. **Coup de Grace** raises its damage and storage rate by 20%. It is 23% of your damage in a full raid (about 14 a fight); with it in the build, the simulator's list spends no points on **Eviscerate**.
- **Ghostly Strike** lets your next **Garrote** within 7 seconds skip stealth, so **Garrote** stays on the boss all fight: **Ghostly Strike** when **Garrote** has 4 seconds or less left, then **Garrote** when it runs out (about 7 a fight, 10% of your damage). **Blood Splatter** makes **Garrote** last 27 seconds instead of 18, **Dirty Deeds** makes it 20 energy cheaper and usable from the front, **Initiative** adds a second combo point to it, and **Opportunity** adds 20% to its damage.
- **Rupture** goes on whenever it is off and you have 3 or more points (about 8 a fight, 10% of your damage). **Serrated Blades** adds 30% to it (and your attacks ignore 9% of armor), **Hemorrhage** adds 15% to **Rupture** and **Garrote** for 15 seconds, and **Blood Splatter** makes **Rupture** last 6 seconds longer.
- **Hemorrhage** is your filler (35 energy, 30 with **Efficient Strikes**; 145% weapon damage with a dagger in your main hand), and the list renews it whenever its 15-second effect has run out. **Shank** costs 5 energy, gives back 25, and with **Boot Knife** adds 2 combo points: press it when it is ready, with 3 or fewer points and 80 energy or less.
- Below 5 points the list keeps building; at 5, with **Death Mark** on cooldown and **Rupture** and **Slice and Dice** up, it waits. It also holds **Hemorrhage** while **Garrote** has under 6 seconds left, so the energy is there for **Ghostly Strike** and the new **Garrote** (the rotation search measured that 0.5% better than holding from 8 seconds). **Slice and Dice** (30% attack speed) goes back up with 1 point whenever it drops.
- **Premeditation** adds 2 points: before the pull, then on its 2-minute cooldown with 3 or fewer points (the simulator needs no stealth for it, and its beta tooltip asks for none). **Vanish** opens a **Garrote** a second into the fight, and **Preparation** finishes the cooldowns of **Vanish** and **Premeditation** once a fight. Each of the two talents measured about 1% in the simulator.

**Caveats**

- The **Garrote** after **Vanish** needs stealth, and damage you take breaks it; the simulator does not model that. If something hits you right after **Vanish**, the next **Ghostly Strike** opens the **Garrote** instead.
- Almost all of this works from the front: **Hemorrhage**, **Ghostly Strike**, **Death Mark**, **Rupture**, and **Garrote** with **Dirty Deeds**. Only **Ambush** and **Backstab** need you behind the target, and the list casts neither.
- Subtlety has no cleave: on adds, stay on the kill target, and do not **Rupture** a target that dies within 8 seconds.

**When to change it**

- In the last 6 seconds, start no **Rupture** and no **Slice and Dice**: they would outlast the boss.
- Without a warrior's Sunder Armor on the boss, keep **Expose Armor** up at 5 points; the simulator's list has a switch for it, off in a raid. An earlier search on the training dummy measured it about 2.5% better.
- The simulator starts every fight out of stealth. In the game you can start in **Stealth** and open with **Garrote** at the pull; that opener was not simulated.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Assassination | 12 | Malice 5, Ruthlessness 3, Improved Slice and Dice 3, Blood Splatter 1 |
| Combat | 8 | Coup de Grace 3, Efficient Strikes 2, Precision 3 |
| Subtlety | 31 | Setup 3, Master of Deception 2, Opportunity 5, Dirty Deeds 2, Camouflage 3, Initiative 3, Premeditation 1, Serrated Blades 3, Ghostly Strike 1, Preparation 1, Hemorrhage 1, Boot Knife 5, Death Mark 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 817 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 797 | this build |
| Raid BiS | 799 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.4; Raid BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Raid BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Fiendish Machete](https://www.wowhead.com/forever/item=18310) · *Alzzin the Wildshaper, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Raid BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md) (21/0/30, 661 DPS in a full raid; fails the signature-spell check: core share 55% under 60% (melee, Hemorrhage, Ghostly Strike, Ambush, Eviscerate, Death Mark)) — [open the talent tree](https://talentsforever.com/rogue/60/0053230020141--3352331313010011-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

