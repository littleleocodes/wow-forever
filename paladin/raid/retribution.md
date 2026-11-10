# Retribution Paladin — Raid (group)

[Paladin](../README.md) > [Raid (group)](README.md) > Retribution

**✅ Recommended** for raid (the best paladin spec here, or within 3% of it).

**[Retribution — Raid](../research/raid/builds/retribution-open-raid.md)** (16/4/31) — [open the talent tree](https://talentsforever.com/paladin/60/0502510021-4-34232001201301351-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds). A model of the beta, to check at launch.

## How to play

**Keep up all fight:** **Seal of Command**, **Seal of Righteousness**.

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
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 878 |

> Note: Retribution's equal-tier set (raidsim/gear_opt.py, 2026-09-30) is caster gear: the simulator's stat weights value spell damage more than Strength for this spec, and the set leans on Forever launch items (Leafre's Ring of Precise Spell Power, +100 spell damage). In a full raid it also gains from both the physical and the spell buffs, and in Forever Curse of the Elements covers Holy (beta tooltip: 'Magic damage taken'). Check the launch items' availability before trusting the full-raid number.

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 16e8542 (client 70790); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Pre-BiS | 886 | [17/3/31](https://talentsforever.com/paladin/60/0502501022-3-15233001021301351-12) |
| Phase 1 BiS | 900 | [17/3/31](https://talentsforever.com/paladin/60/0502510022-3-25232001021301351-12) (as good as this build in this gear) |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Pre-BiS 61.8; Phase 1 BiS 62.9; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Pre-BiS | Phase 1 BiS |
|---|---|---|
| Head | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Lionheart Helm](https://www.wowhead.com/forever/item=12640) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Neck | [Beads of Ogre Might](https://www.wowhead.com/forever/item=22150) · *quest: Falrin's Vendetta* | [Onyxia Tooth Pendant](https://www.wowhead.com/forever/item=18404) · *quest: For All To See* |
| Shoulders | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* | [Highlander's Lamellar Spaulders](https://www.wowhead.com/forever/item=20058) · *sold by Samuel Hawke* |
| Back | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix*<br>+ [Enchant Cloak - Lesser Agility](https://www.wowhead.com/forever/spell=13364) |
| Chest | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Darkmantle Tunic](https://www.wowhead.com/forever/item=22009) · *quest: Saving the Best for Last*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) | [Wildheart Bracers](https://www.wowhead.com/forever/item=16714) · *Scholomance*<br>+ [Enchant Bracer - Superior Strength](https://www.wowhead.com/forever/spell=19984) |
| Hands | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) | [Storm Gauntlets](https://www.wowhead.com/forever/item=12632) · *Leatherworking*<br>+ [Enchant Gloves - Strength](https://www.wowhead.com/forever/item=273529) |
| Waist | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) | [Titanic Leggings](https://www.wowhead.com/forever/item=22385) · *Blacksmithing*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11645) |
| Feet | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) | [Sorcerer's Boots](https://www.wowhead.com/forever/item=22064) · *quest: Anthion's Parting Words*<br>+ [Enchant Boots - Greater Agility](https://www.wowhead.com/forever/item=16245) |
| Finger | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) | [Band of Earthen Might](https://www.wowhead.com/forever/item=21182) · *quest: Veteran's Battlegear* |
| Finger | [Cutthroat's Signet](https://www.wowhead.com/forever/item=272408) · *sold by Pix Xizzix* | [Warden's Signet of Ferocity](https://www.wowhead.com/forever/item=275981) |
| Trinket | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* | [Adaptive Combat Assistant](https://www.wowhead.com/forever/item=272437) · *sold by Pix Xizzix* |
| Trinket | [Jewel of the Guard Captain](https://www.wowhead.com/forever/item=270225) | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Main hand | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) | [Fist of Cenarius](https://www.wowhead.com/forever/item=21188) · *quest: Champion's Battlegear*<br>+ [Enchant Weapon - Crusader](https://www.wowhead.com/forever/spell=20007) |
| Ranged/relic | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* | [Libram of Law](https://www.wowhead.com/forever/item=272435) · *sold by Pix Xizzix* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Pre-BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsE1ca9j8ej09+x4lzyGVyCDDrJZB419nxeLNis0BMwu5yaVQ3qIVKVcsknsSmjiedcaLwUqWI0osoqH1poRVUQCWUQkGgSigqqoRaifJE1ZaiSLSRq0p9oCrNA1L9UFUzjuMLuRQV1PMwGv/n93/5zvm+X4NNBHwgggQtsBviMAzjAC8DvAtwGoBW2ructbsO2FcNhPdxbAwFMt0nZjzIkwNnAXky9Q6gm7x93Sd+LqCb/PI+iN9VoZtc2wfirSoUyM0+8bgbefL9Ycvx5w/A+rebnD8D4rdVyJPXbvuQJ29dt54f2s/XP/ahm3zyHoi3q9CBPLl43edv811NtMw8K9/ti944BK8Ctz/xBnB3+46CcFI9o05tmgD3wcTEaTiUmIb9iS5ilw8RmORWyu2y0i6HZEUJhoOhdiUclq1fobAcCreHrnJ8hrtVh2txeQZErN/Un06MqmlNUk0zMZjSYpI6Yqh+ggLyQUU2UcLaCajB6qxQiRgdSSYlQ00NakUeq7ExA/VYGzW0YWmHpiYlfUDq1oeG1FTM70YXOoNhE/+OqzLQhKzEqzcxGE9r+oiZ0kzTX4FudAVDbe0mtmJTBhqxoVs104XS9ozEBrUhLZUucqWrmR+r/JWIM8SNrhZCbkUzUI3eHn1Uk9K6NKQlNY02sgb0ZgVEsvN/0uCIasSYgDw5dwzsACsDTUSgXIeD1WaFGqzerCXVvVKPukc3pO7NZoeDdrEI/pMp2BhoIEA9RzmCQouTnLsMViDkZBPrAsuIk7pm3BxxMhsfuU0x2ZwjTdKn1eHkM/pwWlJk5V/BkBwMhzqk/riFaEzSDUmNxbSY1LdXSsc1ydDTajqhpyRTU43+uNRiappkaOlgbNgM5jeDuc22PaaeamVoZ3ORj04CfYRtw066oaxt9Po9WHECZrvHFVmBobjNQlYyNDWZMIekYUNPa/1WdJaHlDazv2JDVqhFuiOujyRjkqENGJoZl3bo3bNJL52Exdx6bTdCPj0GdBmryUAVVnbrKVPrN+w2aTXzZgCR/HdMN/oT5pDoDDQvdEOph1XYxbnI5Whg84I3hbaytbg8K4hYv0U153GwixLIl8cg0D//Habb2VbcQP+Dq/wrFg2FYlaow2WPm1p5iAJAgVOwGAfoi8D2AY7S9NLZVmaF5dhYnK0kFIbYP7DJzxauCqv9XvRkiFUckDePQ+GAAt/w5Qy6A+xHwINAX4HF6yqOiD1s+yIF+P3Skm3MhTs8Hs0RPcO50TWkj2oh+lT+pW4CKPqyghc9PRbhcypFvYYHK2ZInupkjvRuvwudk7yD5hljXd4qo0RG6A1gXwCa9LnFG7akoQRKq9JybJc4itLGlHxjyh9tLEe38sbGgT2PYRpa+pKV1hWm/8+/3G9dZSUEYgWe013sCdxOt9oC6qKuK9ycgNrDoCZQbYlzn8MiPDpDcnO5iNlVnoB8cMuvRSDXooFEmcQ8yXY+2Exzcqv4F8KQ2vHTxoimrJr38IscmhdhQpFb4z0Tis4OIaW2eErnrEq7Ult6Si50IrQr6wtjgcq0zUZFKBtgITNvLgJLbguZygFuvllAfwJ6+4HzvoOtQ8+UMEdVbKVr0XMBCgYxUE946pksmFjuImGEbbyXnn+jreidEjDvLOYiCNRzBQjy5OZLURGYjVNoiRmpXJsPiF56kaPnOTv7Uq3eoxUlpW5k6+9TxxfEzlaDYuxyhhLsbFMeu8fYo79D2orAtP89Cybkwfy6AGZ4KTC7Ft6jawKrCU8rJvJsZHUXOEo4WnHCnbdYmv4DdxXucMoLToe9aiOTwCOHDv+vXIVlcIwPRBqPHrHWZ51/GbDXjU5lmhN5qTNwiXP8KSsdyb891LXm7EPL82/72XsqsmnWENltfWIdAfuHY7oz4CSXGrqKvsRkWAcR2AJR2AVxGIYxGON+GwCA3gNI); Phase 1 BiS: [full raid](https://wowsims.com/forever/paladin/retribution/#eJzEV1tsFNUb3292dvb0224vh16mhwLz3z+FdnXr7Kw1WIEuLSoXG9cSBROjTLvT7uJ2p85sm/JiKsFrEBJ9MKABwyUhFYVATEgjPhBNkCeMiqQJ2qya+IAR+0DiPhgzs93uhV4kQjwPm9nvfPNdfuf8fl8GGwlUgQgSNMNOiMEQjAG8AfAhwEkAWm7vctbuGmDf1RO+imOjKJCpXjHtQZ78fACQJ5MfALrJ+1eqxK8FdJM/PwLxpwp0k8t7QLxegQK51isecSNPfjlgOf7xCVhvu8mZUyD+WIE8+fyEFebtG1XIk0+vWL9737U8vzgB4o0KdCBPzl2p8rVWXYo3T78o3+qNXN0PbwG3N/4OcLd6D4FwTD2lTm4YB/e++PhJ2B+fgr3xTmKXD2GY4JbLbbLSFpRlRQmEAkqbElJkOSgrwZAcDLUFL3F8mrtei6txaRpErNvQl4qPqClNUk0zPpDUopI6bKg+ggLyAUU2UcKacajGyoxQjhgZTiQkQ00OaAUeK7EhDXVYEzG0IWmbpiYkvV/q0gcH1WTU50YXOgMhE+/HFWloRFbk1RMfiKU0fdhMaqbpK0M3ugLB1jYTW7AxDQ1Y36WaqXxpu4ajA9qglkwVuNKVzIcVvnLEaeJGVzMh1yNpqERvtz6iSSldGtQSmkYbWD16MwIi2f6YNDCsGlEmIE9OHwY7wHJ/IxEo1+5gNRmhGis3agl1t9St7tINqWuj2e6gnSyMDzIFG/z1BKjnEEdQaHaS0xfACoScbGKtfwlxUte0myNOZuMjtyomm3WkCfq8OpR4QR9KSYqsPBQIyoFQsF3qi1mIRiXdkNRoVItKvbulVEyTDD2lpuJ6UjI11eiLSc2mpkmGlgpEh8xAbjOQ3WzdZerJFoZ2Nhf57BjQJ9gW7KDrStpGr8+DZUdhpntclhEYilssZCVDUxNxc1AaMvSU1mdFZzlIaRP7P9ZnhBqk22L6cCIqGVq/oZkxaZveNZP0/DFYyK3HdiPky8NAl7DqNFRgeZeeNLU+w26TVjJvGhDJo6O60Rc3B0Wnv2m+G0o9rMwuzkUuRPwb570ptIWtxqUZQcS6Tao5h4NdlEC+PQz+vrnvMN3KNuM6+giu8C1bMBSKGaEWlzxtaqUh8gD5j8NCHKCvAtsDOEJTi2dbnhGWYkNhtqJQGGQPYKOPzV8VVvq86EkTqzgg7x2B/AH5f+BLGXQT2G+A+4C+CQvXVRgRu9nWBQrw+aRF25gNd2AskiV6mnOja1Af0YL0udxD7ThQrMoIXvR0W4TPqhT1Gh4smyY5qpNZ0rt9LnRO8A6aY4x1eSuMIhmhV4F9A2jSlxZu2JKGIiitSkuxXeQoihtTco0p/7axLN1KGxsD9jKGaHDxS1ZcV4g+nnu407pKSvBH8zynO9gzuJVutgXURV0XuVkBtYdBtb/SEudeh0V4dAblplIRs6s8Crngll+zQC5H/PESiXmWbb+7mWblVvHNhyG146eMYU1ZMefhFzg0LcCEAreG2yYUnRlCSk3hlM5alTalpviUXOhEaFPW5scClWmrjYpQMsCCZs5cAJbcGjSV17i5ZgH9HeiNu877drYGPZPCLFWxha5Gz1nIG0R/HeGpZyJvYtmLhGG2/nZ63kdb0DspYM5ZzEYQqOciEOTJtdcjIjAbp+AiM1K5PBcQPfQcR89wdvbFWr1NK4pKXc/W3qGOz4udrQaF2GUNRdjZphx2T7En/4G0FYBpvz0DJuTA/D4PZmgxMDvn36Or/CsJT8vGc2xktWc5SjhadtSds1ia/it3CW5yyitOh71qwhPAI4cO319cmWVwjPWHGw4dtNZXHf/rt9fVDmWKE3mpw3+ec/wnKxXOPd3Tterje5bnYfu353h4w4whvNP6xDoI9h/HVIffSc7XdxZ8icmwBsKwCSKwA2IwBKMwyv09ACgbAyw=).

**Points that do nothing for this spec:** **Repentance** (1) only counts toward the points the tree needs before **Champion of the Light** and **Unsealed Wrath**.

## Other builds of this spec

- [Retribution — Raid](../research/raid/builds/retribution-ml-raid.md) (9/14/28, 698 DPS in a full raid) — [open the talent tree](https://talentsforever.com/paladin/60/05013-053020004-1523330100130033-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-10 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 16e8542 (client 1.60.1.70790)). Simulations, not in-game measurements. Do not hand-edit.*

