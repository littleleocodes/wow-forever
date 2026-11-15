# TBC and WotLK PvP builds as evidence for Forever

Hand-kept. Research of 2026-11-15 (task: add the older method to the PvP work: the PvP builds of TBC and WotLK, which talents
they took, as evidence for our Forever builds).
- Data: `_reference/data/pvp-expansion-builds.json`.
- The Classic part: the `pvp-*` builds in `<class>/research/talents/classic-baseline/builds.json`.
- Forever's PvP rules: `pvp-research.md`. The plan: `pvp-plan.md`.

## What was collected

- **89 builds**, 47 TBC and 42 WotLK. Each holds 61 (TBC) or 71 (WotLK) points.
- **Classic-era guides.** TBC Classic plays the 2.4.3 trees and Wrath Classic the 3.3.5 trees.
  - Icy Veins: TBC Classic and Wrath Classic PvP guides.
  - Wowhead: TBC Classic and Wrath Classic PvP arena guides. Wowhead refuses scripts, so these are the Wayback Machine's copies
    (2024-2026 captures).
  - Skill-Capped: TBC only, 2025-2026.
  - wowtbc.gg: TBC, each guide made with a named top player.
  - Warcraft Tavern: WotLK calculator links, and seven TBC builds read from the guides' screenshots.
- **Original-era forum builds.** 28 posts from 15 ArenaJunkies threads, 2007-11 to 2010-01 (patches 2.3-2.4 and 3.1-3.3),
  read through the Wayback Machine.
- **One entry per spec and use.**
  - Identical builds from several sites are merged into one entry with every site as a source.
  - Other sites' versions of the same build are listed as variants in the entry's notes, with every talent difference.
  - Forum builds are separate entries.
- **Decoding.**
  - Wowhead-format strings are read on wowsims' TBC and WotLK trees. Their order and rank caps match Icy Veins' calculator data in
    all 54 trees.
  - Icy Veins, Warcraft Tavern and the 2007-2010 Wowhead hashes have their own encodings, decoded separately.
  - Every build is checked for its point total and rank caps.
- **Mapping to Forever** (`forever` in each build; Forever data build 1.60.1.70753, warrior and rogue 70755).
  - A talent is in Forever if the class's Forever tree has the same name, or a rename with the same effect. Renames are named in the
    note, for example Intensity as Reflection, Lethal Shots as Lethal Attacks, Improved Curse of Agony as Improved Bane of Agony.
  - A partial counterpart is named in the note but counts as absent.
  - Talents that became trainer spells in Forever count as absent: Omen of Clarity, Nature's Grasp, Aimed Shot, Blessing of Kings,
    Divine Spirit, Desperate Prayer.
- **Counting.**
  - "N of M" counts a class's entries that take the talent (both expansions), with the TBC and WotLK split in brackets.
  - A talent counts under its Forever name.
  - "Skipped" uses the entries with 30+ points in the talent's tree (often 2 to 5 builds).

## Druid

13 builds (TBC 7, WotLK 6).
- **TBC builds:**
  - Tree of Life Restoration 8/11/42: Icy Veins and wowtbc.gg identical; Skill-Capped and Wowhead variants.
  - Restoration hybrid 13/11/37: Icy Veins, Skill-Capped and wowtbc.gg identical.
  - Dreamstate/Restokin 34/0/27: Wowhead twice; a Skill-Capped variant.
  - Feral 1/46/14: Icy Veins; a Wowhead variant.
  - Three 2007 forum builds: 8/11/42, 13/11/37 and 27/0/34.
- **WotLK builds:**
  - Balance 57/0/14, Feral 0/55/16, Restoration 13/0/58 and Restoration 2v2 21/0/50: Icy Veins, each with a Wowhead variant.
  - Two 2009 forum Restoration builds: 13/0/58 and 24/0/47.
- **Consensus talents in Forever:**
  - Natural Shapeshifter 13 of 13.
  - Subtlety 11 (6/7, 5/6). Forever's only cuts threat; the dispel protection is gone.
  - Reflection (as Intensity), Improved Rejuvenation, Nature's Swiftness and Gift of Nature 10 each.
  - Swiftmend and Nature's Reach 9; Nature's Focus 8 (3/7, 5/6).
  - Furor 7 (6/7, 1/6); Insect Swarm 7.
  - Brutal Impact and Feral Charge 6 each (5/7, 1/6): TBC's Restoration dip into Feral.
  - Moonglow 6 (1/7, 5/6). Nature's Majesty and Nature's Splendor 5 each (0/7, 5/6): WotLK's Balance dip.
- **Skipped:**
  - Deep Restoration builds took no Naturalist, Tranquil Spirit or Improved Tranquility (TBC 0 of 5, WotLK 0 of 4).
  - Deep WotLK Restoration also skipped Furor and Living Seed.
  - Moonkin Form 2 of 13. Feral damage talents appear only in the two Feral builds.
- **Most-taken talents absent from Forever:**
  - Natural Perfection 9; Improved Mark of the Wild 9; Omen of Clarity 9 (a trainer spell in Forever).
  - Empowered Rejuvenation 8.
  - Nature's Grasp 7 of 7 TBC (a trainer spell in Forever, rooting the next melee attacker); Control of Nature 6 of 7 TBC.
  - Tree of Life 6; Master Shapeshifter 6 of 6 WotLK.
- **Imported talents:**
  - Nature's Majesty, Nature's Splendor and Genesis came with WotLK's Balance dip (5, 5 and 4 of 6 WotLK builds). Forever's
    Nature's Majesty covers all spells and melee; its Genesis gives +10% instead of +5%.
  - Wild Growth: 2 of 6 WotLK builds, both the deep 13/0/58 ones. Forever's heals the party only; its healing was doubled on
    2026-11-13.
  - Living Spirit 6 of 13.
  - Eclipse 1 of 6. Wowhead's Season 6 rank-1 Balance build skips it ("getting even a single long Starfire cast off at the higher
    ratings is unlikely"). Forever's Eclipse is a different talent.
  - Feral Swiftness and Shredding Attacks 2 (both Feral builds); Rend and Tear 1; Natural Reaction none.

## Hunter

9 builds (TBC 5, WotLK 4). No original-era WotLK hunter build was found.
- **TBC builds:**
  - Beast Mastery 41/20/0: Icy Veins; a Wowhead variant.
  - Marksmanship 7/41/13: Icy Veins; Wowhead and Skill-Capped variants.
  - Survival 7/11/43: Icy Veins.
  - Survival/Marksmanship 0/26/35: Skill-Capped, which calls it the most popular hunter PvP build.
  - A 2008 forum Marksmanship 11/41/9.
- **WotLK builds:**
  - Beast Mastery 53/15/3.
  - Marksmanship 7/51/13, Wowhead's battleground version.
  - Marksmanship arena 0/58/13: Wowhead; three Warcraft Tavern variants.
  - Survival 0/16/55.
- **Consensus talents in Forever:**
  - Lethal Attacks (as Lethal Shots) 9 of 9.
  - Mortal Shots and Hawk Eye 8. Wowhead's TBC guide skips Hawk Eye for arenas and takes it for battlegrounds.
  - Scatter Shot 6; Careful Aim 6 (2/5, 4/4); Entrapment 6.
  - Endurance Training 5 (4/5). Forever's no longer adds player health.
  - Improved Revive Pet 5 (4/5).
  - Improved Stings 5. It was taken for Viper Sting's drain, which Forever's version does not raise.
  - TBC only: Efficiency, Improved Concussive Shot and Improved Wing Clip 4 of 5; Deterrence and Clever Traps 3 of 5.
  - WotLK only: Improved Tracking and Survival Tactics 3 of 4.
- **Skipped:**
  - The Bestial Wrath line appears only in the two Beast Mastery builds.
  - Deep TBC Marksmanship skipped Improved Arcane Shot, Rapid Killing and Improved Hunter's Mark.
  - Deep WotLK Marksmanship skipped Efficiency and Improved Concussive Shot.
- **Most-taken talents absent from Forever:**
  - Aimed Shot 9 of 9. Forever's is a trainer spell without the -50% healing.
  - Go for the Throat 6; Survival Instincts 5.
  - Humanoid Slaying 4 of 5 TBC. Improved Tracking replaces it in Forever.
  - Master Marksman and Silencing Shot 4; Readiness, Wyvern Sting and Expose Weakness 3.
- **Imported talents:**
  - Careful Aim 6 of 9 and Improved Stings 5.
  - Improved Tracking and Survival Tactics 3 of 4 WotLK.
  - Focused Fire 3; Rapid Killing and Resourcefulness 2; Rapid Recuperation 1.
  - No evidence for Forever's own Lone Wolf, Summon Hawk, Sniper Shot, Expose Prey, Predator's Edge, Strider Kick or Lacerating
    Strikes.

## Mage

8 builds (TBC 4, WotLK 4).
- **TBC builds:**
  - Deep Frost 17/0/44: identical on Icy Veins, Skill-Capped, wowtbc.gg (with Rivah) and Wowhead; two variants.
  - PoM Pyro 44/17/0: Icy Veins.
  - 2008 forum builds: PoM Pyro 33/28/0 and Deep Frost 17/0/44.
- **WotLK builds:**
  - Deep Frost 20/0/51: Icy Veins and Wowhead identical; three Warcraft Tavern variants, one for battlegrounds.
  - Fire 19/52/0 and Arcane 53/7/11.
  - A 2009 forum Deep Frost 20/0/51.
- **Consensus talents in Forever:**
  - Magic Absorption, Arcane Resilience (as Arcane Fortitude) and Improved Counterspell 8 of 8.
  - Arcane Subtlety 7; Arcane Concentration 5 (4/4, 1/4).
  - All four Frost builds: Improved Frostbolt, Ice Shards, Arctic Reach, Shatter, Cold Snap, Ice Barrier and Winter's Chill.
  - Frostbite and Permafrost 5 (the Frost builds plus one Arcane build).
  - Fire and Arcane builds: Incineration 4; Presence of Mind, Arcane Instability, Arcane Power, Impact, Ignite, Flame Throwing and
    Pyroblast 3.
- **Skipped:**
  - Deep Frost builds took no Frost Channeling, Improved Cone of Cold or Frozen Core (0 of 2 in each expansion). Skill-Capped's TBC
    variant takes Improved Cone of Cold.
  - Elemental Precision 0 of 2 TBC; Precision 0 of 2 WotLK (one Warcraft Tavern variant takes it).
- **Most-taken talents absent from Forever:**
  - Arcane Focus 7; Icy Veins 5; Magic Attunement 5.
  - Summon Water Elemental 4 (every Frost build); Ice Floes and Piercing Ice 4.
  - Focus Magic 4 of 4 WotLK; Torment the Weak and Spell Impact 3.
- **Imported talents:**
  - Fingers of Frost: 2 of 2 WotLK Frost builds.
  - Incineration 4; Improved Fire Blast and Arcane Shielding 2 of 4 WotLK; Missile Barrage 1 (Arcane); Heating Up (as Hot Streak)
    1 (Fire); Arcane Impact none.
  - Forever's Winter's Chill is a different talent (a Cone of Cold buff, not Frost crit), so its 4 of 8 is no evidence for it.
  - Ice Lance, Arcane Blast and Frostfire Bolt were trainer spells in TBC and WotLK, so the builds say nothing about them as
    talents.

## Paladin

12 builds (TBC 6, WotLK 6).
- **TBC builds:**
  - Holy 41/20/0 for 2v2: identical on Skill-Capped, wowtbc.gg (with Eroth) and Wowhead; an Icy Veins variant.
  - Holy 41/20/0 for 3v3 and 5v5: wowtbc.gg and Wowhead identical; variants.
  - Shockadin 40/21/0 (Skill-Capped).
  - Retribution 0/20/41 and Reckoning Retribution 0/27/34.
  - A 2008 forum Holy 41/20/0.
- **WotLK builds:**
  - Holy 52/19/0 and Retribution 0/19/52: Icy Veins and Wowhead identical in both.
  - Protection/Retribution 0/28/43 and Protection 0/53/18.
  - 2009 forum builds: Holy 51/20/0 and Protection/Holy 19/52/0.
- **Consensus talents in Forever:**
  - Guardian's Favor and Improved Righteous Fury 12 of 12.
  - Stoicism 10 (4/6, 6/6); Improved Hammer of Justice 9; Redoubt 8 (6/6, 2/6).
  - Divine Intellect, Spiritual Focus, Healing Light and Toughness 7.
  - All six Holy builds: Holy Shock, Divine Favor, Holy Power and Illumination.
  - Precision 5 of 6 TBC.
- **Skipped:**
  - Deep Holy builds skipped Divine Strength and Pure of Heart (TBC 0 of 4) and Improved Lay on Hands (TBC 0 of 4, WotLK 0 of 2).
  - Purifying Power: TBC 1 of 4, WotLK 0 of 2.
  - Deep TBC Retribution skipped Eye for an Eye, Crusade and Fanaticism. Deep WotLK Retribution skipped Seal of Command and
    Deflection.
- **Most-taken talents absent from Forever:**
  - Blessing of Kings 6 of 6 TBC (a trainer spell in Forever).
  - Divine Sacrifice and Divine Guardian 6 of 6 WotLK.
  - Improved Concentration Aura 7; Sanctified Light and Holy Guidance 6.
  - Light's Grace, Divine Illumination and Aura Mastery 5; Divinity 5 of 6 WotLK.
- **Imported talents:**
  - Stoicism 10 of 12. Forever's cuts stun and charm duration by 20% (2026-11-02).
  - Sacred Duty 3; Infusion of Light 2 of 6 WotLK (both WotLK Holy entries); Purifying Power and Sanctified Judgement 1.
  - Holy Power is a different effect in Forever: crit healing bonus, not crit chance.
  - No evidence for Forever's own Templar's Bulwark, Divine Precision (its silence reduction is a PvP talent), Oath of Light, Light's
    Vigil, Unsealed Wrath or Champion of the Light.

## Priest

10 builds (TBC 6, WotLK 4).
- **TBC builds:**
  - Discipline 49/12/0: Icy Veins; wowtbc.gg (with Xeriyo), Skill-Capped and Wowhead variants.
  - Discipline with Blackout 46/11/4: Skill-Capped; two Wowhead variants.
  - Shadow 20/0/41: Icy Veins; a Wowhead variant.
  - 2008 forum builds: Shadow 20/0/41, Shadow 18/0/43 and Discipline 42/19/0.
- **WotLK builds:**
  - Discipline 57/14/0 and Shadow 20/0/51: Icy Veins, each with a Wowhead variant.
  - Holy 17/54/0 (Wowhead).
  - A 2009 forum Discipline 54/17/0.
- **Consensus talents in Forever:**
  - Inner Focus 10 of 10; Meditation 9; Improved Power Word: Shield 8.
  - Silent Resolve 7 (3/6, 4/4); Mental Agility 7.
  - Martyrdom 6 (6/6, 0/4); Improved Mana Burn 6 (5/6, 1/4); Twilight Focus (as Healing Focus) 6.
  - Power Infusion and Mental Strength 5.
  - All four Shadow builds: Silence, Shadowform, Vampiric Embrace, Mind Flay, Improved Psychic Scream, Shadow Weaving, Darkness,
    Shadow Reach, Shadow Focus and Improved Shadow Word: Pain.
  - Blackout 4 of 6 TBC.
  - Improved Inner Fire 4 of 4 WotLK, 0 of 6 TBC (its extra charges came with WotLK).
- **Skipped:**
  - Deep TBC Discipline took no Improved Inner Fire, Improved Power Word: Fortitude, Improved Divine Spirit, Force of Will or Wand
    Specialization (0 of 3).
  - Deep WotLK Discipline skipped Twin Disciplines and Martyrdom (0 of 2).
  - Deep TBC Shadow skipped Spirit Tap, Shadow Affinity and Shadow Power (0 of 3).
- **Most-taken talents absent from Forever:**
  - Unbreakable Will 10 of 10. It was removed; Forever's Silent Resolve now cuts stun, fear and silence durations by 15%.
  - Absolution 6 of 6 TBC.
  - Pain Suppression, Focused Will, Reflective Shield and Focused Power 5.
  - Misery, Vampiric Touch and Improved Vampiric Embrace 4 (Shadow).
  - Divine Spirit 3 of 6 TBC and Desperate Prayer 3 of 4 WotLK (both trainer spells in Forever).
- **Imported talents:**
  - Penance, Soul Warding and Renewed Hope: 2 of 2 WotLK Discipline builds. Divine Aegis 1 of 2; Twin Disciplines none.
  - Forever's Power Infusion raises damage and healing instead of haste.
  - No evidence for Forever's own Power in Light, Holy Precision, Litany of Light, Improved Mind Flay, Early Demise or Devouring
    Contagion.

## Rogue

11 builds (TBC 6, WotLK 5).
- **TBC builds:**
  - Subtlety/Shadowstep 20/0/41: Skill-Capped and wowtbc.gg (with Mir) identical; five variants from Icy Veins, Skill-Capped and
    Wowhead.
  - Warcraft Tavern's Mutilate 41/20/0 (world PvP and battlegrounds), Mutilate 44/0/17 (arena and battlegrounds) and Midz's
    Mutilate 51/0/10.
  - Warcraft Tavern's Combat HARP 0/33/28.
  - A 2008 forum Combat/Subtlety 0/33/28.
- **WotLK builds:**
  - Subtlety/Shadow Dance 12/3/56: Icy Veins; Warcraft Tavern and Wowhead variants.
  - Mutilate 44/4/23 and Combat 17/54/0 (Wowhead).
  - Two 2009 forum Mutilate/Preparation builds from the Hydramist.net guide: 41/5/25 (2v2) and 44/2/25 (3v3).
- **Consensus talents in Forever:**
  - Malice, Dirty Tricks and Camouflage 9 of 11.
  - Lethality and Elusiveness 8; Vigor 8 (3/6, 5/5).
  - Preparation, Dirty Deeds, Initiative, Master of Deception, Relentless Strikes, Vile Poisons, Puncturing Wounds and Dual Wield
    Specialization 7.
  - All six Mutilate builds: Mutilate, Seal Fate and Cold Blood. Coup de Grace (as Improved Eviscerate) and Opportunity 6.
  - Hemorrhage 4 (3/6, 1/5); Improved Kidney Shot 4; Ghostly Strike 3 of 6 TBC.
- **Skipped:**
  - Deep Assassination builds took no Remorseless Attacks (0 of 3 in each expansion) and in TBC no Improved Poisons.
  - Deep WotLK Assassination skipped Ruthlessness, Improved Expose Armor and Hunger for Blood.
  - The TBC Combat builds (mace) skipped Riposte, Deflection, Aggression and the sword, dagger and fist specializations.
- **Most-taken talents absent from Forever:**
  - Fleet Footed 6; Murder, Master Poisoner and Quick Recovery 5; Deadliness and Find Weakness 4.
  - Deadly Brew and Overkill 3 of 5 WotLK; Shadowstep and Cheat Death 2.
  - Forever has no Shadowstep, Shadow Dance, Cloak of Shadows, Shiv or Dismantle.
- **Imported talents:**
  - Mutilate: 6 of 11, every Assassination build. It is Forever's 31-point talent; it was the 41-point talent in TBC and WotLK.
  - Puncturing Wounds 7 (in Forever's Combat tree); Dirty Tricks 9.
  - Hack and Slash none: the WotLK Combat build took Close Quarters Combat. Forever's merges the weapon specializations.
  - No evidence for Forever's own Shank line (Venom, Boot Knife, Flash of Steel), Death Mark, Quick Getaway, Blood Splatter,
    Composure or Flawless Execution.

## Shaman

10 builds (TBC 5, WotLK 5).
- **TBC builds:**
  - Elemental 40/0/21, Enhancement 0/46/15, Restoration with Toughness 0/20/41 (2v2) and Restoration with Mana Tide 0/9/52
    (3v3/5v5): each identical on Icy Veins and Wowhead.
  - A 2008 forum Restoration 0/9/52, with eight posters' variants.
- **WotLK builds:**
  - Elemental 60/11/0, Enhancement 17/54/0 and Restoration 0/17/54: each identical on Icy Veins and Wowhead. Warcraft Tavern's
    Elemental variants include a battleground build.
  - 2009 forum builds: Elemental 55/16/0 and Restoration 0/15/56.
- **Consensus talents in Forever:**
  - Improved Ghost Wolf 9 of 10; Ancestral Knowledge 8.
  - Tidal Focus 7 (5/5, 2/5); Guardian Totems 7.
  - Ancestral Healing and Nature's Swiftness 6.
  - Thundering Strikes and Shamanistic Focus 6 (1/5, 5/5).
  - Totemic Focus 5 of 5 TBC; Healing Focus and Purification 5.
  - Earth's Grasp 4 of 5 WotLK; Mana Tide Totem 4.
  - All three Elemental builds: Concussion, Elemental Focus, Call of Thunder, Elemental Fury, Lightning Overload and Elemental
    Alacrity (as Lightning Mastery).
- **Skipped:**
  - Deep TBC Restoration took no Improved Healing Wave, Healing Way, Improved Reincarnation or Improved Chain Heal (0 of 3). In the
    2008 "2.4 Resto Spec" thread, eight of the nine builds posted took Improved Healing Wave 5 (the opening post did not), so the
    eras disagree (see the variants).
  - Deep WotLK Restoration skipped Totemic Focus, Tidal Mastery and Improved Reincarnation.
  - Deep WotLK Elemental skipped Convection and Elemental Devastation.
- **Most-taken talents absent from Forever:**
  - Healing Grace 6.
  - Nature's Guidance and Totemic Mastery 5 of 5 TBC.
  - Earth Shield 5 (every Restoration build); Focused Mind and Nature's Blessing 5.
  - Elemental Mastery and Nature's Guardian 3; Shamanistic Rage 2 (both Enhancement builds).
- **Imported talents:**
  - Shamanistic Focus 6 (5/5 WotLK); Lightning Overload 3 (every Elemental build).
  - Elemental Reach: 2 of 2 WotLK Elemental builds. Riptide: 2 of 2 WotLK Restoration builds.
  - Maelstrom Weapon, Mental Dexterity and Improved Stormstrike 1 (the one WotLK Enhancement build); Spirit Weapons and Mental
    Quickness 2 (both Enhancement builds).
  - Forever's versions are weaker or different:
    - Maelstrom Weapon: Lightning Bolt only, 6-10 procs a minute since 2026-11-10.
    - Stormstrike: 100% weapon damage, 8 s cooldown.
    - Riptide: no direct heal.
    - Mana Tide Totem: 88 mana a tick.
    - Toughness: no slow reduction, which was why TBC's 2v2 and Enhancement builds took it.
  - No evidence for Forever's own Water Shield talent, Rage of the Farseer, Earthbound, Mindfulness or Natural Grace.

## Warlock

9 builds (TBC 5, WotLK 4).
- **TBC builds:**
  - SL/SL 25/36/0: Icy Veins; Skill-Capped and Wowhead variants.
  - Unstable Affliction 41/20/0: Skill-Capped; a Wowhead variant.
  - Unstable Affliction/Shadowburn 45/5/11 (Wowhead).
  - 2008 forum builds: SL/SL 30/31/0 and Unstable Affliction 43/7/11.
- **WotLK builds:**
  - Affliction 52/17/2: Icy Veins; a Wowhead variant.
  - Destruction 0/17/54: Icy Veins, with its 2v2 variant.
  - 2010 forum builds: Affliction 54/17/0 and Destruction 3/17/51.
- **Consensus talents in Forever:**
  - Demonic Embrace 9 of 9.
  - Suppression, Improved Corruption, Grim Reach, Nightfall, Siphon Life, Fel Vitality (as Fel Stamina and Fel Intellect), Fel
    Domination, Demonic Aegis and Master Summoner 7.
  - Improved Life Tap, Soul Siphon (5/5 TBC), Amplify Curse, Curse of Exhaustion, Improved Health Funnel, Soul Link (2/5, 4/4),
    Fel Concentration and Shadow Mastery 6.
  - Improved Bane of Agony (as Improved Curse of Agony) 4 of 5 TBC.
- **Skipped:**
  - The TBC SL/SL builds took no Improved Imp, Improved Voidwalker, Improved Succubus, Demonic Tactics or Summon Felguard (0 of 2).
  - Deep TBC Affliction skipped Improved Drain Soul (0 of 4) and mostly Improved Curse of Weakness and Malediction.
  - Deep WotLK Affliction skipped Improved Curse of Agony, Dark Pact and Improved Felhunter (0 of 2).
  - Deep WotLK Destruction skipped Cataclysm and Soul Leech.
- **Most-taken talents absent from Forever:**
  - Empowered Corruption and Shadow Embrace 7.
  - Contagion, Improved Howl of Terror and Unstable Affliction 5.
  - Improved Healthstone 4 of 5 TBC; Fel Synergy 4 of 4 WotLK.
  - WotLK Affliction: Haunt and Everlasting Affliction 2 of 2.
  - WotLK Destruction: Shadowfury, Backlash, Nether Protection, Backdraft and Chaos Bolt 2 of 2.
- **Imported talents:**
  - Grim Reach, Demonic Aegis and Fel Vitality 7; Soul Siphon 6.
  - Pandemic: 2 of 2 WotLK Affliction builds. Forever's is a crit damage bonus.
  - Molten Skin, Fire and Brimstone and Shadow and Flame: 2 of 2 WotLK Destruction builds. Forever's Shadow and Flame is a different
    talent.
  - Demonic Knowledge 1 of 5 TBC; Decimation, Improved Felhunter and Demonic Pact none (WotLK's versions differ from Forever's).
  - Soul Link (6 of 9) is the strongest signal for a Forever talent: Forever's moves 30% of damage to the demon (TBC/WotLK: 20%).
    Soul Link builds won the level-30 Forever Open (`pvp-research.md`).
  - No evidence for Forever's own Wrack, Bane of Havoc, Demonic Brand, Soul Harvest or Malevolence.

## Warrior

7 builds (TBC 3, WotLK 4).
- **TBC builds:**
  - Arms 41/17/3: identical on Icy Veins, Skill-Capped and two Wowhead guides. Warcraft Tavern's 2026 stun build and its
    anti-melee variation are variants.
  - Warcraft Tavern's Arms Poleaxe 41/17/3, for battlegrounds.
  - A 2008 forum Arms/Fury 35/23/3.
- **WotLK builds:**
  - Arms 60/11/0: Icy Veins and Warcraft Tavern identical; Wowhead and Warcraft Tavern variants.
  - Protection 13/7/51: Icy Veins; a Wowhead variant.
  - Fury 18/53/0 (Wowhead).
  - A 2009 forum Arms 57/14/0.
- **Consensus talents in Forever:**
  - Deflection, Deep Wounds, Impale, Cruelty and Improved Tactical Mastery (as Tactical Mastery) 7 of 7.
  - Iron Will, Two-Handed Weapon Specialization and Piercing Howl 6.
  - Improved Overpower, Improved Hamstring, Mortal Strike, Booming Voice and Blood Craze 5.
  - Death Wish, Improved Intercept and Enrage 4.
  - Anger Management 3 of 3 TBC; Weaponmaster (as Poleaxe Specialization) 3: the TBC battleground build and both WotLK Arms builds.
- **Skipped:**
  - Deep TBC Arms took no Improved Heroic Strike, Improved Rend, Improved Charge, Improved Thunder Clap or Sword Specialization
    (0 of 3).
  - Deep WotLK Arms took no Improved Heroic Strike, Anger Management, Improved Slam, Sword Specialization or Mace Specialization
    (0 of 2).
- **Most-taken talents absent from Forever:**
  - Blood Frenzy and Second Wind 5; Endless Rage and Commanding Presence 4.
  - Armored to the Teeth 4 of 4 WotLK.
  - Improved Mortal Strike and Weapon Mastery 3; Mace Specialization (TBC's stun) 2 of 3 TBC.
  - WotLK Arms: Taste for Blood, Trauma, Strength of Arms, Juggernaut, Unrelenting Assault, Sudden Death, Wrecking Crew and
    Bladestorm 2 of 2.
- **Imported talents:**
  - Improved Whirlwind 1 (Fury); Focused Rage 1 (Protection).
  - Weaponmaster replaces the weapon specializations every Arms build took.
  - No evidence for Forever's own Bloodthrill (the nearest to Taste for Blood), Spearing Strike, Gore Drinker, Reckless Swings,
    Vanguard or Bastion.

## Across classes

- **What the consensus lists are made of:** control and anti-control, mobility, dispel protection and mana.
  - Control and anti-control: Improved Counterspell 8/8, Silence in every Shadow build, Stoicism, Iron Will, Improved Hammer of
    Justice, Elusiveness.
  - Mobility: Improved Ghost Wolf, Feral Swiftness, Improved Sprint, Feral Charge.
  - Dispel protection: druid Subtlety, Silent Resolve. Forever kept Vile Poisons' dispel resistance and dropped it from both
    Subtlety and Silent Resolve.
  - Mana: Meditation, Mental Agility, Arcane Concentration, Tidal Focus.
- **Standard talents now gone or turned into trainer spells:**
  - Gone: Unbreakable Will 10/10, Natural Perfection, Improved Mark of the Wild, Arcane Focus, Absolution, Nature's Guidance,
    Totemic Mastery, Empowered Corruption, Shadow Embrace, Blood Frenzy, Second Wind, Fleet Footed.
  - Trainer spells: Aimed Shot 9/9 (without its healing reduction), Blessing of Kings, Omen of Clarity, Nature's Grasp.
- **Same names, different effects in Forever.** These are not evidence for the Forever versions: Winter's Chill, Shadow and Flame,
  Eclipse, Holy Power, Power Infusion, Mental Quickness, and Forever's own Lightning Mastery (TBC/WotLK's Lightning Mastery is
  Forever's Elemental Alacrity).

## Caveats

- **Arenas and resilience shaped these builds; Forever has neither.**
  - Forever has no arenas, ratings, resilience or PvP damage modifiers. Crits against players are at full effect since 2026-10-08
    (`pvp-research.md`).
  - Resilience lowered the chance to be crit and crit damage in both expansions, and in WotLK player damage in general, which
    lengthened matches. Forever's burst lands at PvE strength. An inference, not measured: these builds likely undervalue damage and
    crit talents for Forever, and overvalue mana efficiency.
  - The builds are tuned for 2v2, 3v3 and 5v5 brackets on pillar maps, where long matches make mana and dispel protection decisive.
    Only a few builds are for battlegrounds or world PvP: Wowhead's battleground Marksmanship, Warcraft Tavern's Poleaxe Arms, Mutilate
    41/20/0 and Frost battleground variant, Hawk Eye picks.
- **Point budgets and tree depth differ.**
  - TBC builds have 61 points (level 70), WotLK 71 (level 80), Forever 51 (level 60).
  - Capstones are at 41 points (TBC) and 51 (WotLK); Forever's trees have 7 rows and a 31-point capstone. Hybrids such as 25/36/0
    or 17/0/44 have no direct Forever equivalent.
  - Several talents changed tree in Forever: Puncturing Wounds to Combat, Hawk Eye to Marksmanship, Iron Will to Protection, Heart
    of the Wild and Furor between Feral and Restoration, Divine Intellect to Protection, Unyielding Faith to Retribution.
- **Numbers differ.** The `forever` notes give each talent's material difference.
- **Agreement between sites is not always independent.**
  - Many Icy Veins and Wowhead builds are identical.
  - Classic-era guides were written with hindsight on a settled meta.
  - The 2007-2010 forum posts are single players' choices, not ladder statistics.
- **The counts weigh specs unevenly.** Every taken talent counts, filler included. Some specs have several entries: 6 of the 13
  druid builds are deep Restoration.
- **Transcriptions.** Seven Warcraft Tavern TBC builds were read from screenshots by hand. Each sums to 61 with legal ranks.

## Sources not reached, excluded or disagreeing

- **Not reached:**
  - Wowhead refuses scripts (HTTP 403), so its guides were read from Wayback Machine copies.
  - legacy-wow.com's 3.3.5 PvP guides returned Cloudflare error 520.
  - Skill-Capped has no WotLK guides (404). wowtbc.gg has TBC PvP guides for five specs only, and no WotLK PvP guides were found.
  - Warcraft Tavern shows builds only as images on its TBC pages (rogue and warrior read) and on eleven WotLK talent pages (not
    read).
  - No original-era WotLK hunter build was found.
- **Excluded:**
  - Wowhead WotLK links that hold 68 or 69 points: the Balance "58/0/13" (69), Demonology 0/53/16 (69) and Destruction, whose
    heading copies Demonology's and whose link holds 68.
  - Warcraft Tavern's WotLK Feral calculator links sit in its comments, which call the guide's builds bad.
  - A Warcraft Tavern WotLK Subtlety link that encodes an edit history (106 points).
  - A death knight link.
- **Disagreements:**
  - TBC Restoration shaman: the Classic-era guides take Shield Specialization 5 and skip Improved Healing Wave. The 2008 thread's
    builds take Ancestral Knowledge 5 instead of Shield Specialization, and eight of its nine take Improved Healing Wave 5.
  - WotLK rogue: the Classic-era guides lead with Subtlety and Shadow Dance; the 2009-2010 posts (Hydramist.net, Thakeelol, Zoltan)
    play Mutilate with Preparation.
  - TBC Discipline: Icy Veins' and Wowhead's 49/12/0 differ by ten points (Force of Will and Improved Inner Fire against Mental
    Agility and Focused Power).
  - WotLK Balance: Icy Veins takes Eclipse; Wowhead's Season 6 rank-1 build takes Dreamstate and Genesis instead.
  - Warcraft Tavern's WotLK Arms headings and links disagree: its "57/14/0 Improved Hamstring Build" link holds 60/11/0. Wowhead's
    WotLK Protection paladin (heading 7/52/12, link 0/53/18) and Enhancement (heading 20/51/0, link 17/54/0) also disagree. The
    links are used.
- **Agreement:** the TBC Deep Frost 17/0/44 is identical on four sites, and the TBC Arms 41/17/3 on three sites and two Wowhead guides.

## Sources

- **Icy Veins, TBC Classic** (pages show "Last Updated: Jan 12, 2026"; authors Abide, Impakt, Seksixeny, Sellin):
  https://www.icy-veins.com/tbc-classic/<slug>-pvp-guide for arms-warrior, beast-mastery-hunter, demonology-warlock,
  discipline-priest, elemental-shaman, enhancement-shaman, feral-druid, fire-mage, frost-mage, holy-paladin,
  marksmanship-hunter, restoration-druid, restoration-shaman, retribution-paladin, shadow-priest, subtlety-rogue,
  survival-hunter.
- **Icy Veins, Wrath Classic** (updated 2023-01-18 to 2024-01-10; authors Abide, Chanimal, Farmerfarms, Impakt, Seksixeny, Sellin):
  https://www.icy-veins.com/wotlk-classic/<slug>-pvp-guide for affliction-warlock, arcane-mage, arms-warrior, balance-druid,
  beast-mastery-hunter, destruction-warlock, discipline-priest, elemental-shaman, enhancement-shaman, feral-druid, fire-mage,
  frost-mage, holy-paladin, marksmanship-hunter, protection-paladin, protection-warrior, restoration-druid,
  restoration-shaman, retribution-paladin, shadow-priest, subtlety-rogue, survival-hunter.
- **Wowhead, TBC Classic and Wrath Classic PvP arena guides** via the Wayback Machine (dates and authors per build in the JSON):
  https://www.wowhead.com/tbc/guide/classes/<path> and https://www.wowhead.com/wotlk/guide/classes/<path>.
  - TBC: druid/balance/dps-pvp-arena, druid/feral/dps-pvp-arena, druid/healer-pvp-arena, hunter/dps-pvp-arena, mage/dps-pvp-arena,
    paladin/holy/healer-pvp-arena, paladin/retribution/dps-pvp-arena, priest/healer-pvp-arena, priest/shadow/dps-pvp-arena,
    rogue/dps-pvp-arena, shaman/elemental/dps-pvp-arena, shaman/enhancement/dps-pvp-arena, shaman/healer-pvp-arena,
    warlock/dps-pvp-arena, warrior/dps-pvp-arena, warrior/protection/tank-pvp-arena.
  - WotLK: druid/balance, druid/feral (dps and tank), druid/restoration, hunter/beast-mastery, hunter/marksmanship,
    hunter/survival, mage/arcane, mage/fire, mage/frost, paladin/holy, paladin/protection, paladin/retribution,
    priest/discipline, priest/holy, priest/shadow, rogue/assassination, rogue/combat, rogue/subtlety, shaman/elemental,
    shaman/enhancement, shaman/restoration, warlock/affliction, warrior/arms, warrior/fury, warrior/protection, each
    .../<role>-pvp-arena.
- **Skill-Capped, TBC** (published 2025-01-17, updated 2026-01-01; hunter 2026-01-18):
  https://www.skill-capped.com/wowarticles/tbc/guides/<slug>-pvp-guide/talents/ for affliction-warlock, arms-warrior,
  discipline-priest, frost-mage, holy-paladin, hunter, restoration-druid, subtlety-rogue.
- **wowtbc.gg, TBC** (undated): https://wowtbc.gg/pvp-class-guides/<slug>/ for discipline-priest (Xeriyo), frost-mage (Rivah),
  holy-paladin (Eroth), restoration-druid (Xeriyo), subtlety-rogue (Mir).
- **Warcraft Tavern** (author Nevermore; undated):
  - WotLK: https://www.warcrafttavern.com/wotlk/guides/ frost-mage-pvp-talents-builds, pvp-arms-warrior-talents-builds,
    pvp-elemental-shaman-talents-builds-glyphs, pvp-marksmanship-hunter-talents-builds-glyphs,
    pvp-subtlety-rogue-talents-builds-glyphs, pvp-survival-hunter-talents-builds-glyphs.
  - TBC screenshots: https://www.warcrafttavern.com/tbc/guides/rogue-mutilate-pvp/, /rogue-pvp-combat-harp/, /pvp-arms-warrior/.
- **ArenaJunkies** via the Wayback Machine (http://www.arenajunkies.com/topic/<id>-<slug>/):
  - 3691 Shadow Priest + Rogue 2v2 (2007-11-25).
  - 5682 Druid + Warrior 2v2 (2007-12-19).
  - 11524 2.4 Resto Spec (2008-02-26).
  - 11593 2.4: 30/31/0 vs normal SL/SL (2008-02-27).
  - 13556 2.4 Mage specs (2008-03-16).
  - 13997 Shadow Priest/Rogue 2v2 (2008-03-20).
  - 20436 Paladin/Warrior (2008-05-11).
  - 20569 Shadow Priest/Unstable Affliction Warlock (2008-05-12).
  - 21071 2v2 Disc Priest/MM Hunter (2008-05-15).
  - 100899 Druid/Warrior 2v2 (2009-09-27).
  - 109580 PLD (2009-11-15).
  - 113662 Holy Paladin/Disc Priest/Warrior (2009-12-08).
  - 113663 Hydramist.net RP, RM, RMP and 5s specs (2009-12-08).
  - 113750 Frost Mage/Ele Shaman (2009-12-08).
  - 115272 3.3 Basic rogue guide (2009-12-16).
  - 117560 2v2 Resto Shaman/Rogue (2009-12-31).
  - 121404 2v2 Rogue Mage deep guide (2010-01-21).
  - 122518 Warlock 3.3 Specs (2010-01-26).
  - The exact archive URLs are in the JSON.
- **Tree data:**
  - https://github.com/wowsims/tbc (ui/core/talents/*.ts) and https://github.com/wowsims/wotlk (ui/core/talents/trees/*.json).
  - Icy Veins' calculator data: https://static.icy-veins.com/json/tbc-talent-calculator/ and /wotlk-talent-calculator/.
