# Frost Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Frost

**[Frost — Raid](../research/raid/builds/frost-ml-raid.md)** (15/5/31) — [open the talent tree](https://talentsforever.com/mage/60/023212203-5-153500030121301231-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Frost — Winter's Chill), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Ice Barrier**.

**Then press the first one that is ready**, top to bottom:

1. **Ice Barrier** when Frigid Power has under 2 seconds left
2. **Arcane Missiles** (rank 7) when Missile Barrage is active
3. **Ice Lance** when Fingers of Frost is active
4. **Frostbolt**

**Frostbolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Fire Blast**: in the last 3 seconds of the fight, when there is no time left for another **Frostbolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Frost in a raid is **Frostbolt** with one buff kept up and two procs spent: **Ice Barrier** before the pull and again whenever its Frigid Power is about to run out, a free **Arcane Missiles** on every **Missile Barrage** proc and **Ice Lance** on every **Fingers of Frost** proc. 652 DPS in a full raid, the fifth mage page (Fire 873); **Ice Barrier** is the reason the build takes 31 Frost points.

**Why it works**

- **Ice Barrier** gives Frigid Power on every cast: 15% more Frost damage for a minute, and another 5% while its shield holds, which on a boss that does not hit you it does. Its cooldown is 30 seconds, so the list recasts it once a minute: 4 casts in a 3-minute fight, one before the pull. It is the 31-point Frost talent. Until 2026-11-19 no rotation of ours cast it, so every search valued it at nothing and the Frost builds stopped at 30 points; with one Arcane point moved into it the best Frost build went from 614 to 664 DPS in a full raid.
- **Frostbolt** is the list: 57 casts and 72% of the damage. **Improved Frostbolt** takes its cast to 2.5 seconds, **Ice Shards** doubles its critical bonus, **Frost Channeling** cuts its cost by 15%, and **Precision** adds 6% hit. Each one that lands can set up the next two lines: a 20% chance of **Missile Barrage** and, through its chill, a 15% chance of **Fingers of Frost**.
- **Arcane Missiles** on a **Missile Barrage** proc comes before **Frostbolt**: about 10 casts and 18% of the damage, each free, half as long and firing every half second, with **Arcane Impact**'s 6% crit. **Improved Channeling** at 2 points gives a 40% chance that a hit does not cut it short.
- **Ice Lance** while **Fingers of Frost** is up: about 5 casts and 9% of the damage. The proc makes your next two spells treat the boss as frozen, so **Ice Lance** deals 300% more damage and **Shatter** adds 50% crit chance (**Incineration** another 10%); the list spends both charges on **Ice Lance**.
- Mana holds in a raid: the mana gem (from **Conjure Mana Ruby**) about once a fight and a potion one fight in four; **Evocation** never ran in the simulator. **Arcane Concentration** at 2 points makes 4% of your casts free.
- **Fire Blast** only in the last 3 seconds (under one a fight): a **Frostbolt** started then would still be in the air when the boss dies.

**Caveats**

- The hand-made Winter's Chill build (21/0/30, under Other builds) stops at 30 Frost points, a point short of the 31st row: 523 DPS in a full raid against this build's 652. **Winter's Chill** itself only helps **Cone of Cold** since the 2026-11-02 patch; this build keeps 3 points in it to reach the talents below it.
- The shield's 5% lasts only while it holds. When raid damage breaks it, cast **Ice Barrier** again as soon as its 30-second cooldown allows: the simulator's boss never hits you, so its list recasts only near the end of the minute.
- Several targets: **Blizzard**, **Cone of Cold** (with **Winter's Chill** stacks from your **Frostbolt** hits) and **Arcane Explosion**. The simulator's fights are one boss.
- Moving: **Ice Lance** on a proc, **Fire Blast** and **Ice Barrier** are instant.
- Threat: **Frost Channeling** and **Arcane Subtlety** cut your Frost and Arcane threat by 30%; the simulator ignores threat, so give the tank a few seconds on a fresh pull.

**When to change it**

- In the last 3 seconds, **Fire Blast** instead of a **Frostbolt**.
- When your shield breaks early, **Ice Barrier** again as soon as it is ready.
- On a pack, **Blizzard**, or five **Frostbolt** hits and then **Cone of Cold** on the **Winter's Chill** stacks.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 15 | Improved Channeling 2, Arcane Resilience 3, Arcane Subtlety 2, Arcane Concentration 2, Missile Barrage 2, Arcane Impact 3, Magic Absorption 1 |
| Fire | 5 | Incineration 5 |
| Frost | 31 | Frost Warding 1, Improved Frostbolt 5, Precision 3, Ice Shards 5, Frost Channeling 3, Ice Lance 1, Arctic Reach 2, Ice Block 1, Shatter 3, Cold Snap 1, Fingers of Frost 2, Winter's Chill 3, Ice Barrier 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 652 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 594 | [13/6/32](https://talentsforever.com/mage/60/203201203-5001-253500130100331221-12) |
| Pre-BiS | 646 | [13/6/32](https://talentsforever.com/mage/60/203201203-5001-253500130100331221-12) |
| Raid BiS | 671 | [15/5/31](https://talentsforever.com/mage/60/041203203-5-253500020121301231-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 59.3; Pre-BiS 62.2; Raid BiS 64.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Boreal Mantle](https://www.wowhead.com/forever/item=11782) · *Warder Stilgiss, Blackrock Depths* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sorcerer's Bindings](https://www.wowhead.com/forever/item=226929) · *sold by Mokvar*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Sorcerer's Gauntlets](https://www.wowhead.com/forever/item=226930) · *sold by Mokvar* |
| Waist | [Ban'thok Sash](https://www.wowhead.com/forever/item=11662) · *Ok'thor the Breaker, Blackrock Depths* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Venomspew Footpads](https://www.wowhead.com/forever/item=275606) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Kayser's Boots of Precision](https://www.wowhead.com/forever/item=22231) · *War Master Voone, Blackrock Spire*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* | [Wand of Biting Cold](https://www.wowhead.com/forever/item=19108) · *quest: The Legend of Korrak* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/mage/dps/#eJzElk2MFEUUx6e6Z3drC4W1ERhaDo9NFmfH7aW7h9ksa8IOaIxIlI0eNIhCzXTNdJmerklXDQMXsygaQxQI6gEiiSEYjIgmeAESD5iQrCYaNVEOXogfQU8aD8QTmurpZddwFazDTPX713vvV++9TpqswWgIFRCgItqNQtRGswi9htC7CL2PkHVXqhpanUT2J3djPITtiAzg00dR4ZclJI9f/hgRE7+6k5j42g4ygL85jAo/LSUD+NIRVPhhKTHx5SYx8aFnST/+s6F9+vFHOwuHB4iJ/6bExPtrxMRHWsTEJ5qkH7/eKswtJyaefY7k8am30fDY0BwvfnUIuddrM2+cRAeRcYAfRcb12nFkXNv8AcKn30EfHkSH+FV0gG/BKTCqoovGWt8t+67nu2Wn4rqe41fK+r/seq5bLnu+780Z6GtjyY/GpSXEIgN2HzHxb2x4gPQR0/Gl9W3eOpunQcAC8F1/wvE8x9sIxY5kyRQMh6ILXMLWOoMtNEk4SyAWCroiUSFwBQ2RwCOJkArGx8dhqwIe1xNGJZMQ0BZtMghEzKC2D3x3BLohjxhwJYHWFd/Dhken/hW6G7KY7WE6JG/yAGZElyVjqcMDXmUky5QF1qk9aPF4DEIqoRMHLAEfJESsoR4EFTKQIWdRADQIJFQW0kMookBCUfLWeh1qPa+zXbUew3hTQEsELJJQEyocHYcnBCRCUcVFDKIBopNICGkAdSoVcDUGUoCG3geS0aQewh4adViQAigasVgBVeACjXu23iVqHa4ZpBLtNgv0ibKbSW3BYyWhyJUuvXYpe05qzOKNToGIGWxO6jRm0FN4rERKo88/zWPFkvslPBTyKOrlgopfBmcTVCYn4eGZp1Kchs7ntCInoTyACS89MDHhAo+BQqMTRZAqxYkx13WhwZuhkqM2kFWlFdi0Bi+ifpLHZ27M2P0kTwxfZtNlnUHWK2jRULkbHX9yap74cS4lj5gEodNkT+kQ6L62E1Efg2aHJtq9tg9oJ6Fb5bZYdGNda5rdp8tVKDrqFv/eBOnuSODKXksK1koy+EVeo355oUAGz6Fsm9L+vN16D1mUtqNdoq2yd8B1/PIU1EMaN1kAItEj1IPR5b05DlnDi5KxrJa6XM687vT08RekiEftKpmwNxC7VFio3KcXCvbgcUNv3/puG1lZuldrn93U+ohJkG9nurXGtsk9pWU4bxm1nJ2+wZPuiL7F0NwmK28bUzmrbHukaK1Lz5kL53x3JDX1WcZj86ZKr11vPm/N3pEC3JcS9C8icGV6t5f+mrFW2MvnO3PiYiE1/35lm/XirWCu/1+DrSZDpaUZWDrI5V5lLm+3DqI7ATBC1pRsDbAjZ1vnjGXYXCiS57kpzJXtBfNXYw79Yfj7zVy6NlRP6lEhBkbDN4xBbcrNNqqrjx/T6/PptY10fT/tXzUKeZgunTdy/8tS1fndbV3rzt62PBvT3ydPVTdnhupu/QFxDKUPuavTJROfX7Vl0XeGiyZRFT2KZtAzKERttBftNf4ZACdyBGM=); Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzElkGMFEUXx/f19O7UFt8HYyMwtBwemyzOjjtLdw+zWdaEHdAYkSgbPWg8CD3TNdtlersmXTUMXAwqJoYoEEUSUBNDMBoRTTgYwHiAxGQ10WxMlIMXohLFmGA8EBMTYqqnl8VwFaxDdfX7V733q/deJ03XEChAERBKsBNCaMNegJcB3gF4H8D6X6oaWp0A+9P/E1IgtqJ58tcpKF5eQk3y4sdATfLrYT2/OV+gA2QuLv64lObJ+UNQ/H4pzZELMTXJ5YNAB8gfLX0qT45cKRQP5qlJDvxWoCY5Mq/nT+YLNEcOzdI8ufoRFOeWU5O8clA7PvEGDI0W5njp6wPgXGtMv3oc9oOxj78GxrXGMTB+3vwBkPfegg/3wwF+CfbxLSQFhzqcM9Z6TtVzXM+pVmqO41a8WlU/q47rONWq63nunAHzxpIfjPNLqEXzdj/NkStsKE/7aa7iSesb0zpl+kHAAvQcb7ziuhV3I5Y6kiWTOBSKLnKJW5sMt/hJwlmCsVDYFYkKkStsiQQfSoRUODY2hlsV8riZMF8yiYE/688wDETMsLEHPWcYuyGPGHIl0W8qvosNjUz+w3U3ZDHbxbRLPsMDnBZdloymB+5za8NZpMyxDu3iLI9HMfQlduKAJeihxIi11P2oQoYy5CwK0A8CibXF8BiKKJBYknx2vXa1njfZjkaPYWxG4KwIWCSxIVQ4MoaPCUyE8hUXMYoWik4iMfQDbPpSIVejKAVq6D0omZ80Q9zlRx0WpADKj1is0FfooB/3bL1LNDpcM0gl2m0W6B1VJ5PagsdKYokrnXp9pOpWUmPmb2QSRcxwc9L0Y4Y9hcdKpDR6/5M8Viy5V+IDIY+iXiyseVWsbMLaxAQ+OP1EitPS8SqzUSXxeYDjbrphfNxBHqOPrU4UYaqUxkcdx8EWnwmVHLGRriqvIDlr8BwMUJOcvD5tD1CTGp7Muss6CdZLcFNTORsr3sTkAvGjXEoeMYlCh8ne0ibQdW0nojmKMx0/0ccbe9DvJP5WuS0W3Vjn2s/u0+UqFB11y/leB+nqSOTKXkuL1ko6+KWpUb86W6SDpyFbprQ/bbfeBcv329EO0VbZN+BUvOokNkM/nmEBikS3UA9Gp/dGO2QFL0nGslzqdFUW9EpPH3tWinjErtNxewO1y8XFzH12tmgPHjP08vC32+jK8t1au3BD66c5Cp6d6dYa26Z3lZcR0zIafXb6BU84w/oWhblNlmkbk31W1XZpyVqX7sst7vOc4dTUbxmPLJhqvXK9/oy1944k4J6UYOAmAkemd3vhz2lrhb18oTJvnyum5qsXt1nP3QrmeP822GpaKC/NwNJGrvYy8/l2az/cCYBhuqZsa4Cn+2zrtLGM5BaT5LpOCnNxezH3izEHvxve87m+dGyoH9etQg0CQ9eNQW3q29uqrz52VI8vpta20vHdlHfJKJo4VT5j9P0nQ9UXVrd1rDt12+JsTOfHT9Q3Z4b6Tv0jcRTSl75LU+UcObNqy03/Gw5MQB0ehml4CkJow27Ybfw9AEK+CN4=); Raid BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzEVk+IHMUX3tfTu9Nb+SXZX8ckkzbIy8LG2XFn092TWTYrZCdRgjFoFj0oHkxqpmu2S3q7hq6aneQiUSJI0ATy55CoIEFRjOshB0kWPCgIq6IEQXMQIajBPwSiOQRBCFI9vdlIria+Q1H9vvfqfe+r11BkvQUDUACEIuyFEFpwAOBlgDcB3gWw/5eihkbHwZlfblkDljNL8tZfc1C4vIyY1o2jQEzrt+N6fe3CAOmzFuLCjytI3vrjyvLCdyuIaV27spyY1uUjQPLW9yfSvLx1cQ4KR/LEtL44ATfXg8f0+uGFAZK3rn4AhYVVxLReOQIkZ12LBkcGFnjxq8PgXq9PvXoaDoFxkB8F43r9FBg/b3sPrHdeh/cPwWF+CQ7y7VZKHWowb9znbvZ8t+K7lXK17FcrVdd1fdfzvYrr+RVvwYALxrIfjI+XEZvknV6Ss35lg3nSS3JlX9pfm/acSYOABei7/ljZ88reFiy2JUsmcDAUHeQSdzYYbqdJwlmCsVDYEYkKkStsigR3JEIqHB0dxZ0KedxIGJVMYkBn6DTDQMQM6/vRd4ewE/KIIVcSaUPxWTY4PPGPozshi9ksS3BHwqd5gFOiw5KRNOEBrzqUVcoObooEPZzh8QiGVGI7DliCPkqMWFM9iCpkKEPOogBpEEisLpXHUESBxKLkM5v0UZt4g+2pd9sbnRY4IwIWSawLFQ6P4uMCE6Go4iJG0UTRTiSGNMAGlQq5GkEpUJPej5LRpBHiLI3aLEgJKBqxWCFV6CKNu75uE/U21xykEq0WC3RExc2gluCxkljkSkuvUypeOXVm5w1PoBZ1W9KgMcMuwmMlUjY6/ikeK5bcL/GhkEdRtxZW/QqWt2J1fBwfnnoypdPU9cozUTmhPMAxLw0YG3ORx0ix2Y4iTJHi2Ijrutjk06GSww6StaXVVs7un4c+Ylpnbkw5fcQkhi+z6bLPgP0S3DJU7payPz6xyPgxLiWPmEShy2Rf6XzRaYatRDRGcLpNE51e34+0ndCdclcsOrHWmmb9dLgKRVvdlt+dIH07ErlyNpCCvYb0f25qql+eL5D+s5BtU7Y/7bbfBpvSVrRHtFT2D7hlvzKBjZDG0yxAkegR6pLR8t4ch+zCi5KxTEstV3kRL3fx0eekiIedGhlzNhOnVFhS7qPzBaf/lKG3x7/ZRdaU7tHYJzexXpIj4DsZbq93HPL/0krLtI16j5P+wePukO5iYGGrbTrGRI9dcTxStDemcbmlON8dSl29tvHooqvava5jz9oH7ooA96YM+m5h4Mq0txf/nLJXO6sWb+aN+ULqvnpxl/387cRc/98mto4MlFZkxNJBrnSV+XS3fQjuBoEhsr7kaALP9Dj2WWOllVsSyfPclMzF3YXcL8YC/G74L+R6UttcO61HhRgWDN4w+rWr50Cztu7USW2fTW5opvbtpH/JKJg4WTpn9PwnpmqLuztqG+fuWJ0t6frEW7VtmaO2V78jTkL60XNpspSzzq3dfstzw4VxqMEjMAVPQwgt2Af7jL8HAN1jChE=).

**Points that do nothing for this spec:** **Ice Block** (1) and **Cold Snap** (1) only count toward the points the tree needs before **Ice Barrier**.

## Other builds of this spec

- [Frost — Winter's Chill](../research/raid/builds/frost-winters-chill-raid.md) (21/0/30, 523 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/041215203000201--25353003002100105-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

