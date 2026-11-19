# Arms Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Arms

**[Arms — Battle Stance](../research/raid/builds/arms-battle-raid.md)** (34/17/0) — [open the talent tree](https://talentsforever.com/warrior/60/05303213132215201-55050000002--12)

> **Signature spells: this build fails the check** in a full raid (core share 79% under 80% (melee, Mortal Strike, Overpower, Slam, Execute, Rend, Whirlwind, Heroic Strike, Deep Wounds); Arms is defined by **Mortal Strike** cast every fight and melee, Mortal Strike, Overpower, Slam, Execute, Rend, Whirlwind, Heroic Strike, Deep Wounds carrying 80% of the damage). It stays on the page until a build of this spec that passes is found; the raid searches since 2026-10-22 look only for such builds (signature_spells.json).

## How to play

**Before the pull, then keep up all fight:** **Battle Stance**.

**Then press the first one that is ready**, top to bottom:

1. **Overpower** when it lights up (after the target dodges)
2. **Slam**
3. **Rend**: keep it on the target
4. **Mortal Strike**
5. **Execute** when the target is below 20% health
6. **Spearing Strike**
7. **Hamstring**
8. **Bloodrage** when you have less than 45 rage; no global cooldown, so press it alongside the others

Between these, your white swings do the rest.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Arms in a raid stays in **Battle Stance** and lives off **Overpower**. Keep **Rend** on the boss so **Bloodthrill** keeps lighting up **Overpower**, use **Slam** and **Mortal Strike** on cooldown, let **Execute** take the leftover rage below 20%, and fill every gap with **Hamstring**.

**Why it works**

- **Overpower** is at the top: 5 rage for a full weapon hit with 50% more crit chance (**Improved Overpower**), and it stays lit for only 5 to 6 seconds. Most of yours come from **Bloodthrill**, not from dodges: each main-hand hit on a target with your **Rend** has a 20% chance to light it up. The simulator measured 2% more damage with **Overpower** first.
- **Slam** comes next. With both ranks of **Improved Slam** it is a 1-second cast (1.5 base) on a 10-second cooldown (15 base) that no longer delays your swing, so it costs only 15 rage and a short global cooldown; the simulator measured it best right under **Overpower**.
- **Rend** goes before **Mortal Strike** because **Bloodthrill** only works while it ticks: without it, **Overpower** lights up on dodges alone. It lasts 21 seconds, about 8 casts a fight; the list skips it in the last 6 seconds of the fight (0.3% in the simulator).
- **Execute** stays below **Mortal Strike** even under 20%. It spends all your rage (600 damage plus 15 per extra rage point), so the rotation uses **Overpower**, **Slam**, **Rend** and **Mortal Strike** whenever they are ready and lets **Execute** take what is left; the simulator measured 1.3% more damage than with **Execute** at the top.
- **Spearing Strike** (15 rage, 20-second cooldown) deals only 40% of your weapon damage against most bosses, so it sits under your main attacks and above the filler.
- **Hamstring**, not **Bloodrage**, is your real filler. For 10 rage it is another main-hand hit that can light up **Overpower** through **Bloodthrill** and, in a raid, trigger a shaman's Windfury Totem; the simulator measured about 1% more damage casting it freely than only above 80 rage. **Bloodrage** is a 1-minute rage cooldown for when you run short: the rotation uses it only under 45 rage, 2 or 3 times a fight, which the simulator measured 0.6% better than under 90.

**Caveats**

- This list is for a full raid. With fewer buffs you will not have the rage for free **Hamstring** casts: the simulator's rotation for a warrior alone on a training dummy never casts it and stacks **Sunder Armor** instead.
- Several targets: **Whirlwind** needs **Berserker Stance**, so this list never uses it. With a second target in reach, press **Sweeping Strikes** (30 rage, 30-second cooldown: your next 5 melee attacks also hit a second target), and above 40 rage use **Cleave** in place of **Hamstring**.
- The simulator's full list keeps a **Mocking Blow** line near the bottom that never fires. Never use it on a boss: it forces the boss to attack you for 6 seconds.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- If nobody in your group has **Battle Shout** up, cast it before the pull and again every 3 minutes: the list leaves it out because the simulator's raid already had one.
- If the boss has no **Sunder Armor** and no Expose Armor, put one **Sunder Armor** on it. That is the full list's only **Sunder Armor** line; it never fired because the simulator's raid already carries the tank's 5 stacks.
- Against Giants and Dragonkin, **Spearing Strike** deals an extra 80% of weapon damage (three times as much), so press it right after **Mortal Strike**. The simulator's boss is neither, so that order is untested.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arms | 34 | Deflection 5, Improved Rend 3, Improved Overpower 2, Improved Tactical Mastery 3, Anger Management 1, Deep Wounds 3, Impale 2, Spearing Strike 1, Two-Handed Weapon Specialization 3, Bloodthrill 2, Sweeping Strikes 1, Weaponmaster 5, Improved Slam 2, Mortal Strike 1 |
| Fury | 17 | Booming Voice 5, Cruelty 5, Unbridled Wrath 5, Improved Execute 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 874 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 725 | [32/17/2](https://talentsforever.com/warrior/60/30303213132215201-55050000002-2-12) |
| Pre-BiS | 797 | [32/17/2](https://talentsforever.com/warrior/60/30303213132215201-55050000002-2-12) |
| Raid BiS | 863 | [31/17/3](https://talentsforever.com/warrior/60/30303213032215201-55140000002-21-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 59.6; Pre-BiS 60.4; Raid BiS 61.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Skyfury Helm](https://www.wowhead.com/forever/item=20134) · *quest: The Darkreaver Menace*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* |
| Shoulders | [Dark Warder's Pauldrons](https://www.wowhead.com/forever/item=22241) · *Warder Stilgiss, Blackrock Depths* | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Savage Gladiator Chain](https://www.wowhead.com/forever/item=11726) · *Gorosh the Dervish, Blackrock Depths*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Vambraces of the Sadist](https://www.wowhead.com/forever/item=13400) · *Timmy the Cruel, Stratholme*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Vambraces of the Sadist](https://www.wowhead.com/forever/item=13400) · *Timmy the Cruel, Stratholme*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Vambraces of the Sadist](https://www.wowhead.com/forever/item=13400) · *Timmy the Cruel, Stratholme*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Reiver Claws](https://www.wowhead.com/forever/item=13162) · *Overlord Wyrmthalak, Blackrock Spire*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Highlander's Plate Girdle](https://www.wowhead.com/forever/item=20041) · *sold by Samuel Hawke* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Highlander's Chain Girdle](https://www.wowhead.com/forever/item=20043) · *sold by Samuel Hawke* |
| Legs | [Handcrafted Mastersmith Leggings](https://www.wowhead.com/forever/item=13498) · *Goraluk Anvilcrack, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Swiftwalker Boots](https://www.wowhead.com/forever/item=12553) · *Princess Moira Bronzebeard, Blackrock Depths*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Furbolg Berserker's Boots](https://www.wowhead.com/forever/item=287033)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Battleboots of Heroism](https://www.wowhead.com/forever/item=226857) · *sold by Mokvar*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Magni's Will](https://www.wowhead.com/forever/item=12548) · *quest: The Princess's Surprise* | [Painweaver Band](https://www.wowhead.com/forever/item=13098) · *General Drakkisath, Blackrock Spire* | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Magma Forged Band](https://www.wowhead.com/forever/item=22255) · *Dark Coffer, Blackrock Depths* | [Magma Forged Band](https://www.wowhead.com/forever/item=22255) · *Dark Coffer, Blackrock Depths* | [Painweaver Band](https://www.wowhead.com/forever/item=13098) · *General Drakkisath, Blackrock Spire* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Treant's Bane](https://www.wowhead.com/forever/item=18538) · *Tribute, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Nightfall](https://www.wowhead.com/forever/item=19169) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHFUU3jN/e/ak2U5vIp3cqJ0uWjdbJ85PJk2qmE1RUF8s+qBEwUySTXelJsvOPsS3JvRBRUp8qJBQSfyphmBQq8QSpKCCtkLFPhisKNYoKFGxzyJW7uxuUpPgQ2D1POzeveece77vfOfODt2IoIMBJqShH/JQhGMAzwDMAswBsB2RVxLeLuCXd6KiAy9SHF9/CYyVBpLx3TFS8PsFIA1P5Y1LGmn4+WPGD0nS8Ku88a34Xh02ZuKk4IVTImqpIBI1fHbA+C5JMh4fIAV/XwCS8Y3HScG3TwLFcXUSjF+TFCMZfxtI3ap/Ukj/OAOHl0/AcyBNFKYh8WrwZvB178xpmAfp+cJVmCgcwggtZGFJ2uPZnu25jud4ruv4ru1Yvm/7dmSu5Z6XlBVptZEYxblKMk41peKkkmw5IUvwyt6HfWvLL/tYlt9NHnOoNdOCMkt+BA2kplW82MckXRVBBA6xlE7JM1XXuUciV7wWVz1Mf/FhRhy5Rop+6QVgnbyD9vM22pXZiQqTHojxCIlnh9ScYahFW0RImus47X4oauFcP7sZgfONWU7V/34j87hDbfy2jRGuHRLL6NVzkTRSnA475ApJBmcHuL8VGHczGKcjAqORgt/MAruJt25M6rRDQRJ/OQfM595WYLwtwHiVNP2D09tJw1d+2la18fe2nfYWsCNB8egTo8Wy6dpup+XYluccNAfzwciR3JA5WjKDoaHckDnwtFnO58zSaDkoF0ZHzDAXlAbzZjrM5cyg9FRoDQTl8tGcVQoKQ1YtyqpEtT8Zjo608XvoLnaQ9vFbiKYxTrJ+bb/Oa+vx29fXEwWdk55Jim6XYgIrSY5fVVmIJXwqk1cgVh1eoYiZxMlGdnILQu6B+hDK0F62hxpSCYq7YrAX+yLUlYGIUHdWJnqxr3Zr8J05YE18F6mfSRKCUCSt4uLLsBZw4s8H2Q5OkUfB5SVgRTb4D0Z2t+V2bYeRm/83Non1JvbyHnLYHZv7TK28pcaxpkyHXSNDhCakVbw8C6y8WQbbrY8MEfC0jBe72fH/cJwrjZCva4QfiX2tmd2PwO+lO1l39MRVWcM8rMlZvYTtfkg8Y6DKaB5qjV/3iRPx40lg4QZCQvzu+hCKHuv4xezmonW8Q1FR/dMVne3mN9COFBGeAdHGqabqn5sh/yydh6uSOy7HImvOzksNlKA4ymmw/4DUX1JC7MeODWdbpqeEXejZOxzZco97RTIUsydzVor9L1bO1lZ1tX0LdavTHX0+9Fq2t7qR7RevWVMQ/Yhd6cnIeHb3oevexmzogizcB4fhUchDEcZgTPp7AKvZ2vY=); Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHFUU3jM/O2dPks3kJtLJjdrponWzdeL8ZNKkitkUBfXFog9KEMwku+mu1Oyysw/xrQk+iEiJSIUEIfGnGBbrTy2xFilYRau00CIGlYohCkpVrK8iVmZ2N6lJ8CGweh6Wu/ecc8/3ne/cmaEbEVTQQIckjEAOinAY4BmABYBFANYceoXA2w/8citKKnCforgyqq02kYjvTpKEX5xXKYov5bRLUVLw45Ot2vdxiuJXOe3beLBxXtXmFZLwhYsqKfj7mxDkKvj+2TbtuziJWBknCX87DiTi64+RhG8fBVLwygxov8QpQiL+Opq4Vf0kn/xhHg4sH4FnQZjOz0HsVe8N75uh+WNQAeG5/FWYzu/HEDCk4bSw0zEd07Etx3Js23Jt0zJc13TN0GzDPidIq8KVFmKkcJlEnG1PKCSTaFg+i/Hq3ofDa8svh1ma300Os6gr1Ykii5+FJpKTMl4YZoIqB0EEFrGESvETNdeZR0KXUo+rHaa++DAjjjxKknrpeWB9vJf28G5qS7WixIQHIjxE4pg+daQYRsMtIqSobVk9rh/UwsURdjMC5xuzrJr/vRbmcIu6+W0bI2zTJ5ZSa+ciRUmyek2fSyRonO3l7lZg7M1grN4QTJQkvLwA7CbetTGpz/QDkvjzGWAud7YC42wBxqmmqR8c204avvLjtqpNndx22lvADnrFQ48XimXdNu0+wzINx9qnj+W8iYPZjF4o6V4mk83oo0/p5VxWLxXKXjlfmND9rFcay+lJP5vVvdKTvjHqlcuHskbJy2eMepRRjep5wi9MdPN76C62j3bzW4jmUCFRvbZH5fX11O3r6+m8yklNxYNulyIBVhIst6ZyIFbgk5m4CpHa8AaK6HGcaWFHtyBk720MoRTtYjupKREjxQ4Ge2k4RF0diBB1X3Wil4brtwbfWQTWzttI/lwQEAJFkjIuvQxrAUf+fJA1cwo9Ei6fBlZkY/9gZA4Ydv92GNm5f2MTW2/iEB8ki92xuc/UxTvrHOvK9Jp1MkSoQ1LGrxeAlTfLYNqNkSEEnhTxwgB7+j8c52ojxOsa4YZiX+tg9yPwe+lONhA+cWXWVIE1OWuXsMf1iac0lBlVoN74dV9wIn40A8zfQCgQf6AxhMLHOl5c2Fy0gXcoLKp+uqqyHfwGak4Q4QkI2jjbXnu5aeJPwjm4KthTYiS0jnRFaKIYKSgmwfwDEn8JsWA/cng83Tk3G9hng7vGQ1setFcETdIHU6eEyP9i5XR91VDbfbxhdQbC34deSw/VNtIjwZfWLIR/IiuDKRFP7dh/3QeZCf2QhvvgADwKOSjCJEwKfw8ABnPdIA==); Raid BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVltoHGUU3jOXnbMnzWb6J9LJHy/TRetm68S5ZNOkitkUBfXFog9KEMwk2XRXanbZ2Yf41gQFESkViZBQTLxU4+K1lliKFLyg9VKwiEHFYoyCohXqq4iVf3Y3qUnwIbB6HoZ//3POf77vfOefHboSQQcDTEjCEOSgCIcAHgOYB1gAYNtCryS8vcDPt6CiAw8oisvDxkoTyfjWBCn4xWc6RfFozjgXJQ0/ONFi/BCnKH6VM87HScNnXgRjTiMFPz0KpOHvr4HI1fDlC83Gd3FS8NGngGSsjJGML91PCr4xLeK+nwbjQpwiJONvw4nr9A/zyR/nYP/SYXgcpKn8LMSe91/xvxmYOwYVkJ7IX4Sp/D4MAUMGTkmmZ3u25zri4Tpp13asdNrptkNzLdc5Iykr0i/NxEjjKsk405rQSCXZcgIW49W9dwdXl18Osgy/hTzmUEeqHWUWfw+aSE2qeHaQSboqgggcYgmd4sdrrtP3hi6tHlc7TH/6HkYceZQU/dyTwHp4N+3mnbQ91YIKk+6M8BCJZwfUlmIYDbeIkKKu43SlA1ELF4bY1Qicr89yav63m5nHHerk16+PcO2AWEqvnYsUJcXptgOukGRwtoenNwPjbgTjdIdgoqTgt/PAruId65N67ECQxF9PA0tzbzMw3iZgvGqa/s6xraThcz9tqdrkiS2nvQ7sgF88+EChWDZd2+2xHNvynL3mSM4fP5AdNQsl0x8dzY6aww+b5VzWLBXKfjlfGDeDrF8ayZnJIJs1/dJDgTXsl8sHs1bJz49a9SirGtX1YFAY7+S30s1sL+3i1xLNokayfmm3zuvryRvW1lN5nZOeiotulyICK0lOuqayEEv4VCavQKQ2vEIRM45Hmtn0JoTcPY0hlKKd7BpqSsRIc8VgLw6GqKsDEaLuqU704mD91uCbC8Ba+XZSP5EkBKFIUsXFZ2E14PCfd7FtnEKPgkungBXZyD8Y2X2W27sVRm7u39jE1po4wPvJYTdu7DN18PY6x7oy3XadDBGakFTx63lg5Y0y2G5jZAiBJ2U828ce+Q/HudoI+bJGpEOxL7WxOxD4bXQT6wvfuCprqsCqnLVL2JUOiKcMVBlVoN74NZ84Ed8/AixYR0iI39cYQuFrHT+f31i0gXcoLKp/tKKzHfwK2pYgwuMg2jjTWvtzM+SfpTNwUXIn5UhobZmK1EQx0lBOgv0HJP6SYmI/cmgs0z47I+zj/p1joS31u8uSoZj9qZNS5H+xcqa+aqjterVhdfrC590vZAZqG5kh8ak1A+GPyHJ/SsaTO/Zd9kVmQy9k4HbYD/dBDoowARPS3wMAL7rceg==).

**Points that do nothing for this spec:** **Improved Tactical Mastery** (3) only counts toward the points the tree needs before **Anger Management**.

## Other builds of this spec

- [Arms — Raid](../research/raid/builds/arms-ml-raid.md) (39/10/2, 867 DPS in a full raid; fails the signature-spell check: core share 79% under 80% (melee, Mortal Strike, Overpower, Slam, Execute, Rend, Whirlwind, Heroic Strike, Deep Wounds)) — [open the talent tree](https://talentsforever.com/warrior/60/35313213132215211-0505-2-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

