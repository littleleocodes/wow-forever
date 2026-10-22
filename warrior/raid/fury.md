# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**[Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md)** (20/31/0) — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-05250030052210501--7)

**Other setups of this spec.** This build is the Two-handed setup. The spec's best build for each other setup, in a full raid:

- Dual-wield: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (18/31/2, 883 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7)

## How to play

**Press the first one that is ready**, top to bottom:

1. **Whirlwind**
2. **Bloodthirst**
3. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
4. **Execute** when the target is below 20% health
5. **Hamstring**
6. **Bloodrage** when you have less than 90 rage

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Recklessness**: once a fight, in the last 33.75 seconds of the fight
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

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 881 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 887 | [18/31/2](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7) |
| Phase 1 BiS | 903 | [18/31/2](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-7) |

**The gear** (average item level: Pre-BiS 63.2; Phase 1 BiS 65.3; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Flameguard Gauntlets](https://www.wowhead.com/forever/item=19143) · *Molten Core*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Radiant Girdle of the Dawn](https://www.wowhead.com/forever/item=227814) | [Onslaught Girdle](https://www.wowhead.com/forever/item=19137) · *Ragnaros, Molten Core* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234021) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Main hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Cleaver](https://www.wowhead.com/forever/item=272592)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVl1oHFUU3jM/uycnyXZyk5LJjdUxSN2MTLwzu5NmW3Q3BaH6YkXB4ovZZjdmRbNhJ2IKKm1AKPWvIpQ2ook/gRj/2lp/KNIHrSWVDSSIBaWixKJC+xDxTRRlZncTXINISEPP091zz7n3+85+58ylBgQNdDAgBgJY2/IvSUAPpGE37IFh2A/ApzRUNOBPUhh/2Ksv1pOMH4ySgl+VNIrgq/OavhCmCJ49tUn/MUphPJjTv4v6jpKmT0RIwZ9+a6QI/voe+MkRvPw26N9HScE/jwApOPVmlGR87lFS8MN5/8Sz85p+xT9gfiFYKPjSC9Bh4VheO5fXn83HLk3A7ksnYM+hpw6BNJY/Cm9kJuGdzDR823scJqZgFmAnrbA7Ld0Qt+PCFXZcCMcSrnDjIu7awhG277WcWUlZlCairIETRwrHFLxwGlia305xZlO72YYyi34G9aTGVJx7gEmaylWSCWxiHRpFT1a2ztwfbEWqcXU84sdpR+5lxJGHSdEWXgT2MrD+zPAjDxaGRwxHON2WLSzhbDf6BzNDD+WyRqFoZLLZXNbYu88YGcwZxcJIZiRfGDK8XKbYP2jEvFzOGHisuM/KPm4VM/msVY2wyhFdD3uFoU6eoFt4JzWZm1Bh0l0hHiGV5ITrUYvJMBy4iJDCjm13uZ6PFKf72PUInNdm2ZX9jxvZ0dXQJ9cfvU2d/OZaHHHhETO1CnqkMCl2QnhcIUlvYtu4uxplR/yLsp0IKIdJwYuTwLbw9tqkbuH5fxhePgPM5fH/CyZeTtM+nVpLGr7+85puO3BqzWlPbIwWN9fiSrje9hAb3hgt1fl3GoCHG1kzbyL1S0lC8IsRU/Gj16DanXhiemX9/B93s2c2qFNvojazFVVWPwPL88cHRJLwVqD38hTZ7FbSzCiqTF6EUHUKtfO2wBtmUjFUTkyIKk0iNCCm4jeTwN5fjVDP+hPaRbexHbTFbK8lVe6+LttxPeKmjiqjGagyrMjT70x/hso4l2RjtYhF0nKuAuL2oEvkoIABDMfpcv364l8t7E4EfgftYMngY1BDaRn0fxLyJfX5YWCvwMZIvptibGsgCviHVCqzoMqye1uXW1EI4rkvgLXyzdTQQYQnwSc/3hzUYLxZl3+RZmFJcg7IocBa0jNSPdVRRJMF9PwOHW/Jdb4/tH8g3TZ+zLfzqRsHAruQcpYkXTFS5qwUuqZsJF1dXVXb+u6635OcK5VKDX3H070VR7oPDgIcg3xh6enz932dSgbe0Hyq148sla6k7ikvLqZMGT9p3Xndyhup/ObbFbz6BmEYRmGU/T0AJBINSQ==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVn9oW9UXz3k/ktPTLnu77ejr7Xdfn0VmGkm97yWvazY06UCY/uNEweE/NmtSG9Gm5FXcQHQrFGT+qoyNraKtSrFWp9uYPxgy/DFnJyl0iANlotSCwvZH/VcU5b4kLcYiUrri+evk3HPu/XxuPue8Sw0IBphgQQQEsJalX4qALkjDbtgDg3AAgL9hoGYAf4qC+MNec76eNFx4AUjDr0oGhfCVOcO8FKQQnj+z0fwxTCH8eBLM76TzxREwx0Ok4SdHgEL4yzsgy0N49S0wvw+ThiOH5T6/HwVS8blHScP35uSWo4fBvCY3OD9nSEfDEyPQFsPhvHEhbz6bjyyMw+6FU7Dn0JOHQBnOH4PXMxPwdmYKvu0+CeOTMAOwk5b5nVVuiNtx4Qo7LoQTE65w4yLu2sIRtozGnBlFm1fGw6yBE0cKRjS8fBZYmt9OcWZTa7QFVRb+FOpJj+g4+wBTDJ3rpBLYxNoMCp+uLJ27318KVfPqeEjmGUfvZcSRB0kzLr0I7CVgvZnBRx4sDA5ZjnA6Y7aICWe71dufGXgol7UKRSuTzeay1t791lB/zioWhjJD+cKA5eUyxd5+K+LlclbfY8X9sezjsWImn41VM2LljI6HvcJAO0/QLbydNkU3osaUuwI8RDqpCdejpijDoB8iQgo6tt3hehIpTvWw/yNwXltlV9Y/2MCOrYQ+ufbobWrnN9fiiAuPWNSooEcKkmYnhMc1UsxNbBt3V6LsiL9RthM+5SBpeGUC2BbeWlvUKTz5h+HVc8BcHv+3YOLlMuOjydWU4Ws/req0g2dWXfbE+mhxcy2uhOttD7DB9dFSnTzTAhzdwBr5JtK/VBQEeRkRHd9/Fardiaemlv3nf7ubPbNOnXoTtUSbUWf107A0fyQgUoS3DL2bp8hmt5IRDaPO1HkIVKdQK2/xo0GmFAPlwoSo0iRCCyI6fjMB7N2VCHWtPaFddBvbQVuirbWkyt3XYTuuRzxqos5oGqoMK/KUnSlnqIqzSTZci1gkY851QNzqd4nqX6APw3E6XHm/+EcTuxOB30E7WNL/GNRQWgL9j4SkpD4bBfYyrI/kOynCtvqigL9IpTILqiw7t3W4FYUgXvgcWDPfTA1tRHgaJPmxRv8OxhpN9WdlBhYV56Aa8K0pPa3UUx2FDFVA16/Q9qZaJ+OBA33plrHj0i6mbuzz7XLKWVRMzUpFZ5TAf8qG0lXvutrWE2t+TnK2VCo19JxMd1cC6R54GuA45AuLIxfv+zqV9KOBuVS3zCyVrqXuKTtXUlEVP2ze+b/lN1L51bfLf/f1wyDsg33szwEA9DYMhA==).

## Other builds of this spec

- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 870 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013031-55350000052010501--7)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (19/32/0, 853 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/04305013102-25050035102210501--7)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 839 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/20305012-55053005152010501--7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-22 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70425). Simulations, not in-game measurements. Do not hand-edit.*

