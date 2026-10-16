# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (10/11/30) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055020510310035-6)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Destruction — Incinerate), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Fire: [Destruction (optimized, fire)](../research/raid/builds/opt-fire-destro-raid-raid-dps.md) (10/11/30, 685 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030510310025-6)
- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 665 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-6)

## How to play

**Before the pull:** **Life Tap**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage for 2 hours; summoning any demon cancels it).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Conflagrate**
7. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Shadowburn**: in the last 1.5 seconds of the fight, when there is no time left for another **Shadow Bolt**
- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Destruction in a raid is still a **Shadow Bolt** spec: you sacrifice the Imp for 15% more Shadow damage, keep **Immolate** on the boss so **Conflagrate** can go out every 10 seconds, and let **Shadow and Flame** turn each **Conflagrate** into 10% more Shadow damage.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours; summoning any demon ends it), then **Life Tap** once so you start full. Put a Spellstone (**Create Spellstone**) on your weapon on top of your wizard oil: Forever lets them stack, and the simulator measured about 3% more damage. This build has no **Amplify Curse**; without the sacrifice the simulator measured about 10% less damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school, Fire and Shadow alike, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana (the simulator measured that 0.4% better than 10%), and **Improved Life Tap** adds 20% to each tap.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (0.8 seconds with 3 points in **Improved Corruption**) goes back up when it is about to run out, but not in the last 10 seconds.
- **Immolate** matters as much for **Conflagrate**, which needs it on the target, as for its own damage: start a new one when less than its cast (1.5 seconds with the **Bane** talent) is left on the old one, but not in the last 20 seconds. Both end-of-fight cut-offs measured small gains.
- **Conflagrate** goes out whenever it is ready. With 5 points in **Shadow and Flame** it no longer eats your **Immolate**, and each hit gives you 10% more Shadow damage for 20 seconds, twice its cooldown; **Fire and Brimstone** and **Ruin** make its crits frequent and big. The simulator measured adding it at about 8% more damage.
- **Shadow Bolt** is the filler, not **Incinerate**: the sacrificed Imp, **Improved Shadow Bolt** and **Shadow and Flame** raise Shadow damage only. Even the Incinerate build's own rotation search put **Shadow Bolt** ahead of **Incinerate** in a raid.

**Caveats**

- The last seconds belong to quick spells: with 3.5 seconds left the rotation casts **Searing Pain** (a 1.5-second cast) and with 1.5 left an instant **Shadowburn**, because a **Shadow Bolt** still casting when the boss dies does nothing. Neither belongs earlier in the fight.
- **Shadowburn** on cooldown measured worse in the fire rotation (about 0.8%): it costs nearly as much mana as **Shadow Bolt** for about two thirds of the damage. Keep it for the last global cooldown, or for a moment when you must move.
- With the Imp sacrificed you play without a demon: any summon ends the buff, so if you die, summon the Imp and sacrifice it again before the next pull.
- On the move, **Bane of Agony**, **Curse of the Elements**, **Conflagrate**, **Shadowburn** and **Life Tap** are instant; **Corruption** still has a 0.8-second cast in this build.

**When to change it**

- If you play the Incinerate build listed above instead, it still fills with **Shadow Bolt** in a raid: its full-raid rotation adds **Shadowburn** on cooldown (with 10 or more seconds left) and keeps **Shadow Bolt** ahead of **Incinerate**.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 705 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 683 | [9/11/31](https://talentsforever.com/warlock/60/252-0050203001-055030510310035-6) |
| Phase 1 BiS | 722 | [9/11/31](https://talentsforever.com/warlock/60/252-0050203001-055030510310035-6) (ties this build) |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 65.8; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Stats](https://www.wowhead.com/forever/spell=13824) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Nemesis Leggings](https://www.wowhead.com/forever/item=16930) · *Ragnaros, Molten Core*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18467) · *quest: Harnessing Shadows* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Elemental Attuned Blade](https://www.wowhead.com/forever/item=20698) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Azuresong Mageblade](https://www.wowhead.com/forever/item=17103) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* | [Scepter of Interminable Focus](https://www.wowhead.com/forever/item=22329) · *Stratholme* |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlU+IG3UUx/N+89vM29fdbfZXZWfHP4yBLTEw4TcTxk32kmxPxdMKHoSCNmmyTUJJQiaHipdqVxSRVcypoaCrlLpoNXixelIxmJUoe1HQuiqC6MFDqJKLF5nJNAvbPXjIQt8lL+87v3mf77wfPJpBiIAGBsRAglgc/2MSUpCFNXgK6nAJQH+PUIlM6y6p+O8N0H4/RhwvfwjE8de/Z4njD1tAYdypam+ppOIX10C7NUcKds8Tx5+HsxTG2+veKRU774P2mkocv7o+Rxy/3gJS8IUicXzndSAVf9wCrXeCOH7ygafcvhCVuFGO9MrG9asQ+3YT5DC/9vaX8AqwjfIbwIb5d+GP1Q68eQ1uQuf0LmyWT9G+rU/Zw7Zjm1I60pZJKS1TOo5MSseSSUvKpNNjyi479hvbRjpBqIeJ42AToipNkWI6Lt1Hqj5FCm6fiU6TSlOmlXBc8ZD+AM1Hj9PsR0DE8bOX1gSLTPmnvdzWJcXESZqPH8ewYI+HdP99luP6JS5YPigtO0s6J6bNixaIp3P1C8/U6k3DlvZjpiVNaa8Y50q56vliwag1jFyhUCwY+WeNZqloNGrNXLNcqxpuMdc4VzJibrFouHmzkSsXzDuiORITFbdWfVS3/idUSi55niPDvOA6WwmN7I7Ax8cSjm/34xYcJicD+fKrIJ47YEymTXt5osYWKRKfQ8X/rGHixJylYGiC9PFQRVQ3aCF+P3KhVjz58zM6tlmQjX7E1YNj8GhTE6VdISkStBhfQC6w4sH90gV9us2C9K4JSVcPpMPxlo8Yb28fb+9uPDvA2+uCqByg8+6wNVG60TT/aR3eKz35XpGNFoxv0a0uaMqfrAcDZj+vhPxIZ9tshogQwWAxSLHotjLtCaFL69nF9hUvdjKPrPvxfcYeMI0bmXiPhe6paGbvZEcaJ29MvE/6m36/P3O2k10NCtmz8DLAFSjXBi/uPPldJu1XQ7uZVe/Jfv+vzBOj5KdMXMGbC6ce3F8Yo8132t99JajDRbgo/hsA7Wx8eQ==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/warlock/dps/#eJzMlU9oK1UUxnPuTDo35/W9l96ndDL+YQy0xMCEOxPGJt0k7aq4iuBCKGiTJm0SShMyESpuqqZURCo0dNFQUAtFC1aCG6urKgZSjNqNgtSiCKILF0GlG0FkJtMU2i5cpOBZzJw539y5v2/OhYPDFPwggwoh4MAC/SfCIQZJSMFzUIZVAOUAqeD3KS+iRP8+APmXOyjSfzYBRfrTn3dRpN+/CyjR4y2Q35FQop/vgXx6DwXaWkSRHm3Z4m7NWSfR5gcgvyWhSL/cgv61VgcU6Ks5lOg3ayC3H6BIP/nQrv2xFOS0VvC3C+p7OxD6egP4eSa1+wW8AaRW2ARynnkffp1qwtt7cAjNmRPYKEzjpbFPyeOGaWicm9zgUc51jZsmj3JT51Gd86jZJsIJufMz2af4AKkyhCLtbkBQQi8KmmnhQygpXhTo/mzQhxJ6NT1iWuwx5REcCd7Hux8B2h7XU4z4vc7qo/UUMxSOITaOI+H7dIiRpz2K8z3dtJySyEjGLU2YY4qIRB5hdWDPp8tLL5TKVdXgxlOazjVuTKrz+fTyYi6rlipqOpvNZdXMS2o1n1MrpWq6Wigtq1YuXZnPqyErl1OtjFZJF7Lahaj1xEjRKi0/qej/ESrGx2zP/vMMExUy6enZ7YH3l0VMx+7HdbhJjrrya28Ce/mKMR7XjImBGgugP3yPCs5vHUIRiTnmNo2h0m8qCyoqjoYfpiKTirb82axCG8TNeje2c7UNNm1soLSTyFkEA+FRKjJatOF+bIHiaxA3vdYhbimudDPexC3jnV3inV3HM1y8sxaw4hU6+wzrA6XrdfOv+s17xQe/l79Wh/4pOm2BLPxG2tAlxiuCx4l4skGGEZFSUEkIYiS4L/hswbO6kAw0tu04Tjyx4MR3CaNLZFFNhNvE87+KavIiu9UYPxj4PvGvOp3O8FwzOeUWknPwOsA2FErdteNnv03EnarnJDFlv9np/J54ppf8kAgL9HB0+tHLgdGbfTPO9MtDGVZghf07ACu1e+A=).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-16 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

