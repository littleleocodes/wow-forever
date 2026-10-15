# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**[Fury — Raid](../research/raid/builds/fury-open-raid.md)** (18/31/2) — [open the talent tree](https://talentsforever.com/warrior/60/31305013002-05053035102010501-2-6)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (arms-2h-raid), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0), 881 DPS in a full raid — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-05250030052210501--6)

## How to play

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst**
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Whirlwind**
4. **Execute** when the target is below 20% health
5. **Hamstring**
6. **Bloodrage** when you have less than 23 rage
7. **Heroic Strike** when you have 68+ rage

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
- **Death Wish** (+20% physical damage for 30 seconds, 3-minute cooldown) and **Recklessness** (+100% crit chance for 15 seconds) wait until about 45 seconds are left, so they cover the execute phase; the line above that says to use **Death Wish** at the start does not match the rotation. Crits give double rage in Forever, so the **Recklessness** window also feeds bigger **Execute** hits. The simulator measured 0.7% more damage with **Death Wish** at 45 seconds than at 30, and in fights longer than about 3.5 minutes it presses it at the pull as well.
- **Hamstring** (10 rage) fills a global cooldown only when **Bloodthirst** is more than a second away and **Whirlwind** more than 1.5 seconds: it is a cheap extra main-hand hit that can trigger on-hit effects such as a shaman's Windfury Totem, but it must never delay your main attacks. The simulator measured 1.9% more damage with this rule than with **Hamstring** only above 80 rage.
- **Heroic Strike** is a rage dump, not a filler: queue it only at 67 rage or more on a single target. It replaces a white swing, and white swings are your steady rage (each gives rage in proportion to your weapon's speed, double on a crit), so an early one starves **Bloodthirst** and **Whirlwind**; in Forever it also no longer helps your off-hand hit. The simulator measured 0.9% more damage at 67 rage than at 45.
- **Bloodrage** waits until you are under about 22 rage, so it refills an empty bar instead of topping up a full one. The simulator measured 1% more damage than pressing it whenever you are under 90.

**Caveats**

- The page's numbers assume a **Recklessness** in every fight and two Mighty Rage Potions (one early, one in the last 30 seconds). **Recklessness** has a 30-minute cooldown, so you will not have it on every boss: the simulator measured 11% more damage with it than without.
- With several targets, **Whirlwind** hits up to 4 of them, and above 40 rage **Cleave** replaces **Heroic Strike** (the full list does this).
- The simulator ignores threat. **Heroic Strike** causes a high amount of threat, so it is the first thing to stop if you pull aggro. **Death Wish** and **Recklessness** also make you take 5% and 20% more damage.
- Stand behind the boss: from the front it can parry and block, and a swing that does not land gives you no rage.

**When to change it**

- Alone or in a small group (fewer buffs, less rage), put **Execute** first below 20%, stack **Sunder Armor** to 5 yourself and skip **Hamstring**. That is the simulator's rotation for a warrior alone on a training dummy, where stacking **Sunder Armor** was worth 12%.
- If nobody in your group has **Battle Shout** up, keep it up yourself (3 minutes), and put one **Sunder Armor** on a boss that has none: the list leaves both out because the simulator's raid already had them.
- Before a boss's fear, press **Berserker Rage** (30-second cooldown, 10 seconds of fear immunity); **Death Wish** also makes you immune. The simulator's boss never fears, so the list leaves it out.
- With a two-hander (the page's two-handed option), drop **Heroic Strike** and cast **Hamstring** whenever nothing else is ready: in the simulator's two-handed raid rotation those two changes were worth 5.4% and 6.6%. That rotation also uses **Bloodrage** under 90 rage and puts **Whirlwind** before **Bloodthirst** when **Bloodthirst** is more than 1.5 seconds away.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 917 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 938 | this build |
| Phase 1 BiS | 943 | [18/32/1](https://talentsforever.com/warrior/60/21305113002-25053005102012501-1-6) (ties this build) |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 64.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Battleborn Armbraces](https://www.wowhead.com/forever/item=12936) · *Warchief Rend Blackhand, Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/spell=13828) | [Flameguard Gauntlets](https://www.wowhead.com/forever/item=19143) · *Molten Core*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/spell=13828) |
| Waist | [Radiant Girdle of the Dawn](https://www.wowhead.com/forever/item=227814) | [Onslaught Girdle](https://www.wowhead.com/forever/item=19137) · *Ragnaros, Molten Core* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Feet | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Boots of Heroism](https://www.wowhead.com/forever/item=21995)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234021) | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Main hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Cleaver](https://www.wowhead.com/forever/item=272592)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVl1oHFUU3jM/uycnyXZyk5LJjdUxSN2MTLwzu5NmW3Q3BaH6YkXB4ovZZjdmRbNhJ2IKKm1AKPWvIpY2ook/gRj/0lpUivTBn5LKBhLEglJRYlGhfYj4Jooys7sJrkEkpMHzdPfc8+39vrvfOXupAUEDHQyIgQDWtvJJEtADadgL+2AYDgLwKQ0VDfjjFMbv9+tL9STj+6Ok4JcljSL4yoKmL4Ypgp+d3qL/EKUwHs7p30b9REnTJyKk4I+/NlIEf3kXfHAEL78F+ndRUvCPY0AKTr0RJRmfeZgUnH0RfNyCpl/xv2BhMVgo+MJz0GHhWF47l9efzscuTcDeSydh35EnjoA0lj8Or2cm4e3MNHzTOwsTUzAHsJtW1Z2RrovbceEKOy6EYwlXuHERd23hCNvPWs6cpCxJE1HWwIkjhWMKXjgDLM1vpTizqd1sQ5lFP4F6UmMqzt/HJE3lKskENrEOjaKnKltn7w22ItW6Oh7x67RjdzPiyMOkaIvPA3sJWH9m+KH7C8MjhiOcbssWlnB2Gv2DmaEHclmjUDQy2Wwua+w/YIwM5oxiYSQzki8MGV4uU+wfNGJeLmcMPFI8YGUftYqZfNaqVljliq4HvcJQJ0/QTbyTmswtqDDpjhCPkEpywvWoxWQYDlJESGHHtrtcz2eK033sWgTOa1F2Zf/DRnZ8LfbJjWdvUye/sZZHXHjETK3CHilMip0QHldI0pvYDu6uJdkR/5BsJwLJYVLw4iSwbby9FtQtPP8Hw8tngbk8/l/JxMsw7eOp9cDwtZ/Wddqh0+uGPbY5XtxayyvhejtDbHhzvFTnn2kAHm1kzbyJ1C8kCcG/jJiKH7wK1e7Ek9Or62d/v5M9tUmdegO1ma2osvoZWJk/PiGShLdKvZenyGY3k2ZGUWXyEoSqU6idtwXZMJOKoTIwIaoyidCAmIpfTwJ7by1BPRsvaA/dwnbRNrO9VlS5+7psx/WImzqqjGagqrBiT78z/Rkq43ySjdUyFknLuQqM24MukYMLDGg4Tpfr3y/+2cJuR+C30S6WDP4MaiStkP5XQb6lPj0K7GXYHMt3U4xtD0wBf7NKZRZUVXbv6HIrDkE89zmwVr6VGjqI8BT44sebgzsYb9bln6U5WJacQ3IoiJb0jFRPdRTRZAE9v0HHm3Kdnw8dHEi3jZ/w43zq+oEgLqScZUlXjJQ5J4X+VzGSrq6uamx/Z8PPSc6XSqWGvtl0byWR7oPDACcgX1h+8vw9X6WSQTa0kOr1K0ulK6m7youLKVPGj1p3X7P6Riq/+fYEr75BGIZRGGV/DQAxbAz6); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warrior/dps/#eJzMVm9oW1UUz3l/8k5Pu+z1tqOvt06fRWYaSb3vJa9rNjTpQJh+caLgEMFmTWoj2pS8iBvI2AoFmf8qY2OraKtSrdXpNobKkOGfOTtJoUMcKBOlFhS2D/WrKMp7SVqMRaR0xfPp5Nzzy/39bn7n5lIDgg4GmBAGAax16ZMkoBtSsAt2wxAcAOBv6qjowPdTEH/cY8zXk4ILLwIp+HVJJw1fndONS0HS8PyZjcZPIdLwk0kwvveSL4+AMa6Rgp8eAdLw1/fAg2t49R0wfgiRgiOHve/54yiQjG89TDI+/wRpOHoYjGse/vyc7iUKnhiB9igO5/QLOeO5XHhhHHYtnILdh/YfAmk4dwzeSE/Au+kp+K7nJIxPwgzADlqWd1a6ybZiwrGsmBB21HaEExPCsYQtLNsRVtSakZR5aTzEGjhxpGBYwctngaX4nRRjFrVFWlFmoc+gntSwirMPMUlXuUoygUWsXafQ6crSuQf9Ja3aV8c1r08/ej8jjjxIin7pJWAvA+tLDz3+SH6oaNrC7opaIirsbWbfQHrw0WzGzBfMdCaTzZh79pnFgaxZyBfTxVx+0HSz6ULfgBl2s1mz/8nCvmjmqWghnctEqx3RckfnY25+sIPH6TbeQY2Rjagw6Z4A10glOe641BxhGPRLREhB27I6HddjilO97EYEzmtRVmX9ww3s2ErsE2vP3qIOfmstj5hwiUX0CnukIClWXLhcIcloZFu5s5JkW/xDshX3JQdJwSsTwDbztlpQl3C9HwyvngPm8Nh/JRMrw/SPJ1cDw9d/XtVuB8+sGvb0+nhxUy2vuONuC7Ch9fFSnbenCTi6gTXxRlK/kiQE7zDCKn7wGlSnE09NLecv/H4ve3adJvUWao20oMrqp2Hp/vEIkSTcZeo9PEkWu530SAhVJs9DoHoLtfFWvxpkUiFQBsZFVSYRmhBW8dsJYO+vJKh77QXtpDvYdtocaasVVZ6+Tst2XOIRA1VG01BVWLGnN5neHSrjbIIN1zIWiah9HRi3+VMi+wfo07DtTsc7X/yzmd2NwO+i7Szh/xnUSFoi/a+CPEt9PgrsFVgfy3dRmG3xTQF/s0rlLqiq7Nra6VQcgnjhC2AtfBM1tBPhafDEjzX5ZzDWZMi/SDOwKNkH5YAfzalpqZ7qSNNlAd2/Qfvbcp1XDxzoT7WOHffiYvLmfj8uJ+1FyVDMZGRGCvyvopiqZtc1tpxY830Ss6VSqaH3ZKqnUkj1wjMAxyGXXxy5+MA3yYRfDcwle7zOUula8r5yciUZkfGjlh03LL+Ryo++nf6zbwCGYC/sZX8NAEOKC+8=).

## Other builds of this spec

- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 881 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013032-05250030052210501--6)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (19/32/0, 879 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/04305013102-25050035102210501--6)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 875 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/20305012-55053005152010501--6)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 870 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/03305013031-55350000052010501--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

