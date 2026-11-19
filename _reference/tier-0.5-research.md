# Tier 0.5 in WoW: Forever (research of 2026-11-18)

User, 2026-11-18: "there is currently a 0.5 tier set for each set. So we may need to do a full research analysis on the list again",
then "loot is extremely hard to get regardless if you don't need raids. So I still think that we should keep a different list, maybe
even like a pre-BIS list for the things that can just be obtained through questing or doing dungeons and not having to do all of the
work to get the 0.5 tier set. But first you need to do the research on everything to see what it needs, how much is available, and
how obtainable it actually is."

Hand-kept. Sources at the end. Forever facts and Classic assumptions are marked; seller pages are marketing, not player reports.

## What it is

Forever's Tier 0.5 is Season of Discovery's reissue of Dungeon Set 2, not Classic's. The simulator calls it that too
(`sim/common/forever/items_sets.go`).
- **The chain.** A quest chain at level 58 upgrades the Tier 0 (Dungeon Set 1) pieces slot by slot. Each turn-in consumes the matching
  Tier 0 piece, and each reward is one spec version of the player's choice (druids: Feline, Astral, Guardian's or Mender's).
- **The vendors.** Deliana (Ironforge) and Mokvar (Orgrimmar) list all 144 pieces (18 spec versions × 8 armor slots) for gold.
- **Versions per class:** warrior 2, paladin 3, shaman 3, priest 2, druid 4, and hunter, rogue, mage and warlock 1 each.
- **Stats:** item levels 55-66, a mix of rares (shoulders, belts, bracers, legs) and epics (head, chest, gloves, boots).

## What it needs (Forever, from Wowhead's Forever quest and vendor pages unless marked)

- **Level and inputs.** Every step needs level 58 and the matching Tier 0 pieces. Tier 0 is still a random drop in Scholomance,
  Stratholme and Blackrock Spire (the simulator's database; Wowhead's own drop tab not checked).
- **Steps.**
  - An Earnest Proposition (bracers): the Tier 0 bracers, 15 Silithus Venom Samples (Horde; a seller page says Winterspring Blood
    Samples for the Alliance) and 20g.
  - Just Compensation (belt, gloves): the two Tier 0 pieces.
  - Anthion's Parting Words (boots, legs, shoulders): the three Tier 0 pieces.
  - Saving the Best for Last (helm, chest): the two Tier 0 pieces.
- **The middle of the chain (Classic's, ids unchanged):**
  - an Ectoplasmic Distiller: a Delicate Arcanite Converter, 4 Greater Eternal Essence, 10 Stonescale Oil, 25 Volcanic Ash, 40g;
  - ectoplasm in Silithus, Winterspring and the Eastern Plaguelands;
  - Magma Lord Bokk's core, a Fel Elemental Rod, the Ysida rescue in Stratholme (a timed Baron run in Classic);
  - 3 Dark Iron Bars, 20 Enchanted Leather, 3 Mooncloth, 4 Cured Rugged Hides, 25 Ogre Warbeads;
  - Jeering Spectre's Essence with 4 Dark Runes and 8 Large Brilliant Shards;
  - the Three Kings of Flame with a Hallowed Brazier (a seller page says Argent Dawn Honored);
  - a spirit boss per class (Mor Grayhoof, Isalien, Jarien and Sothos, Kormok);
  - 20 Bloodkelp, 40 Blackrock Bracers and a Flask of Supreme Power;
  - Lord Valthalak in Upper Blackrock Spire, a 10-player instance by Warcraft Tavern's Forever guide. Blizzard's hotfix of
    2026-11-17: Upper Blackrock Spire had been far too easy and "again requires a full complement".
- **No raid needed.**
- **Vendor prices, gold only:**
  - Deliana: helm and chest 88.89g; boots, legs and most gloves 50g; shoulders and most belts 25g; 28 cheap pieces at 4.6-11.7g.
  - Mokvar: 94.74g, 47.06g and 23.53g.
  - Two guards (Ironforge Guard, Kor'kron Elite) list them dearer.
  - In Season of Discovery the vendor was an exchange that each slot's quest unlocked (hotfix of 2024-07-17); whether Forever gates
    it the same way is **unconfirmed**.

## How obtainable it is (players on Blizzard's Forever forums, 2026-11-14 to 11-18)

- "Over 1000g" for a 5-piece bonus even with double gathering.
- The turn-ins are sequential, so a player loses the Tier 0 bonuses on the way.
- Worth about "50 dps on sims", or "a 20 dps loss" against another best-in-slot list.
- Called a long project for people who do not raid. Raids open on 2026-12-09.
- One player had 8/8 by 2026-11-18.
- **Since launch players report that no class's Tier 0.5 set bonuses work**; no Blizzard reply was visible.
- The 2026-11-17 hotfix gave the Soulforge tank version spell power in place of Strength.
- No Forever-specific guide from Wowhead, Icy Veins or Warcraft Tavern was found.

## How much it is worth (our numbers)

Each piece scored by each damage spec's own BiS stat weights (the ML records' simulator stat weights, a linear estimate; scratch
`t05_inventory_1118.py`), against the item the spec's current BiS and pre-BiS sets hold in that slot. Set bonuses are left out.

| | Over our BiS set | Over our pre-BiS set |
|---|---|---|
| Most specs | +0.0% (no piece better in any slot) | +0.0% |
| The most | warrior Arms +1.1%, mage Arcane +0.9%, shaman Enhancement +0.9% | Arcane and Enhancement +0.9%, the Elemental/Enhancement hybrid +4.8% (its pre-BiS set is weak) |

Examples:
- **Pieces that win:** Sorcerer's Crown for Arcane (+6.4 DPS over Spellweaver's Turban); Gauntlets of Heroism for Arms (+10.1 over
  Stormshroud Gloves); a few Five Thunders pieces for Enhancement (+1 to +3 each).
- **Pieces that lose:** most others lose, often by a lot. Virtuous is healer gear with spell power swapped in, so Shadow loses in
  every slot.

The set bonuses, as the simulator models them (the same as Wowhead's tooltips; there is no 8-piece bonus):

| Pieces | Bonus | Damage value |
|---|---|---|
| 2 | +8 all resistances | none |
| 3 | 8 mana or 15 health per 5 sec | little |
| 4 | the class's proc: mana, energy or rage; a spell-power proc for the paladin; a heal for the warlock | some, mostly mana |
| 5 | a defensive proc when struck | not modelled |
| 6 | +23 spell power for cloth, +40 attack power, +20 Strength for the warrior, both for the druid | about 1-2% of a spec's damage |

So the full set is at best a small upgrade over our lists, for the few specs whose pieces hold up in six slots. That matches the
players' "50 dps on sims" and "a 20 dps loss". **The bonuses may not work in the game today.**

Earlier ML records already admit Sorcerer's Leggings and Gauntlets: 24 of our 99 gear sets hold a Tier 0.5 piece, because a
community preset used them. The pool rule of 2026-11-05 counts only drops, recipes and reputation as sources, so every other piece
is out (`raidsim/gear_opt.py` in_pool).

## Gaps in the simulator's data

The simulator's database has 133 of the 144 pieces. It is missing 8 druid helm and chest versions and 7 priest pieces, and holds
Classic's ids for the druid's and the priest's helm and chest.

## The current pre-BiS lists, by the same test

Our pre-BiS tier is "no raid drop, no raid-boss quest reward, no crafted item made from Molten Core or Onyxia materials". By the
user's test of what can just be obtained through questing or dungeons, it is not that tier. Its sets lean on:
- crafted epics with rare materials and high cost (Lionheart Helm, Robe of the Archmage, Belt of the Archmage, Black Dragonscale Helm);
- exalted reputations (Timbermaw's Mantle and Tunic);
- rare dungeon drops at their full drop chance.
The character planner already holds the rule this would need: only what you can count on (quests, crafts, buys), with dungeon drops as
bonuses at their one-run chance.

## Open (not confirmed for Forever)

- Whether each vendor slot needs its quest first, and the real in-game prices.
- The total gold cost.
- The Baron timer, and whether The Challenge (Theldren, Blackrock Depths) is still a step.
- The Fel Elemental Rod's price, and the Hallowed Brazier's reputation requirement.
- Upper Blackrock Spire's official group size.
- Whether the set-bonus bug is fixed.
- Drop rates of the quest materials, and Tier 0's drop tables.

## Sources

- Wowhead Forever:
  - the vendors: https://www.wowhead.com/forever/npc=230319/deliana and https://www.wowhead.com/forever/npc=230317/mokvar
  - the quests: https://www.wowhead.com/forever/quest=84155, quest=84171, quest=84187, quest=84203, quest=8921, quest=8947,
    quest=8994, quest=8995
  - item tooltips: https://nether.wowhead.com/forever/tooltip/item/226932 (also 226862, 226973, 226772, 16730)
- Blizzard: hotfixes of 2026-11-17, https://us.forums.blizzard.com/en/wow/t/2403040.
- Player threads: https://us.forums.blizzard.com/en/wow/t/2419986 (11-17), /t/2415227 (11-14), /t/2421405 (11-18),
  /t/2418483 (11-16), /t/2376012.
- Season of Discovery hotfix of 2024-07-17: https://us.forums.blizzard.com/en/wow/t/1788040
- Guides: https://www.warcrafttavern.com/forever/guides/blackrock-spire/ and https://wow.gg/guides/wow-forever-tier-set-bonuses
  (2026-09-17).
- Sellers (marketing):
  - https://leprestore.com/guides/world-of-warcraft-forever/wow-forever-tier-0-5-upgrade-guide-dungeon-set-2/
  - https://boostroom.com/product/wow-forever-tier-0-5-boost
- The simulator: the official wowsims/forever at 2e6e77d84, `assets/database/db.json` and `sim/common/forever/items_sets.go`.

## What we did with it (2026-11-18, user: "Go with your recs", then "Go with your rec")

- **Tier 0.5 is out of both pre-raid tiers.** The BiS lists are not rebuilt around it: by our numbers it changes them by 0-1%, and
  the bonuses may not work in the game.
- **A third tier, Quests and dungeons, is the practical list** (definitions in `raidsim/gear_tiers.py` `DUNGEONS`): quest rewards of
  no raid; named-mob drops of the 5-player dungeons at 5% or more, with no Upper Blackrock Spire boss; trainer recipes; reputation up
  to Honored; no auction house, no Tier 0.5, no PvP.
- **The research found a bigger gap than Tier 0.5.** The simulator's database dates every item (phase 1 now, phase 2 the raids from
  2026-12-09 and later content), and 15 later items had sat in our sets, Rockfury Bracers in 41 of 99. The pools now read the field;
  "Phase 1 BiS" is now "Raid BiS" (Molten Core and Onyxia).
- **Every set is made again** by the gear night `deep-runs/gear_phase_1118.sh` (page-audit Q10-Q12).
