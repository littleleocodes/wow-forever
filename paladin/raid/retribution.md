# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Raid](../research/raid/builds/retribution-open-raid.md)** (16/4/31) — [open the talent tree](https://talentsforever.com/paladin/60/0502510021-4-34232001201301351-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**, **Seal of Righteousness**.

**Talents with no line below:** **Repentance**: taken because Unsealed Wrath requires it.

**Then press the first one that is ready**, top to bottom:

1. **Judgement**; no global cooldown, so press it alongside the others
2. **Hammer of Wrath** when the target is below 20% health
3. **Consecration**
4. **Holy Strike**

Between these, your white swings do the rest.

**Advanced: your cooldowns and extras.** Once the list above feels easy, add these:

- **Seal of the Crusader**: put it up at the start and keep it up
- **Retribution Aura**: put it up at the start and keep it up

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Retribution in a raid twists seals: you swap between **Seal of Righteousness** and **Seal of Command** around every swing so each hit carries both, judge **Seal of Righteousness** on cooldown, and give the remaining global cooldowns to **Consecration**, **Holy Strike** and, under 20% health, **Hammer of Wrath**.

**Why it works**

- Only one seal can be active, so keeping up two seals means a twist: with **Unsealed Wrath**, your swings store a copy of your active seal, and landing a swing under a different seal spends the copies. The full rotation casts **Seal of Righteousness** in the last 0.4 seconds before each swing and **Seal of Command** after the swing, in any global cooldown that **Hammer of Wrath**, **Consecration** and **Holy Strike** do not need: about 14 and 12 times a minute. Opening with **Seal of Command** means your very first swing already carries both.
- Press **Judgement** every time it is ready while **Seal of Righteousness** is up, whether or not the short list shows it. It is off the global cooldown, comes back every 8 seconds with **Improved Judgement**, no longer uses up your seal in Forever, and **Sanctified Judgement** returns 60% of the seal's mana cost; in the simulator the judgement of **Seal of Righteousness** is about an eighth of your damage. If it comes off cooldown while **Seal of Command** is up, judge anyway.
- **Hammer of Wrath** goes first once the boss is below 20% health: it takes 1 second to cast, it comes back every 6 seconds, and at about 500 Holy damage plus a share of your spell damage it is your biggest single hit.
- **Consecration** comes before **Holy Strike** while you have at least a quarter of your mana: on a single boss it deals 312 Holy damage over 8 seconds plus a share of your spell damage, about a sixth of your damage in the simulator, and **Holy Conduit** makes it 40% cheaper.
- **Holy Strike** sits last but is not a real filler: it has a 10-second cooldown, so press it whenever it is ready (20 mana, and **Sacred Arbiter** adds 20% to it). The global cooldowns between your other buttons go to the seal swaps.
- **Seal of Command** is always rank 4: every rank adds the same 70% of weapon damage, rank 4 costs 30 mana less, and the simulator measured it 0.3% better than rank 5. When mana runs low the full rotation steps down: **Seal of Righteousness** rank 7 below half mana, **Seal of Command** rank 2 below 30%, a rank 1 **Consecration** below a quarter, and no seal swaps at all below 15%.

**Caveats**

- The twist rests on the simulator's reading of **Unsealed Wrath**: your swings store up to 3 copies of your active seal for 15 seconds, and landing a swing under a different seal spends them. This rotation dates from before that talent replaced Twist of Light, and the raid runs test it again.
- All those swaps cost mana. The full-raid numbers assume the raid's **Blessing of Wisdom**, Mana Spring and other paladins' judgements of **Seal of Wisdom** and **Seal of the Crusader** on the boss; with only your own buffs the simulator keeps **Seal of Righteousness** up and twists on every swing only while your mana is above about two thirds.
- Forever weakens ranks far below your level, and the simulator applies an assumed formula (TBC's) since 2026-10-09. **Seal of Command** rank 4 and **Seal of Righteousness** rank 7 are close enough to 60 to lose nothing, but rank 1 **Consecration** keeps only a bit over half of its spell damage bonus, so it is a low-mana stopgap only; the game may also lower a low rank's chance to trigger effects, which no simulator models.
- Several targets: only **Consecration** spreads (its bonus damage hits the first four enemies in it); your seals, judgements and **Holy Strike** stay on one target.
- The full rotation also has a **Holy Shock** line (after **Holy Strike**) for builds that take it, worth several percent there in the simulator; this build has no **Holy Shock**, so skip it.

**When to change it**

- If you cannot time your swings (no swing timer, high latency), skip the swaps: keep **Seal of Righteousness** up, judge it on cooldown and press **Consecration** and **Holy Strike**. How much that costs on the current beta build was not measured.
- Against an Undead or Demon boss, add **Exorcism** on cooldown (15 seconds, 40% cheaper with **Holy Conduit**): it hits harder than **Holy Strike**. The simulator's target is an Elemental, so where it fits best was not measured.
- When you have to leave melee range, keep pressing **Judgement** (10 yards) and, under 20%, **Hammer of Wrath** (30 yards); your seals only work on swings.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Holy | 16 | Divine Strength 5, Reverence 2, Improved Seals 5, Holy Conduit 2, Divine Precision 1, Purifying Power 1 |
| Protection | 4 | Divine Intellect 4 |
| Retribution | 31 | Deflection 3, Benediction 4, Improved Judgement 2, Conviction 3, Sanctified Judgement 2, Seal of Command 1, Pursuit of Justice 2, Sacred Arbiter 1, Two-Handed Weapon Specialization 3, Repentance 1, Vengeance 3, Champion of the Light 5, Unsealed Wrath 1 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 817 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever ff9babb (client 70888); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 811 | [16/4/31](https://talentsforever.com/paladin/60/0502510021-4-35233001001301351-12) |
| Phase 1 BiS | 822 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 62.9; Phase 1 BiS 63.1; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Star of Mystaria](https://www.wowhead.com/forever/item=12103) · *Balnazzar, Stratholme* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Dawn Armor](https://www.wowhead.com/forever/item=252483) · *Leatherworking*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Rockfury Bracers](https://www.wowhead.com/forever/item=21186) · *quest: Stalwart's Battlegear*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Stormshroud Gloves](https://www.wowhead.com/forever/item=21278) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* | [Marksman's Girdle](https://www.wowhead.com/forever/item=22232) · *Urok Doomhowl, Blackrock Spire* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Highlander's Lamellar Greaves](https://www.wowhead.com/forever/item=20049) · *sold by Samuel Hawke*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Highlander's Lamellar Greaves](https://www.wowhead.com/forever/item=20049) · *sold by Samuel Hawke*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* | [Hand of Justice](https://www.wowhead.com/forever/item=11815) · *Emperor Dagran Thaurissan, Blackrock Depths* |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFNcZ3n92dvb4X6+9PvgyPhiYbjHY2647M4sr6gJebNpyqdWtUQuVEGXsHXuXrnfcmbULL5Vb0asolfrSQJCJuCTICiGCREJWeCGJQngyCiKRJRJr85IHohA/8LAPUTSzXu8FX4ICynmwjv/z73/5zvm+fxdbCARABAna4AgkYBQmAP4J8BLAZQBa7Zxy9ulWYPeaCB/g2J9QIHMDYtaHbvLeYeTJ7FlAL3lxJiDeFdBL3n6jVvy0Br3k1iUQH9ibyZdBPOdFnnx0xfb88jWwP+0ld8+C+EkN8uQ/DwPIkxdmAugmrxxCnrw5E0AveecSiA9r0IU8uT4TCHYEbifb5v8gPx6I3T8F/wbuRPJ/wD0eOAPCBe1VbXbnFHhPJqcuw6nkHJxI9hCneojCNLde7pTVTkWWVSW8JRzpVCMRWVZkWYnISqRTuc3xWe5BA27GtVkQsXHnYCY5rmV0SbOs5HBaj0vamKkFCQrIh1XZQgnrp6AOa3NCNWJsLJWSTC09rJd4bMTmLDRifczUR6X9upaSjCGp1xgZ0dLxoBc96A5HLPwhbshCC7Iyr/7kcCKjG2NWWresYBV60RNWOjotbMeWLDRjU69mZYqlHR2LD+sjejpT4ko3siDWBKsR54kXPW2EPIhloRb9fca4LmUMaURP6TptZk3ozwmI5MDPpeExzYwzAXlydRKcAOtDLUSgXJeL1eeEOqzdpae041KfdtQwpd5dVpeL9rAobmEqNoeaCFDfGY6g0OYmV2+CHQg52cKG0Bripp55L0fczMFH7lAttuhIU/SwNpr6vTGakVRZ/XFYkcMRpUsaTNiIxiXDlLR4XI9LA8elTEKXTCOjZZJGWrJ0zRxMSG2WrkumngnHR61w4TCcP+w4ahnpdoZONg956wLQX7K92E23V7SN/qAPq87DQve4LicwFPfayEqmrqWS1og0ahoZfdCOzgqQ0lb2fWzKCfVI9yeMsVRcMvUhU7cS0n6jdyHpjQuwklu/40bIu5NA17C6LNRgda+RtvRB02mT1jJ/FhDJz44Z5mDSGhHdodblXij1sSqnOA+5GQvtWval0Ha2GdfmBBEbd2vWEg5OUQK5NwmhwaXfMN3H9uB2+lPcEFy3YigUc0IDrvmNpVeGKAIUuggrcYD+DdhfAcdpZvVs63PCWmwuzVYWChX2I2wJsuWrwtqgH31ZYhcH5P/noHhBoY/5SgY9AvY54Emg/4KV6yqNiH1s3woFBIPSqm0shvvvRCxP9CznRc+IMa4r9FBh0zAFFAM5wY++PpvweZWiftOHVfOkQHWySHpv0IPuad5FC4yxH2+NWSYj9D6wDwAt+seVG7aloQxKu9JKbFe5ivLG1EJj6rdtLE+3ysYmgP0ZI1RZ/ZGV1xWhvyhsnrauihJC8SLP6UH2W9xH9zgC6qGeW9yigDrDoC5Ua4vzgMsmPLoVubVSxJwqz0MhuO3XJpA7sVCyQmJ+xw4820yLcqsGl8OQOvEz5piubljy8kscWldgQolb8xMTii4MIbW+dErnrWqnWl9+Sx50I3Sq24pjgcq0w0FFqBhgilUwl4AldyiW+nduqVlAvwD68JnzvottRd+ssEhVbKeb0XcNigYx1Eh46psumlj+IWGU7XiSnj+g7eifFbDgLOYjCNR3C4j9/e0fMRGYg5OyyoxU7ywFRD+9ztHXOSf7aq0+oRVlpe5g255Sx5fFzlGDUuzyhjLsHFMBu1+zX30DaSsB0/n0AphQAPPDIpiR1cDsWf6MbgptJDytmiqwkTVc4yjhaNV5b8Fia/pn3G14xKl/cbucVR+dBh45dAW/4qpsg2tiKNp85rS93u/+3pCz7nerc5zIS92hG5zrO1mZaGH3XNemK88tz0+cv/0XozsXDNEj9i+s0+D845rrDrnJjaaekh9iMmyFKOyGGByEBIzCMTjGfT0A0xgDAg==); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFNcZ3n92dvb4X6+9PvgyPhiYbjHY2647M4sr6gJebNpyqdWtUQuVUMvYO/YuXe+4M2vLvFRuRa+iIPUlgiATcUmQFUIEiYSskAeSSIQnUBISWSKxNnnIA1GIH3jYhyiaWa/3gi9BAeU8WMf/+fe/fOd837+LLQQCIIIEbXAYEjAKkwD/BngB4BIArXZOOft0K7APmggf4NgECmRuQMz6kCefnQTkyewZQC95/k5AvCugl7z1Wq34aQ16yc2LIN63N1MvgnjWizz56LLt+dUrYH/cS+6eAfGTGuTJmxftOP97EEA3eekQ8uT1OwH0krcvgvigBl3Ik2t3AsGOwK1k2/yf5UcDsXsn4L/AHUv+H7hHA6dBOK+9rM3unAbv8eT0JTiRnINjyR7ilA9RmOHWy52y2qnIsqqEt4QjW9SIKsuKKisRWYl0Krc4Psvdb8DNuDYLIjbuHMwkx7WMLmmWlRxO63FJGzO1IEEB+bAqWyhh/TTUYW1OqEaMjaVSkqmlh/USj43YnIVGrI+Z+qi0X9dSkjEk9RojI1o6HvSiB93hiIU/xg1ZaEFW5tWfHE5kdGPMSuuWFaxCL3rCSkenhe3YkoVmbOrVrEyxtCNj8WF9RE9nSlzpRhbEmmA14jzxoqeNkPuxLNSiv88Y16WMIY3oKV2nzawJ/TkBkRz4pTQ8pplxJiBPrkyBE2B9qIUIlOtysfqcUIe1u/SUdlTq044YptS7y+py0R4WxS1MxeZQEwHqO80RFNrc5MoNsAMhJ1vYEFpD3NQz7+WImzn4yB2qxRYdaYr+URtN/ckYzUiqrP40rMjhiNIlDSZsROOSYUpaPK7HpYGjUiahS6aR0TJJIy1ZumYOJqQ2S9clU8+E46NWuHAYzh92HLGMdDtDJ5uHvHEe6K/ZXuym2yvaRn/Qh1XnYKF7XJcTGIp7bWQlU9dSSWtEGjWNjD5oR2cFSGkr+yE25YR6pPsTxlgqLpn6kKlbCWm/0buQ9Pp5WMmt33Ej5J0poGtYXRZqsLrXSFv6oOm0SWuZPwuI5BcThjmYtEZEd6h1uRdKfazKKc5DbsRCu5Z9KbSdbca1OUHExt2atYSDU5RA3p+C0ODSb5juY3twO/05bgiuWzEUijmhAdf8ztIrQxQBCl2AlThA/wHs74DjNLN6tvU5YS02l2YrC4UK+wm2BNnyVWFt0I++LLGLA/LcWSheUOhjvpJBD4F9AXgc6H9g5bpKI2If27dCAcGgtGobi+FOTsbyRM9yXvSMGOO6Qg8VNg3TQDGQE/zo67MJn1cp6jd9WDVPClQni6T3Bj3onuFdtMAY+/HWmGUyQu8Bew/Qon9ZuWFbGsqgtCutxHaVqyhvTC00pn7XxvJ0q2xsEthfMUKV1R9ZeV0R+qvC5knrqighFC/ynB5kv8d9dI8joB7qucktCqgzDOpCtbY4D7hswqNbkVsrRcyp8hwUgtt+bQK5HQslKyTmD+zA0820KLdqcDkMqRM/Y47p6oYlL7/EoXUFJpS4NT82oejCEFLrS6d03qp2qvXlt+RBN0Knuq04FqhMOxxUhIoBplgFcwlYcodiqf/klpoF9EugD54677vYVvTNCotUxXa6GX1XoWgQQ42Ep76ZoonlHxJG2Y7H6fkj2o7+WQELzmI+gkB9N4HY39/+FROBOTgpq8xI9fZSQPTTaxx9lXOyr9bqY1pRVuoOtu0JdXxZ7Bw1KMUubyjDzjEVsPst+823kLYSMJ1PL4AJBTA/LIIZWQ3MnuXP6KbQRsLTqukCG1nDVY4Sjlad8xYstqZ/zt2Ch5z6N7fLWfXRGeCRQ1fwa67KNrgmh6LNp0/Z693uHww56163OseJvNQdus65vpeViRZ2z3RtuvzM8vzM+dt/IbpzwRA9bP/EOgXOP6657pCbXG/qKfklJsNWiMJuiMFBSMAoTMAE980AIr8DQA==).

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (9/14/28, 652 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05013-053020004-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-13 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at ff9babb (client 1.60.1.70888)). Simulations, not in-game measurements. Do not hand-edit.*

