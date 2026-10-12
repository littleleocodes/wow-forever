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

*Gear-tier numbers searched on 2026-10-03, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

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
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Lord Valthalak's Staff of Command](https://www.wowhead.com/forever/item=22335) · *Lord Valthalak, Blackrock Spire*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Staff of Dominance](https://www.wowhead.com/forever/item=18842) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/enhancement/#eJzMlE9IG1kcx+f3ZpJ5+a2rcXTZcdZlxwiLG5jwJuMsxkuip2VPBvbgbZ014yb7JwmZsLiXYlv7B2krPbVKDy1FbCFaC6VYLwULaSwp5NAW+odSWgUPPUhbLLSXMknU1nOVfk9vvnze/L7v/R4/bKDgBxlU6AIGUtv2F2HQAzEYgEHIwhiAsiJSr19UcijS93Mgr32FAj18BVCgz15/jSJ9eAHkMYIifTMN8otGFOnyDMiPG1GgSzMu9nTTxYrXmty9Il0ogDwpokBvz7rMrXlAnh6yUaDXK34U6c15kEstyCEXMOh4yl9KySdS6uw56Hr198DqVRicODABZDx1Fi5a56FgXYJHfYuwppcAKnAq1Y87B1si35km0w1DNxjTmcFMjZmMGRozDWaWCFQI/5zc8eA3SBUvCvR0EQI+FNGjdYdMB1vq9mQRAiJ6kNcMB1tRVDzI02K8juoh05F+UL7HlmAzFSTPBE8ouPuQMGfrt7sB8gkwWQRJUEgvJ6FSK3nvGEhnQBqxsv/8nsnm1TAL/6yxiBbu6VWHk1b6TzuhZnKqlUjYCfWP/9V80lZzmbyVT2XSqmNbueGk2uXYtmqnk1Z62P7XTue1RNbRtiCtBoX+cjLpnxQNO6UObAgg0rBbvrAK2Bxsol6J/Mop1bPr9ayFVZBO7k6mM41F9iRZJypBmXol3zK4wW68lZXqtXeHwnpPtRHr/0lH9++m2j/uIr/dRTdIMS75lNrjmI9LuX2LVHsxU5uyzK+TEmyQ8EGeq6o19g5QoUgo+HkZApd5n2tzYyOxtukpVyvRjpGqHkTDG0QW1GiwRLgvSvnY1mpP9ePcZ68TuVsulxuGFmJ9dSM2BMcBpiCV2Tiy8tv9aKTqcpVon0uWyy+j8driSTTI08Vv+9t3hlltLv9SncxJyMIojEofBgALbC4N); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/elemental/#eJzMVE9IFFEYn+/N6Dw/TbcX1DgIjXuIbWnkzWwbrhS7CkHURaVDdMnRHdsN29l2l7BLWGwQHpQUIcVD/6QCjfBknaJC1trCS0HYISzJQ4EUeAkiZtSU6JjS7zDzve/93vd+v4/HhxUUfKCABgHgwKp/rwiHeohBM5yANPQAqHdkSn2ymkGZ/pgAZaEcJfpzAFCiH75vQ5m+uwlKD0GZzgyB8rESZfp0DJS5SpToo16X9mQIUKaTee+sTAf6QemXUaLPHri7L4fcb34QUKSXbZTpyCAohR0ooOAP0XzSV0hqd0ch8LoP+HJ7863n0AsknxwAstx+HW5bN2DcugefG6dgwZiFvmQTrht7TNRwmPMQN0LcNIyQETZ0Hjb1kBni4QIRZwnMk/ESZCirJSjSxfN+GUtQ1M0sGwMWt9Jdp5x0TjO5eUDnEd2sb9A6ElbqtB3XnIxmxeN2XGu/oOUStpZxclYu6aS0rG1lOhJaIGvbmt1ln7VTOatLj6ez+hpFX6HUnck6qb3qIdzPTPQFKykwcR4EVwmCgeX+MpRNV9Z0C24PVtFSRo4KqifQ4FmXRqdb2D41iLVst1egdEMBc0OBuVaPPdfKJJU0CExRd2KFH5GapSjR8U+grv4ZqtSLR18cYxNb1YHDeFBtQDoJrsjli3+xUhNUXfsnBZVNkioqrnfC5Nzz9rWVOX/INbjOI5sgd+2tsHNb1J8y12qA0GuSIi6SAiwR85IoeKiLfQOJERT898UyNyH0dMaqR4ZdzERrOz28jZpLRJG0aLBAhP8KudhatKnYM/HP74m8KhaLFW0PY42riVgbXAUYhqSzdGXm+JtoxMsKs9FGl1ksfom2rATvo0GRTu1qqlmfUysj94g3dBOQhm7oZr8GAOmxJQc=).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-12 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

