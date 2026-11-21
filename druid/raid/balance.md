# Balance Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Balance

**[Balance — Moonkin / Nature's Grace](../research/raid/builds/balance-moonkin-raid.md)** (33/0/18) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051--5553-12)

## How to play

**Before the pull, then keep up all fight:** **Moonkin Form**.

**Then press the first one that is ready**, top to bottom:

1. **Moonfire** and **Insect Swarm**: keep them on the target
2. **Starfire** (rank 6)

**Starfire** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

A raid Moonkin keeps **Insect Swarm** and **Moonfire** ticking on the boss and casts **Starfire** the rest of the time. **Moonkin Form** goes up before the pull, and **Innervate** is your mana button.

**Why it works**

- **Moonkin Form** first (the rotation shifts 10 seconds before the pull) and for the whole fight: it gives all party or raid members within 45 yards 3% spell critical strike chance and doubles how often **Omen of Clarity** makes your next spell free. A feral druid's **Leader of the Pack** adds melee and ranged crit instead of competing with it, and you cannot heal while in the form.
- **Insect Swarm** and **Moonfire** each do close to a fifth of your damage for one instant cast every 14 to 15 seconds (**Nature's Splendor** makes them last that long, **Genesis** adds 2% to their ticks a point, 10% at 5 points). Recast each one the moment it runs out, not before: recasting a running one throws away the ticks it had left.
- Both sit at the top of the list, above your cooldowns, and when both are due **Moonfire** goes first: its direct hit lands at once and can crit into **Nature's Grace** for the next **Starfire**. The rotation search of 2026-11-01 measured that order about 0.5% better in a full raid than the old **Insect Swarm** first.
- **Starfire** is your filler and about two thirds of your damage. It beats **Wrath** per second of casting at any gear: 350 to 412 damage plus all of your spell power in 3 seconds with **Improved Starfire**, against 92 to 102 plus 57% of it in 2 seconds. The raid build takes no **Eclipse**, so the list's one **Wrath** line (a weave for an Eclipse build) never fires.
- Critical strikes feed the filler: **Vengeance** doubles their bonus damage, and every critical hit from **Starfire** or **Moonfire**'s first hit triggers **Nature's Grace**, 10% faster casts and global cooldown for 3 seconds.
- **Innervate** at 10% mana: for 20 seconds your mana regeneration is five times higher and all of it continues while you cast (6-minute cooldown). The 2026-11-01 search moved it down from 30% (about 0.2% better in a full raid): pressed late, none of it is wasted on a full bar. With a raid's Blessing of Wisdom and Mana Spring you need it in about 1 fight in 10.

**Caveats**

- Moving: **Starfire** needs 3 seconds standing still. Refresh **Insect Swarm** or **Moonfire** while you move, then go back to **Starfire**.
- Damage taken pushes your casts back. **Nature's Focus** gives you a 14% chance a point (70% at 5 points) to ignore each push, and **Barkskin** (1-minute cooldown) stops pushback for 15 seconds without slowing your casts as it did in Classic: press it when the raid is taking damage.
- Without raid mana buffs (a small group, or alone) you run short. The training-dummy rotation then casts rank 1 **Starfire** (95 mana) whenever a full one is out of reach, which the simulator measured better than waiting for mana.
- **Eclipse** (each **Wrath** takes up to 0.5 seconds off your next 2 **Starfire** casts, at 3 points) is not in the raid build despite its name, The list carries a guarded **Wrath** weave for an Eclipse build (about 7% better for such a build in the simulator, 2026-11-20), which never fires for this one; that Eclipse build is not a page build.

**When to change it**

- When the boss will die before a 3-second **Starfire** can land, cast an instant **Moonfire** instead: its first hit lands at once.
- In the last 10 seconds of a fight, skip a new **Insect Swarm**: most of its 14 seconds would tick on nothing. The simulator measured that 0.2% better on the training dummy.
- On a pack that will live a while, **Hurricane** hits every enemy in the area each second for 10 seconds (1,495 mana); the list itself is for one target.
- If you end fights with mana to spare, your raid may want **Innervate** on a healer instead: it works on any target.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Balance | 33 | Genesis 5, Improved Moonfire 2, Moonglow 3, Nature's Majesty 2, Nature's Reach 2, Nature's Splendor 1, Improved Starfire 5, Insect Swarm 1, Vengeance 5, Nature's Grace 1, Moonfury 5, Moonkin Form 1 |
| Restoration | 18 | Heart of the Wild 5, Nature's Focus 5, Naturalist 5, Reflection 3 |

## The numbers

**How this pick was checked:** no talent search or short check of its own in this entry's current setup; one follows in the optimality pass.

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 689 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 632 | this build |
| Pre-BiS | 694 | [32/0/19](https://talentsforever.com/druid/60/053222011550105--555301-12) |
| Raid BiS | 717 | [36/0/15](https://talentsforever.com/druid/60/0532223115501051--055203-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 60.8; Pre-BiS 61.1; Raid BiS 62.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Shroud of the Nathrezim](https://www.wowhead.com/forever/item=18720) · *Balnazzar, Stratholme* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Spritecaster Cape](https://www.wowhead.com/forever/item=11623) · *Houndmaster Grebmar, Blackrock Depths* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Alanna's Embrace](https://www.wowhead.com/forever/item=13314) · *Ras Frostwhisper, Scholomance*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [item 17721](https://www.wowhead.com/forever/item=17721) | [item 17721](https://www.wowhead.com/forever/item=17721) |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Waterspout Boots](https://www.wowhead.com/forever/item=18322) · *Hydrospawn, Dire Maul*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Waterspout Boots](https://www.wowhead.com/forever/item=18322) · *Hydrospawn, Dire Maul*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Waterspout Boots](https://www.wowhead.com/forever/item=18322) · *Hydrospawn, Dire Maul*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Smolderweb's Eye](https://www.wowhead.com/forever/item=13213) · *Mother Smolderweb, Blackrock Spire* | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Headmaster's Charge](https://www.wowhead.com/forever/item=13937) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Ironbark Staff](https://www.wowhead.com/forever/item=20069) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Ranged/relic | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* | [Swarming Idol](https://www.wowhead.com/forever/item=272430) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/druid/balance/#eJzEVMFr5FQYz/eSmbz5Kutstq7Z6OFtZXV22JQkJbL2MrMDwh5cWLwoXtyXyZtJ1mwyJBlmvbXQgwi2tQjSUqEUoSDo1eJFrIijB60XL15Ki1QURAWvKsm02H+g7O+QfO/3/R7f7/cOH16hUAcdGDTgHgQwgAWAtwC2ALTHyhYpWjfB2K5QtT5lRKjSnTXQf55ChR6+D6jQrTVAmR6/hir9YQX0owuo0i9WQf/pAsr0qz4q9PtNwCr9q1fcUunaCugrKsr0X44yXfRQpqsPUKYf9LFK/4z08SWUUKGf7NdnrtbHYeO7Zbj7zja8DWQp3AByfOsjqOxswnJ4AEthh5YuoQ2fkcuWO+c4jmXbrmvZlmubpuu6c2MC+2TqkHwt4zTS+1VU6MYezFCsomLaVqZNG1qnjjL97aU6GCpWULYeZNoTxqXORVTou1/CWVoxyLykLYLm8UH0ejLImWM5z5u2Zc7Z86wb8LgvfJakjPu+8Jn3JssDwdIk53mYxCwTPO0GrJEJwTwe8bgrTH+QmacCcyKYvZ8l8XXjKbzYfJwqGvGkiQPbumYUAX4/Au1X0D6FyZSJBdt0LNYoxoWxLwYi9kWcMz70w/y5jN12r8+zV1KeB2wUhJFgPTESKcsDHjOHvdiNwkEmigBpX2SMp4JleZIK/wbrD3l6JsuplA9TzjwRxn32RpyM4hssS5g3DCM/Y6MwD5JhXupzHpU+UsGG8ckDGbN4TXsGa98qRZrP/9bxcnOaylptD04Io4IyglP86O4drWaoZfneHV3+hYzhD+IvylKJ2bZXNRQkKM38Q2oFIy302lc21gt807raK/FjyzkgusJazV0iPRLk7dPqXPHsx+c254Xy+/KH7VsnRPtesSzWoTxIB62mTHef7Dz9/06x4Ca04TbchVchgAE8hIfkvwEA6jPQWA==); Pre-BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEVMFL5GYUz/uSmXzzWTRGW2Paw6fFdhyMJJEU62XGgYKHCtJLe6uZyeckdkyGJMPYmxYPRajaIhSth7YUSgv2VFrbS6mFduqhzKmXvYgiu7jLspc9LSxLMsr6D8j+Di8vv/cL7/fL4ZFhDBIoQCEPi+BCA9YAPgX4GkB+KR2hZDQN6g8ZLEo9akhE/OQQlIseIuCzL4EI+HI3qV91JJLFn7jKeS8R8Z87oNzpJQL+bTMZXmwDEfHfP/cl34n4i21QtkUi4K0HEhHwyTeJ5peORHi8s0JEfHEASnuAcETAP3Wk0RGp7eX/24KFz76FTUAb3j6gu7M/Qub7A9jyTmHDK+PUK5TgdzSkW1OmaeqGYVm6oVuaZlnWlG60EXRQzxn6hyeDBC9niYD3j2EUkywRNEOP5EFVLicW7r8rgSqSDOH1lUh+WR0o9xMBf/4X3KQFFc1w8jrIFbtR/zBoxNTUzbc0Q9emjBladW2/xhwahNR2HObQysc0dhkNg9iOvcCnEbPDqkvzEWO0Ytdtv8o0pxFp1wKtK5hcjgJ/XH2V9Bf6sCCjCtd1YOhjahLg4TnIlyD/Ct0tXQuGZuo0n6zzfIc1mO8wP6Z20/HiNyM6Z43P0PdDO3Zpy/XqjC6xFgtp7No+Nek71brXiFgSIKyxiNoho1EchMyZoLWmHd7Ici21m6FNK8zza/QjP2j5EzQKaKXp1Z2ItrzYDZpxqo/teuojZLTpX/0gdZKMya+T3ImQpPnjsUJeKQxiXs4dwxWhZghPwEwe+Ghezqli2u7OK/w91IZHyFnnuRSTpUpWFQgi3OhTlEsYbm2pNLy/l+Df4shSiv+L5ilSBFosHCHuhSAuXXe3ijcOb23P22l977vS7BVRWkxuxh6kL9xpscDjo6Hya89Piw7TUII5WIAPwIUGrMIqejYAsNnS1g==); Raid BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEVMFL5FYczu8lM3nzLBqjbWPaw9NiOw5GkgxTrJcZBwoeKkgv7a1mJs9J7DQZkgxjb1o8FKHaWnvQeiilUGixp9K6e1nWhd3ZXVjmtJe9yIrs4i7LXva0IEsyyvoPyH6Hl1++7wu/78vhkSEMEihAIQvz4EADlgG+B/gNQH4rkVAsTYL6dwqLUo8aEhG/3APluIcI+HQTiIBPtuLz145E0vg7RznqJSK+/iMoD3qJgK+sxeLxBhAR3/y3L/5OxJsboGyIRMB3f4nV9acSEfDqz/H8X0ciIj7eBaU9QDgi4H860siw1Haz99Zh7offYQ3QqrsD6NH0X5D6cxfW3UNYdcs4CQsluIoUvZA3TTNvGIWCbugFQ9P0QsHU820EHdTzEN3iySDBi2ki4J0DGMEkTQTN0EN5UJXLEuHxk88kUEWSIrz+TSi/rQ6U+4mAf7oBF2lBRVOcvAJyxWrUv/IbETV182PN0LW8MUWrjuXVmE39gFq2zWxa+ZZGDqOBH1mR63s0ZFZQdWg2ZIxWrLrlVZlmN0Lt3KB1DROLoe+Nqe+R/lwfFmRU4boJDH1UjQs8OwL5BOT/obulG8HQTJ1m43WuZ7MG82zmRdRq2m70UUhnCmNT9IvAihzactw6owusxQIaOZZHTfppte42QhYXCGospFbAaBj5AbPHaa1pBRe6nFutZmDRCnO9Gv3a81veOA19Wmm6dTukLTdy/GaU+COrnuQIGG16Zz9InSCj8gckc0eI21x7oZB3coOYlzMHcEaoKcITMOMH3p+VM6qYjFuzCv8YteE5sld4LsFEqZJWBYIIN3KKMjHDLS+Uhna2Y9wuDi8kuF80D5Ei0GJuH3FvBFHpfLpUfLh3aXs+Sc7P/yhNnxGl+fjW2IbkhTss5ni8/275/deXiw6TUIIZmIMvwYEGLMESejUAYcrTMg==).

## Other builds of this spec

- [Balance (optimized)](../research/raid/builds/opt-balance-dps-raid-dps.md) (36/0/15) — [open the talent tree](https://talentsforever.com/druid/60/0532223115501051--055302-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-20 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Spell ranks: trainer ranks only. The class books' ranks (Grimoire of Shadow Bolt X, Tome of Frostbolt XI and the like) are not in Forever on the evidence there is (2026-11-20): in Classic every one drops in the Ruins of Ahn'Qiraj, which Forever's roadmap does not have; Wowhead's Forever pages list no source for them; the simulator's own authors leave them off by default. Checked again when the raids of 2026-12-09 open. Do not hand-edit.*

