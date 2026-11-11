# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Raid](../research/raid/builds/fury-open-raid.md)** (20/31/0) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fury — Two-Handed), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Two-handed setup. The spec's best build for each other setup, in a full raid:

- Dual-wield: [Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md) (17/32/2, 865 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

## How to play

**Setup, before the pull:** **Berserker Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Then press the first one that is ready**, top to bottom:

1. **Recklessness** when the target is below 20% health
2. **Whirlwind** when **Bloodthirst** is more than 1.5 seconds from ready
3. **Bloodthirst**
4. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
5. **Heroic Strike** when you have 90+ rage; no global cooldown, so press it alongside the others
6. **Execute** when the target is below 20% health
7. **Hamstring**
8. **Bloodrage** when you have less than 90 rage; no global cooldown, so press it alongside the others

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Reckless Swings**: a cooldown, use it in the last 33.75 seconds of the fight (about 3 times a fight)
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
| Arms | 20 | Improved Heroic Strike 3, Deflection 2, Improved Rend 3, Improved Tactical Mastery 3, Anger Management 1, Deep Wounds 3, Two-Handed Weapon Specialization 3, Impale 2 |
| Fury | 31 | Cruelty 5, Unbridled Wrath 5, Furious Precision 3, Blood Craze 3, Enrage 1, Reckless Swings 1, Improved Execute 2, Improved Berserker Rage 2, Death Wish 1, Gore Drinker 2, Improved Whirlwind 2, Flurry 3, Bloodthirst 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 865 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 924 | [17/32/2](https://talentsforever.com/warrior/60/30303213002-150530105122100231-2-12) |
| Phase 1 BiS | 939 | [17/32/2](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.2; Phase 1 BiS 62.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Bloodmail Boots](https://www.wowhead.com/forever/item=14616) · *Instructor Malicia, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* | [Riphook](https://www.wowhead.com/forever/item=12653) · *Shadow Hunter Vosh'gajin, Blackrock Spire* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV2toHNUX3zMzO3v2pN1Ob9p/JzftnzGUup268c7sTtpUMdui4gOx6ocWEcy2u3VXpBt2IqbohyYoiI9SiUi6PhIf0RBtwVq1FAnio1Sx0CIEfGGIgoIVIvjFB1budDdrN/kgIVnvh+XsPedwf7/7+80ZhtYiGGCCBXHohjz0wAGARwFGAMYA2LIgq8jsFuC/rUbNAP4g6Ti125xuIhXf6iMNP//MIB2fy5vndIrgR8dXmN/FKILvj4L5jQxeeBXM4QhpOHjWoAj+chRks45DJfPbGGn45HmDNBw6a5CKr91FGr4d1M0cBfO87P/qkZUyUPHn3W1x41Qh/v0w7Jg8CLt+7X4MlIFCGaIvZ97IfLlteBTGQXmiMAMDhe0YYIc0nFSspEiKpOskhXATjie8pHCE57iuI4SbdBLuaUWbVv5oZg8D25Ppue/uYk+v5Qq3I+E4CbFlq7Unn9l3Ty5rFUtWJpvNZa3d+63efM4qFXszvYXiPsvPZUp78lbcz+WsvfeX9ieyDyRKmUI2Ua1IXKxov9cv7tvI19FKewXqTLkpxCMUJjUpfI6kxzWcPAksza+hJHOo1W5BlcU+gCYKx8N45k6mGGEeJpXAIdZmUOxYJTWxM0hFqnVRHpF1xjN3MOLIddKMc08Be3YOP5EQ7uLzS9EmvjHgqNU4pjyfVtmsQpsISXcdp93zJVIc62b/R+C8vsup5N9dzobmQ9+5+Ogd2sgvr8eRFD4x26igR9JJc1LC5xopJmebuTcfZVfMoeykAso6afj1CLB1vLW+qUP4UjD8aQKYx5P/Foy0kNT5vdGFtOFLPyzotP7jC24r1qvpJERq8dUM3I+Dg7ex1+fxT9JZ/BOvpavZVtrA1xOVMUKqcWGTwatx/xW1eKBgcDLsmJS2FJI4SXG8iqUeasyjurpetpTnbw2xnsY8alF5phXDQ8tZM19J4U8VBUF6JR7Gd16E6vDCN8dq8cE/b2WPQ2NuZz212GswzJrGYXY8S0CkCL8GfRvvIoddGUgZZuo0hKpDupW3BLt6TeCUqNIkQgviYfxiBNiRBr15rqerWCets1vrSQXz2Gl3XM8n0/4fhhmNQ5XhReRuQDmu4plONlCPV3Qm3CXA2xqMEDW4vmDOuW67J28XL6xiNyLw6wJC8k1ZRyiolrOWuG3W0ZnNSWL44SFgz0NjDN9BcbYhsARcYpTKoKyy7Njc7lX8gXjqY2ADDfLHnPvu2Fy77wlozMjeSbewm4MhKqXTWXQcpE7SptFypBLSWpujfomsVI5UY2qaRmluwKdHYFblNXw1LWsjwmMgLVRuDpiVm031R+U0zChuvxoK1qr0uNJEUYqgGgfxO7T9pUTlfujA3nRL+bBcn3RdtjdYk13ulGJqVpd9Qgn9J6s3XY2WdG04smTndAa/t7+S3lbZSHfLz5DDEPwJTXXZKp5Ys/0fXysCtkAaboAdsAvy0AN90Kf8PQC5zchK); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3v2pN1Ob1o7uWllDKVup268M7uTNlXMtqj4g1j1oUUEs+1u3RXphp2ILfrQBgVRKZWotOtP40+0RFuwVi1FgvhTqliwCAVFMURBQYUKvviDlXu7m7WbPEhI1vuwnL3nHO733e+bMwwtR7DABgeS0A9FGIDdAI8CjAAcAmALVFaT2XXAf1+KhgX8QTJxYqs92UY6vrWTDPziM4tMfK5onzEphh8dW2R/l6AYvj8K9jcyeOFVsA/GyMDhzy2K4a9HQDabuL9if5sgAx8ZBjJwfBRIx9fuIgPfVnUTT4P9s+w/d0QFOv6ytStpnSwlvz8Im87uhS2/9T8G2lCpCvGXc2/kvtpwcBTGQHuidA6GShtRYYcsnNCctJ8WaeGlhfBTIhBBWvgi8HzfE8JPeyn/lGZMan+2s4eBbcsN3Hd3eWDQ8YXfk/K8lFi33tlWzO24p5B3yhUnl88X8s7WXc5gseBUyoO5wVJ5hxMWcpVtRScZFgrO9vsru1L5B1KVXCmfqlekLlR03xuWd6zmK2ixuwhNpt0U4TGKkp4WIUcykwaePQEsy6+hNPOo0+1AnSU+gDaKJqN4+k6mWVEeJZ3AI9ZlUeJoLTW+WaVi9bo4j8k665k7GHHkJhnWmSeBPTuNn0gJf+75ZWgNX604Gg2OmSCkJS6r0SZCMn3P6w5CiRQP9bNLEThv7vJq+XcXsv0zoe+de/QereaXN+NIi5CYa9XQI5lkeBkRcoM0m7O1PJiJsi+mUfYyirJJBn49AmwF72xu6hGhFAx/GgcW8PR/BSMtJHV+b3Q2bfjSD7M6bc+xWbeVm9X0UiIz92oq9+Pw8G3s9Rn8k/bm/sRr6Wq2nlbxlURVjJFunV9j8Xq854pGPFSyOFluQkpbiUicpHlBzVIPteZRXdosWyYI10fYQGsetbg800ngvoWsnS+m6KeahiC9koziOy9CfXjhm4ca8d6/bmWPQ2tuZyV1uMswytrGYGo8S0CkibABfQPvI49dqaSMMn0SIvUh3ck71K7ZEDgj6jSJ0IFkFL8cAXa4RW+e6+kq1ksr3M5mUmoee92eH4Rku5dglNEY1BleQO4rykkdT/eyoWa8ojflzwPeTjVCdHV9as75fncgbxfPL2E3IvDrFCH5pmwipKrlrCXu2k10pnKSGH64D9jz0BrD91CSrVKWgIuMUhuUdZY9a7uDmj8QT34MbKhF/ph23z1rG/c9Dq0Z2ZvpFnazGqJSOpPFx0DqJG0ar8ZqIS13OZoXyUrVWD2mtkmU5gZ8agSmVF7Gl9KCLiI8CtJC1XbFrNpu6z9qp+Cc5u/RI2otyY5pbRSnGOpJEH9A199aXO5Hdm/PdlQPyPVJ32Xb1Trb509otuH0uce1yP+yBrP1aF7XqsPzdk6v+r39leyG2ka2X36GHAD1JzLR5+p4fNnGf32tCFgHWbgBNsEWKMIA7ISd2j8DAKB1x8s=).

**Points that do nothing for this spec:** **Improved Tactical Mastery** (3) only counts toward the points the tree needs before **Anger Management**, **Impale** and **Two-Handed Weapon Specialization**.

## Other builds of this spec

- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 855 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500305022100231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 842 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-553500050020100231--12)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 826 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013102-050530305022110231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 788 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530055021100231--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

