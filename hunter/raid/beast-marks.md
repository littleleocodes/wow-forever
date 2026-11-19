# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Beast Mastery's pet talents with Marksmanship's shot talents (Mortal Shots, Improved Arcane Shot, Careful Aim): a pet build short of 30 Beast Mastery points.* (a hybrid: Beast Mastery/Marksmanship).

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (28/21/2) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-00530503005-2-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Summon Hawk), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 921 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--12)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Serpent Sting**: keep it on the target
2. **Arcane Shot**
3. **Rapid Fire**; no global cooldown, so press it alongside the others
4. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Marks puts Beast Mastery's pet talents on a Marksmanship shot core and plays the same short list as Beast Mastery: keep **Serpent Sting** up, fire **Arcane Shot** and **Aimed Shot** each time they are ready, and let **Auto Shot** and the pet do the rest.

**Why it works**

- **Serpent Sting** first so it never drops, 20% stronger with **Improved Stings**. Recast it only as it runs out (a new sting replaces the old one), whatever your mana: the 2026-11-10 search dropped the old 30% mana guard.
- **Arcane Shot** every time it is ready: 3 points in **Improved Arcane Shot** bring its cooldown to 5.1 seconds, about 34 casts in a 3-minute fight. **Summon Hawk** would share that timer, and in a full raid the simulator measured **Arcane Shot** as the better use of it, so this build skips the hawk.
- **Rapid Fire** (40% faster attacks for 15 seconds, 5-minute cooldown) once a fight, at the pull. The full rotation presses it just before an **Auto Shot** with **Aimed Shot** about to come off cooldown.
- **Aimed Shot** is listed last but goes out almost every time it can: a 2-second cast, then its 6-second cooldown. The simulator measured it slightly better below the instants; **Multi-Shot** shares its cooldown and never comes up on one target.
- The pet half: **Unleashed Fury** (+15% pet damage), **Ferocity** (+10% pet crit on top of your own crit, which Forever pets inherit), **Frenzy** (3 points) and **Focused Fire** (+2% to you and the pet while it is out). There is no **Bestial Wrath** here, so there is nothing to time but **Rapid Fire**, trinkets and a potion.

**Caveats**

- Mana: the list assumes a full raid with Blessing of Wisdom and Mana Spring. With only your own buffs the simulator drops **Aimed Shot** (310 mana) and keeps **Arcane Shot** going above 10% mana, so **Aimed Shot** goes first when you run low.
- Keep the pet alive with **Mend Pet**: it is about a quarter of your damage and takes no stat buffs from players in Forever. A faster pet does more damage as modelled here (a 1.2-second cat over a 2.0-second pet; measured by players only at levels 20 and 30).
- Track the boss's creature type: **Improved Tracking** (2 points here) counts only against the tracked type.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot** and **Serpent Sting** are instant. The simulator starts **Aimed Shot** 2.5 seconds before the pull; in a real raid, wait for your tank.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98), **Trueshot Aura** rank 5 +100 (rank 4 +75; if your build has it) and **Aspect of the Hawk** rank 7 +120 (rank 6 +110). Cast the highest rank you have.

**When to change it**

- Two or more targets close together: **Multi-Shot** instead of **Aimed Shot** on their shared cooldown (up to 3 targets for weapon damage each, against 350 extra on one). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last few seconds, skip the **Serpent Sting** refresh: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out at once; the pet keeps attacking meanwhile.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 28 | Deadly Aspects 5, Endurance Training 3, Focused Fire 2, Bestial Swiftness 1, Unleashed Fury 5, Ferocity 5, Summon Hawk 1, Intimidation 1, Bestial Discipline 2, Frenzy 3 |
| Marksmanship | 21 | Lethal Attacks 5, Improved Stings 3, Careful Aim 5, Improved Arcane Shot 3, Mortal Shots 5 |
| Survival | 2 | Improved Tracking 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 1005 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 910 | this build |
| Pre-BiS | 983 | this build |
| Raid BiS | 1028 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 61.6; Pre-BiS 62.5; Raid BiS 63.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Ogre Forged Hauberk](https://www.wowhead.com/forever/item=18530) · *Tribute, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Leggings of Destruction](https://www.wowhead.com/forever/item=18524) · *King Gordok, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Tribute, Dire Maul* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Beastslayer's Trident](https://www.wowhead.com/forever/item=279910) · *quest: Mapping the Way Forward*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIHGcU3vfP7Mzb13bZjtodh7ZMtyDrwiz/zHZELWVXTz0V6akn6+iuzkh1l92l6M2ChSK2Ls1JIxgwIUbiXXLIQSIxJw2BJCQbYowJOXjwmhxCmHEXQsxRyXcY3nzfDN/3/v/x6GuEGKigQxKGwIUSzAD8A3AJYA1A+TxQma92g/ZMRowJ2p8kYd1VDz8jAW8PkoA3XZJw2VXvSiTjQQ3U51GS8OKY+iRKMm4sgPo0SiI+3ACSsV4D/1cJFyZO6Fs1IBFnj2Ik4L8TJOK1mv/dy7kv1aMohUjGCwugPm5JdMR2vOThCswBm/WWILLqXHfqfStXYB3kee/qMvzn7cOs149BaMjBDfaNnbE456bNbZObVsbg3M5wm2c4tw1rh4l7DA9YPUythJpEIu5tQwJJItEweYXaGuzaKiQiJFPYsNJ2RfkblEGn9MfvxVJVt7jVZZjcMLt69RHXmRwr5PViWXfy+UJeH57Wq25BLxerTtUrTuqVglMecfVkpVDQhyeMsuPljaZonIjp8UpxslP7ntpTcRQUHPdT7W6DFvjztGVXtAaliBrrDSne6TC850zDyFqYBNwtKtMf6fuHM7WK0xePJCIRt2YGFBYTg179+iftR7IUTq0pBQUlvMUYhjWZwiTwtElq6isUlMg6NG6rqdhB8hdxZfyD5LzHsLrPNPnJpDx4/cspL5Mb3DoHr7VVUHTtW2pLtWC4eSTB8PK0XQk6v9eqCq/YDhwz6y8hFCCZm4N2ilMbLv0PsTfzoEqdoQDH2SFMvGURvw7NjObalxZ93Ml+NxrgftbaZ6qoZ1ObLPRJUM01q3NFx8a5+fQEz18v5/oaRG7IX7eLELyE9rMpATfj/e9tZQ7dkIOfYQB+AxdKMAVT7N0A9xQrOg==); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IHHcU3veb2Z23r+06jNodh7ZMtyDrwiy/me2IWsqunnoq0lNPraO7uiPVXXb3oDcLFopobT1VE2LASEQiBJKABHIxCAYCbhCSkBgiiYEEPHjMHwhhxl0IMUcl32F4830zfN/7/R6PvkKQQQUd4tAHeSjCBMDfAOcBVgCUz32VeWoHaPsSoixo4yThjWsN6v5nJOCVMRJx57ZMEp6ryuqdEEl482qD+jRCITwzpD6KkIRrs6A+jpCI99eAJLw8B97PIZwdOaL/r8ok4syBTALOjJCIL/71vnuz3KAeRChAEr78D9SHjbFWecuN7y/CFLBJdwHCS84lZ7d7cRlWQZp2L56Ff9w9mHR70M8NGbjOvrZTFufctLltctNKGZzbKW7zFOe2YW0xscrwCdsNUhOhFiIRq5sQQwqRaJi8TM01dmUJYmGSKGhYSbus/AXKb07xj98LxYpucavdMLlhtnfpA3lndCiX1Qsl3clmc1m9f1yv5HN6qVBxKm5hVC/nnNJAXo+Xczm9f8QoOW7WqIvGkZgcLhdG27TvqCURRUHBYS/V9iZovj9PWnZZq1GKqLGugOIeD8M7TzSMpAVJwO2CMv6Rvr8/UasoffEgRCTixkSvwmTR79Wrf9R+IEvh1JRQUFCCG4xhUJMoSAJPmqQmvkRBCa9C7bbqiu0nfxZVhj9IzjsNq+NEkx9Nyr1XPx/zMrnBrVPwWlkCRde+oeZEIwbrR+IPL0/aZb/znSZVeM624JBZfwoBH/HMFLRQlJpxYQ7k19OghtoCPg7TfRh7y8JeHZgYzLQszHu4lf520MfdtLXHVFFPJ9ZZ4JOgkqlXp4rWtVPz6fSfv1zIdNeITJ+3cefBfwnspRMCrkd73lvMHDogAz9BL/wKeSjCGIyxdwMA474tcw==); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIG2kUzvtnMvPydjeGUTfjsLvMZkFiYMI/kx1RlyXR054W2dOedh1NNCOrCUkOenNBoYitxV6qFSxYqZUKPbQghV4sgoWCFqEtraXSptBDD17bQikzJlBqj0q/w/Dm+2b4vvf/j0c/IERABR3i0Ad5KMIEwBmAywCrAMq3vso8tQO0qowYEbRxkvHOrQa1+g2JWJ0FEnHvfoQkXMyrDySS8e7NBvVlmCS8NKQ+C5OM67OgPg+TiI/XgWS8MQfezxLOjhzRF3cjJOLUBSABz46QiNfOe9+9X2lQ34QpQDLOz4H6tDHWGtl249UlmAY26S5AaNm57ux3L63AGsgz7tVFOOcewKTbg35uyMBt9qOdsjjnps1tk5tWyuDcTnGbpzi3DWubibsMX7D9IDURahKJuLsFMSSJRMPkZWqusavLEAuRTEHDStplZQqUf5zif/8WihXd4la7YXLDbO/SB/LO6FAuqxdKupPN5rJ6/7heyef0UqHiVNzCqF7OOaWBvB4v53J6/4hRctysUReNIzE5XC6Mtmm/UEsiioKCw16qnS3QfH+etOyyVqMUUWNdAcU9HoZ3nmgYWQuSgDsFZfwLff96olZR+u6JRCTi5kSvwiKi36tX/679RpbCqSmhoKAENxnDoCZTkASeNElNfI+CElqD2m3VFdtP/iqqDH+WnHcaVseJJj+alEdv/zzmZXKDW6fgtboMiq79RM2JRgzWj8QfXp60y37ne02q8JptwyGz/hcCPuKZaWihKDXjwhxE3s2AKrUFfBym+zD2gYW8OjAxmGlZmPdwL/3zoI+HaeuAqaKeTmywwFdBJVOvThWt66fm0+k//7qS6a4RmT5v486D/xI4SCcE3Ij2fLKYOXRABv6AXvgb8lCEMRhjHwcAckssNA==).

**Points that do nothing for this spec:** **Intimidation** (1) only counts toward the points the tree needs before **Frenzy**.

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 937 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

