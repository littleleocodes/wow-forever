# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (13/33/5) — [open the talent tree](https://talentsforever.com/rogue/60/005303002-3053130000011321451-005-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Combat Daggers), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (21/30/0, 703 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053032020051-32503300000123215--12)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 773 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 767 | [13/33/5](https://talentsforever.com/rogue/60/005303002-3053130000012221451-005-12) |
| Phase 1 BiS | 773 | [13/33/5](https://talentsforever.com/rogue/60/005303002-3053130000012221451-005-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.3; Phase 1 BiS 62.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (21/30/0, 683 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-32503300000123215--12)
- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (21/30/0, 681 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-30532300000123215--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

