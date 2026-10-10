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
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234439) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Dark Whisper Blade](https://www.wowhead.com/forever/item=20720) · *world drop*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Aurastone Hammer](https://www.wowhead.com/forever/item=17105) · *Garr, Molten Core*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/priest/dps/#eJzMll9oI1UUxufcmWROTpoar6udDovMxl2Jkal3JkY260PSfZBFUSsY8M0mm+kma5uETsCKL6uusAjGdR9WVhRZQVaFlfXBpfjYIqYQNSAK4h+kIvpgJbYQH/oik0kaKX2MwfN0cu65nO9++c3MpQmEKGhgQBwE8Om9X0zAccjCHDwFNTgHoP8ZQYwG9DqpuHsdtF/DpODmG0AK/rwTIQW/uwqk4sWtiPbLJKm49h5o30+SjJ+dIQV/6kYoiNsL3jYVX9uKaF8HScH1j7z9n1/z+l50SMGb7Sip2LkKWvM2UnDnMpCM24uxe/F8OdosG9fegviXDRDdwtyr78IrwM6XLwHrFt6H32ZX4capNjTKJ2l4pE+ZkRIpOynspJUUKSEsISzTy1KWl9tmssmgzcKbrBumQxTSVQrEEd9+NqZSgGQz6fIKn8/XFp+u1uqGLewHTEuY4vgJ43QpXznjFI3qspEvFp2iUXjOqJccY7laz9fL1YrhOvnl0yUj7jqO4S6V645ZrLnmYNn0l2fOutXKPTrpSMG4jK//+AhXdHZC4pdg31iRNu1Rj52hu/gRisTCFLL9gzdyFE1MYpCzhyU9SAoxS/Q9aeT482PQNGXfTqoeIBnfccn3JYjty8AvjMORozSdmEKZh84OQPAUkGLNpNw9Nrim32EfGqocUHMzxyf6f6WCL308xytjUDxAZ/3vx/kzY0DVP3XrMb50wLD0iIf9y1lLv4+O8th+Wm9N3OLRWpC8TpKT4lh/SyPHPxwHMQ/Rgzy9X4YtjvVK8rCU6pf8R6sv1meK4VcKXxqDVt/OEK7n+J364QNED+0O95tV/CTHF8fAFXqvG7y4++iBFFsjnuZT/NeKJv/OmtBh9guy1Iv7s2ug6Iyk2AdyyCtI5xay029e8WIjc2ShF99m7A7TFCOTaDLpfxX17CD7T+Pu6yOfk/6i1WpNzN/IzvYL2Xm4AHAFytXOyxtPfpNJ96pSOzPrdbZaf2Se8JMfMgkZV6dOHh5+9/3Ly6ne9aUENViBFf7PAEGfI9w=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/priest/dps/#eJzMll1oI1UUx+fcmWROTpoar6udDovMxl2Jkal3JkY260PSfZBFUSsY8M0mm9lN1jYJnYgVX1bdhUUwaiELK4ooiB9QqQ+W4pO0CClGjYiCaEEU0QfFaqE+FEQmkzRS+hiD5+nMOffO+Z8zv5m5NIYQBQ0MiIMAPrl/xQSchCzMwCNQg4sA+u8RxGhAf5xU3FsG7acwKfj3EpCC3+9ESMFvXgdScbMJ2o/jpOL6m6B9O04yfnyeFPyo6SW3mt19Kr7wW0T7MkgKbrzn3eCTJpCMzzik4GonSip+cRm01g2k4M5VL/PnXOx2vFSOtsrGW69A/LMGiN3CzPNvwHPALpWXgO0W3oafp9dg5UwHGuXTNOjpQ2akRMpOCjtpJUVKCEsIy/S8lOX5tplsMeiw8A9sN0xHKKSrFIgjvvpETKUAyWbS5RU+m6/NPVqt1Q1b2HeZljDFyVPG2VK+ct4pGtUFI18sOkWj8KRRLznGQrWer5erFcN18gtnS0bcdRzDnS/XHbNYc81+2vTTUxfcauU2nXSkYFzGl7bu44rOTkl8CQ6UFWnTHnbZKbqFH6NILEwh22+8kaNoYhyDnN0r6UFSiFmiN5NGjj81Ak0T9o2k6gGS8TWX/LkEsXMV+JVRTOQ4TSYmUOahC30QPAWkWFMpd58Nruk32UcGKvvUrOb4WO9RKvjs+zO8MgLFfXQ2/nqQPzYCVP2u2w/w+UOKpYdc7F+TtfQ76DiPHaT1+sR1Hq0FyVtJclKc6G1p5Pi7oyDmHrqbpw/KsMWJbkgehFK9kP9q9cT6TDH8XOHzI9DqjzOEGzl+s370ENGDcYd7i1X8IMfnRsAVep8bfHHv/kMptoZczaf4j0VN/oW1YJvZT8tS1+7MroOiM5Ji78ghLyBdPJedfPmaZ5uZY+e69nXG3maaYmQSLSb9r6ye7Xv/qd26PPQ66U/b7fbY7Ep2uhfIzsIVgGtQrm5f3nz4q0y6G5U6mWlvZbv9a+Yh3/kuk5BxbeL00cF/3z+9nOmeX0pQg0VY5P8MAD9bIwU=).

## Other builds of this spec

- [Smite — Raid](../research/raid/builds/smite-open-raid.md) (21/23/7, 583 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505020021302001-305151000320003-50002-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-10 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

