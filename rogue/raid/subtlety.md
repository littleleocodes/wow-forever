# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Raid](../research/raid/builds/subtlety-ml-raid.md)** (12/8/31) — [open the talent tree](https://talentsforever.com/rogue/60/00530301-320003-325230031301001151-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Subtlety — Hemorrhage), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Premeditation**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Vanish**; no global cooldown, so press it alongside the others
3. **Preparation**
4. **Shank**
5. **Premeditation** when you have 3 or fewer combo points; no global cooldown, so press it alongside the others
6. **Death Mark** when you have 4 or more combo points
7. **Rupture**: keep it on the target, when you have 3 or more combo points
8. **Ghostly Strike** when Garrote has under 4 seconds left
9. **Hemorrhage**

**Hemorrhage** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Subtlety in a raid is a Death Mark rotation: **Hemorrhage** and **Shank** build combo points, **Garrote** and **Rupture** stay on the boss, **Slice and Dice** stays up, and 4 or more points go into **Death Mark**, which stores part of your damage and deals it a second time. The list never casts **Eviscerate**.

**Why it works**

- **Death Mark** is your main finisher: 25 energy, a 10-second cooldown, at 4 or more points. For 6 seconds it stores a portion of the damage you deal the target per combo point, **Garrote** and **Rupture** damage at twice the rate, then deals what it stored, up to a maximum your attack power and crit chance raise. **Coup de Grace** raises its damage and storage rate by 20%. It is 23% of your damage in a full raid (about 14 a fight); with it in the build, the simulator's list spends no points on **Eviscerate**.
- **Ghostly Strike** lets your next **Garrote** within 7 seconds skip stealth, so **Garrote** stays on the boss all fight: **Ghostly Strike** when **Garrote** has 4 seconds or less left, then **Garrote** when it runs out (about 7 a fight, 10% of your damage). **Blood Splatter** makes **Garrote** last 27 seconds instead of 18, **Dirty Deeds** makes it 20 energy cheaper and usable from the front, **Initiative** adds a second combo point to it, and **Opportunity** adds 20% to its damage.
- **Rupture** goes on whenever it is off and you have 3 or more points (about 8 a fight, 10% of your damage). **Serrated Blades** adds 30% to it (and your attacks ignore 9% of armor), **Hemorrhage** adds 15% to **Rupture** and **Garrote** for 15 seconds, and **Blood Splatter** makes **Rupture** last 6 seconds longer.
- **Hemorrhage** is your filler (35 energy, 30 with **Efficient Strikes**; 145% weapon damage with a dagger in your main hand), and the list renews it whenever its 15-second effect has run out. **Shank** costs 5 energy, gives back 25, and with **Boot Knife** adds 2 combo points: press it when it is ready, with 3 or fewer points and 80 energy or less.
- Below 5 points the list keeps building; at 5, with **Death Mark** on cooldown and **Rupture** and **Slice and Dice** up, it waits. It also holds **Hemorrhage** while **Garrote** has under 6 seconds left, so the energy is there for **Ghostly Strike** and the new **Garrote** (the rotation search measured that 0.5% better than holding from 8 seconds). **Slice and Dice** (30% attack speed) goes back up with 1 point whenever it drops.
- **Premeditation** adds 2 points: before the pull, then on its 2-minute cooldown with 3 or fewer points (the simulator needs no stealth for it, and its beta tooltip asks for none). **Vanish** opens a **Garrote** a second into the fight, and **Preparation** finishes the cooldowns of **Vanish** and **Premeditation** once a fight. Each of the two talents measured about 1% in the simulator.

**Caveats**

- The **Garrote** after **Vanish** needs stealth, and damage you take breaks it; the simulator does not model that. If something hits you right after **Vanish**, the next **Ghostly Strike** opens the **Garrote** instead.
- Almost all of this works from the front: **Hemorrhage**, **Ghostly Strike**, **Death Mark**, **Rupture**, and **Garrote** with **Dirty Deeds**. Only **Ambush** and **Backstab** need you behind the target, and the list casts neither.
- Subtlety has no cleave: on adds, stay on the kill target, and do not **Rupture** a target that dies within 8 seconds.

**When to change it**

- In the last 6 seconds, start no **Rupture** and no **Slice and Dice**: they would outlast the boss.
- Without a warrior's Sunder Armor on the boss, keep **Expose Armor** up at 5 points; the simulator's list has a switch for it, off in a raid. An earlier search on the training dummy measured it about 2.5% better.
- The simulator starts every fight out of stealth. In the game you can start in **Stealth** and open with **Garrote** at the pull; that opener was not simulated.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Assassination | 12 | Malice 5, Ruthlessness 3, Improved Slice and Dice 3, Blood Splatter 1 |
| Combat | 8 | Coup de Grace 3, Efficient Strikes 2, Precision 3 |
| Subtlety | 31 | Setup 3, Master of Deception 2, Opportunity 5, Dirty Deeds 2, Camouflage 3, Initiative 3, Premeditation 1, Serrated Blades 3, Ghostly Strike 1, Preparation 1, Hemorrhage 1, Boot Knife 5, Death Mark 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 803 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 774 | [12/8/31](https://talentsforever.com/rogue/60/00530301-320003-305230031321001151-12) |
| Phase 1 BiS | 789 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.7; Phase 1 BiS 62.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Outlaw's Collar](https://www.wowhead.com/forever/item=279253) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Bracers of the Eclipse](https://www.wowhead.com/forever/item=18375) · *Prince Tortheldrin, Dire Maul*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) · *sold by Pix Xizzix* |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Dunestalker's Boots](https://www.wowhead.com/forever/item=20715) · *quest: Armaments of War*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Fiendish Machete](https://www.wowhead.com/forever/item=18310) · *Alzzin the Wildshaper, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzUWX1sHEcV99s7341fXOc8/jqPk3S8SRPnwjl7e7bJR0v8lbRuQuvWLTkkULP2rXNXn3fN7rptqlJMkRGilBLSEtUSVZQaUgJExSJplD8qoVZJQKkEQQQBQYQ0hYAiFAUI0pEStOs9Z+M7n0uVhHb/OM3Me/PezPv4zZs5XEQgBGHg0ATbIAUjMAbwFYA9AK8C0HKHKtjUNcDGmokQ8rMvYJD8arwyfG4B+sm55wH95JcnQhgkb34Hwr8I2I0fLwy/U4FBcux5CP/ebpw4EQr/oQL95NmfhzBATo3as4Pk2DMwPTy+yxbz3IUQ+si+z6CfvPYiYJCceRHCF+z5vxuvtBt+sut5EJtDx9NN5zPSlfW9p74OiX9s+yYIV9ZPAHlF+YFyuuNbfftB+Fr6NTiz8TBc2AudxNkFtMMRQZSk1rgUl2LRuCxJUjwal1vluCTFY3EpJkmxWGvsuOA/K7y3CisxyErRRw5mxAD6UYjGkbpDf9bEIJaiLyqbuAo51mQDFEN9lmJYvEfjfZaqZKwUC2Jpk5/8+zaXOWbSKFvlMj9sqnzjEyO6qfIOY1g3zkIlLvykktYsJa25FNrPtuFW+jCybKAOa+wpn1K0tJnig7rBu5VhZbuKtdlAFVbatI7h/lEzxe8fUTXVwNuzgUXIukYNQ9Us3qunNcvkGdU0uZVSNN7qbGQ8QU32OUzRQWRieE5ZxfTPpwcXiGUYlG1tEwlH6USCHgH2OuD3gb4K19GRRkIkQIUnSxi55HPHbtrKrgnu07r5JiWT4T3Dw2lN1SwMRSrshawrYY7zY6bjTYH8pIJ+D9h3ASeA7ob89Y4nPlRrXcwakNIQVojliHshN+744S8aXc6WIWNhLBcRyUm/PXowg2QKplv23snpPUAl1ox1tAbJXpeCZSf9LlGuQpJjnEkZGmIViFMQRB+53BKGdSV0EWNnoQ5rNmqqsX0H79X1TFrbzrtS6sCQSZ9mT6HBRvAuut7NkE5dt/hmLT2o8s2a/rjmuMRPfc9Aia0EIe6O2NHibHyNhKtpFOvFuuIiPBOchT+36wHaw+7GT9A7Z3O0St5d4G3igtzOd1/a4u2e3gP2qsihIaqyAdxC780Z69AQhmmthw/L9kKu6aHYAl2K3fSoLWDhQ0P0TrYOl9JGj5p5ZttSZ2YvYyKGI7UkQMl+dz4jGEB/rHntcI6drmIr3dC8W9OHVb5x1FCHFB7lfSl9NJPkXYppOcyTl7Y4wbSIsVnB5K7kYCYMzI9CmNG/AU0qI5lH9BGLy5LcFo3FotLadXwgpWjb1STXDa4kk2qS9+/gVkrlhm4pVlrXuKkqxkCKN5mqys3RfiujWjuihpJORnMs0WmW5kdNXVvJxgGfYk/iHXTpbLfGWnGheBsuOEsIBpqAvHugF2N0dc4Vk5e2zJ4htxYYWUIXFRglsi3jjX/22rYOXVlPG1h9fvC6BwnlbAlWU+om8TWGFuZKofuB7QP8NtAJcOw7s+rz33jgWufqGGA1y5cT9wDsswlsEOuxLhuoRropvT1l8Y5+fdTils43aklcKa7AO7IBEXNHU5T3GupjNnzeb6VUg29K2yCrGub15vvX1fttZeTZBH0F2B7AF4DuBFyRDSxDscOyPdqpZvTHuY1dXZn0yIid+Q+lDNVM6ZkkLskGGrC+o19/THVYHKz20G/Qol1YvNxCnwP2VcAxoE879gKPvYpDbR7eTyb+Z6tNAZlOr/A0ZPxRo38SblFKvAf4d6AXAX8E7ADkBUsrNtLb80zSggtO+m1P+8jFdzbjPXRTgYm1kWrip+SIAyaXnehFoc0sas0oXZUnKX7jw/PdA04qkskEfZSl8BH62fnP26WsEYNiKfqyvhJ3/d1pw9rBu1U1abrHSU2kivhp8FG3uHG23GI6uo7qdP+twrlOXEPbsEqsxIVTUI5+cnUMqBAqDcO8+7Td5LAfE9hbAh4R6OuCN0oP7HwgDFiZDVRguV1ldSoDQ6al9M9vwKPA3oSi3u+iHbg00khKHfSsnxJqCVA3rS635BJsZ6KoEFHk88IHzwYWY0OPxrvtbDK4PsjdIqRLcaDILc1momqL/jjvHjUcb7goNuv86xiw0o+ptgvv0y3+oKokdzhu35mg+wQ2KeBugb4gzG+lY8DeKm6lbtqJyyKiayU2JdRdZ6WySz7bhXZefkTMNAMk9G3fLUqQcwL+RqCnBKwRqz5QMN8oN10dKy7lw+MmXMlWOPgWmIVvbeb0ZeIssU9TIEf1GQz5rcB+LeDbAv2ZiyHeU8NTK9tW+KCeuFGw8vJHClZeToR9kbvyHwgirMk12YwST2U+fbdyBLyxNfLQXFev9WytK2TuIl+uxWojV1zOFLtrJXlx/rsHLcMglg4qGVOV66/3r5e0OP8RxEtunOOqTJ1bimWMqvKSAi8CXhEcq3qNtM77MukBlStaknenB1QvR3OxWKP2bn3eIkfuKRArtIXKhasf2cRwNlBTcBXyCqyapTptconOrr0keXORGKTN7GN5FVSsiNY73089TgvuRjLl1UXDnc6Kjo+3yssL1XHUvTLd6/K1mbI6R5ZQ+x5d+MEMY2w1hsQKLJ+CMifC7ZIHGyL1xE/Lj3jG7LIffbE2U76vWJ5QiTYXug3MncPyp+evRGkrjc+1g2KiP/9+sIFuZQ97gdW+t7qF26R9vZimTb8K2LQmutzbrY/UEb/n/l+2N+iS5C9BMTSgKh3w6vTI3Mx6vA8Ah4ZyTxGHhsLgaCwtqNF5SfM5QTFDlrfmP+HQLtaRq+xLyZd3ztyA/d6Oz9sRvB2wO/LtBap56h5pAnlGOy8ch4uC/EVfifNVt/8V/ChgifgfocweKBkbbK+feMn+frqhcdD5Tm2QzwhhP98QOSyU/F8+qz3Xuqnf8h/eND1rnd8HJ9s73IH2bfa/ES+B0yk5syHiI4frOj1/WkiwBtrhHuiFBKRgBJ6AJ4T/DgDAW+km).

## Other builds of this spec

- [Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md) (21/0/30, 651 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053230020141--3352331313010011-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

