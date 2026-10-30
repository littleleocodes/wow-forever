# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution (optimized)](../research/raid/builds/opt-ret-dps-raid-dps.md)** (17/0/34) — [open the talent tree](https://talentsforever.com/paladin/60/55003003001--05225331001330321-7)

## How to play

**Before the pull:** **Seal of Command**.

**Keep up all fight:** **Seal of Righteousness**, **Concentration Aura**.

**Then press the first one that is ready**, top to bottom:

1. **Holy Strike**
2. **Hammer of Wrath** when the target is below 20% health
3. **Judgement** when Seal of Righteousness is active
4. **Consecration** when you have at least 25% mana

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

*This guide was written for the rotation of 2026-10-15; the list above was re-tuned since, so follow the list where the two differ.*

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 785 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 30f67f5 (client 70450); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 771 | this build |
| Phase 1 BiS | 790 | [9/8/34](https://talentsforever.com/paladin/60/51003-503-05225331001330321-7) |

**The gear** (average item level: Pre-BiS 62.8; Phase 1 BiS 65.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Stalwart Helm](https://www.wowhead.com/forever/item=250599) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Hermit's Pauldron](https://www.wowhead.com/forever/item=275737) | [Theramore Shoulderguards](https://www.wowhead.com/forever/item=272957) |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411)<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Earthpower Vest](https://www.wowhead.com/forever/item=21183)<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186)<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Soulforge Gauntlets](https://www.wowhead.com/forever/item=22090)<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of Preserved Heads](https://www.wowhead.com/forever/item=20216) | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Ironfeather Leggings](https://www.wowhead.com/forever/item=252486) · *Leatherworking*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064)<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Don Julio's Band](https://www.wowhead.com/forever/item=19325) | [Channeler's Ring](https://www.wowhead.com/forever/item=272406) |
| Finger | [Band of the Better Half](https://www.wowhead.com/forever/item=284716) | [Signet Ring of the Bronze Dragonflight](https://www.wowhead.com/forever/item=21210) |
| Trinket | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) |
| Trinket | [Shard of the Splithooves](https://www.wowhead.com/forever/item=10659) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188)<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) | [Libram of Law](https://www.wowhead.com/forever/item=272435) |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzsWF9oHEUYv29uczv5UtLraMn2tGUMnF6u2WN2t1tjRHLpk+hLqC8+afd6e72N5+2xuyfJW4UiIqWID0Iixj9noLSpLRY0BH0wtBAfSuODRYRiqA8W8cH6UBRRZDeX9EgqetAgDfdx3O3NfDvz+37zm+8bBh+mkAQFOGTgCJShBscBXgd4H+A0ANsR9ZKwdwhSH+ylUpKkJlCmP87uVG70oERfOwco0amfkijTd5aTytcJlOnvZ0H5oRdlujgLyvVeTNBvC8p7Mkr0t3cBZXrrYwjflumFOVC+70WJ/vl2OMzchV0o0U+XkxinjedQppdmQfm5F2Mo0YvLyf5ccsnJ/PqSuF0Yu3YK3gBywnkLyO3CNCQa1pz13egZkE86Z07DKWcFTjiHdtwJLg8LZJ9pCmFEH01VhanrpmFoQmiGIQxdWyLSDTL7EPYhpigmMl10vgH93Shjl6rlTJ9dBfYl+LZdtItcF/pBVROqMHnJc1/mvm1VVLeklurepOpZTvExn4c/3HMDK3DcKs8EZZu7Nbsa+npHy9yz1aBetYvcCbhb5RY/bAeeU6hH3oW6UykODPP9Wm4ozQOX79dzWpqXXI/br9je5GZn7oRjlOqVyurEGU0MCiF4yTlWDvxBHgLnmjGQ6k7J2JWh9PoYW94eEa2uV5ye/wLYH4SdJfd9SE9yq1Z50a0FLTEM86Nlq3rMLnLX41YxVGFhkoeA1+E3QWd8294crLrmpq665cZ9tzqQehZH2FO4K7uTJhgpxEJxYFwz07g7+wCNs65FQigJCUZJ5A74kWf8jqcp0mFnRqaXZoDd7LDfHvtDOMiy/5398ClD6eUZYJc7VLdH9W7s+QTW+UslUKLnZ4Bd6fDYHo97N8pVN9PNgvl5A9g4e2EjFO1Am1A8O1CLNf8fANBo7RYbwJa2R/0iwzF2qyPD9mQ4iiYz7pY5W3f5xmplNKsVoRcbwN6EzVoVj99Treawn/F/QxlBkuhnDWAn7wJJP3hPIWWRs33YPQ3NDLiG7pl1jvz15LitDohAr1wF9k1no7W30dK4J9tHJdaz0KLYBEpItNbzyPiWC3c17384DUr8JlmCX4j+ajwW2YP5BZCQYKz/L9IdNsSOl/J7pqdC+2rkkVJk10b0FaJIfCQ7T2L/iwX5tacttUfPbdk8T0Tfhz/KjzYb8kfC64IpiP7EVkaycTrfd6jlVkHAEOThaRiD56EMNZiACfL3APDLiGo=); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzsWEFoHFUY3v/tZOflT0nXpyXTrZVnYHWzzSxvZjo1RiSbnkQvoSdP2tnubHfiurPMzErjqUIOIqVKBaERYnFdKDVSsaIhWMTQShRKI2gPhWKoiD14UA+9CEVmskmXpKILDWLY/7D777xvZ77/m+/9/zD4MIUkKMAhA4ehDDU4DvA6wBmAswBsR7RKwtURSJ3ZS6UkSb2KMv2luVO52YcSvXMKUKIXv0+iTN9dTirfJVCmXzZB+akfZbrYBOVGmHw7B8p7Mkr05zcBZfr1p9HfZfrxHCg/9qNE31lOokSvN8OzfRbl02+HyEtNUH7txxhK9MJycjCXXHIyf7wkbhcmrp2EN4BMO6eA3C7MQKJhzVnXx8+BfMI5dxZOOisw7Rzccbe8PCyQPaYmhKGawlCFqeumYWhCaIYhDF1bItJN0tyDA4gpiolMD51vwGAvytijajnTZ1eBfQW+bRftIteFfkDVhCpMXvLcl7lvWxXVLamlujelepZTfNzn4Rf33MAKHLfKM0HZ5m7NroZY70iZe7Ya1Kt2kTsBd6vc4ofswHMK9QhdqDuV4tAo36flRtI8cPk+Paelecn1uP2K7U1tBnMnPEepXqmsXjijiWEhBC85R8uBP8xD4lwzhlK9KRl7MpTemGDL26Oi1fsVp+cvAvuTsA/J/76kp7hVq7zo1oK2Gkb5kbJVPWoXuetxqxi6sDDFQ8Lr9FukM75tby5WXYOpq7DcpO9Wh1LP4Rh7Gh/I7qQJRgqx0BwY18w07so+SOOsZ5EQSkKBURK5/X6EjN9FmiIdLmZkemkW2K2u+p2pP4LDLPvv1Q+zDKWXZ4Fd7krdmdS7sO8TWNcvlUCJnp8FdqWrY2c67t1oV91MtwbmFw1gk+yFjVS0/R1S8exALdb8vyFAo3u32AC2tD3mFxmNsd+7NuzMhuNoMuNenbN9l2+cVkZrWhF6oQHsLdjsVfHEffVqDgcZ/yeWESWJft4AduIelPQD95VSFjl7BHtnoNUB19g9u66Rv94ct9UDItArV4H90N1onW20NO7ODlCJ9S20OTaBEhKt/XlkcsuNu9r3358BJX6LLMFvRH8tHoviofwCSEgwNniH9IYHYsdL+d0zp8P4ZuzRUhTXxvQVokh8LDtPYv9JBPm1bEvjsY+27DpPRp+HPsiPtw7kD4dvC05D9CO2MpaN0/mBg20vFQSMQB6egQl4HspQg2NwjPw1ADRKiCE=).

## Other builds of this spec

- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-raid-dps.md) (17/0/34, 784 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/550030030001--05225331001330321-7)
- [Retribution — Seal of Command / Twist of Light](../research/raid/builds/ret-full-buffs-raid.md) (10/8/33, 778 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/52003-503-05225231001330321-7)
- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (11/8/32, 770 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/25003001-503-05225131001330321-7)

---
*Generated by `_reference/data/render_modes.py` on 2026-10-30 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70425; raid numbers: the official wowsims/forever simulator at 30f67f5 (client 1.60.1.70450)). Simulations, not in-game measurements. Do not hand-edit.*

