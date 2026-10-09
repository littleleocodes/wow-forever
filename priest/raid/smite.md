# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**[Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md)** (31/17/3) — [open the talent tree](https://talentsforever.com/priest/60/505230231305001001-30505101002-3-6)

## How to play

**Before the pull:** **Holy Fire**.

**Talents with no line below:** **Holy Nova**: a defensive or healing spell: cast it when you need it, it is not part of the damage rotation.

**Then press the first one that is ready**, top to bottom:

1. **Penance**
2. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
3. **Inner Focus**, then straight away **Devouring Plague**
4. **Holy Fire**: keep it on the target
5. **Inner Focus**, then straight away **Smite**
6. **Shadow Word: Death**
7. **Power Infusion**
8. **Smite**

**Smite** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Dark Sacrifice**: when you run low on mana (about 1 time a fight)

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Smite in a raid keeps two burns up, **Shadow Word: Pain** and **Holy Fire**, fires **Penance** whenever it is ready and casts **Smite** in every gap. **Holy Fire** counts for more than its own damage: with **Power in Light** your **Smite** and **Penance** deal 10% more while it burns.

**Why it works**

- **Holy Fire** starts 3 seconds before the pull (a 3-second cast with **Divine Fury**), so it lands as the fight begins. Recast it when its burn has about 1.5 seconds left, roughly every 12 seconds: the new one lands just after the old burn ends, and the simulator measured that 0.5% ahead of starting 3 seconds early.
- **Penance** is on top: three Holy bolts in 2 seconds on a 12-second cooldown, about a quarter of your damage, and the simulator measured 3.1% more damage with it first. The full list casts rank 3 (from the community simulator's rotation): a little less damage than rank 4 for 30% less mana, and high enough that our downranking model leaves it its full spell power.
- **Shadow Word: Pain** is about 30% of this build's damage for one global cooldown every 18 seconds. Recast it when it falls off, but not in the last 10 seconds of the fight.
- **Inner Focus** goes into **Devouring Plague** once a fight to make it free; the simulator measured about 1% more damage with that pair. Paid for, the plague costs this build about 890 mana (no **Shadowform** or **Devouring Contagion** to cut it), and the simulator measured 2.0% more damage after dropping the plain **Devouring Plague** line.
- **Shadow Word: Death** and **Power Infusion** go out on cooldown, then **Smite** fills everything else. **Mind Blast** is left out: none of your Holy talents help it and it costs more mana than **Smite**, and the simulator measured about 5% more damage casting **Smite** in its place.

**Caveats**

- **Dark Sacrifice** at the bottom of the list is not your filler, and only Undead priests have it. It turns 1,600 health into mana over 15 seconds, once every 10 minutes; the simulator casts it once a fight when it is nearly out of mana. Your filler is **Smite**.
- This build runs short of mana even in a full raid: the simulator's priest also uses two mana potions and two Demonic Runes a fight. **Meditation** keeps half your regeneration going while you cast, and the cheaper ranks the full list picks (rank 3 **Penance**, rank 3 **Shadow Word: Death**, the latter measured 0.5% better than rank 4) are part of the mana plan; neither is far enough below your level to lose spell power in our downranking model.
- The full list still holds a rank 2 **Smite** for 20-50% mana, measured before 2026-10-09; it now sits under the top-rank **Smite** and never fires. Ranks far below your level get much less from your spell power (a beta change; our model leaves rank 2 a small fraction of it), so do not downrank **Smite**.
- **Shadow Word: Death** hits you for 10% of your maximum health each time the boss survives it, about 10 times a fight: your healers pay for that.

**When to change it**

- When the boss has under 3 seconds to live, cast **Smite** (2 seconds) rather than a new **Holy Fire** (3 seconds): only a spell that finishes casting does damage.
- If healing is tight, cast **Shadow Word: Death** only in the last 20% of the boss's health, as the simulator's rotation for fighting alone does. You give up a little damage.
- When you must move, use the instants: **Shadow Word: Death**, and **Shadow Word: Pain** if it fell off. **Holy Fire**, **Smite** and **Penance** all need you to stand still.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 584 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 622 | this build |
| Phase 1 BiS | 643 | this build |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 63.0; Phase 1 BiS 65.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* | [Crystalline Threaded Cape](https://www.wowhead.com/forever/item=20697) · *world drop* |
| Chest | [Virtuous Gown](https://www.wowhead.com/forever/item=226960)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Volatile Power](https://www.wowhead.com/forever/item=19145) · *Molten Core*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Mana Igniting Cord](https://www.wowhead.com/forever/item=19136) · *Molten Core* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11648) |
| Feet | [Virtuous Slippers](https://www.wowhead.com/forever/item=226959)<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/spell=13368) | [Virtuous Slippers](https://www.wowhead.com/forever/item=226959)<br>+ [Enchant Boots - Spirit](https://www.wowhead.com/forever/spell=13368) |
| Finger | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Dark Whisper Blade](https://www.wowhead.com/forever/item=20720) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Aurastone Hammer](https://www.wowhead.com/forever/item=17105) · *Garr, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/priest/dps/#eJzMlkGIG2UUx+d9M8m8vCRr/KzudCgyTVuJkVm/mTTS1EOyPUjx4goGvJmkmW1S2yTsBFzxsmqFIhhLD5WKRSroqrCyHlwWj7uIWYgaEAVRRFZEDy7EXVgPXmQyyUbidQ2+05v/93283/fe+3hDEYQYaGBAAgTwEwdfTMAZyMEcPA0FqEADlgCuAVwH0N+LIMYCepNU/GsFtF/CpOD2G0AK/rQXJQW/uwOk4vWdqPbzFKm48S5o30+RjJ9dJAV/3I9SEHfnvWMqvr4T1b4OkoK3d2Ok4OfL3r6XHFJwrRsjFXt3QGvfQwru3QSScfdy/CG8Wo21q8byW5D4sgVivzT32jvwKrCr1RvA9kvvw6+z67B6vgut6jkaXe5TZqRF2k4JO2WlRFoISwjL9Ly05fm2mWoz6LLwNvuI6AiFdJUCCcTbz8VVCpBsplyu6OysxG8ALxQbl5+pN5qGLexHTJEx7TNnjQuVYu2iUzbqC0axXHbKRul5o1lxjIV6s9is1muG6xQXLlSMhOs4hnul2nTMcsM1h8umvzxzya3XHtRn6AQ/TtF4mEK2D9LKUyw5hUHOHpf0ICnELDFgbOX5CxNgmrbvJVUPkIxvu0Q6UjARxO5N4NcmkZGTdDQ5jTIPXRoWxiMgxZpJuwe14pp+n31kRDms4lqeR3QfWcGXP57jtQkQ+/Fk3PzzCb40niJLmMI+5IDH6O7kXV6HlCTv3iSfFqdGCbD0h+kkj4831diR1MGRVp5/OInCPkaP8sw4hi1O9SV5JKUHkv8CBrB+6Rl+pfArE2D1+ymEm3l+/7/Tbf8z3ZPD6d8+PPhQ8ZM8f3Ysttds1iHH9t/YH4ua/BtrQ4/ZL8pS307nNkDRGUnxD+SQJ0hL87mjb97ybCt7fL5v32btHtNUI5tsM+l/Zc3c0PtP7YGVQ4+T+aLT6UQKq7nZgZAreCP7FlTrvVe2nvomm+mrUjc76+3sdH7PPuk7P2STMq5Pnzs2mpf++D/f/wGoQAMWYZH/PQDpH944); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/priest/dps/#eJzMlkFoI2UUx+d9M8m8vKQ1fq52dlhkNrsrMTL1m8lGNush6R5k8WIFA95MspndZN1NQidixUvVXVgEoxSyULGIglSFSj1YiidpEVKMGhEFUUEU0YNCbaEeBJHJJI3Eaw37Tu/7v/l4v++99/ENRRCioIEBcRDATxysmIAzkIVZeBzyUIY6LADcAHgFQF+JIEYD+lOk4l+roP0cJgX/XgRS8Ie9CVLwmzeAVNxugfbTJKm4+RZo306SjB9fIgU/annB71u9fSq+/PuE9mWQFFzejZKCn7SAZHzeIQXXu1FS8YvroLXvIAX3bnqR3Sux+/BaJdquGCuvQfyzJoj94uxLb8KLwK5VFoHtF9+GX2Y2YO18F5qVczQ83YfMSImUnRR20kqKlBCWEJbpeSnL820z2WbQZeEf2XtERyikqxSIIy4/HVMpQLKZdLmis7MSXwSeL9SvPFGrNwxb2A+YIm3aZ84aF8qF6iWnZNTmjEKp5JSM4jNGo+wYc7VGoVGpVQ3XKcxdKBtx13EM92ql4ZilumsOwqYfnr7s1qr36tN0gh+niViYQrYP0sxRNDGJQc4elvQgKcQs0Wds5vizY2Casu8kVQ+QjK+7RDpSMB7E7k3gN8ZRkZN0NDGFMg9dHjTGIyDFmk65B73imn6XfWRIOejieo5HdB9ZwRfen+XVMRD7+WTc+vMRvjBaIkuYwj7khMfo9sRt3oQUJe/cJJ8Wp4YFsPT76SSPjQ7VyJbkwZZmjr87jsY+RA/y9CiGLU71JHkopfqSfwP6sH7rGX6u8KtjYPXnKYRbOX73f8tt/7vc48PpnT7cX6j4QY4/OZLbGzbrkHP7d+yPeU3+lbVhh9nPyVLPTmc3QdEZSbF35JAnSAsXs0dfXfJsO3P8Ys++ztg7TFONTKLNpFvKGtmB97/aPauHnif9aafTieTXsjN9IZv33uwlqNR2rm8/9lUm3VOlbmbG+7LT+S3zqO98l0nIuDF17tjwvfTf//O9P4Ay1GEe5vk/AwCQid1h).

## Other builds of this spec

- [Smite — Raid](../research/raid/builds/smite-open-raid.md) (21/23/7, 583 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505020021302001-305151000320003-50002-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

