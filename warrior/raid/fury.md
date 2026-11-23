# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md)** (17/32/2) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (20/31/0, 921 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

## How to play

**Setup, before the pull:** **Berserker Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst** until the last 30 seconds of the fight
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Reckless Swings**
4. **Whirlwind**
5. **Execute** when the target is below 20% health
6. **Hamstring** when **Bloodthirst** is more than 1.1 seconds from ready and **Whirlwind** is more than 2 seconds from ready
7. **Bloodrage** when you have less than 23 rage; no global cooldown, so press it alongside the others
8. **Heroic Strike** when you have 68+ rage; no global cooldown, so press it alongside the others

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Berserker Rage**: a cooldown, use it in the last 45 seconds of the fight (about 3 times a fight)
- **Recklessness**: once a fight, in the last 45 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a two-handed weapon: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in every other gap and **Heroic Strike** only at 90 rage or more. **Death Wish** waits for the last 45 seconds and **Recklessness** for the target's last 20%.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 8-second cooldown with **Improved Whirlwind**) are your main attacks: press **Bloodthirst** the moment it is ready, and **Whirlwind** whenever **Bloodthirst** is more than 1.5 seconds away. **Whirlwind** needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them. A full raid gives you the rage for this order; the simulator's rotation for a warrior alone on a training dummy, short of rage, puts **Execute** first.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) waits until 45 seconds are left and **Recklessness** (+100% crit chance for 15 seconds) until the target is below 20%, so both cover the execute phase; **Reckless Swings** (your next 4 melee attacks give 5 more rage) joins them in the last 34 seconds. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) is your filler: cast it whenever nothing else is ready, about 56 times a fight. It is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem; the simulator measured 6.8% more damage casting it freely than only above 80 rage with **Bloodthirst** and **Whirlwind** more than 1.5 seconds away.
- **Heroic Strike** is a rage dump, not a filler: queue it only at 90 rage or more, and not below 20%, where **Execute** wants every point. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**. The simulator measured 5.3% more damage after dropping its default line at 40 rage, and 0.2% more after adding this one at 90.
- **Bloodrage** (1-minute cooldown) goes whenever you are under 90 rage, about twice a fight.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one at the pull, one when its cooldown is back). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 13% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage the full list adds **Cleave**.
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and use **Hamstring** only above 80 rage. That is the simulator's two-handed rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** to 5 was worth 5.8%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** and **Recklessness** also make you immune. The simulator's boss never fears, so the list leaves it out.
- With a weapon in each hand (the page's dual-wield option), the simulator's dual-wield raid rotation differs: **Reckless Swings** on cooldown, **Heroic Strike** from 67.5 rage on a single target, **Hamstring** only when **Bloodthirst** is more than a second away and **Whirlwind** more than 2 seconds, **Recklessness** with **Death Wish** in the last 45 seconds, and no **Bloodthirst** in the last 30 seconds. **Whirlwind** hits with both weapons there.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 17 | Improved Heroic Strike 3, Deflection 2 (tier point: needed to reach Anger Management), Improved Rend 3 (needed for Deep Wounds), Improved Tactical Mastery 3 (needed for Anger Management), Anger Management 1, Deep Wounds 3, Impale 2 |
| Fury | 32 | Cruelty 5, Unbridled Wrath 5, Furious Precision 3, Dual Wield Specialization 5, Reckless Swings 1, Improved Execute 2, Improved Berserker Rage 2, Death Wish 1, Improved Whirlwind 2, Flurry 3, Bloodthirst 1, Blood Craze 2 (tier point: needed to reach Dual Wield Specialization) |
| Protection | 2 | Improved Bloodrage 2 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a full search on 2026-11-08 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 987 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 832 | its own set |
| Pre-BiS | 958 | its own set |
| Raid BiS | 988 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.2; Pre-BiS 62.4; Raid BiS 63.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Wyrmhide Spaulders](https://www.wowhead.com/forever/item=12082) · *quest: A Taste of Flame* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Death Grips](https://www.wowhead.com/forever/item=18722) · *Magistrate Barthilas, Stratholme*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* |
| Legs | [Handcrafted Mastersmith Leggings](https://www.wowhead.com/forever/item=13498) · *Goraluk Anvilcrack, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Blackstone Ring](https://www.wowhead.com/forever/item=17713) · *Princess Theradras, Maraudon* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Tooth of Eranikus](https://www.wowhead.com/forever/item=10837) · *Shade of Eranikus, The Temple of Atal'Hakkar*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Mirah's Song](https://www.wowhead.com/forever/item=15806) · *quest: Kirtonos the Herald*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Raid BiS: Quick Strike Ring (Molten Core); Raid BiS: Onyxia Tooth Pendant (Onyxia's Lair)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11sFFUU3jMzO3v2FNbhFmR6C2ZsCA6DW+/M7gBFY7dEjT8x4k8CQaNdu1t2jXab3Rog+kAbYgwaQGuMLI2tCrGpNobGH9KYPmhiUIORB5toMJLqgw888OCTMWLusNuVbR8Madf7sHvmnnvnft/5znyToXUIBphggQ3dkIN+OAjwMsAYwDgAWxFkFZndBvztNagZwPeRjhdy5lwTafjSJJCKU0+SjiM587xOOn73uPlrjHQ8sdf8OUYRfPd1MEcjpOG3I0A6TuflTh2PPmf+EiMND10ySMPTh+V93n+CNPzke4N0/OEx85K8y8wL8l/D4aPQZhtf5e3fRmHn7BHY/Uf3YVCG8mWIvpf+MP1T1+gpmADl1fxlGMrvwAA3pGBasRJeQiSEmxDCiwtf+AnhCd/1PFcIL+HGvbOKNqecbGaHgPWk+599qtA/YHnC2xJ33bjYtt3qyaX79mYzVqFopTOZbMZ6+oA1kMtaxcJAeiBf6LNK2XSxJ2fZpWzW6n2+eCCe2RcvpvOZeHVF/OqK9mdKhb5NfD2tcm5AnSn3h3iEwqQmRIkj6baGs9PAUvxOSjCXWp0WVFnsC2iisB3Gc3uYYoR5mFQCl1ibQbGpSmpmV5CKVNdFeUSuM958lBFHrpNmnH8N2IkF/ERceEvPL0mb+aaAo1bjmPRLtNphFdpESLrnuu1+SSLF8W52EwLn9bvcSv6zleytxdB3LD16lzbxW+pxJESJmGNU0CPppLlJUeIaKSZnW7m/GGVPLKDsJgPKOml4YQyYzxP/9TTZI1LIz09d17bBj697W6G+7m5cJJe+7kGf4vDww+yDRZROuEt/4l10B9tOG/kGojJGSDWubDZ4NR68tRYP5Q1OhhOTGhVDEicprl8R/8XGPFRr6mVL+qXtIdbfmIciKs+0YnhsJWvmqyj8jaIgyF6xw/jpO1C1GTw9XouP/PUQewUaU50N1OKsxTBrmoB5I5WASBGlGvQu3kkuuy2QMszUOQhV7bSVtwSzek3gpKjSJEIL7DD+OAZsskHviHvodtZB653WelKBc7rtrueXyHRuxDCjCagyvIrcCyjbKp7rYEP1eEVH3FsGvK2BhahB+QLD8rx2X1YXr6xm9yHwuwNC8p1WRyhYLV2RuGPW0ZnPSWL45TFgI9CYhvfJZhuDloBrGqVilFWWW7a2+zxKEQtsxI/2sKEGtceCcm/ZWiv3DDTGsXfRg+yBwEOlcjqLToCUSXZptByphLTO4ahfoyqVI9WYmuZQ9jbgG2MwL/JavoZWtBHhFMgOKjcHzMrNpvq7chYuK5lBNRSM1akJpYmiFEHVBvEntP2tROV86GBvqqV8XI6vO2/uDcZsp3dRMTWr0zmjhP6XMZCqRss6Nk4u2zkdwe8jJ1NdlYlUt/xWOA7BRehip6PimbU7/vVJIWAbpOBe2Am7IQf9sB/2K/8MAOpJuWY=); Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3P2pN1Oblo7uWllDKVOp268M7vTNlXMtqj4g1j1oaUIZtvdmhXJht2IKSg0QaH4UysRaVcxEVMM0VasVWuRPlSRKi2kCAH/MEQffOhDBJ9ErNzpbtZu8iAlWe9DOLnn3L3fd74z3zC0BsEEC2xwoBt6oA8OABwEGAUYB2DLwqwis1uAj61CzQT+LOk4vceaaSIVPxogDb+9YJKBb02a1iWdDPzy1ArrlzjpeDBn/RSXGxdMa8QgDYcnZeHvJ0AeNvCzc83Wz3HS8OXLJml4ZNIkFd99lDT8OCz84flm67L8gdkTIAMNh1+Bdsf8Ku/8OgI7pg7Brj+6XwBlKF+G2DuZ9zPfbxs5BhOgvJSfhaH8dgzRQxrOKHbST4qk8JJC+AkRiCApfBF4vu8J4Se9hH9e0WaUsRb2HLC9mb4nHyv09du+8DclPC8htmy19/Zkeh/PZe1C0c5ks7msvWe/3d+Ts4uF/kx/vtBrl3KZ4t4e2ynlcva+p4r7E9mnE8VMPpuoViSuVnQ8USr0buBrqdldgTpT7otwg6KkJkWJI+mOhlNngKX5HZRkHrW5raiy+DlooqgTxYu7mWJGeZRUAo9Yu0nxk5XU2Z1hyqjWxbgh68zXH2HEkeukmZdeBfbGPH4iIfzF55eijXxDyFGrcUwFJVrpsgptIiTd97yOoCSR4ng3uxGB8/pTXiX/6XJ2ZCH0nYuP3qMN/OZ6HElRIuaaFfRIOmleSpS4RorF2WYeLETZF/Moe6mQsk4a/jgKLODJ/3qbnBEp5OfHruvY4KnrPlao77uXEKnF73s4pzg8/BB7bwGlk97i33gn3c620nq+jqiMBqnmlY0mr8aDt9TiobzJyXTjUqNiROIkxQsq4j/TmIdqVb1sqaC0NcL6GvNQxOSddhwPL2ctvJmi3ygKgpwVJ4qfvA1Vm8EPx2vxob8eZC9CY7qzjlrd1RhlTRMwZ6QSECmiVIO+jXeRx24NpYwydQYiVTtt463hrl4TOCWqNInQBieK340CO96gd8TddBvrpLVuWz2p0Dm9Ds8PSmS5N2CU0QRUGV5F7oeUHRUvdrKheryiM+EvAd620ELUsH2hYfl+RyC7i1dWsnsR+F0hIflOqyMUVktXJO5adXTmcpIYfnEY2JvQmIEPyGHrw5GAawalYpRVlps2dwQ8RoYNDuIHu9lQg8ZjXrs3ba61+yw0xrF30gPs/tBDpXI6i02AlElOaaxsVEJa43LUr1GVykY1pqYZlLMN+NoozIm8mq+iZe1EeBLkBJVbQmblFkv9TTkPs0p2UI2Ea2V6QmmiGBmoOiD+hPa/lZjcjxzYl24tH5Xr666b9oVrqsufVizN7nJPK5H/ZfWnq9GSrvXHl+yezvDvw2PpbZWNdLf8YjgK4T+R6S5XxdOrt//rw0LAFkjDPbADdkEP9MEADCj/DAAW+L1F); Raid BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11sFNUX3zMzO3P2FJbpLfyZ3sI/Y0NwGNx6Z3YHKBq7EDV+xIj6AOHFLuzWrtFus1sjJMbQRhKi8mFqjKzE1kiTpgpGgorE8IDGoEICMWniV2wqDz7wUBOfjBFzh92ubPtgSLveh83Ze+7H73d+Z36ToVUIJlhggwPd0Av9sA/gAMAowDgAWxJmFZndBHxsBWom8BdJx6ld1nQTaXj1MJCG3140ycC3L5vWFZ0M/OL0MuuXOOl4IGf9FJcTF01rxCANvzkGZOBvJ0HuNvDT883Wz3HScP+wPObgNZNUPPgsafjRZXnizEmwrskDftjfLAMNhw9Du2N+mXeujsC2yUOw4/ful0EZypch9m7m/cz3W0bGYAKUV/MzMJTfiiF8SMNZxU76SZEUXlIIPyECESSFLwLP9z0h/KSX8C8o2rRyvIW9BGx3pv+ZJwv9A7Yv/A0Jz0uITZvt3b2ZvqdyWbtQtDPZbC5r79prD/Tm7GJhIDOQL/TZpVymuLvXdkq5nN3zXHFvIvt8opjJZxPVFYkbKzqeLhX61vHV1OwuQ50pD0W4QVFSk6LEkXRHw8mzwNL8Hkoyj9rcVlRZ/Dw0UdSJ4qWdTDGjPEoqgUes3aT4qUrq3PYwZVTXxbgh15lvPMGII9dJM6+8BuytOfxEQvgLzy9F6/m6kKNW45gKSrTcZRXaREi673kdQUkixfFu9n8Ezut3eZX8J0vZm/Oh71x49B6t47fX40iKEjHXrKBH0knzUqLENVIszjbyYD7KvphD2UuFlHXS8MdRYAFP/tvbZI9IIT8bu6Vtg6dveVuhvu5eQqQWvu5hn+Lw8GPsvXmUTnoLf+O9dDfbTGv5GqIyGqSa19ebvBoP3lGLh/ImJ9ONS42KEYmTFC+oiP9CYx6qFfWypYLS5gjrb8xDEZN32nE8spS18GaKfq0oCLJXnCh+/A5UbQY/HK/Fh/58lL0CjanOGmp1V2KUNU3ArJFKQKSIUg36Ft5FHrszlDLK1GmIVO20jbeGs3pN4JSo0iRCG5wofjcK7ESD3hH3012sk1a7bfWkQuf0Ojw/KJHl/g+jjCagyvAGcj+k7Kh4qZMN1eMVnQl/EfC2hRaihuULDcv3OwJZXby+nD2IwO8LCcl3Wh2hcLV0ReKuVUdnNieJ4edHgB2DxjR8QA5bG7YE3NQoFaOsstywsSPgMTJscBA/2MmGGtQec8q9YWOt3OegMY69nR5hD4ceKpXTWWwCpEyyS2NloxLSKpejfpOqVDaqMTVNo+xtwNdHYVbklXwFLWknwlMgO6jcEjIrt1jqr8oFmFGyg2okHMvTE0oTxchA1QHxB7T/pcTkfGRfT7q1fFSOr7pu6wnHZJc/pVia3eWeUSL/yRhIV6NFHWtPLNo9neHv48fTWyoT6W75yXAUwj+RqS5XxTMrt/7jy0LAJkjDA7ANdkAv9MMe2KP8PQBlW70e).

**Points that do nothing for this spec:** **Blood Craze** (2) only counts toward the points the tree needs before **Dual Wield Specialization**; **Deflection** (2) only counts toward the points the tree needs before **Anger Management**; **Improved Rend** (3) is needed for **Deep Wounds**; **Improved Tactical Mastery** (3) is needed for **Anger Management**.

## Other builds of this spec

- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (17/34/0, 960 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013002-050530305022120231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/36/2, 914 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530305021100231-002-12)
- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 912 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500303022120231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/31/1, 899 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-552500300020120231-001-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Windfury Totem's buff changed in client 1.60.1.71037 and the raid simulator used here predates it: full-raid numbers of melee builds assume the old totem.*

