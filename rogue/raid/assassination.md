# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**✅ Recommended** for raid (the best rogue spec here, or within 3% of it).

**[Assassination — Raid](../research/raid/builds/assassination-open-raid.md)** (31/19/1) — [open the talent tree](https://talentsforever.com/rogue/60/00530320250151031-30331300020103-001-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target (timing: see below)
2. **Vanish** (timing: see below); no global cooldown, so press it alongside the others
3. **Shank** (timing: see below)
4. **Eviscerate** (rank 8) when you have 3 or more combo points (timing: see below)
5. **Mutilate** (timing: see below)

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Assassination in a raid is a Mutilate rotation: **Mutilate** builds combo points two at a time, **Slice and Dice** stays up, and every 3 or more points go into **Eviscerate**. **Shank** goes on cooldown to keep **Venom** going, and **Vanish** opens one **Garrote** early in the fight.

**Why it works**

- **Slice and Dice** is 30% more attack speed: more white hits (35% of your damage in a full raid) and more chances for your poisons, which can proc on every weapon strike. Put it back up the moment it drops, even with 1 combo point; the list never refreshes it early.
- **Eviscerate** goes at 3 or more points: **Mutilate** brings 2 at once, **Seal Fate** adds a third when it crits (**Puncturing Wounds** gives **Mutilate** 15% more crit chance), and **Ruthlessness** adds a point after 60% of your finishers, so waiting for 5 wastes points. The rotation search measured 3 or more 0.6% better than 5.
- Each **Eviscerate** pays for itself: **Flawless Execution** cuts its cost from 35 to 20 energy, and **Relentless Strikes** gives each combo point a 20% chance to restore 25 energy. In the simulator these are the build's two most valuable talents (removing **Relentless Strikes** costs 12% of its damage, **Flawless Execution** 8%). **Coup de Grace** and **Aggression** add 20% and 15% to **Eviscerate**, about a quarter of your damage.
- **Mutilate** is your builder and filler: 60 energy, both weapons, 2 combo points, 20% more damage against a poisoned target; about 36 a fight and 20% of your damage. Its tooltip, unlike **Backstab**'s, does not ask you to stand behind the target. **Malice** and **Lethality** make its crits more frequent and bigger, and every crit feeds **Seal Fate**.
- **Shank** goes on its 10-second cooldown at 80 energy or less: it costs 5 energy, gives back 25, and with **Venom** raises your poison damage by 30% and your chance to apply poisons by 20% for 6 seconds (removing **Venom** costs 7%). Poisons are 18% of your damage in a full raid: **Instant Poison** on the main hand, **Deadly Poison** on the off hand, with **Vile Poisons** adding 20% to their damage and **Improved Poisons** 2% to their chance to land.

**Caveats**

- **Garrote** is on the list, but it only works from stealth: the simulator presses **Vanish** a second into the fight and opens a **Garrote** right after, once a fight (**Vanish** has a 5-minute cooldown; that **Garrote** is under 1% of your damage). Starting the fight in **Stealth** was not simulated.
- There is no **Expose Armor** in the list: in a full raid a warrior keeps Sunder Armor on the boss, and the two do not stack (only the stronger one counts).
- The list ends with **Backstab**, but this build never casts it: **Mutilate** is the builder whenever you have under 5 points. Blizzard built Forever's Assassination around **Mutilate** and **Venom**, and the simulator agrees: our hand-made Seal Fate **Backstab** build (28/21/2) did 687 DPS in a full raid against this build's 813.
- Poisons now go on a weapon together with a sharpening stone (Blizzard's rogue deep dive, 2026-10-07), so use both.

**When to change it**

- In the last 6 seconds, start no **Slice and Dice**: keep putting 3 or more points into **Eviscerate** even with it down.
- If no warrior keeps Sunder Armor on the target (a small group or a dungeon), keep **Expose Armor** up. The simulator's list has a switch for it, off in a raid: at 5 points, renew it when it has 16 seconds or less left, before any other finisher. An earlier search on the training dummy, where nothing else lowers armor, measured about 9% from it.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Assassination | 31 | Malice 5, Ruthlessness 3, Improved Slice and Dice 3, Vigor 2, Lethality 2, Vile Poisons 5, Improved Poisons 1, Relentless Strikes 5, Venom 1, Seal Fate 3, Mutilate 1 |
| Combat | 19 | Coup de Grace 3, Lightning Reflexes 3, Puncturing Wounds 3, Deflection 1, Precision 3, Composure 2, Flawless Execution 1, Aggression 3 |
| Subtlety | 1 | Opportunity 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 833 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 825 | [31/19/1](https://talentsforever.com/rogue/60/00530311230351031-31131301020103-001-12) |
| Phase 1 BiS | 835 | [31/19/1](https://talentsforever.com/rogue/60/00530311220451031-31131301020103-001-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.6; Phase 1 BiS 62.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Black Amnesty](https://www.wowhead.com/forever/item=19166) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [The Thunderwood Poker](https://www.wowhead.com/forever/item=22377) · *quest: The Perfect Poison*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Heartseeker](https://www.wowhead.com/forever/item=12783) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzUWH1sVFkV73kznbk9LWV6+zW95eN2YKEMTnnz2iJQkH7Bbre4lO0iY6JZXttXZuj0vfreKx+blVQMxogri6ySbWJC2K6sqGRThSUkEg0roMFEUUlMUJFls6xZ46ZxMRmJmPfmTXm00+lqQNf3R3vvPeeec++55+N3BucRCEAQONTCdojDEIwAfBngGMBrALTIpgoWdRWwS2EiBLxsH/rJbw+UBG8VopfcOgToJb++EkA/ufAqBH/lswY/nBt8qxj95NIhCP7eGly5Egj+sRi95OAvA+gj14at3X5yaT+klw8cscScfxXQQ058Br3k3RcB/eQP34Dge8XoI3/ttf57yZFDEKoLXE7U3k6Kd5u6rn0NYn/b/nUQ7jaNAnlF/p58veWb3SdB+Gridbix4Sy8dxxaiX0JaIZzwmJRbKwX66NRSRIbGqNifTRSH43WR+vFqCiJUbE+IorRy4L3pnChFkvQz/LRQ04nQz70ohCpR+osvaOG/JiPnohk4HLkWJ7yUQx0m7Ju8g6Vd5uKnDTjzI/5tV7yjzkOc9SgEbbcYd5qKHzDniHNUHiLPqjpN6EE535STqimnFAdCu1h23Eb3Yos5avEcmvLp2Q1YcR5v6bzdnlQ3qFgRcpXiiUWrWWwZ9iI881DiqrouDDlm4esbVjXFdXkXVpCNQ2eVAyDm3FZ5Y32RQ7EqME+h3HajywUnFFWLv2z6cHCUAH6JUvbaMxWOhqj54C9AfhdoK/BA3Sk4QDxUeG5PEYmPM7aIzvZfcHdajvfKCeTvGNwMKEqqomBcLF1kDV5zH78qGG/pkB+Uky/A+zbgKNAj8L08x6IfaTOOp9VI6UBLA4VIR6HzLr9Du+qdAlbjIwFsSiESK56rdXTSSTjkB5ZdyfXjwEVWR1W0nIkxx0KFlz1OkSpFEmGcTJkaIAVI46DHz3kTkMQ1uTReYzdhEos36Aq+o69vEvTkgl1B2+LK70DBt3HnkedDeE62uRESKummbxTTfQrvFPVdqv2k3ipZz/kWUoQ6p0Vy1vsi68ScQWNYFWoMrcI1wb74C8c2UI72OP4Cbp2Kkej6L4FzgkVZm5+dGKTe3r9GFinImcGqMJ6cRN9MmOsMwMYpBUuPiw4Dpmhi2IJdCjW0KU2i4XPDNC1bA0uojUuNbPstqRO7l7MQhgMVxAfJSed/YygD73RutWDGXa6nC1zXPNxVRtU+IZhXRmQeYR3x7XhZB9vkw3TZh6b2GQ70zzGpjiTc5LTySAwLwpBRn8B7OeAPwb6I8Dn2XP4GF001ezRRpwbmoOFNwlBXy2Qt091YZSuyJhqbGLT1B1SY5aVBXRellUiWTLOf9CF61iTTfc84FXpnOIk5wjfpO3m7cO6bCY0FQvHgaSvG7TfO3C3iVazqum+6dQJytkCLKPUidH7DA3MOQQ9CewE4LeAjoJtvslL335xy/3JvRHAMjZdTr0rfx6MYXWoCitTvjKkGxM74iZv6dGGTW5qfIPah8tCS/GxlC+EmcoT4V26ssvKjpvNuKLzjQkrhyq68aD1/35vs6WMHIzRV4AdA3wJ6GHApSnfYgy1mFzTeauS1HZzKzW1JRNDQ1ZgPxPXFSOuJftwQcpXjVUtPdouxWaxU7GL/pAO7WS9Ow30BWBfARwBus+2F7jslTuTTkvnY7F/22ppDzma8RDyJ5X+RaAJeSj5rDZkckmUVkai0Yi4eg3vjcvqDqXPMqDc16f08Z693IwrXNdM2924och6b5zXGorCZcOQDSOh2pSILif6Ihm+SJqvbqehqcvYPcAPgE4A/gDY65kSZVvAxiFSXSPW0IXTLNOAhVe91oN7yPtvdeITdON0p8WKcBnxUnLOThl3bCdGYaWR06gRujyL2z50L337VJdt77EY3cni+Cz97OxVdRGrQX8oHz0pT55z/vaEbu7l7YrSZzhFozxcSrzUv9OBMPaVGwxb10WNbmNbsZN2YEnKV4xFFhJplXsHDFPuwdJQCc4dhyL0knsjQIVAfhBmPZNlUpv9ksDeFPCcQN8Q3I516vCWIGTTNutlLwK7ADlfqo224KJwDcm382XVuFBBgDqRcKchExOHYzmFhEJ81ojnKd98rO5QebsVADrX+rkDC9pkO3s4YCl7Ek4nnikVqaXXTOxSrFB6SjP504rct9d+osMxekJgYwIeFehLwuxWugTszdxWaqetuDgccqzExoXKB6xUMOGxntCKof8TM00GPX1HYLcE/J1ArwlYHir9j9zsYRnw3khuKR8dA+IyttTOEr4pWWKVkQbeN4lVmoBc1Caje/i/WRHS+Pw3P4WgJ7xuepsZZrXOs07awYXv0gjdjqXz28LPzATgm9hqR8jMUFGqwDI9g2EmIdlqUZo/vXumBejH/H45aShS1YM+6CbNn95Ku8k1MzRc1Ma6pj6sSAuy9JVuERxLu/SExruTiV6Fy2ofb0/0Km6OulzxQKcCzEapI4s70wYqZa+ukoHBlK886ymkpVg6RXXC4CKdWttFqTNHmNA69rFpFTqaQ+vaDwP7aNbbiIa0ImdE0ine8fFGaUk2nEAdYP+kw7fSkJQZApla3Vj2n10wylZgIFSMReNQYHu4VaaxOlxFvLTonGvNQpfoia40pKdyxQkVaV020DlzmpE+PTvSoY20fqYb5BL9+Q+TvmwI42plre7K3eek29x0b2nRaukS97QqXEm8ri6y4LjfIUlfhFzZgCq0163TJbOTdbjbyDMDmYb2zEAQbI35WTXaYNdjO8UkWdo2/YcA2sZaMsgxn3zp8GSj5XVPPO6J4J6ANZEWZkGL1En2Atmv3hYuw/uC9AVPnv2VNf8ZvChgXuifQoG1kDfS31w1+rL1/Wx9Tb/9XVsv3RCCXr4+fFbI+598ZnNm9Ei/Jd9/ZHpW23+fHmtucRaat1s/ar8M9iTvxvqwh5ytbHX99i3CKmiGJ6ALYhCHIdgDe4R/DQBr716t).

**Points that do nothing for this spec:** **Composure** (2) only counts toward the points the tree needs before **Aggression** and **Flawless Execution**.

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

