# Beast-Marks Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Beast-Marks

*Beast Mastery's pet talents with Marksmanship's shot talents (Mortal Shots, Improved Arcane Shot, Careful Aim): a pet build short of 30 Beast Mastery points.* (a hybrid: Beast Mastery/Marksmanship).

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Beast-Marks — Raid](../research/raid/builds/beast-marks-ml-raid.md)** (28/21/2) — [open the talent tree](https://talentsforever.com/hunter/60/532000150510123-00530503005-2-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Summon Hawk), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** The spec's best build for each other setup, in a full raid:

- With a pet: [Beast Mastery / Marksmanship](../research/raid/builds/bm-mm-raid.md) (22/29/0, 879 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005041002-005355010150004--12)

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

- **Serpent Sting** first so it never drops, 20% stronger with **Improved Stings**. Recast it only as it runs out (a new sting replaces the old one), and the full rotation does so only while you have 30% mana or more.
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

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 28 | Deadly Aspects 5, Endurance Training 3, Focused Fire 2, Bestial Swiftness 1, Unleashed Fury 5, Ferocity 5, Summon Hawk 1, Intimidation 1, Bestial Discipline 2, Frenzy 3 |
| Marksmanship | 21 | Lethal Attacks 5, Improved Stings 3, Careful Aim 5, Improved Arcane Shot 3, Mortal Shots 5 |
| Survival | 2 | Improved Tracking 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 957 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 941 | [28/22/1](https://talentsforever.com/hunter/60/512210150501023-00530504005-1-12) |
| Phase 1 BiS | 980 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.9; Phase 1 BiS 63.2; each item opens its Wowhead page, with where it drops and its enchant):

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
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gorewood Bow](https://www.wowhead.com/forever/item=16996) · *quest: The Scarlet Oracle, Demetria*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVEFIFG0Y3veb2Z1v3///dfjUf8ehYtpA1oVZvhkdUSN29dQppFOncnTXdqTcZXcPeghMDEIkqEOoCAabZVK3BAkiMCSDBTeEgjKSMvDQwWsFETPuQmRHpefw8sz7MPM873wfLx6hIIMCGkSgF9KQhVGA6wB3ABYA2L+eSly1HdQdiVJZUK+gRJ8u1Srb/6BIi1OAIt0oySjR5/OgvAq45HGt8qkGJfpgDJT3LimVZOVDDYq0NAso0Xtj4L4u0RdjsNefKsso0ttevfnMrUtl95vf52uVLzXoQ4luj4Pyri7cJK85ke05mAAy7sxAsGg/tDe75uZhEaRJ5/4s3HC2YNzppl52SMATctQyTNPghsUtbnCzRefcauEWb+Xc0o01IpYJ/Ug2/ViPVA2gSMurEKYYQFE3eB4bKt2FIoSDKKFfN2NWnl0Ddt7OXrqQyRY0k5ttusF1o61T60/bQxdTSS2T0+xkMpXU+ka0Qjql5TIFu+BkhrR8ys71p7VIPpXS+i7rOdtJ6lVR3xNjg/nMULN6AhujISowOuimWl8F1fPnMdPKq5UWE1XS6WPO/jC840DDSKofBbqeYSN/mLv1QK1C+N/bAKJIV0Z7GJFFb1aXn1JPosk41kcZFZh/hRDqVyX0o8BjBirR/6nAgotQOa2qYnnJP4fY4G/JeYduth9o8r2b8ubrmX1eBte5eQheC0VgmnoMG6J11F/9Jd7l5TEr702+Ua8IO2QNdol5VfB5iCQmoBFD2EBnboH8bRKUQLPPw268l4Z/kKDLfaMDicaZaRcv48cHPLyOm1tEEbV4dJn4/goKiSo7VDQ9OjSfDq+evZvoqjQSve7WnQbvwbcVjwp0OdT9y3Lm0A4JOA09cA7SkIVhGCY/BwCJjy50); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzEVFFIFFsY3v/M7M7Z/96rw1HvjsO9MW0g68IsZ2YbUSN29amnkJ56Kkd3bUfKXXb3QR8CE4MQKRKClMDAtkzqLUGCCgzJQHBDKEgjKQMfevC1gogZdyGyR6Xv4fDN9zHn+/6Zw8H/KMiggAYR6IYM5GAY4ArAbYBZAPa35xLXbQV1W6JUFtSLKNEn87XK1l8o0q1rgCJdW5FRos9LoLwKuORRrfKxBiV6fwSUdy5ZWZGV9zUo0vUbgBK9OwLu6xJ9MQK7+tOSu8/Nsowivf7MXefL7p7fSrXK5xr0oUQnJ0BZrws3yctOZGsaxoCMOlMQnLEf2Bsd0yWYA2ncuXcLrjqbMOp0Uq87JOEx+d+Km5xzw+KWwQ0zrnNuxbnF45xburlMxDKhH8iGH+uRqgEUaXkJwhQDKOoGL2BDRZ2dgXAQJfTrZswqsMvAzti582ezuaJmcrNFN7hutLRrvRl74Fw6pWXzmp1KpVNaz5BWzKS1fLZoF53sgFZI2/nejBYppNNazwU9bzspvWrqu2asv5AdaFaPYGM0RAVG+91Wq0ugevk8ZloFtSIxUSXtPubsLcPb9rWMpPpRoKtZNvSbuY/ua1QI/3kbQBTp4nAXI7Lozery4+oxNBnH+iijAvMvEkL9qoR+FHjMQCX6LxVYcA4qf6vqWF7zTyHW/0tz3qabrfvafPekvPlyck+WwXVuHkDW7AwwTT2EDdE66q9+Eu/w8phV8CZfq1eEbbIMO8S8JPg8RJJj0IghbKBTEyB/HQcl0OzzsJPopuHvJOhy33BfsnFq0sXLxOE+D68T5iZRRC0RXSC+P4JissoOFE0PDyynzVtP3Ul2VIRkt3vrToL34NtMRAW6EOr86XLm0ApJOAFdcBoykINBGCQ/BgBUkS5l).

**Points that do nothing for this spec:** **Intimidation** (1) only counts toward the points the tree needs before **Frenzy**.

## Other builds of this spec

- [Marksmanship — Summon Hawk](../research/raid/builds/mm-hawk-raid.md) (22/29/0, 894 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005051001-105355000150004--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

