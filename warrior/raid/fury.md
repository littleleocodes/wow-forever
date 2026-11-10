# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Raid](../research/raid/builds/fury-open-raid.md)** (20/31/0) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fury — Two-Handed), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Two-handed setup. The spec's best build for each other setup, in a full raid:

- Dual-wield: [Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md) (17/32/2, 894 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

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

- **Reckless Swings**: a cooldown, use it in the last 33.75 seconds of the fight (about 2 times a fight)
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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 909 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 924 | [17/32/2](https://talentsforever.com/warrior/60/30303213002-150530105122100231-2-12) |
| Phase 1 BiS | 939 | [17/32/2](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.8; Phase 1 BiS 62.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) | [Gryphonwing Long Bow](https://www.wowhead.com/forever/item=13022) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHNUX3zMzu3P2pN1Ob9p/JzftnzGUup268c7sTtpUMdui4gdi1YcWX8y2uzErkg07EVsQbIKC+FEqUUlXJNEaCKktWqqWIkFsLVVaaBECfocoKLQPEXzyq3Knu1m7yYOEZL0Pl7P3nLv397u/35xhaC2CASZYEIdO6IZe2A/wHMAIwBgAWxZkFZndAvzP1agZwJ+mCE7tNqcbSMPDQ0AafnHeIB1Pj4J5KUI6njmxwvwhRjp+PArmtzI4c94wh3XScPCirPzlGMjtOl4+Aub3MdLwpSsGaTh0Uc7vB/O7rwLpOHMMzCvyH75+dqUMVPwu1xI3zubjPw7DjskDsOvXzudBGciXIHo4807mq23DozAOyov5GRjIb8cAP6ThlGIlRVIkXScphJtwPOElhSM8x3UdIdykk3DPKdq08nsjewbYnkzv448UevssV7htCcdJiC1brT3dmZ5Hc1mrULQy2Wwua+3eZ/V156xioS/Tly/0WH4uU9zTbcX9XM7qeqK4L5F9MlHM5LOJSkXiWkXrY36hZyNfRyvtFRhhyj0hrlOY1KTwOVIkruHkKWBpfhslmUPNdhOqLPYJNFA4HsYLDzPFCPMwqQQOsRaDYsfLqYmdQUqv1EW5LuuM1x5ixJFHSDMuvQzs9Tn8REK4i88vRZv4xoCjVuWY8nxaZbMybSKkiOs4rZ4vkeJYJ/s/Aue1u5xy/sPlbGg+9O2Lj96hjfzGWhxJ4ROzjTJ6pAhpTkr4XCPF5Gwz9+aj7Io5lJ1UQDlCGn4zAmwdb67d1CZ8KRhengDm8eS/BSMtJHX+aHQh2/CtnxZ0Wv+JBW8r1KrpJERq8dUM3I+Dgw+wI/P4J+ks/om3061sK23g64lKqJNqXN1k8Ercf1M1HsgbnAw7JqUthiROUhyvbKmn6vOorq6VLeX5W0Ostz6PWlSeacXw4HLWyFdS+HNFQZBeiYfxgzeh0rzwvbFqfOCP+9kLUJ/bWU9N9hoMs4ZxmG3PEhApwq9C38Y7yGE3B1KGmToNoUqTbuZNwWqkKnBKVGgSoQXxMH45Auxond48d9ItrJ3W2c21pIJ+7LQ6rueTaf8Pw4zGocLwGnI3oBxX8UI7G6jFK9oT7hLgbQ5aiBpcX9DnXLfVk7eLV1exuxH4HQEh+aasIRRUy15L3DZr6MzmJDE8fRDYG1Afw7dRnG0ILAHXGaXcKCss2za3emV/IJ79FNhAnfwx577bNlfvewLq07J30n3s3qCJSukiLDoOUidp02hJL4e01uYYuU5WKumVmBqmUZob8JURmFV5DV9Ny1qI8DhIC5UaA2alRlP9WTkHM4rbr4aCsSo9rjRQlHRU4yB+g5a/lKhcD+3vSjeVDsnxWccNXcGY7HCnFFOzOuyTSug/GX3pSrSkY8PRJTunPZgffDu9rbyQ7pSfIocg+BGa6rBVPLlm+z++WARsgTTcBTtgF3RDL+yFvcrfAwBCysnr); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzu3P2pN1Ob1o7uWllDKVup268M7uTNlXMtqj4g1j1ocUXs+1uzIpkw07EFgSbYEFUaiUqdkUTfwIhtUVL1VIkiNZSpYUUIeB/iAWF+hDBJ/8qd7qbtZs8SEjW+zCcuefcud93v2/OMLQWwQATLIhDJ3RDL+wHeBpgGGAUgC0LsorMbgH+12rUDOBPUgSndpvTDaThxeeBNPzynEE6vj5hmBcipOPpEyvMH2Ok48cjYH4ng9PnDHNIJw0HJ2Tlr8dALtfx0hEwf4iRhgcG5XPGR+T1/QmDNHz3JSAdZ46B+Yt8wjcHVspAxe9zLXHjTD5+cQh2TB6EXb91PgPKQL4E0bcy72S+3jY0AmOgPJefgYH8dgzwQxpOKVbSTYqkcJJCuAnhCS8pXOE5rusI4SadhHtW0aaVPxrZU8D2ZHoffajQ22e5wm1LOE5CbNlq7enO9Dycy1qFopXJZnNZa/c+q687ZxULfZm+fKHH8nOZ4p5uK+7nclbXY8V9iezjiWImn01UKhJXKlof8Qs9G/k6WmmvwAhT7gpxncKkJoXPkSJxDSdPAUvzWyjJHGq2m1BlsU+ggcLxMJ5/kClGmIdJJXCItRgUO15Oje8MUnqlLsp1WWe8/AAjjjxCmnHhBWCvzuEnEsJdfH4p2sQ3Bhy1KseU59Mqm5VpEyFFXMdp9XyJFEc72bUInNeucsr5D5ezV+ZD37746B3ayK+vxZEUPjHbKKNHipDmpITPNVJMzjZzbz7KrphD2UkFlCOk4bfDwNbx5tpFbcKXguGlcWAeT/5XMNJCUuePRhayDN/8aUG79Z9Y8LJCrZpOQqQWX83A/Tg4eB87Mo9/ks7i73gr3cy20ga+nqiEOqnG5U0Gr8T9N1TjgbzBybBjUtpiSOIkxfHKlnqiPq/q6lrZUp6/NcR66/OqReWeVgwPLWeNfCWFv1AUBOmVeBg/eAMqzQvfG63GB/+8lz0L9Tmd9dRkr8EwaxiD2fYsAZEi/Cr0bbyDHHZjIGWYqdMQqjTpZt4UzEaqAqdEhSYRWhAP41fDwI7W6ctzO93E2mmd3VxLKujHTqvjej6Z9jUYZjQGFYZXkLsB5biK59vZQC1e0Z5wlwBvc9BC1OD4gj7nuq2ePF28vIrdicBvCwjJL2UNoaBa9lritllDZzYnieGnh4C9BvUxfBvF2YbAEnCVUcqNssKybXOrV/YH4pnPgA3UyR9zzrttc/W8x6E+LXsn3cPuDpqolC7ComMgdZI2jZb0ckhrbY6Rq2Slkl6JqWEapbkBXxyGWZXX8NW0rIUIj4O0UKkxYFZqNNWflbMwo7j9aigYq9JjSgNFSUc1DuJ3aPlbicr50P6udFPpsByfd1zXFYzJDndKMTWrwz6phP6X0ZeuREs6Nhxdsn3ag+v9b6e3lSfSnfJX5DAEN6GpDlvFk2u2/+uPRcAWSMMdsAN2QTf0wl7Yq/wzALRdybQ=).

**Points that do nothing for this spec:** **Improved Tactical Mastery** (3) only counts toward the points the tree needs before **Anger Management**, **Impale** and **Two-Handed Weapon Specialization**.

## Other builds of this spec

- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 900 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500305022100231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 886 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-553500050020100231--12)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 859 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013102-050530305022110231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 818 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530055021100231--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

