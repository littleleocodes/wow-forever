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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 602 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 604 | [17/17/17](https://talentsforever.com/priest/60/50203003103-00515121002-503520000002-12) |
| Phase 1 BiS | 632 | [17/17/17](https://talentsforever.com/priest/60/50203003103-00525111002-502520010002-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 59.1; Phase 1 BiS 61.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183) · *quest: Veteran's Battlegear*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) · *quest: Armaments of War* | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) · *quest: Armaments of War* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [item 254013](https://www.wowhead.com/forever/item=254013)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* | [Orb of the Forgotten Seer](https://www.wowhead.com/forever/item=7685) · *Bloodmage Thalnos, Scarlet Monastery* |
| Ranged/relic | [Ritssyn's Wand of Bad Mojo](https://www.wowhead.com/forever/item=22408) · *Baron Rivendare, Stratholme* | [Ritssyn's Wand of Bad Mojo](https://www.wowhead.com/forever/item=22408) · *Baron Rivendare, Stratholme* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk9oI1UYn+/NJPPypWbjc93ODovMxlViZOKbl0baVUh2T8uCuggD3mzSpCa1TUInaNVLhQpFMNUgSmulKpaKIHoxFEEq7SWKaE5eBCmVqoce/APtQRCZSVIl7THNfocvL+/jze/3/b7fDA8vUQiDBgZEYRwKUIF5gEWA9wA+AmBDXpW41VHQfwpRGvbpz6FKN+qg7QdRoXtvAyr0rzfd/E4rjCrdWgft5xCqdHsdtB9DqNCD993q/hKgn/456Z5T6ZdfndOWVFToN16xdhBGhTZabn5jy33ML6ugNe9Cmb7yKCp08VOIPBhuFqPf1YAfZm+99gG8CmShWAdymF0B8uu1j0HdWIXPbtSKu7BQvE495pCGL8iVJBc8wXnC4gmT86SVtITFuTCTPJEU3AvRJNAiwT2yN4TnMaCr6ItS+u7zERV9KJsJh9WBjWcq00+XK1VDcPGwycdMMXrVmChkSs/kc0Z51sjkcvmckX3BqBbyxmy5mqkWyyXDyWdmJwpG1MnnDWemWM2buYpjdstmuxyfcsqlB/Q43ssu4x2RIAZEm0LNxnAsRP2M3JR0PypILN5hV7PZzAA4tcUI0B2bvTQAuGFxN6q6D2W65iDqFP1RP229BUzRyVWJrfWOweKmGOszh0eQszhejA1TmQWmul5wuaDC40kH74ydc0eSlVxtUB7h9x07hmn6BXH+vxa6XmrYrDQA+dqKyXTn6An27EmpeL/x2n1++zibH8RgLvUqL5Jd5Rs2s/SH8AqL9L4/PUcSx8Oq2QNmfbNDweKOu4gS+r3C7jmlq2OKDZsF9baFVPq5zaYHMFLqfmfo638/dqqBrD6jtQ30x9xJMMvkibMACx9m2YsnO7NG+gx2AYciiFS4ah7VQe/8avJvpAm/E/GyLHkxkt4GRScoRf4hAXdDmp9MX1xZduPr1OVJL35IiV2iKUYqtkmk2xLVdHd1pnH/J2eGM+blJz9MX+tspMfdu84yeH+k3VRMppvD1/93JeIwCmm4AbfgKShABeZgjvw7ADm5MyY=); Phase 1 BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk9oI1UYn+/NJPPypWbjc93ODovMxlViZOKbl0baVUh2T8uCWoQBbzZpUpPaJqETaNVLhQpFMJVohdZKVSwVQfRiKIIo7SX+QXvyImKpVD14UIT2IBSZSVIl7TGN3+HNm/fNm9/v+32/GR5eoRAGDQyIwhgUoALzAIsAbwO8D8AGvCxxs8Og/xSiNOzTZ1Glm3XQDoKo0OM6oEL/et0d39wNo0o/3wDt5xCqdHsDtB9CqNDf33GzB0uAKv1x2duo0s++uKAtqajQr5fd7FfeMwuvuWPDe88va6A170KZvvQoKnTxI4g8GG4Wo9/WgB9mR195F14GslCsAznMrgL59cYHoG6uwce3asU9WCjepB51SMOn5FqSC57gPGHxhMl5UiQty+JcmEkukoJzi3MumgR2SXCf7A/gRQzoKvqilL41G1HRh7KZcFgd2FimMvV0uVI1BBcPm3zEFMPXjfFCpvRMPmeUZ4xMLpfPGdnnjGohb8yUq5lqsVwynHxmZrxgRJ183nCmi9W8mas4ZidtttLxSadcekCP473sKt4RCWJAtCjUbAzHQtTPyG1J96OCxOJtdjWbTfeBU0uMAN2x2Qt9gBsUd6Oq+1Cm6w6iTtEf9dPdN4ApOrkusfXuNljcFCM95vAIchbHy7FBKrPAZMcLLhdUeDzp4J2xC25LspKrDcpD/L4TxzBNvyQu/ltCx0sNm5X6IF9LMZnuHD3Bnj0tFe81XqvObx5n8/1ozJVu5UWyo3zDZpb+EF5jke7vp2tL4qRZNbvPrG+3KVjccSdRQr9T2D1nVHVCsWGzoN6ykEo/sdlUH1pK3f8MffXvx840kNVjtJaB/pw7DWaZPHEeYOHDLHv+dGXWUI/BLuFABJEKV82jOujtqyb/RprwBxEvypIXQ+ltUHSCUuSYBNwFaX4ifXl1xY0vU1cnvPg+JfaIphip2BaR/peopjuzc437Pzw3nBFvfPK99I32QnrMPeysgHcj7aViMt0avPmfMxGHYUjDLRiFp6AAFZiDOfLPAFOWMuo=).

## Other builds of this spec

- [Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md) (31/17/3, 583 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-11 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

