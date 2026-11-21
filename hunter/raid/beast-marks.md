# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Beast Mastery's pet talents with Marksmanship's shot talents (Mortal Shots, Improved Arcane Shot, Careful Aim): a pet build short of 30 Beast Mastery points.* (a hybrid: Beast Mastery/Marksmanship).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (27/22/2) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510122-0053050200502-2-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Summon Hawk), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 905 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--12)

## How to play

**Before the pull:** **Hunter's Mark**, **Aspect of the Hawk**.

**Keep up all fight:** **Aspect of the Hawk**.

**Then press the first one that is ready**, top to bottom:

1. **Hunter's Mark** and **Serpent Sting**: keep them on the target
2. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Summon Hawk**: part of the rotation (about 20 times a fight)
- **Arcane Shot**: part of the rotation (about 10 times a fight)
- **Rapid Fire**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast-Marks puts Beast Mastery's pet talents on a Marksmanship shot core and plays the Beast Mastery list exactly, without **Bestial Wrath**: keep **Hunter's Mark** and **Serpent Sting** on the boss, spend the cooldown **Summon Hawk** shares with **Arcane Shot** as hawk, hawk, **Arcane Shot**, and fire **Aimed Shot** whenever it is ready. This is the official simulator's own rotation with hawks (its turret_hawk file; since 2026-11-20, when it beat ours by 2.1% on this build). In a 3-minute raid fight: **Aimed Shot** 23 casts, **Summon Hawk** 20, **Serpent Sting** 12, **Arcane Shot** 10, **Rapid Fire** 1; **Auto Shot** 32% of the damage, the cat's and the hawks' swings 28% (one line in the record), **Aimed Shot** 15%, **Serpent Sting** 12%, the cat's Claw 5%, **Arcane Shot** 5%, the hawks' dives 3%. In the same raid it does 942 DPS, against 946 for the Beast Mastery page's build.

**Why it works**

- **Hunter's Mark** and **Serpent Sting** come first, each cast only when it is missing from the boss: the mark lasts 2 minutes (2 casts a fight), the sting 15 seconds (12 casts, never refreshed early; 20% stronger with **Improved Stings**). The mark and **Aspect of the Hawk** go up before the pull; **Deadly Aspects** needs the aspect: each **Auto Shot** then has a 10% chance to speed your shots by 30% for 12 seconds.
- **Summon Hawk** and **Arcane Shot** share one cooldown, spent in a fixed order: hawk, hawk, **Arcane Shot**, then again (20 hawks and 10 Arcane Shots a fight, a use about every 6 seconds). A hawk dives for 108 plus 5% of your ranged attack power, then attacks for 18 seconds; only 2 can be out, and one every 9 seconds keeps both out nearly all fight.
- **Aimed Shot** whenever it is ready: a 2-second cast on a 6-second cooldown, 23 casts a fight, 10% stronger with 2 points in **Barrage**. **Multi-Shot** shares that cooldown and is switched off for a single target ("Use Multi-Shot").
- From 5 seconds in, every other cooldown as it comes ready: **Rapid Fire** (40% faster attacks for 15 seconds) once, your on-use trinket (the page's sets carry Blackhand's Breadth) and a Major Mana Potion. At 27 Beast Mastery points there is no **Bestial Wrath** to time, and **Intimidation** has no line: it only counts toward the points **Frenzy** needs.
- The pet half: **Unleashed Fury** (+15% damage to the cat and the hawks), **Ferocity** (+10% crit to both), **Frenzy** (2 points: a 40% chance of 30% faster attacks for 8 seconds after each pet crit) and **Focused Fire** (+2% to you both while the cat is out). The cat takes a tenth of your attack power and your crit chance, and attacks and uses Claw on its own.

**Caveats**

- Full raid: every raid buff and debuff, phase-1 gear, 3-minute fights. The list has no mana guard: on the simulator's training dummy (your own buffs only), the raid's mana buffs alone (Mana Spring Totem, Mana Tide Totem, Greater Blessing of Wisdom, Judgement of Wisdom) add 18% to this build's damage.
- Keep the cat alive with **Mend Pet**: Forever pets take no stat buffs from players. In the simulator a pet keeps the attack power it took from you when called until it is dismissed (its authors' reading of combat logs), so call it after your buffs are up.
- The pet and the hawks are the simulator's models, unmeasured at 60: since 2026-11-19 a faster pet's swing hits for less, so its damage a second stays the same (fitted to one level-30 combat log), and the hawks' attacks after the dive, which the game files do not describe, are fitted to combat logs.
- Track the boss's creature type: **Improved Tracking** (2 points here) adds 2% only against the tracked type; the simulator's boss is an Elemental.
- Ranks: the list casts the trainer's top ranks, **Serpent Sting** rank 8 and **Aspect of the Hawk** rank 6 (ranks 9 and 7 are class books, not in Forever on the evidence there is; checked again when the raids open on 2026-12-09). For **Hunter's Mark** the simulator uses rank 3's +98 ranged attack power, as the client data it reads lists rank 4 lower; the beta tooltip (build 70753) reads rank 4 +143. Cast whichever rank your tooltip shows higher.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot**, **Serpent Sting** and **Summon Hawk** are instant. Move right after an **Auto Shot** goes off, as the simulator's walk to its spot does ("Windup close", "Just shot").
- The page's With a pet setup (22/29/0, also with **Summon Hawk**) runs another entry's list: the official turret file with our search's edits of 2026-11-20, which drop the turret file's hawk switch, add a **Summon Hawk** line above 60% mana and put a Major Mana Potion at the end. It plays like this page's list (20 hawks, 9 Arcane Shots, 23 Aimed Shots a fight) with a second Major Mana Potion: 905 DPS there, 905.6 on the official hawk file.

**When to change it**

- Two or more targets close together: **Multi-Shot** in place of **Aimed Shot** (it hits 3 targets). For a pack, **Volley**: a 6-second channel with no cooldown.
- In the last few seconds, skip the **Serpent Sting** recast: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out. **Summon Hawk** has no minimum range, and the cat keeps attacking meanwhile.
- Short on mana: let **Aimed Shot** go first. In this build's full-raid numbers it does about 1,160 damage for 310 mana, **Arcane Shot** 830 for 190, **Serpent Sting** 1,640 for 230.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 27 | Deadly Aspects 5, Endurance Training 3 (tier point: needed to reach Bestial Swiftness), Focused Fire 2, Bestial Swiftness 1 (needed for Intimidation), Unleashed Fury 5, Ferocity 5, Summon Hawk 1, Intimidation 1 (tier point: needed to reach Frenzy), Bestial Discipline 2, Frenzy 2 |
| Marksmanship | 22 | Lethal Attacks 5, Improved Stings 3, Careful Aim 5, Improved Arcane Shot 2, Mortal Shots 5, Barrage 2 |
| Survival | 2 | Improved Tracking 2 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a short check on 2026-11-20 (every one-move and chain-move neighbour raced in a full raid, two rounds; the best kept move is +1.0%, under the 0.5% bar). A full search, talents and rotation in turns until stable, follows in the optimality pass.

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 942 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 868 | its own set |
| Pre-BiS | 920 | its own set |
| Raid BiS | 969 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 61.6; Pre-BiS 62.5; Raid BiS 63.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Shadowcraft Spaulders](https://www.wowhead.com/forever/item=16708) · *Cannon Master Willey, Stratholme* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Ogre Forged Hauberk](https://www.wowhead.com/forever/item=18530) · *Tribute, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Legguards of the Chromatic Defier](https://www.wowhead.com/forever/item=12903) · *quest: Legplates of the Chromatic Defier*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Tribute, Dire Maul* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Beastslayer's Trident](https://www.wowhead.com/forever/item=279910) · *quest: Mapping the Way Forward*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVU9sG8UX9luv1+OX/NzNxG230z+/qVGLsZJos8HQRoDtSkCEBCpYqAhx6BKvvavYO5F33aS3gnJAUSERPTVEKlJBRBG5lEvVI+ohcAGEBEgUEYUKKOqhCnDAB4R2nT+OBQcOFe/gfe97733fm9kZLx4ioIIGHDJwFmyYhAsAbwC8C7AEQHvDrBRkTwBb6SFEjbJzqJBbtna7B6Pko2mUyc3XARWyaGtfKBgn6/Og/ZBEhbxT1b5LYpyszIH2fRJl8s1KUPdTOWhVyFy9jd6cB5TJzF0Vo+TNOsrkzjxgnPw426fdTWIE4+TSHGjf9qePq6tO5vYVmAVpxlmAxFXzQ/NW8cr7sAzxi84Hi/CWswYzzikSDg0FuCEdzo0Yuq4P5/TcsD5sjAzqem5Ez+kjup4bNFYl+XOJrEtLCdyLCRbHWEYmv4s0QQXlQcPwtmGFbGzDuoccU8vQh3taSi/i6WatxhumW7U2K4ZPenQfS6GaTRKFSqMRpqCMUs4bjdDD7CCq6ST2XoMERslvgkpqbFuZMqbh/9I9mDACiJBfHbbl0KfZk/gYHcUhOoCpltKHe170LF5q1uvC5WPm1EQHWmyMm67FS7bwkaxLMYyOjRWz7Qd9hb38b0lopt2KjKCSkcnXfzy3y09sjvmZoAX2BBpU/wd2Lb3v7xU6yPLs8S6Gjrouhg7unRGOsv9jf0tRMRmUFJ26Vd7RUMjSVaBH2KGOkmebNd8ZDEtiGCVfpqig+ZJvNnwuKty3LV5xqrY/yquWz33B6+e5Nyl8PuX4tmj6vCY8x61y0+XFpi9CrSE2gEeyh4hE458qMkqqzNrHpWQL4Yft65DA+BmzNsEdV4tmF6XtiN4BegnCYEdtgNeEmAh1qqbjcuuc1TjPG5Y57jvC5b5Tt4Z4yReTfMp2albQtj3Ngx6fctxyc5I7Hh+vCc/iosEbTdd13OoAN91ymyhYnGWO29yzhc9ftSqiYfEpsxbKCneIPY8n049ijo4gbpCtDcdj7AHsaylJ7D3TVgklMNlSejDxTNPzQ75l6MfuPVCBHqOs5JtuOZCoiMauuYdYPB3D6A05YrDut0nD2+Y3mpZxsPs10gTGMVYxa16Q7D5Duzq7j1FHMtU5KQ0v8bBhpDqvfBs1csZTu9dOH2EPh38AMo19LEkkxoJFIM8eIcoW0n9NUolEY7/Egyi2ETyMwx0bRgOCKG1nQoKfpVW4J5Vfi0ZCyxRm4QDux71k4W1QWxdBUx6KhHYvf5ak/5QSgR+5UCkcWLgc2Cf5o5XQvsoba5Im83z2uhT5T8wvbHn31Y6v3Dedk+HvC+8ViptA4Wzw6bwMYRBZy2ej5Pr+Ux1fWB1OQAHG4DS8BDZMwjRMS38NAI/kjJs=); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVV9oHNUX3jM7O3P3JL/N9GbbTm///G5XWtclCZOJq21Qd7egBkGpLlIRHzIms7tDdueGnVmTvFXog5TWan2xsVihFkMwUKpCKfiiL1EEIwUVVAyxD1b6UKKCriAys/mzWfTBh+J52DnnO+d837l37t3BPQQ00IFDGkahApNwHOAlgLcA5gBod5iVguwhYJe7CNGibAZV8uEHPfqNLoyS96ZRJtc/01Alby5p+hcKquTj93v0HxKokDfK+ncJVMnCGdC/T6BMvl4AVMnlsxA0K+RMrQW/vqShTE7f0jBKTtdQJjdfCer+uNSj30pgBFXy26ugf9ObOqgtOukbF+AkSCecWYhftN61vi1cuATzoJ5y3jkPLzvLcMI5QsK5IQ/XpL3ZIdMwjMGskR00Bs2hfsPIDhlZY8gwsv3moiQvSWRFmovjdowzFWNpmfwqUgQVlPtN09uAFbK6ARseckzOwzbsaSrdiEcb1SqvW27ZXqsYPOzRHSyJWiZBFCoNR5iCMkpZbzhC97LdqKUS2H0F4hglvwgqabENZcqYjv9LdWHcDCBCfnbYukMfZQ/jA3QYB2gfJpvKNux52rN5sVGrCZePWFMTbWihPma5Ni9WhI9kRYphdGSkkGk96HPs2X9LQtOtVmQElbRMvvr9iS1+fG3MzwXNs4fQpMY/sOupHX+v0EaWYw92MLTVdTC0cW+OsJ/9H3ubioaJoKTg1OzxTQ2FzF0Euo/taSt5vFH1nf6wJIZRcj1JBc0Vfavuc1HifsXmJadc8Yd52fa5L3hthnuTwudTjl8RDZ9Xhee4ZW65vNDwRag1wPpwX2YPkaj6qSKjpMmsdVyKFSH8sH0F4qges6oT3HH1aOa8tBHRm0BfgzDYVOvjVSEmQp2y5bjcfsGuz/C6bY35jnC579TsAV70xSSfqjhVO2jbmOZuj0857nhjkjseH6sKz+aizusN13Xcch+33PEWUbA42xqrcK8ifP68XRJ1m09Z1VBWuAPsSTycuh+zdAhxlaxvOB5gd+G2ppLA7mMtlVACE02lC+OPNTw/5JuHXuzcAw3oAcqKvuWOBxIlUd8y9wBTUzGMXpMjJut8mzS8bX69YZu7O18jjaOKsZJV9YJk5xna0tl5jNqSyfZJaXiJB00z2X7lW6iZNR/ZunZ6H7s3/AOQaewjSSIxFiwCeWYfUdaR3iuSRiQa+0kNothq8DD3tm0YDQiitJUJCX6UFuG2NP5iNBJaOn8SduFO3E5mz4LWPAW6ck8ktNu5UZL6U4oHfuR4Kb9r9lxgn+T2l0L7MmcuS7rMc5mrUuQ/MT+/7t1RO7hwx3QOh79PvZ0vrAH50eDreQ7CILKcy0TJ1Z1H2j6yBhyCPIzAUXgGKjAJ0zAt/TUAoLGOjw==); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVV9oHNUX3jM7O3P3JL/N9GbbTm///G5XWtclCZOJq21Qd7egBkGpLlIRHzoms7tDdueGnVnTvFWoIKUaSV9MDFSoxRgMlKJQCr7oSxTBSkEFFUPMg4oPJeqDK4jMbP5sFn3woXgeds75zjnfd+6de3fwAAENdOCQhtNQgQk4C/AywJsACwC0O8xKQfYYsKtdhGhRNoUq+eD9Hn2tC2WyNg0ok1ufaqiQ+Yr+uYIq+ei9Hv37BCrkjbL+bQJVsjQN+ncJlMlXS4AquToDQbNCpmst+PWbGsrkpYuAUfJKDWXyzmtB3R9XevSfExhBlczOgP51b+qotuyk1y7BeZDOOXMQv2y9a31TuHQFFkG94Lw9D686K3DOOUHCuSEPN6SD2SHTMIzBrJEdNAbNoX7DyA4ZWWPIMLL95rIk35TIqrQQx90YZyrG0jL5TaQIKij3m6a3BStkfQs2POSYXIRd2NNUuhFPNqpVXrfcsr1RMXjco3tYErVMgihUGo4wBWWUst5whB5k+1FLJbD7GsQxSn4VVNJiW8qUMR3/l+rCuBlAhPzisE2HPsoexgfoMA7QPkw2lV3Y87Rn82KjVhMuH7Emx9vQQn3Ucm1erAgfyaoUw+jISCHTetDn2LP/loSmW63ICCppmXz5+xM7/PjGmJ8JmmcPoUmNf2DXU3v+XqGNLMce7GBoq+tgaOPeHuEw+z/2NhUNE0FJwanZY9saClm4DPQQO9BW8nij6jv9YUkMo+RWkgqaK/pW3eeixP2KzUtOueIP87Ltc1/w2hT3JoTPJx2/Iho+rwrPccvccnmh4YtQa4D14aHMASJR9RNFRkmTWeu4FCtC+GH7KsRRPWVVx7nj6tHMvLQV0R+BXoQw2Fbr41UhxkOdsuW43H7Brk/xum2N+o5wue/U7AFe9MUEn6w4VTto25rmbo9POu5YY4I7Hh+tCs/mos7rDdd13HIft9yxFlGwONsarXCvInz+vF0SdZtPWtVQVrgD7Ek8nrofs3QIcZ1sbjgeYXfhrqaSwO5TLZVQAhNNpQvjjzU8P+RbhF7s3AMN6BHKir7ljgUSJVHfMfcAU1MxjN6QIybrfJs0vG1+vWGb+ztfI42jirGSVfWCZOcZ2tHZeYzaksn2SWl4iQdNM9l+5VuomTUf2bl2eh+7N/wDkGnsQ0kiMRYsAnnmEFE2kd5rkkYkGvtJDaLYevAwD7ZtGA0IorSVCQl+kJbhtjT2YjQSWjp/HvbhXtxN5mZAa14AXbknEtrt3GmS+lOKB37kbCm/b242sI9zh0uhfZEzVyRd5rnMdSnyn5if3/TuqB1dumM6x8Pfp97KFzaA/Ong6zkLYRBZyWWi5PreE20fWQOOQR5G4CQ8AxWYgDNwRvprAPHdjVA=).

**Points that do nothing for this spec:** **Endurance Training** (3) only counts toward the points the tree needs before **Bestial Swiftness**; **Intimidation** (1) only counts toward the points the tree needs before **Frenzy**; **Bestial Swiftness** (1) is needed for **Intimidation**.

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 905 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

