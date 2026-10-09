# Elemental Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Elemental

**[Elemental (optimized)](../research/raid/builds/opt-elemental-dps-raid-dps.md)** (31/7/13) — [open the talent tree](https://talentsforever.com/shaman/60/5500301303113051-052-05305-6)

## How to play

**Before the pull:** **Lightning Bolt**.

**Keep up all fight:** **Searing Totem**.

**Then press the first one that is ready**, top to bottom:

1. **Flame Shock**: keep it on the target
2. **Lava Burst**
3. **Chain Lightning** when Clearcasting is active or there are 2 or more targets or you have mana to spare for the rest of the fight
4. **Lightning Bolt**

**Lightning Bolt** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

**Lightning Bolt** fills every gap; around it you keep **Flame Shock** ticking, cast **Lava Burst** on cooldown, spend Clearcasting on **Chain Lightning** and keep a **Searing Totem** down. Forever removed Elemental Mastery, so there is no burst window: you play the same list from pull to kill.

**Why it works**

- **Flame Shock** comes first because **Lava Burst** deals 20% more damage while your Flame Shock is on the target, and the burn itself is about a fifth of your damage. Recast it only after it falls off: it lasts 12 seconds and the shock cooldown is 6, so it never has to wait.
- **Lava Burst** has the cast time of a **Lightning Bolt** and hits harder, and 20% harder again with Flame Shock up. Only its 10-second cooldown holds it back, so cast it whenever it is ready.
- **Chain Lightning** waits for Clearcasting: **Elemental Focus** gives each damage spell a 10% chance to make your next one free. Chain Lightning costs more than twice the mana of a Lightning Bolt, so a free one saves the most, and on one target it does about the same damage per second of casting (1.5 seconds against 2 with **Elemental Alacrity**).
- **Lightning Bolt** is the filler, always at the top rank. With a full raid's mana buffs the simulator does not run you dry in a 3-minute fight, and dropping the old rule that switched to a cheap low rank to save mana measured 1.4% better. Start the first bolt 2 seconds before the pull so it lands as the fight starts.
- **Searing Totem** shoots the boss for about 7% of your damage. It lasts 55 seconds, so drop a new one when it expires, and stand within 20 yards of the boss: that is as far as it shoots.

**Caveats**

- Several targets: with two or more enemies close together the rotation casts **Chain Lightning** whenever it is ready (3 targets, each jump 30% weaker) and swaps **Searing Totem** for **Magma Totem**. Magma Totem only hits enemies within 8 yards of it; **Totemic Projection** can move it, but it moves all your totems.
- Mana: in a full raid you will not run dry in 3 minutes; the simulator's list falls back to a cheap rank 2 **Lightning Bolt** only when it cannot pay for the top rank, which almost never happens there. Alone, or in much longer fights, keep **Chain Lightning** for Clearcasting and drink a mana potion instead of downranking: Forever gives ranks far below your level much less from spell power (Blizzard's beta notes; the exact rule is not published).
- Moving: **Flame Shock** (28 yards with your point in **Elemental Reach**) and your totems are instant, so use them while you move. If you must keep moving, an **Earth Shock** (20 yards) beats casting nothing as long as Flame Shock has more than 6 seconds left: the two share a cooldown.
- Your other totems: the simulator's full raid already counts **Mana Spring Totem**, **Strength of Earth Totem** and **Windfury Totem** as up, so this list drops only your Fire totem. If you are your group's shaman, drop what your group needs at the pull; they last 5 minutes.

**When to change it**

- In the last 10 seconds, do not drop a new **Searing Totem**: it would shoot only a few times. Cast a **Lightning Bolt** instead (the simulator measured this 0.5% better).
- When your mana will clearly outlast the fight (more than 200 mana for every second left, say 6,000 with 30 seconds to go), cast **Chain Lightning** whenever it is ready, not only on Clearcasting. The simulator measured a small gain.
- If the boss will die before a 2-second cast can finish, only an instant still lands: an **Earth Shock**, which hits harder at once than **Flame Shock**.
- On a real pull, give the tank a moment before your first bolt: the simulator never lets the boss turn on you.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 510 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 543 | [30/8/13](https://talentsforever.com/shaman/60/550133130010305-05003-05305-6) |
| Phase 1 BiS | 556 | [31/7/13](https://talentsforever.com/shaman/60/5500301302113151-052-32305-6) |

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 64.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) |
| Chest | [Zandalar Augur's Hauberk](https://www.wowhead.com/forever/item=19828)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) | [Gloves of the Greatfather](https://www.wowhead.com/forever/item=17721) · *Leatherworking* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Legplates of Ten Storms](https://www.wowhead.com/forever/item=16946) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Waterspout Boots](https://www.wowhead.com/forever/item=18322) · *Hydrospawn, Dire Maul*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak"].." - "..format(AL["Tier %s Sets, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Lord Valthalak's Staff of Command](https://www.wowhead.com/forever/item=22335) · *Lord Valthalak"].." - "..format(AL["Tier %s Sets, Blackrock Spire*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Staff of Dominance](https://www.wowhead.com/forever/item=18842) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/enhancement/#eJzMlE1oE1sUx+fcmWRuzutr02kfb968Pt40hUdfcMKdiSNtN0m7ElcGXLizYzM18SMJmSB1V7V+UNTqSlsUFCkqpLULkdqNUCGkEiELFfxARFvowkWpUkE3Mknaate2+F/dOfzunP+95/LHOgp+kEGFdmAgta19EQYdEIXdsBd6IQEZGAQ4C3ARQJkVqdcvKlkU6dcJkBd+Q4GevAso0Lcff0eRvrgB8iBBkX4aA/l9PYp0dhzkV/Uo0JlxF3uz4mKFew3uXpFO5UEeEVGg15b9KNBHk4A8PWGjQO+X/SjSh5MgF5uQQy6wjQ4l/cWkfC6p3roK7cuHhoEMJa/ATes65K3b8LJ7Ghb0IkAZLiR7cP1sM+Rv02R6OKyHGdNZmJkaMxkLa8wMM7NIoEz4d+SxB/9AqnhRoJcKEPChiB5te8h0sKlWHilAQEQP8lrYwWYUFQ/ytBCroXrIdKR/lX+wKdhIBckzzBMK7j4kzFn97UaA/ACMFEASFNLFSahUWz49A9JlkPqtzOF96UxONZixQ2OdmtHRpfYlrNQBO66ms6oVj9txdf8xNZew1Ww6Z+WS6ZTq2Fa2L6G2O7at2qmEleqzj9ipnBbPONoqpFWh0EEnnfpf0bBNasW6ACI13Pb5ecDGYAP1SmQXp1TOrte85udBOr/Rmc40ZmyKszZUgjL1Sr5ZcI09+CwrlWs3Qh26URnE4lHp9NbdVMv3U+TXpugaKcQkn1J9HJMxKbtllqovZnRFlvlFUoQlYhznuYqao18AFYqEgp+XIXCH97llbrA/+tfYqKu5SGt/Rc8jxhKRRTUSLBLul1IuurraVP038dP7dD4plUp1vVPR7loh2uvG6Sgk00un5vY8i3RWqlw50u2SpdKHSKy6eB0J8nT6z56W9TCrRvPOSjgnIAMDMCB9GwC1zSzG) · [training dummy](https://elliotwood.github.io/Forever/forever/shaman/elemental/#eJzMkEFoE1kYx+d7M8m8fO226dtld/ZRdqc5LGnY6c5MNmVbVpIWRNBTiicvdtpMTaRmajKIXqRqBfFQqRdtqaBIUaGtpYiUXgSFkkqUIChIRaRa7EGhVMnFi8wYsQePWvxf3sfH//v/fzwUGIkCfxSkNCzzAsr0wwwoa3Uo0VM3ASX64t1PKNOnV0AZJijT9xOgvGxAmd6dAmWlASW6OOXZnlc929KtRu9WpnPToJyTUaKXNsMo0XuzgCI9aaNEb1fCKNM7s6CUfkYBhcg/dCQXLuXUa5MQfTgKerXvLJCR3Hkg1b6LcNW6DNPWdXjdtQBrRgVGc93CIuGJhK7HDSOuG4YRNxKGpidMLW7G9USJiBUCq2RdQoYyD6BI149EZAygqJlFNgUsYw0N7neGXNXUzXZN79DM/zrV/qyVP2BnVKegWpmMnVH7jqlu1lYLjmu5OSevFm2r0J9Vo0XbVu1B+5Cdd61BLTNU1AqOa7k5J68VbavQn207WHTyrXwH/stMDMcaKDBxFQQeQBHBwLpICGUzgCJdSmNTrJEGGdktcB/Q1Is+8FKa/c1j2ML+9AOCWwLMLQErPb57pYdJnHQKTOG/Yn0EkZpBlOj0K+C1lyGn/jx5fw/bxXfi/7wT6Tx419XjX+lojnEaZGSfwNk8aaTiF0RD1/3Stz1sbLu+shX/iDXXeH6ZJ001nhDKGDDb28yEhxaV6YU0O7xNSCG/ktAxSRHXSQk2iHlCFHy1pTZBYgSFyA0x5C2E4YHU7xPjnpaTLQO+niTNDaLIajJWIsIPJTf1efqu+mvmm/d0PCiXy/W9c6mu2iLVC2cAxiHnbJxe3vs42eFvhUqyy3OWy2+S6U/Ds2RMpAu/dQtH2ccBAJM+/f8=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/elemental/#eJzMlFFIFFsYx+c7M+4cP73rei7cO54r3HHvRfYud2xmtg2VYlchiHpJ6SF6ydEd2w3b3XaXsJew2CB80FKEFIMipAKF2CfrKXqQtbbwpSLsITTJhwIx8CWImHFNH3os6f8y33z85pv//xz4sJqCDxRQIQA6sH++vREdmiEKR+E4dEEc0jAAcAXgKgB/5aHUJ/MMyvTzDCgrVSjRLyOAEn376TeU6etboAwQlOn8GCjLXpTp4ylQFr0o0QeDDvZoDFCmhbz7rUxHhkEZllGiN9Z9KNGnYw6THwUU6SUbZToxCkrxdxRQ8O+h+YSvmFDvTELg+RDoG92DQPKJESAb3dfhtnUTpq278L5tFlaMBRhKtON2vIeEh8O6HtKNkG4aRsgIG5oeNrWQGdLDRSIuEFgiyxIylHkFinT1nF/GChQ1M8umgMWsdN/JVDqnmrq5T9NbNLO5Ve2JW8lTdkxNZVQrFrNjavd5NRe31UwqZ+USqaSata1MT1wNZG1btfvsM3YyZ/VpsXRW20K0TaTpdDaV/I8fwL3MRF/QS4GJSyA4ThAMrPJXomw6tuY6sDZYQz2MHBa4a9DQsw5G5zrY/zyIDexvd4BnxwBzx4DFTpde7GQSJ60CU/gfWO1HpKYHJTr9Dnj5yZBTt558coTN7NYJHMT9vBVpARyTGxe+E6U+yJ34JwTOCqSGitsnYeq6m+1jJ2vk/+JfwboyWFsg3jLoQQlJKFy+YnZ2l2JVOg4DhF6TFHGVFGGNmBdFwVVTdB0kRlDw3xMrnYYw0Butmxh3NB9p6HX1MmKuEUVWI8EiEX4p5aJb1U9V48wP/0/Ls1KpVN11P9pWbkS7nB03DonU2uX5Yy8iLW5XWIi0OWSp9CHSsVm8iQRFOvtne/32etncl4fcjRmHNPRDP/s6ABq/BTc=) · [training dummy](https://elliotwood.github.io/Forever/forever/shaman/elemental/#eJzMkEFoE1kYx+d7M8l7+dpt07fL7uyj7E5zWNKw051MNmVbdklaWBZ2Tyl78mKnzdREaqYmg+hFqkSQHlraUrSlgiJFhRYkp+pJPJRUoxRBQepBqsUeFEqFXgSRGSP24FGL/8v7+Pi////HhxInURAPgoyFqSgiZW+WQN1sQIW9nQJU2NPX3yBljy+BOkqQstUZUJ81IWW3F0Bdb0KF3RjzbLdmACmrlP2/lE1NgDpBUWEXdsKosLsznqc8DSiz0zZSNjcNavVblFCK/MbK+XA1r12Zh+j9cTB2B8aAlPNTQHYHzsNl6yIsWlfhRc8ybMbXYDzfK90kIpk0jIQRTxiJeDxhJOO6kTR1M5EwklUirxHYIFsKcqQigDLbOhahGEBZN0t8AXjWGhk+6Iy4mmmYnbrRpZt/dGuDOatwyM5qTlGzslk7qw2c0NycrRUd13LzTkEr2VZxMKdFS7at2cP2EbvgWsN6dqSkFx3XcvNOQS/ZVnEw13G45BTaxV/4OzcxHGtiwOUNkEQAZYQ4NkRCSM0Aymwlgy2xZhbk5F9JUAygbBolH3glw38VMWzjP/sBwT0B5p6A9T7fvd7HFUG6Ja6K77ExgsjMICps8TmI+stRMH+ev/Mf/0f8jX+KbmQV8H7vnvxER2tMeFwHJMErpJnJHxHjhuGXvurjk/t1ynb8KdZa5/muQlrqPCGkGDA7O8ykd70oZecy/Og+IYX8SsImFVXeIlXYJuYpWfLVkd4BhROUItfkkLeQRofSP87NelpNtQ35epQyt4lKtVSsSqSvSm76w/RF9cvSZ+/puler1Rr7r6d76ot0P5wFmIW8s31m9f+HqS5/K62lejxnrfYylXk/PEnFZLb8Q690nL8bAAS0/Co=).

## Other builds of this spec

- [Elemental — Raid](../research/raid/builds/elemental-raid.md) (31/7/13, 510 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5500301303113051-052-05305-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

