# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Raid](../research/raid/builds/fire-open-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fire — Ignite / Heating Up), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 5 seconds left and the target has fewer than 2 stacks of Fire Vulnerability
4. **Arcane Blast**: keep its buff stacked on you
5. **Arcane Missiles** (rank 7) when Missile Barrage is active
6. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Combustion**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fire keeps its own **Improved Scorch** debuff at 5 stacks, fires **Fire Blast** every 6 seconds, casts **Pyroblast** whenever three crits have made it a 1.5-second cast, keeps one stack of its **Arcane Blast** buff up, spends **Missile Barrage** procs on free **Arcane Missiles**, and fills with **Fireball** or **Scorch**. The best mage page in the simulator: 828 DPS in a full raid.

**Why it works**

- **Pyroblast** at 3 stacks of **Heating Up** comes first (15 casts, 26%, plus most of **Ignite**'s 10%): crits from **Fireball**, **Fire Blast** and **Scorch** each cut its 6-second cast by 25%, and **Fire Blast** adds a stack on every hit, so three stacks come about every 12 seconds and the cast takes 1.5 seconds. One hard cast before the pull lands as the fight starts. The full list adds "not while casting": finish the spell you are on.
- **Fire Blast** on cooldown (29 casts, 22%): every 6 seconds with **Improved Fire Blast**, instant, 10% crit from **Incineration** and 6% from **Critical Mass**; its crits start **Ignite** (40% of the hit over 4 seconds) and every hit feeds **Heating Up**.
- **Scorch** keeps Fire Vulnerability at 5 stacks (**Improved Scorch**: 3% more Fire damage per stack for 30 seconds) and refreshes it under 5 seconds left, between casts. It is also the short filler (35 casts, 17%): when **Fire Blast** will be back before a 3-second **Fireball** could land, the full list casts a 1.5-second **Scorch** instead.
- **Fire Power** is why the burns matter: 3% more Fire damage per Fire effect of yours on the target, up to 12%, and Fire Vulnerability, **Ignite**, **Pyroblast**'s burn and **Fireball**'s burn are four. **Fireball** (11 casts, 13%) casts in 3.1 seconds with four points of **Accelerant**; the list names rank 11, which the search kept over rank 12.
- The 17 Arcane points: one **Arcane Blast** every 18 seconds (9 casts, 4%) keeps its buff on you (12% of your Intellect as spell damage) and rolls 40% for **Missile Barrage**, which **Fireball** rolls at 20%; the proc's free, fast **Arcane Missiles** are 8% of the damage (11 casts). **Arcane Concentration** makes one cast in ten free.
- **Combustion** at the pull (3-minute cooldown): each Fire hit adds 10% Fire crit until you land 3 crits, which fills **Heating Up** fast.
- Mana: a mana potion whenever it is ready (2 a fight), your mana gem (from **Conjure Mana Ruby**), a Demonic Rune, and **Master of Elements**' 30% refund on every Fire crit; **Evocation** in about one fight in five. In a 6-minute fight the simulator's DPS falls to 441: the mana runs out.

**Caveats**

- Mana without a raid's buffs: the simulator's list for playing alone adds **Evocation** below 10% mana with more than 25 seconds left.
- Several targets: **Flamestrike** (this build has no **Blast Wave**); **Fire Blast** hits one target only.
- Fire resistance: the simulator's boss resists nothing. Against a target that resists Fire, **Frostbolt** is your fallback and most of this list loses value.
- Threat: this build skips **Burning Soul**, so only **Arcane Subtlety** lowers your threat, and only for the Arcane spells; the simulator ignores threat.

**When to change it**

- In the last 3 seconds a **Fireball** would land too late: **Scorch** or **Fire Blast**.
- Moving: **Fire Blast** and the 1.5-second **Scorch** keep the stacks and **Heating Up** going; **Pyroblast** and **Fireball** wait.
- The list has no 2-stack **Pyroblast** line (the simulator's own Fire rotation, which this list is built on, dropped it): with 2 stacks and the boss about to die, a **Scorch** and a **Fire Blast** in the same 3 seconds are its choice.

*This guide was written for the rotation of 2026-11-04; the list above was re-tuned since, so follow the list where the two differ.*

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Arcane | 17 | Wand Specialization 2, Arcane Subtlety 2, Arcane Concentration 5, Missile Barrage 2, Arcane Blast 1, Arcane Meditation 2, Arcane Resilience 3 |
| Fire | 31 | Incineration 5, Accelerant 5, Ignite 5, Pyroblast 1, Improved Fire Blast 2, Improved Scorch 3, Heating Up 1, Master of Elements 2, Critical Mass 3, Fire Power 3, Combustion 1 |
| Frost | 3 | Precision 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 869 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 885 | this build |
| Phase 1 BiS | 903 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-54500001230133031-003-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 60.8; Phase 1 BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Dreamweave Circlet](https://www.wowhead.com/forever/item=10041) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Magister's Leggings](https://www.wowhead.com/forever/item=16687) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Blessed Band of Light](https://www.wowhead.com/forever/item=272407) · *sold by Pix Xizzix* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Truesilver Conduit](https://www.wowhead.com/forever/item=249455) · *Enchanting* | [Truesilver Conduit](https://www.wowhead.com/forever/item=249455) · *Enchanting* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV01sG0UU9htv7fFL2pjpD8uSwzRQkjhxsl7HVRIh4lYCAi244sQJsvau4y1br+Vdo/ZWohwQEolUIlVNc0ARKFBBi4KE6ki9mIs5gCKkUgGHRIEAQkglPUTiAEKzdtocqp6oOPhJfjv7nr73Zr9588aDnRSiIAOHHpiAApTgPMDbAO8DfATA2n0vEd5hUDYOUhqlSgVDtPqyvNmGEt24CCjR3+eEvrwaxRCtF+Wf9mGY1j4E+cd9GKS1Ikp0cxYwTK9NgYCF6WefgDwbRonO/BFFiV5cFfoLX/+90IFhevsqyPX9KNHbCx0o0Y8XOrr6onWr55sZULezp95dhHeATFsXgGxn54H8euwKhJcWYDMxY63DtHWc+hOHNKyQJzQ1qakpTVUTqqrFU6mUqqpqQkv6v2QirqrJOoFV0rZBftmPTyJVQijRvy5Al7xMDtIgi8yTpkV4kMQT7A02oZfs152SxzVVOxpPJOJqYpTnCnpx0jS4U+a6YZgGz57jXsHkZcfTPcspctfUy7kC73FNk+etshkv65YR33HHG+6B065T7FXCyh4MRqctdpWwbWikUePJxKgf0snnrZyl29y1zlRs3XPK3S4/o0+ag0bJHdRLtjtomGbpOatsDugl24/JdY+nhnKmnjuaHOa64ZQ80+A9d9Pb+iTXK4blcT3vmWU/T9mMl6ziKO/TBoaP8LzTsJpFr3yu2+VZ0/V4tmLZBreKXOf5im1z8U39TYDn8L6hgVQDaXkuty1XJPUxbj9PqP2qqvK8NVnwXO4zZBou17heNHiyV0liL+vGQ7EDFFikBmIdtqqyYAYhiXu72jByB3atjniyqRYmzK8aeivDvof71GjyP67RCtrsNI4qw6jEZBpke2uAKNFrnwMjUSKmgpDa8a3cz9evxB6A1bC9C5HeAfFRaxkBomsZdrmFF5hjZ0yhwDpq0H6PLhmahI4G2JctzM44PsOexj6lF9t+CFGU6I2qLEOzwiIrfqu4UZWVZk+fu3lidxOZu3lCaT7ZbAuzeADblkGw97VgT1QW/TnDFlqYkcMoxw7REKNX/FZ0K6PQeSJGS42mtJRp8VNHnDprGTkYWwSMPPumk/Pnyl5QnsdOpjQ22bK//VbqL2HkW0kMq1snte7mH67q1kl8fApkDNL3XlMeiXXQECPZgBLGPRgcGTnCXlTG/Y3th7qLb0RehJ3Xe0keEOs3Uoc/ifZWMODLUNrHI6HQ9Q+JCFPgfD792PwlIV+NHc778t2Ytk5kiY/FrpPA/yJeemf0UOWpTx9anhFfv/JB+ljTkJ4Q941L4L8E1sdiQXr90eO7riUqDEMaxuEUvAoFKMFZOEv+HQDv+kA5); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkV09sG0UX9xtv4/FL2vib/vmWJYdpoCRx4mR2N66SCBG3EhBokStOnCBr7zresvVa3k3V3kqUA0KikdL00DQHFIECFRQUJNRE6iVcjBAoQioVIJSIEkBcSnqIxKVCu3bSHKqeqDj4Hd7Ovqffe7O/efNmB9soJEAGDp0wCkUowwWAtwHeA/gQgLWEXhJ4B0C5c5DSBFXOYowuT4C80YwSvT8NKNE/ZwJ9dTWBTbRaku/swxhd+QDkn/ZhlK6UUKIbU4Ax+vPlEBajn30M8lQMJfr1ZdjRk5cC/cVqAmP07nWQq/tRonfnWlGiH821tncnqnbntxdBbOVOvTsP7wCZtKeBbOVmgfx+7BrEFuZgQ71or8OkfZyGM4cMLJOnNKFrIq0JoQqhpdL9aSGEUDVdqLoudDUlhF4lsEqafyG/7cenkSpNKNG/p6FdXiQHaZTFZ0ndEniQpFT2Jhs1ys4bbtnnmtCOplQ1JdQhni8apTHL5G6FG6ZpmTx3nvtFi1dc3/Btt8Q9y6jki7zTsyxesCtWqmLYZmrbnaq5e097bqlLiSl7MJqYtNl1wraglkakdHUoDOkWCnbeNhzu2WfGHcN3Kx0eP2OMWX1m2eszyo7XZ1pW+QW7YvUaZSeMyQ2fp/vzlpE/qg9ww3TLvmXyzp30jjHGjXHT9rlR8K1KmKdipcp2aYh3a70DR3jBrVmtkl853+HxnOX5PDduOya3S9zghXHH4cE39dQBvsu7+3vTNaTte9yxvSBpiPF6uCp6hBC8YI8VfY+HDFmmxzVulEyudyk6drEOPJQ8QIHFVyBYh80lOWAGQce97c0Yvwe7Vid4sokGJiysGno7y36Ah9So/i/X6Dg67DQOKQOoJGUaZXtXAFGin34OjCRIMBWE9LZv+WG+HiX5CKyGLe2I9B4EH7WWDUB0LcuuNvACc2xLKhRY6wq0PKBLhjqhQxH2ZQOzM4LPsWexW+nC5h+bKEr05pIsQ73C4sthq7i5JCv1nj5z68TuJjJz64RSf7KpBmbxADYvQsDeNwF7QWXRX7NsroEZOYxy8hBtYvRa2IpuZxU6S4LRQq0pLWQb/NQJTp21rBxNzgPGnz/r5sO5speUF7GNKbVNthhuv+XqKxj/TgqGS5sntY76D9fS5kl8cgJkjNJLryv/S7bSJkZyESWGezA6OHiEvayMhBs7DLWDr0Weh+3XB0keEesPUoW/iPZWNBJKfybEI6HQfp/EA1PkQiHzxOyVQL4aPlwI5fthbZ3IEh9O3iCR/0T8zPboscoznzy2PIOhfvX9zLG6ITMaXDiuQPgSWR9ORumN/x/fdS8RMAAZGIFT8BoUoQzn4Bz5ZwAldT/7).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (16/32/3, 831 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000001-35500201230133031-003-12)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 827 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000003-35500101230133031-002-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

