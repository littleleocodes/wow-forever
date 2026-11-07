# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md)** (18/33/0) — [open the talent tree](https://talentsforever.com/warrior/60/05303013102-050530305022110231--12)

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 862 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500305022100231--12)

## How to play

**Press the first one that is ready**, top to bottom:

1. **Bloodthirst**
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Whirlwind**
4. **Execute** when the target is below 20% health
5. **Hamstring**
6. **Bloodrage** when you have less than 23 rage
7. **Heroic Strike** when you have 68+ rage
8. **Bloodrage** when you have less than 90 rage

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Berserker Rage**: a cooldown, use it in the last 45 seconds of the fight (about 2 times a fight)
- **Recklessness**: once a fight, in the last 45 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a weapon in each hand: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in the short gaps and **Heroic Strike** only when rage piles up. **Death Wish** and **Recklessness** wait for the last 45 seconds.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 10-second cooldown) are your main attacks: press them the moment they are ready. **Whirlwind** now always hits with both weapons, and it needs **Berserker Stance**, the stance this list never leaves.
- Below 20%, **Execute** still comes after **Bloodthirst** and **Whirlwind**. It spends all your rage (600 damage plus 15 per extra rage point; 10 rage to cast with **Improved Execute**), so it takes the global cooldowns between them; a full raid gives you enough rage that the simulator measured this order slightly better.
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) and **Recklessness** (+100% crit chance for 15 seconds) wait until about 45 seconds are left, so they cover the execute phase. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) fills a global cooldown only when **Bloodthirst** is more than a second away and **Whirlwind** more than 1.5 seconds: it is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem, but it must never delay your main attacks. The simulator measured 1.9% more damage with this rule than with **Hamstring** only above 80 rage.
- **Heroic Strike** is a rage dump, not a filler: queue it only at about 68 rage or more on a single target. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**; in Forever it also no longer helps your off-hand hit. The simulator measured 0.9% more damage at 67.5 rage than at 45.
- **Bloodrage** waits until you are under about 23 rage, so it refills an empty bar instead of topping up a full one. The simulator measured 1% more damage than pressing it whenever you are under 90.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one early, one in the last 30 seconds). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 11% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage **Cleave** replaces **Heroic Strike** (the full list does this).
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and skip **Hamstring**. That is the simulator's rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** was worth 12%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** also makes you immune. The simulator's boss never fears, so the list leaves it out.
- With a two-hander (the page's two-handed option), drop **Heroic Strike** and cast **Hamstring** whenever nothing else is ready: in the simulator's two-handed raid rotation those two changes were worth 5.3% and 6.8%. That rotation also uses **Bloodrage** under 90 rage and puts **Whirlwind** before **Bloodthirst** when **Bloodthirst** is more than 1.5 seconds away.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 887 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 977 | [18/31/2](https://talentsforever.com/warrior/60/31303013002-050530305020100031-2-12) |
| Phase 1 BiS | 981 | [19/31/1](https://talentsforever.com/warrior/60/30303213002-350530005020100031-1-12) |

**The gear** (average item level: Pre-BiS 66.9; Phase 1 BiS 66.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Field Marshal's Plate Shoulderguards](https://www.wowhead.com/forever/item=16480) · *sold by Sergeant Major Clate* | [Field Marshal's Plate Shoulderguards](https://www.wowhead.com/forever/item=16480) · *sold by Sergeant Major Clate* |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587) · *sold by Illiyana Moonblaze*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587) · *sold by Illiyana Moonblaze*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Marshal's Plate Gauntlets](https://www.wowhead.com/forever/item=16484) · *sold by Sergeant Major Clate*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Marshal's Plate Gauntlets](https://www.wowhead.com/forever/item=16484) · *sold by Sergeant Major Clate*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) · *quest: A Collection of Heads* | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) · *quest: A Collection of Heads* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Marshal's Plate Boots](https://www.wowhead.com/forever/item=16483) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Marshal's Plate Boots](https://www.wowhead.com/forever/item=16483) · *sold by Sergeant Major Clate*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) · *sold by Gaelden Hammersmith* | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) · *sold by Gaelden Hammersmith* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) · *quest: The Qiraji Conqueror* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) · *quest: Job Opening: Guard Captain of Revantusk Village* |
| Main hand | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Grand Marshal's Longsword](https://www.wowhead.com/forever/item=12584) · *sold by Lieutenant Jackspring*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345) · *sold by Sergeant Thunderhorn*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [High Warlord's Blade](https://www.wowhead.com/forever/item=16345) · *sold by Sergeant Thunderhorn*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3v2pN1Ob1o7uWl1DKVup268M7uTZKOYTVHxB7HqQ4svZpPdmBXJht2ILYhu4ouolEq1NCsl0RoI0YqWqqVIHiyWKhSMYKCiGNKCgj5U8EFErdzJbmLXPEhI1/swObnnnNzvu983JwxtRTDABAui0AMDMAQlgBcBJgCmANg6P6vIbAfw0mbUDODPkY7zveZCA2l4/CiQhvMloBCenQRzVpfBqQ3mpQiF8IUxML+TweUSmOMh0vC3Y7Lyl/dAtofwUgnM7yOk4Z9H5N/5elI+P/zSIA3ffx1Ix6le8+cI6XjxeflTw69mjZaocS4XvTwOe+YOwr5fe14CZTRXhvDx9Lvpb7rHJ2EalFdyV2A0txt9+JCCM8pNcScuPOHEhXBjwhNeXMQ9R7jCkbsx97yiLSilRraOE0fSoxrOnQGW4ndSnDnUbDehyiKfQgMFo0G88BhTjCAPkkrgEGsxKHKykprZ66dC1bowD8k648ijjDhynTRj9lVgbwDrSw899Xh+aNhyhdsWc0RMuJ1W30B68IlsxsoXrHQmk81YvQes4YGsVcgPp4dz+UGrmE0X+gasaDGbtfqfLhyIZZ6JFdK5TKxaEVusaH2ymB/cyRO0i++kjfYG1Jhyf4CHKEhqwivSJpuh7m8RIemu47R6RYkUp3rYjQic13Y5lfzH69nRldAn1x69Qzv5LbU44qJIzDYq6JF00pyEKHKNFJOzdu6tRNkV/6LsJHzKOmn47QSwbby5tqlNFKVg+NMMMI/H/yuY+GKb8cnkatrwrR9WddrIqVW35WvVdGIisfZq+u7Hw4cfZu+s4J+4s/Yn3kV3sE7awbcTlTFEqnF1l8Gr8city/FozuBk2BEpbSEgcZLieBVLPVufV3VzrWwJr9gZYEP1edXC8kwrgofWs0a+kYJfKAqC9Eo0iB+9CdXhhR9MLccH/3iIvQz1uZ3t1GRvwSBrmIal8SwBkSKKy9C7eRc57DZfyiBTFyBQHdLNvMnf1ZcFTogqTSK0IBrEixPATqxAyG1fe0L30O0sSdvs5lpS/jx2Wh3XK5Jp34BBRtNQZVixpk85quKFJButxSuSMbdj7fE2+yNE9a/Pn3Ou2+rJ28Wrm9h9CPxun5D8T1lDyK+Ws5a4bdbQWcpJYnj2ELBjUB/Dt1GU7fAtAdcYpTIoqyzb2lu9ij8Qz30GrFQnfyzaVV22a1JUb3sG6jOw99KD7AF/hErhdBaeBqmSNGm4HKqEtNXmqF8jKpVD1ZgaFlBaG/C1CVjSeAvfTOtaiPAkSErlRp9ZudFUf1TOwxXFHVED/tqUmlYaKEwhVKMgfoeWv5Sw3A+U+lNN5TG5Pu+6ud9fc13uvGJqVpd9Wgn8L2s4VY2u69px4rqdk/Sfj7yd6q5spHrk18AY+L8E5rtsFU9v2f2PjwYBHZCCe2EP7IMBGIL9sF/5ewDyGqIc); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3v2pN1Ob1o7uWl1DKVup268M7uTZKOYTVHxB7HqQ4svZpPdmBXJht2ILYhu4ouo1Eq1mJWS+BMI0YqWqqVIHiyWKhSMD4GKYkgDCvpQwQcRtXInu4ld8yAhXe/D5OSec3K/737fnDC0HcEAEyyIQg8MwBCUAJ4HmACYAmAb/Kwisx3AS1tRM4A/QzrO95oLDaTh4stAGs6XgEJ4dhLMWV0GpzaZlyIUwufGwPxOBoslMMdDpOFvx2XlL++DbA/hpRKY30dIwz+Pyb8zMymfH31lkIYfvAak41Sv+XOEdLz4rPyp4dezRkvUOJeLLo7DvrnDcODXnhdAGc2VIfx2+r30N93jkzANyku5yzCa24s+fEjBGeWGuIgLz3XiQrixuCe8uBCeI1zhCE84Mee8oi0opUa2gRNH0qMazp0BluK3U5w51Gw3ocoin0EDBaNBvPAIU4wgD5JK4BBrMShyspKa2e+nQtW6MA/JOuPYw4w4cp00Y/YVYG8A60sPPfFofmjYcoXbFnNETLidVt9AevCxbMbKF6x0JpPNWL2HrOGBrFXID6eHc/lBq5hNF/oGrGgxm7X6nywcimWeihXSuUysWhFbqmh9vJgf3M0TtIfvps32JtSYcm+AhyhIasIr0haboe5vESHpruO0ekWJFKd62PUInNd2OZX8JxvZ66uhT64/eod285tqccRFkZhtVNAj6aQ5CVHkGikmZ+3cW42yK/5F2Un4lHXS8NsJYDt4c21TmyhKwfCnGWAej/9XMPGlNuPTybW04Vs/rOm0kVNrbsvXqunERGL91fTdj0ePPsjeXcU/cWf9T7yDbmOdtIvvJCpjiFTjyh6DV+ORm1fi0ZzBybAjUtpCQOIkxfEqlnq6Pq/q1lrZEl6xM8CG6vOqheWZVgSPbGSNfDMFv1QUBOmVaBA/fhOqwws/nFqJD//xAHsR6nM7O6nJ3oZB1jANy+NZAiJFFFegd/MuctgtvpRBpi5AoDqkm3mTv6uvCJwQVZpEaEE0iBcngJ1YhZDbvv6E7qJbWZJ22M21pPx57LQ6rlck074Og4ymocqwYk2fclTFC0k2WotXJGNux/rjbfZHiOpfnz/nXLfVk7eLV7awexD4nT4h+Z+yhpBfLWctcdusobOck8Tw7BFgx6E+hm+jKNvlWwKuMkplUFZZtrW3ehV/IJ77HFipTv5Ysqu6YtekqN72DNRnYO+n+9l9/giVwuksPA1SJWnScDlUCWm7zVG/SlQqh6oxNSygtDbgqxOwrPE2vpU2tBDhSZCUyo0+s3Kjqf6onIfLijuiBvy1JTWtNFCYQqhGQfwOLX8pYbkfKPWnmspjcn3RdWO/v+a63HnF1Kwu+7QS+F/WcKoaXdO168Q1OyfpPx96J9Vd2Uj1yK+BMfB/Ccx32Sqe3rb3Hx8NAjogBXfDPjgAAzAEB+Gg8vcAiB+iPQ==).

## Other builds of this spec

- [Fury — Raid](../research/raid/builds/fury-open-raid.md) (18/31/2, 892 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013102-050530305021100231-2-12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 850 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-553500050020100231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 841 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530055021100231--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-07 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 02bd77c (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

