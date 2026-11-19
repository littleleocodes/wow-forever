# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md)** (17/32/2) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (20/31/0, 922 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

## How to play

**Setup, before the pull:** **Berserker Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst** until the last 30 seconds of the fight
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Reckless Swings**
4. **Whirlwind**
5. **Execute** when the target is below 20% health
6. **Hamstring** when **Bloodthirst** is more than 1.125 seconds from ready and **Whirlwind** is more than 2 seconds from ready
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
| Arms | 17 | Improved Heroic Strike 3, Deflection 2, Improved Rend 3, Improved Tactical Mastery 3, Anger Management 1, Deep Wounds 3, Impale 2 |
| Fury | 32 | Cruelty 5, Unbridled Wrath 5, Furious Precision 3, Dual Wield Specialization 5, Reckless Swings 1, Improved Execute 2, Improved Berserker Rage 2, Death Wish 1, Improved Whirlwind 2, Flurry 3, Bloodthirst 1, Blood Craze 2 |
| Protection | 2 | Improved Bloodrage 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 990 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 835 | [17/32/2](https://talentsforever.com/warrior/60/30303213002-250530005122100231-2-12) |
| Pre-BiS | 961 | [17/32/2](https://talentsforever.com/warrior/60/30303213002-250530005122100231-2-12) |
| Raid BiS | 991 | [17/32/2](https://talentsforever.com/warrior/60/32303013002-250530005122100231-2-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.2; Pre-BiS 62.4; Raid BiS 63.1; each item opens its Wowhead page, with where it drops and its enchant):

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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11sFFUU3jMzO3v2FNbhFmR6C2ZsCC6DW+/M7hSKxi5EjT8x4k8CUaNd2YVdo91mpwaIPtCGGIMG0BojC6YVJTbVPtD4QxrTB40ENRh5sIkGI6kmmsgDD/qiRswddruy7YNp2vU+7J65596533e+b85kaBWCASZYEIduyEMv7AN4AWAYYASALQmyisxuBP77CtQM4LtJx/N5c7qJNHx+DEjF8cdIx2N585xOOn71iPljjHQ8usv8PkYRPP4KmEMR0vDLY0A6ThTkTh0PPW3+ECMN9180SMOTB+R93nmUNPzga4N0/OYh86K8y+Sz8l/DwUPQFjdOF+I/DcHWqYOw/bfuA6AMFMoQfSvzXua7zUMnYBSUlwqXYKCwBQPckIYJxUqKpEi6TlIIN+F6wksKITzHdR0h3KSTcM8o2rTyZzPbD2xHpvepx4u9fZYr3I6E4yTExk3WjnymZ1cuaxVLViabzWWtJ/ZaffmcVSr2ZfoKxR7Lz2VKO/JW3M/lrJ3PlPYmsrsTpUwhm6iuSFxZ0f6kX+xZx1fTMvsa1Jlyd4hHKExqUvgcSY9rODUBLM1vpSRzqNVuQZXFPoEmCsfDePZhphhhHiaVwCHWZlBsvJKa3BakItV1UR6R64zXHmTEkeukGedeBnZ0Fj+REO7C80vRer4u4KjVOKY8n5bbrEKbCEl3Hafd8yVSHOlm1yFwXr/LqeQ/Wspenwt958Kjd2gdv6EeR1L4xGyjgh5JJ81JCZ9rpJicbeDeXJRdMYuykwoo66Th+WFgq3lr/aYO4UvB8NdJYB5P/lcw0kJS549PzGcbHv95Xqf1vz/vbcV6NZ2ESC28moH7cXDwfvbuHP5JOgt/4m10C9tEa/kaojJGSDUurzd4Ne6/sRYPFAxOhh2T0pZCEicpjlex1HONeVRX1MuW8vxNIdbbmEctKs+0Ynh4KWvmyyj8haIgSK/Ew/jhm1BtXnhypBYf/Os+9iI0pjprqMVeiWHWNAoz7VkCIkX4NeibeRc57KZAyjBTpyFUbdKtvCWY1WsCp0SVJhFaEA/jt8PAxhr05rmDbmadtNpurScV9GOn3XE9n0z7WgwzGoUqwyvI3YByXMWznWygHq/oTLiLgLc1aCFqUL6gz7luuyeri5eXs7sQ+O0BIfmmrCMUrJa9lrht1tGZyUli+OlhYG9AYwzfQXG2NrAEXGWUSqOssuzY0O5V/IF4+jNgAw3yx6x6d2yo1XsSGtOyt9G97J6giUrpdBYdBamTtGm0HKmEtMrmqF8lK5Uj1ZiaplGaG/DVYZhReSVfQUvaiHAcpIXKzQGzcrOp/qKcgUuK26+GgrE8Pao0UZQiqMZB/AFtfytROR/atzPdUj4ix+dd1+8MxlSXe0ExNavLPqWE/pfRl65GizrWji3aOZ3B7wNvpzdXJtLd8hPkCAQXoQtdtoqnVm7515eKgI2QhjthK2yHPPTCHtij/DMAbVPFIw==); Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3v2pN1Oblo7uWllDKVup268M7uTNlXMtqj4g1j1oUUEs+1uzYpkw07EFBSaoFD8qZWItCua+FMM0RasVWuRPFQtVVpIEQL+YYiCgn2I4JMVK3e6m7WbPEhI1vsQTu45d+/3ne+bMwytQTDABAvi0AXd0Av7APYDjACMArBlQVaR2c3AL61CzQD+FOk4tcucbiAVP+gnDb8+Z1AEX58wzAs6RfDzEyvMn2Kk4/6c+UNMbpwzzOEIaTg0IQt/PwbycAQ/Od1o/hgjDV+4aJCGhyYMUvGdh0jDD4PC755pNC/KH5g5BjLQcOhFaI0bZ/Lxn4dh++QB2PlH17OgDOZLEH0r817m263DR2AMlOfzMzCY34YBekjDKcVKiqRIuk5SCDfhesJLCiE8x3UdIdykk3DPKtq0cqmJPQ1sd6b3sYcLvX2WK9z2hOMkxOYt1u7uTM8juaxVKFqZbDaXtXbttfq6c1ax0Jfpyxd6LD+XKe7utuJ+Lmfteby4N5F9IlHM5LOJSkXiSkXbo36hZwNfS432CtSZcleIRyhMalL4HEmPazh5Clia30JJ5lCL3Ywqi52GBgrHw3j+QaYYYR4mlcAh1mpQ7Hg5Nb4jSEUqdVEekXXGKw8w4sh10owLLwF7dQ4/kRDu4vNL0Ua+IeCoVTmmPJ9W2qxMmwhJdx2nzfMlUhztYtcicF57yinnP17ODs2HvmPx0Tu0gV9fiyMpfGK2UUaPpJPmpITPNVJMzjZxbz7KrphD2UkFlHXS8PsRYGt5S+2hduFLwfC3cWAeT/5XMNJCUudPjyzkGL75y4JuGzix4GOFWjWdhEgtvpqB+3Fo6D727jz+STqLf+OtdDPbQuv5OqISRkg1Lm80eCUeuKEaD+YNToYdk9IWQxInKY5XttST9XlUV9XKlvL8LSHWW59HLSrvtGJ4cDlr4o0U/kpREKRX4mH86A2oDC98f7QaH/jrXvYc1Kc766jZXo1h1jAGs+NZAiJF+FXoW3knOezGQMowU6chVBnSLbw52NWrAqdEhSYRWhAP4zcjwI7W6c1zO93EOmit3VJLKpjHTpvjej6Z9jUYZjQGFYZXkLsB5biK5zvYYC1e0ZFwlwBvSzBC1KB9wZxz3TZPdhcvr2R3IvDbAkLyTVlDKKiWs5a4bdbQmc1JYvjZQWCvQX0M305xtj6wBFxllPKgrLBs39Tmlf2BeOYLYIN18secfrdvqvZ7HOozsnfQPezuYIhK6XQWHQOpk7RptBQph7TG5qhfJSuVIpWYGqZRmhvw5RGYVXk1X0XLWonwOEgLlZoCZqUmU/1VOQszijughoK1Mj2mNFCUIqjGQfwJrX8rUbkf2rcn3Vw6LNeXndftCdZkpzulmJrVaZ9UQv/L6ktXoiVd648u2T0dwd/7305vLW+ku+SHyGEI/glNddoqnly97V/fKwI2QxrugO2wE7qhF/qhX/lnAOzVyQI=); Raid BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11sFNUX3zMzO3P2FJbpLfyZ3sI/Y0NwGdx6Z3anUDR2IWr8iBH1AeKLXdjFrlG22akREmOgkYSofJgaI+sH9YOkqUIiQUVi+oBKUCGBmDTxKzaVRBN5qIlPSsTcYbcr2z6Ypl3vw+bsPffj9zu/35zJ0DIEEyywIQE90At9sAtgL8AQwDAAWxBmFZldC/zKEtRM4M+QjuNbrIkm0vDSASANvz5nkoFvXDCtizoZ+NmJRdZPcdJxb976IS4nzpnWYYM0/Oo1IAN/OwZyt4Efn262foyThnsG5TH7Lpuk4r4nSMMPLsgTJ4+BdVke8N2eZhloOHgA2hPmmULi0mHYOLYfNv/e8xwoA4UyxN7Ovpf9dv3hIzACyguFSRgobMAQPmTglGKnvJRICTclhJf0fOGnhBC+63muEF7KTXpnFW1C+bOFPQtsa7bv8UeKff22J7zOpOsmxdp19tbe7PZH8zm7WLKzuVw+Z2/Zaff35u1SsT/bXyhut4N8trS1104E+by97cnSzmTuqWQpW8glqyuS11Z0PBYUt6/iy6nZWYQ6U+6JcIOipKZEwJH0hIZjp4Bl+G2UYi61Oa2osvhpaKJoIornH2aKGeVRUglcYu0mxY9XUqObwpRRXRfjhlxnvvwQI45cJ828+CKwV6fxE0nhzT2/NK3mq0KOWo1j2g9oscMqtImQdM91O/xAIsXhHvZ/BM7rd7mV/EcL2Sszoe+ae/QureI31uNIiYCYY1bQI+mkuWkRcI0Ui7M13J+JsiemUXbTIWWdNPx+CNhy3la/qVMEUjD8dRSYz1P/Foy0kNT5kyOz2YZv/Tyr23afmPW2Yr2ablKk517N0P04OPgAe3cG/6Tcub/xdrqVraOVfAVRGQ1SzaurTV6Nd99UiwcKJifTiUtpSxGJkxTXr1jq6cY8qkvqZUv7wboI62vMoxaTd9pxPLiQtfBmin6pKAjSK4kofvgmVJsXvj9ci/dfuZ89D42pzgpqdZZilDWNwFR7loBIEUEN+nreTS67OZQyytQJiFSbdBtvDWf1msBpUaVJhDYkovjNELCjDXrz3Em3sC5a7rTVkwr7sdvhen5AlvM/jDIagSrDa8i9kHJCxfNdbKAer+hKevOAty1sIWpYvrDPeV6HL6uLVxezuxH4HSEh+aasIxSulr2WuGPV0ZnKSWL46UFgr0NjDN9JCbYytARcZ5RKo6yy7FzT4Vf8gXjmc2ADDfLHtHp3rqnVexQa07I30X3s3rCJSul0FhsBqZO0aaxsVEJa5nDUr5OVykY1pqYJlOYGfGkIplReypfQgnYiPA7SQuWWkFm5xVJ/Uc7CpOLtViPhWJwZUZooRgaqCRB/QPtfSkzOR3Zty7SWD8nxRfcN28Ix1u2NK5Zmdzsnlch/Mvoz1Whex8qj83ZPV/j74DuZ9ZWJTI/8EjkE4Z/IeLej4smlG/7xwSJgLWTgLtgIm6EX+mAH7FD+HgAuZcjb).

**Points that do nothing for this spec:** **Improved Tactical Mastery** (3) only counts toward the points the tree needs before **Anger Management** and **Impale**.

## Other builds of this spec

- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 916 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530055021100231--12)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 962 DPS in a full raid; fails the signature-spell check: core share 79.8% under 80.0% (melee, Bloodthirst, Whirlwind, Heroic Strike, Execute, Slam)) — [open the talent tree](https://talentsforever.com/warrior/60/05303013102-050530305022110231--12)
- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 913 DPS in a full raid; fails the signature-spell check: core share 71% under 80% (melee, Bloodthirst, Whirlwind, Heroic Strike, Execute, Slam)) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500305022100231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 900 DPS in a full raid; fails the signature-spell check: core share 71% under 80% (melee, Bloodthirst, Whirlwind, Heroic Strike, Execute, Slam)) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-553500050020100231--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

