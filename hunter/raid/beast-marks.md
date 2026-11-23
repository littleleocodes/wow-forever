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

**How this pick was checked:** a short check on 2026-11-20 (every one-move and chain-move neighbour raced in a full raid, two rounds; it found +0.99% in 2 moves, above the 0.5% bar: a full search follows). The full search, talents and rotation in turns until stable, runs in the optimality pass.

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

*Molten Core is not in Forever: no raid is open yet, and the raids of 2026-12-09 are The Barrow Deeps, Hyjal Summit and Onyxia's Lair. These sets still count raid gear (Raid BiS: Quick Strike Ring, Rhok'delar, Longbow of the Ancient Keepers (Molten Core); Raid BiS: Onyxia Tooth Pendant (Onyxia's Lair)). The gear lists are being made again.*

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVU9sG8UX9luv1+OX/NzNxG23039T/9RirCTabDG0EWC7EhAhgQoWKkIcusRr7yr2TuRdN+mtoBxQVEhETw2RilQQUUSEVC5Vj6iHwAUQEiBRRBQqoKiHKsABHxDadf44Fhw4VLzD7rzvvfd9b2ZndvAAARU04JCBs2DDBFwAeB3gHYBFANobRqUgegLYhz2EqFF2DhVyy9Zu92CUfDSFMrn5GqBCFmztCwXjZG0OtB+SqJC3q9p3SYyT5VnQvk+iTL5ZDvJ+KgelCpmtt9Gbc4Aymb6rYpS8UUeZ3JkDjJMfZ/q0u0mMYJxcmgXt2/70MXXFydy+AjMgTTvzkLhqfmDeKl55D5YgftF5fwHedFZh2jlFwqahADekw7njhq7rwzk9N6wPG8agrueO6znd0IPHoLEiyZ9LZE1aTOBuTLA4xjIy+V2kCSooDxqGtwUrZH0L1j3kmFqCPtzVUnoRTzdrNd4w3aq1kTF80qN7WArVbJIoVBqJMAVllHLeSIQeZPtRTSex9xokMEp+E1RSY1vKlDEN/5fuwYQRQIT86rDNAX2KPYGP0hEcogOYail9uOsFz+KlZr0uXD5qTo53oMXGmOlavGQLH8maFMPo6Ggx237Rl9lL/5aEZtqlyAgqGZl8/cezO8aJjTY/E7TAHkeD6v/ArqX3/L1CB1mePdbF0JHXxdDBvd3CEXYY+1uKiskgpejUrfK2hkIWrwI9xA50pDzTrPnOYJgSwyj5MkUFzZd8s+FzUeG+bfGKU7X9EV61fO4LXj/PvQnh80nHt0XT5zXhOW6Vmy4vNn0Rag2xATyUPUAkGv9UkVFSZdbeLiVbCD8sX4MExs+YtXHuuFo0uyBtefQO0EsQOttqA7wmxHioUzUdl1vnrMZ53rDMMd8RLvedujXES76Y4JO2U7OCsq1uHvD4pOOWmxPc8fhYTXgWFw3eaLqu41YHuOmW20TB5CxzzOaeLXz+ilURDYtPmrVQVrhD7Dk8mX4Ec/Q44jrZXHA8yv6PfS0lib1n2iqhBCZbSg8mnm56fsi3BP3YvQYq0KOUlXzTLQcSFdHY0fcQi6djGL0hRwzW/TVpeNr8RtMy9nd/RprAOMYqZs0Lgt17aEdl9zbqCKY6O6XhIR42jFTnkW+jRs54cufc6cPsofAHINPYx5JEYiyYBPLsIaJsIv3XJJVINPZLPPBi68HLONixYDQgiNJ2JCT4WVqBe1L51WgktExhBvbhXtxN5t8CtXURNOXBSGj38mdJ+k8pEYwjFyqFffOXA/skf6QS2ld5Y1XSZJ7PXpci/4n5hc3RfbVjy/dN52T4fP7dQnEDKJwNLs/LEDqR1Xw2Sq7vPdVxx+pwAgowCqfhRbBhAqZgSvprAJZ8jP8=); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVV9oHNUX3jM7O3P3JL/N9GbbTm//3e6P1nVJwmTqahvU3S2oQVCqi1TEh4zJ7O6Q3blhZ9YkbxX6IKW1Wl9sLFaoxRAMSFQoBV/0JYpgpKCCiiH2wUofSlTQFURmNn82iz74UDwPM/d855zvO/fOvXNxDwENdOCQhhGowAScBHgR4E2AWQDaHUalIHoE2EIXIVqUTaNKPvygR7/RhVHy3hTK5PpnGqrkjSVN/0JBlXz8fo/+QwIV8npZ/y6BKpk/B/r3CZTJ1/OAKnn3PATFCjlXa8GvLWkok7O3NIySszWUyc2Xg7w/rvTotxIYQZX89gro3/SmDmmLTvrGJTgN0ilnBuKXrXesbwuXrsAcqGecty/CS84ynHKOkbBvyMM1aX/2sGkYxmDWyA4ag6bZbxjZw0bWMI3g0W8uSvKSRFak2ThuxzhTMZaWya8iRVBBud80vQ1YIasbsOEhx+QcbMOeptKNeLxRrfK65ZbttYzBox7dwZKoZRJEodJQhCkoo5T1hiJ0L9uNWiqB3QsQxyj5RVBJi20oU8Z0/F+qC+NmABHys8PWB/QR9hDeT4dwgPZhsqlsw56nPJsXG7WacPmwNTnehhbqo5Zr82JF+EhWpBhGh4cLmdaLPsue+bckNN0qRUZQScvkq98f3zKOr7X5uaB59iCa1PgHdj214+8V2shy7IEOhra8DoY27s0WDrD92NtUNEwEKQWnZo9taihk9jLQfWxPW8pjjarv9IcpMYyS60kqaK7oW3WfixL3KzYvOeWKP8TLts99wWvT3JsQPp90/Ipo+LwqPMctc8vlhYYvQq0B1of7MnuIRNVPFRklTWat7VKsCOGH5SsQR/WEVR3njqtHMxelDY/eBPoqhM6mWh+vCjEe6pQtx+X283Z9mtdta9R3hMt9p2YP8KIvJvhkxanaQdlGN3d5fNJxxxoT3PH4aFV4Nhd1Xm+4ruOW+7jljrWIgsnZ1miFexXh8+fskqjbfNKqhrLCHWBP4NHUfZilhxFXyfqC40H2f9zWVBLYfaKlEkpgoql0YfzRhueHfHPQi51roAE9SFnRt9yxQKIk6lv6HmBqKobRa3LEZJ1fk4anza83bHN352ekcVQxVrKqXhDs3ENbKju3UVsw2d4pDQ/xoGkm2498CzWz5sNb507vZfeEPwCZxj6SJBJjwSSQZ/YRZR3pXZA0ItHYT2rgxVaDl7m3bcFoQBClrUhI8KO0CLelsReikdDS+dOwC3fidjJzHrTmGdCVuyOh3c6NkNSfUjwYR06W8rtmLgT2Se5AKbQvc+aypMs8l7kqRf4T8/Proztqh+bvmM7R8PnkW/nCGpAfCe7PCxA6keVcJkqu7jzWds0acATyMAzH4WmowARMwZT01wCrN47z); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVV9oHNUX3jM7O3P3JL/N9GbbTm//3e6P1nVJwmTqahvU3S2oQVCqi1TEh47J7O6Q3blhZ9Y0bxUqSKlG0hcTAxVqMQYDEhRKwRd9iSJYKaigYoh5UPGhRH1wBZGZzZ/Nog8+FM/DzD3fOef7zr1z71w8QEADHTik4SxUYBzOA7wE8AbAPADtDqNSED0BbKmLEC3KJlElH7zfo691oUzWpgBlcutTDRUyV9E/V1AlH73Xo3+fQIW8Xta/TaBKFqdA/y6BMvlqEVAl705DUKyQqVoLfu2mhjJ58TJglLxcQ5m8/WqQ98e1Hv3nBEZQJTPToH/dmzqmLTvptStwEaQLzizEr1rvWN8UrlyDBVAvOW/NwSvOClxwTpGwb8jDDelw9rhpGMZg1sgOGoOm2W8Y2eNG1jCN4NFvLkvyTYmsSvNx3I1xpmIsLZPfRIqggnK/aXpbsELWt2DDQ47JBdiFPU2lG/F0o1rldcst2xsZgyc9uoclUcskiEKloQhTUEYp6w1F6EG2H7VUAruXII5R8qugkhbbUqaM6fi/VBfGzQAi5BeHbQ7oI+whvJ8O4QDtw2RT2YU9T3k2LzZqNeHyYWtirA0t1Ecs1+bFivCRrEoxjA4PFzKtF32WPfNvSWi6VYqMoJKWyZe/P75jHN9o8zNB8+xBNKnxD+x6as/fK7SR5dgDHQxteR0MbdzbLRxhh7G3qWiYCFIKTs0e3dZQyPxVoIfYgbaUxxpV3+kPU2IYJbeSVNBc0bfqPhcl7ldsXnLKFX+Il22f+4LXJrk3Lnw+4fgV0fB5VXiOW+aWywsNX4RaA6wPD2UOEImqnygySprMWtulWBHCD8tXIY7qGas6xh1Xj2bmpC2P/gj0MoTOtlofrwoxFuqULcfl9vN2fZLXbWvEd4TLfadmD/CiL8b5RMWp2kHZVjd3eXzCcUcb49zx+EhVeDYXdV5vuK7jlvu45Y62iILJ2dZIhXsV4fPn7JKo23zCqoaywh1gT+DJ1H2YpccR18nmguNR9n/c1VQS2H2mpRJKYKKpdGH80Ybnh3wL0Iuda6ABPUpZ0bfc0UCiJOo7+h5gaiqG0RtyxGSdX5OGp82vN2xzf+dnpHFUMVayql4Q7NxDOyo7t1FbMNneKQ0P8aBpJtuPfAs1s+bDO+dO72X3hD8AmcY+lCQSY8EkkGcOEWUT6V2SNCLR2E9q4MXWg5d5sG3BaEAQpa1ISPCDtAy3pdEXopHQ0vmLsA/34m4yOw1a8xLoyt2R0G7nzpLUn1I8GEfOl/L7ZmcC+zh3pBTaFzlzRdJlnstclyL/ifn5zdEdtWOLd0znZPh88s18YQPInw3uzxkInchKLhMl1/eeartmDTgBeRiG0/A0VGAczsE56a8BAPnljbQ=).

**Points that do nothing for this spec:** **Endurance Training** (3) only counts toward the points the tree needs before **Bestial Swiftness**; **Intimidation** (1) only counts toward the points the tree needs before **Frenzy**; **Bestial Swiftness** (1) is needed for **Intimidation**.

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 905 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-23 from this project's builds and simulations of the WoW: Forever beta (talent data: client build 1.60.1.70753; spell numbers: client 1.60.1.70938; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

*The live client is 1.60.1.71037 (2026-11-20); these pages are on 1.60.1.70938; an update follows. Windfury Totem's buff changed in client 1.60.1.71037 and the raid simulator used here predates it: full-raid numbers of melee builds assume the old totem.*

