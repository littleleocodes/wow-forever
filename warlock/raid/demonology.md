# Demonology Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Demonology

**✅ Recommended** for raid (the best warlock spec here, or within 3% of it).

**[Demonology — Raid](../research/raid/builds/demonology-ml-raid.md)** (2/31/18) — [open the talent tree](https://talentsforever.com/warlock/60/011-0025003031220301351-0550005003-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds). A model of the beta, to check at launch.

## How to play

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage), then summon your Succubus: Demonic Pact keeps the Imp's buff while another demon is out; **Soul Link**: turn it on with your demon out (it lasts while the demon lives).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Demonology in a raid is a **Shadow Bolt** caster with two demons' worth of bonuses: you sacrifice the Imp for 15% more Shadow damage, and **Demonic Pact** keeps that buff while your Succubus fights. Then you keep **Curse of the Elements** and your dots up and cast **Shadow Bolt**.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours), then summon the Succubus and turn on **Soul Link**. **Demonic Pact** keeps the sacrifice while a different demon is out, but summoning the Imp again cancels it; the simulator measured about 10% less damage without the sacrifice.
- The Succubus earns her place: while she is out, **Master Demonologist** gives you and her 10% more Shadow damage, **Soul Link** 3% more damage and **Demonic Knowledge** 60 more spell damage at level 60. She takes 17% of your spell damage as attack power and 10% as spell damage, and her attacks and **Lash of Pain** add about 9% of your damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school for 5 minutes, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana: every tap is a global cooldown with no damage, and the simulator measured tapping at 5% about 0.5% better than at 10%.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (a 1.6-second cast with this build's single point of **Improved Corruption**) goes back up when less time is left on it than its cast, but not in the last 10 seconds.
- **Immolate** is Fire, so none of your Shadow bonuses reach it, and it only just pays: the simulator measured this spec better without it when it was recast to the very end, and better with it when you stop 20 seconds before the end. Start it when less than its 1.5-second cast is left on the old one.
- **Shadow Bolt** is the filler because every bonus you stacked is Shadow: the sacrificed Imp, **Master Demonologist** and **Improved Shadow Bolt**'s 20% after your own crits. **Decimation** adds 6% to it once the boss is below 35% health.

**Caveats**

- **Searing Pain** has no cooldown: the rotation casts it only in the last 3.5 seconds, when its 1.5-second cast lands before the boss dies and a **Shadow Bolt** might not. So **Demonic Brand** and the **Soul Fire** half of **Decimation** do nothing here: they are points on the way to deeper talents, and the simulator found **Soul Fire** a loss wherever it tried it.
- If the Succubus dies, summon her again unless the boss is about to die (6 seconds with **Master Summoner**) and turn **Soul Link** back on: without a demon you lose **Master Demonologist**, **Soul Link**, **Demonic Knowledge** and her own damage. Never summon the Imp during the fight: that cancels your sacrifice even with **Demonic Pact**.
- Summon her after your buffs, wizard oil and Spellstone (**Create Spellstone**) are on: in this project's model a demon copies its share of your spell damage when it is summoned. Forever lets the Spellstone stack with the oil, and the simulator measured about 3% more damage from it.
- On the move, **Bane of Agony**, **Curse of the Elements** and **Life Tap** are instant; **Corruption** keeps a 1.6-second cast in this build, so put it back when you stand still.

**When to change it**

- In the last 20 seconds start no new **Immolate**, and in the last 10 no **Corruption**: cast **Shadow Bolt**, then **Searing Pain** in the last 3.5 seconds.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 870 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 838 | this build |
| Phase 1 BiS | 869 | this build |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 63.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9II3cUx/N+M8n88rQ6/kpxnLYwDShpYOQ3E8YaLxk9SelBeip4qImJJsFmQpKD3iwKLaVV+ocWo2BpldZSi/SwyF7WFYR4WTztYUVWXGSXZWGXXfC4LDMZcVn3sJes7/Dyzfe9N+/zmzn88AMKMiigQRTGIAclmAX4FuB3gL8BWKtXJW61H9S1MBXksFrFEF0tKqctKNKT3wBF+vAXNy8fyBii+0XlXhtKdHcdlMM2FOhuEUV6uggYojvelES3/gVlUUKR3ll3BxceySjSawdu/vGGjBJ9/B8o9XdRpM9+dRs2VtojplzPR28tAD9Lj/zwB3wHZD7/E5CzdA2C9wdX1+EfkP5aga3hhfwW/Fk4hvn8UOvF4Wy4TiLcMHTOTYvzOI8bpsnj3Ihbhs4ti3Pu2nUiHJCWE7IssQ/V97Ej0o7v/A+IIt35ZoQROaiGfG2qHKOsBzti7TTEyKcBVcIgCoZV8SyRkbRvfWJ1qyISRWFx1XjDmT7erQZRkM/STFTJQKBB03ju+Vi81/Jo5r4HNgdsIlWa+tIpVTWTm306T+hm/4A2nksVJ7MZzSlrqUwmm9HSM1o1l9XKTjVVzTtFrZJNlcdzWrSSzWqZ7FdO0ZlyJmf0ciqf0c+b9EZTb6HiFD9Wu1COtVHBO18IRSSWh0o3RllE1bAz9h4VmVRwrZujKq0RXzV+2NqrpAbXudkU0gHkrBe7Yp1UZLTgvqq7e6CGa8SXl74Dr6h+6Woxjy4wjy5jmj7m0R6w8msoE02hpO5Oef7nt76Tbj79jKGvD/dAER6QOjwh5tdCwIuEXSOIFENU0IgNkeck7NqB2Qm7q7bkxn7yowkvbifNY6KIWjK2TQJXElX7XDU1ejabtifh5c/X7EHfsMfcG2MJvD+B42RMoNudQy9dLBz6wYZhGIEvIAclmIZp8mIA/GhQiA==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElUFII2cUx/O+mWS+PK2OXymO0xamASUNjHwzYazxktGTlB6kp4KHmphoEmwmJCnozWKgpbQKWgtGwdIqraUW6aFIT60gRArFUy8SKi3S0ssuu+BRlpmM67LuYS9Z3+Hln/97b97vmzl8+BoFGRTQIApTkIMSLAJ8AvAVwHcArNOrErc6DOpumApyWP0QQ3S7qFx0oEivVgFF+v8Xbt48lTFET4rKP10o0aNdUM66UKBHRRTpxQqgRJvr4I5J9OAHUFYkFOnv6/A4/3wqo0hra27nvR9BabyMIn34pVva2+qOmHIjH/1jGfhleuLzr+FTILX8KpDLdB2C/45u78L3IH27BQfjy/kD+KZwDrX8WOfN6Wz4hUS4YeicmxbncR43TJPHuRG3DJ1bFufctRtEOCUdf5NNib2uvoo9kW586SdAFOmvH08wIgfVkK9NlWOUDWBPrJuGGHk7oEoYRMGwKp4lMpL2rbesflVEoigsrhrPOTPE+9UgCvJlmokqGQm0aFrPvR6LD1oezdJnwJaAzaRKc+87papmcnNI5wndHB7RpnOp4mw2ozllLZXJZDNaekGr5rJa2ammqnmnqFWyqfJ0TotWslktk/3AKTpzzuyCXk7lM/p1k95qGixUnOKbah/KsS4qeOcLoYjE8lDp3iSLqBr2xl6hIpMKrvXbpErrxFetH7bzNKnBdW62hXQEORvEvlgvFRktuK/qr2NQw3Xiy1vfgVdUv3S3mM0bzOZtTNPHbB4DKz+DMtEWSurulGtrL3wn3X/wDkNfnx2DIvxHGnCfmB8JAS8Sdp0gUgxRQSM2RK5I2LUDizN2X33DjZPkGzNe/Jk0z4kiasnYIQncSVTta9XWGNhv256El9/dsUd9w55yr4wN8P4EzpMxgR72jj1xs3AYBhvGYQLegxyUYB7myaMBAP/VUFc=).

## Other builds of this spec

- [Demonology — Demonic Pact](../research/raid/builds/demonology-pact-raid.md) (2/31/18, 865 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/101-0035003021220301351-0550005003-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

