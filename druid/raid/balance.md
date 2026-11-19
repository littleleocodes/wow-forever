# Balance Druid — Raid (group)

[Druid](../README.md) > [Raid (group)](README.md) > Balance

**[Balance — Moonkin / Nature's Grace](../research/raid/builds/balance-moonkin-raid.md)** (33/0/18) — [open the talent tree](https://talentsforever.com/druid/60/0532220115501051--5553-12)

## How to play

**Before the pull, then keep up all fight:** **Moonkin Form**.

**Then press the first one that is ready**, top to bottom:

1. **Moonfire**: keep it on the target
2. **Insect Swarm**: keep it on the target
3. **Starfire**

**Starfire** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

A raid Moonkin keeps **Insect Swarm** and **Moonfire** ticking on the boss and casts **Starfire** the rest of the time. **Moonkin Form** goes up before the pull, and **Innervate** is your mana button.

**Why it works**

- **Moonkin Form** first (the rotation shifts 10 seconds before the pull) and for the whole fight: it gives all party or raid members within 45 yards 3% spell critical strike chance and doubles how often **Omen of Clarity** makes your next spell free. A feral druid's **Leader of the Pack** adds melee and ranged crit instead of competing with it, and you cannot heal while in the form.
- **Insect Swarm** and **Moonfire** each do close to a fifth of your damage for one instant cast every 14 to 15 seconds (**Nature's Splendor** makes them last that long, **Genesis** adds 2% to their ticks a point, 10% at 5 points). Recast each one the moment it runs out, not before: recasting a running one throws away the ticks it had left.
- Both sit at the top of the list, above your cooldowns, and when both are due **Moonfire** goes first: its direct hit lands at once and can crit into **Nature's Grace** for the next **Starfire**. The rotation search of 2026-11-01 measured that order about 0.5% better in a full raid than the old **Insect Swarm** first.
- **Starfire** is your filler and about two thirds of your damage. It beats **Wrath** per second of casting at any gear: 350 to 412 damage plus all of your spell power in 3 seconds with **Improved Starfire**, against 92 to 102 plus 57% of it in 2 seconds. The raid build takes no **Eclipse**, so **Wrath** has no place in the list.
- Critical strikes feed the filler: **Vengeance** doubles their bonus damage, and every critical hit from **Starfire** or **Moonfire**'s first hit triggers **Nature's Grace**, 10% faster casts and global cooldown for 3 seconds.
- **Innervate** at 10% mana: for 20 seconds your mana regeneration is five times higher and all of it continues while you cast (6-minute cooldown). The 2026-11-01 search moved it down from 30% (about 0.2% better in a full raid): pressed late, none of it is wasted on a full bar. With a raid's Blessing of Wisdom and Mana Spring you need it in about 1 fight in 10.

**Caveats**

- Moving: **Starfire** needs 3 seconds standing still. Refresh **Insect Swarm** or **Moonfire** while you move, then go back to **Starfire**.
- Damage taken pushes your casts back. **Nature's Focus** gives you a 14% chance a point (70% at 5 points) to ignore each push, and **Barkskin** (1-minute cooldown) stops pushback for 15 seconds without slowing your casts as it did in Classic: press it when the raid is taking damage.
- Without raid mana buffs (a small group, or alone) you run short. The training-dummy rotation then casts rank 1 **Starfire** (95 mana) whenever a full one is out of reach, which the simulator measured better than waiting for mana.
- **Eclipse** (each **Wrath** takes up to 0.5 seconds off your next 2 **Starfire** casts, at 3 points) is not in the raid build despite its name, and no rotation here weaves **Wrath**. A 3-point **Eclipse** with a **Wrath** whenever its charges run out has not been simulated.

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

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 711 |

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

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk8FLFGEYxuf5vnHn7TVsHa3GqcOnUJgwMjMyYV523FOHDtIpuuSsO7or6+7i7sFuCh4iSM1LKAYSgRDUMaRbhbBdyjp08SJKGARR/QEVOyb1D0i/w8f7Pe/78T3v4eEuQhoWFHoxigKqmAXuAOuAeTJpiWZrEPZzSUa61S6xQRvLsD61sk57D8A6rS+DJR3cZIPeL8Lab2ODXi7B2mljSVsTrNO7NXCKfow3Xxm0vAhr0WBJvyKWNJdjSUtTLOnhBKfoe8lqdLDGOj3bTvd0pxvF3rcLGLn3CHch5ourEAfDT9CysYaF4i7mi1lKXCLEC3HGDQZ833c9Lwhczw08xwmCYKAhsC1a98QOuJNpMsU6rb5CD3GKdcdza2anbWbTLOnLtTRsg1tYulM187TdkW1nne6/xr+yboshzZyDmYuqpVuVal35rn/Z8VxnwBtSY4WoPBHnVWVaRfl8nFe526peiNV0pR7Vi5WyqsXR9FhB9dbiWOWiUlQei518teYcDTiHA/2TtUr5kn2O2/tOkW6KnHbowHMv2M0Fvu7DZJuS+sMWLPlZNPBN+HNSS+gPcylbZ8Faz09xoqlos+Nh1+pKkzeZ7vGEjxl/V1i6yvRtCu2/UA+PqmPl4tNj++dKcl5/HA7/EcLRZoBWkFy03UyfpM2z2fN/c+ZiECGuYgQ3UEAVM5gRvwcA+sWHfw==); Pre-BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk8FLFG8Yx+f77uvO+3v8oeNoOE4dXoXChJGZkQnzsuOeOnSQTt1y1h2bFd1ddvZgNw0PIaQWQWgeKoIgsFOEBR0qiq1DLB26eBFFioroHkTMmNQ/IH0OD8/7fL8v7/c9PNQjoMGARD/GEaGKOeAKcBvQ/08llkjDMJ9lhKq1mjVSxY8NGHutxMXOTRAXn28k9VZTo6y4HBm7baSK5yswttqIiyeLibi3DFLF60ftyT1VXF+GsawSF0tfNeLi7Z3E87ipUUaszJAq9tZhNDpJIS4eNrW+Xq1R6n+3hLGrd7EItlBaA/s4+gAt99exVNrGQikv0qzw8ZR1296Q67q243ie7dieZXmeN2Q7DYYma91hW6AuElNZ4mLtBfoEZYlbjh3rXaaeTyJ8OavBVKmFMvZMrB8xO/MdxMW1l/h7zE02oujz0AtBdfpCpVqXru2eshzbGnJG5EQUlC+GRVmpyaBYDIuycEnWo1DWKvWgXqqUZRwGtYlI9sdhKAvBdFCeCK1iNbYODNa+YXAqrpRPmkepY6BdcJ0VlP0Ejn3cTD7wbRc6mSLt37+CkfnEGvjO3PmMkjLoF7ImJ0ZK30/2XzJR5ib9nrXVhDe53smUDzl3mxlc5gY2mfJPqPsH3aFyYuPQ3jmd1nP3/NHfA3882aNVpAdlOzeQEZvd+WN/1s3GMHycwRjOI0IVs5hlvwYAdaOJ/Q==); Raid BiS: [full raid](https://wowsims.com/forever/druid/balance/#eJzEk8FLFG8Yx+f77uvO+3v8oeNoNE4dXoXChJGZWSbMy4576tBBOnXLWXdsVmx3cfZgNw0PIaRlddA8RARBYKcI6xIVxUYQS4cuXiRZioroHkjMmNQ/IH0OD9/3+31e3uc9PNQroMGAxADGEaGGOeAKcAfQ/08jlkTDMJ9lhKq1mzGp4ucGjFY7cbG7AuLiy82k3m5qlBWXI2Ong1Tx/BqMrQ7i4sliEraWQap4/agzuaeKlWUYyypx8fZWki5904iLhRuJftzUSBWtdRiNblKIi4dNrb9Pa5QH3i1h7OpdLIItlNfAPo0+QNv9dSyVt7FQLoh0WPh4ygzby7mum3Mcz7Md23Msy/Y81841GJqs/SPbAvWQmMoSF2sv0C8oS9xy7FjvMfWCRhnx9YwGU6U2ytgXY/2Q2V3oIi6uv8TfNjfZiKLPQy8Gtenz1VpdurZ70nJsK+eMyIkoqFwIS7I6I4NSKSzJ4iVZj0I5U60H9XK1IuMwmJmI5EAchrIYTAeVidAq1WJrv8HaaxiaiquVE+YR6hrsFFxnRWVvAsc+ZiYf+L4DnUyR6vevYGQ+swZ+MHc+o6QM+cWsyYmR0r/L/kscZW7S711bTXiT75tM+ZB3t5nBZX5wkyn/hLq/rw6U4xsH9s6ptJ6954/+NvzxZJNWkR6U7fxgRmweLhz9s3A2huHjNMZwDhFqmMUs+zUA0dmKWQ==).

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

