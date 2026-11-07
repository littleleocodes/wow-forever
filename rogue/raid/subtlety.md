# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md)** (21/0/30) — [open the talent tree](https://talentsforever.com/rogue/60/0053230020141--3352331313010011-12)

## How to play

**Before the pull:** **Premeditation**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Vanish**
3. **Preparation**
4. **Shank**
5. **Premeditation** when you have 3 or fewer combo points
6. **Rupture**: keep it on the target, when you have 3 or more combo points
7. **Cold Blood** right before your finisher
8. **Eviscerate** (rank 8) when you have 5 combo points

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Hemorrhage**: part of the rotation (about 30 times a fight)
- **Ghostly Strike**: part of the rotation (about 8 times a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Subtlety in a raid is a bleed rotation: **Hemorrhage** builds combo points, **Rupture** stays on the boss from 2 points, **Slice and Dice** stays up, and **Vanish** buys a second stealth opener of **Premeditation** and **Garrote**.

**Why it works**

- **Rupture** is your main finisher, not **Eviscerate**: put it back on the boss whenever it is off and you have 2 or more points. **Hemorrhage** makes the boss take 15% more **Rupture** damage and **Serrated Blades** adds 30%. The simulator measured **Rupture** from 2 points about 1.5% better than waiting for 4.
- **Slice and Dice** is still 30% attack speed: put it back up with 1 point when it drops. When both are off, **Rupture** goes first if you have 2 or more points; with 4 or more points and under 3 seconds left on **Slice and Dice**, refresh it before you **Eviscerate**.
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

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 607 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 681 | [20/0/31](https://talentsforever.com/rogue/60/0053030020141--0322320313110011-12) |
| Phase 1 BiS | 683 | [20/0/31](https://talentsforever.com/rogue/60/0053030020141--0322330313010011-12) (ties this build) |

**The gear** (average item level: Pre-BiS 66.5; Phase 1 BiS 66.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Field Marshal's Leather Mask](https://www.wowhead.com/forever/item=16455) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Zandalar Madcap's Mantle](https://www.wowhead.com/forever/item=19835) · *quest: Paragons of Power: The Madcap's Mantle* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587) · *sold by Illiyana Moonblaze*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587) · *sold by Illiyana Moonblaze*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454) · *sold by Sergeant Major Clate*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Marshal's Leather Handgrips](https://www.wowhead.com/forever/item=16454) · *sold by Sergeant Major Clate*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Marshal's Leather Leggings](https://www.wowhead.com/forever/item=16456) · *sold by Sergeant Major Clate*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) · *sold by Gaelden Hammersmith* | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345) · *sold by Sergeant Thunderhorn*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345) · *sold by Sergeant Thunderhorn*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-07 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 92c4c35 (client 1.60.1.70755)). Simulations, not in-game measurements. Do not hand-edit.*

