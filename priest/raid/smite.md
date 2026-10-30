# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**[Smite — Raid](../research/raid/builds/smite-open-raid.md)** (17/17/17) — [open the talent tree](https://talentsforever.com/priest/60/50203003103-30505101002-502520010002-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Discipline/Holy — Smite), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Holy Fire**.

**Talents with no line below:** **Holy Nova**: a defensive or healing spell: cast it when you need it, it is not part of the damage rotation.

**Then press the first one that is ready**, top to bottom:

1. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
2. **Mind Blast**
3. **Inner Focus**, then straight away **Devouring Plague**
4. **Holy Fire**: keep it on the target, when you have at least 40% mana
5. **Inner Focus**, then straight away **Smite**
6. **Shadow Word: Death** (rank 3)
7. **Smite** when you have at least 25% mana
8. **Smite** when you have at least 20% mana

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

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 611 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 613 | [17/17/17](https://talentsforever.com/priest/60/50203003103-30505101002-503520000002-7) |
| Phase 1 BiS | 627 | [17/17/17](https://talentsforever.com/priest/60/50503000103-30515100002-502520010002-7) (ties this build) |

**The gear** (average item level: Pre-BiS 62.2; Phase 1 BiS 65.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellpower Goggles Xtreme Plus](https://www.wowhead.com/forever/item=15999) · *Engineering*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Dreadmist Mask](https://www.wowhead.com/forever/item=16698) · *Darkmaster Gandling, Scholomance*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* | [Theramore Shoulderpads](https://www.wowhead.com/forever/item=271953) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) | [Theramore Handwraps](https://www.wowhead.com/forever/item=271945) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageclaw](https://www.wowhead.com/forever/item=20070)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk1MK1UUnnNn2rk95fHq9fmYN3kx8+rT1Jqpd6bUAC5aWBESlZhM4k5aWmwR2oZpFH8WmLAwJhYlBgNiUCPxJ5qwsSFuMLCpxmhXLnRDMKgLFxoDLEzU3P6AKSxL31nc3t5v7j3f+c43k4s3KQRAAwNCMAFZKMICwKsA7wF8DMB66igR6ADoR1coDXj059BL/31ZO/SjQg/eBlToX2+J8Z1aAFW6swnaz72o0t1N0H7qRYX+/r5AD5cAvfSrvNin0q3PQFtSUaE/bgrwm/ojlVoAFfrmjjjml3XQqneLs1cE9Mn61eBDgWou9F0Z+HFq/PUP4DUgi7llIMepNSC/Dn8K6kfrsDVazu3DYm6k56yuBHxJbse4zaOcRy0eNaM8xmMWtzi3zRiPxmxeD7tKoEb8B+TIj9fQp6voCVH67vNBFT0om1GXLQObSBZnni4US4bN7UdMPmjaA0PGZDaZfyaTNgpzRjKdzqSN1AtGKZsx5gqlZClXyBtuJjk3mTVCbiZjuLO5UsZMF12zBZsNODLtFvIP6hG8j93CK0E/+uwGhbKDgXAv9TIyJuleVJBYvMmu7LDZLnBqiOGjew57qQvp+ux7UNU9KNMNF1Gn6A15aW0FmKKTIYlttLfB4qY92GEOjyJnEbwR7qMy8023vCC4oMIjMRfvCl8VLUlJQhuU+/n9p45hmn7dvnZWQstLFYfluyBfQzGZ7p08wZ49LxXvdL5Gnd8+zha60Zib7crbsZbyFYdZ+sN4mwXb35+2LdHTZpWdLrMea1KwuCsmIUK/V9i9F1R1SrHiML/esJBKv3DYTBdaSsV3hr7x92MXGsjqcLaGgf6cZy+eT2b1dzjZdewJIlJbFHiyDHrzV5N/I1X4g9ivyFI9+hO7oOgEpeA/xCcWpIWpxI21VRFfx29N1eOHuL1PNMWIh7eJdEeilGjNLjUe+PzS8gzWxyc/TAw3FxIT4gqyCvU/0n48LNPtvpH/3VQ4DEACRmEcnoIsFGEe5sl/AwDNbRB+); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk9oI2UUn/fNJPPlpduNn+t2dlhkNq4SIxO/mXSkXQ/J7qkU1CIMeLNJk5rUNgmdgFEvVXoQwVQiLbRWKmLxDwq9GEovQntJsWi9eFCEolQ9KmJ7EIrMJGkl7THNvsObb97j+97v/d5vhg9vUgiBAhpEYBxyUII5gLcAPgT4FID1eVniZodAPb5CacinVlCmW2+CchhEiZ7UACX6/V4IJfr+fghl+vU6KL/2o0y310H5qR8luutlDxcAZfrzordRphtfgLIgo0R/XHdP+GbR9fPvub7unfPbKiiNB1Gify+5wc9Wr4afCDXykW+rwI/SY+98BG8Dmc/XgBylV4D8fvdzkD9ZhY2Rav4A5vP3+s46S8IWuW1xi8c55waP63FuGZbBOeembnHTMt0w52aDwD4J/kL+CeI1DKgy+iKUfvBKWEYfinrcYTVg46nS9IvFUlkzufmUzod1c+iONpFLFV7KZrTirJbKZLIZLf2qVs5ltdliOVXOFwuak03NTuS0iJPNas5MvpzVMyVHb6f1Zjo25RQLj6sxfITdwivhIAbMJoSqjaFoP/UzMiqofpSQGLyFrmqzmR5gapIRoDs2e70H5QbMh1BWfSjSNQdRpeiP+On+EjBJJXcEttY5BoPr5nCXMTyNnMXwRnSAiiww1daCiwUlHrMcfCB61R1JWnC5QXGQP3qqGKao181rZy20tVS3WaEH9DUZE+nO8XPs5fNU8W7Xa/a59yyb68VgbnYyb1pt5us2M9Qn8TYLd34/HVvip8Oq2j1GPdqCYHDHXUQI/U5iD1/Q1SnEus2CalNCMv3KZtM9GCl1/zP03X+fuVBARperNQX0V4W9dr6YMdjlYtexL4xITbfB4xqoraci/kEa8Ccx3xAFzwaT2yCpBIXwCQm4AWFuMnljZdm13cStSc9+SJgHRJG0RHSTCPfFysn26lLtsS8vrc6w55//OHm3FUiOu5eQZfBehINEVKSbA/f+d1fhMARJGIExeAFyUIIKVMh/AwBg9BCL).

## Other builds of this spec

- [Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md) (31/17/3, 594 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

