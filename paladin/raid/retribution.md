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
| Head | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Theramore Shoulderguards](https://www.wowhead.com/forever/item=272957) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=22089)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Soulforge Gauntlets](https://www.wowhead.com/forever/item=22090)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) |
| Finger | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzsmEFoHFUYx/d7O9l5+VLS7dOS6VLDM7A62WaWN7MdjRHZTU+il1AvnrSz3dnu1HVnmZmV5FaxqIgU8SAkYhTWQGlTWyxoCHowtBAPpfFgkUIx1INFPFgPRRFFZrJJl0TRBYM07HfYffvet+9932/+b77Hw/0UkqAABxWOQAXqcALgdYAPAE4DsF3RKAlHRyH1yiCVkiQ1iTL9fm63crMPJfrqOUCJTv+QRJm+u5JUvkqgTH89C8p3/SjTpTlQbvRjgn5TVN6XUaK/vAco09sfQfhvmV6YB+XbfpTo7++E08xf2IMS/WQliXHafAZlemkOlB/7MYYSvbiSHMomlx315xfEneLEtVPwBpCTzttA7hRnING05q3r42dAftM5cxpOOatw0jm0625yBVgkg6YhRE4IQzOFoQnTMEw9pwuh53IiZ+jLRLpJXtuPA4gpigm1hy40YagXZezR9KzpsxVgX4Bv2yW7xA1hPKLpQhMmL3vui9y3rarmlrVyw5vSPMspPezz8It7bmAFjlvjalCxuVu3a6Gvd7TCPVsLGjW7xJ2AuzVu8cN24DnFRuRdbDjV0vAYP6BnR9M8cPkBI6unedn1uP2S7U1tdeZOOEe5Ua2uLazqYkQIwcvOsUrgj/AwcK7nhlNr2cXp+c+B/UbYWXLPp/Q4t+rV59160JbDGD9asWrH7BJ3PW6VwmdWnOJhwBvht4JWfdvemqy27qatuWWP+25tOPU05tkTuCezmyYYKcZSMvZgXDfTuDdzH42zniVCKAkBoySyB/3IM37X0xTpcFCV6aVZYLe69DujP4ojLPPv6YctldLLs8Aud1F3hnov9n0MG/xSCZTo+VlgV7ocO+P4wGa5Gma6VV4+awK7ujNqSm+Ym0rpjQl2nD23Ga5+sEO4nh1opbr/N0hppMalJrDlnUGPjMXY7e7G6mxjjaPJcn9VC9rfW5vrb65Vfwm92AT2FmzVqnj0P9VqFocY/6coo5Ak+mkT2PWuDDqTQQY5G8TeGWhVqHXWT7VYG8LfKF476gAP9MpVYF939dKZXtK4LzNAJda32Lb/Eigh0dvOi0r8FlmGn4jxcjwW2f2FRZCQYGzoD9IbdsROlAv7ZqZD+zL/YDmya3ljlSgSz2cWSOx/saCw3tpWe+jctq3zWPR5+MPCeKujcCS8kJiG6EdsNZ+J04WBQ233FgJGoQBPwgQ8CxWowyRMkj8HAK4pqOg=); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzsmFFoW1UYx/Od3Oaefh1dPDp6F2Y5FqJp1hvOvdnVWpGkexJ9KXvySZcsN8udMTfceyOrTxMqisiUCcIqVCEWxqxOHGgp7sGyQSeMRdA9FIZlIu7BB+fDXoQh5zbtQqtowCEr+R5uTs75cs73/fI/9zsc3EchDhpwSMFhqEAdTgC8CfARwBkAtiscJXJ0HBKvD1MlThKvokp/md+t3RhAhd45BajQC9/HUaUftOLadzFU6eUF0H4aRJUuz4N2XTa+XQDtQxUV+vM7gCq99RnIn6v08wXQfhxEhb7fiqNCV+flbDPvyeeXLTnnxXnQfh3ECCr0fCs+komvOKnfXxK3i1PXTsJbQGacU0BuF2ch1iwsFFYnz4L6tnP2DJx01mDGObjrbnp5WCLDlilEVghDt0RWF5ZpWkbWEMLIZkXWNFaIcoO8sQ+HEBMUY6k+utiEkX5UsU83MpbPWsC+Ad+2S3aJm8J8XDeELixe9tyXuW8Xqrpb1ssNb1r3Ck7pMZ/LD+65QSFw3BpPBRWbu3W7Jn29IxXu2XrQqNkl7gTcrfECP2QHnlNshN7FhlMtjU7w/UZmPMkDl+83M0aSl12P26/Y3vR2Z+7IOcqNanV94ZQhxoQQvOwcrQT+GJeBcyM7mljPLkrPXQD2B2GfkPs+pad4oV590a0HHTlM8COVQu2oXeKuxwsl+Z8Vp7kMeDP8dtAp37a3J6tvuOnrbpljvlsbTTyHOfY0PpDeTWOMFCMJFfswalhJ3JN+kEZZ3zIhlEjAqIjMAT/0jN71tERSDqZUenEO2M0e/e7oj+MYS/97+rKVovTSHLBLPdTdod6DA1/AJr9EDBV6bg7YlR7H7jg+vFWuppVsl5evm8Cu7oya0i9zS1F6fYodYy9shWsc6BKuZwd6qe7/DVIaqnG5CWxlZ9AjExF2q7exuttYk2ix7F/Vgs731tb6m23XX0LPN4G9C9u1Kp74T7WawRHG/ynKMCSFftUEttqTQXcySCNnw9g/C+0KtcH62TZrU/ibxWtHHeCBXrkK7IeeXrrTSxL3poeowgaWOvZfDBUkRsd5UYveJCvwGzFfi0ZCeyi/BAoSjIzcIf2yI3KinN87e1ra5dwj5dCu5cw1oik8l14kkf/FgvxG657ao5/es3WeDJ+HPs5Ptjvyh+WVxGkIv0TWcukoXRw62HFzIWAc8vAMTMHzUIE6HIfj5M8BAHAJqV0=).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 952 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-7)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 925 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-7)
- [Retribution (optimized)](../research/raid/builds/opt-ret-dps-raid-dps.md) (17/0/34) — [open the talent tree](https://talentsforever.com/paladin/60/55003013--05225331001330321-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-26 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the ElliotWood/Forever fork (deleted 2026-10-18) at b7083fa (client 1.60.1.70425, its spell data of 14-15 Oct)). Simulations, not in-game measurements. Do not hand-edit.*

