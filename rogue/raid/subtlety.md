# Subtlety Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Subtlety

**[Subtlety — Raid](../research/raid/builds/subtlety-ml-raid.md)** (12/8/31) — [open the talent tree](https://talentsforever.com/rogue/60/00530301-320003-325230031301001151-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Subtlety — Hemorrhage), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Premeditation**.

**Keep up all fight:** **Slice and Dice**.

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target (timing: see below)
2. **Vanish** (timing: see below); no global cooldown, so press it alongside the others
3. **Preparation**
4. **Shank** (timing: see below)
5. **Premeditation** when you have 3 or fewer combo points; no global cooldown, so press it alongside the others
6. **Death Mark** when you have 4 or more combo points
7. **Rupture**: keep it on the target, when you have 3 or more combo points (timing: see below)
8. **Ghostly Strike** when Garrote has under 4 seconds left (timing: see below)
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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 798 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 797 | this build |
| Phase 1 BiS | 799 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.6; Phase 1 BiS 62.9; each item opens its Wowhead page, with where it drops and its enchant):

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
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Fiendish Machete](https://www.wowhead.com/forever/item=18310) · *Alzzin the Wildshaper, Dire Maul*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#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); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzUWX1sHEcV99s7341fXOc8/jqPk3S8SRPnwjl7e7bJR0v8lbRuQuvWLTkkULP2rXNXn3fN7rptqlJMkRGilDakENUSVZQaUgJEYJE0yh+VUKskoFSCIIKAIEKaQooiFAUI0pEStOs9Z+M7n0uVhHb/OM3Me/PezPv4zZs5XEQgBGHg0ATbIAUjMAbwFYA9AK8C0HKHKtjUNcDGmokQ8rMvYJD8erwyfG4B+sm55wH95FcnQhgkb3wHwr8M2I2fLAy/XYFBcux5CP/Bbpw4EQr/sQL95NlfhDBATo3as4Pk2DMwPTy+yxbz3IUQ+si+z6CfvPsCYJCc+SaEL9jzfz9eaTf8ZNfzIDaHjqebzmekK+t7T30dEv/Y9g0QrqyfAPKK8gPldMe3+vaD8LX0j+DMxsNwYS90EmcX0A5HBFGSWuNSXIpF47IkSfFoXG6V45IUj8WlmCTFYq2x44L/rPDeKqzEICtFHzmYEQPoRyEaR+oO/UUTg1iKvqhs4irkWJMNUAz1WYph8R6N91mqkrFSLIilTX7y79tc5phJo2yVy/ywqfKNT4zopso7jGHdOAuVuPCTSlqzlLTmUmg/24Zb6cPIsoE6rLGnfErR0maKD+oG71aGle0q1mYDVVhp0zqG+0fNFL9/RNVUA2/PBhYh6xo1DFWzeK+e1iyTZ1TT5FZK0Xirs5HxBDXZ5zBFB5GJ4TllFdM/nx5cIJZhULa1TSQcpRMJegTYa4DfB/oqXEdHGgmRABWeLGHkks8du2kruya4T+vmm5RMhvcMD6c1VbMwFKmwF7KuhDnOj5mONwXy0wr6PWDfBZwAuhvy1zue+FCtdTFrQEpDWCGWI+6F3Ljjh3c1upwtQ8bCWC4ikpN+e/RgBskUTLfsvZPTe4BKrBnraA2SvS4Fy076XaJchSTHOJMyNMQqEKcgiD5yuSUM60roIsbOQh3WbNRUY/sO3qvrmbS2nXel1IEhkz7NnkKDjeBddL2bIZ26bvHNWnpQ5Zs1/XHNcYmf+p6BElsJQtwdsaPF2fgaCVfTKNaLdcVFeCY4C39u1wO0h92Nn6B3zuZolby7wNvEBbmd7760xds9vQfsVZFDQ1RlA7iF3psz1qEhDNNaDx+W7YVc00OxBboUu+lRW8DCh4bonWwdLqWNHjXzzLalzsxexkQMR2pJgJL97nxGMID+WPPa4Rw7XcVWuqF5t6YPq3zjqKEOKTzK+1L6aCbJuxTTcpgnL21xgmkRY7OCyV3JwUwYmB+FMKN/A5pURjKP6CMWlyW5LRqLRaW16/hAStG2q0muG1xJJtUk79/BrZTKDd1SrLSucVNVjIEUbzJVlZuj/VZGtXZEDSWdjOZYotMszY+auraSjQM+xZ7EO+jS2W6NteJC8TZccJYQDDQBeedAL8bo6pwrJi9tmT1Dbi0wsoQuKjBKZFvG6//stW0durKeNrD6/OB1DxLK2RKsptRN4msMLcyVQvcD2wf4baAT4Nh3ZtXnX3jgWufqGGA1y5cT9wDsswlsEOuxLhuoRropvT1l8Y5+fdTils43aklcKa7AO7IBEXNHU5T3GupjNnzeb6VUg29K2yCrGub15vvX1fttZeTZBH0F2B7AF4HuBFyRDSxDscOyPdqpZvTHuY1dXZn0yIid+Q+lDNVM6ZkkLskGGrC+o19/THVYHKz20G/Qol1YvNxCnwP2VcAxoE879gKPvYpDbR7eTyb+Z6tNAZlOr/A0ZPxJo38WblFKvAf4d6AXAX8M7ADkBUsrNtLb80zSggtO+m1P+8jFtzfjPXRTgYm1kWrip+SIAyaXnehFoc0sas0oXZUnKX7jw/OdA04qkskEfZSl8BH62fnP26WsEYNiKfqyvhJ3/d1pw9rBu1U1abrHSU2kivhp8FG3uHG23GI6uo7qdP+twrlOXEPbsEqsxIVTUI5+cnUMqBAqDcO8+7Td5LAfE9ibAh4R6GuCN0oP7HwgDFiZDVRguV1ldSoDQ6al9M9vwKPA3oCi3u+iHbg00khKHfSsnxJqCVA3rS635BJsZ6KoEFHk88IHzwYWY0OPxrvtbDK4PsjdIqRLcaDILc1momqL/jjvHjUcb7goNuv86xiw0o+ptgvv0y3+oKokdzhu35mg+wQ2KeBugb4ozG+lY8DeLG6lbtqJyyKiayU2JdRdZ6WySz7bhXZefkTMNAMk9C3fLUqQcwL+VqCnBKwRqz5QMN8oN10dKy7lw+MmXMlWOPgWmIVvbeb0ZeIssU9TIEf1GQz5ncB+I+BbAv25iyHeU8NTK9tW+KCeuFGw8vJHClZeToR9kbvyHwgirMk12YwST2U+fbdyBLy+NfLQXFev9WytK2TuIl+uxWojV1zOFLtrJXlx/rsHLcMglg4qGVOV66/3r5e0OP8RxEtunOOqTJ1bimWMqvKSAi8CXhEcq3qNtM77MukBlStaknenB1QvR3OxWKP2bn3eIkfuKRArtIXKhasf2cRwNlBTcBXyCqyapTptconOrr0keXORGKTN7GN5FVSsiNY73089TgvuRjLl1UXDnc6Kjo+3yssL1XHUvTLd6/K1mbI6R5ZQ+x5d+MEMY2w1hsQKLJ+CMifC7ZIHGyL1xE/Lj3jG7LIffbE2U76vWJ5QiTYXug3MncPyp+evRGkrjc+1g2KiP/9+sIFuZQ97gdW+t7qF26R9vZimTb8K2LQmutzbrY/UEb/n/l+2N+iS5C9BMTSgKh3w6vTI3Mx6vA8Ah4ZyTxGHhsLgaCwtqNF5SfM5QTFDlrfmP+HQLtaRq+xLyZd3ztyA/d6Oz9sRvB2wO/LtBap56h5pAnlGOy8ch4uC/EVfifNVt/8V/ChgifgfocweKBkbbK+feMn+frahcdD5Tm2QzwhhP98QOSyU/F8+qz3Xuqnf8h/eND1rnd8HJ9s73IH2bfa/ES+B0yk5syHiI4frOj1/WkiwBtrhHuiFBKRgBJ6AJ4T/DgCs2+la).

## Other builds of this spec

- [Subtlety — Hemorrhage](../research/raid/builds/subtlety-hemo-raid.md) (21/0/30, 645 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053230020141--3352331313010011-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

