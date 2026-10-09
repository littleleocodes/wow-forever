# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**[Assassination — Raid](../research/raid/builds/assassination-ml-raid.md)** (30/19/2) — [open the talent tree](https://talentsforever.com/rogue/60/0053031052150005-305313000013-002-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 3 seconds left).

**Then press the first one that is ready**, top to bottom:

1. **Cold Blood** right before your finisher
2. **Eviscerate** when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
3. **Backstab**

**Backstab** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Assassination in a raid is a Seal Fate dagger rotation: **Backstab** from behind builds combo points, often two at a time, **Slice and Dice** stays up, and every 4 or more points go into **Eviscerate**. **Cold Blood** goes in front of an **Eviscerate** whenever it is ready.

**Why it works**

- **Slice and Dice** is 30% more attack speed: more white hits, and more chances for your poisons, which can proc on every weapon strike. Put it back up the moment it drops, even with 1 combo point. With 5 points and under 3 seconds left on it, refresh it before you **Eviscerate**.
- **Eviscerate** goes at 4 or more points because a **Backstab** often brings two: **Seal Fate** adds a point to every **Backstab** crit, and **Puncturing Wounds** raises its crit chance by 30% and adds a point 45% of the time. From 4 points that second point would be lost at the cap of 5, and **Ruthlessness** adds a free point after 60% of your finishers.
- **Cold Blood** spends no combo points: it turns your next **Sinister Strike**, **Backstab**, **Ambush**, **Eviscerate** or **Mutilate** into a critical strike. Press it with 4 or more points and **Slice and Dice** up, then **Eviscerate** right away, so the crit lands on your biggest hit instead of a **Backstab**.
- **Backstab** is your only builder and your filler: 60 energy, from behind the target, with a dagger in your main hand. **Malice** and **Lethality** make its crits more frequent and bigger, and every crit also feeds **Seal Fate**.
- Poisons are a real share of your damage: **Instant Poison** on the main hand, **Deadly Poison** on the off hand, where it stacks up to 5 times. **Improved Poisons** raises their chance to land and **Vile Poisons** their damage; **Deadly Poison** alone did 8% of your damage in the simulator's training-dummy runs.

**Caveats**

- **Backstab** needs you behind the boss with a dagger in your main hand. When the boss turns to face you or you have to stand in front, build with **Sinister Strike** until you are behind it again.
- There is no **Expose Armor** in the list: in a full raid a warrior keeps Sunder Armor on the boss, and the two do not stack (only the stronger one counts).
- Poisons now go on a weapon together with a sharpening stone (Blizzard's rogue deep dive, 2026-10-07), so use both.
- This build has no **Mutilate** or **Venom**, though Blizzard built Forever's Assassination around them. In the simulator **Backstab** with **Puncturing Wounds** out-damaged **Mutilate**, the talent search dropped **Venom**, and the simulator's own Mutilate build did about 5% less than this one in a full raid: check it at launch.

**When to change it**

- In the last 6 seconds, start no **Slice and Dice**: put 4 or more points into **Eviscerate** even with it down. If the boss is about to die with 1 to 3 points, an **Eviscerate** still beats keeping them.
- If no warrior keeps Sunder Armor on the target (a small group or a dungeon), keep **Expose Armor** up with 4 or more points, refreshing it before it runs out. On the training dummy, where nothing else lowers armor, the simulator measured that about 9% better.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 707 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 647 | [30/19/2](https://talentsforever.com/rogue/60/0053031052150005-304313100013-002-6) |
| Phase 1 BiS | 703 | this build |

**The gear** (average item level: Pre-BiS 63.1; Phase 1 BiS 67.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Hood](https://www.wowhead.com/forever/item=16908) · *Onyxia, Onyxia's Lair*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Neck | [Mark of Fordring](https://www.wowhead.com/forever/item=15411) · *quest: In Dreams* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Cape of the Black Baron](https://www.wowhead.com/forever/item=13340) · *Baron Rivendare, Stratholme*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) | [Nightslayer Gloves](https://www.wowhead.com/forever/item=16826) · *Gehennas, Molten Core*<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/spell=13823) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) | [Bloodfang Pants](https://www.wowhead.com/forever/item=16909) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11647) |
| Feet | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Darkmantle Footpads](https://www.wowhead.com/forever/item=226831)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Band of Accuria](https://www.wowhead.com/forever/item=17063) · *Ragnaros, Molten Core* |
| Finger | [Ferocious Watcher's Signet](https://www.wowhead.com/forever/item=275981) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18465) · *quest: Garona: A Study on Stealth and Treachery* |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Perdition's Blade](https://www.wowhead.com/forever/item=18816) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Blade](https://www.wowhead.com/forever/item=272452)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Brutality Blade](https://www.wowhead.com/forever/item=18832) · *Garr, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Striker's Mark](https://www.wowhead.com/forever/item=17069) · *Magmadar, Molten Core* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE9IHGcUnzczu/P5uq7DR8XpUMpooaxbpv1mx7Wulu4qlJb2orQHb3Xqrt0tdmfZXakWCta2tGClkkOIISEJuRiSQDA5BK9JZIUJqDEegiEk5iBhD0sgORkSZnbVJeYYQ36n37zv93v/GB4GCMiggAYhYEA/3PviGXRBAvphEIYgDTmYBPgXYBZAPSkRXhbV31EiT86D8vAdFMjlcRTJLUdGPzmRVlb9KJFrV5qUrSBK5M85UO66xHFk5V4QRTK94go3xlyvRP4vN1bDz44CimSmLKNAZn5BkZyZBZTI+qqslF3/9RWPiGRtVW4Ly6WM8l8mtD3KdnoS0D+9BoML63AE+J2eY3DWOg0XrHnY7C0B9OH+kIt8K2NRk5kGi0aMKGMsqpuswzRMgzFmmDpjkRIvPuBP+eg/oP4FOKH+ilFqohwOEj8VpoBTfSggGBhsCyAugIS+EE+edmBTuJH4Kf9NTdCJX9DPD9ii2BJuJgLFxT1jVW56ft++P6buCqisBusrdXP0Y7UdNfrBgfQd9To3D7mfpVNAM1Zu9Ac7V9QiLNKpG0xnRrc2nLayP6WSmp3XrGQyldR+nNCK6ZSWt4tWMWNntULKyg+ntVAhldKsQsEqFDJZ70XPW5mkvqvTq7pPfi7Y2Xa1GQN3/A0okCWbuj+K28SSTb9TB/Ar+uUrOjbUT+u7rin43zjVjyLyn8W8zQh1m3UfyPxjoGMvDcZieqTrsAYjXtn1G0Cxxitb39KxN7nbatnnk6AI23wJKnzkD4Hz8G7iEYjII9d2TmhwA9zkSOK943MuluOtIx424pEKr0haPFziubcKxcQuO1R8dPG114nddBwnMHQp0VsLJIbcSzkHGbvy9/L3t+MxL8qtxHtdpeOU4wNVshkPC+RqS9/7++epenW/9u5uGnIwDuP0xQAs4xZH) · [training dummy](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE1oI2UYnm9+v75N0+mn4nQEmeYg7cDUb2YyrWkPSQr+oBeLor3ZsUlNtCYlk0IVhFoRhFoUD8WKB8VLxR+kikgPvagllRHSWnuQyrLbPZQlh7Cwe+qyy0wmbNlet2Hf08vzPW++53neLwMMYdStbszKvPoeSPjGd0i52g0c/nkRePyPL4OIvywoeyJI+PdfepXjOEj4g3Wk/B80vi8rl+LA45V6QDxcCGYl/EmjpwXfWkPA49WGDBxefRt4/PWnCCR8sCcrjWD+j3rY8Hh/T07ocq2ofFwcPJmjp+MZ9OLKPpraPECfIfZ0/HP0jfsV+t7dQEfZGkITzBY7QKljU9u0HGo6lFLHsGnSpjalFjVtg1KrxvJX2J0usoxI0Z2fe608X9Usao0YJjWoOabNFNzSG/mcVq5obi6Xz2mvv6NVC3mtUq661WK5pHl5tzJT0Aa9fF5zPc/1vGIpPDEqbjFntHlGizf8plcuDamPQOw/sQs4vFMmQapCq92+VwRNGdZTFyViEp4jzwDRZcwT9l1GxSACn7SHHZD1OBYI95fAqAJwgMwQ4Qi3jCLEgVgCAG+iQPmvbwWgfDpOFjqpH6si8PjgT0TqHc1tBqbIK/CY3o85Et9C3SAMCnj7VcLKQpADIBse0vuw2IorTNUeHnWgV+/BImGfjyK0oU/vjQAJBOBM6qlS+8d+7KilLIyQZLjkSHW09ngiBrCJAlUsvtlmBBZE4IE1LbV9RGQ1fpY6xpC1jloYAo08fs6Cc1ZTkDu+XCIvqZPwLHn6HDkJpvrk2YGIEfw5Qr+jqXCJ3N0ljoRvcOM6IhC9x+bxC2Shk9+S1rW3l5DCnbA11GSt9zkmrIcz1xAPLDCJb7muAGCWZjP9X6wHtZsemA3rMG01WUXS0nqNZR6oqmba3YXWEz/c93tSf/u+H5v+KZONgMw0+gihdVQsNz/cffnfdCpEmXo6GzB9v5GebDVHaZ3Dvz06wSySOwMAK0Kypg==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE9IHGcUnzczu/P5uq7LR8XpUMpooaxbpv1mx7Wulu4qlJb2orQHb3Xqrt0tdmfZXan20q26tKCi1EstARNyiIEIQXIIXkNkhQ2YxOQQDCHRgwQPSw45CQkzs+oSc4whv9Nv3vf7vX8MD30EAiCDCkFgQD8+/uIZdEEc+mEQhiAFWSgC/AOwAKAsS4QPiMqfKJHZaZD33kOR7M0DiuRuJYBeci4l3/aiRG5ca5J3/SiRqSWQH9pkfQrkR34UycxWACUy57olMn/Q6MYvlew0pUVAgcz9hiK5sAAokeIiyAd2ggWXiGS1BG2hQDktz6aD+6PssCcO/TN3YHBtG/4F/rDnP7honocr5grs9JYB+vBkzHW+lbGIwQydRcJ6hDEW0QwWMXSDMcZ0Q2MsXObFJ/yyh/4NyjTghPI7RqiBgZCfeKkwCZziQQFBR3+bD3ENJPQEefK8A5tCjcRL+e9qgk78in55yhbBllAzESiuHxtdueH4PSf+qHIkoAHFX1+pm6OfKu2o0o9Ope+o19l5yOMMnQSaNrOjP1nZghpm4U5NZxrTu9XhlJn5JZlQrZxqJhLJhPrzhFpIJdWcVTALaSuj5pNmbjilBvPJpGrm82Y+n844L1rOTCe0I53m6j77NW9l2pVm9D3wNqBANixq/yp2ExsW/UEZwG/o16/pWFc+r++6puD/4BQvish/EXU2I9Rt1n4gK8+Ajr0yGItq4a6zGow4ZbdvAsUar+5+T8fe5m7dsi+KIAv7fBmqfPgvgXPwfvwpiMgj13ZZaLADXHEk/sH/SzY2Y60jDu7HwlVeltRYqMxz7xQK8SN2pvhk9Y3Xid6qVCq+oavx3logPmTfyiVIW9XS5o/3YlEnym3Fem1lpXIQG3DJTiwkkOstfR+enCf37n7rXN4UZGEcxunLAQBGJRLr) · [training dummy](https://elliotwood.github.io/Forever/forever/rogue/dps/#eJzMVE1oK1UUnjO/t6d56byr4rwRZF4W0jcw9c5M0mdeF0kK/qAbi6Ld2bFJTbQmJZOCurG2BoS2tFgQKy4UF1awIkVEinQjllQiVK0upCLaLop0EVy4KijzEyx2a8M7q8N3v3vv933nziBHOf3LfsKrov4qKmTpddCO+1EkxyuAIvmhraJM3i1r38mokK8+G9COkqiQhXXQfgma7QXQfk2iSBb3VVTIcrRbISunVyL8w2ZwTHMNUCDLL6JI3l8FVMjcGminwQGrUSOSzSakTLVV0ZYqgyfT7GwkD48vfg/jWwfwJvBnI2/DB9578LG3AYeFFsAot81fZyzjMtd27LSdYYxlLJelXdtlzGa2azHmtHjxd363j84DrXgz08/UZhqGw5xhy2YWs28Zk2Wv+lypaNTqhlcslorGsy8bjXLJqNcaXqNSqxp+yatPlo1Bv1QyPN/3fL9SDVesulcpWl2eFfGGnvdr1Rv6XZj4We5DgezWaJCrFLU7/xXBspbzwGWJGMNH6ENITZWIlH+F0wnKKKbdoQyqZpJIVPhG4nQJBQQ7RAQqzEOMZDCRQiRbECj//IUAVM9G6Gwv9RNdRpEcfA10v6e5TeI4fQrvMa8RgSa3oR+lQYnsPE15VQpyQHDxDvMqkaO4wlTdoZsZHDCvEJnyj8YRunjVHIgBBSUUbObrSvewT3pqqYDDNB0OOVYdjz2ZSiBuQaCKJ391GYEFGUXkbUfvLlFVT56n3uLoWz21cAMNeu8FC5nzmoLcyW9V+oQ+hg/TBy+Q02jr95/fEDOCjyP0ezMbDlH4d4jD4Rvc+BMoxu+xc/QYne3lvyS69u850IQTvgUd3nlN4MK6M/8HiMgjl/pI6AsAbm4qf+2d9aD2ctenwvop53R4TTFyZovnbqtq5LvdpdZ9m//7Pdlv2+12YuLTfCEG8hPwBsA6VGqd5t6TP+ayIcrt5woBs90+zY1FzWHOFMgXd49yL9F/BgB9669K).

## Other builds of this spec

- [Assassination — Seal Fate daggers](../research/raid/builds/assassination-seal-fate-raid.md) (30/19/2, 702 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053031232150005-305313000013-002-6)
- [Assassination — Seal Fate / Vigor](../research/raid/builds/assassination-mutilate-raid.md) (30/21/0, 690 DPS in a full raid) — [open the talent tree](https://talentsforever.com/rogue/60/0053031252112005-305313000015--6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

