# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Assassination — Raid](../research/raid/builds/assassination-open-raid.md)** (31/19/1) — [open the talent tree](https://talentsforever.com/rogue/60/00530320250151031-30331300020103-001-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Vanish**; no global cooldown, so press it alongside the others
3. **Shank**
4. **Eviscerate** (rank 8) when you have 3 or more combo points
5. **Mutilate**

**Mutilate** is your filler: cast it whenever nothing above is ready.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 839 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 803 | [31/19/1](https://talentsforever.com/rogue/60/00530311250151031-30330311010103-001-12) |
| Phase 1 BiS | 817 | [31/19/1](https://talentsforever.com/rogue/60/00530311240251031-30331300020103-001-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.6; Phase 1 BiS 62.6; each item opens its Wowhead page, with where it drops and its enchant):

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
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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).

**Points that do nothing for this spec:** **Composure** (2) only counts toward the points the tree needs before **Aggression** and **Flawless Execution**.

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

