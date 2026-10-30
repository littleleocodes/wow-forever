# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Raid](../research/raid/builds/fury-open-raid.md)** (18/31/2) — [open the talent tree](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fury — Dual Wield), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 845 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-25050034102210501--7)

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

- **Recklessness**: once a fight, in the last 45 seconds of the fight
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fury in a raid fights in **Berserker Stance** with a weapon in each hand: **Bloodthirst** and **Whirlwind** on cooldown, **Execute** in the gaps below 20%, **Hamstring** in the short gaps and **Heroic Strike** only when rage piles up. **Death Wish** and **Recklessness** wait for the last 45 seconds.

**Why it works**

- **Bloodthirst** (30 rage, 6-second cooldown) and **Whirlwind** (25 rage, 22 with **Raging Blows**, 10-second cooldown) are your main attacks: press them the moment they are ready. **Whirlwind** now always hits with both weapons, and it needs **Berserker Stance**, the stance this list never leaves.
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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 925 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 919 | this build |
| Phase 1 BiS | 923 | this build |

**The gear** (average item level: Pre-BiS 62.6; Phase 1 BiS 62.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gauntlets of Heroism](https://www.wowhead.com/forever/item=21998)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Gauntlets of Heroism](https://www.wowhead.com/forever/item=21998)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Cleaver](https://www.wowhead.com/forever/item=272592)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Cleaver](https://www.wowhead.com/forever/item=272592)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHFUU3jM/OycnaTq5Sc3kxuoYpE5GNt6Z3UmyFcymoKgvFn2w+GK22Y1ZkSTsRGzBhzS+iEqpD5YmUhKtwZC2UkvVUqQPtpYqFhKFgKIYoqBQkQo+iPjHnd1tdM2DhHQ9D8vd8zP3+85+5+zQzQgmWGCDAwMwDGMwAfA8wCzAPABriKKKjPYCf7MJNRP4BFAcV/Zaq/Wk4bEjQBp+9olJBl6YA2spTgZePLPV+qaRDHxuCqyv5OHH42DNGKThL0eBDPzpLZDlBl49DtbXjaThiVNNpOHvh+XT3lk0ScNTr8jMi4um9YN8wuJSdNDw0yWzwzEvFZxvZ2D38kHY8/PAC6BMFqah7lj2RPaL/pk5WADlpcI1mCzsaljjl4Fzyq1JLykC4SWF8BMiEEFSJANP+MKT3oR/WdFWldmtrIETR4o7Gi6fA5bh91CSedTutqHKGj+AetIdHa88xhRT5zqpBB6xDpMaT5dD5x+NQkYlr44bMs88/AgjjjxOmrn0MrBXgQ1mx556fHRs3PaF353wREL4O+3B4ezIE/mcPVq0s7lcPmfv3W+PD+ft4uh4drwwOmKH+WxxcNh2wnzeHnq6uD+ReyZRzBZyiUpGopTR9WQ4OtLJU3Qn76QmdytqTHkwxg3SSU0FIbW4DOORiwgp7nteVxBKpDg/wG5B4Ly6yivH39vCjqyHPr356D3q5HdU40iKkJhrltEjxUnzUiLkGikWZz08WI+yL/5F2UtFlOOk4ZezwLbz9uqibhHKHwyvngcW8OR/BZMslZnvz22kDF//bkO3HTiz4bJna6PFbdW4UkG4M8bGaqOlOnmnDXhoC2vmTaR/rCgIshmOju++BpXpxLfn184Hf3uIvVijSb2d2txW1Fn9AlzfPxIQKSJcg97P+8hjd5HpNqLO1FWIVbZQO2+LvHGmFGOlwpSo0CRCGxwdP58FdnIdQn7P5hO6j+5madrutleTKk1fl+cHIVnuTagzWoAKwxJyL6LsqHglzSar8Yp0wu/dfLzt0YyoUfuiQfb9rkB2F/9sYQ8g8HsjQvKvoIpQlC2XCXHXqqJzPSaJ4YVDwI5CbQTfTQ7bEUkC/iGU8iaosOzu6QrK+kC89CGwiRrpoyRXdU2uaVHpdivfRg0dRHgapGe6OQpMN1vq98pluKb4B9RYZC2ZBaWe6shA1QHxK3T8odRJf2xiKNM2PSXto77bhiJb7vNXFEuz+9yzSux/sfFM5XRDbcfJG3ZPOvp8+I1Mf9mRGZAvjVMQfYmt9Lkqnm3d9bd3SwG9kIH7YTfsgWEYg32wT/lrAJibIBg=); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEVl1oHFUU3jM/OycnaTK5Sc3kxuoYpE5GNt6Z3UmyFcymoKgvFn2w+GK22Y1ZkSTsRGzBhzS+iEqtDxYTqYk/xZC2UkvVUqQPWksVC4lCQFEMsaBQkQo+iPjHnd1tdM2DhHQ9D8vd8zP3+85+5+zQ9QgmWGCDA4MwAuMwCfA0wBzAPABriKKKjPYBf7MZNRP4JFAcV/ZYq/Wk4aXngTT8/FOTDHxl0bSW4mTguVNN1reNZOBT02B9LQ8/HgVr1iANfzkMZOBPb4EsN/DyUbC+aSQNj51oJg1/PySf9s6iSRqeeFFmnls0rR/kExaXooOGny2ZnY55vuBcmoVdywdg98+Dz4AyVZiButezx7JfDswegQVQnitcganCzoY1fhk4o9yY9JIiEF5SCD8hAhEkRTLwhC886U34FxRtVZlrYg2cOFLc0XD5DLAMv4OSzKMOtx1V1vgB1JPu6HjxIaaYOtdJJfCIdZrUeLIcOvtgFDIqeXXckHnmoQcYceRx0sylF4C9DGwoO/7Yw2PjE7Yv/J6EJxLC32EPjWRHH8nn7LGinc3l8jl7zz57YiRvF8cmshOFsVE7zGeLQyO2E+bz9vDjxX2J3BOJYraQS1QyEqWM7kfDsdEunqJbeRc1u02oMeXeGDdIJzUVhNTqMoxHLiKkuO953UEokeL8ILsBgfPqKq8cf28Le2k99OnNR+9RF7+lGkdShMRcs4weKU6alxIh10ixOOvlwXqUffEvyl4qohwnDb+aA7aNd1QX9YhQ/mB4+SywgCf/K5hkqcx8/8hGyvC17zZ02/5TGy57sjZa3FqNKxWEO2JsvDZaqpN32oAHt7AW3kz6J4qCIJvh6Pjuq1CZTnx7fu184Lf72LM1mtSbqd1tQ53VL8DV/SMBkSLCNegDvJ88dhuZbiPqTF2FWGULdfD2yBtnSjFWKkyJCk0itMHR8Ys5YMfXIeT3bj6hu+h2lqZtbkc1qdL0dXt+EJLlXoc6owWoMCwh9yLKjooX02yqGq9IJ/y+zcfbEc2IGrUvGmTf7w5kd/HPVnYPAr8zIiT/CqoIRdlymRB3rSo6V2OSGH54ENhhqI3ge8hh2yNJwD+EUt4EFZY9vd1BWR+I5z8CNlkjfZTkqq7JNS0q3W7jW6mhkwhPgvTMtESBmRZL/V65AFcUf78ai6w1s6DUUx0ZqDogfoXOP5Q66Y9NDmfaZ6alfdx/03Bky/3+imJpdr97Won9LzaRqZyuqW0/fs3uSUef97+RGSg7MoPypXEaoi+xlX5XxdNtO//2bimgDzJwN+yC3TAC47AX9ip/DQCrSyBl).

## Other builds of this spec

- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 914 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013102-05053035102210501--7)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 875 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/20305012-55053005152010501--7)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 828 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013031-55350000052010501--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

