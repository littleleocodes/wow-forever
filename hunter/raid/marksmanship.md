# Marksmanship Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Marksmanship

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Marksmanship — Raid](../research/raid/builds/marksmanship-ml-raid.md)** (7/39/5) — [open the talent tree](https://talentsforever.com/hunter/60/502-0053252501523051-5-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (raid BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Lone Wolf), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the With a pet setup. The spec's best build for each other setup, in a full raid:

- Lone Wolf: [Marksmanship — Lone Wolf](../research/raid/builds/mm-lone-wolf-raid.md) (5/41/5, 987 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5-0053452511513051-5-12)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Talents with no line below:** **Trueshot Aura**: turn it on before the pull.

**Then press the first one that is ready**, top to bottom:

1. **Aimed Shot**
2. **Arcane Shot**
3. **Rapid Fire**; no global cooldown, so press it alongside the others
4. **Multi-Shot**
5. **Serpent Sting**: keep it on the target
6. **Sniper Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Marksmanship raids with its pet out: the cat does about a fifth of the damage in the simulator's full raid, and **Focused Fire** adds 2% to everything you and the pet do while it is out. **Auto Shot** is about a third of your damage; **Aimed Shot**, **Arcane Shot** and **Sniper Shot** go out as soon as their cooldowns allow, **Aimed Shot** first.

**Why it works**

- Before the pull: call your cat, cast **Trueshot Aura** (in Forever a buff you cast, 30 minutes for your party and raid) and **Aspect of the Hawk**, and track the boss's creature type, since **Improved Tracking** adds 5% only against the tracked type.
- **Aimed Shot** comes first: it is your biggest regular hit (weapon damage plus 350, 10% more with **Barrage**), and its 6-second cooldown starts only when the 2-second cast ends, so any delay pushes every later cast back. Start it while the next **Auto Shot** is more than half a second away, so the cast does not clip one.
- **Arcane Shot** every time it is ready: 5 points in **Improved Arcane Shot** bring its cooldown to 4.5 seconds, about 35 casts in a 3-minute fight, more than any other button.
- **Rapid Fire** gives 40% faster attacks for 15 seconds; **Rapid Killing** cuts its cooldown to 3 minutes, so it comes once in a 3-minute fight, at the pull. The full rotation presses it right before an **Auto Shot**.
- **Serpent Sting**: recast it with under 0.75 seconds left, but not when **Aimed Shot** or **Multi-Shot** is half a second from ready, and not in the last 6 seconds. Each sting also starts **Rapid Recuperation**: with both points, half your mana regeneration keeps going while you cast for 15 seconds (all of it once a **Rapid Killing** is spent).
- **Sniper Shot** hits hardest (weapon damage plus 590) but takes 4 seconds, so it goes last: start it only when **Aimed Shot** is at least 2.25 seconds from ready and **Multi-Shot** at least 1, so the long cast barely delays your biggest hit. It comes about 9 times a fight on its 15-second cooldown; between casts **Auto Shot** does the work.
- The pet: Forever pets take their stats from your gear (a tenth of your attack power and all of your crit chance), so the cat grows with you. It claws on its own; keep it on the boss and alive with **Mend Pet**.

**Caveats**

- **Multi-Shot** is on the list but shares **Aimed Shot**'s cooldown, so on one target it almost never comes up. It is there for groups of targets.
- Mana is tight even in a full raid: the simulator's hunter drinks a mana potion a fight. With only your own buffs its rotation drops **Sniper Shot** (365 mana) and holds **Aimed Shot** when your mana runs low.
- Moving: **Auto Shot**, **Aimed Shot** and **Sniper Shot** need you to stand still, while **Arcane Shot** and **Serpent Sting** are instant. Do not start a 4-second **Sniper Shot** when you know you must move.
- **Rapid Killing**'s other half (a kill makes your next Shot within 20 seconds hit 20% harder) never happens on a boss; on trash, let the next pull's first **Aimed Shot** spend it.
- A fight that kills pets (cleaves, area damage) takes about a fifth of this build's damage with the cat.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98), **Trueshot Aura** rank 5 +100 (rank 4 +75; if your build has it) and **Aspect of the Hawk** rank 7 +120 (rank 6 +110). Cast the highest rank you have.

**When to change it**

- Two or three targets close together: **Multi-Shot** instead of **Aimed Shot** (same cooldown, up to 3 targets for weapon damage each). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last seconds, skip the **Serpent Sting** refresh and do not start a **Sniper Shot** that will not finish; **Arcane Shot** instead.
- Without a pet, play the Lone Wolf setup linked above, about 1% behind this build in a full raid: its Lone Wolf talent adds 20% to everything you do while no pet is out, and its rotation starts **Sniper Shot** with **Aimed Shot** 2 seconds from ready.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 7 | Deadly Aspects 5, Focused Fire 2 |
| Marksmanship | 39 | Lethal Attacks 5, Improved Stings 3, Efficiency 2, Careful Aim 5, Rapid Killing 2, Improved Arcane Shot 5, Trueshot Aura 1, Mortal Shots 5, Rapid Recuperation 2, Barrage 3, Ranged Weapon Specialization 5, Sniper Shot 1 |
| Survival | 5 | Improved Tracking 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 1023 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 904 | [7/39/5](https://talentsforever.com/hunter/60/502-0053552401521051-5-12) |
| Pre-BiS | 985 | [7/39/5](https://talentsforever.com/hunter/60/502-0053552401521051-5-12) |
| Raid BiS | 1032 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 61.5; Pre-BiS 62.5; Raid BiS 63.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Soulstealer Mantle](https://www.wowhead.com/forever/item=13374) · *Ramstein the Gorger, Stratholme* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Heliotrope Cloak](https://www.wowhead.com/forever/item=18496) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Ogre Forged Hauberk](https://www.wowhead.com/forever/item=18530) · *Tribute, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Magister's Bindings](https://www.wowhead.com/forever/item=16683) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Gauntlets of Accuracy](https://www.wowhead.com/forever/item=18349) · *Illyanna Ravenoak, Dire Maul*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) · *sold by Samuel Hawke* |
| Legs | [Legguards of the Chromatic Defier](https://www.wowhead.com/forever/item=12903) · *quest: Legplates of the Chromatic Defier*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Plaguehound Leggings](https://www.wowhead.com/forever/item=18736) · *Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Beaststalker's Boots](https://www.wowhead.com/forever/item=16675) · *Nerub'enkan, Stratholme*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tarnished Elven Ring](https://www.wowhead.com/forever/item=18500) · *Tribute, Dire Maul* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18473) · *quest: The Greatest Race of Hunters* |
| Main hand | [Beastslayer's Trident](https://www.wowhead.com/forever/item=279910) · *quest: Mapping the Way Forward*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Ancient Bone Bow](https://www.wowhead.com/forever/item=18680) · *Instructor Malicia, Scholomance*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElU9M82Qcx/t72rW//dS593nZu67xT13Mm71NurSVvvw5uMHJeDDEkydcYYOOMLZsM8GTkHAwBGXRiyAJJGhEInfiwQORiBfBmIhBjATxz4EDVzwYs24L/ok3Fr+H5unzbdNPP8/TlBIIUVBBhxTkwIcKzAFsAGwB8EeDijWrftCOw4hRUXuNZDz11YtHSMQvRknEz3yScc1Xv5ZJwfMGqD9FSMb3J9UfIqTgzjKoP0ZIwu92gGT8Nd+8U8blUmv28waQhAuXURLxrRJJ+HEDSMFfFu+olxESSMF3l0H9/m7yfvSgmLpYh0VgC8VVCG96n3inQ+sfwjYoS8WP1uDt4hksFIcxYIYsfMruuZZjWpb7nOs6vZbtOrbl2qZ7wKQjhufsRKEeQk0mCY/2IYkkk2TaVo1i7dmtTUiGSaGQ6aTdGp8HPupVpl8tV+q6YzkPTdsyrd5Bfdz3ZiYLeb1c1b18vpDXx17X635Br5brXr1YntFrBa867uupWqGgl0pm1SvmzU5ptsr0VK0880B7mmLGXQzx0B5jGNICJCvt1jo4PKwpWohEPCzzRvdx0vQsT9JjJzKRhMfXL3EWleiO8TjKnL0oaAqFSLStFl2zljQ2KPA3/sFlDZhO361yPUk9BkexoyngsNJ2YObnONe1p/7LY/OKb3r4V/9yZ9+2u2ka4zlKGHEUOU41DR3ugxZsJyvd59ZINe6hzMPb0F7bzmu4FDdiKHPchhbtTRE1Im31MknEHrbMH+4Dn+r6Xmh9EtfvAd/ovrznqZc7gby/GQrW0Uk7brC8f1UUIpHADhD35kZU8Td2AFfMmReFIKnsIiQoTjFcfQeivy+BKj8Qglxlcpj8g4WbY2FuIptYXWnmy8wzE0G+zThnTJX0jLHLhP8l9Wxn1NXc3+nacwaC48sfZIfaE9kcvAmwAsGJcJYxRNyNDz9x8yOyoB+y8AKMwCvgQwVmYZb9OQDS6F7G); Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElU1oI2UYx+d5ZzLz5FGT8d1mMxn8GIMs2YEJM2Nnvw4muyfxIIsnT5rZTXaTsmlCkkN7soUepLS29tRWsYVaLMWCoEIRvFQKFcRGCiqtYtEKCj30aBVEZpJQP/DW4P8wvPP832H+83ue4aUUggoaGJCBApShDmMAywBrAPzh0GKBdQ30gyiiKuqjpOAnH8W1o4dIxA9GSMK9z1VS8O22qn0pk4KffhjXfoyRjG/e176LkYIbM6B9HyMJv9kAUvD9OQgelnGm2inPt1WScPpYJRGnqyThL7PBvt9X49pxjARS8Nc3QDu4kL6k7lQyR0swCWyisgjRFf89/9ubS6uwDspU5d234PXKIUxUbmGYG/LwMbvo2a5l294znucO2o7nOrbnWN4Ok9oMf2D7Cg0Q6jJJ2N6GNJJMkuXYTUp0q2srkI6SQhHLzXpNPg78Zb/+4JVavWW4tnvFcmzLHrxh3C37w/dLRaPWMPxisVQ07owarXLJaNRafqtSGzaaJb9xt2xkmqWSUa1aDb9StHqm1TGzQ83a8GX9SUqYFzDCI1uMYUQPI9lZr9mLw6O6okdIxN0an+1/nCw9zdP0yL5MJOHXpy9wpkr0qBlHmbPnBV2hCImO3UkX2JLObgj81X/ksq9b7tVzzfU4DZgcxR6mMIeddUIyPyW5oT/xXxyDHXsD/It/sXPOm90DusMLlDKTKHIcCgjtboMejpOdveo1STMvosyj69Dtbe8zPEqaCZQ5rkMn7ZmhmrEuepkkYlc65He3gQ/1fRY6v8TpPPDl/sN7lga5G8L7G6Gwj27W9cL2/hVRhEQCJ4y4NXZbE39mO3DC3HFRCJXJT0KKkpTAxTlQf5sCTb4shDrJFTD9B4sGa2HsXj61uBDos9xT90J9lXMPmSYZOXOTCf+LWvneqq+6tNG391wPry++k7/ZLeQL8BrAAoQ3wmHOFHEzeeuxs8PIhmuQh+fgNrwEZajDCIywPwcA4PphJA==); Raid BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElV1o62QYx/O8SZOnj9rG96ynafAjFjn0BFKSnJPzdWG7XYkXMrzySputne3Y1tL2YoLgNnYhY7oxUNwYbDCnc7o7hSEIMhlMGG4yUJhfQyd44cVupyCStGV+4N3K+V+EJ8//Dfnn97zhpRSCChoYkIEClKEGEwCrABsA/MHQYoF1B/QfooiqqL9CCn76cVw7fYAkPJ0DkvBoXyUFP5sH7SuZFPz8o7j2c4wU/GAKtO+DYmsOtB9jJOH+MpCC705B8LiCa1Pt/luHKkm48yaQiK+PkoTvzwcL/1iPa7/FSCAFFxdA+/ZK+pq6V8mcrsAMsOnKEkTX/A/973pX1mETlNnKe8vwRuUEpit9GEaHPHzCrnq2a9m2d8P1XM92PPeG7TmWt8ekQ4Y/sWOFegh1mSQ83IU0kkyS5dgNSrS7G2uQjpJCEcvNeg0+CfwFvzbyYrXWNFzbvWU5tmXfvGcMlv2xl0pFo1o3/GKxVDQGXjaa5ZJRrzb9ZqU6ZjRKfn2wbGQapZIxOmrV/UrR6phWy8wON6pj1/XHKWFewQiP7DCGET2MZGe9RicOj+qKHiERD6p8vvtxsvQkT9NDxzKRhN+cP8uZKtHDZhxlzp4RdIUiJDp2K11gSzq7J/BX/5XLvmu5ty8116PUY3IUO5jCHHbWCcn8kuSG/tj/cQxWHPXwL//DzrlsdiM0wAuUMpMochwOCB3sgh5uJzt722uQZl5FmUc3oT3bzmd4lDQTKHPchFbaC0M1Y230MknEbrXIH+wCH+76Xmj9EudvA1/tPryn6CZ3Q3j/IBTO0c26XjjevyOKkEjghBF3Jvo18Ve2B2fMnRSFUJn8DKQoSQlcWgD191nQ5OtCqLNcAdN/smhQCxND+dTSYqAvck8Mhfo6554wTTJy5jYT7oua+U7VVV3b6tp77obX597J97Yb+QK8BrAI4Y1wkjNF3E72PXJxHtlwB/LwNPTD81CGGozDOPtrANWdYJc=).

## Other builds of this spec

- [Marksmanship with Beast Mastery support](../research/raid/builds/bm-mm-full-buffs-raid.md) (21/30/0, 931 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005050001-005155000150305--12)
- [Marksmanship (optimized, lone wolf)](../research/raid/builds/opt-mm-lonewolf-raid-raid-dps.md) (7/41/3, 917 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/50002-3053552011523051-3-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

