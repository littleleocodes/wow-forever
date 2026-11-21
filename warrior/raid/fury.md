# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md)** (17/32/2) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (20/31/0, 921 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

## How to play

**Setup, before the pull:** **Berserker Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst** until the last 30 seconds of the fight
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Reckless Swings**
4. **Whirlwind**
5. **Execute** when the target is below 20% health
6. **Hamstring** when **Bloodthirst** is more than 1.1 seconds from ready and **Whirlwind** is more than 2 seconds from ready
7. **Bloodrage** when you have less than 23 rage; no global cooldown, so press it alongside the others
8. **Heroic Strike** (rank 8) when you have 68+ rage; no global cooldown, so press it alongside the others

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Berserker Rage**: a cooldown, use it in the last 45 seconds of the fight (about 3 times a fight)
- **Recklessness**: once a fight, in the last 45 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a two-handed weapon: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in every other gap and **Heroic Strike** only at 90 rage or more. **Death Wish** waits for the last 45 seconds and **Recklessness** for the target's last 20%.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 8-second cooldown with **Improved Whirlwind**) are your main attacks: press **Bloodthirst** the moment it is ready, and **Whirlwind** whenever **Bloodthirst** is more than 1.5 seconds away. **Whirlwind** needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them. A full raid gives you the rage for this order; the simulator's rotation for a warrior alone on a training dummy, short of rage, puts **Execute** first.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) waits until 45 seconds are left and **Recklessness** (+100% crit chance for 15 seconds) until the target is below 20%, so both cover the execute phase; **Reckless Swings** (your next 4 melee attacks give 5 more rage) joins them in the last 34 seconds. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) is your filler: cast it whenever nothing else is ready, about 56 times a fight. It is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem; the simulator measured 6.8% more damage casting it freely than only above 80 rage with **Bloodthirst** and **Whirlwind** more than 1.5 seconds away.
- **Heroic Strike** is a rage dump, not a filler: queue it only at 90 rage or more, and not below 20%, where **Execute** wants every point. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**. The simulator measured 5.3% more damage after dropping its default line at 40 rage, and 0.2% more after adding this one at 90.
- **Bloodrage** (1-minute cooldown) goes whenever you are under 90 rage, about twice a fight.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one at the pull, one when its cooldown is back). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 13% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage the full list adds **Cleave**.
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and use **Hamstring** only above 80 rage. That is the simulator's two-handed rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** to 5 was worth 5.8%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** and **Recklessness** also make you immune. The simulator's boss never fears, so the list leaves it out.
- With a weapon in each hand (the page's dual-wield option), the simulator's dual-wield raid rotation differs: **Reckless Swings** on cooldown, **Heroic Strike** from 67.5 rage on a single target, **Hamstring** only when **Bloodthirst** is more than a second away and **Whirlwind** more than 2 seconds, **Recklessness** with **Death Wish** in the last 45 seconds, and no **Bloodthirst** in the last 30 seconds. **Whirlwind** hits with both weapons there.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 17 | Improved Heroic Strike 3, Deflection 2 (tier point: needed to reach Anger Management), Improved Rend 3 (needed for Deep Wounds), Improved Tactical Mastery 3 (needed for Anger Management), Anger Management 1, Deep Wounds 3, Impale 2 |
| Fury | 32 | Cruelty 5, Unbridled Wrath 5, Furious Precision 3, Dual Wield Specialization 5, Reckless Swings 1, Improved Execute 2, Improved Berserker Rage 2, Death Wish 1, Improved Whirlwind 2, Flurry 3, Bloodthirst 1, Blood Craze 2 (tier point: needed to reach Dual Wield Specialization) |
| Protection | 2 | Improved Bloodrage 2 |

A talent marked as a tier point measures nothing in the simulator's raid fight; the build holds it for the tier it opens (or the talent it is needed for).

## The numbers

**How this pick was checked:** a full search on 2026-11-08 (the talent search that found this build).

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 987 |

**By gear tier** (this build in the best set each tier allows, full raid, 5,000 fights; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | In |
|---|---|---|
| Quests and dungeons | 832 | its own set |
| Pre-BiS | 958 | its own set |
| Raid BiS | 988 | its own set |

*Each tier's number is this build in its own tier set, in a lower tier's set, or in the standard set when every item of it is allowed in the tier, whichever is best. The tier sets were chosen for the builds and rotations of before 2026-11-20 and are being made again for this build.*

**The gear** (each tier's own set; average item level: Quests and dungeons 60.2; Pre-BiS 62.4; Raid BiS 63.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Mask of the Unforgiven](https://www.wowhead.com/forever/item=13404) · *The Unforgiven, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Wyrmhide Spaulders](https://www.wowhead.com/forever/item=12082) · *quest: A Taste of Flame* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Slashclaw Bracers](https://www.wowhead.com/forever/item=13211) · *Halycon, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Death Grips](https://www.wowhead.com/forever/item=18722) · *Magistrate Barthilas, Stratholme*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* |
| Legs | [Handcrafted Mastersmith Leggings](https://www.wowhead.com/forever/item=13498) · *Goraluk Anvilcrack, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Tracker's Signet of Ferocity](https://www.wowhead.com/forever/item=275972) | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Blackstone Ring](https://www.wowhead.com/forever/item=17713) · *Princess Theradras, Maraudon* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Tooth of Eranikus](https://www.wowhead.com/forever/item=10837) · *Shade of Eranikus, The Temple of Atal'Hakkar*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Mirah's Song](https://www.wowhead.com/forever/item=15806) · *quest: Kirtonos the Herald*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV19sFNUX3jMzO3v2FPY33MKP6S2YsSE4DG69M7tTKBq7EDX+iRH/JBA02pVd2DXKNjs1QPQBGmIMGkAxRhaSVpTYVBtD4x/SmD5oYlCDkQebaDCSaqKJPPDAEzFi7rDblW0fTNOu92H3zD33zv2+831zJkMrEAwwwQIbeqEAfbAP4GWAIYBhALYozCoyux74lWWoGcB3k44XCuZUC2n40iiQimNPko4nCuZ5nXT89nHzlwTpeHyn+VOCYnjydTAHY6ThNyeAdBwvyp06Hn7O/DlBGh64ZJCGpw/K+7z3BGn48XcG6fj9Y+YleZeJF+S/hkcPQ4dtfFm0fx2EzZOHYOuV3oOgDBQrEH8n+0H2x42Dp2AElFeLl2GguAlD3JCBccVKiZRIeW5KCC/p+cJPCSF81/NcIbyUm/TOKtqUcrWVHQC2Pdv37FOlvn7LE15X0nWTYv0Ga3shu2tnPmeVylY2l8vnrKf3Wv2FvFUu9Wf7i6VdVpDPlrcXLDvI560dz5f3JnO7k+VsMZesrUheX9H5TFDatYavpCXO/1Bnyv0RHqMoqSkRcCTd1nByHFiG30kp5lK704YqS3wOLRS1o3huG1OMKI+SSuAS6zAoMVZNTWwJU7HaujiPyXXGm48y4sh10ozzrwE7PoOfSApv/vmlaS1fE3LU6hzTfkBLHValTYSke67b6QcSKQ73spsQOG/c5Vbzny5mb82Gvnv+0bu0ht/SiCMlAmKOUUWPpJPmpkXANVJMztZxfzbKnphB2U2HlHXS8MIQsJW8vXFTlwikYPjHBDCfp/4tGGkhqfNnp+ayDU/+NqfT9n80522lRjXdpEjPv5qh+/Ho0YfZ+7P4J+XO/4l30R1sA63mq4gqGCPVuLbW4LV4/631eKBocDKchJS2HJE4SXH9qqVebM6juqxRtrQfbIiwvuY8anF5ppXAI4tZK19C0a8VBUF6xY7iJ29DrXnh6eF6fOjPh9gr0JzqrKI2ZzlGWcsITLdnCYgUEdShb+Q95LLbQimjTJ2CSK1Jt/O2cFavC5wWNZpEaIEdxR+GgI026c1zD93Oumml095IKuzHbqfr+QGZzv8xymgEagyvI/dCyraK57rZQCNe0Z30FgBve9hC1LB8YZ/zvE5fVhevLWX3IfC7Q0LyTdlAKFwtey1xx2ygM52TxPCLI8BOQHMM75PNVoeWgBuMUm2UNZZd6zp9HqeYBTbih9vYQJPsMaPcXevq5Z6A5nTsLfQgeyDsoVI5ncVHQMokXRqvxKohrXA46jeoSpVYLaaWKZTeBnxjCKZFXs6X0aIOIhwD6aBKa8is0mqqvytn4bKS269GwrE0M6K0UJxiqNogrkLHX0pczkf27ci0VY7J8VXPzTvCMdnjXVRMzepxziiR/2T0Z2rRgo7Vowt2Tnf4+8i7mY3ViUyv/AI5BuFF5GKPo+KZ5Zv+8aEiYD1k4F7YDFuhAH2wB/Yofw8At3nEzA==); Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHNUX3zMzO3P2pN1Obtp/JzftnzGUOp268c7sTtpUMdui4gdi1YeWIphtd2tWpBt2Irag0AaF4ketRKRdxcaPYom2Yq1ai/ShilRpoUUo+IUhCgr2IYJPQazc6W7WbvIgIVnvQzi559y9v9/5/eYMQ8sQTLDABgf6oB8GYDfAXoARgCMAbEGUVWR2LfDJJaiZwJ8kHce2WuMtpOIHO0nDr8+ZZOBrF0zrok4Gfn5ikfVTknTcW7B+SMqNc6Z1yCANhy/Iwt+PgTxs4CdnWq0fk6Th85dN0vDABZNUfPtB0vDDqPC7p1uty/IHJo6BDDQcfgE6HfOLovPzIdh4aR9s/qPvGVCGihVIvJl7N/ft+kOHYRSU54oTMFTcgBF6yMIpxU6LtEj7XloIP+UHIkgLIQLP9z0h/LSX8s8q2rgy2caeArYtN/DoQ6WBQdsXfnfK81Ji7Tp7W39ux8OFvF0q27l8vpC3t+6yB/sLdrk0mBsslnbYYSFX3tZvO2GhYG9/rLwrlX88Vc4V86laRepqRdcjYWnHKr6cWt1FqDPlrhg3KE5qWoQcSXc0vHQKWJbfQmnmUYfbjipLnoEWijtxPL+FKWacx0kl8Ih1mpQ8Xk2d3hSljFpdghuyznz5AUYcuU6aefFFYK9M4ydSwp97fhlazVdFHLU6x0wQ0mKXVWkTIem+53UFoUSKR/rY/xE4bzzlVfMfL2QHZkLfM/foPVrFr2/EkRYhMdesokfSSfMyIuQaKRZna3gwE2VfTKPsZSLKOmn4/Qiw5byj8VC3CKVg+NtpYAFP/1sw0kJS508Pz+YYvvHLrG7bc2LWx0qNanopkZl7NSP34/DwfeydGfyT9ub+xlvpZraOVvIVRBU0SDWvrDZ5Ld5zQz0eKpqcTDcppS3HJE5SvKBqqSea86guaZQtE4TrYmygOY9aQt5pJ3H/QtbGWyn+laIgSK84cfzodagNL3z/SD3e9+e97FloTndWULu7FOOsZRSmxrMERIoI69DX817y2I2RlHGmjkOsNqQ7eHu0q9cFzogaTSK0wYnjNyPAjjbpzXM73cR6aLnb0Ugqmsdel+cHIVnu/zDOaBRqDK8i9yPKjorne9hQI17Rk/LnAW9HNELUqH3RnPP9rkB2F68sZnci8NsiQvJN2UAoqpazlrhrNdCZykli+Nl+YK9CcwwfkMNWRpaAa4xSHZQ1lt1rugKeIMMGB/G9LWyoSfaY1u7uNfV2n4bmTOxNdA+7O5qhUjmdJUZByiRdmqgY1ZCWuRz1a1SlilGLqWUcpbcBXxqBKZGX8iW0oJMIj4N0UKUtYlZps9RflbMwoeT3qLFoLc6OKi2UIANVB8QkdP6lJOR+bPf2bHvloFxf9l63PVqXev0xxdLsXvekEvtP1mC2Fs3rWnl03u7pif7e/1Z2fXUj2ye/Qw5C9E9srNdV8eTSDf/4XBGwFrJwB2yEzdAPA7ATdip/DwAzJcir); Raid BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11sFNUX3zMzO3P2FJbpLfyZ3sI/Y0NwGNx6Z3anUDR2IWr8iBH1AcKLXdjFrlG22akREmOgkYSofJgaIyuR+kFCqmAkqEgMD2gMKiQQExK/IqkkmshDTXxCI+YOu13Z9sE07XofNmfvuR+/3/n95kyGFiGYYIENDvRBPwzAdoBdACMAhwHYnCiryOxK4H8sQM0E/izpeGmjNdZCGl7eC6Th12dNMvD186Z1QScDPzs+z/opSTruKlg/JOXEWdM6aJCGXx0AMvC3oyB3G/jx6VbrxyRpuHNYHrP7ikkq7n6SNPzgvDxx/ChYV+QB3+1slYGGw3uh0zE/LzqXD8Lai3tg/e99z4MyVKxA4q3cu7lvVx88BKOgvFgch6HiGozgQxZOKnbaT4u08NJC+Ck/EEFaCBF4vu8J4ae9lH9G0caUq23sOWCbcgNPPFoaGLR94XenPC8lVq6yN/XntjxWyNulsp3L5wt5e+M2e7C/YJdLg7nBYmmLHRZy5U39thMWCvbmp8rbUvmnU+VcMZ+qrUhdX9H1eFjasowvplZ3HupMuS/GDYqTmhYhR9IdDS+eBJbld1CaedThtqPKkqehheJOHM9tYIoZ53FSCTxinSYlj1VTp9ZFKaO2LsENuc585RFGHLlOmnnhJWCvTeInUsKfeX4ZWs6XRRy1OsdMENJ8l1VpEyHpvud1BaFEiof72P8ROG/c5VXzH81lr06Fvmfm0Xu0jN/ciCMtQmKuWUWPpJPmZUTINVIszlbwYCrKvphE2ctElHXS8PsRYIt5R+OmbhFKwfDXU8ACnv63YKSFpM6fHJrONnzz52ndtuP4tLeVGtX0UiIz82pG7sfh4YfYO1P4J+3N/I130u1sFS3lS4gqaJBqXltu8lq845Z6PFQ0OZluUkpbjkmcpHhB1VLPNOdRXdAoWyYIV8XYQHMetYS8007ivrmsjbdS/EtFQZBeceL44RtQa174/uF6vOfPB9kL0JzqLKF2dyHGWcsoTLRnCYgUEdahr+a95LFbIynjTB2DWK1Jd/D2aFavC5wRNZpEaIMTx29GgB1p0pvnbrqN9dBit6ORVNSPvS7PD0Ky3P9hnNEo1BheR+5HlB0Vz/WwoUa8oiflzwLejqiFqFH5oj7n+12BrC5em8/uReB3RYTkm7KBULRa9lrirtVAZyInieGn+4AdgOYYPiCHLY0sATcYpdooayy7V3QFPEGGDQ7iexvYUJPsManc3Svq5T4FzenY6+gBdn/UQ6VyOkuMgpRJujRRMaohLXI56jeoShWjFlPLGEpvA748AhMiL+QLaE4nER4D6aBKW8Ss0mapvyhnYFzJ71Bj0ZifHVVaKEEGqg6Iq9D5l5KQ87Htm7Ptlf1yfNF70+ZoXOz1LymWZve6J5TYfzIGs7VoVsfSI7N2T0/0+/Db2dXViWyf/BDZD9Gf2KVeV8UTC9f843tFwErIwj2wFtZDPwzAVtiq/D0AdMzIhA==).

**Points that do nothing for this spec:** **Blood Craze** (2) only counts toward the points the tree needs before **Dual Wield Specialization**; **Deflection** (2) only counts toward the points the tree needs before **Anger Management**; **Improved Rend** (3) is needed for **Deep Wounds**; **Improved Tactical Mastery** (3) is needed for **Anger Management**.

## Other builds of this spec

- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (17/34/0, 960 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013002-050530305022120231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/36/2, 914 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530305021100231-002-12)
- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 912 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500303022120231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/31/1, 899 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-552500300020120231-001-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-21 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

