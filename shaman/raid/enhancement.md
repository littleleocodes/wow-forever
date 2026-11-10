# Enhancement Shaman — Raid (group)

[Shaman](../README.md) > [Raid (group)](README.md) > Enhancement

**✅ Recommended** for raid (the best shaman spec here, or within 3% of it).

**[Enhancement — Raid](../research/raid/builds/enhancement-ml-raid.md)** (17/31/3) — [open the talent tree](https://talentsforever.com/shaman/60/253103102-053030310051002251-03-12)

> 🔬 Derived build: found by this project's machine-learning search over every legal build of the spec in the community's raid simulator (phase-1 BiS gear, then raced against the spec's builds); it beat the hand-made build (Enhancement — Stormstrike / Maelstrom Weapon), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Strength of Earth Totem**, **Grace of Air Totem**, **Searing Totem**.

**Keep up all fight:** **Strength of Earth Totem**, **Grace of Air Totem**, **Magma Totem**, **Searing Totem**, **Rockbiter Weapon**.

**Then press the first one that is ready**, top to bottom:

1. **Flame Shock**: keep it on the target, until the last 10 seconds of the fight
2. **Stormstrike**
3. **Lightning Bolt** when Maelstrom Weapon has 5 or more stacks
4. **Earth Shock**
5. **Fire Nova** when you have at least 10% mana

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Rage of the Farseer**: a cooldown, use it at the start of the fight and again whenever it is ready (about 1 time a fight)
- Use your trinkets and a potion together with your big cooldowns.

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Enhancement is a melee spec that spends mana: your two-hander and **Windfury Weapon** do about half the damage, and you fill the gaps between swings with **Flame Shock**, **Stormstrike**, instant **Maelstrom Weapon** bolts, **Earth Shock** and **Fire Nova**, in that order. Mana is the limit, so the list puts the cheap and free casts first and **Fire Nova**, your most expensive, last.

**Why it works**

- Before the pull, drop **Strength of Earth Totem**, **Grace of Air Totem** and **Searing Totem** (one by one, or all at once with **Call of the Elements**). In Forever the first two last 5 minutes, so one cast covers the fight. Grace of Air rather than **Windfury Totem**: your own **Windfury Weapon** turns Windfury Totem off for you, and a party gets only one of the two.
- **Flame Shock** goes on the target whenever it is off (it lasts 21 seconds with **Call of Flame**; keeping it up measured about 1% better), so most presses go to **Stormstrike**: it costs only 8% of your base mana, hits for 150% weapon damage and makes your next **Lightning Bolt**, **Chain Lightning** or **Earth Shock** deal 20% more for 12 seconds. With **Improved Stormstrike** each one also keeps half your mana regeneration going while you cast for 15 seconds, so on its 6-second cooldown that never drops.
- **Flame Shock** and **Earth Shock** share one cooldown (6 seconds, 5.8 with your point in **Reverberation**), and **Shamanistic Focus** makes both 45% cheaper. Every shock that is not a Flame Shock is an **Earth Shock**, which also takes **Stormstrike**'s 20%.
- **Lightning Bolt** only at 5 stacks of **Maelstrom Weapon**: 5 stacks make the bolt instant and free. Waiting for the full stack measured better than casting at 3.
- **Fire Nova** erupts around your Fire totem, not around you, so keep **Searing Totem** down within 10 yards of the boss and replace it the moment it expires, even late in the fight. Adding Fire Nova measured about 7% more damage in the rotation search, the biggest single change to this list. With **Trial by Fire** its cooldown is 6 seconds (10 without), so it is not a true filler: the list casts it with at least 10% mana, and when nothing is ready you keep swinging.
- Put **Windfury Weapon** on your two-hander with an Elemental Sharpening Stone on top: in Forever an imbue and a stone stack. Its extra attacks are about a fifth of your damage, and **Elemental Weapons** makes them 40% stronger. Press **Rage of the Farseer** (30% attack speed for 25 seconds) at the pull with your trinkets and potion.

**Caveats**

- Mana runs short: with only your own buffs the simulator's build runs out of mana for part of a 3-minute fight. Do not hold shocks in reserve (casting **Earth Shock** freely measured 3% better than keeping 60% of your mana, on the training dummy), and use a mana potion and a Demonic Rune when low. Clearcasting from **Elemental Focus** makes your next damage spell free: nothing to change, the next line takes it.
- Several targets: **Fire Nova** hits every enemy within 10 yards of your Fire totem, so it gains the most from adds. You can have only one Fire totem out at a time; if the adds stand away from it, **Totemic Call** brings it to you, with all your other totems.
- **Maelstrom Weapon**'s proc rate is not published. The stacks last 30 seconds, so cast the bolt when you reach 5.
- Forced out of melee range? A 5-stack **Lightning Bolt** (instant) and the shocks (20 yards) still land.

**When to change it**

- In the last 10 seconds, skip **Flame Shock**: its burn would not finish. Use the shock on **Earth Shock** instead.
- If the fight runs past 3 minutes, press **Rage of the Farseer** again as soon as it is ready.
- In a party of warriors and rogues, ask whether they want **Windfury Totem** instead of **Grace of Air Totem**. A party gets only one of the two, and Windfury Totem does nothing for you while you use **Windfury Weapon**.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Elemental | 17 | Convection 2, Concussion 5, Elemental Devastation 3, Reverberation 1, Call of Flame 3, Elemental Focus 1, Trial by Fire 2 |
| Enhancement | 31 | Thundering Strikes 5, Ancestral Knowledge 3, Mental Dexterity 3, Elemental Weapons 3, Shamanistic Focus 1, Flurry 5, Stormstrike 1, Mental Quickness 2, Improved Stormstrike 2, Maelstrom Weapon 5, Rage of the Farseer 1 |
| Restoration | 3 | Tidal Focus 3 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 998 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 985 | this build |
| Phase 1 BiS | 1021 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.1; Phase 1 BiS 62.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Mantle of the Timbermaw](https://www.wowhead.com/forever/item=19050) · *Tailoring* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Timbermaw Tunic](https://www.wowhead.com/forever/item=252484) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Theramore Handwraps](https://www.wowhead.com/forever/item=271945)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) · *sold by Pix Xizzix* | [Quick Strike Ring](https://www.wowhead.com/forever/item=18821) · *Magmadar, Molten Core* |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) | [Totem of the Storm](https://www.wowhead.com/forever/item=23199) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzEVU1MK1UU7rkznbk9EigXiOOIYSjBYHWaO1NKCpsWVsYVsGInAx1s/WkbpjHoBkwQDREIG0zRiImiRsG4kAQNxoSYBneYGBYQI0FJiGFhjO938fIy0/aFB29b3lncnJ7zde73nfMlF1spBEEBDbpgFNKQhxmA9wE+BfgKgNV5XeJ246DeCFApKKtvo0x/2mpQTp5Akc5tAoq0+E8QZfrRflD5TUKZ3vkGlL/qUaa766D84SaffAHKmowiPV0ClGnpe+/vMv1uA5Q/61GkK/tBFOnCuXtuefnyz+43f1kH5bwefSjStS0IPR/cy3T999rgwSKM/D86D2Q2swrSZ9aGddj/NQQ+yHz5MZwai5ljmM0MUI89JOFH0mbGogaPGtzUeSzKo27KYwbnphkzdB7dI7BPhBNyW8YWpKrk3l+CUABl9OvdkZiDTZXyUglCMvpR0KMONqOs+lGgpaEK1IjEHPYhsAkr//rLuXxBM7nZo/Ne3Yz3aeNpK/uKndJyk5qVStkpbewtrZC2tclcwSpkclnNsa3J8bTW5di2ZmfTVnbcfsPOFvRU3tGrIL0Mirzq5LLPqTp2sHasCyFS0yW98TdgY7iBSoy85FM9ngZ31EqLtanPYFO4kYrMPy8QCm4DSQWwXLoCIA8BlkrARJX0+Riq5WH8/h6wlctqDa6bPTVR+0JZ7aEUQIEeDTMSFKtqxypqzVint5GjYbbwCGK8tybEOlANK1RigV1wx/LDLUX1/NAdMY24x+fsTTZ3fbZovbhE4cESXSKlIRZQy679doi9e2VGhs67a8Lp6curMniny4wWbyps+to81FL1z8606x9vEDvTinBG9uBfYr4j+LxoTt4FSRWRUAjdIwG35JuZSD61WnTj10T7hBcHCfOYKKKWCG8T32OJQrKa1TSe3azZPb3eOfx5sr9SSI66T1ARvB++40RYoNtPDlx4qTjEIQkvwiCMQBryMAVT5P4AVrRxtQ==); Phase 1 BiS: [full raid](https://wowsims.com/forever/shaman/enhancement/#eJzEVV9INFUU33Nndubu6cPd736fNE2G44phW7PcmXVl9WVXn6In9cm3HN2x3f7sLs4S1osGWiHlIkWhCQYlRVj0oGBhPUgsCj0YhA9KJKYg0UNE/wiKuLO7Ydrr2nm4nD3nt3d+v3N+cLGNQgQ0MKAbxiAHJZgFeBngbYD3Adgtv0tENwX6LyGqRFT9eVTpZ1th7fQelOlZBVCm378OqNK3DiLaVwqq9IvNsPZdC6p0dx20b0Sy/2VEW1NRpucVgaxu+n9X6ccboH3bgjKdf03c8/m6OLcOIijTP1fD4qp10H5owQDKdG0Log9H9vLdPz01dLgIoz+PLQCZy6+A8o6z4RwNfAChV/LvrcK5tZg/gbn8IPXZQwY+Je12MmHxhMVtkycTPCFSnrQ4t+2kZfLEHoEDIp2S31VsRaorKNOlKkRDqGLQ7IknPbxTL1eqEFUxiJKZ8PAuqnoQJVodrkOteNJjbwKbdEpPP14slQ2b270m7zPtVL8xkXMKT7hZozhlONmsmzXGnzPKOdeYKpadcr5YMDzXmZrIGd2e6xpuIecUJtxn3ELZzJY8swEya6D4k16x8JBuYifrwFtRRGoL0htngLdjYaow8lhA93la3NPrLdauP4B3YrepzIILEqEgGkjqgKXqNQD5F6BSBSbrpD/AUK8N4+uXgL1xVa3FTbu3KWofqak9UkIo0eMRRiJyQ+14Xa2d7PI3cjzCXv0PYryvKcQ6UY9pVGGhXRBj+eQ3Tff90BO3rZTP5+JZ9uLN2aLt8hKlf5YoiFSHWUivufajYTZ/bUaWyXuawun+q6uyeJdgRpd/1djMjXmoteGfnRnhH38QOzOadEH24EdivyAF/Lib+QMUXUZCIfoXCYlSYHYyc9/Ksoj9dMekH4dp+4RospGObZPA/xLlTCNrajz4YdO+0+efI+9mBuqFzJh4gpbB/xE4Scckun3v4KWXikMKMvAoDMEo5KAE0zBN/h4ArBFx6Q==).

## Other builds of this spec

- [Enhancement — Stormstrike / Maelstrom Weapon](../research/raid/builds/enhancement-raid-dps.md) (11/31/9, 930 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5230001-055030310051002051-05004-12)
- [Enhancement (optimized)](../research/raid/builds/opt-enhancement-dps-raid-dps.md) (14/31/6, 915 DPS in a full raid) — [open the talent tree](https://talentsforever.com/shaman/60/5005031-155030010151012051-051-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

