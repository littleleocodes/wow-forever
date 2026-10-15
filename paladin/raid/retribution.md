# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-full-buffs-raid.md)** (10/8/33) — [open the talent tree](https://talentsforever.com/paladin/60/52003-503-05225231001330321-6)

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 979 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 945 | [12/7/32](https://talentsforever.com/paladin/60/34003002-502-05225131001330321-6) |
| Phase 1 BiS | 999 | [11/8/32](https://talentsforever.com/paladin/60/52003001-503-05225131001330321-6) |

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 65.4; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=234020) | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) |
| Finger | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Serenity Field](https://www.wowhead.com/forever/item=272439) |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Bonereaver's Edge](https://www.wowhead.com/forever/item=17076) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzsmF2IG1UUx3NuZnfunq3beLXsbKjLdSGaTXfCncmOblck2T6Jvqzig0/apJk0U9NMmJlI961CxQ9URBBthVVJA1UrXa3gsiji0koqWRof6kOxKqtgH/qwKuyLLzJJ9oNdRQMVdMl5SE5u/smc88v/5gwXd1EIgQIcoiCADa2/IgImIAXT8BiU4DhA+PlhKoVIeAZl+nN1t7LcjxJdfh1Qoj/8dgvK9M1GSPm6F2X6eRWUHwdQpotVUK75yUIVlLdklOh3q77yy4+bH5fp3FlQvh9AiZ4+7T9+9Q5gkL50FCU69xqgTC9UQbkxgAGU6PlGaMSgJ6xQzVJetKK/PilWM9M/fQgvADlhvQpkNfMGVNJvw9n0Gbg6NQ/vnYEaQANetg7gRocLZDgxLkRCCF01hK4KQ9cNLaEJoSUSIqFrNSItk2f34iBimGJvtIfOV2CkD2XsUbW44bIGsC/ANc2smeW60O9RNaEKg+cc+yh3zXRBtXNqruzMqE7ayt7tcv+JO7aX9iy7yKNe3uR2ySz6WudQnjum6pWLZpZbHreLPM0fMT3HypSb6kzZKmRHJ/k+LT4R4Z7N9+lxLcJztsPNp0xnZruYW/535MqFQuvCUU2MCSF4zjqc99wx7hfOtcRouNVdkJ77DNjvhL1P/vct3cfTpcITdsnb1MMkP5RPFw+bWW47PJ31f7PMDPcLXi+/XXTUNc3tzaprMrUlix9x7eJo+CFMsvvx1thu2stIJhCWsQeDmhHBPbHbaJD1LBJCiQ8YJREfd5vK4IbSEBH/zahML8wCu96l3xn9CRxjsX9O38+ilF6cBXaxi7oz1Huw/yNY5xfuRYmemwW21OXYGcc7ttpVNyLt8fJpBdjlnTFT+vzeopRem2ZH2ONb4WrjHcJ1TE/Nlty/QEqbblysAKvtDHpkMsB+6W6szjbWFBos8WezYPP/1tb5m2jPX0LPV4C9Atu9Ku69qV6N4wjjf1dlsySJflIBdrVrg85sEEPOhrHvFLQn1BrrB9usdeGuD68ddQMPdOkysCtdv3TmlwgOxQapxPoXNu2/XpSQaJvuF5XgdVKDFaI/HQw04/bUAkhIMDDybrDPXwgcz6WGTp3041LyzlwzvknqK0SReDJWI4H/VHiptexfjbs+uOnX2b9Ur9d3HZxLTbUXUgfhOYCTYNkrz1x69Epyf3M10EhO+cp6/Uby4VbybTIWpPODB/ZunAG0zjUeaJ5s5KEEx+AY+2MAKNO+GA==); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzsmF2IG1UUx3NuZjN3z7bbeLXsbKjLdSGaTXfCnUlHtyuSbJ9EX1bxwSdt0kyaqWkmzEyk+1ahix+oSEGwBVclLFSttNpil0UfXKykmqXxoT4Uq1IF+1BhVdgXQWSS7Ae7igYq6JLzkpObf2bO+eV/c4aL2yiEQQEOMRDABlffEQFjkIZJeBzKcBQg8vwQlcIkMoUy/XF2h3K9DyX6+3FAiX7363aU6YfToHwZQpm+/tN25ft+lOnCLCjX/GR+FpQ3ZJToN8u+8rPzza/L9OxpUL7tR4l+/pZ/nS9eBQzSlw6jRC80wijT89Og3OzHAEr0XCM8bNBjVrhmKS9asV+eEsvZyR/ehxeAHLOOA1nOvgbVzJtwOnMKrk7MwTunoAbQgJetfbjW4TwZMnQhkkJoqiGSqjB03dCSmhBaMimSulYj0nXy7C4cQIxQDMV66FwVhntRxh5VSxguawD7BFzTzJk5rgv9XlUTqjB43rEPc9fMFFU7r+YrzpTqZKzcPS73X7hjexnPsks85hVMbpfNkq91DhS4Y6pepWTmuOVxu8Qz/FHTc6xspanOVqxibmSc79YSY1Hu2Xy3ntCiPG873HzadKY2i7nlXyNfKRZbN45pYlQIwfPWwYLnjnK/cK4lRyKt7oL0zMfAfiPsXfK/b+l+nikXn7TL3roexvmBQqZ00Mxx2+GZnP+bZae4X/Bq+e2iY65pbm5WXZGpLVnikGuXRiIPY4o9gLfFd9AQI9lARMYeDGpGFHfGb6dB1rNACCU+YJREYo/bVAbXlIaI+h/GZPrpDLAbXfqd0R/DURb/5/T9LEbpxRlgF7uoO0O9E/s+gFV+kRBK9MwMsMUux8443rnRrroRbY+Xj6rALm+NmdLr9xaj9NokO8Se2AhX29MhXMf01FzZ/QuktOnGhSqw2tagR8YD7OfuxupsY02gwZJ/NgvW/29tnL/J9vwl9FwV2Cuw2avivlvq1QQOM/53VTZLkuiFKrCrXRt0ZoM4cjaEvSehPaFWWD/UZq0Ld3V4bakHeKCLl4Fd6fqlM79EcTA+QCXWN79u/4VQQqKte15UgjdIDZaI/kww0Iw70vMgIcHA8NvBXn8hcDSfHjx5wo9LqbvyzfgqpS8RReKpeI0E/lPhpVeyfzXufu+W32fvYr1e37b/bHqivZDeD88BnADLXpq+9NiV1N7maqCRmvCV9frN1COt5OtUPEjnBvbtWjsDaJ1rPNg82ShAGY7AEfbHAKTXvk4=).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 982 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-6)
- [Retribution (optimized)](../research/raid/builds/opt-ret-dps-raid-dps.md) (12/8/31, 979 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003002-503-05225131001230321-6)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 954 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-15 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

