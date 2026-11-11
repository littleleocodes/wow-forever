# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Beast Mastery's pet talents with Marksmanship's shot talents (Mortal Shots, Improved Arcane Shot, Careful Aim): a pet build short of 30 Beast Mastery points.* (a hybrid: Beast Mastery/Marksmanship).

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (28/21/2) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-00530503005-2-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Summon Hawk), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 917 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--12)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 998 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 941 | [28/22/1](https://talentsforever.com/hunter/60/512210150501023-00530504005-1-12) |
| Phase 1 BiS | 980 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Beaststalker's Bindings](https://www.wowhead.com/forever/item=16681) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Beaststalker's Bindings](https://www.wowhead.com/forever/item=16681) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) · *sold by Samuel Hawke* | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gorewood Bow](https://www.wowhead.com/forever/item=16996) · *quest: The Scarlet Oracle, Demetria*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIG2kYzffPJPPl210dRt2Mw+4ymwWJgQn/jI6oy5LoaU+L7GlPu44mbkZWE5IcFPbgigtFbCk9FBXBQmprpb21IIVeLFILAVOEFlpLpbW0hR68toVSZkyg1B6VvsPw5r0Z3vtmfj76DkEGFXSIwSBkIQ9TAKcALgCsAihf+y7z3G7QXkiIsqD9SxLeutGo7n9FIpbngUTcqcgk4e0VUO+FPHK9UX3WQBJemQb1sUcqFVl90kAiVpaAJLw0Dd7rEt6ZhkN9viqTiOerMgl4eoxEfHXWe/DdSqP6uoECJOH+DKiPmqJt8pYb21+GWWAz7iKEy85VZ7dveQXWQJpzLy/BGXcPZtx+9KtDCm6y723Tskxu2tzmJrc6DM7tDm7zTs5tw9xiYpXhU7YbpGZCLUQiVjchihQi0TB5kVpq6moZomGSKGhYCbuo/A/Kn07+n79y+ZJucavLMLlhdvXqw1ln/O9MWs8VdCedzqT1oUm9lM3ohVzJKbm5cb2YcQrDWT1WzGT0oTGj4Lhpo24ah2ZitJgbb9d+otZ4BAUFR71W25ug+fk8YdlFrSYposZ6A4p7tAzvOdYykhYkAbdzyuRn5u481qgIffMwRCTixtSAwmTRn9Xjv2g/k6Vwao4rKCjBDcYwqEkUJIEnTFLj36KghNeg9rfqju03fx5RRj9pznsMq/tYmx+elAdvfjuSZXKDWyeQtVoGRdd+oJZ4Ewbrn8Q/vDxhF/3Jd5pV4SXbggNm/ScEfMRSs9BKEWrBxXMgv50DNdQe8HGQHMToexb2eGBqJNW6uODhbvLHER/3k9YeU0U9GV9ngS+CUqrOThRt104sp8e//n4x1VcTUoPe0l0A/yawl4wLuB7p/2g3c+iGFPwKA/AHZCEPEzDBPgwAwGQt8A==); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVE9IG2kcze+bSeaX3+7qMOpmHHaX2SxIDEz4ZrIj6rIketrTInva066jiZuR1YQkB4UerFgoYv8gFKoULNi0VtpbC1JoDxapBUGL0EK1VFpLW+jBa1soZcYESu1R6TsMb96bmfd+83189AOCDCroEINeyEEBxgBOAlwEWABQvvVd5rntoL2UEGVBO0YS3r5Zr+5+QyLungEScXNNJgnvVkB9EPLIjXr1eR1JeHUc1CceWVuT1ad1JOLWOSAJL4+D97qE98ZhX79T8b5zfkMmAU8NkYivz3oPvq/Uq2/qKEASzkyDutUQbZFX3djuHEwCm3BnITzvXHO2u+YqsAjSlHvlApx2d2DC7Ua/OqThFvvRTlqcc9PmtslNK2lwbie5zZOc24a1ysQNhs/YdpAaCbUQibixAlGkEImGyUvUVFUX5iEaJomChpWwS8oJUP5xCv//my+UdYtbbYbJDbOtU+/POcP/ZTN6vqg7mUw2o/eN6uVcVi/my07ZzQ/rpaxT7M/psVI2q/cNGUXHzRg109g3E4Ol/HCr9gs1xyMoKDjotVpfAc3P5wnLLmlVSRE11hlQ3INleMehlpG0IAm4nldGvzD3r4caFaHvHoeIRFwe61GYLPqzevx37TeyFE6NcQUFJbjMGAY1iYIk8IRJavx7FJTwIlRXq+bYfvMXEWXws+a8w7DaD7X5/k559PbPA1kmN7h1BFkL86Do2k/UFG/AYO2X+JuXJ+ySP/lmoyq8Yquwx6zjQsBHLD0JzRShJpydBvndFKih1oCPvVQvRj+wsMcDYwPp5tkZD/dTPw/4eJiydpgq6qn4Egt8FZTTNXakaLl+ZDkd/vWvS+muqpDu9Q7dGfBvAjupuIBLke5PzmYO7ZCGP6AH/oYcFGAERtjHAQCLOC3h).

**Points that do nothing for this spec:** **Intimidation** (1) only counts toward the points the tree needs before **Frenzy**.

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 931 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

