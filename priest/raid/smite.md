# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**✅ Recommended** for raid (the best priest spec here, or within 3% of it).

**[Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md)** (31/17/3) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-7)

## How to play

**Before the pull:** **Holy Fire**.

**Talents with no line below:** **Holy Nova**: a defensive or healing spell: cast it when you need it, it is not part of the damage rotation.

**Then press the first one that is ready**, top to bottom:

1. **Penance** (rank 3)
2. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
3. **Inner Focus**, then straight away **Devouring Plague**
4. **Holy Fire**: keep it on the target
5. **Inner Focus**, then straight away **Smite**
6. **Shadow Word: Death** (rank 3)
7. **Power Infusion**
8. **Smite**

**Smite** is your filler: cast it whenever nothing above is ready.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Smite in a raid keeps two burns up, **Shadow Word: Pain** and **Holy Fire**, fires **Penance** whenever it is ready and casts **Smite** in every gap. **Holy Fire** counts for more than its own damage: with **Power in Light** your **Smite** and **Penance** deal 10% more while it burns.

**Why it works**

- **Holy Fire** starts 3 seconds before the pull (a 3-second cast with **Divine Fury**), so it lands as the fight begins. Recast it when its burn has about 1.5 seconds left, roughly every 12 seconds: the new one lands just after the old burn ends, and the simulator measured that 0.5% ahead of starting 3 seconds early.
- **Penance** is on top: three Holy bolts in 2 seconds on a 12-second cooldown, about a quarter of your damage, and the simulator measured 3.1% more damage with it first. The full list casts rank 3 (from the community simulator's rotation): a little less damage than rank 4 for 30% less mana, and high enough that our downranking model leaves it its full spell power.
- **Shadow Word: Pain** is about 30% of this build's damage for one global cooldown every 18 seconds. Recast it when it falls off, but not in the last 10 seconds of the fight.
- **Inner Focus** goes into **Devouring Plague** to make it free (its 3-minute cooldown allows one in a 3-minute fight; the list's second **Inner Focus** line, into **Smite**, only comes up in longer fights); the simulator measured about 1% more damage with that pair. Paid for, the plague costs this build about 890 mana (no **Shadowform** or **Devouring Contagion** to cut it), and the simulator measured 2.0% more damage after dropping the plain **Devouring Plague** line.
- **Shadow Word: Death** and **Power Infusion** go out on cooldown, then **Smite** fills everything else. **Mind Blast** is left out: none of your Holy talents help it and it costs more mana than **Smite**, and the simulator measured about 5% more damage casting **Smite** in its place.

**Caveats**

- This build runs short of mana even in a full raid: the simulator's priest also uses two mana potions and two Demonic Runes a fight. **Meditation** keeps half your regeneration going while you cast, and the cheaper ranks the full list picks (rank 3 **Penance**, rank 3 **Shadow Word: Death**, the latter measured 0.5% better than rank 4) are part of the mana plan; neither is far enough below your level to lose spell power in our downranking model.
- The full list still holds a rank 2 **Smite** for 20-50% mana, measured before 2026-10-09; it now sits under the top-rank **Smite** and never fires. Ranks far below your level get much less from your spell power (a beta change; our model leaves rank 2 a small fraction of it), so do not downrank **Smite**.
- **Shadow Word: Death** hits you for 10% of your maximum health each time the boss survives it, about 10 times a fight: your healers pay for that.
- The full list also holds **Mind Blast**, **Shadowform** and **Mind Flay** lines below the unconditional **Smite**: they never fire for this build.

**When to change it**

- When the boss has under 3 seconds to live, cast **Smite** (2 seconds) rather than a new **Holy Fire** (3 seconds): only a spell that finishes casting does damage.
- If healing is tight, cast **Shadow Word: Death** only in the last 20% of the boss's health, as the simulator's rotation for fighting alone does. You give up a little damage.
- When you must move, use the instants: **Shadow Word: Death**, and **Shadow Word: Pain** if it fell off. **Holy Fire**, **Smite** and **Penance** all need you to stand still.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 597 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 603 | [21/23/7](https://talentsforever.com/priest/60/505031021030001-305151001121003-50002-7) |
| Phase 1 BiS | 632 | [21/23/7](https://talentsforever.com/priest/60/505031021030001-305151001121003-50002-7) |

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 65.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Theramore Shoulderpads](https://www.wowhead.com/forever/item=271953) | [Theramore Shoulderpads](https://www.wowhead.com/forever/item=271953) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) | [Theramore Handwraps](https://www.wowhead.com/forever/item=271945) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Dreadmist Leggings](https://www.wowhead.com/forever/item=16699) · *Baron Rivendare, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Alchemist's Stone](https://www.wowhead.com/forever/item=13503) · *Alchemy* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageclaw](https://www.wowhead.com/forever/item=20070)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk9oI2UUn/fNJPPyErPxc93ODovMxq3EyNRvJhtp1kOye5BFUYsQ8GaTTdZk3SahE9iql1X3sAhmtYeVXSv+waIuCvVgKfVQaC9RisaLB0UolaoHD/6jPQgik5mYUntM4zvMn/fex+/3fvObj4+OIcRAAwMSMAkVaMBlgKsAbwN8AMAj3Spzq+Og/xlFjAX0S6Ti8ougbYVJwc3XgRT8ej1GCr7RiZGKK/Og/RAlFVfnQfsuSgr+8o7bs3UNSMXPvIUqLnwE2jWVFPx23q1+0e1Z7MRIxpUqqfjjHGjtO0jBP667lQ/nDsXvi7WriS9bILaLE6+8Cy8Du1KdBbZdvAnsp9O3QH1/DhbOtqobcKV6JtIfLAfLbDQt0iJlCdsSKSGEZaZE2kpbQliWbQmRMtNCCLvNoMPCm+z3CB2mkK5SIIH45qW4SgGSzZTDa3yy0Lj4VL3RNGxhP2BawhTjp4xzlULt6XLJqE8bhVKpXDKKzxrNStmYrjcLzWq9ZjjlwvS5ipFwymXDmao2y2ap4Zi9sumVxy449dq9OulIwYSMr33/CFd0dkris7AHVmRMe9CwY3Q3P063xcMUsr3BW3mKJaMY5OxhSQ+SQswSviatPH9+CJxG7DtJ1QMk41sOeboEsXMd+NVhKHKCjiZHUOahCz0juAxIscbSzr/e4Jp+xD7cZ9lzzWKeR/xPqeBLn0zw2hAY96yztvM4f2YIVvWmXn+MT+0Dlhkw2C5lLf1+OsHje916e/KQ69ai5HaSnBKj/pJWnt8ahmMeogd5Zi8NW4x2U3I/lfZT3q/lk/U8xfArhU8NgasnZwjX8vwu/dg+pPtyh/1mFT/N84tD8BW62w2++tej+7rYGjCa5+LfZvhz/wWzTg4Y7AhF4kRouwPuzILu3zX5Z9aGX5n9gix142RuFRSdkRT/m4XchHT5fO7ozRtufJ49fr4b32TtDaYpRja5xKT/JZq53tOBxj0fHxhOpnt94r3caT+Rm3RPQDeg+yJtZJMyLo2c2XVQEjAOOTgLE/AkVKABMzDD/hkAi2o3LA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk9oI1UYn+/NJPPyJWbjc93ODovMxq3EyNQ3k4006yHZPciiqEUIeLPJJmuybpPQCRj1UrWHIphqpIXWiiIWtSjUg6X0IrSXFIvWiwelUJSqR/9gexCKzJ+YUntMs9/hzcz3vfd+v+83vxkeXqAQAQU0iMEolKAGEwBTAB8AfALAQk6V2NVhUP8OUxrxqQ2U6dproOwFUaKHLUCJfrcVQYm+ux1BmX61CMrPYZTp+iIoP4ZRoptOdW8aUKY7M85CmS5/Bsq0jBL9YdHe4esZe5x8xx5XnH1+WQClfQ9K9K9ZO/npwpnoQ5F2OfZNE/h+fuTND+ENIJPlFpD9/DyQX68ugfzxAixfb5Z3YbJ8LdTtLANrZDDJkzxhcNPgCc65oSd40kganBuGaXCe0JOcc7NNYJsEfyJ/hvAsBlQZfTFK33sxKqMPRT1hsQobzdVuP1et1TWTm4/oBtf58BXtRilXeb5Y0KrjWq5QKBa0/EtavVTUxqv1XL1crWhWMTd+o6TFrGJRs8bK9aJeqFl6p6y75aFbVrXyoIoqRX9MpG/vPMEklVwRWAuOwfKUbvYadgjvZxfxrmgQA6bbeDOLkXiY+hl5XFD9KCExuKdJM8te6QOnAfNelFUfivR9C11d/HR7FthUPxS5hOfjA1RkgVsdI9gMUDKGktZ/3mCKes4822XZcc1KloW8VynR178YYZU+MO5YZ+PgafZCH6zqdr31FBs7ASzVY7Ajyhrqw3iJRY+79e74GdutecGeiWKCD3pLmlm21A/HPIaPstRxGiYfdFJiN5X0Uu6n5ZF1PUXotxIb6wNXV84A3ciy+9QLJ5Duyh30Jsv0yyy73QdfUft3Q9/658kTXWz0GM118R8N9vL/wYzLPQY7h6EoIjXtBg9aoHpXRfyNtOF3Yr4qCk5czqyDpBIUoockYCeEiZuZ8/NzdmymL9504vu0uUsUSUvHV4lwR6Ke6dydajzw+anhpJzxmY8yV71EZtQ+As2B8yDspuMiXR24duSkxGEYMnAdRuBZKEENGtAg/w4ASaY3dw==).

## Other builds of this spec

- [Smite — Raid](../research/raid/builds/smite-open-raid.md) (21/23/7, 597 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505031021030001-305151000221003-50002-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

