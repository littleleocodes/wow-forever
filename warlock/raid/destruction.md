# Destruction Warlock — Raid (group)

[Warlock](../README.md) > [Raid (group)](README.md) > Destruction

**[Destruction — Raid](../research/raid/builds/destruction-ml-raid.md)** (10/11/30) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055020510310035-7)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Destruction — Incinerate), which stays below as the alternative. A model of the beta, to check at launch.

**Other setups of this spec.** This build is the Shadow Bolt setup. The spec's best build for each other setup, in a full raid:

- Fire: [Destruction (optimized, fire)](../research/raid/builds/opt-fire-destro-raid-raid-dps.md) (10/11/30, 685 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055030510310025-7)
- Incinerate: [Destruction — Incinerate](../research/raid/builds/destruction-incinerate-raid.md) (9/11/31, 665 DPS in a full raid) — [open the talent tree](https://talentsforever.com/warlock/60/153-0050203001-0050245103101351-7)

## How to play

**Before the pull:** **Life Tap**.

**Talents with no line below:** **Demonic Sacrifice**: before the pull, summon your Imp and sacrifice it (+15% Shadow damage for 2 hours; summoning any demon cancels it).

**Then press the first one that is ready**, top to bottom:

1. **Curse of the Elements**: keep it on the target
2. **Life Tap** when your mana is below 5%
3. **Bane of Agony**: keep it on the target
4. **Corruption**: keep it on the target, until the last 10 seconds of the fight
5. **Immolate**: keep it on the target, until the last 20 seconds of the fight
6. **Conflagrate**
7. **Shadow Bolt**

**Shadow Bolt** is your filler: cast it whenever nothing above is ready.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Shadowburn**: in the last 1.5 seconds of the fight, when there is no time left for another **Shadow Bolt**
- **Searing Pain**: in the last 3.5 seconds of the fight, when there is no time left for another **Shadow Bolt**

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Destruction in a raid is still a **Shadow Bolt** spec: you sacrifice the Imp for 15% more Shadow damage, keep **Immolate** on the boss so **Conflagrate** can go out every 10 seconds, and let **Shadow and Flame** turn each **Conflagrate** into 10% more Shadow damage.

**Why it works**

- Before the pull: summon the Imp, use **Demonic Sacrifice** (+15% Shadow damage for 2 hours; summoning any demon ends it), then **Life Tap** once so you start full. Put a Spellstone (**Create Spellstone**) on your weapon on top of your wizard oil: Forever lets them stack, and the simulator measured about 3% more damage. This build has no **Amplify Curse**; without the sacrifice the simulator measured about 10% less damage.
- **Curse of the Elements** goes up first: 10% more damage from every magic school, Fire and Shadow alike, and as a Curse it sits beside your **Bane of Agony**. **Life Tap** waits until you are below 5% mana (the simulator measured that 0.4% better than 10%), and **Improved Life Tap** adds 20% to each tap.
- **Bane of Agony** grows over its 24 seconds, so recast it only once it has run out. **Corruption** (0.8 seconds with 3 points in **Improved Corruption**) goes back up when it is about to run out, but not in the last 10 seconds.
- **Immolate** matters as much for **Conflagrate**, which needs it on the target, as for its own damage: start a new one when less than its cast (1.5 seconds with the **Bane** talent) is left on the old one, but not in the last 20 seconds. Both end-of-fight cut-offs measured small gains.
- **Conflagrate** goes out whenever it is ready. With 5 points in **Shadow and Flame** it no longer eats your **Immolate**, and each hit gives you 10% more Shadow damage for 20 seconds, twice its cooldown; **Fire and Brimstone** and **Ruin** make its crits frequent and big. The simulator measured adding it at about 8% more damage.
- **Shadow Bolt** is the filler, not **Incinerate**: the sacrificed Imp, **Improved Shadow Bolt** and **Shadow and Flame** raise Shadow damage only. Even the Incinerate build's own rotation search put **Shadow Bolt** ahead of **Incinerate** in a raid.

**Caveats**

- The last seconds belong to quick spells: with 3.5 seconds left the rotation casts **Searing Pain** (a 1.5-second cast) and with 1.5 left an instant **Shadowburn**, because a **Shadow Bolt** still casting when the boss dies does nothing. Neither belongs earlier in the fight.
- **Shadowburn** on cooldown measured worse in the fire rotation (about 0.8%): it costs nearly as much mana as **Shadow Bolt** for about two thirds of the damage. Keep it for the last global cooldown, or for a moment when you must move.
- With the Imp sacrificed you play without a demon: any summon ends the buff, so if you die, summon the Imp and sacrifice it again before the next pull.
- On the move, **Bane of Agony**, **Curse of the Elements**, **Conflagrate**, **Shadowburn** and **Life Tap** are instant; **Corruption** still has a 0.8-second cast in this build.

**When to change it**

- If you play the Incinerate build listed above instead, it still fills with **Shadow Bolt** in a raid: its full-raid rotation adds **Shadowburn** on cooldown (with 10 or more seconds left) and keeps **Shadow Bolt** ahead of **Incinerate**.
- A boss needs only one **Curse of the Elements** (in Classic two never stacked): if another warlock keeps it up, take the curse your raid gives you, such as **Curse of Recklessness** for the physical fighters.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 705 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 683 | [9/11/31](https://talentsforever.com/warlock/60/252-0050203001-055030510310035-7) |
| Phase 1 BiS | 722 | [9/11/31](https://talentsforever.com/warlock/60/252-0050203001-055030510310035-7) (ties this build) |

**The gear** (average item level: Pre-BiS 62.4; Phase 1 BiS 64.2; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Felcloth Hood](https://www.wowhead.com/forever/item=14111) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Red Mageweave Headband](https://www.wowhead.com/forever/item=10033) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) |
| Chest | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of the Void](https://www.wowhead.com/forever/item=14153) · *Tailoring*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* | [Gloves of Spell Mastery](https://www.wowhead.com/forever/item=14146) · *Tailoring* |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ghostweave Pants](https://www.wowhead.com/forever/item=14144) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Finger | [Brilliant Watcher's Signet](https://www.wowhead.com/forever/item=275982) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageblade](https://www.wowhead.com/forever/item=22383) · *Blacksmithing*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) | [Therazane's Touch](https://www.wowhead.com/forever/item=19315) |
| Ranged/relic | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* | [Brilliant Wand](https://www.wowhead.com/forever/item=249385) · *Enchanting* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU9oK1UUxnPu3GRuznu28+5TOh3/MAb6iIEJdyaMTbrJvK6Kq+JKKGiTJjUJkoRMFhU3FQuKaIpGlMZCRS1aqVJcaHFjLRTSjXTlwlIslaKIYEHpUmQm01baLlykeBY3J+ebM/f3zblw8REGCqigQxymoQR1mAd4DeADgE8B+G1fJZ6aBm0dmaREtSZG2EpVPb6FlB29B0jZb+946/t7CkbYblX9eQBltr0K6v4ASmy7ipQdLwJG2JbfJbONdVAXZaTsx1WvsfW7gpR9teetb32roMz++ALU7l2k7M93vQfWlgdjltItx79vgTjNT775IbwOZKH8NpDTfAfCv9xfWYXPQP5kGTYmWuUN+KhyCAvl8dsX5hz4hjxm2ZYhhC0skRLCNIRti5SwTZEyhUjZXSLtkVtHZI3hXWRaBCk7aUFMxjBKhu3igyhrYZTY2lQsijKGDTNpu/xR7WG8ExvEB74ERMq2Xp3kRAn73V5uaQLj/B7eSQyyCCdPhTT/fabt+iXKST4ojdojGkWiqrwN/Nlc/YXnavWmbgnrScMUhrDG9JlSrvp8saDXGnquUCgW9PyLerNU1Bu1Zq5ZrlV1t5hrzJT0uFss6m7eaOTKBeNMNHpisuLWqk9o5n+ESosRz7NymudUI2Ohnt0e+Hlb0vbtft2G6+RUIL/yBvCXLhkTGcMa7auxYVQSA0zyP2sEKRJ7JBgaR+18qDym6TiUeIhRLlc8+bspjXVIkPV++PLlMXi06b7SjqHgSRxODDHKWcWD+2kHtGiHBOmVCQlXC6Tr8UZvGO/gAu/gKp4V4B3sAK9covPOsNlXut40/2pfv1em/3spC204P0X7O6BKv5IunBDrZSnkR8bpEIYRpDpxIPY3iXrF0PysM9xZ8mI3+/isHz9krUOiUj2b2CSh/yWazll2o3Hv8xvbJ+OvT3/s3A8KzrR3cy2B/yd0mE1IbHNo/F8XnIA0ODABk/AMlKAOczBH/hkAkHRqig==); Phase 1 BiS: [full raid](https://wowsims.com/forever/warlock/dps/#eJzElU1oK1UUx3PuTDI35z3befcpnY4fjIE+YmDCnQljk24y760eLqS4Eh5okyY1CZKETISKm4oBRbSFxgqNBUUtWrFSXWhxpYVCiiBdubAEi1IUNxaULovcybSVtgsXKe8szpw5f86c35lz4eIjFFTQwIA4TEEJ6jAH8AbABwCfArDrvkqEmgZ9HamkRvWXMEK/fFo7uIYyPV4ElOmf7wj/3q6KEbpT1X4bQoVurYK2N4QS3aqiTA8WABXaWwJRptCNz0FbUFCmP6+Kyh+WhG+1hf96V0WF/vUFaN2bKNO/3xXJtZXhmK12y/Ef54Ef5Sff/hDeBNIqLwI5yncg/Pvt91fhM1A+WYGNu/PlDfiosg+t8p3rZ9O58C15zHZsk3OH2zzFuWVyx+Ep7lg8ZXGecrpE2iXXfiVrFG8i1SMo08N5iCkYRsl0PHwQFT2MEl27F4uigmHTSjoee1R/GG/EhvGBrwBRpt+9PsmIGvarRWzrHOPsFt5IDNMII0+FdP97luP5KZmRfJAad8Z0GYmmsTaw53L1F5+v1ZuGze0nTYub3J4wpku56gvFglFrGLlCoVgw8i8bzVLRaNSauWa5VjW8Yq4xXTLiXrFoeHmzkSsXzBPR7IvJilerPqFb/xMqzcfEzOpRnsk6mQj1x+2Dn5YlHX/cb9pwmZwK5NfeAvbKucF4xrTHBzrYKKqJISr5vzWCMhJnLFgaQ/10qSymGziSeIjKTKkI+ft7Ou2QIOo/2Mr5NQja9EBpJ5CzJI4mRqjMaEXA/bINerRDgvDChrinB9LleONXjNc7w+tdxLMDvN42sMo5OnGGrYHS9bf5T/vyXpnB91JbbTg9RXvboEl/kC4cEvtVKeRbxu0QihGUDeJC7JhERTI0N+OOdpaF7WQfn/Htp6y9TzTZyCY2Sei+WNM9ia7Ubq1fWZ+M75/52L0dJNwpcXUtg/8S2s8mJLo5cuc/NxyHNLhwFybhWShBHWZhlvw7AOGwamo=).

## Other builds of this spec

- [Destruction (optimized, shadow bolt)](../research/raid/builds/opt-sb-raid-raid-dps.md) (10/11/30) — [open the talent tree](https://talentsforever.com/warlock/60/253-0050203001-055002510310035-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at 2ce8265 (client 1.60.1.70291)). Simulations, not in-game measurements. Do not hand-edit.*

