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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 508 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 497 | [31/7/13](https://talentsforever.com/shaman/60/5502301300113151-052-05305-6) |
| Phase 1 BiS | 510 | [31/7/13](https://talentsforever.com/shaman/60/5502301300113151-052-05305-6) |

**The gear** (average item level: Pre-BiS 63.3; Phase 1 BiS 64.5; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Deep Earth Spaulders](https://www.wowhead.com/forever/item=18829) · *Molten Core* |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair*<br>+ [Enchant Cloak - Lesser Fire Resistance](https://www.wowhead.com/forever/spell=1248239) |
| Chest | [Zandalar Augur's Hauberk](https://www.wowhead.com/forever/item=19828)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) | [Gloves of the Greatfather](https://www.wowhead.com/forever/item=17721) · *Leatherworking* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21207) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Main hand | [Lord Valthalak's Staff of Command](https://www.wowhead.com/forever/item=22335) · *Lord Valthalak, Blackrock Spire*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Staff of Dominance](https://www.wowhead.com/forever/item=18842) · *Golemagg the Incinerator, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/elemental/#eJzMVEFIFF8Yn+/N6Dw//ev+X1DjIDTuIbalkTezbbhS7CoEUReVDtElR3dsN2x3213CLmFhEB2MupTiIaulgjVEIsRLECGrbLGXijAiLMlDgVTspUvMqCnRMaXf5X3ve7/3vd/v4/FhDQUPKKCBDziw+l87wqEZItAOxyAFAwDqXZlSj6ymUaY/xkFZrEaJLtwAlOj7b/+hTN+MgTJAUKbfR0D5UIsyfZoDZb4WJTqdc2jvyg5t5lGdc1emE3lQrsoo0bkx5/R1DlCkF22U6OOSB2X65CEohW0ooOAN0MG4pxDX7o2C78UQ8HJ3++1ncAXIYPw6kHL3Tbhj3YK8dR8+tU7BolGCoXgbrhubJmowyM0ANwKcG0bACBo6D5o6DwZ4sEDEEoEFkq9AhrJagSJdOuuVsQJF3cywHLColeo7kUxlNZOb+3Qe0s3mFq0nZiVO2lEtmdasaNSOat3ntGzM1tLJrJWNJxNaxrbSPTHNl7Ftze6zT9uJrNWnR1MZfY2ir1CaTmWSid3qAdzLTPT4aykwcQEERwmCgdXeKpRNR9ZMB/7vr6OVjBwWVFegwTMOjc50sD2qHxvZTrdA5YYC5oYC850ue76TSSppEZiibscaLyI1K1Gi+Y+grq4MVerGo3NH2PhWdeAg7ldbkE6CI7J8/g9WGvyqY/+4oLJJUkfF9U6YnLvevnSy5G9yDa7z0CbIXfsr7MwW9afKseoj9JqkiEukAMvEvCAKLpoiX0FiBAXvA7HKSQgDvZH6kWEHs+HGXhevwuYyUSQt7C8Q4Z9CNrIWbSp2jf/1d0LPi8ViTddEpHU1EemCywDDEE8uX5o9+jIccrNCKdzqMIvFz+GOleBt2C/SqR1tDetzamXkHnKHbgxS0A/97OcA2e0nKA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/shaman/elemental/#eJzMVEFIVF0Ufue+p+96FJ3//vD/z4fwP2fxMw09ue9NE44UMwpB1EalRbTJp/NsJmxmmhnCNmGhEEJGipDiIiqpYAyRCGsVFTLWFG5qYytLclEgLdwEEfepKdEypW/x3rnnfvfc7ztcDlZR8IEGBgSAA6v9sSIcGiEGrXAcMtAHoN9WKfWpehZV+nUKtOVKVOi3YUCFXhkBVOnDAdD6CKp0fhS099Wo0qeToC1Wo0IfDQrak1FBm3tQI86qdLoA2lUVFfrsvth9OSq+/SOAMr3kokrHR0Ar/o0SSv4Q7U/6iknjzgQEXg8BX+tsvfkcBoH0J4eBrHVeh1vODSg4d+Fj8ywsWwswlGzBLWOPiR4OczvErRDnlhWywpbJw7bJwyEeLhJ5gcASKZQhQ1UvQ5munPOrWIayaefYJLC4k+k5mc7kDZvb+00eMe3GJqMr4aROuXEjnTWceNyNG53njXzCNbLpvJNPplNGznWyXQkjkHNdw+1xz7ipvNNjxjM5c5NirlMaTufSqT36QdzHbPQFqykweQkkoQTBwkp/Baq2kDXXhn8Fa2g5I0ck3RNo8Zyg0bk2tlcPYj37zytQvq2Ava3AYrvHXmxnik6aJKbp/2CVH5Ha5ajQwgfQN/4MderFEy+Osqnd6sAhPKA3IZ0BIXLtwi+s1AV1Yf+EpLMZUkPlrU7YnHvePrez9E9yLW7yyA7I3Xwr7Owu9adCWA0Qek3R5BVShFViX5QlDw2xL6AwgpL/nlwhElJfd6x2fExgPlrf7eFt1F4lmmJEg0Ui/VHIxzajHcX/U7/9nsirUqlU1TEda95IxDrgMsAYJNOrA/PH3kQjXlZaiDYLZqn0Kdq2HryLBmU6+29L3dacWh+5h72hm4AM9EIv+z4Aclgklg==).

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

