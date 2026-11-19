# Smite Priest — Raid (group)

[Priest](../README.md) > [Raid (group)](README.md) > Smite

*Damage from Smite and Holy Fire, carried by Discipline talents.* (a hybrid: Discipline/Holy).

**[Smite — Raid](../research/raid/builds/smite-open-raid.md)** (17/17/17) — [open the talent tree](https://talentsforever.com/priest/60/50203003103-00515121002-502520010002-12)

> 🔬 Derived build: found by this project's open talent search (every legal build, no tree rule, in the community's raid simulator in a full raid, raced against the rotation's builds); it beat the hand-made build (Discipline/Holy — Smite), which stays below as the alternative. A model of the beta, to check at launch.

## How to play

**Before the pull:** **Holy Fire**.

**Talents with no line below:** **Holy Nova**: a defensive or healing spell: cast it when you need it, it is not part of the damage rotation.

**Then press the first one that is ready**, top to bottom:

1. **Shadow Word: Pain**: keep it on the target, until the last 10 seconds of the fight
2. **Mind Blast**
3. **Inner Focus**, then straight away **Devouring Plague**; no global cooldown, so press it alongside the others
4. **Holy Fire**: keep it on the target, when you have at least 40% mana
5. **Inner Focus**, then straight away **Smite**; no global cooldown, so press it alongside the others
6. **Shadow Word: Death** (rank 3)
7. **Smite** when you have at least 25% mana
8. **Smite** when you have at least 20% mana

*The simulator's full rotation for this build, with every condition: [research rotation page](../research/raid/rotation.md).*

## Why this rotation

Smite in a raid keeps **Shadow Word: Pain** on the boss, fires **Mind Blast** every time it is ready, keeps **Holy Fire** burning while your mana holds, casts **Shadow Word: Death** on cooldown and **Smite** in every gap. **Power in Light** is the tree's reason: your **Smite** deals 10% more while your **Holy Fire** or **Shadow Word: Pain** is on the target. 602 DPS in a full raid against the Shadow page's 788.

**Why it works**

- **Shadow Word: Pain** (8 casts, 19%) comes first: instant, 762 damage over 24 seconds with **Improved Shadow Word: Pain**, and the cheapest way to keep **Power in Light** on. Recast it when it falls off, not in the last 10 seconds.
- **Mind Blast** whenever it is ready (22 casts, 19%): 477-503 damage in a 1.5-second cast every 5.5 seconds with **Improved Mind Blast**. It costs more than a **Smite** but lands far more per cast; **Shadow Focus** gives it hit.
- **Inner Focus** goes into **Devouring Plague** at the pull: the plague is free that once (985 mana otherwise, which this build cannot halve) and runs 24 seconds. In a longer fight the second **Inner Focus** goes into a **Smite** for its 25% crit bonus.
- **Holy Fire** (6 casts, 8%): 184-232 damage plus 75 over 10 seconds in a 3-second cast with **Divine Fury**; one goes out 3 seconds before the pull, and the list recasts it as its burn ends while you have at least 40% mana. **Searing Light** adds 5% Holy damage, **Holy Specialization** 5% crit, **Holy Precision** 18% hit.
- **Shadow Word: Death** (10 casts, 8%) on its 18-second cooldown: the list casts rank 3 (the search measured it 0.5% ahead of rank 4: less mana for nearly the same hit).
- **Smite** is the filler (60 casts, 45%): 2 seconds with **Divine Fury**, 280 mana less **Mental Agility**'s 10%, 10% more under your **Shadow Word: Pain** or **Holy Fire**. The page's two **Smite** lines are mana gates: top rank above 25% mana; between 20 and 25% the full list drops to rank 2, under 20% to rank 7, and only when you cannot afford even that does it channel **Mind Flay** (no casts in the simulator's raid fights).
- Mana: **Meditation** keeps half your regeneration going while you cast; the simulator's priest also uses two mana potions and two Demonic Runes a fight and still runs dry late. In a 6-minute fight its DPS falls from 602 to 280.

**Caveats**

- This build has no **Penance** (it needs 20 Discipline points) and no **Power Infusion** or **Shadowform**: the full list's lines for them never fire. The Smite page is a showcase for the tree, 24% behind Shadow.
- **Shadow Word: Death** hits you for 30% of your maximum health each time the boss survives it, about 10 times a fight: your healers pay for that.
- When you must move, use the instants: **Shadow Word: Death**, and **Shadow Word: Pain** if it fell off. **Holy Fire**, **Smite** and **Mind Blast** all need you to stand still.
- Ranks far below your level get much less from your spell power (a Forever change; our model gives rank 2 a small share of it), so the rank-2 **Smite** line is a stopgap, not a mana trick to use early.

**When to change it**

- When the boss has under 3 seconds to live, cast **Smite** rather than a new **Holy Fire**: only a spell that finishes casting does damage.
- If healing is tight, cast **Shadow Word: Death** only in the last 20% of the boss's health, as the simulator's rotation for fighting alone does.
- Packs: **Holy Nova** hits everything within 10 yards and heals your party, and **Searing Light** gives each **Holy Fire** tick a 10% chance to make your next **Holy Nova** cost no mana.

## Talents

| Tree | Points | Talents (ranks) |
|---|---|---|
| Discipline | 17 | Power in Light 5, Twin Disciplines 2, Holy Precision 3, Mental Agility 3, Inner Focus 1, Meditation 3 |
| Holy | 17 | Holy Specialization 5, Divine Fury 5, Holy Nova 1, Blessed Recovery 2, Inspiration 1, Searing Light 2, Spell Warding 1 |
| Shadow | 17 | Shadow Focus 5, Improved Mind Blast 5, Improved Shadow Word: Pain 2, Mind Flay 1, Shadow Weaving 2, Spirit Tap 2 |

## The numbers

| Setting | DPS |
|---|---|
| Full raid, 3-minute fight (every raid buff and debuff: what this page ranks on) | 605 |

**By gear tier** (the spec's best talents for each tier and setting in its own gear, found by this project's machine-learning search in the community simulator, wowsims/forever 2e6e77d (client 70938); [every spec](../../_reference/dps-rankings.md)):

| Gear | Full raid DPS | Best talents |
|---|---|---|
| Quests and dungeons | 568 | [17/17/17](https://talentsforever.com/priest/60/50203003103-10505121002-500520012002-12) |
| Pre-BiS | 602 | this build |
| Raid BiS | 625 | this build |

*Each row is in that tier's own gear set; the DPS at the top of the page is this build in the standard set, so the two do not match.*

**The gear** (average item level: Quests and dungeons 61.0; Pre-BiS 61.8; Raid BiS 63.6; each item opens its Wowhead page, with where it drops and its enchant):

| Slot | Quests and dungeons | Pre-BiS | Raid BiS |
|---|---|---|---|
| Head | [Crimson Felt Hat](https://www.wowhead.com/forever/item=18727) · *Magistrate Barthilas, Stratholme*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Spellweaver's Turban](https://www.wowhead.com/forever/item=22267) · *General Drakkisath, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Neck | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Orb of the Darkmoon](https://www.wowhead.com/forever/item=19426) · *quest: 1200 Tickets - Orb of the Darkmoon* | [Choker of the Fire Lord](https://www.wowhead.com/forever/item=18814) · *Ragnaros, Molten Core* |
| Shoulders | [Thuzadin Mantle](https://www.wowhead.com/forever/item=22412) · *Baron Rivendare, Stratholme* | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* | [Argent Shoulders](https://www.wowhead.com/forever/item=19059) · *Tailoring* |
| Back | [Amplifying Cloak](https://www.wowhead.com/forever/item=18350) · *Magister Kalendris, Dire Maul* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* | [Arcanoweave Cloak](https://www.wowhead.com/forever/item=272411) · *sold by Pix Xizzix* |
| Chest | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) | [Robe of Everlasting Night](https://www.wowhead.com/forever/item=18385) · *Immol'thar, Dire Maul*<br>+ [Enchant Chest - Greater Stats](https://www.wowhead.com/forever/spell=19988) |
| Wrist | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) | [Sublime Wristguards](https://www.wowhead.com/forever/item=18497) · *Guard Mol'dar, Dire Maul*<br>+ [Enchant Bracer - Greater Intellect](https://www.wowhead.com/forever/spell=13825) |
| Hands | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* | [Hands of Power](https://www.wowhead.com/forever/item=13253) · *Quartermaster Zigris, Blackrock Spire* |
| Waist | [Highlander's Cloth Girdle](https://www.wowhead.com/forever/item=20047) · *sold by Samuel Hawke* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* | [Belt of the Archmage](https://www.wowhead.com/forever/item=18405) · *Tailoring* |
| Legs | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Skyshroud Leggings](https://www.wowhead.com/forever/item=13170) · *Highlord Omokk, Blackrock Spire*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) | [Flarecore Leggings](https://www.wowhead.com/forever/item=19165) · *Tailoring*<br>+ [Lesser Arcane Amalgamation](https://www.wowhead.com/forever/item=11648) |
| Feet | [Omnicast Boots](https://www.wowhead.com/forever/item=11822) · *Golem Lord Argelmach, Blackrock Depths*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Venomspew Footpads](https://www.wowhead.com/forever/item=275606) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) | [Venomspew Footpads](https://www.wowhead.com/forever/item=275606) · *Tailoring*<br>+ [Enchant Boots - Minor Speed](https://www.wowhead.com/forever/spell=13889) |
| Finger | [Songstone of Ironforge](https://www.wowhead.com/forever/item=12543) · *quest: The Princess's Surprise* | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* | [Ring of Spell Power](https://www.wowhead.com/forever/item=19147) · *Lucifron, Molten Core* |
| Finger | [Eye of Orgrimmar](https://www.wowhead.com/forever/item=12545) · *quest: The Princess Saved?* | [Warden's Signet of Brilliance](https://www.wowhead.com/forever/item=275982) | [Elemental Focus Band](https://www.wowhead.com/forever/item=20682) · *Prince Skaldrenox, Silithus* |
| Trinket | [Eye of the Beast](https://www.wowhead.com/forever/item=13968) · *quest: For The Horde!* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* | [Talisman of Ephemeral Power](https://www.wowhead.com/forever/item=18820) · *Magmadar, Molten Core* |
| Trinket | [Royal Seal of Eldre'Thalas](https://www.wowhead.com/forever/item=18469) · *quest: Holy Bologna: What the Light Won't Tell You* | [Briarwood Reed](https://www.wowhead.com/forever/item=12930) · *Jed Runewatcher, Blackrock Spire* | [Weakness Analyzer](https://www.wowhead.com/forever/item=272438) · *sold by Pix Xizzix* |
| Main hand | [Witchblade](https://www.wowhead.com/forever/item=13964) · *Darkmaster Gandling, Scholomance*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) | [Sageclaw](https://www.wowhead.com/forever/item=20070) · *sold by Samuel Hawke*<br>+ [Enchant Weapon - Spell Power](https://www.wowhead.com/forever/spell=22747) |
| Off hand | [Spirit of Aquementas](https://www.wowhead.com/forever/item=11904) · *quest: It's Dangerous to Go Alone* | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) | [Obsidian Bauble](https://www.wowhead.com/forever/item=18316) |
| Ranged/relic | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* | [Bonecreeper Stylus](https://www.wowhead.com/forever/item=13938) · *Darkmaster Gandling, Scholomance* |

**Open in the simulator** (the community's Forever simulator on the web, loaded with the gear, enchants, talents, rotation, consumables and buffs we simulate): Quests and dungeons: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk+IG1UYn+/NJPPlyxrjs3anQ5FprBIjE9+8bGS3HpL2VApqEQY8KG7SZJvUzR92Aq56SaEHkZoNOSgtlYooFcHqxWXxposQQdz1ogcvy4roUfewexBUJn9Wye4xm36HN2/eN4/f7/t9v3k8OokQBQMsiMM8lKAOTYA3Ad4H+BiAT/WyzM/OgvlTBDEaMGuk450OGL+GScPtd4E0vP6ZP95dAdLxhxUwfomQjl+1wfg5Qip+c5k03LgFFMSdBX9bEO++aKzopOI/OVLxap5UbFdIw4/a/kfXK0b3QVKx+RKpuLMYeyLaLce/b4HYzV98+wN4C9i1cgfYbv4msN/OfgL6nVvw+flWeQuulc9hjzJk4Ut2Oi2kSAmRckTKdkRapB3pCCHttBBpKYQjhZBdBpssvM22p+gYhUydAnHE916N6RQg1U55vAN8PldffLlWb1hSyKdsMWfL2TPWpVKuerlYsGpLVq5QKBas/GtWo1S0lmqNXKNcq1peMbd0qWTFvWLR8irlRtEu1D17mLb76eQVr1Z93EzSI/wU3RcLU0j2KbRciiYiGOTsgmIGSSPmiAG7lssrE+DUFyOE6y5/YwJw0/Ih0s0AqXjbIzKRgvEgbr4DXDPZGYXfHm2DI2w5N2YOT5PgSTqRmEaVh64MveBzIU0k0x49kLjfb0le8bUhdUY8uu8YbpjH5bH/Shh6adXl1QnI11dMxfW95/grB6US48br1/nds7w5icacHFVepofKr7rcMZ+k0zw2+v+MbEntN6vlTpj1hQEFR3j+JM5wQ+MPH1LVPsVVl4fNvoV0/MLlixNoKfrnDLb/euZQAzljRusb6M/lg2COLVJHARbdzfPXD1bmzIwZ7DhNxYhQ+mrudcAcPA31d9aFP5i8qiq9mMl+DZrJSIn9zUL+gtJcyJ64ecOPbzOnFnrxY0ZuMUOzMok1ptyTaGSHsyONxz49Mpy53vj8h9mzg4XsvH/JuQG9F2Urk1Bxbfrc/+5CAmYhC+fhIrwAJajDMiyzfwcA5YQvww==); Pre-BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk+IG1UYn+/NJPPlyxrHZ+1OhyLTWCVGJr552chuPSTtqRTUIgx4c5NmtkndJmEn4KqXVXoQ0aQsUmmtVEVQhIIXQ/GmRYgiGi9e9LCs1D/gQStsDwWRyZ9VsnvMpt/hzZv38fH7fb/vN8OjgwgGmGBDChahAg1YA3gV4F2AjwD4TD/Lwuw8WD8lEI2I1SQdb18F80acNNx8C0jDv98M17d7Bun4fRvMnxOk4+fnwfwxQSp+eZo0vNEGiuLNpbBMxwu/G2ZbJw2/fi+sbP1hkIadnkEqvuKTjr9cBrN7L2n4ehtIxZvLyUeMbjX1bQvEVunkG+/Da8DOVdeBbZUuAfv16Megf3gZPjneqm7Aueox7POGAnzGDueEFFkhsq7IOkLk3JwrXSGkkxMyJ4VwhRCyy6DH4ptsc4b2UczSKZJCfOf5pE4RUp1swNeBLxYby8/WG01bCvmYIxYcOX/EPlUp1k77Zbu+YhfLZb9sl16wmxXfXqk3i81qvWYHfnHlVMVOBb5vB2erTd8pNwJnlHYG6cyZoF572MrQA/wQ3ZWMU0wOKLQ8MtIJjHJ2QrGipBFzxZBdy+Nnp8BpIEYMr3v8pSnAzcr7SLcipOKVgMhCiqai2LsAXLPYEYVfGR+DKxy5MGEOj5PgGTqQnkWVx86MvBByIU1kcgHdk747HElJCbUhdU48uO0Yblr75b7/Whh5qePx2hTkGyim4vVbT/HndkolJo036PObJ/naNAZzcFx5mRsp3/G4az1Kh3ly/PsZK8luD6vlTZn1iSEFVwThJsXwO43fv0tX2xQ7Ho9bAwvp+KnHl6cwUgz/M3j+9hO7GsidMNrAQH+t7gRzHZHdCzBjq8Rf3NmZOzdhsP00kyRCGap5ax2s4dNUf2Nd+JPJl1WlH3OFL0CzGCnJf1gsPFDWlgoHLl0M46v8oaV+/JCXG8zU7Hz6GlPuSDQLo92exkNX9wxnob8+/UHh6PCgsBjedC5C/0XZyKdVvDZ77H8XIgHzUIDjcBKegQo0YBVW2b8DAMUEMx4=); Raid BiS: [full raid](https://wowsims.com/forever/priest/dps/#eJzEVk1oK1UUnnNnkrk5qTFen6/zhofMi0+JkYl3bhppn4vkvdXjgfoQBtzZpEmb1DYJnaBVNxW6ENGkRFtorVRFUISCG0Nxp0WIP2jduBGlVOrPzh9oF4UiM0mqpF2m8SxObu7hzved73wzXLxMIQwaGBCFcShABRYAXgZ4G+ADADbkVYlbHQX9pxClYZ/+LKr0aBO0/SAq9LgBqNC/33DzmzthVOl3ddB+DqFKP10C7YcQyvTzKVTofh1QpT8ue+dUuvJ7WKurqNCvlt2jX77j5sXX3dz0HvPLOmitu1Ghr9YBZfrXTOShcKsY/aYG/CB7+7V34RUgi8UGkIPsGpBfr38I6vvr8NHNWnEXFos3qMcc0vAJuZrkgic4T1g8YXKetJKWsDgXZpKLpODc4pyLFoEdEtwje0N4AQO6ir4opW89F1HRh7KZcFgD2HimMvN0uVI1BBePmHzMFKPXjIlCpjSVzxnlOSOTy+VzRvZ5o1rIG3PlaqZaLJcMJ5+ZmygYUSefN5zZYjVv5iqO2S2b7XJ82imXHtTjeB+7gndEghgQbQo1G8OxEPUzckvS/aggsXiHXc1mswPg1BYjQLdt9uIA4IbFPajqPpTphoOoU/RH/XRnBZiik2sS2+gdg8VNMdZnDo8iZ3G8FBumMgtMd73gckGFx5MO3hW70x1JVnK1QXmE33/iGKbpF8WFf1voeqlps9IA5GsrJtPtwyfYM6el4v3Ga/f59eNsYRCDudyrvEh2lW/azNIfxqss0vv+9BxJnAyrZg+Y9a0OBYs77iJK6LcKu/eMrk4oNm0W1NsWUunHNpsZwEip+52hS0ePnWkgq89obQP9OX8azDJ54jzAwgdZ9sLpzqyRPoNdxKEIIhWumocN0Du/mvwbacEfRLwkS16MpD8DRScoRY5JwN2QFibTl9ZW3fgidWXSi+9TYpdoipGKbRHpf4lqurs613hg89xwxrz85Hvp652N9Lh711kF74+0m4rJdGv4xn+uRBxGIQ034TY8BQWowDzMk38GACz1M14=).

## Other builds of this spec

- [Discipline/Holy — Smite](../research/raid/builds/smite-discipline-raid.md) (31/17/3, 586 DPS in a full raid) — [open the talent tree](https://talentsforever.com/priest/60/505235231030001001-30505101002-3-12)

---
*Generated by `_reference/data/render_modes.py` on 2026-11-19 from this project's builds and simulations of the WoW: Forever beta (talent and spell data: client build 1.60.1.70753; raid numbers: the official wowsims/forever simulator at 2e6e77d (client 1.60.1.70938)). Simulations, not in-game measurements. Do not hand-edit.*

