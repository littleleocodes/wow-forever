# Assassination Rogue — Raid (group)

[Rogue](../README.md) > [Raid (group)](README.md) > Assassination

**[Assassination — Raid](../research/raid/builds/assassination-ml-raid.md)** (30/21/0) — [open the talent tree](https://talentsforever.com/rogue/60/0053031033150105-305313000015--7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Assassination — Seal Fate daggers). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Slice and Dice** (put it back up as soon as it drops, even with 1 combo point; refresh it early at 5 combo points when it has under 3 seconds left).

**Then press the first one that is ready**, top to bottom:

1. **Garrote**: keep it on the target
2. **Cold Blood** right before your finisher
3. **Eviscerate** (rank 8) when you have 4 or more combo points and either Slice and Dice is active or you have 79+ energy
4. **Mutilate**

**Mutilate** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Vanish**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

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

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 662 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 668 | [30/21/0](https://talentsforever.com/rogue/60/0053031033150105-311313102015--7) |
| Phase 1 BiS | 674 | this build |

**The gear** (average item level: Pre-BiS 63.3; Phase 1 BiS 64.0; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Darkmantle Cap](https://www.wowhead.com/forever/item=22005)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Howler's Furs](https://www.wowhead.com/forever/item=272414)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Forest Stalker's Bracers](https://www.wowhead.com/forever/item=19587)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) | [Assassin's Waistguard](https://www.wowhead.com/forever/item=272395) |
| Legs | [Devilsaur Leggings](https://www.wowhead.com/forever/item=15062) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Sentinel's Leather Pants](https://www.wowhead.com/forever/item=22749)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21205) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) |
| Main hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Off hand | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Premier High Warlord's Razor](https://www.wowhead.com/forever/item=272596)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) | [Premier High Warlord's Recurve](https://www.wowhead.com/forever/item=272594) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVU1MK1UUnnNn6Nye1r7JzXt548SfeV2Yvmqf89N50oex80heNOqCPDfdyUgLrZC2aUsEVwVNJJGYaCIRFsYIJsafhBAlhK0JYsICUFkYDSguiGFBjLrCn9wphQpsyzuLe++c8333fOeeO7n4AAUFVNAhBr2QhzLUASYAPgD4GICF/Sjh0U7QJkOUKJJWB5Tpn5+C+msIJTr7HqBEv11TUKbvryvqRgBl+tUXl9TdCMr0tWlQf+KLtTVF3Y6gRN9cVzBAt4Y5W6Zfj0PD/f1HfJu/p/j45bqCEp1/l+f5bkNR9yMnC4lubijRG8pqIbY3ZBx29Wy9BZk/et8Bctg1A3TW+8z78fbUC58AmSzMw86dJdj/ELrDJ1W6sEweNAzHNmzTsG3TMUzDSdimaZu2aViG6awS6RcyEWRjwApeeejFUrmmW4Z1M2EaCSt5S+/Le8WBXFYvVXQvm81l9ZdG9Vo+p1dKNa9WKBX1as6r9OX1WDWX071q1atWC0U/kqh4hWyiiUs0cDderpaK17XLGIoGUbY6UKQzGa0xse0L1VDBAhvAbs1FJR6hEiOvCloAJSSmg4+xOAY3pQBKdO73508DLAdDC0AbQRXwmvawDxGZOA4CrwbB/h+E+5TDLvYGaK8DjmqvoMNsnxNo4ZgYiYYRF0DGjhihfyXxUvw+GmDk2SPATXyKPXmG5uDV+BUqMlw+JjY1cH7HCT+lNQFM0SKtmW4J7FHtOursoTPbJ1txfB/6c5GNn9Mqw2xXq65g+IdAEEW6UmL8p+QiVkrnijCTbRexOHgsYnGQ3dV68Gl255xjM7XHW4/uCHF8i55I+e0VW9rLJzqXYahRftPowe5zrHaqRiOVsDrbVaPsK3g7w4Yvsr2NYv+tgyrukVU4INaYKPh22f0NJCQoRP8hQe4Q6v3u/TPT3L5JX+v3bStt7RBV0tPxJSLcE6u5zVVb7ZHP25Yn5Y9359zbRw63l7+M0+B/CDvpuEiXrna3PKAGdIILz0APZCAPZRiBEfLfAC8njlg=); Phase 1 BiS: [full raid](https://wowsims.com/forever/rogue/dps/#eJzEVU9MI1UYn+/N0Hn9WruTl93sOPHPbA+mW+36Zqaz0sXYWZKNRj2Q9dKbjNvuti5pm7ZG8ASokcR/UaMJHIxRTIx/EiRKCFcTxIQDoHIwElA4EMOBGPVE1LwphQpci9/hvTff9/u97/e9700e3kVBAx1MSEA/FKEKwwBjAB8AfALAokGUiGg3GK9HKNEUYwRQpX9+BvpWBBW69SagQr9f1FCl7y9p+nIIVfrNV2f0zRiq9MVx0NfEYnFR09djqNBXlwRy7cuArtJvR6Hp//Fjsc/L74jx6yUNFTr1rkj0w7Km78QOFwpdWdbil7SFUmJ7gO/19K2+Abk/+t8GstczAfQj/3P/56vvPfUpkNdKU7BxbRZ2PoTe6GGZHsyRuzl3He5Y3HEsl1vcTTncdSyHc84td4Eov5KxMBsBVvKrA09Xqg3T5vbllMVTdvqKeaPol28V8malZvr5fCFvPjNkNooFs1Zp+I1SpWzWC37tRtFM1AsF06/X/Xq9VA4iqZpfyqdauFQTd+nZeqV80TiLkXgYVbsLZTqRM5oTWz9VDTUssVvYa3ioJWNUYeQFyQihgsRy8QGWxPCKEkKFTv7+5FGA7WJkGmgzqANeMO4NIDKTR0ES1SA4/4EIn7bXw14B4yXAIeN5dJkTcEJtHAtj8SjiNKjYlSD0rzSeSd5BQ4w8vg+4jI+wh4/RXDyfPEdlhnMHxJYGwe865GeMFoBpRqw90xWJ3W9cRJPdc2z7dDtO7EN/KbPRE1rFrU616hxGfwqFUabzFSb+SiFivnKiCCvdcREztw9EzNxm140+fJRdO+HYLOPB9qPbRxzcoocyQXvltvaKiU7mGBpU3DS6u/kEaxypkWdSdnenalQDBW/l2HOn2d5msf8Mgy5vkwXYJfaILAV21vsNFCQoxf8mYeGQhm96d06MC/sue+FmYKtZe4PoiplNzhLpf7GG11p11O77omN5MsF4fdK7uu/w+sXTOA7Bh7SRTcp09nxv2wvKoRs8eAz6IAdFqMIgDJJ/BwB79I5c).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

