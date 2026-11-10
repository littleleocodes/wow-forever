# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Subtlety — Raid](../research/raid/builds/subtlety-ml-raid.md)** (12/8/31) — [open the talent tree](https://talentsforever.com/rogue/60/00530301-320003-325230031301001151-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Subtlety — Hemorrhage), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Premeditation**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Vanish**; no global cooldown, so press it alongside the others
3. **Preparation**
4. **Shank**
5. **Premeditation** when you have 3 or fewer combo points; no global cooldown, so press it alongside the others
6. **Death Mark** when you have 4 or more combo points
7. **Rupture**: keep it on the target, when you have 3 or more combo points
8. **Ghostly Strike** when Garrote has under 4 seconds left
9. **Hemorrhage**

**Hemorrhage** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Subtlety in a raid is a bleed rotation: **Hemorrhage** builds combo points, **Rupture** stays on the boss from 2 points, **Slice and Dice** stays up, and **Vanish** buys a second stealth opener of **Premeditation** and **Garrote**.

**Why it works**

- **Rupture** is your main finisher, not **Eviscerate**: put it back on the boss whenever it is off and you have 2 or more points. **Hemorrhage** adds 15% to your **Rupture** and **Garrote** damage and **Serrated Blades** adds 30%. The simulator measured **Rupture** from 2 points about 1.5% better than waiting for 4.
- **Slice and Dice** is still 20% attack speed: put it back up with 1 point when it drops. When both are off, **Rupture** goes first if you have 2 or more points; with 4 or more points and under 3 seconds left on **Slice and Dice**, refresh it before you **Eviscerate**.
- **Vanish** puts you back in stealth, which **Premeditation** and **Garrote** need. **Premeditation** adds 2 points, and **Garrote** adds 2 more with **Initiative** plus an 18-second bleed, 20 energy cheaper and usable from the front with **Dirty Deeds**; the simulator measured that **Garrote** worth about 1.6%. The full list presses **Vanish** only with **Slice and Dice** up, 60 or more energy and 3 or fewer points.
- **Preparation** finishes the cooldown of your other abilities, **Vanish** and **Premeditation** included. Press it right after your first **Vanish** opener, not at the pull, so you get a second one; the simulator uses it only while **Vanish** is on cooldown.
- **Cold Blood** needs no timing here: it boosts only **Sinister Strike**, **Backstab**, **Ambush**, **Eviscerate** and **Mutilate**, so **Hemorrhage** and **Ghostly Strike** leave it up and it waits for your next **Eviscerate**. **Eviscerate** spends the points that **Rupture** and **Slice and Dice** do not need.
- **Hemorrhage** is your filler and **Ghostly Strike** goes in on its 20-second cooldown, a small gain (about half a percent in the simulator). Keep a dagger in your main hand: **Hemorrhage** then deals 145% weapon damage instead of 100%, and **Ghostly Strike** 180% instead of 125%.

**Caveats**

- The list says to keep **Garrote** on the target, but it only works from stealth: you cast it right after each **Vanish**, about twice in a 3-minute fight.
- Damage you take breaks stealth, and the simulator does not model that. If something is hitting you or ticking on you, the stealth from **Vanish** may break before you use **Premeditation** and **Garrote**; then keep building with **Hemorrhage**.
- Almost all of this works from the front: **Hemorrhage**, **Ghostly Strike**, **Rupture**, **Eviscerate**, and **Garrote** with **Dirty Deeds**. Only **Ambush** and **Backstab** need you behind the target.
- Subtlety has no cleave: on adds, stay on the kill target, and do not **Rupture** a target that dies within 8 seconds.

**When to change it**

- In the last 8 seconds, start no **Rupture**; in the last 6, put 4 or more points into **Eviscerate** even with **Slice and Dice** down.
- Without a warrior's Sunder Armor on the boss, keep **Expose Armor** up at 5 points: **Improved Expose Armor** in this build makes it 10 energy cheaper and hands back 2 points. On the training dummy the simulator measured it about 2.5% better.
- The simulator starts every fight out of stealth. In the game you can start in **Stealth** and open with **Premeditation** and **Garrote** at the pull; that opener was not simulated.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Assassination | 12 | Malice 5, Ruthlessness 3, Improved Slice and Dice 3, Blood Splatter 1 |
| Combat | 8 | Coup de Grace 3, Efficient Strikes 2, Precision 3 |
| Subtlety | 31 | Setup 3, Master of Deception 2, Opportunity 5, Dirty Deeds 2, Camouflage 3, Initiative 3, Premeditation 1, Serrated Blades 3, Ghostly Strike 1, Preparation 1, Hemorrhage 1, Boot Knife 5, Death Mark 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 789 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 774 | [12/8/31](https://talentsforever.com/rogue/60/00530301-320003-305230031321001151-12) |
| Phase 1 BiS | 789 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.6; Phase 1 BiS 62.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005) · *quest: Saving the Best for Last*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005) · *quest: Saving the Best for Last*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Shadowcraft Bracers](https://www.wowhead.com/forever/item=16710) · *Instructor Malicia, Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Darkmantle Bracers](https://www.wowhead.com/forever/item=22004) · *quest: An Earnest Proposition*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715) · *quest: Armaments of War*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Frostguard](https://www.wowhead.com/forever/item=12797) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md) (21/0/30, 639 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053230020141--3352331313010011-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

