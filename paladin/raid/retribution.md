# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-full-buffs-raid.md)** (10/8/33) — [open the talent tree](https://talentsforever.com/paladin/60/52003-503-05225231001330321-7)

## How to play

**Before the pull:** **Seal of Command**.

**Keep up all fight:** **Seal of Righteousness**.

**Then press the first one that is ready**, top to bottom:

1. **Hammer of Wrath** when the target is below 20% health
2. **Judgement** when Seal of Righteousness is active
3. **Consecration** when you have at least 25% mana
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of Command**: seal twisting. While **Seal of Righteousness** is up and you have at least 15% mana, switch to Seal of Command; just before your next swing, switch back to **Seal of Righteousness**, so the swing gets both seals

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Retribution in a raid twists seals: you swap between **Seal of Righteousness** and **Seal of Command** around every swing so each hit carries both, judge **Seal of Righteousness** on cooldown, and give the remaining global cooldowns to **Consecration**, **Holy Strike** and, under 20% health, **Hammer of Wrath**.

**Why it works**

- Only one seal can be active, so keeping up two seals means a twist: with **Twist of Light**, replacing a seal leaves an Echo of it that your next melee swing applies. The full rotation casts **Seal of Righteousness** in the last 0.4 seconds before each swing and **Seal of Command** after the swing, in any global cooldown that **Hammer of Wrath**, **Consecration** and **Holy Strike** do not need: about 14 and 12 times a minute. Opening with **Seal of Command** means your very first swing already carries both.
- Press **Judgement** every time it is ready while **Seal of Righteousness** is up, whether or not the short list shows it. It is off the global cooldown, comes back every 8 seconds with **Improved Judgement**, no longer uses up your seal in Forever, and **Sanctified Judgement** returns 60% of the seal's mana cost; in the simulator the judgement of **Seal of Righteousness** is about an eighth of your damage. If it comes off cooldown while **Seal of Command** is up, judge anyway.
- **Hammer of Wrath** goes first once the boss is below 20% health: with 2 points in **Instrument of Law** it is instant, it comes back every 6 seconds, and at about 500 Holy damage plus a share of your spell damage it is your biggest single hit.
- **Consecration** comes before **Holy Strike** while you have at least a quarter of your mana: on a single boss it deals 312 Holy damage over 8 seconds plus a share of your spell damage, about a sixth of your damage in the simulator, and **Holy Conduit** makes it 40% cheaper.
- **Holy Strike** sits last but is not a real filler: it has a 10-second cooldown, so press it whenever it is ready (20 mana, and **Sacred Arbiter** adds 20% to it). The global cooldowns between your other buttons go to the seal swaps.
- **Seal of Command** is always rank 4: every rank adds the same 70% of weapon damage, rank 4 costs 30 mana less, and the simulator measured it 0.3% better than rank 5. When mana runs low the full rotation steps down: **Seal of Righteousness** rank 7 below half mana, **Seal of Command** rank 2 below 30%, a rank 1 **Consecration** below a quarter, and no seal swaps at all below 15%.

**Caveats**

- The twist rests on the simulator's reading of **Twist of Light**: every Echo you have up fires on the next swing, so a swing after both swaps applies **Seal of Righteousness** twice (the seal and its Echo) and **Seal of Command**'s chance once. If the game allows only one Echo per swing, one swap per swing, alternating the two seals, does the same work with half the global cooldowns: check it at launch.
- All those swaps cost mana, even 20% cheaper with **Twist of Light**. The full-raid numbers assume the raid's **Blessing of Wisdom**, Mana Spring and other paladins' judgements of **Seal of Wisdom** and **Seal of the Crusader** on the boss; with only your own buffs the simulator keeps **Seal of Righteousness** up and twists on every swing only while your mana is above about two thirds.
- Forever weakens ranks far below your level, and the simulator applies an assumed formula (TBC's) since 2026-10-09. **Seal of Command** rank 4 and **Seal of Righteousness** rank 7 are close enough to 60 to lose nothing, but rank 1 **Consecration** keeps only a bit over half of its spell damage bonus, so it is a low-mana stopgap only; the game may also lower a low rank's chance to trigger effects, which no simulator models.
- Several targets: only **Consecration** spreads (its bonus damage hits the first four enemies in it); your seals, judgements and **Holy Strike** stay on one target.
- The full rotation also has a **Holy Shock** line (after **Holy Strike**) for builds that take it, worth several percent there in the simulator; this build has no **Holy Shock**, so skip it.

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 952 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, ElliotWood/Forever fork 2ce8265 (client 70291); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 929 | [12/7/32](https://talentsforever.com/paladin/60/52003002-502-05225131001330321-7) |
| Phase 1 BiS | 954 | [11/8/32](https://talentsforever.com/paladin/60/52003001-503-05225131001330321-7) |

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 64.7; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Bonereaver's Edge](https://www.wowhead.com/forever/item=17076) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzsmE1sG0UUx/3GG+/kpU3NQJWNVaIhksFxs9bsugtpELLTE4JLQBw4Qe16XW9xvdbuGjW3Ior4EKCKE61EALmRChSlUCqiiB6IWuQih5pDOVQUUOHQQ5ECSLlwQWs7H0pAYKlIEPkd7Ofx3973fv6P32pwG4UwKMAhBgLY4OorImAM0jAJT0IZjgJEXh6iUphEplCmF87vUG70oUSfnwWU6A+/bUeZfnUclK9DKNO3ft6u/NiPMl2YAeW6n8zPgPK2jBL9btlXfvFJ8+MyPXsGlO/7UaKnTvmPX74LGKSvHUaJnm+EUaYXZ0C51Y8BlOi5RnjYoMescM1SXrVivz4jlrOTP30ErwA5Zr0BZDn7JlQz78CZzGm4NjEH75+GGkADXrf24VqH82RIN4RICqGphkiqwtB1Q0tqQmjJpEjqWo1IN8iLu3AAMUIxFOuhc1UY7kUZe1QtYbisAexzcE0zZ+a4LvT7VU2owuB5xz7MXTNTVO28mq84U6qTsXL3udx/4o7tZTzLLvGYVzC5XTZLvtY5UOCOqXqVkpnjlsftEs/wx03PsbKVpjpbsYq5kXG+W0uMRbln8916QovyvO1w81nTmdos5pb/HflKsdi6cEwTo0IInrcOFjx3lPuFcy05Eml1F6SzF4D9TtgH5H/f0oM8Uy4+bZe9dT2M8wOFTOmgmeO2wzM5/zfLTnG/4NXy20XHXNPc3Ky6IlNbssQh1y6NRB7FFHsI74jvoCFGsoGIjD0Y1Iwo7ozfSYOsZ4EQSnzAKInEHrepDK4pDRH134zJ9OI0sJtd+p3RH8NRFv/n9P0sRumlaWCXuqg7Q70T+z6GVX6REEp0dhrYYpdjZxzv3mhX3Yi2x8tnVWBXtsZM6fV7i1F6fZIdYk9thKvt6RCuY3pqruz+BVLadONCFVhta9Aj4wH2S3djdbaxJtBgyT+bBev/tzbO32R7/hJ6rgrsOGz2qnjgtno1gcOM/12VzZIk+mkV2LWuDTqzQRw5G8Lek9CeUCusH2mz1oW7Ory21A080MUrwK52/dKZX6I4GB+gEuubX7f/Qigh0dbdLyrBm6QGS0R/Lhhoxl3peZCQYGD4vWCvvxA4mk8Pnjzhx+XUPflmfJPSl4gi8VS8RgL/qfDSK9m/Gvd+eNuvs3exXq9v2382PdFeSO+HlwBOgGUvvXD5iaupvc3VQCM14Svr9Vupx1rJt6l4kM4N7Nu1dgbQOtd4uHmyUYAyHIEj7I8BAExAvhw=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzsmF2IG1UUx3NuZjN3T9ttvFp2NtTluhDNpjvhzqSj2xVJtk+iL6v44JM2aSbN1DQTZibSfavS4gcq0idbcRXSQtVKq624LPpgsZJKlsaH+lCsShXsQ4VVYV8EkZlkP9hVNFBBl5yH5OTmn8w5v/xvznBxM4UoKMAhAQLY0PIrImAcsjAFj0MVDgHEXhimUpTEplGmP57cqlzfhBL9/SigRL/7dQvK9PVWVPkygjJ946ctyvcDKNMvngXlmp/MnQTlTRkl+s2ir/z8fPBxmZ49Dcq3AyjREyeWHsP05QMo0Q9bUZTp+SOg3BzAEEr0XCs6YtDDVrRhKS9ZiV+eEov5qR/ehxeBHLaOAlnMvwb13FtwOncKrk7OwjunoAHQgles3bjS4RwZNnQh0kJoqiF0VRi6buhpTQgtnRZpXWsQ6Tp5bjsOIsYoRhJ9dLYOI/0oY5+qpQyXtYB9Cq5pFswC14V+r6oJVRi86NgHuGvmyqpdVIs1Z1p1clbhHpf7T9yxvZxn2RWe8Eomt6tmxdc6e0vcMVWvVjEL3PK4XeE5/qjpOVa+FqjzNatcGJ3gO7TUeJx7Nt+hp7Q4L9oON582nen1Ym7531GslcvtCyc0MSaE4EVrX8lzx7hfONfSo7F2d2F65hNgvxH2Lvnft3Q/z1XLT9pVb1UPE3xvKVfZZxa47fBcwf/N8tPcL3i5/E7RCdc01zerLsnUtiy137Uro7GHMcMewNuSW2mEkXwoJmMfhjUjjtuSt9Mw67tACCU+YJREaqcbKMMrSkPE/TcTMv1sBtiNHv3u6I/jGEv+c/p+lqD04gywiz3U3aHehps+gGV+sQhK9MwMsPkex+443rnWrroR74yXj+vALm+MmdLv95ag9NoU28+eWAtX29klXMf01ELV/QukNHDjhTqwxsagRyZC7OfexupuY02iwdJ/NgtW/2+tnb/pzvwl9Fwd2Kuw3qvivlvq1RSOMP53VQYlSfSjOrCrPRt0Z4MkcjaM/cehM6GWWD/UYa0Ld3l4bagbeKDzl4Fd6fmlO7/EcSg5SCW2aW7V/oughERbdb+ohG+QBiwQ/ZlwKIg7snMgIcHQyNvhfn8hdKiYHTp+zI9LmbuKQXyV0ReIIvFMskFC/6nwskvZvxp3v3fLr7Nrvtlsbt5zNjvZWcjugecBjoFlLxy59NiVzK5gNdTKTPrKZvNm5pF28nUmGaazg7u3r5wBtM81HgxONkpQhYNwkP0xAL9+vk8=).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 952 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-7)
- [Retribution (optimized)](../research/raid/builds/opt-ret-dps-raid-dps.md) (17/0/34, 948 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/55003013--05225331001330321-7)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 925 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-25 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at b7083fa (client 1.60.1.70425, its spell data of 14-15 Oct)). Simulations, not in-game measurements. Do not hand-edit.*

