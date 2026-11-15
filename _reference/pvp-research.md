# WoW: Forever PvP research

Hand-kept. Research of 2026-11-14 for the PvP builds (user: "do full research on WoW Forever PvP builds and build whatever is
necessary").
- Tags: [B] Blizzard; [V] checked by us in the client's tables (wago.tools, builds 70888 and 70938) or Blizzard's API;
  [C] community, press or datamine.
- Dates are 2026.
- What the duel lab does with each fact: `_reference/data/duellab/dtables.py`.
- The work plan: `_reference/pvp-plan.md`.

## Systems

- **Battlegrounds** [B S1-S3, V S14]:
  - Warsong Gulch (10v10; brackets 10-19 to 50-59, then 60) is live.
  - Darkspear Islands is new and live: 15v15, levels 30-60, four capture points plus a flag, first to 2,000, with two
    reputations of its own.
  - Arathi Basin (15v15) and Alterac Valley (40v40, 51-60) are promised as "original Vanilla battlegrounds". No post-launch
    source confirms either is open.
  - Battlegrounds mix Normal, PvP and RP players.
  - The client holds unannounced entries: "Battle for Blackrock" (50-60, 15 players), "Battle for Gilneas", "Mak'gora Arena".
- **No arenas, ratings or ladders.** Developers said arenas are probably not coming [C S9].
- **Honor and ranks** [B S1, C S10]:
  - Honor is spent. Rank points climb ranks 1-14 under a weekly cap (datamined: 2,700 in week 1, 24,750 by week 10). No
    standing or decay is mentioned.
  - Weekly "Field of Honor" tasks grant both.
  - Rank 14 within a patch cycle is the stated goal [B S8]. A reset each season is implied, not stated.
  - The honor cap is 25,000 [B S4].
- **Rank rewards** [B S1]: 2 the PvP trinket, 3 a cloak, 4 a necklace, 8-10 and 12-13 epic armor tokens, 11 mounts, 14 weapons.
- **Gear** [V S14]:
  - Honor buys a blue set: item level 60, requires level 55.
  - The epic piece needs the blue piece plus a rank-gated seal: item level 65.
  - Rank 14 weapons are item level 65 (Classic's were 78).
  - The PvP vendors have been "temporarily unavailable" since launch [B S7].
- **World PvP** [B S5, S6, C S9]:
  - Rulesets: Normal, PvP, RP and RP-PvP.
  - On PvP realms: one faction per account, creation limited for the bigger faction, tighter zone population caps (11-09).
  - No new objective or war mode is confirmed.

## Mechanics

- **PvE numbers hold in PvP:**
  - Crits against players were halved in the beta. Blizzard removed that on 10-08: "Critical strikes in PvP no longer have
    reduced efficacy" [B S4; C S17]. A designer had called it a bug [C: Icy Veins, 09-29].
  - No resilience [C S11].
  - Every spell effect's PvP multiplier is 1 in clients 70888 and 70938, apart from 8 blank dummy auras. Server-side rules would
    not show there [V S14].
  - No tooltip has a PvP clause but Bane of Doom's "Cannot be cast on players".
- **Diminishing returns:**
  - Forever has published no categories or timers.
  - Since 11-02, roots from procs diminish: Frostbite, Entrapment, Improved Wing Clip, Counterattack, Improved Hamstring [B S4].
  - The duel lab uses Classic Era's categories from DRList-1.0's "classic" section (github.com/wardz/DRList-1.0, read 11-14):
    - stun: Cheap Shot, Charge, Intercept, Hammer of Justice, Bash, Pounce, Intimidation, Concussion Blow, War Stomp.
    - kidney_shot: its own category.
    - random_stun: Impact, Mace Specialization, Blackout, Seal of Justice, Improved Concussive Shot.
    - incapacitate: Polymorph, Sap, Gouge, Repentance, Freezing Trap, Scatter Shot, Wyvern Sting, Hibernate.
    - fear: Fear, Psychic Scream, Howl of Terror, Intimidating Shout, Seduction, Scare Beast.
    - root: Frost Nova, Entangling Roots, Counterattack, Nature's Grasp.
    - random_root: Frostbite's freeze, Improved Hamstring, Improved Wing Clip.
    - frost_shock, mind_control: their own categories.
    - None: Blind and Death Coil.
    - Each application runs half, then a quarter, then immune; the reset is dynamic between 15 and 20 s.
  - DRList calls itself "mostly obsolete for Retail/Forever" since patch 12.0's own API.
- **The PvP trinket** is per class, comes at rank 2, and has a 5-minute cooldown. Each class's breaks different control [V S14]:

  | Classes | Breaks |
  |---|---|
  | Warrior, Hunter, Shaman | stun, root, slow |
  | Rogue, Warlock | charm, fear, Polymorph |
  | Mage | fear, Polymorph, slow |
  | Paladin, Priest | fear, Polymorph, stun |
  | Druid | charm, fear, stun |

- **Control changes:**
  - 11-02 [B S4]: Stoicism stun and charm -20%; Divine Precision silence -20%; Sacred Duty Forbearance -10 s; Quick Getaway +1 Sap;
    Frost Warding lost its reflect.
  - 11-13 hotfix [B S3]: Berserker Rage breaks Sap; Frost Nova "now breaks on damage from procs and Blizzard".
  - The user saw Ice Lance end a Frostbite freeze (11-14).
- **Balance hotfixes since launch** [C: Blizzard hotfix thread us.forums.blizzard.com/en/wow/t/2403040]:
  - 11-10: Wrack -30%; Summon Hawk +80%.
  - 11-10, live 11-12: Stormstrike 150% -> 100% weapon damage and cooldown 6 -> 8 s; Maelstrom Weapon 20 -> 6-10 procs a minute.
  - 11-13: Wild Growth healing doubled.

## What the community plays (live unless marked)

Sources: talentsforever.com PvP tags (players' own tags, counted 11-04 on the launch trees; intent, not results), Mobalytics
guides, RankedBoost, forums. Our copies of the exact builds: `_reference/data/pvp-community-builds.json`.

| Class | Builds |
|---|---|
| Warrior | 31/20/0 (TF top, 16 tags; Chooki); battleground 35/16/0 and world PvP 35/5/11 (Omnivore, MB 11-07: Spearing Strike, Weaponmaster, Improved Hamstring) |
| Rogue | 16/7/28 Hemorrhage (TF top); 16/14/21 Backstab and 14/12/25 battleground (Perplexity, MB 11-04); Mutilate 32/10/9 advised against (no Preparation); "Death Mark isn't usable in PvP"; Shank is the energy tool after the 11-03 Relentless Strikes nerf |
| Priest | 25/3/22 duel (Penance, Silence), 35/16/0 battleground (Power Infusion), 26/25/0 large battleground (Hydramist, MB 11-06); TF tags all Shadow, top 14/3/34 |
| Hunter | 0/21/30 ranged Survival (Feor, MB 11-13); 0/26/25 Warsong Gulch (Cpt, MB 11-09); TF top Marksmanship 5/46/0 |
| Warlock | 7/7/37 Destruction (Saucy722, MB 11-10); TF Affliction 40/11/0 and Soul Link 5/36/10 |
| Paladin | No real PvP guide; TF's most-tagged PvP build of any class is Ret/Prot 0/20/31 (23 tags); players call Unsealed Wrath "roulette" |
| Shaman | No real PvP guide; TF Enhancement 8/39/4 (before the 11-12 nerf); forum posts of one-shots before it |
| Druid | No real PvP guide; TF healer 16/11/24 (Heart of the Wild), Feral/Restoration 11/24/16 |
| Mage | No real PvP guide; TF Frost 3/5/43 |

**Tier lists and results:**
- Tier lists are opinion only:
  - RankedBoost (11-08): S tier Feral, Arcane, the three rogue specs and Discipline.
  - Seemeta (11-14): Subtlety, Shadow, Frost, Demonology.
  - Icy Veins: "too early to tell".
- No level-60 duel or battleground statistics are published.
- The Forever Open (beta, level 30, 10-17/18, 1,714 entrants; raider.io): warlocks first and second; in finals games warlocks won
  26 of 33 against other classes and shamans 19 of 30.
- The community calls these decisive: Soul Link and Seduction, Penance, Ice Lance with Fingers of Frost, Enhancement before its
  nerf, Wrack before its nerf.

**Tools:**
- talentsforever.com's Training Grounds (/duel) is a fan-made real-time 1v1 and 2v2 game. It models diminishing returns, healing
  dampening and line-of-sight pillars, uses fixed Tier 1 gear and the 11-02/03 trees, and says 443 of 465 talents work as
  written. It has 355 ranked level-60 duels (11-09 to 11-14), too few for matchups.
- github.com/yazpad/wow_forever_pvp_sim: a Monte Carlo 1v1 sim with learned play, written in Zig. Only the warlock is trained.
- wowsims covers PvE only.
- **Our API check:** Blizzard's API gives each Forever character only `honorable_kills` and `pvp_rank` (`/pvp-summary`), plus its
  talents by name (`/specializations`). It has no seasons, ladders or rank points, so there is no list of top players to read
  builds from.

## What this means for the duel lab

| Fact | In the model |
|---|---|
| No resilience, PvP crit penalty or PvP multipliers | the fight lab's PvE numbers, unchanged |
| Classic Era's categories, half then a quarter then immune, 15-20 s reset | `DR_CATEGORY`, `DR_STEPS`, `DR_RESET` 17.5 |
| Per-class trinket | `TRINKET_BREAKS`; the trinket needs rank 2 (on by default: `TRINKET`) |
| Frost Nova breaks on any damage (11-13); a Frostbite freeze ends on a hit (user) | `ROOT_BREAK` |
| No arenas; battlegrounds and the open world | duels as the measure (1v1); battleground roles are a planned addition (pvp-plan.md) |
| Item level 60/65 PvP gear | the fight lab's dungeon-blue tier for both sides (comparable item level); a PvP set is planned |

## Open questions

- Forever's own DR categories and timers.
- Whether Arathi Basin and Alterac Valley are open.
- Real honor and rank-point rates.
- Season length and resets.
- The vendor fix, the unannounced battlegrounds, war games.
- Whether Forever has healing dampening (the fan sim models it; no Blizzard source).
- Whether Frost Nova breaks on dots outside Blizzard.

## Sources

- S1 worldofwarcraft.blizzard.com/news/24303316 (10-07)
- S2 worldofwarcraft.blizzard.com/news/24307308 (10-07)
- S3 worldofwarcraft.blizzard.com/news/24315643 (10-29) and hotfixes worldofwarcraft.blizzard.com/news/24315281 (11-05 to 11-13)
- S4 us.forums.blizzard.com/en/wow/t/forever-beta-development-notes/2360696 (10-01 to 11-02)
- S5 worldofwarcraft.blizzard.com/news/24302070 (10-22)
- S6 us.forums.blizzard.com/en/wow/t/2408781/1 (11-10)
- S7 us.forums.blizzard.com/en/wow/t/2402363 (11-05)
- S8 kotaku.com/new-things-learned-world-of-warcraft-forever-2000734005 (09-14)
- S9 podcast youtube.com/watch?v=bzaMA5fZ1tE (10-15), with recaps mein-mmo.de/wow-forever-pvp-podcast/ and
  eu.forums.blizzard.com/en/wow/t/635761
- S10 kami-labs.fr/en/wow-forever/wow-forever-datamine-pvp-rang-grand-marechal/ (09-24)
- S11 kami-labs.fr/en/wow-forever/wow-forever-deep-dive-resume/ (09-14)
- S12 insider-gaming.com/world-of-warcraft-forever-roadmap/ (09-18)
- S13 kami-labs.fr/en/wow-forever/forever-open-resultats-finale/ (10-19); raider.io/events/the-forever-open/brackets/finals
- S14 wago.tools client tables, builds 70888 and 70938 (read 11-14)
- S15 our Blizzard API calls (11-14)
- S16 warcrafttavern.com/forever/news/pvp-progression-in-wow-forever-ranks-honor-seasons/ (10-07)
- S17 us.forums.blizzard.com/en/wow/t/2362058 (09-25)
- Mobalytics guides (mobalytics.gg/wow-forever/...): warrior-pvp-guide 11-07, rogue-pvp-guide 11-04, priest-pvp-guide 11-06,
  survival-hunter-pvp-guide 11-13, hunter-pvp-guide-captain 11-09, destruction-warlock-pvp-guide 11-10
- rankedboost.com/world-of-warcraft/forever/tier-list/pvp/ (11-08); seemeta.com/en/wow-forever/pvp-tier-list (11-14);
  icy-veins.com/wow-forever/pvp-tier-list-dps-specs (10-26)
- talentsforever.com/duel (Training Grounds); github.com/yazpad/wow_forever_pvp_sim (10-27); github.com/wardz/DRList-1.0
