# Marksmanship Hunter — Raid (group)

[Hunter](../README.md) > [Raid (group)](README.md) > Marksmanship

**✅ Recommended** for raid (the best hunter spec here, or within 3% of it).

**[Marksmanship — Raid](../research/raid/builds/marksmanship-ml-raid.md)** (7/39/5) — [open the talent tree](https://talentsforever.com/hunter/60/502-0053552201523051-5-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Marksmanship — Lone Wolf), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the With a pet setup. The spec's best build for each other setup, in a full raid:

- Lone Wolf: [Marksmanship — Lone Wolf](../research/raid/builds/mm-lone-wolf-raid.md) (5/41/5, 1002 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/5-0053452511513051-5-12)

## How to play

**Before the pull:** **Aspect of the Hawk**, **Aimed Shot**.

**Keep up all fight:** **Aspect of the Hawk**.

**Talents with no line below:** **Trueshot Aura**: turn it on before the pull.

**Then press the first one that is ready**, top to bottom:

1. **Aimed Shot**
2. **Arcane Shot**
3. **Rapid Fire**; no global cooldown, so press it alongside the others
4. **Serpent Sting**: keep it on the target
5. **Sniper Shot**

Between these, **Auto Shot** keeps firing on its own.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Marksmanship raids with its pet out: the cat does about a fifth of the damage in the simulator's full raid, and **Focused Fire** adds 2% to everything you and the pet do while it is out. **Auto Shot** is about a third of your damage; **Aimed Shot**, **Arcane Shot** and **Sniper Shot** go out as soon as their cooldowns allow, **Aimed Shot** first.

**Why it works**

- Before the pull: call your cat, cast **Trueshot Aura** (in Forever a buff you cast, 30 minutes for your party and raid) and **Aspect of the Hawk**, and track the boss's creature type, since **Improved Tracking** adds 5% only against the tracked type.
- **Aimed Shot** comes first: it is your biggest regular hit (weapon damage plus 350, 10% more with **Barrage**), and its 6-second cooldown starts only when the 2-second cast ends, so any delay pushes every later cast back. Start it while the next **Auto Shot** is more than half a second away, so the cast does not clip one.
- **Arcane Shot** every time it is ready: 2 points in **Improved Arcane Shot** bring its cooldown to 5.4 seconds, about 31 casts in a 3-minute fight, more than any other button.
- **Rapid Fire** gives 40% faster attacks for 15 seconds; **Rapid Killing** cuts its cooldown to 3 minutes, so it comes once in a 3-minute fight, at the pull. The full rotation presses it right before an **Auto Shot**.
- **Serpent Sting**: recast it with under 0.75 seconds left, but not when **Aimed Shot** or **Multi-Shot** is half a second from ready, and not in the last 6 seconds. Each sting also starts **Rapid Recuperation**: with both points, half your mana regeneration keeps going while you cast for 15 seconds (all of it once a **Rapid Killing** is spent).
- **Sniper Shot** hits hardest (weapon damage plus 590) but takes 4 seconds, so it goes last: start it only when **Aimed Shot** is at least 2.25 seconds from ready and **Multi-Shot** at least 1, so the long cast barely delays your biggest hit. It comes about 9 times a fight on its 15-second cooldown; between casts **Auto Shot** does the work.
- The pet: Forever pets take their stats from your gear (a tenth of your attack power and all of your crit chance), so the cat grows with you. It claws on its own; keep it on the boss and alive with **Mend Pet**.

**Caveats**

- **Multi-Shot** is on the list but shares **Aimed Shot**'s cooldown, so on one target it almost never comes up. It is there for groups of targets.
- Mana is tight even in a full raid: the simulator's hunter drinks a mana potion a fight. With only your own buffs its rotation drops **Sniper Shot** (365 mana) and holds **Aimed Shot** when your mana runs low.
- Moving: **Auto Shot**, **Aimed Shot** and **Sniper Shot** need you to stand still, while **Arcane Shot** and **Serpent Sting** are instant. Do not start a 4-second **Sniper Shot** when you know you must move.
- **Rapid Killing**'s other half (a kill makes your next Shot within 20 seconds hit 20% harder) never happens on a boss; on trash, let the next pull's first **Aimed Shot** spend it.
- A fight that kills pets (cleaves, area damage) takes about a fifth of this build's damage with the cat.
- Watch your ranks: in the beta client (build 70753) the top ranks are the strongest. **Hunter's Mark** rank 4 gives +143 ranged attack power (rank 3 +98), **Trueshot Aura** rank 5 +100 (rank 4 +75; if your build has it) and **Aspect of the Hawk** rank 7 +120 (rank 6 +110). Cast the highest rank you have.

**When to change it**

- Two or three targets close together: **Multi-Shot** instead of **Aimed Shot** (same cooldown, up to 3 targets for weapon damage each). For a pack, **Volley**: a 6-second channel with no cooldown in Forever.
- In the last seconds, skip the **Serpent Sting** refresh and do not start a **Sniper Shot** that will not finish; **Arcane Shot** instead.
- Without a pet, play the Lone Wolf setup linked above, about 1% behind this build in a full raid: its Lone Wolf talent adds 20% to everything you do while no pet is out, and its rotation starts **Sniper Shot** with **Aimed Shot** 2 seconds from ready.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Beast Mastery | 7 | Deadly Aspects 5, Focused Fire 2 |
| Marksmanship | 39 | Lethal Attacks 5, Improved Stings 3, Efficiency 5, Careful Aim 5, Rapid Killing 2, Improved Arcane Shot 2, Trueshot Aura 1, Mortal Shots 5, Rapid Recuperation 2, Barrage 3, Ranged Weapon Specialization 5, Sniper Shot 1 |
| Survival | 5 | Improved Tracking 5 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 1015 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 981 | [7/39/5](https://talentsforever.com/hunter/60/502-0053352401523051-5-12) |
| Phase 1 BiS | 1024 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.5; Phase 1 BiS 63.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Neck | [Amulet of the Darkmoon](https://www.wowhead.com/forever/item=19491) · *quest: 1200 Tickets - Amulet of the Darkmoon* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) | [Theramore Pauldrons](https://www.wowhead.com/forever/item=271955) |
| Back | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) · *quest: Volunteer's Battlegear*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Beaststalker's Bindings](https://www.wowhead.com/forever/item=16681) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Beaststalker's Bindings](https://www.wowhead.com/forever/item=16681) · *Blackrock Spire*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) | [Theramore Gloves](https://www.wowhead.com/forever/item=271948)<br>+ [Enchant Gloves - Agility](https://www.wowhead.com/forever/item=273520) |
| Waist | [Highlander's Mail Girdle](https://www.wowhead.com/forever/item=20044) · *sold by Samuel Hawke* | [Molten Belt](https://www.wowhead.com/forever/item=19163) · *Leatherworking* |
| Legs | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) | [Beaststalker's Pants](https://www.wowhead.com/forever/item=16678) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11647) |
| Feet | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Shadowcraft Boots](https://www.wowhead.com/forever/item=16711) · *Rattlegore, Scholomance*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) · *quest: For The Horde!* |
| Trinket | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* | [Counterattack Lodestone](https://www.wowhead.com/forever/item=18537) · *Tribute, Dire Maul* |
| Main hand | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Legionite Glaive](https://www.wowhead.com/forever/item=250619) · *Blacksmithing*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Gorewood Bow](https://www.wowhead.com/forever/item=16996) · *quest: The Scarlet Oracle, Demetria*<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) | [Rhok'delar, Longbow of the Ancient Keepers](https://www.wowhead.com/forever/item=18713)<br>+ [Biznicks 247x128 Accurascope](https://www.wowhead.com/forever/item=18283) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElU1oK1UUx+fcmcycHDUZ72teJoMfY5BH3sCEmWnnfS1M3luJCymuXGmmTWpS2iYkWVQQbEsXUqoUF9KWQgu1WovuFIrgplKsEGykoFC/ilZQcNFtFURmklA/cNfw/ovhzPnfYf7zO3e4lEJQQQMDMlCAMtRgBmADYBuAPxhaLLBugf59FFEV9VdIwU8+imunD5CEm8tAEh61VFLw0y3QvpSD4sO49lOMFHxvDrTvgqLVUrUfYiRhaw1IwXfmIHhcwc/moNNfbqsk4VttlUR8fZIk/HUpWPjHVlz7LUYCKXg6D9o3V9LX1INK5nQdFoDNV1Yhuum/7397d30LdkBZrLy7Bm9UTmC+cg/D6JCHj9lVz3Yt2/YGBz13yHY8d9D2HMs7YFKb4Y/sWKEBQl0mCdv7kEaSSbIcu0GJbnd7E9JRUihiuVmvwWeBv+DXJl6s1pqGa7s3LMe27KE7xmjZn3qpVDSqdcMvFktFY+Rlo1kuGfVq029WqlNGo+TXR8tGplEqGZOTVt2vFK2eaXXM7HijOnVdf5wS5hWM8MgeYxjRw0h21mv04vCorugREvGwypf6HydLT/I0PXQsE0n49fmznKkSPWzGUebsGUFXKEKiY3fSBbakszsCf/VfuezblnvzUnM9SgMmR7GHKcxhZ52QzM9JbuiP/R/HYMXRAP/iP+ycy2Y3QSO8QCkziSLH8YDQ4T7o4Xaysze9BmnmVZR5dAe6s+19hkdJM4Eyxx3opL0wVDPWRS+TROxGh/zhPvDxvu+Fzi9xvgx8o//wnqIh7obw/kEonKObdb1wvH9HFCGRwAkj7s0Ma+Iv7ADOmDsrCqEy+QVIUZISuPomqL8vgiZfF0Kd5QqY/pNFg1qYGcunVlcCfZ57YizUVzn3hGmSkTN3mXBf1Mz3qr7q2gd9e8/t8Prc2/m73Ua+AK8BrEB4I5zkTBF3k/ceuTiPbLgFeXgahuF5KEMNpmGa/TUANHZhoQ==); Phase 1 BiS: [full raid](https://wowsims.com/forever/hunter/dps/#eJzElV1o62QYx/O8SZOnj9rG96ynafAjFjn0BFKSnJPzdWG7XYkXMrzySputne3Y1tL2YoLgNnYhY+oYCNsQNpjVOfROYQh6MRlOGG4yUNj8GDpBwYvdTkEkacv8wLsV/xfhyfN/Q/75PW94KYWgggYGZKAAZajBFMAawAYAvz+0WGDdAf27KKIq6i+Rgh9/GNdO7yMJT18HkvBwTyUFP22B9qUcFB/EtR9jpOC7M6B9GxR7e6r2fYwkPH4DSMG3ZyB4XMHPZqDdXzpQScJPWkAivjpOEv6yECz8vRXXfo2RQAouL4J2fCV9Td2tZE5XYQ7YbGUFouv+e/43/ast2ARlvvLOm/Ba5QRmKwMYRoc8fMSuerZr2bZ3w/Nc13Y894btOZa3y6QDhj+wI4X6CHWZJDzYgTSSTJLl2A1KdLob65COkkIRy816DT4N/Dm/NvZ8tdY0XNu9ZTm2Zd+8ZwyX/YkXSkWjWjf8YrFUNIZeNJrlklGvNv1mpTphNEp+fbhsZBqlkjE+btX9StHqmlbbzI42qhPX9UcpYV7BCI9sM4YRPYxkZ71GNw6P6ooeIRH3q3yh93Gy9DhP0wNHMpGEX58/zZkq0YNmHGXOnhJ0hSIkOnY7XWBLOrsn8Jf/kcu+a7m3LzXXw9RnchS7mMIcdtYJyfyU5Ib+yH9xDFYc9vEv/sXOuWx2YzTEC5QykyhyHA0I7e+AHm4nO3vba5BmXkWZRzehM9vuZ3iUNBMoc9yEdtoLQzVjHfQyScRutcnv7wAf7fleaP8S50vA13oP7wm6yd0Q3t8IhXN0s64XjveviCIkEjhhxO2pQU38me3CGXOnRSFUJj8HKUpSAlcWQf1tHjT5uhDqLFfA9B8sGtTC1Eg+tbIc6PPcYyOhvsq5J0yTjJy5xYT/Rc18t+qprr3fs/fcDa/PvJXv7zTyBXgFYBnCG+EkZ4q4lRx46OI8suEO5OFJGIRnoQw1mIRJ9ucA8Uhhkg==).

## Other builds of this spec

- [Marksmanship with Beast Mastery support](../research/raid/builds/bm-mm-full-buffs-raid.md) (21/30/0, 942 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/53200005050001-005155000150305--12)
- [Marksmanship (optimized, lone wolf)](../research/raid/builds/opt-mm-lonewolf-raid-raid-dps.md) (7/41/3, 930 DPS in a full raid) — [open the talent tree](https://talentsforever.com/hunter/60/50002-3053552011523051-3-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-18 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

