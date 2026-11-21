# Beast Mastery Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast Mastery

**[Beast Mastery — Raid](../research/raid/builds/beast-mastery-ml-raid.md)** (31/20/0) — [open the talent tree](https://talentsforever.com/hunter/60/5320001505101251-00530502005--12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Before the pull:** **Hunter's Mark**, **Aspect of the Hawk**.

**Keep up all fight:** **Aspect of the Hawk**.

**Talents with no line below:** **Intimidation**: taken because Bestial Wrath requires it.

**Then press the first one that is ready**, top to bottom:

1. **Hunter's Mark** and **Serpent Sting**: keep them on the target
2. **Aimed Shot**

Between these, **Auto Shot** keeps firing on its own.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Summon Hawk**: part of the rotation (about 20 times a fight)
- **Arcane Shot**: part of the rotation (about 10 times a fight)
- **Bestial Wrath**: a cooldown, use it at the start of the fight and again whenever it is ready (about 2 times a fight)
- **Rapid Fire**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Beast Mastery in a raid shoots from range with its cat out: keep **Hunter's Mark** and **Serpent Sting** on the boss, spend the cooldown **Summon Hawk** shares with **Arcane Shot** as hawk, hawk, **Arcane Shot**, fire **Aimed Shot** whenever it is ready, and use **Bestial Wrath** and **Rapid Fire** as they come up. This is the official simulator's own rotation with hawks (its turret_hawk file; since 2026-11-20, when it beat ours by 2.1% on this build). In a 3-minute raid fight: **Aimed Shot** 23 casts, **Summon Hawk** 20, **Serpent Sting** 12, **Arcane Shot** 10, **Bestial Wrath** 2, **Rapid Fire** 1; **Auto Shot** 31% of the damage, the cat's and the hawks' swings 30% (one line in the record), **Aimed Shot** 14%, **Serpent Sting** 11%, the cat's Claw 5%, **Arcane Shot** 5%, the hawks' dives 3%.

**Why it works**

- **Hunter's Mark** and **Serpent Sting** come first, each cast only when it is missing from the boss: the mark lasts 2 minutes (2 casts a fight), the sting 15 seconds (12 casts, never refreshed early; 20% stronger with **Improved Stings**). The mark and **Aspect of the Hawk** go up before the pull; **Deadly Aspects** needs the aspect: each **Auto Shot** then has a 10% chance to speed your shots by 30% for 12 seconds.
- **Summon Hawk** and **Arcane Shot** share one cooldown, spent in a fixed order: hawk, hawk, **Arcane Shot**, then again (20 hawks and 10 Arcane Shots a fight, a use about every 6 seconds). A hawk dives for 108 plus 5% of your ranged attack power, then attacks for 18 seconds; only 2 can be out, and one every 9 seconds keeps both out nearly all fight. **Unleashed Fury** and **Ferocity** work on the hawks as well as the cat.
- **Aimed Shot** whenever it is ready: a 2-second cast on a 6-second cooldown, 23 casts a fight. **Multi-Shot** shares that cooldown and is switched off for a single target (the rotation's "Use Multi-Shot").
- From 5 seconds in, the rotation uses every other cooldown as it comes ready: **Bestial Wrath** (+50% pet damage for 18 seconds) about 5 seconds in and 2 minutes later, **Rapid Fire** (40% faster attacks for 15 seconds) once, your on-use trinket (the page's sets carry Blackhand's Breadth) and a Major Mana Potion. **Intimidation** has no line: the build takes it only because **Bestial Wrath** requires it.
- The cat takes a tenth of your attack power and your crit chance. **Ferocity** (+10% crit), **Frenzy** (30% faster attacks for 8 seconds after each crit), **Unleashed Fury** (+15% damage) and **Bestial Wrath** build on that, and **Focused Fire** adds 2% to you both while it is out. It attacks and uses Claw on its own; keep it on the boss.

**Caveats**

- Full raid: every raid buff and debuff, phase-1 gear, 3-minute fights. The list has no mana guard: on the simulator's training dummy (your own buffs only), the raid's mana buffs alone (Mana Spring Totem, Mana Tide Totem, Greater Blessing of Wisdom, Judgement of Wisdom) add 18% to this build's damage.
- Keep the cat alive with **Mend Pet**: Forever pets take no stat buffs from players, and a dead cat takes **Bestial Wrath** and **Focused Fire** with it. In the simulator a pet keeps the attack power it took from you when called until it is dismissed (its authors' reading of combat logs), so call it after your buffs are up.
- The pet and the hawks are the simulator's models, unmeasured at 60: since 2026-11-19 a faster pet's swing hits for less, so its damage a second stays the same (fitted to one level-30 combat log), and the hawks' attacks after the dive, which the game files do not describe, are fitted to combat logs.
- Ranks: the list casts the trainer's top ranks, **Serpent Sting** rank 8 and **Aspect of the Hawk** rank 6 (ranks 9 and 7 are class books, not in Forever on the evidence there is; checked again when the raids open on 2026-12-09). For **Hunter's Mark** the simulator uses rank 3's +98 ranged attack power, as the client data it reads lists rank 4 lower; the beta tooltip (build 70753) reads rank 4 +143. Cast whichever rank your tooltip shows higher.
- Moving: **Auto Shot** and **Aimed Shot** stop while you move; **Arcane Shot**, **Serpent Sting** and **Summon Hawk** are instant. Move right after an **Auto Shot** goes off, as the simulator's walk to its spot does ("Windup close", "Just shot").

**When to change it**

- Two or more targets close together: **Multi-Shot** in place of **Aimed Shot** (it hits 3 targets). For a pack, **Volley**: a 6-second channel with no cooldown.
- In the last few seconds, skip the **Serpent Sting** recast: its damage comes over 15 seconds.
- Inside 8 yards your shots and **Auto Shot** stop: step back out. **Summon Hawk** has no minimum range.
- Short on mana: let **Aimed Shot** go first. In this build's full-raid numbers it does about 1,030 damage for 310 mana, **Arcane Shot** 810 for 190, **Serpent Sting** 1,600 for 230.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 31 | Deadly Aspects 5, Endurance Training 3 (tier point: needed to reach Bestial Swiftness), Focused Fire 2, Bestial Swiftness 1 (needed for Intimidation), Unleashed Fury 5, Ferocity 5, Summon Hawk 1, Intimidation 1 (needed for Bestial Wrath), Bestial Discipline 2, Frenzy 5, Bestial Wrath 1 |
| Marksmanship | 20 | Lethal Attacks 5, Improved Stings 3, Careful Aim 5, Improved Arcane Shot 2, Mortal Shots 5 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a full search on 2026-10-16 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 946 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 889 | its own set |
| Pre-BiS | 941 | its own set |
| Raid BiS | 956 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 61.9; Pre-BiS 62.6; Raid BiS 63.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Backwood Helm](https://www.wowhead.com/forever/item=18421) · *quest: The Treasure of the Shen'dralar*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Shadowcraft Spaulders](https://www.wowhead.com/forever/item=16708) · *Cannon Master Willey, Stratholme* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Ogre Forged Hauberk](https://www.wowhead.com/forever/item=18530) · *Tribute, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Legguards of the Chromatic Defier](https://www.wowhead.com/forever/item=12903) · *quest: Legplates of the Chromatic Defier*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Tribute, Dire Maul* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Beastslayer's Trident](https://www.wowhead.com/forever/item=279910) · *quest: Mapping the Way Forward*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVU1sG0UU9luvd8cvwd1M3HY7TcvUqMVYabTeYmgjwHYlIEICFSxUhDh0idf2qvZO5F3j9lZQDygqJKKnhkhFKogoIpdyqXpEPQQugJAACRBRqICiHqpAD/iA0K7z41hw4FDxDt73vvfe972ZnfHiCAENdOCQhlNQgyk4B/AmwHsACwB0MMxKQfYosKUBQrQoa6NK7s6AfnMAo+TjMyiTG28AKmS+pn+poEpWZ0H/KYEKebeq/5BAlSzNgP5jAmXy7VJQ90s5aFXITKOL3pgFlMn52xpGyVsNlMmtWUCV/Dw9pN9OYARVcnEG9O+GU4e0ZSd98zJMg3TemYP4Fesj6/vi5Q9gEdQLzofz8LazAued4yScGgpwXRrJHTENw8jmjFzWyJq57GHDyB0xcoZpGLllSf5CIqvSQhx3YpypGEvL5K5IEVRQPmya3iaskLVN2PCQY3IRhnBHRxlEPNGq13nTcqv2ekX2mEd3sSRqmQRRqDQeYQrKKOW88Qjdx/ailkrg4FWIY5T8IaikxTaVKWM63pcawLgZQIT87rANhz7NnsTH6DiO0VFMdpQh3PGiZ/NSq9EQLp+w2qd70GJz0nJtXqoJH8mqFMPoxEQx033QV9jL/5WEprutyAgqaZl88+dz2/z4+pifC1pgT6BJjX9h11O7/lmhhyzPHu9j6KnrY+jh3hrhALsfhzuKhomgpOg07PKWhkIWrgDdz0Z6Sp5t1X3ncFgSwyj5KkkFzZd8q+lzUeF+zeYVp1rzx3nV9rkveOMs96aEz9uOXxMtn9eF57hVbrm82PJFqDXGRnF/ZoRIVP1MkVHSZNY9LqWaEH7YvgpxVE9a9dPccfVoZl7ajOgtoBchDLbURnldiNOhTtVyXG6/ZjfP8qZtTfqOcLnvNOwxXvLFFG/XnLodtG1O86DH245bbk1xx+OTdeHZXDR5s+W6jlsd5ZZb7hIFi7OtyRr3asLnr9oV0bR526qHssIdY8/jsdSjmKNHENfIxobjQfYADnWUBA6e7KqEEpjoKAMYf6bl+SHfIgxj/x5oQA9SVvIttxxIVERz29xjTE3FMHpdjpis/23S8Lb5zZZt7u1/jTSOKsYqVt0Lkv1naFtn/zHqSSZ7J6XhJc6aZrL3yndRM2c+tX3t9BH2cPgHINPYJ5JEYixYBPLMfqJsIMNXJY1INPabGkSxteBh7uvZMBoQRGk3ExL8Ki3DHan8ejQSWrowDXtwN+4kc++A1rkAuvJQJLQ7+VMk9ZcUD/zIuUphz9ylwD7NH6iE9nXeXJF0mecz16TI/2J+YcO7p3Zo6Z7pHAt/X3i/UFwHCqeCT+clCIPISj4TJdd2H+/5whpwFAowASfgJajBFJyBM9LfAwAYJIyw); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVV2IG1UUzplMZm7Ortnp3bSd3m7rbaQ1hu0ymRptFzVJQV0EpRqkIj7suDtJhk3mLpmJu32r0AcprT/1xa4LFWpxXaxIVSgFX/RllQUrBRVUXNY+qPShrAoaQWQm+5MN+uBD8TxkzvnOOd937p17MzhAQAMdOKRhFKowCccBXgB4A2AOgPaGWSnIHgT2bg8hWpRNo0o++rBPv96DUfL+NMrk2qKGCpmt6l8oqJJPPujTf0igQl6v6N8lUCWLi5r+fQJl8vVFQJW8dwaCXoW8VG/Dr13VUCanb2gYJafrKJO3Xw7q/rzQp99IYARV8vsroH/Tn9qnLTjp6+fgJEgnnBmIn7fesb4tnrsA86Cect6ahRedJTjhHCbh2FCAK9JA7oBpGEY2Z+SyRtbMZfcbRu6AkTNMw8gtSPJViSxLc3HcinGmYiwtk99EiqCC8n7T9NZhhaysw4aHHJPzsAX7Wkov4pFmrcYblluxVyuyhzy6jSVRyySIQqXhCFNQRinnDUfoLrYTtVQCey9BHKPkV0ElLbauTBnT8bZUD8bNACLkF4etOfRh9iDeR4dxiA5isqVswb4nPZuXmvW6cPmINTXRgRYbY5Zr81JV+EiWpRhGR0aKmfaDPsOe/q8kNN1uRUZQScvkqz8e2+THV8f8XNACewBNavwLu57a9s8KHWR5dn8XQ0ddF0MH98YIe9jt2N9SNEwEJUWnbo9vaChk7jzQ3Wygo+TRZs139oclMYySa0kqaL7kWw2fizL3qzYvO5WqP8wrts99wevHuDcpfD7l+FXR9HlNeI5b4ZbLi01fhFpDbBB3ZwaIRNXPFBklTWbt41KqCuGH7csQR/WoVZvgjqtHM7PSekR/AvoqhMGG2iCvCTER6lQsx+X2c3bjGG/Y1pjvCJf7Tt0e4iVfTPKpqlOzg7b1ae70+JTjjjcnuePxsZrwbC4avNF0XcetDHLLHW8TBYuzrbEq96rC58/aZdGw+ZRVC2WFO8Qex0OpezFHDyCukLUNx73sDtzSUhLYe7StEkpgoqX0YPyRpueHfPPQj917oAHdS1nJt9zxQKIsGpvmHmJqKobRK3LEZN1vk4a3zW80bXNn92ukcVQxVrZqXpDsPkObOruPUUcy2TkpDS9x1jSTnVe+jZo586HNa6f3sLvDPwCZxj6WJBJjwSKQZ3YTZQ3pvyRpRKKxn9Ugiq0ED3NXx4bRgCBK25mQ4EdpAW5K489HI6GlCydhB27HrWTmDGitU6Ard0VCu5kfJam/pHjgR46XCztmzgb2aX5PObQv8+aSpMs8n7ksRf4X8wtr3i21fRdvmc6h8PeJNwvFVaAwGnw7z0IYRJbymSi5vP1wxyfWgINQgBE4Ak9BFSZhGqalvwcA2cOODg==); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVV9oHNUX3jM7O3P3JL/N9GbbTm/T/m5XWtclDbNTV9ug7m5BDYJSXaQiPnRMZneH7s4NO7Om9alCH6S0RuKLicUKtRiDgVIUSsEXfYkiGCmooGKIeVDpQ4n64AoiM5s/m0UffCieh51zvnPO9517594dHCCggQ4c0nACqjAOZwBeBngLYBaA9oZZKcgeBna1hxAtyl5ElXz4QZ++0oMyWZkElMnNzzRUyZuLmv6Fgir5+P0+/YcEKuSNiv5dAlUyPwn69wmUydfzgCq5OgVBt0Im62349UUNZXLhloZRcqGOMnn31aDujyt9+q0ERlAl01Ogf9OfOqAtOOmVS3AOpLPODMQvW+9Z3xYvXYE5UM8771yEV5wlOOscJeHgUIAb0kDukGkYRjZn5LJG1sxlDxpG7pCRM0zDyC1I8qJElqXZOG7HOFMxlpbJbyJFUEH5oGl6G7BCVjdgw0OOyTnYhn0tpRfxWLNW4w3LrdhrFdkjHt3BkqhlEkSh0nCEKSijlPOGI3QP241aKoG91yCOUfKroJIW21CmjOn4v1QPxs0AIuQXh6079FH2MD5Ah3GIDmKypWzDvqc9m5ea9bpw+Yg1cbIDLTZGLdfmparwkSxLMYyOjBQz7Qd9jj37b0lout2KjKCSlslXvz+xxY+vjfm5oAX2EJrU+Ad2PbXj7xU6yPLswS6Gjrouhg7uzRH2sf9jf0vRMBGUFJ26PbapoZDZy0D3soGOksebNd85GJbEMEpuJqmg+ZJvNXwuytyv2rzsVKr+MK/YPvcFr5/m3rjw+YTjV0XT5zXhOW6FWy4vNn0Rag2xQdybGSASVT9VZJQ0mbWPS6kqhB+2L0Mc1eNW7SR3XD2auShtRPQnoK9BGGyqDfKaECdDnYrluNx+wW6c5g3bGvUd4XLfqdtDvOSLcT5RdWp20LYxzd0en3DcseY4dzw+WhOezUWDN5qu67iVQW65Y22iYHG2NVrlXlX4/Hm7LBo2n7Bqoaxwh9iTeCR1P+boIcRVsr7huJ/dhdtaSgJ7j7dVQglMtJQejD/W9PyQbw76sXsPNKD7KSv5ljsWSJRFY8vcQ0xNxTB6Q46YrPtt0vC2+Y2mbe7ufo00jirGylbNC5LdZ2hLZ/cx6kgmOyel4SXOmmay88q3UTNnPrJ17fQ+dm/4ByDT2EeSRGIsWATyzF6irCP91ySNSDT2sxpEsdXgYe7p2DAaEERpOxMS/CgtwG1p7KVoJLR04Rzswp24ncxMgdY6D7pyTyS02/kTJPWnFA/8yJlyYdfMdGCf5PeVQ/syby5JuszzmetS5D8xv7Du3VE7MH/HdI6Ev0+9XSiuAYUTwddzGsIgspTPRMn1nUc7PrIGHIYCjMAxeAaqMA6n4JT01wAh6o4O).

**Points that do nothing for this spec:** **Endurance Training** (3) only counts toward the points the tree needs before **Bestial Swiftness**; **Bestial Swiftness** (1) is needed for **Intimidation**; **Intimidation** (1) is needed for **Bestial Wrath**.

## Other builds of this spec

- [Beast Mastery (optimized, with a pet)](../research/raid/builds/opt-mm-raid-raid-dps.md) (31/16/4) — [open the talent tree](https://talentsforever.com/hunter/60/5420001505001251-0050550001-4-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

