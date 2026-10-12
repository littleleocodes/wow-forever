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

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 996 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator; [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 969 | [10/8/33](https://talentsforever.com/paladin/60/25003-503-05225231001330321-6) |
| Phase 1 BiS | 1042 | [9/8/34](https://talentsforever.com/paladin/60/15003-503-05225331001330321-6) |

*Gear-tier numbers searched on 2026-10-02, on an older simulator build than the rest of this page (before beta 70291 and the 2026-10-09 audit that took Atiesh out of the full raid): they run 3-7% high and can order the specs differently than the full-raid ranking. The searches are queued to run again.*

**The gear** (average item level: Pre-BiS 61.8; Phase 1 BiS 66.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/spell=13828) | [Gloves of the Hypnotic Flame](https://www.wowhead.com/forever/item=18808) · *Molten Core*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/spell=13828) |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcanum of Voracity](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/spell=13823) |
| Finger | [Rune Band of Wizardry](https://www.wowhead.com/forever/item=22339) · *Lord Valthalak, Blackrock Spire* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* |
| Main hand | [The Unstoppable Force](https://www.wowhead.com/forever/item=19323)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Bonereaver's Edge](https://www.wowhead.com/forever/item=17076) · *Ragnaros, Molten Core*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzsWE1sG0UU9pvdZCcvbRoGqmxcioZIBsfNWrNrFtIgZKcnBJeAOHCCrut1veB6rd01Sm5FFAkhQBUSiBQRkKxKBQoJFEQU0QOFIldyaDiUQ0UBFQ49FCmAlEsPoLWdHzUgsAQSjfwufh5/3vnet9/Omx3cRqEfVOAQBwFscO0bETAKGZiAR6EMhwGi07up3E+ik6jQ0x/vUC/3okyfmQWU6Q+/bUeFfnUU1K+7UaFv/Lxd/bEPFXrmOKiXwmThOKhvKijT71ZC5JcfNf6u0LmToH7fhzL9/H1Aif5uoURfPIQynXsFUKHXXgX1ah9GUKanlvqHTHrE6a856gtO/NcnxUp24qcP4HkgR5yXgaxkX4Oq9RactE7AxfF5eOcE1ACW4CVnH64XuEB2GaYQKc0UKU2YhmEaKV0IPZUSKUOvEfkyeX0XDiBGKXbHu+h8FYZ6UMEuTU+aPlsC9hn4tp2zc9wQxt2aLjRh8rznHuK+bRU1N6/lK96U5llO7k6fhx/ccwMrcNwSjwcFm7tluxRivQMF7tlaUCnZOe4E3C1xiz9sB56TrTTQ2YpTzA2P8T16cjTGA5fvMZJ6jOddj9tP2d7UZjB3wmvkK8Vic+K4LkaEEDzvHCwE/ggPiXM9NRxtVifR2dPArhH2LrnhS7qXW+Xi42452FDDGD9QsEoH7Rx3PW7lwnuWneIh4TX6LdJx37Y3F6utwrQmLPmE75aGow9imt2HNyV20G5GspGogl0o6WYMdyZuphLrOkMIJaHAKIvkXX4DKa0jTRELf4wr9IsZYFc66ren/iiOsMQ/Vz/M4pSenQF2tiN1e1LvxN4PYU2/aDfKdHYG2GJHx/Z03H29XQ0z1movn1aBnd8aPaUnrC1O6aUJVtsaFZGxCPulY/b2zD6OJkv92fq8cS25viemWj2R0FNVYEeBPbaJ7z1t8vXsQMuV/b9gmcQhxv+OZYOSTD+pArvYsUF7NkggZ7dhzzFodY1VrR9oaW0If62hbKlNNdDF88AudPzSnl9iOJgYoDLrXdjw/HWjjETfsIdTpSukBsvEeFqKNOKWzALISDAy9LbUEw5EDuczg8emwziXvj3fiG/SxjJRZZ5O1EjkfxVBZjX7T+OO9/71efYu1uv1bfvnMuOtgcx+eA5gGhx3+dlzj1xI722MRpbS4yGyXr+afqiZfJtOSHR+YN+t6y/lzXOG+xsnDQUowyRMsj8GADQCmoE=); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzsWF9oW1UYz3dym3v6dWvr0dHbzMmxEE2z3nDuvV7tKpJ0T6IvVXzwSZcsN8vVLDfceyPr24QVRFSkMHBVqxCEqZNNN7UU92BxkmHK6sN8GE5l+rCHCVWhCKLITdI/tIoGFLTke8mXk1/O+X2//HK+cw/uoNAPCnCIgwA2uPaOCBiFNEzAo1CGowDRmT1U6ifRSZTp+ff7lGs9KNHfpgEl+s1PO1GmH0yB8nkEZfrq9zuVb3tRpgtvgHI1SH6eBuU1GSX61UqA/PRc4+syPXMKlK97UaKfHQ/mWTgOGKbPH0aJ/vpKH8r03BQoN3oxhBI9u9Q/ZNJjdn/NVp6z4z8+KVayE9+9C88COWZPA1nJvgTVzOtwKnMSrozPwVsnoQawBC/Y+3G9wnmyWzOFMFRTGKowdd00DE0IzTCEoWs1Il0jL+/GAcQoxUi8i85VYagbZexStaTpsSVgH4NnWTkrx3Wh361qQhUmz7vOYe5ZmaLq5NV8xZ1U3Yydu9PjwQt3HT/j206Jx/2CxZ2yVQqw7sECdy3Vr5SsHLd97pR4hj9s+a6drTTQ2YpdzA2P8b1acjTGfYfv1ZNajOcdl1tPWe7kVjC3gznylWKxuXBcEyNCCJ63DxV8b4QHxLlmDEeb1YXp6fPAfiHsbfK/L+lenikXH3fK/oYaxvjBQqZ0yMpxx+WZXPCbZSd5QHiNfot03LOsrcWqqzC1CUs+4Tml4eiDmGL34U2JPhphJBuKytiFYc2M4a7EzTTMuhYIoSQQGCWRvMtrIMPrSFPEgg/jMv1kFtj1jvrtqT+KIyzx99UPsjilF2aBXehI3Z7Uu7DnPVjTLxpBiZ6eBbbY0bE9Hfdstqtuxlrt5aMqsEvbo6d0B7XFKb06wWrboyIyFmI/dMzentnH0WTGH+3PG/eSzT3RaPVEQs9Wgb0I7LEtfO9pk69r+Wqu7P0JyyQOMf5XLBuUJPphFdiVjg3as0ECObsNu2eg1TVWtX6gpbUuvLWGsq0O1UAXLwG73PFLe36J4WBigEqsZ37D/y+CEhJtwxlOCV8nNVgm+tPhUCNuSc+DhARDQ2+Gu4OB0NF8enDmRBAXU7fnG/FFSl8misRTiRoJ/afCT69m/2rc8c4/vs6+xXq9vuPAmfR4ayB9AJ4BOAG2szx18ZHLqX2N0dBSajxA1us3Ug81ky9TiTCdG9h/6/pDefOi4f7GVUMBynAEjrDfBwATYprb).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 999 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-6)
- [Retribution (optimized)](../research/raid/builds/opt-ret-dps-raid-dps.md) (12/8/31, 995 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003002-503-05225131001230321-6)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 970 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-12 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

