# Fire Mage — Raid (group)

[Mage](../README.md) > [Raid (group)](README.md) > Fire

**✅ Recommended** for raid (the best mage spec here, or within 3% of it).

**[Fire — Raid](../research/raid/builds/fire-open-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/mage/60/2032052001002-54500001230133031-003-7)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Fire — Ignite / Heating Up), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Pyroblast**.

**Then press the first one that is ready**, top to bottom:

1. **Pyroblast** when Heating Up has 3 stacks
2. **Fire Blast**
3. **Scorch** when either the target has fewer than 5 stacks of Fire Vulnerability or Fire Vulnerability has under 5 seconds left and the target has fewer than 4 stacks of Fire Vulnerability
4. **Arcane Blast**: keep it on the target
5. **Arcane Missiles** (rank 7) when Missile Barrage is active
6. **Fireball** (rank 11)

**Fireball** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Combustion**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- **Evocation**: when you run out of mana (needed in about 3 of 10 fights)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Fire keeps its own **Improved Scorch** debuff at 5 stacks, fires **Fire Blast** on cooldown and casts **Fireball** in between. Crits build **Heating Up**; at 3 stacks **Pyroblast** becomes a 1.5-second cast.

**Why it works**

- **Fire Blast** first whenever it is ready: every 6 seconds with **Improved Fire Blast**, instant, and **Incineration** and **Critical Mass** make it crit often, feeding **Heating Up** and **Ignite**. The simulator measured using it on cooldown, with no mana saving, 3.7% better than the rule it replaced.
- **Scorch** keeps Fire Vulnerability at 5 stacks. In Forever **Improved Scorch** is your own debuff: +3% to your Fire damage per stack, for 30 seconds. Build 5 stacks, then refresh it once 7.5 seconds or less are left so a long cast cannot let it drop; the list shows only the stack count, but the early refresh is part of the rule (the simulator measured 7.5 seconds 0.4% better than 5).
- **Pyroblast** waits for 3 stacks of **Heating Up**. Each crit from **Fireball**, **Fire Blast** or **Scorch** takes 25% off your next **Pyroblast**'s 6-second cast, so 3 stacks make it 1.5 seconds: your biggest hit for its cast time. The list's 2-stack line is a last-chance rule: cast a 3-second **Pyroblast** at 2 stacks only if **Heating Up** has under 3.5 seconds left or the boss dies within 6 seconds.
- **Fireball** fills everything else: 3 seconds with **Improved Fireball**, about half your damage, and each crit also starts **Ignite**. The list stops starting it with under 3 seconds left, when it would land too late.
- **Combustion** at the pull and whenever it is back (3 minutes): each Fire hit adds 10% crit until you land 3 crits, which fills **Heating Up** fast. It shares its cooldown with **Presence of Mind** (client data), so a build with both gets only one of the two every 3 minutes.

**Caveats**

- Mana: Fire runs short even in a full raid. The simulator uses your mana gem (from **Conjure Mana Ruby**) at 80% mana and a mana potion whenever it is ready, and still runs dry now and then; **Master of Elements** refunds 30% of a spell's base cost on each crit.
- The raid list has no **Evocation**: in a 3-minute fight with raid buffs the simulator measured it slightly better without (0.2%). In a longer fight or without mana buffs, channel it when nearly empty with plenty of fight left; the simulator's list for playing without raid buffs does so below 10% mana with more than 25 seconds to go.
- Several targets: the simulator's own Fire list adds **Blast Wave** and **Flamestrike** at 3 or more targets; this build has no **Blast Wave**, so use **Flamestrike**.
- The simulator's boss resists nothing. Against an enemy that resists or ignores Fire, every spell here loses damage, and **Frostbolt** is your fallback.

**When to change it**

- In the last 3 seconds a **Fireball** would land too late: cast **Scorch**. The simulator's list uses Rank 1 there, the same line it falls back on when you cannot afford a **Fireball**; Forever gives ranks that low only part of your spell power and fewer talent procs, so use your top **Scorch** whenever you have the 150 mana.
- With 2 stacks of **Heating Up** and the boss dying within 6 seconds, cast **Pyroblast** now: the third crit may never come.

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 828 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 54ceac6 (client 70707); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 885 | [17/31/3](https://talentsforever.com/mage/60/2032052001002-55500001230123031-003-7) |
| Phase 1 BiS | 903 | this build |

**The gear** (average item level: Pre-BiS 66.1; Phase 1 BiS 67.0; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Field Marshal's Coronet](https://www.wowhead.com/forever/item=16441)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Field Marshal's Silk Spaulders](https://www.wowhead.com/forever/item=16444) | [Field Marshal's Silk Spaulders](https://www.wowhead.com/forever/item=16444) |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Earthweave Cloak](https://www.wowhead.com/forever/item=21187) |
| Chest | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Archmage](https://www.wowhead.com/forever/item=14152) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Marshal's Silk Leggings](https://www.wowhead.com/forever/item=16442)<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Marshal's Silk Footwraps](https://www.wowhead.com/forever/item=16437)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Grand Marshal's Mageblade](https://www.wowhead.com/forever/item=23451)<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkl09sG8UXx/1mt/H4uX/caX/tdn85TFNKEidO1uu4SiJE3EpAoEWuOCEOkLV3HW/Zei3vpmpvocoBIZFAqUBNogpFVIFKgBQE1BEVUriYA1WFVCqVQ6JABAcOTZAicUFo1k6bA+qt4uAneXZ2nr/v2Z+debODrRRioACHDhiBIpRhHOBNgA8BPgZgOwMvEd5+UGcOURqj6jkM0+o4KGtRlOnqB4Ay/WZctLfeAWyhtZLyy24M06VroPy8GyW6VEKZrk0BhuliXRamX46DMhVGmd67JpSTf8RQpl/dFu2738YwTGe+BqW2D2X65/viC5/M7mnritXsjluToG3mTr89B28BmbAvAdnMTQP57fh1CM/Pwlpy0l6BCfsEDX45ZGCRHNG1lK6ldU1LapqeSKfTmqZpST0VfFLJhKalagRuk+gquXoQn0CqtqBM/7oEbcoC+R+VWGSaNEaEB0kiyV5nI0bZec0t+1zX9GOJZDKhJQd5vmiURi2TuxVumKZl8twF7hctXnF9w7fdEvcso5Iv8g7PsnjBrliJimGbiS13ou7uOeO5pU41rO5AKTZhs6uEbUI9jZZIJQeDkG6hYOdtw+GefXbMMXy30u7xs8ao1WuWvV6j7Hi9pmWVn7UrVo9RdoKY3PB5ui9vGfljqX5umG7Zt0ze8SC9Y4xyY8y0fW4UfKsS5KlYibJdGuRdek//UV5w66NWya9caPd4zvJ8nhuzHZPbJW7wwpjjcPGfuhsC3+VdfT3putL2Pe7YnkgaaLxuntS6NU3jBXu06Hs8IGSZHte5UTJ5qlM9gvvie6nEyCshNbIhNZ7DKkQx8sw5Nx9QZZ81MaAUdrJ2PBDfT4FFlkAAWq8qYuogpHBXWxQjG7Bt+ooru9jEwIJlRe9m2f0mhjCGDjuDg2o/qnGFSmzXEiDK9PMvgJEYEYQQ0lu+xX/zdavxR2j7cGcbIt0AwXo5K0R0Octmmhg5x9a4SoHtWYKdD3Ep0AA6GGLfNTGdYXyaPYVdaidG77VQlOnNqqJAY4ZFFoMKdrOqqI29+PKdk9tr2+U7J9XGlU01McX9GF0AQe8HQU/MLPprls02MZHDqMQP0BZGrwel6G5WpdNE9ObrRWk+2+SbodgMl7OKFJ+D7a9Uz6vPYStT64tsIVh+i7UXMfKjLLrV9VN6e+NFubp+Cv9/ERSU6Huvqnvje2gLI7mQGsYdKA0MHGUvqMPBwg5CPdDXI8/B1u3DJI+I9TupwX2ivyGFAuvLBHokFNr+JhExFBovZA5NXxH2/dDhQmA/DekrRJH5UPwGCf0n5me2eo/Vnvz0seUZCNqXPsocbwxkRsRB8QoEN6GVobhEbxw8se08qUE/ZGAYTsPLUIQynIfz5J8BAL+wyGY=); Phase 1 BiS: [full raid](https://wowsims.com/forever/mage/dps/#eJzkl0FsG0UXx/3Gbjx+bht32q/d7pfDNKUkceJkvI6rJELErQQEWuSKE+IAWXvX8Zat1/JuqvYWqhwQEo2UFqQmUYUiqkAlQAoC6ohe0osRAlVIpRIcEhUiODZBisSlQrN20hxQbxUHv8Ps7Hv6v2f/dubNLrZRiIECHDphFIpQhgmAdwE+AvgEgO32o0RGB0CdPUxpjKrnMUyrE6CsRTFEH00Dhui3E3K8cwOwhdZKym97MUyXb4Dy614M0uUShujaFGCYLtVlYfrVBChTYQzR7z+A7XHyihy/vhvDMJ39BpTafgzRvz6Uzk/nWtu7YzWr88fLIDZzZ96fh/eATFrTQDZzM0D+OHETwgtzsJa8bK3CpHWS+r8cMrBEjmoipYm0JkRSCC2R7k8LIURSS4lkKiVSyYQQqRqBuyT6gFw/hM8gVVswRP+ehnZlkfyPBllkhjQ8MoIkkWRvs1G9bL/llD2uCe14IplMiOQQzxf10phpcKfCdcMwDZ67yL2iySuOp3uWU+KuqVfyRd7pmiYvWBUzUdEtI7EVTtTDvWddp9SlhtVdGIxNWuw6YZtQLyMSqeSQn9IpFKy8pdvctc6N27rnVDpcfk4fM/uMstunl223zzDN8otWxezVy7afk+seT/fnTT1/PDXAdcMpe6bBO7fL2/oY18cNy+N6wTMrfp2KmShbpSHerfUOHOMFp+41S17lYofLc6br8dy4ZRvcKnGdF8Ztm8v/1NMQeA7v7u9N15WW53LbcmVRX+P28KToEULwgjVW9FzuEzINl2tcLxk81aUexf3xfTTIyBsBNbIRbDyHBxDFyAvnnbxPlX3exIBS2MU68GD8AAUWWQYJaL2qyKWDkMI97VGMbMCO5Suv7FITA/O3Fb2fZQ+bGMI42uwsDqkDqMYVGmR7lgExRL/4EhiJEUkIIb0VW/q3WI8af4K2H3e3I9INkKxXslJEV7JstomRc2yLqxRY6zLsfoxLgQbQoQC708R0RvB59hx2q10Y/aWFYojerioKNFZYZMnvYLerito4i6/eO7Wzt129d0ptXNlUE1M8gNFFkPR+kPTkyqK/Z9lcExM5gkr8IG1h9Kbfiu5nVTpD5Gyh3pQWsk1+GMrDcCWrBOPzsPOV6mX1JWxjan2TLfrbb6n2KkZ+Cslpdf201tF4Ua6un8b/XwIFg/TKm+q+eCttYSQXUMO4C4ODg8fYK+qIv7H9VNv6euZ52Lp9XOQJuf4kNXhItHeCAd/6M74eCYX2RyQiXYGJQubwzDVp3w0fKfj287C2SpQQH47fIoH/xLzM1uyp2rOfPbU6g/742seZEw1HZlR+KF4D/yawOhwP0luHTu74nhQwABkYgTPwOhShDBfgAvlnAMBDx/c=).

## Other builds of this spec

- [Fire — Ignite / Heating Up](../research/raid/builds/fire-raid.md) (16/32/3, 798 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000001-35500201230133031-003-7)
- [Fire (optimized)](../research/raid/builds/opt-fire-raid-raid-dps.md) (18/31/2, 795 DPS in a full raid) — [open the talent tree](https://talentsforever.com/mage/60/0502152000003-35500101230133031-002-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-02 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70707; raid numbers: the official wowsims/forever simulator at 54ceac6 (client 1.60.1.70707)). Simulations, not in-game measurements. Do not hand-edit.*

