# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (13/33/5) — [open the talent tree](https://talentsforever.com/rogue/60/005303002-3053130000011321451-005-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Combat Daggers), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (21/30/0, 693 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053032020051-32503300000123215--12)

## How to play

**Before the pull:** **Blade Flurry**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Vanish**; no global cooldown, so press it alongside the others
3. **Shank**
4. **Adrenaline Rush** when Slice and Dice is active
5. **Eviscerate** (rank 8) when you have 4 or more combo points
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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 764 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 755 | [12/34/5](https://talentsforever.com/rogue/60/005302002-3113130201012221551-005-12) |
| Phase 1 BiS | 765 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.4; Phase 1 BiS 62.1; each item opens its Wowhead page, with where it drops and its enchant):

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
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (21/30/0, 675 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-32503300000123215--12)
- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (21/30/0, 673 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-30532300000123215--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

