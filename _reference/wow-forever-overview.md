# WoW: Forever — what we know (as of 2026-09-25; beta builds and talent counts updated 2026-10-15)

> Sources: the BlizzCon 2026 reveal and demo, Blizzard's beta announcement and beta development notes
> (2026-09-17 and 2026-09-24), and beta-client datamines (warcraftforever.games, talentsforever.com, thewowdb.com,
> wowforevertalents.com, the ElliotWood/Forever simulator). Numbers and talent names change between beta builds;
> every number below says which build it comes from. Update this file when new development notes appear.

## Headline facts

| | |
|---|---|
| **What** | World of Warcraft: Forever — Blizzard's "Classic+" evolution of vanilla WoW |
| **Launch** | November 4, 2026 |
| **Beta** | Opened 2026-09-17, last full day 2026-10-21. Level cap **20** at the start, raised to **30** "after a couple of weeks" (not yet announced as of 2026-09-25); no level 31-60 or raid testing in the beta. A "Server Slam" with broader access is planned. Beta characters are wiped at launch. |
| **Beta builds** | 1.60.1.69876 and 69893 (2026-09-17), 69913 (2026-09-18), 69977 (2026-09-22), 70009 (2026-09-24, first class tuning), 70170 (read 2026-10-03, with the warrior hotfixes of 1-2 October), 70205 (the simulator's build of 2026-10-03), **70291 (2026-10-08; the project's data since then, `_reference/data/data_build.py`)** |
| **Level cap (launch)** | 60 (dungeons scale 13–60; 51 talent points, i.e. level 10–60) |
| **Classes** | The 9 Classic classes: Druid, Hunter, Mage, Paladin, Priest, Rogue, Shaman, Warlock, Warrior — no new class |
| **New race** | Skyborne (both factions): Warrior, Hunter, Rogue, Druid, Shaman (Horde), Mage (Alliance) |
| **New race/class combos** | Dwarf Shaman, Human Hunter, Undead Paladin, Gnome Priest, Orc Mage, Troll Warlock (16 new combos in total per the datamine) |
| **Talents** | Classic-style 3 trees × 7 tiers, 51 points; gold-medal 1-point talents at 11/21/31 **plus a new one at 16**; **466 talents** in build 70291 (467 in 70009, 469 at BlizzCon): the beta client stores them in retail-style Trait tables, the talent panel has Primary and Secondary tabs (unexplained; likely dual spec), and no talent has four ranks any more |
| **Legacy system** | Account-wide Legacy Points from challenges (65 earnable at launch, 16 spendable per character, each character spends its own copy) in three perk trees — Adventures, Professions, Resourcefulness (rested-XP, stealth detection, profession perks; no combat talents) — plus a cosmetic progress track |
| **Raids** | The Barrow Deeps (10-man), Hyjal Summit (20-man) |
| **Zones** | Mount Hyjal, Zephras Isle, Riverglades |
| **Dungeons** | Nine new dungeons from level 13 to 60; the beta opened with Hall of Thanes (13–18) and Ruins of Lordaeron (15–20) |
| **Battleground** | Darkspear Islands (15v15) |

## Beta facts that matter for talents and builds

- **Respec cost (beta only):** 1 silver if you have not changed talents recently; after a reset the next one is much
  dearer but drops back to 1 silver after an hour (dev notes 2026-09-24). The respec planner still assumes Classic's
  launch prices (1g, +5g per respec, cap 50g) until Blizzard states the launch schedule.
- **Cooldown Manager** (the retail UI) is being tested; gamepad support expanded.
- **DoTs and HoTs crit:** the 2026-09-24 build fixed Rejuvenation, Tranquility, Wild Growth, Renew, Riptide, Lacerating
  Strikes and Contingency Plan so they can crit — consistent with the "all periodic effects crit" reveal claim the
  Forever models assume.
- **Wands** no longer gain damage from spell damage (2026-09-24); Wizard Oils are back at Classic values (8/16/24).
- **Racials:** Gnome Eureka! is a flat 10% discount on Mana/Rage/Energy abilities on every class (was up to 50%);
  Tauren Cultivation has level requirements per herb; Undead Touch of the Grave no longer breaks crowd control.
- **Air totems** from different shamans no longer stack; Flametongue Totem no longer stacks with Windfury Totem or
  Flametongue Weapon.

## Class changes in build 70009 (2026-09-24 development notes)

- **Druid:** Wrath base damage +50%; Rejuvenation/Tranquility/Wild Growth crit; Thorns scales with the caster's spell
  power; Mangle renamed **Primal Bite** (its debuff is gone); Primal Fury renamed **Blood Frenzy** (original icon).
- **Hunter:** Furious Howl's attack power -40%; Tame Beast no longer works on higher-level beasts; Lacerating Strikes
  can crit; **Strider Kick** also grants 30% movement speed for 3s; talenting out of Lone Wolf no longer leaves a
  -4% debuff.
- **Mage:** Arcane Missiles checks line of sight once; **Wake of Fire** window 30s (was 20), **Hot Streak** 20s (was
  15); Ignite no longer double-dips damage modifiers.
- **Paladin:** **Holy Strike** weapon damage 25/29/32/36/39/43/46/50% by rank (was 25-40%), 10s cooldown (was 12),
  **Improved Holy Strike removed**; **Holy Power** also gives Holy Strike +15% crit; Retribution Aura scales with spell
  power; **Righteous Fury** Holy threat +60% (was 90%); **Vengeance** procs on non-periodic crits and stacks 3 (was 5);
  **Two-Handed Weapon Specialization** 2/4/6% (was 3/6/9%); **Sacred Arbiter** +20% Holy Strike (was 10%);
  **Twist of Light** also cuts Seal mana by 20%; Echo of Justice's proc chance fixed; **Crusade** is gone from the
  trait tables (not in the notes).
- **Priest:** Renew can crit; Power Word: Shield can always overwrite a shield on a target without Weakened Soul;
  racial priest spells fixed (Contingency Plan crits, Starshards pushback, Dark Sacrifice).
- **Rogue:** Sap flags for PvP correctly (no talent change).
- **Shaman:** Lightning Bolt ranks 3-4 raised so every rank is an upgrade; **Elemental Fury and Elemental Alacrity
  swapped rows** (Alacrity tier 3, Fury tier 6; Call of Thunder now requires Alacrity 3 and Fury requires Call of
  Thunder); **Lava Burst** ranks 1-2 raised ~10% above the Lightning Bolt rank of the same level; **Rage of the
  Farseer** no longer speeds spell casting; Riptide crits; totem buff names cleaned up.
- **Warlock:** Life Tap tooltip fixed; Voidwalker Sacrifice scales with 10% of spell healing.
- **Warrior:** Sunder Armor threat corrected (explicit threat values, more from attack power); **Bloodthrill**
  4/8/12/16/20% (was 2-10%) and only from main-hand attacks (Cleave and Heroic Strike count); **Slam** cooldown 18s
  (was 15) and **Improved Slam** cuts it by 1.5/3s; the notes say Bastion (row 5) and Focused Rage (row 6) swap, but
  the build's trait tables still show them where they were.

## What the beta client changed against the BlizzCon demo (builds 69876–69893)

- **Trees renamed:** the Priest tree is "Shadow" (the demo transcription had "Shadow Magic") and the Shaman tree is
  "Elemental" (was "Elemental Combat").
- **Talents cut:** Balance of Nature (Druid), Vitality (Warrior); **replaced:** Drain Hope → **Wrack** (Warlock, a 6s
  Shadow channel that buffs your other Shadow DoTs), Restless Blades → **Flawless Execution** (Rogue, Eviscerate -10
  Energy); **moved:** Shaman Tidal Mastery to Restoration tier 4 and Totemic Focus to tier 1, Warrior Bastion to
  Protection tier 5.
- **Every rank's tooltip is real** (the demo had rank-1 text only; ~280 talents had extrapolated ranks). Notable
  corrections: Winter's Chill stacks to 5 (demo read 1), Improved Counterspell silences 4s (demo 2s), Moonfury is
  2%/rank (demo 1%), Mental Dexterity gives 100% of Intellect as attack power at 3/3 (demo read 33%), Mental Quickness
  30% (demo 15%), Fingers of Frost is 15% for 1/2 spells, Redoubt is 6%/rank block at 2%/rank chance, Vindication 1/2/3%.
- **Spellbooks:** most direct-damage spells deal roughly **half their Classic damage at 60** (Shadow Bolt 253-283 vs
  482-538, Lightning Bolt 189-211 vs 428-477, Fireball 425-541 vs 596-760, Smite 166-187 vs 384-429, Starfire 350-412
  vs 496-584) while low-rank coefficients rose (Frostbolt rank 1 40.7% vs 16.3%); Lightning Bolt casts in 2.5s and
  Chain Lightning in 2s; Aimed Shot is baseline with a 2s cast and +166 at 60; Multi-Shot is a single rank; Holy Strike
  has 8 ranks from level 6; Seal of Fury 7 ranks; Lava Burst, Incinerate, Penance, Riptide, Mutilate and Primal Bite have
  level-40/50/60 ranks; Divine Spirit and Shadow Word: Death are trained; Blessing of Sanctuary, Curse of Shadow, Dark
  Pact, Fire Nova Totem and cat Mangle are gone. Per class: `<class>/research/spells/README.md`.

## Changes after build 70009 (2026-10-01 to 2026-10-08)

Collected from the refreshes and the 2026-10-09 audit (details and sources: `_reference/data/forever-talents/README.md`,
`_reference/data/raidsim/patches/README.md`, CLAUDE.md "Beta build 70170/70205" and "Audit of 2026-10-09").

- **70170** (2026-10-03): warrior Fury rework (the 1-2 October hotfixes); Hot Streak became **Heating Up**; King of the Jungle and
  Toughness removed. **70205**: Lightning Reflexes 2% Agility a rank.
- **70291** (2026-10-08): Impale needs 3 points in Deep Wounds; Predatory Instincts became Natural Instinct (Intellect to healing);
  Penance much weaker; Water Shield has no cooldown; Reckoning a 1.5 s limit; Expose Prey 10 s; spell ranks rescaled.
- **Beta notes**: critical strikes give 100% more rage (warriors 2026-10-02, druids 2026-10-08); Bear Form threat bonus 50% (was 30%);
  rage from damage taken uses an expected creature's health (2026-10-08); low spell ranks get less from spell power (2026-10-01, no
  formula published); queued Heroic Strike no longer raises off-hand hit (2026-10-01).
- **Pets** scale from their summoner's stats (Rogue and Warlock deep dive, 2026-10-07); the client's UI gives the shares (build 70291).

## Class-level changes called out at the reveal (still true in the beta)

- **All classes:** DoTs can crit. Many later-expansion spells return as talents.
- **Druid:** Revive, Wild Growth, Berserk, Eclipse and Primal Bite (bear) added; Omen of Clarity is baseline and now
  affects spellcasting; Balance gets mana help; Restoration's Swiftmend no longer consumes the HoT.
- **Hunter:** Mine!, Sniper Shot, Strider Kick, Summon Hawk and Lone Wolf; Marksmanship can play without a pet
  (Lone Wolf); Survival supports a melee playstyle (Strider Kick, Lacerating Strikes, Expose Prey).
- **Mage:** Hot Streak, Fingers of Frost, Missile Barrage, Arcane Blast, Frostfire Bolt, Ice Lance; Fire DoTs crit.
- **Paladin:** Light's Vigil, Holy Shock reworked, Twist of Light; Blessing of Kings is baseline; blessings last 1 hour;
  Holy Strike (level 6) and Seal of Fury (tank seal whose Judgement taunts) are baseline; Judgement no longer consumes seals.
- **Priest:** Penance, Prayer of Mending, Binding Heal, Divine Aegis; Shadow gains Improved Mind Flay, Devouring Contagion, Early Demise.
- **Rogue:** Mutilate and Venom (Assassination), Flawless Execution and Hack and Slash (Combat), Cutthroat / Thousand Cuts (Subtlety); weapon specializations removed.
- **Shaman:** Lava Burst, Lightning Overload, Maelstrom Weapon, Rage of the Farseer, Water Shield, Riptide; Fire Nova is a spell.
- **Warlock:** Wrack, Pandemic, Malevolence, Demonic Pact, Demonic Knowledge, Incinerate, Bane of Havoc, Shadow and Flame; curses partially renamed to "Bane of …".
- **Warrior:** Bloodthrill, Weaponmaster (replaces the four weapon specializations), Vanguard (Charge in Defensive Stance),
  Master of Defense, Bastion, Boundless Rage, Raging Blows, Precision; Tactical Mastery is a baseline passive (Improved Tactical Mastery talent instead).

Per-class detail, tier by tier: `<class>/research/talents/forever/talent-trees.md`; what each beta build changed:
`_reference/data/forever-talents/README.md`.

## New-talent count per class (beta client 1.60.1.70291 vs Classic Era)

| Class | New | Removed | Class | New | Removed |
|---|---|---|---|---|---|
| Warlock | 22 | 20 | Priest | 14 | 8 |
| Paladin | 19 | 13 | Warrior | 11 | 10 |
| Hunter | 18 | 14 | Mage | 11 | 6 |
| Druid | 18 | 13 | Rogue | 10 | 8 |
| Shaman | 17 | 13 | | | |

Warlock, Paladin, Hunter, Druid and Shaman change the most — their Classic baselines need the heaviest rework.
Rogue and Mage change the least.

## Open questions

- When the beta cap rises to 30, and whether anything above 30 is tested before launch (no raid testing is planned).
- Launch respec prices; whether the Primary/Secondary talent tabs are dual spec.
- Raid buff/debuff limits (Classic's 16-debuff cap drove many talent choices).
- Which Classic mechanics stay: weapon skill and glancing blows (Rogue Weapon Expertise no longer gives weapon skill),
  spell hit caps, threat values (Sunder Armor now carries explicit threat).
- Data slips in the client (Aspect of the Hawk rank 6 at 55 RAP, Trueshot Aura rank 5 at +50, Penance rank 4's bolt
  smaller than rank 3's) — bugs or intended?
