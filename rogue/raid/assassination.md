# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Assassination — Raid](../research/raid/builds/assassination-open-raid.md)** (31/19/1) — [open the talent tree](https://talentsforever.com/rogue/60/00530320250151031-30331300020103-001-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target (timing: see below)
2. **Vanish** (timing: see below); no global cooldown, so press it alongside the others
3. **Shank** (timing: see below)
4. **Eviscerate** (rank 8) when you have 3 or more combo points (timing: see below)
5. **Mutilate** (timing: see below)

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Assassination in a raid is a Mutilate rotation: **Mutilate** builds combo points two at a time, **Slice and Dice** stays up, and every 3 or more points go into **Eviscerate**. **Shank** goes on cooldown to keep **Venom** going, and **Vanish** opens one **Garrote** early in the fight.

**Why it works**

- **Slice and Dice** is 30% more attack speed: more white hits (35% of your damage in a full raid) and more chances for your poisons, which can proc on every weapon strike. Put it back up the moment it drops, even with 1 combo point; the list never refreshes it early.
- **Eviscerate** goes at 3 or more points: **Mutilate** brings 2 at once, **Seal Fate** adds a third when it crits (**Puncturing Wounds** gives **Mutilate** 15% more crit chance), and **Ruthlessness** adds a point after 60% of your finishers, so waiting for 5 wastes points. The rotation search measured 3 or more 0.6% better than 5.
- Each **Eviscerate** pays for itself: **Flawless Execution** cuts its cost from 35 to 20 energy, and **Relentless Strikes** gives each combo point a 20% chance to restore 25 energy. In the simulator these are the build's two most valuable talents (removing **Relentless Strikes** costs 12% of its damage, **Flawless Execution** 8%). **Coup de Grace** and **Aggression** add 20% and 15% to **Eviscerate**, about a quarter of your damage.
- **Mutilate** is your builder and filler: 60 energy, both weapons, 2 combo points, 20% more damage against a poisoned target; about 36 a fight and 20% of your damage. Its tooltip, unlike **Backstab**'s, does not ask you to stand behind the target. **Malice** and **Lethality** make its crits more frequent and bigger, and every crit feeds **Seal Fate**.
- **Shank** goes on its 10-second cooldown at 80 energy or less: it costs 5 energy, gives back 25, and with **Venom** raises your poison damage by 30% and your chance to apply poisons by 20% for 6 seconds (removing **Venom** costs 7%). Poisons are 18% of your damage in a full raid: **Instant Poison** on the main hand, **Deadly Poison** on the off hand, with **Vile Poisons** adding 20% to their damage and **Improved Poisons** 2% to their chance to land.

**Caveats**

- **Garrote** is on the list, but it only works from stealth: the simulator presses **Vanish** a second into the fight and opens a **Garrote** right after, once a fight (**Vanish** has a 5-minute cooldown; that **Garrote** is under 1% of your damage). Starting the fight in **Stealth** was not simulated.
- There is no **Expose Armor** in the list: in a full raid a warrior keeps Sunder Armor on the boss, and the two do not stack (only the stronger one counts).
- The list ends with **Backstab**, but this build never casts it: **Mutilate** is the builder whenever you have under 5 points. Blizzard built Forever's Assassination around **Mutilate** and **Venom**, and the simulator agrees: our hand-made Seal Fate **Backstab** build (28/21/2) did 687 DPS in a full raid against this build's 813.
- Poisons now go on a weapon together with a sharpening stone (Blizzard's rogue deep dive, 2026-10-07), so use both.

**When to change it**

- In the last 6 seconds, start no **Slice and Dice**: keep putting 3 or more points into **Eviscerate** even with it down.
- If no warrior keeps Sunder Armor on the target (a small group or a dungeon), keep **Expose Armor** up. The simulator's list has a switch for it, off in a raid: at 5 points, renew it when it has 16 seconds or less left, before any other finisher. An earlier search on the training dummy, where nothing else lowers armor, measured about 9% from it.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Assassination | 31 | Malice 5, Ruthlessness 3, Improved Slice and Dice 3, Vigor 2, Lethality 2, Vile Poisons 5, Improved Poisons 1, Relentless Strikes 5, Venom 1, Seal Fate 3, Mutilate 1 |
| Combat | 19 | Coup de Grace 3, Lightning Reflexes 3, Puncturing Wounds 3, Deflection 1, Precision 3, Composure 2, Flawless Execution 1, Aggression 3 |
| Subtlety | 1 | Opportunity 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 844 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 825 | [31/19/1](https://talentsforever.com/rogue/60/00530311230351031-31131301020103-001-12) |
| Raid BiS | 835 | [31/19/1](https://talentsforever.com/rogue/60/00530311220451031-31131301020103-001-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.5; Raid BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Raid BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Main hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Raid BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

**Points that do nothing for this spec:** **Composure** (2) only counts toward the points the tree needs before **Aggression** and **Flawless Execution**.

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

