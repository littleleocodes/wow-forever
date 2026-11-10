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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 813 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 803 | [31/19/1](https://talentsforever.com/rogue/60/00530311250151031-30330311010103-001-12) |
| Phase 1 BiS | 817 | [31/19/1](https://talentsforever.com/rogue/60/00530311240251031-30331300020103-001-12) (as good as this build in this gear) |

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
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzUWH1sFMcV99s7342fHXOMv85jIOODgDl6Zm/PpoCh+AsSxzSYOJTrH1VY22vu8HnX3V3zEaXIpaKqStOWJimKpUqIOE0KLUJuIQipqBUp0IpKKa2QKtGUEqLQKlUjK1Dpikq1e3tmsc/ntII23T/udua9eW/mzfv4vcV5BAIQBA51sA0SMAQjAF8DOAzwBgAtsamCRV0J7EKYCAEv24t+cusYBG8Uo5fc+Bagl/z2UgD95NxrEPyNz3r5yZzgu6XoJx8dg+AfrJdLlwLBP5ailxx4O4A+cmXYWu0nF/ZBZnr/i5aYs69ZvyffDqCXnHgZ0E/eeRmCH5Sij/yt1/r3kHeUUH3gYrLuZkq809R15ZsQ/2jbd0C40zQK5FX5h/LVlu92HwXhG8kTcG39afjgCLQS+xDQDGeERaLYGBNj0ajUIEqNUTEWjcTEWCwaE0VREqNiLCKK0YuC97pwrg7nop8VooecTIV86EUhEkPqTL2vhvxYiJ6IZOAy5FiR9lEMdJuybvIOlXebipwyE8yPhXVe8o9HHOaoQSNsmcO8xVD4+t1DmqHwFn1Q06/DXJzzWTmpmnJSdSi0h23DrXQLsrSvCiusJZ+T1aSR4P2aztvlQXm7gpVpXxnOtWgtgz3DRoJvGlJURcdH0755yNqGdV1RTd6lJVXT4CnFMLiZkFXeaB9kf5wa7IuYoP3IQsEZZeXTP5seLA4VoV+ytI3GbaWjcXoG2JuAx4C+AffRkYYDxEeF5woYmfA4cw9tZ/cEd6vtfIOcSvGOwcGkqqgmBsKl1kZWFzD78qOGfZsC+Xkp/QGw7wOOAj0E0/e7P/6J2ut8VoOUBrA0VIJ4BLLz9j38WaWL2SJkLIglIURy2WvNnkwhGYfMm3V2cvUwUJHVYxWtQHLEoWDRZa9DlMqQZBknQ4YGWCniOPjRQ243BGF1AZ3H2HWowor1qqJv38O7NC2VVLfztoTSO2DQvex51NkQrqVNToS0aprJO9Vkv8I7VW2Xal+Jl3r2QYGlBCHmzFjeYh98pYjLaQSrQ1X5RbgW2Bt/4cXNtIM9jp+ha6ZyNIruU+AjoeLsyQ9NbHQPrx4Ga1fk1ABVWC9upE9mjXVqAIO00sWHRUcg++qiWAIdivXqUpvDwqcG6Bq2GhfSWpeaWVZbUidXL2IhDIYriY+So856RtCH3mj9qsEsO13Gljqu+biqDSp8/bCuDMg8wrsT2nCqj7fJhmkzj01stJ1pHmNTnMnZyclUEJgXhSCjvwb2K8CfAf0p4PPsOXyMLpxq9mgjzgk9gsXXCUFfHZD3jndhlC7PmmpsYuPUFVJjjpkFdF6OWSJZMs7e6sK1rMmme+7zqkxOcZJzhG/UdvH2YV02k5qKxeNAMscN2vcduNNEa1j1dN906gTlbAGWU+rE6D2GBuZsgh4F9jrg94COgm2+yUPf/Pbme4O7I4DlbLqcmCt/HohjTagaq9K+cqQbktsTJm/p0YZNbmp8vdqHS0NL8LG0L4TZyhPhXbqy08qOm8yEovMNSSuHKrpxv/X/fneTpYwciNNXgR0GfAnoQcAlad8iDLWYXNN5q5LSdnErNbWlkkNDVmA/k9AVI6Gl+nBB2leD1S092k7FZrFTsYv+gDbtZL3bDfQFYF8HHAG617YXuOyVP5NOS+dj8X/bahkPOZT1EPInlf5VoEl5KPWsNmRySZRWRKLRiLhqNe9NyOp2pc8yoNzXp/Txnj3cTChc10zb3bihyHpvgtcZisJlw5ANI6nalIguJ/siWb5Ihq9+h6GpS9ldwFtAJwB/DOxEtkTZFrBxiFTfiLX00WmWacDiy17rwj3kw3c78Qm6YbrTYmW4nHgpOWOnjNu2E6Owwshr1AhdlsNtH7iXvne8y7b3WJzuYAl8ln5h9qq6kNWiP1SInrSnwNl/e1I39/B2RekznKJRES4jXurf4UAY+8gNhq3rvEa3si3YSTtwbtpXiiUWEmmVewcMU+7BstBcnDMOJegld0eACoHCIMy6J8ukNvsFgb0l4BmBvim4Hev4wc1ByKVt1sOeB3YO8t5UG23BheFaUmjny+pxoZIAdSLhdkM2Jg7G8woJhfisEc/TvvlY06HydisAdK71cwcWtMl29nDAUu4knEk8UypSS6+Z3KlYofSUZvKnFblvj31FB+P0dYGNCXhIoC8Js1vpArC38lupnbbionDIsRIbF6rus1LRhMe6QiuG/k/MNBn09H2B3RDw9wK9ImBFqOw/crMHZcC7I/mlfHIMiEvZEjtL+KZkiZVGBnhfJ1ZpAnJem4zu4f9mRcjg89/9AoKe8NrpbWaY1TnXOmkHF77LIHQ7ls5uDT8zE4BvYqscITNDRakSy/UshpmEZKtEaf707pkWoR8L++WUoUjV9/ugmzR/eivtJtfO0HBRG+ua+rAiLcjRV7pFcCzr0pMa704lexUuq328PdmruDnq88UDnQowG6WOHO5MG6iUu7pKBgbTvoqcu5CWYNkU1UmDi3RqbRelzjxhQuvZp6ZV6GgerWs+DuyjOU8jGtLyvBFJp3jHpxulxblwAnWA/ZMO3wpDUmYIZGp1Y7k/u2CULcdAqBRLxqHI9nCrTGNNuJp4ackZ15yFLtETXWFIT+WLEyrS+lygc+Y0I31+dqRDG2lsphPkE/2lj5O+bAjjamWt7srd52Ta3ExvadHq6GL3sDpcRbyuLrLoiN8hSV+BfNmAKrTXrdMls5N1uNvIUwPZhvbUQBBsjYU5Ndpg12M7xSRZ2jr9QwBtYy1Z5FhIvnpwstHyugce90BwD8AaSI/mQIvUSfYC2afeFC7Ch4L0ZU+B/ZQ3/wW8KGBB6J9CkTVRMNLfXD36ivX8cl1tv/1cWSddE4Jevi58Wij4nzxmc/btoT6Lf/TQ9Kyyf58ea25xJpq3WR+1XwF7UHBtXdhDTle1ur59i7ASmuEJ6II4JGAIdsNu4V8DAMlwX6o=).

**Points that do nothing for this spec:** **Composure** (2) only counts toward the points the tree needs before **Aggression** and **Flawless Execution**.

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

