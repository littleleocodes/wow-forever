# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**[Smite — Raid](../research/raid/builds/smite-open-raid.md)** (17/17/17) — [open the talent tree](https://talentsforever.com/priest/60/50203003103-00515121002-502520010002-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Discipline/Holy — Smite), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Holy Fire**.

**Then press the first one that is ready**, top to bottom:

1. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
2. **Mind Blast**
3. **Inner Focus**, then straight away **Devouring Plague**; no global cooldown, so press it alongside the others
4. **Holy Fire**: keep it on the target, when you have at least 40% mana
5. **Inner Focus**, then straight away **Smite**; no global cooldown, so press it alongside the others
6. **Shadow Word: Death** (rank 3)
7. **Smite** when you have at least 25% mana
8. **Smite** when you have at least 20% mana

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Smite in a raid keeps **Shadow Word: Pain** on the boss, fires **Mind Blast** every time it is ready, keeps **Holy Fire** burning while your mana holds, casts **Shadow Word: Death** on cooldown and **Smite** in every gap. **Power in Light** is the tree's reason: your **Smite** deals 10% more while your **Holy Fire** or **Shadow Word: Pain** is on the target. 602 DPS in a full raid against the Shadow page's 788.

**Why it works**

- **Shadow Word: Pain** (8 casts, 19%) comes first: instant, 762 damage over 24 seconds with **Improved Shadow Word: Pain**, and the cheapest way to keep **Power in Light** on. Recast it when it falls off, not in the last 10 seconds.
- **Mind Blast** whenever it is ready (22 casts, 19%): 477-503 damage in a 1.5-second cast every 5.5 seconds with **Improved Mind Blast**. It costs more than a **Smite** but lands far more per cast; **Shadow Focus** gives it hit.
- **Inner Focus** goes into **Devouring Plague** at the pull: the plague is free that once (985 mana otherwise, which this build cannot halve) and runs 24 seconds. In a longer fight the second **Inner Focus** goes into a **Smite** for its 25% crit bonus.
- **Holy Fire** (6 casts, 8%): 184-232 damage plus 75 over 10 seconds in a 3-second cast with **Divine Fury**; one goes out 3 seconds before the pull, and the list recasts it as its burn ends while you have at least 40% mana. **Searing Light** adds 5% Holy damage, **Holy Specialization** 5% crit, **Holy Precision** 18% hit.
- **Shadow Word: Death** (10 casts, 8%) on its 18-second cooldown: the list casts rank 3 (the search measured it 0.5% ahead of rank 4: less mana for nearly the same hit).
- **Smite** is the filler (60 casts, 45%): 2 seconds with **Divine Fury**, 280 mana less **Mental Agility**'s 10%, 10% more under your **Shadow Word: Pain** or **Holy Fire**. The page's two **Smite** lines are mana gates: top rank above 25% mana; between 20 and 25% the full list drops to rank 2, under 20% to rank 7, and only when you cannot afford even that does it channel **Mind Flay** (no casts in the simulator's raid fights).
- Mana: **Meditation** keeps half your regeneration going while you cast; the simulator's priest also uses two mana potions and two Demonic Runes a fight and still runs dry late. In a 6-minute fight its DPS falls from 602 to 280.

**Caveats**

- This build has no **Penance** (it needs 20 Discipline points) and no **Power Infusion** or **Shadowform**: the full list's lines for them never fire. The Smite page is a showcase for the tree, 24% behind Shadow.
- **Shadow Word: Death** hits you for 30% of your maximum health each time the boss survives it, about 10 times a fight: your healers pay for that.
- When you must move, use the instants: **Shadow Word: Death**, and **Shadow Word: Pain** if it fell off. **Holy Fire**, **Smite** and **Mind Blast** all need you to stand still.
- Ranks far below your level get much less from your spell power (a Forever change; our model gives rank 2 a small share of it), so the rank-2 **Smite** line is a stopgap, not a mana trick to use early.

**When to change it**

- When the boss has under 3 seconds to live, cast **Smite** rather than a new **Holy Fire**: only a spell that finishes casting does damage.
- If healing is tight, cast **Shadow Word: Death** only in the last 20% of the boss's health, as the simulator's rotation for fighting alone does.
- Packs: **Holy Nova** hits everything within 10 yards and heals your party, and **Searing Light** gives each **Holy Fire** tick a 10% chance to make your next **Holy Nova** cost no mana.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 17 | Power in Light 5, Twin Disciplines 2, Holy Precision 3, Mental Agility 3, Inner Focus 1, Meditation 3 |
| Holy | 17 | Holy Specialization 5, Divine Fury 5, Holy Nova 1, Blessed Recovery 2, Inspiration 1, Searing Light 2, Spell Warding 1 |
| Shadow | 17 | Shadow Focus 5, Improved Mind Blast 5, Improved Shadow Word: Pain 2, Mind Flay 1, Shadow Weaving 2, Spirit Tap 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 616 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 604 | [17/17/17](https://talentsforever.com/priest/60/50203003103-00515121002-503520000002-12) |
| Phase 1 BiS | 632 | [17/17/17](https://talentsforever.com/priest/60/50203003103-00525111002-502520010002-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 59.9; Phase 1 BiS 62.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellpower Goggles Xtreme Plus](https://www.wowhead.com/forever/item=15999) · *Engineering*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellpower Goggles Xtreme Plus](https://www.wowhead.com/forever/item=15999) · *Engineering*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) · *quest: Armaments of War* | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) · *quest: Armaments of War* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk1oK1UUnnNnkrk5qXnx+nydNzxkXnxKjEy8c9NI+xSS91aloBZhwJ1NmtSktknoRKw/iwoVRDDVIkprpSoWf1DoxlDcVNpNFNGs3IhQKlUXXShCuxBUZpJUSbtM887i5OYe7nzf+c43w8UrFMKggQFRmIACVGAB4BWA9wA+BmADXpW41WHQfwpRGvbpz6Cf/vOidhBEhe6/DajQP9908zvNMKp0ewO0n0Oo0p0N0H4MoUIP33erB0uAfvpVyT2n0s3PQFtSUaHfeMXaYRgVWm+6+Y1t9zG/rIHWuANl+vLDqNBP1i5E7g83itHvasCPsuOvfQCvAlksLgM5yq4C+fXGp6B+tAabo7XiHiwWb1KPOKThS3ItyQVPcJ6weMLkPGklLWFxLswkTyQF90I0CDRJcJ/sD+BFDOgq+qKUvvtsREUfymbCYcvAJjKVmSfLlaohuHjQ5COmGL5uTBYypafyOaM8Z2RyuXzOyD5nVAt5Y65czVSL5ZLh5DNzkwUj6uTzhjNbrObNXMUxO2WzVY5PO+XSfXoc72ZX8bZIEAOiRaFmYzgWon5GxiTdjwoSi7fZ1Ww22wdOLTECdNdmL/QBblDciaruQ5muO4g6RX/UT5tvAVN0cl1i691jsLgpRnrM4SHkLI6XY4NUZoHpjhdcLqjweNLB22MX3JFkJVcblIf4PSeOYZp+SVz8r4WOl+o2K/VBvpZiMt09fow9fVoq3mu8Vp/fPsoW+jGYK93Ki2RH+brNLP0BvMYi3e9P15HEybBqdp9Zj7UpWNxxF1FCv1fYXWd0dUKxbrOg3rKQSr+w2UwfRkrd7wx9/a9HzjSQ1WO0loH+mD8NZpk8cR5g4aMse/50Z9ZQj8Eu4UAEkQpXzeNl0Nu/mvwbacDvRLwkS14MpXdA0QlKkb9JwN2QFqbSl1dX3Pg6dXXKix9SYo9oipGKbRHplkQ13Vmda9z7+bnhjHj58Q/TN9ob6Qn3qrMC3h9pLxWT6dbgzf/diDgMQxpGYRyegAJUYB7myb8DAEOLMyc=); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk1oK1UUnnNnkrk5qXnx+nydNzxkXnxKjEy8c9NI+xSS91aloBZhwJ1NmtSktknoBK0/iwoVRDCVaIXWSlUs/qDQjaG4EdpN/EG7ciNKqVRduFCEdiFUmUlSJe0yjWdx5849c+f7zne+GS5eoRAGDQyIwgQUoAILAC8BvA3wAQAb8LLEzQ6D/mOI0rBPfwr99O/ntYMgKvS4DqjQP193xzd3w6jSzzdA+ymEKt3eAO37ECr0t3fc7MESoEp/WAZ3o0o3PwZtSUWFfrXsZr/0nll8zR0b3nt+XgOteRvK9MUHUaEfrl2I3BtuFqPf1IAfZsdfeRdeBrJYrAM5zK4C+eXGR6C+vwabo7XiHiwWb1KPOaThM3ItyQVPcJ6weMLkPCmSlmVxLswkF0nBucU5F00CuyS4T/YH8CIGdBV9UUrfejqiog9lM+GwOrCJTGXm8XKlaggu7jf5iCmGrxuThUzpiXzOKM8ZmVwunzOyzxjVQt6YK1cz1WK5ZDj5zNxkwYg6+bzhzBareTNXccxO2myl49NOuXSPHsc72VW8JRLEgGhRqNkYjoWon5ExSfejgsTibXY1m832gVNLjADdsdlzfYAbFLejqvtQpusOok7RH/XT3TeAKTq5LrH17jZY3BQjPebwAHIWx8uxQSqzwHTHCy4XVHg86eCtsQtuS7KSqw3KQ/yuE8cwTb8kLv5bQsdLDZuV+iBfSzGZ7hw9wp48LRXvNV6rzq8fZgv9aMyVbuVFsqN8w2aWfh9eY5Hu76drS+KkWTW7z6zH2hQs7riTKKHfKuyOM6o6odiwWVBvWUiln9pspg8tpe5/hr7610NnGsjqMVrLQH/MnwazTJ44D7DwYZY9e7oya6jHYJdwIIJIhavmUR309lWTfyVN+J2IF2TJi6H0Nig6QSlyTALugrQwlb68uuLGF6mrU158lxJ7RFOMVGyLSP9LVNOd2bnG3Z+cG86INz76XvpGeyE94Z51VsC7kfZSMZluDd78z5GIwzCkYRTG4TEoQAXmYZ78MwDNjzMV).

## Other builds of this spec

- [Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md) (31/17/3, 597 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

