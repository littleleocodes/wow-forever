# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Beast Mastery's pet talents with Marksmanship's shot talents (Mortal Shots, Improved Arcane Shot, Careful Aim): a pet build short of 30 Beast Mastery points.* (a hybrid: Beast Mastery/Marksmanship).

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (28/21/2) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-00530503005-2-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Summon Hawk), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 910 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--12)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 992 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 970 | [28/22/1](https://talentsforever.com/hunter/60/542100150500023-00530504005-1-12) |
| Phase 1 BiS | 1015 | [28/20/3](https://talentsforever.com/hunter/60/532001150510023-00530502005-3-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Leggings of Destruction](https://www.wowhead.com/forever/item=18524) · *King Gordok, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Leggings of Destruction](https://www.wowhead.com/forever/item=18524) · *King Gordok, Dire Maul*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIG2kYzffPJPPl2904jLoZh91lNgsSAxP+GR1RlyXR054W2dOeto4mmpFqQpKD3ixYKKJV2ku1BQtWKlJPbUEKvVgEC4IWoS2tpdJaaMGD17ZQyowJlNqj0ncY3rw3w3vfzM9HvyDIoIIOceiBHBRgDOACwHWAJQDlR99lntsG2r6EKAvaKEl4/26Nuv8DCXh7hETc2ZRJwgeLoD4KeeROjfo6QiG8OqC+iJCEm5uy+jJCIj5dAZJwdwa8l0M4PXQkX9mWScSpA5kEnBoiEd/NeM99XKxRDyIUIAkvT4P6vDbWKG+48f15mAA27s5BeMG55ex2zi/CMkiT7s1rcNHdg3G3C/3ekIZ77Fe7xTI5N21uc86tZoNzu5nbvIVz2zA3mLjN8BXbDVIdoRYiEbfXIYYUItEweYnqK+rSAsTCJFHQsJJ2STkPyv9O4eyZfKGsW9xqNUxumK0del/OGR7IZvR8UXcymWxG7x3Vy7msXsyXnbKbH9ZLWafYl9PjpWxW7x0yio6bMaqmcWQmB0v54SbtD2pIRFFQcNBrtbUOmp/Pk5Zd0iqSImqsI6C4x8vw9hMtI2lBEnArr4x+Y+6WE42K0k/PQkQiro11K0wW/Vk9/pf2J1kKp7qEgoISXGMMg5pEQRJ40iQ18TMKSngZKn+r6th+8zdRZfCr5rzdsNpOtPnRSXny/p9jWSY3uHUKWUsLoOjab1SfqMVg9ZP4h5cn7ZI/+U6dKrxlG3DIrHNCwEc8PQENFKV6nLsE8odJUENNAR+HqR6MfWJhjwfG+tMNc7MeHqZ+7/fxOGXtMVXUU4lVFvguKKer7FTRuHJqOe3+9d8b6c6KkO7xNu4s+DeBvVRCwNVo1xeLmUMbpOFv6Ib/IAcFGIER9nkAfuctjA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVFFIFGsY3e+f2Z1vv3uvLqPeHYd7L3P3gqwLs/wze0fUiF196imkp57K0V3bkXSX3X1QejFQCLEUe1ICA1sSybcCCerBkAwEDaGijKQsCnrwtYKIGXchskel8zCcOWdmzvnm//npL4QQKKBBFLohC3kYAbgEcB1gAUD+3XOZ67aC+k5CDAnqBZLw3p1aZfc3EnF3EkjErfUQSfigDMrjgEtu1ypvakjCh5OgvHTJ+npIeVVDIj5bApJwewrc1wM4ObAv3y+7nxm7CiTg5QES8cOU+9yXcq3ysYZ8JOHMNCgv6iJNoTUnujsH48BGnVkIztu37O2OuTIsgjTh3LwGV5wdGHU60WsOKbjL/rYSJueGYXHL4NxM6JxbCW5xk3NLT6wxcZPha7btp3pCNUAibq5CBClAom7wIjVU1IV5iARJIr9uxq2iPAbyGTt//mwuX9JMbrboBteNlnatN2sPnsuktVxBs9PpTFrrGdZK2YxWyJXskpMb1IoZu9Cb1aLFTEbrGdALtpPWq6a+b8b7i7nBZvU/aoyFUZCx3221sQqql8/jplVUK5IsqqzdJzsHy/C2Qy0jqX4ScCMnD/9k7v8PNSpMfzwPEIm4MtIls5Dozery4+oxMmVO9TEZBdm/whj6VYn8JPC4QUrsTxTk4CJUVqvqWF7zt2G5/4fmvE03Ww+1+f5Oefrp5IEsg+vcPIKshXmQNfUfaojVob/6S7zNy+NW0Zt8q14R3rM12GPmRcHnIZoah0YKUwPOTkPo8wQogWafh71kN0a+sqDLfSN9qcbZGRePkv/2eXiSNHeYImrJ2DLz/RKUUlV2pGhaOrKcNu966kaqoyKkut0zdwa8G99OMibgcrjzu6OZQyuk4AR0wWnIQh6GYIh9GwCW6i21).

**Points that do nothing for this spec:** **Intimidation** (1) only counts toward the points the tree needs before **Frenzy**.

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 927 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

