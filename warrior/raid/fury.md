# Fury Warrior — Raid (group)

[Warrior](../README.md) > [Raid (group)](README.md) > Fury

**✅ Recommended** for raid (the best warrior spec here, or within 3% of it).

**[Fury — Dual-wield](../research/raid/builds/fury-dual-wield-open-raid.md)** (17/32/2) — [open the talent tree](https://talentsforever.com/warrior/60/32303013002-050530205122100231-2-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Dual-wield setup. The spec's best build for each other setup, in a full raid:

- Two-handed: [Fury — Raid](../research/raid/builds/fury-open-raid.md) (20/31/0, 856 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/32303013032-050530310122120231--12)

## How to play

**Setup, before the pull:** **Berserker Stance**: the simulator starts the fight in it, and the rotation below assumes it.

**Then press the first one that is ready**, top to bottom:

1. **Bloodthirst** until the last 30 seconds of the fight
2. **Death Wish**: a big cooldown, save it for the last 45 seconds of the fight
3. **Reckless Swings**
4. **Whirlwind**
5. **Execute** when the target is below 20% health
6. **Hamstring** when **Bloodthirst** is more than 1.125 seconds from ready and **Whirlwind** is more than 2 seconds from ready
7. **Bloodrage** when you have less than 23 rage; no global cooldown, so press it alongside the others
8. **Heroic Strike** when you have 68+ rage; no global cooldown, so press it alongside the others

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
| Arms | 17 | Improved Heroic Strike 3, Deflection 2, Improved Rend 3, Improved Tactical Mastery 3, Anger Management 1, Deep Wounds 3, Impale 2 |
| Fury | 32 | Cruelty 5, Unbridled Wrath 5, Furious Precision 3, Dual Wield Specialization 5, Reckless Swings 1, Improved Execute 2, Improved Berserker Rage 2, Death Wish 1, Improved Whirlwind 2, Flurry 3, Bloodthirst 1, Blood Craze 2 |
| Protection | 2 | Improved Bloodrage 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 858 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 908 | [17/32/2](https://talentsforever.com/warrior/60/32303013002-150530205121100231-2-12) |
| Phase 1 BiS | 883 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 63.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Deeprock Bracers](https://www.wowhead.com/forever/item=21184) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Gauntlets](https://www.wowhead.com/forever/item=271940)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* | [Valiant's Waistguard](https://www.wowhead.com/forever/item=272403) · *sold by Pix Xizzix* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Windreaver Greaves](https://www.wowhead.com/forever/item=13967) · *Kirtonos the Herald, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Blackguard](https://www.wowhead.com/forever/item=19168) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Ironwood Blade](https://www.wowhead.com/forever/item=279259) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Persuader](https://www.wowhead.com/forever/item=22384) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* | [Satyr's Bow](https://www.wowhead.com/forever/item=18323) · *Zevrim Thornhoof, Dire Maul* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHNUX3zMzO3v2pN1Ob9p/JzftnzGUup268c7sTtpUMdui4gdi1YcWEcy2u3VXtBt2IqbQhyYoiB9tJSLtqiR+BEO0BWvVUiSI1lKlhRYh4BeGKCjYhwg+VbFyp7tZu8mDhGS9D8vZe87h/n7395szDK1GMMAEC+LQDXnogf0AzwAMA4wCsCVBVpHZTcAvr0TNAL6PdJzcaU41kYrv95GGX50zSMdX8+ZFnSJ4+sQy88cYRfCTETC/l8Hpc4Y5FCENBy8YFMHfjoFs1vHg4+YPMdLwhUsGaXj4gkEqvv0QafhBUDd9DMxLsv/bp5fLQMPBg9AWN84U4j8NwbaJA7Dj9+5nQRkolCH6ZubdzDdbhkZgDJTnC9MwUNiKAXhIwynFSrpJkRROUgg34XjCSwpXeI7rOEK4SSfhnlW0KeWPZvYUsF2ZnsceLvb0Wq5wOxKOkxCbNlu78pk9j+SyVrFkZbLZXNbaudfqzeesUrE301so7rH8XKa0K2/F/VzO2v1EaW8i+2SilClkE9WKxNWK9kf94p71fA0tt5ehzpS7QjxCYVKTwudIelzDiVPA0vwWSjKHWu0WVFnsU2iicDyM5x9kihHmYVIJHGJtBsWOV1Lj24NUpFoX5RFZZ7z8ACOOXCfNuPgisFdm8RMJ4S48vxRt4OsDjlqNY8rzaYXNKrSJkHTXcdo9XyLF0W72fwTO67ucSv6jpezwXOg7Fx69Q+v59fU4ksInZhsV9Eg6aU5K+FwjxeRsI/fmouyKWZSdVEBZJw2/Gwa2hrfWN3UIXwqGv44D83jy34KRFpI6fzwynzZ84+d5ndZ/Yt5txXo1nYRILbyagftxcPA+9s4c/kk6C3/irXQz20zr+FqiMkZINa5sMHg17r+hFg8UDE6GHZPSlkISJymOV7HUvsY8qivrZUt5/uYQ62nMoxaVZ1oxPLSUNfPlFP5SURCkV+Jh/PB1qA4vfG+0Fh/48172HDTmdtZSi70Kw6xpDGbGswREivBr0LfwLnLYjYGUYaZOQag6pFt5S7Cr1wROiSpNIrQgHsavh4EdbdCb53a6iXXSGru1nlQwj512x/V8Mu3/YZjRGFQZXkXuBpTjKp7vZAP1eEVnwl0EvK3BCFGD6wvmnOu2e/J28coKdicCvy0gJN+UdYSCajlridtmHZ2ZnCSGnx0C9ho0xvAdFGfrAkvANUapDMoqy46N7V7FH4hnPgc20CB/zLrvjo21+x6Hxozs7XQPuzsYolI6nUXHQOokbRotRyohrbY56tfISuVINaamKZTmBnxpGGZUXsVX0pI2IjwO0kLl5oBZudlUf1HOwrTi9quhYK1IjylNFKUIqnEQl6HtLyUq90P7d6dbykfk+qLrut3BmuhyJxVTs7rsk0roP1m96Wq0qGvd0UU7pzP4vf+t9JbKRrpbfoccgeBPaLLLVvHkqq3/+FwRsAnScAdsgx2Qhx7ogz7l7wEArzTIbg==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warrior/dps/#eJzEV11oHFUU3jMzO3v2pN1Ob1o7uWllDKVup268M7uTNlXMtqj4g1j1oUUEs+1uzYp2w07EFkTaoCAqbSUqdkUbf4Il2oKlaikSRGup0kKLUFAUQywo6EMEn7RYube7WbvJg4RkvQ/h5J5z9n7f/b45w9ByBAtscCAJvdAH/bAb4DmAYYBDAGyBymoyuw74paVoWMCfJhPHt9oTLWTgxX1ABn5zxqIYvnnOss+bFMOTxxbZPyUohp+NgP2DDE6eseyDMTJw6Jys/P0IyHYT9z1u/5ggA58dkj8zNgKk43sPkYEfqbrxV8D+TfZPHlGBgUP7oCNpnSomLx6ETRf2wpY/ep8HbbBYgfg7uQ9y3204OAKjoL1YnITB4kZU8CELJzQn7adFWnhpIfyUCESQFr4IPN/3hPDTXso/rRkT2l+t7Blg23L9jz1c6h9wfOF3pTwvJdatd7b15XY8Usg7pbKTy+cLeWfrLmegr+CUSwO5gWJphxMWcuVtfU4yLBSc7U+Ud6XyT6bKuWI+VatIXanofDQs7VjNV9BidxGaTLsrwmMUJT0tQo5kJg28cAJYlt9CaeZRu9uGOkt8Di0UTUbx7INMs6I8SjqBR6zDosTRampss0rFanVxHpN11qsPMOLITTKs8y8Be30aP5ES/tzzy9AavlpxNOocM0FIS1xWpU2EZPqe1xmEEike6mXXInDe2OVV858sZK/NhL577tF7tJpf34gjLUJirlVFj2SS4WVEyA3SbM7W8mAmyr6YRtnLKMomGfj9MLAVvL2xqUuEUjD8dQxYwNP/FYy0kNT505HZtOHbP8/qtD3HZt1WalTTS4nM3Kup3I9DQ/ex92fwT9qb+xNvpZvZelrFVxJVMEa6dXmNxWvxnhvq8WDR4mS5CSltOSJxkuYFVUs91ZxHdWmjbJkgXB9h/c151OLyTCeB+xeyVr6Yol9rGoL0SjKKH78FteGFHx6qx3sv3ctegObczkpqc5dhlLWMwtR4loBIE2Ed+gbeQx67UUkZZfoERGpDup23qV2zLnBG1GgSoQPJKH47DOxwk948t9NNrJtWuO2NpNQ89jo9PwjJdq/BKKNRqDG8gtxXlJM6nu1mg414RXfKnwe87WqE6Or61Jzz/c5A3i5eXsLuROC3KULyTdlASFXLWUvctRvoTOUkMfxiP7A3oDmG76IkW6UsAVcZpTooayy71nYGVX8gnvoS2GCT/DHtvrvW1u97DJozsjfTPexuNUSldCaLj4LUSdo0XolVQ1rucjSvkpUqsVpMLRMozQ348jBMqbyML6UFHUR4FKSFKq2KWaXV1n/RTsOk5u/RI2otyY5qLRSnGOpJEH9Cx99aXO5Hdm/PtlUOyPVVz3Xb1brQ449rtuH0uMe1yP+yBrK1aF7XqsPzdk63+nv/u9kN1Y1sr/wSOQDqn8h4j6vj8WUb//XBImAdZOEO2ARboA/6YSfs1P4ZAIWLyLg=).

**Points that do nothing for this spec:** **Improved Tactical Mastery** (3) only counts toward the points the tree needs before **Anger Management** and **Impale**.

## Other builds of this spec

- [Fury (optimized, two-handed)](../research/raid/builds/opt-arms-2h-raid-raid-dps.md) (20/31/0, 845 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013032-250500305022100231--12)
- [Fury — Two-Handed](../research/raid/builds/arms-2h-raid.md) (19/32/0, 833 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013031-553500050020100231--12)
- [Fury (optimized, dual-wield)](../research/raid/builds/opt-fury-dw-raid-raid-dps.md) (18/33/0, 821 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/05303013102-050530305022110231--12)
- [Fury — Dual Wield](../research/raid/builds/fury-dw-raid.md) (13/38/0, 783 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warrior/60/22303012-550530055021100231--12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

