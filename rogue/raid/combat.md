# Combat Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Combat

**[Combat — Raid](../research/raid/builds/combat-ml-raid.md)** (13/33/5) — [open the talent tree](https://talentsforever.com/rogue/60/005303002-3053130000011321451-005-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Combat Daggers), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Daggers setup. The spec's best build for each other setup, in a full raid:

- Swords: [Combat (optimized, swords)](../research/raid/builds/opt-combat-swords-raid-raid-dps.md) (21/30/0, 709 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053032020051-32503300000123215--12)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 777 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 755 | [12/34/5](https://talentsforever.com/rogue/60/005302002-3113130201012221551-005-12) |
| Phase 1 BiS | 765 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.6; Phase 1 BiS 61.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

## Other builds of this spec

- [Combat Swords](../research/raid/builds/combat-swords-raid.md) (21/30/0, 690 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-32503300000123215--12)
- [Combat Daggers](../research/raid/builds/combat-daggers-raid.md) (21/30/0, 687 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/2053232020101-30532300000123215--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

