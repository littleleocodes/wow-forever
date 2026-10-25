# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

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
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Wizardweave Robe](https://www.wowhead.com/forever/item=14128) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) | [Sandworm Skin Gloves](https://www.wowhead.com/forever/item=20716) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) | [Earthen Silk Slippers](https://www.wowhead.com/forever/item=254013) · *Tailoring*<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/item=16220) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21207) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Dark Whisper Blade](https://www.wowhead.com/forever/item=20720) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Aurastone Hammer](https://www.wowhead.com/forever/item=17105) · *Garr, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Ritssyn's Wand of Bad Mojo](https://www.wowhead.com/forever/item=22408) · *Baron Rivendare, Stratholme* | [Ritssyn's Wand of Bad Mojo](https://www.wowhead.com/forever/item=22408) · *Baron Rivendare, Stratholme* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/priest/dps/#eJzMll+IG1UUxufcmUxOTrIxXmt3digyjV2JkVnvTBpp6kOyfZCiqCsY8EFwk2bWpHaTsBNw1ZeqFRbBoPtQqSiyQqkK1fXBUnxsH0whakBUxD9IRfShYGxh+9AXmcykkXUfY/C85Obcc/m+c+Y3w6UYQgI0MCAFAvjMzX9MwAEowAI8AU04DqD/GUdMhPQWhfHGWdB+i5KCl98EUvCXa1Ok4PcbQCpu1rVf4xTGC6dB+yFOCl7Z8Ep+3poiFa8uecdU/OhJ7WuVFPz8jFfx3WkgGV9ySMFzvQSFsb8BWuc2UvDaSe/s2seQvAdP1BKdmnHmbUh92QaxVV547T14FdiJ2jqwrfL78Pv8edg83IN27RCNWvqMzWZFVmSEsK2MsISwzIzIWllvZdmWEBkzK4SwOwx6LHqZXY3RLoroYQqlEN95NhmmEMlmxuV1vlhqHnuq0WwZtrDvMy1higMHjSPVUv1pp2I0VoxSpeJUjPJzRqvqGCuNVqlVa9QN1ymtHKkaKddxDHe51nLMStM1h9umvz131G3U79ZJR1JTMr7x00Nc0dlBia/DNlmRM+1xy87RnXwvTSWjFLH9xttFSqTjqHL2oKSrpBCzRDCTdpG/MAFP0/btFNZDJOO7LvlzUbF3EvjaJCayj2bS0yjzyNEhCJ4DUqy5rHuTDa7pu+1dI5dDas4VeSx4lAq+/MkCr0/A8RCdi9cf5c9MAFW/6+4jfHkHsdyYxf4xWUu/l/bx5HZab03f4tFalrxKkjNiNjjSLvIPJ0HMA3Q/z223YYvZQUoepbJByn+1ArM+Uwy/UvjyBLz644zgxSK/Q9+zg+nRuKNBcRg/LfJjE+AKvc8Nvn7j4R0ptsas5lP81yp//t9i1v4xi+2mWJIIba/B6+ugB7+a/AfrQJ/ZL8rSIPYXLoCiM5KSH8gRLyEdXyrMvHXKi0v5vUuD+DZv95mmGPl0h0n/q2gVhqv/NO46O3ad3Bfdbje2uFmYDxKFRVgDOAW1Rv+VS49/k88NslIvP+9VdrtX8o/5ix/zaRnPTx/aM7p4+Lenw4P7UxWasAqr/O8BAFukSoQ=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/priest/dps/#eJzMVkGIG2UUnvfPbOblJU3jb+3ODkWmsSsxMus/k0aaeki2BymKuoIBb27STE1qNwk7ga56qdrCIhg0kEJFkQpSFYr1YCmCUNqDWYwaEQXRgiiihx7WFtpDQWQyk42se4zBd8mf997P971vvhkeRRHioIEBSRDAZzb+MQH7IA8L8DQ04DiAfj2GGJ/Sj5GKt8+B9luEFPyrDaTgzze2kYI/nAFSca0D2q8xUvHye6D9GCMFr53xei51vOrVzuCiip9d2q59GyIFv+h41c/PxkjGlx1S8EI/Tip+cxK07p2k4I1TXn31I0jcjyeq8W7VOPsWJL9qgbhZWnjtXXgV2IlqG9jN0vvw+/xFOH+wD63qARpN9SmbzYiMSAthW2lhCWGZaZGxMt7Jsi0h0mZGCGF3GfRZ5Bd2PUo7KKyrNJVEfPtYQqUpks20y2t8sdg4+ky90TRsYT9oWsIU+/YbhyrF2rNO2agvG8Vy2SkbpeeNZsUxluvNYrNarxmuU1w+VDGSruMY7lK16ZjlhmsOy6Zfnjvi1mv36aQjhZIyvnH1Ua7obL/E27AJVmRNe9ywc3QP303bEhEK2/7grQLFUzEMcfaIpIdIIWaJQJNWgb84AU7T9l2k6lMk4zsu+bqEsH8K+OokFNlDM6lplHn4yNAIHgNSrLmMu+ENruk77R0jlkPXXCjwaPAoFXzl4wVemwDjoXWu3HqCPzcBq/pT9x7nS1uAZccM9g9lLf0B2sMTm916R2q759aS5HWSnBazwZVWgX84Ccc8TA/x7GYatpgdpORRKhOk/FcrIOt7iuHXCl+aAFdfzjBeKfC79V1bkB7JHQmaVfykwI9OwFfofW7w9duPbelia8xovov/XOEv/BvM2jtmsJ0UTRCh7Q14qw168KvJf7AurDP7JVkaxN78ZVB0RlLiAznsJaTjh/Mzb572Yi23+/Agvs/Z60xTjFyqy6T/VTTzw9N/GveeGztO9sterxddPJ+fDxL5RVgFOA3V+vrJtae+y2UHWamfm/c6e71ruSf9w0+5lIwXpw/sGi0e/gJ1cLBCVaABK7DC/x4Ap+FKoA==).

## Other builds of this spec

- [Smite — Raid](../research/raid/builds/smite-open-raid.md) (21/23/7, 597 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505031021030001-305151000221003-50002-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

