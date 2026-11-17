# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (13/33/5) — [open the talent tree](https://talentsforever.com/rogue/60/005303002-3053130000011321451-005-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Combat Daggers), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (21/30/0, 713 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053032020051-32503300000123215--12)

## How to play

**Before the pull:** **Blade Flurry**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target (timing: see below)
2. **Vanish** (timing: see below); no global cooldown, so press it alongside the others
3. **Shank** (timing: see below)
4. **Adrenaline Rush** when Slice and Dice is active
5. **Eviscerate** (rank 8) when you have 4 or more combo points (timing: see below)
6. **Backstab**

**Backstab** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Combat in a raid is a dagger rotation run on energy: **Backstab** from behind builds combo points, **Slice and Dice** stays up, and 4 or more points go into **Eviscerate**. **Shank** goes on cooldown for energy, **Blade Flurry** before the pull and again when it is back, **Adrenaline Rush** once a fight.

**Why it works**

- **Slice and Dice** comes first: 30% more attack speed, and white hits are 45% of this build's damage in a full raid. Put it back up the moment it drops, even with 1 combo point: it lasts 9 seconds at 1 point and 21 at 5, and **Improved Slice and Dice** makes that 45% longer. The list never refreshes it early: while it is up, your points go into **Eviscerate**.
- **Eviscerate** goes at 4 or more points, and at 3 when **Slice and Dice** has 6 seconds or less left. Waiting for 5 wastes points: **Puncturing Wounds** gives **Backstab** a 45% chance to add a second point, and **Ruthlessness** adds a point after 60% of your finishers; the rotation search measured finishing at 4 rather than 5 0.6% better. **Flawless Execution** cuts its cost from 35 to 20 energy, and **Coup de Grace** and **Aggression** add 20% and 15% to its damage.
- **Shank** costs 5 energy and gives back 25; **Flash of Steel** adds 15 more and takes its cooldown from 10 to 8 seconds. Press it whenever it is ready and you have 80 energy or less (about 23 times in a 3-minute fight). In the simulator this build loses 8% of its damage without **Flash of Steel**, more than without any other talent but **Puncturing Wounds** (10%).
- **Adrenaline Rush** doubles your energy regeneration for 15 seconds on a 5-minute cooldown: once a fight, with **Slice and Dice** up and 50 energy or less, so little of the extra energy is lost at the cap. **Blade Flurry** (20% more attack speed for 15 seconds, 2-minute cooldown) goes 3 seconds before the pull and again when it comes back: twice in a 3-minute fight.
- **Backstab** is your only builder and your filler: 60 energy, from behind, with a dagger in your main hand; about 38 a fight and 30% of your damage. **Opportunity** adds 20% to its damage, **Lethality** 20% to its crit damage, **Puncturing Wounds** 30% to its crit chance, and **Hack and Slash** gives you 4% crit with daggers.

**Caveats**

- **Backstab** needs a dagger in your main hand and you behind the target. If you cannot get behind the boss, build with **Sinister Strike**; with a sword, take the swords setup this page links (21/30/0), which plays that way.
- **Garrote** is on the list, but it only works from stealth: the simulator presses **Vanish** a second into the fight and opens a **Garrote** right after, once a fight (**Vanish** has a 5-minute cooldown). Starting the fight in **Stealth** was not simulated.
- While **Blade Flurry** is up, your attacks also strike a second nearby target: with adds, it is your cleave.

**When to change it**

- In the last 6 seconds, skip **Slice and Dice** and put any combo points, even 1, into **Eviscerate**: a buff that outlives the boss does nothing.
- If no warrior keeps Sunder Armor on the target (a small group or a dungeon), keep **Expose Armor** up at 5 points. The simulator's list has a switch for it, off in a raid; an earlier search on the training dummy, where nothing else lowers armor, measured about 10% from it.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Assassination | 13 | Malice 5, Ruthlessness 3, Improved Slice and Dice 3, Lethality 2 |
| Combat | 33 | Coup de Grace 3, Lightning Reflexes 5, Puncturing Wounds 3, Deflection 1, Precision 3, Flawless Execution 1, Weapon Expertise 1, Aggression 3, Dual Wield Specialization 2, Blade Flurry 1, Hack and Slash 4, Flash of Steel 5, Adrenaline Rush 1 |
| Subtlety | 5 | Opportunity 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 781 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 767 | [13/33/5](https://talentsforever.com/rogue/60/005303002-3053130000012221451-005-12) |
| Phase 1 BiS | 773 | [13/33/5](https://talentsforever.com/rogue/60/005303002-3053130000012221451-005-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Main hand | [Felstriker](https://www.wowhead.com/forever/item=12590) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (21/30/0, 694 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-32503300000123215--12)
- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (21/30/0, 689 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-30532300000123215--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-17 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

