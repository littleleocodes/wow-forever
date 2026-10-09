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

**The gear** (average item level: Pre-BiS 61.8; Phase 1 BiS 66.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking* | [Black Dragonscale Helm](https://www.wowhead.com/forever/item=252605) · *Leatherworking* |
| Neck | [Nacreous Shell Necklace](https://www.wowhead.com/forever/item=22403) · *Cannon Master Willey, Stratholme* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) | [Rugged Mantle of the Timbermaw](https://www.wowhead.com/forever/item=227808) |
| Back | [Hide of the Wild](https://www.wowhead.com/forever/item=18510) · *Leatherworking* | [Sapphiron Drape](https://www.wowhead.com/forever/item=17078) · *Onyxia, Onyxia's Lair* |
| Chest | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973) | [Soulforge Breastplate](https://www.wowhead.com/forever/item=226973) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) |
| Hands | [Gloves of Earthen Power](https://www.wowhead.com/forever/item=21178) | [Gloves of the Hypnotic Flame](https://www.wowhead.com/forever/item=18808) · *Molten Core* |
| Waist | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) | [Knowledge of the Timbermaw](https://www.wowhead.com/forever/item=228190) |
| Legs | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking* | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking* |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) |
| Finger | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) | [Leafre's Ring of Precise Spell Power](https://www.wowhead.com/forever/item=276765) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Band of Sulfuras](https://www.wowhead.com/forever/item=19138) · *Ragnaros, Molten Core* |
| Trinket | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) | [Blackhand's Breadth](https://www.wowhead.com/forever/item=13965) |
| Trinket | [Rune of the Guard Captain](https://www.wowhead.com/forever/item=19120) | [Frozen Heart of the Mountain](https://www.wowhead.com/forever/item=249469) · *Enchanting* |
| Main hand | [The Unstoppable Force](https://www.wowhead.com/forever/item=19323) | [Bonereaver's Edge](https://www.wowhead.com/forever/item=17076) · *Ragnaros, Molten Core* |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzMVU9oE08U3je7SSav/dH8ppamq8JaqcTAltmN0aaXpAXRYwUPnjSbJjVbaxOSHOrJihVFVIpgsYUWIYhVKi3+gRLspaCkEKUXPYiKePKgUCoEwYMySf/Rm9CA77D77feGne/N95iH9RQ84AUNfMCB7d/4Ihw6IAI9cAqikIQ0DANcAxgFUH9SqniIGkWFLjxvQIVengVU6Ocf/6FC34wKPPld4MX7Ahcqz09lwbx6JtbPzQhmctWDMv1toUxvnhfsHcH+GgOUUKFPlz2tBh2xPUXbe8P2rZ7j5dh1ICP2bSDl2F3IW/dgxpqG913z8GgaigDLcMvuxs1yCmS3GeQ8oAd5QOdB0wyaAYNzIxDgAdMoEuULGXNhM6JK0elz0Pk8tLrRhQ7daA9mWb1aTch0dgHYA2CnrfTAmVQ6p5ncPKzzkG52dGq9SWvwbCKupTKaFY8n4lrsgpZLJrRMKmfl7NSglk1Ymd6k5ssmElomkdPj6ay+ntSryfb+bGrwoHoUQ+wI/u9voE5GYpLqQgfKRrANm/yNVGaORUIoEZJQMdoPZbHuCWwIF7SP0pdTwBSVdEqsSW1E9wQ4UaGzU6CuvdnAtioMrnNzR6tYP80XeWB2zXdzqQ6UPeUYu1p7f9qwxd9MFVZX2HLuTlSQGNnNFmLH/sZIvsXIin1bfnSx5hXt3S4yyNvWBAj76lS3oH2Ufuxh/dvUiM4xdlQNrXTpYh688ldShBViXpKlSuyKFEBBglLrQ9ktCGm4L9IyMS5iKbyvrxLvwuYK8bq0sL9IpH8qcpF1VNM48HjH9wm9LpVK9dG5SNcaEYmKITAOdmrlytLJt+FQhZWWw11iZan0LXyiCj6E/TKdb+7es3kfVwfK8cpISUIahmCI/RkAII1k7Q==) · [training dummy](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzMk99LFF8Yxuecmd09++oX93tM1LmISVK2hZEzZ5tFvdld6Q8o6Fqddcd2zHaWnbmouySDiIqIihSUYCksDKUfIEveCMUKa3lTF1ESXXVRIAbedFGcVcu81ui5mHl43hfez7xzDkhUUlcJUSJYHQCFLDxrAIVcmEWgkI/f/gOFvLou/ORX4RfvCV+uPVc3RPLyqeifmxHJ5HoEZPLDAplcPSPSWyL9fhuBBAp5shJpM8iYE6k4LVec6PpptpG5jPCYcwPhjcwdVLLuohlrGr1Lz6OH06iC0Aq65vTiCCrjg9xkLM4Y100W15nJuWnEDcYMHmdxblSw8gmPhqAZQCUQjAbIfAm1hSEEAd3oND06TPuswki/W/A1znhCN5jOjB5tMGflT9lZzS1qVjZrZ7XMOc3P2VrR9S3fcfOaZ1vFwZwW9WxbK9q+ni14etH1Ld9x87pnW8XBXOew5+aPqEQNgkIWS4jeRLTPKoz0uwVf44wndIPpjO/pMA4d9DA0xRqJTAOLGBMsPhsU1nnUg7rH6NcORBwl5MUUooqKeyTapDZCeAIJ1tkppG696f39Zz4GXTQBrbFmotC68g7EICiADe/PUo1Z4AHm3u9/Skv7D5oGk8bh/1gDCVKckdQQBEA2zPbtxdbQdtcTZvsOynp18xzKZHYB0To1LJqihHw4Tkd28bNunXftKf/2FXheQn9tGiLLr1GL/BlX0Brmo7JU04FUGSmAQWp7IIdFIJ0fSrVOjAstJQ8N1fQ2yddwS0hLxipY+qfkp7bdvqrj0Z7P6V6uVqv1A3Op9FaQGkCXEBpHjrt2cenkm2R3LZVWkmnRWa1+SZ7YNO+TMZnMN/dKZ+nPAQBPBVoX); Phase 1 BiS: [full raid](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzMVU1oE1sUnnNnktyc9tG821eaznsPxkolBqbcmRhtuklaEF1WcOFKO2lSM7U2IcmirqzQooiKFBRbbBGCWKXSolVKsZuCkkKEbnQhKuLKhUKpEHShyJ30j+6EBjybOfN9h7nfud9hDtZS8IEfNAgAB7Z3841waIMYdMEJ6IYUZGAI4BLAdQD1O6WKj6gWKnTxSR0q9OcooEI/fP0LFfp0ROQTX0S+dFfk3xz2fVkgL+ZE/ey0QCbWfKLmBqBMr55Fhf64Lci5EUAJFfp4xdds0GHbV7T9V+zA2hlejl8GMmyPAinHb0HBugPT1hS86ZiHB1NQBFiBa3YnbvWzQP41wpyH9DAP6TxsmuFQyODcCIV4yDSKRPlIbnqwEVGl6A646HwBmr3oQZdutIZzrFatEDKdWQR2D9hJK9N/Kp3JayY3D+o8optt7VpPyho4nUxo6axmJRLJhBY/p+VTSS2bzlt5Oz2g5ZJWtielBXLJpJZN5vVEJqdvkHqFbO3LpQf2q4cxwg7h38E66mYkLqkedKFshFuwIVhPZeZaIoQSIQkVo/VADmsewaZwAQcofT4JTFFJu8Qa1Hr0joMbFTozCer6k/Xv6MLgOjd3tYuN23xWAGZX/TSP6kLZV46zi9X3pwWbgo1UYTUL2+7djQoSI7c1QuzI7xjJtxnp2LftQ+er3tH/O0WGecu6AGFfjeoVcIDSd12sb4caMTnGrqqhzpQuFcAvfyJFWCXmBVly4p/YAihIUGq+L3sFIA31xprGx0QsR/f0OvE6aq4Sv0eLBotE+qMiH9vIqhr7Hu76OZGXpVKptns21rEOxLrFFhgDO706snz8VTTioNJKtENUlkqfo8cqydtoUKbzjZ3/bf2PKxvlqLNTUpCBQRhkvwYA01RlWA==) · [training dummy](https://elliotwood.github.io/Forever/forever/paladin/retribution/#eJzMk89LG2kYx+d5Z5K8eXQx+7qizmGZlVWygZF3JjtBvSSR/QN2Yc/qxIybcd1MyMxh97aCQiltD9JClSqF0GKLRWltEakXoSVCpF7aQ+kveuqhBbEgvbSUN2prPWvp9zJfvs8Xns+8My9KTFKfU6rEiGqjQtduN6FCP0wBKvTF2+9QoXcmhZ99I/z6FeHf1afPdkVyf1n0lxZEMrsTE50LgDI9+w8q9P0lMVyeBJRQobe2Yh0GnXBjVbftjBvf+Zvv5k4DmXCngOzmLkLFvgwL9jw8zq7A9XmoAmzBObefxGCV/GhanCc5N3SLJ3VumaZlJA3OjWSSJ02jSpSXZDyCrYgqxXA8RFcq0BHFCIZ0o9vy2SgbsEtjg14p0ExupnSD69zo04YLdvEvJ695Zc3O5528lvtPCwqOVvYCO3C9ouY7dnm4oMV9x9HKTqDnS75e9gI7cL2i7jt2ebjQPep7xV9UqoZRoesVYOeBDdilsUGvFGgmN1O6wXVuHusyE7vYz9iSaKYyC60TQol4bVR4968+NtyET2cg4jil9+aAKSrpk1iL2ozRGRCsi3Og7j/Z1ZNn/g17WArbE61UYQ2rhxDDqCAx/C9HdWaBh8T0P39TVjl50CxaLInfJ5pomJGcpEYwhLJhdR4cbB3t6DxldR6ibFT3/kOZLq4Ba1CjohSn9OnvbOwIP+/VzZ5j5T+4Ancr8NW2Ad18AG3yK1KFbWKOy1JdP2RWQUGCUsc1OSoC6f+RTPvMtNBG+qeRuh6lzW3SFtHSiSqRvikFmQN3ouq6cex7ejdrtVrj0FImux9khuAUwDS43vbkxp8P0731VNpKZ0WzVnud/mPPPEknZLrS2i/9yz4OAOWVWoI=).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 999 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-6)
- [Two-handed Retribution](../research/raid/builds/opt-ret-dps-raid-dps.md) (12/8/31, 995 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003002-503-05225131001230321-6)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 970 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-6)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-09 from this project's builds and simulations of the WoW: Forever beta (client build 1.60.1.70291). Simulations, not in-game measurements. Do not hand-edit.*

