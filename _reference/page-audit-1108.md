# Full page read of 2026-11-08 (hand-kept)

User, 2026-11-08: "Make sure we're auditing the github as the runs complete and EVERY single part of every single page of every single
spec and class and raid and leveling and everything is up to date and makes sense ... Self audit, self audit, self audit."

One read-only reader per class read every player page (README, leveling/, raid/, macros.md, keybinds.md, the by-level guides) and
checked each claim against the talent and spell data. Every row is a reader's finding, condensed: **verify before fixing**. Status:
open / fixed (commit) / wrong (the reader was mistaken). Sources: GUIDES = `_reference/data/guides/<class>.json`, STEPS =
`_reference/data/leveling-steps.json`, LG = `_reference/data/level-guides/<class>.json`, BUILDS = proposed-builds.json, SR =
`simple_rotation.py`, RM = `render_modes.py`, hand = hand-written file. The page audit `dead` check and section O of
`page-audit.md` are the automatic side of the same work.

## Systemic (several classes: fix once, in the generator or the data)

| # | Finding | Source | Status |
|---|---|---|---|
| S1 | "Advanced" calls auras and seals cooldowns: "Seal of the Crusader: a cooldown, use it ... whenever it is ready", "Retribution Aura: a cooldown" (paladin Ret, Prot-Ret, Shockadin raid) | SR.advanced | open |
| S2 | A rotation line whose talent the build lacks is still printed next to a "Not in this build ... skip the lines" banner: Ele-Enh raid "Lightning Bolt at 5 Maelstrom Weapon"; Elemental leveling step 1 Lightning Mastery; Balance leveling Insect Swarm (also in its signature list); Discipline leveling Power Infusion and Renewed Hope; Shadow leveling Inner Focus; rogue Combat Blade Flurry/Adrenaline Rush, Combat-Subtlety Boot Knife/Death Mark/Riposte/Preparation, Assassination Riposte; warrior Arms leveling Spearing Strike, every warrior list "Reckless Swings (if your build has it)" | SR, STEPS, RM | open |
| S3 | A weapon imbue read as the filler: "Rockbiter Weapon is your filler: cast it whenever nothing above is ready" (Enhancement, Ele-Enh raid) | SR | open |
| S4 | One fire totem slot: Magma Totem and Searing Totem both under "keep up all fight" (Enhancement, Ele-Enh raid) | SR | open |
| S5 | A long-cooldown emergency spell in the priority list: Protection paladin "Lay on Hands" step 5 | SR | open |
| S6 | An always-ready line above conditioned lines ("press the first one that is ready"): Hamstring above Bloodrage and Heroic Strike (Fury, Arms raid), its real condition dropped | SR | open |
| S7 | A signature builder under "Advanced" instead of the list: Subtlety raid Hemorrhage (about 30 casts a fight); the list ends "your white swings do the rest" | SR.advanced | open |
| S8 | Healer builds hold lab-zero points on off-role talents (page-audit O2-O3): Resto druid Improved Wrath/Moonfire/Furor/Natural Shapeshifter; Holy paladin Divine Strength 5 (1 gate, 4 free), Benediction 5, Pursuit of Justice, Unyielding Faith, Deflection 2, Improved/Sanctified Judgement; Resto shaman Totemic Focus 5 (Improved Healing Wave untaken, Healing Wave 3/4 of its healing); Disc priest Silent Resolve 3, Holy Precision, Power in Light, Blessed Recovery 2, Holy Reach 2 while Power Infusion is untaken; Holy priest Power in Light 2, Holy Nova, Holy Binding, Improved Power Word: Shield 3 | BUILDS, heallab | open |
| S9 | Raid pages show standard-gear DPS next to tier-table DPS of other talents with "(ties this build)" and no word on why they differ: Feral 758 vs 834; Ele-Enh 917 vs 755 (ranked above Elemental while its tier numbers are below); Combat 666 vs 744 (a different 16/33/2 build); Balance 33/0/18 vs best 36/0/15 | RM tier_lines | open |
| S10 | Hand-written class README sections ("Roles and specs", "Forever headline changes") still on 70425/70291 facts and rankings: shaman, paladin, druid, rogue (Thousand Cuts, Cutthroat, Quietus, Murder, 17/17/19), warrior (Arms "best", Slam 18 s, 52 talents), priest (SW:D 10%, Binding Heal "talent", Smite 17%) | hand README | open |
| S11 | Potion macros on keys a guide uses: druid C (Innervate from 40), paladin C (Swift Judgement in three guides), warrior C (Heroic Strike from 40) | hand macros, LG | open |
| S12 | One keybinds.md per class, built on one spec, linked from every spec page without saying so: shaman (Enhancement), rogue (Combat: Kick "never interrupts" vs Assassination/Subtlety keep Kick), priest (Shadow: Holy/Disc/Smite guides use Smite on Q), druid (Feral; Balance moves Moonfire/Starfire) | hand keybinds | open |
| S13 | Signature lines count spells the page says are never cast or the build cannot have: Feral leveling Primal Bite (29 points), Shadow leveling Devouring Plague ("Skip"), Disc leveling Holy Fire ("never cast"), Prot-Ret Seal of Fury, Fury leveling Whirlwind | signature text | open |
| S14 | Free points in leveling orders: Ret 49-60 (Vindication 2-3, Purifying Power 2, Sacred Duty while Improved Seals 3/5, Champion of the Light 3/5); Prot-Ret Redoubt 2; Feral Nature's Reach 2, Improved Wrath 59, Nature's Splendor 60; Combat Improved Expose Armor and Improved Slice and Dice 3 (gate for Venom, the 60th point); Combat Lightning Reflexes at 13 before Efficient Strikes 2 at 22; Subtlety Master of Deception 17-19 before Opportunity 28-32; Combat-Subtlety Hemorrhage (signature) as the 60th point; Arms Deflection 2 vs Improved Heroic Strike; Arms/Prot 4 Unbridled Wrath + Lingering Rage/Booming Voice; Prot Iron Will first | BUILDS, fl orders | open |
| S15 | Gear sets still hold PvP, AQ and Signet Ring items (rogue, priest, paladin pages): the gear redo rebuilds them; check the exclusions after it | gear redo | open: after the redo |
| S16 | Raid pages show no talent list, only the tree link and the split; "How to heal" and guides talk about talents the player cannot see | RM | open |

## druid

| # | Finding | Source | Status |
|---|---|---|---|
| D1 | raid/feral-combat: "Ferocious Bite is not in the list" while list step 2 is Ferocious Bite; "Faerie Fire opens the fight" not in the list | GUIDES | open |
| D2 | raid/feral-combat: "4 points in Furor give back 80%"; build has Furor 2 (40%) | GUIDES | open |
| D3 | raid/feral-combat: quotes 694/688/590 DPS, page shows 758/745/630/619; calls 9/31/11 "without Shifting Power" while the tier table recommends it | GUIDES | open |
| D4 | raid/restoration: "This build has no Wild Growth and no Nature's Swiftness"; build has Nature's Swiftness | GUIDES | open |
| D5 | raid/restoration: "3.2 with this build's 3 points in Naturalist"; build has 5 (3.0 s) | GUIDES | open |
| D6 | Swiftmend: pages say Forever no longer consumes the HoT; the spell text says "the consumed spell"; by-level says "eats your Rejuvenation" | GUIDES, README, LG, heallab | open: check the tooltip |
| D7 | raid/balance: Moonkin aura "does not stack with Leader of the Pack ... party 3%"; README says raid-wide and stacking since 70425 | GUIDES | open |
| D8 | Genesis "5%" (GUIDES, 4 places; BUILDS core); tooltip 10% at 5/5 | GUIDES, BUILDS | open |
| D10 | feral-combat-by-level: "Restoration ... raid build (11/4/36): 28.5 s, a quarter slower"; build 12/1/38, page +21% | LG other | open |
| D11 | Rip "once in ten fights from 52" vs "under one kill in two at 60"; Ravage 350% (page) vs 435%; Rend and Tear "35-39" vs table 55-58 | LG, GUIDES | open |
| D12 | leveling/restoration "Why": every talent level from an old order | GUIDES | open (known class) |
| D13 | leveling/balance: Nature's Focus "70% from 46" (5 points only at 60); Reflection 56-58 vs table | GUIDES | open |
| D14 | macros "Instant Starfire": Nature's Swiftness only makes Nature spells instant (Starfire is Arcane); no Balance build takes it | hand macros | open |
| D15 | keybinds bear bar (10-19) lists spells learned at 16, 28, 36 | LG, hand | open |
| D17 | raid/feral-combat lists four tank builds under "Other builds" with no label; Tanking has no how-to lines | RM | open |

## shaman

| # | Finding | Source | Status |
|---|---|---|---|
| SH3 | raid/elemental: "this build has no Elemental Reach" (takes 1/2); "2 points in Reverberation" (has 0) | GUIDES | open |
| SH4 | raid/elemental-enhancement: "3 points in Reverberation ... 5.4 s"; build 2 (5.6 s) | GUIDES | open |
| SH5 | Stormstrike "costs only 125 mana": 8% of base mana since 70425 | GUIDES | open: verify |
| SH6 | leveling/elemental caveat "Lightning Mastery comes at 59" (build lacks it); "From 28, Elemental Focus" vs table 39 | GUIDES | open |
| SH7 | macros "Lightning Mastery into your first bolt" replaces a key no leveling layout has; "Instant big hit" and Enhancement "Instant heal" need Nature's Swiftness no such build takes | hand macros | open |
| SH8 | Fire Nova "the blast around you": Forever's Fire Nova hits around your active Fire totem | LG keys, hand keybinds | open |
| SH9 | leveling/restoration "45% slower (44 vs 30.5)" vs header 38 vs 25 | GUIDES | open |
| SH10 | leveling/elemental-enhancement "5% faster than Elemental (37)" while the index shows it slower | GUIDES | open |
| SH12 | Elemental raid build: Natural Grace 2 (threat), Elemental Reach 1 free; Mindfulness 2/3 | BUILDS | open |
| SH14 | Gate points never named: Mental Dexterity 3 (Elemental leveling, gate to Shamanistic Focus), Toughness 4 and Improved Lightning Shield (Ele-Enh, gate to Mental Quickness), Anticipation (Enhancement) | RM note | open (the note) |

## paladin

| # | Finding | Source | Status |
|---|---|---|---|
| P1 | raid/holy: "This build takes no Holy Shock ... no group heal"; holy-ml-heal has Holy Shock, Boundless Light, Light's Vigil | GUIDES | open |
| P2 | Holy Power "adds 5%/15% crit" (raid/holy, leveling/holy, README); 70753 tooltip: +50% critical healing bonus of Holy spells | GUIDES, STEPS, hand README | open |
| P3 | raid/holy: "Spiritual Focus (one point) keeps 35%"; build has 5 (70%) | GUIDES | open |
| P4 | leveling/retribution (the user's page) "Why" opens with "Hammer of Wrath to finish"; the rules leave it out | GUIDES | open |
| P5 | leveling/prot-ret "Why" describes another build and "3% slower than Retribution" while the page is the recommended, faster one | GUIDES | open |
| P7 | leveling/protection "Why": old order (Holy Shield 60, Templar's Bulwark 49, no Improved Righteous Fury, Holy Conduit); speed 13% vs 9% vs 16%; Holy 38% vs 7% | GUIDES | open |
| P9 | leveling/holy "Why": "first 21 points into Retribution ... Holy Shock at 51"; table Divine Strength at 10, Holy Shock 30 | GUIDES | open |
| P10 | raid/protection: Seal of the Crusader before the pull vs Why's Seal of Righteousness vs Advanced Seal of Fury; Retribution Aura, no word on Devotion | SR, GUIDES | open |
| P11 | raid/protection: Iron Creed "25% more threat, 10% less damage"; tooltip 30% and 6% | GUIDES | open |
| P12 | raid/shockadin: no seal named; Divine Favor "before your next big heal" on a damage list; Hammer of Wrath last | SR | open |
| P13 | Twist of Light (removed; Unsealed Wrath replaced it) in a build name and README: "Retribution — Seal of Command / Twist of Light" (ret-full-buffs-raid) | BUILDS, hand README | open |
| P14 | Prot-Ret raid and a Retribution alternative both at 697 DPS; Prot-Ret raid has no guide section | RM, records | open: verify |
| P15 | Ret leveling: the Hammer of Justice stun combo is a 1-minute cooldown; nothing says so | STEPS, LG | open |
| P16 | by-level "New ranks to buy" lists only pressed spells; bound defensive spells (Divine Protection 18, Blessing of Protection 24/38, Lay on Hands 30, Divine Shield 50) never listed | level_guides.py | open |
| P17 | macros "Fill it with: R takes Exorcism from 2, ... and 2 goes free" unreadable; keybinds Blessing of Protection "10 seconds" (6/8/10 by rank) | hand | open |
| P18 | Holy/Prot leveling: Holy Conduit 2 (54-55) dead while Improved Seals 4/5 | BUILDS | open |

## rogue

| # | Finding | Source | Status |
|---|---|---|---|
| R1 | raid/combat (swords 21/30/0, Sinister Strike list): Why says Backstab is the only builder, Adrenaline Rush and Cold Blood (build has neither), Puncturing Wounds; finish at 4 vs list's 5 | GUIDES | open |
| R2 | raid/daggers-split: Why says Mutilate is builder and filler, Cold Blood and Blade Flurry cooldowns (build has no Mutilate, no Blade Flurry); "It has no Seal Fate" (takes 3/3); list says Sinister Strike filler | GUIDES | open |
| R3 | raid/subtlety gear holds swords while its guide says keep a dagger for Hemorrhage (145% vs 100%); raid/combat (swords) gear holds daggers | gear tiers | open |
| R5 | raid/subtlety: list "Rupture at 3 or more", Why "from 2 points" | SR/GUIDES | open |
| R6 | leveling/assassination: "Venom is not in the list" though taken at 30 and a signature spell: never says Venom is Mutilate's prerequisite | GUIDES | open |
| R7 | leveling/subtlety: "This build has no Preparation" (taken at 31, Death Mark needs it) | GUIDES | open |
| R8 | leveling/combat: "This build has no Cold Blood" (taken at 55, on C in keybinds and guide) | GUIDES | open |
| R9 | leveling/assassination Why: Mutilate 32 (40), Seal Fate 56-60 (35-37), Cold Blood 27 (25); combat Riposte 20 (21), Remorseless Attacks 41-42 (40-41) | GUIDES | open |
| R12 | raid/README tier table lists Assassination 716/719 linking to a page that says "No build for this spec in this mode yet" | RM tier_table | open |
| R19 | macros: Mutilate/Hemorrhage macros "Replaces: Q, and Attack. Frees: Middle mouse" (no key holds Attack; middle mouse already free); Daggers (split) filed under Mutilate builds | hand macros | open |
| R20 | macros "Cold Blood into Eviscerate" filed for raid Combat, whose build has no Cold Blood; fires on every Eviscerate | hand macros | open |
| R22 | raid/combat lists Combat Daggers and "Combat (optimized, daggers)" with identical talents and DPS | RM dedup | open |
| R25 | combat-by-level 1-5: "Stealth is not worth the walk yet" and "Shift+1 = Stealth" in the same stage | LG | open |

## warrior

| # | Finding | Source | Status |
|---|---|---|---|
| W1 | raid/protection Caveats "The list has no Sunder Armor ... Shield Block has no line": the list has Shield Block #1 and Sunder Armor #6 | GUIDES | open |
| W2 | raid/protection Why: Heroic Strike at 45 rage (list 34+), Bloodrage under 70 (list 90), Revenge first (list puts Shield Block, Shield Wall above), Shield Bash fills gaps (not in list) | GUIDES | open |
| W4 | leveling/arms: "Bloodthrill (20% with all 5 points, levels 30-34)"; 2 ranks, 30-31 | GUIDES | open |
| W5 | leveling/arms: no Spearing Strike in the build, yet step 8, the Why ("level 25") and "When to change it" rely on it | GUIDES, STEPS | open |
| W6 | leveling/arms: eat below 40% (steps) vs 50% (Caveat) vs half (Why) | GUIDES | open |
| W7 | leveling/fury Why and Caveats from an older order (Furious Precision, Dual Wield Specialization, Improved Execute, Gore Drinker, Improved Rend, Improved Overpower levels) | GUIDES | open |
| W8 | leveling/protection: "From 41 the points go to Fury" (43); names Improved Sunder Armor and Improved Shield Wall as fillers (build has neither) | GUIDES | open |
| W9 | Slam: Improved Slam rank 2 now -5 s cooldown, Slam 15 s; pages say 3 s and an 18-second cooldown | GUIDES, hand README | open: verify |
| W15 | macros "Last Stand with a heal": no Protection build takes Last Stand; Shield Wall a 15-minute cooldown (Improved Shield Wall untaken) | hand macros, BUILDS | open |
| W16 | macros: Fury "Intercept, for mobs that run" (needs Berserker Stance; Fury leveling stays in Battle Stance); "Battle Stance's Overpower" for Fury raid (never cast) | hand macros | open |
| W17 | macros potion on C (Heroic Strike from 40 in all three guides); Arms "C takes Hamstring from 3" (already on 3); "Charge, then Rend" macro moves keys without saying it replaces the table | hand macros | open |
| W18 | macros: "Fill it with: Revenge" (already on Mouse 5) | hand macros | open |
| W22 | leveling/protection pick protection-open-leveling 3/16/32 is not the raid tank build (healer and tank specs level in their raid build): the raid-path build is under "Other builds" | RM pick | open: check the decision's scope |
| W24 | Fury raid dead points: Spearing Strike, Gore Drinker 1 (free); candidates Improved Heroic Strike, Reckless Swings | BUILDS | open |
| W27 | raid/fury has no "Before the pull: Berserker Stance" line (Arms and Protection have one) | SR | open |
| W32 | Retaliation bound to key 4 at 20 (15-minute cooldown) with no word on use | LG | open |

## priest

| # | Finding | Source | Status |
|---|---|---|---|
| PR1 | leveling/shadow Why and Caveats describe an older build: "no Improved Mind Blast" (takes 5), Shadow Reach, Spirit Tap, Early Demise, Vampiric Embrace, Meditation, Silence, Blackout levels all wrong | GUIDES | open |
| PR3 | leveling/discipline: Inner Focus "(30)"; table 26 | GUIDES | open |
| PR4 | leveling/smite: Searing Light 53-54; table 56-57 | GUIDES | open |
| PR5 | leveling/holy and holy-by-level: Improved Healing 48-50; table 49-51 | GUIDES, LG | open |
| PR6 | leveling/shadow: eat below 40% (steps) vs two thirds (Why); Discipline says two thirds | STEPS, GUIDES | open: check the rules file |
| PR8 | shadow-by-level and keybinds: "Early Demise lets you cast Shadow Word: Death on any mob below 20%": the tooltip is only +30% crit below 20%; SW:D costs 30% of max health when it does not kill | LG, hand keybinds, STEPS | open |
| PR10 | macros: castsequences "Holy Fire, Shadow Word: Pain, Smite" and "Vampiric Embrace, Shadow Word: Pain" wrap to the first spell; the text says Smite repeats | hand macros | open |
| PR11 | macros Discipline section: Power Infusion macros and "Fill it with: Power Infusion" while no Discipline build takes it; section says "the Discipline leveling page" (a damage build) | hand macros | open |
| PR12 | raid/shadow tells every Shadow priest to use Dark Sacrifice (Undead racial); by-level trainer lists show racial spells (Chastise, Fear Ward, Feedback, Starshards, Hex of Weakness...) with no race note | GUIDES, level_guides.py | open |
| PR14 | README: SW:D "10% of your health back" (30%); Binding Heal called a talent (a trained spell; the talent is Holy Binding) | hand README | open |
| PR15 | One comparison quoted with three numbers on a page (Holy 2.3x/25/2.2x; Disc 1.7x/40 vs 25/1.6x; Smite 52/51/49) | GUIDES | open |
| PR16 | shadow-by-level keeps Smite on Q for levels 4-19 after saying "Stop casting Smite" | LG keys | open |
| PR17 | raid/shadow: Spirit Tap 5 (nothing on a boss) unexplained, likely a gate | RM note | open (the note) |
| PR21 | raid/holy and raid/discipline gear rows with a bare item number (13002, 7721) | gear_links | open |
| PR25 | raid/holy: two alternatives both "21/30/0" with different links and no difference named | BUILDS names | open |

## warlock

| # | Finding | Source | Status |
|---|---|---|---|
| WL1 | raid pages: the setup worth about 10% (Imp, Demonic Sacrifice, Succubus, Soul Link, Spellstone) only in "Why"; "How to play" has no such pre-pull line | SR pre-pull, GUIDES | open |
| WL2 | raid/shadow-bolt-hybrid: "This build has no Amplify Curse"; the build and its list have it | GUIDES | open |
| WL3 | Improved Corruption cast times swapped: Destruction "0.8 s with 3 points" (has 2: 1.2 s), hybrid "1.2 s with 2 points" (has 3) | GUIDES | open: verify on the regenerated builds |
| WL4 | Shadow and Flame "10%" (raid/destruction, leveling/destruction, README); tooltip 20% at 5 ranks; by-level says 20% | GUIDES, hand README | open |
| WL6 | README: "Amplify Curse strengthens Curse of Exhaustion by 50%"; tooltip: Weakness and Bane of Agony 50%, Exhaustion 20% | hand README | open |
| WL7 | leveling/demonology: Improved Imp 3 (17-19) "only help reach the deeper talents" but no gate needs them; Demonic Aegis 2 also; Fel Vitality or Demonic Embrace instead | BUILDS | open |
| WL8 | leveling/affliction: last points Demonic Sacrifice 59 and Improved Sayaad 60 gate nothing; Fel Vitality or Demonic Embrace instead | BUILDS | open |
| WL9 | leveling/destruction: Pyroclasm 33, Bane of Havoc 34 (row-5 gate, any talent counts), Incinerate 40 (switched off: a pure waste) | BUILDS | open |
| WL10 | leveling/destruction: steps vs Why: eat 40% vs 55%; "no Fear" vs "Fear it while half mana"; Shadow Bolt cut-off 35% vs a fifth; "no Incinerate" vs "Incinerate from 40"; signature lists Searing Pain, Soul Fire, Incinerate (none cast) | GUIDES, signature | open |
| WL11 | leveling/destruction caveats: Suppression 45-48 and 57 (45-49), Intensity 29-31 (28-30), Voidwalker talents 49-60 (50-60) | GUIDES | open |
| WL12 | raid/demonology: the "other build" 2/31/18 at 841 beats the pick at 838; tier links differ from the headline | RM pick, tier | open |
| WL13 | raid/README: Destruction 795 (#3) in the main table, last in the tier table (757/783) below the hybrid | RM (S9) | open |
| WL15 | leveling/demonology signature line: "21% from pet (the spec's rule: at least 0%)" | signature rule | open |
| WL16 | leveling/affliction-demonology: Grim Reach as the Shadow Mastery gate while Improved Drains (used) would gate the same | BUILDS | open |
| WL17 | raid/affliction: "With Nightfall, as in the other build below" (this build has Nightfall); Succubus caveats with 0 Demonology points | GUIDES | open |
| WL19 | keybinds: "the fastest warlock spec" (Demonology is second) | hand | open |
| WL20 | macros "Immolate, then Conflagrate" castsequence stalls on Conflagrate's cooldown; "consumes or refreshes" wrong at 5 ranks (100% not consumed) | hand macros | open |
| WL21 | macros "Summon in a hurry" needs Fel Domination; no Demonology page build takes it | hand macros | open |
| WL24 | demonology-by-level: "the Voidwalker's next 6 attacks" from 28; 2 at rank 1, 6 at rank 3 (34) | LG | open |
| WL25 | destruction-by-level: "The warlock's leveling search is still running" banner (stale) | LG | open |
| WL26 | keybinds: Fear "up to 20 seconds" (10/15/20 by rank) | hand | open |
| WL29 | README: dates to 70425/2026-10-16; Malevolence called new and replaced | hand README | open |

## hunter

| # | Finding | Source | Status |
|---|---|---|---|
| H2 | README "To check at launch", leveling "Watch your ranks", raid caveats: Trueshot Aura r5 +50, Hunter's Mark r4 +71, Aspect of the Hawk r6 +55, "keep the lower rank"; 70753 spells: +100, +143, +110/+120 | hand README, GUIDES | open |
| H3 | Beast-Marks described as "Marksmanship's shots (Trueshot Aura, Barrage, Sniper Shot)"; beast-marks-ml-raid 28/21/2 has none | spec_modes.py | open |
| H4 | raid/beast-marks: "Improved Tracking (3 points)", "Frenzy (2 points)"; build 2 and 3 | GUIDES | open |
| H5 | raid/survival list starts "Explosive Trap when at least 60% mana"; the page says it never comes up on one target (shares Immolation Trap's cooldown) | SR | open |
| H6 | macros "Feign, then trap": "Traps need you out of combat"; README and pages say traps work in combat | hand macros | open |
| H7 | raid/marksmanship and raid/survival: Dismiss Pet (Lone Wolf, about 16% of the damage) not in "Before the pull" | SR pre-pull | open |
| H8 | raid/marksmanship: Lone Wolf headline 5/41/5 at 984; tier tables' best 13/33/5 and 11/35/5 are pet builds (Lone Wolf 0); raid README ranks MM first by tier, third in the main table | RM (S9) | open |
| H9 | leveling/beast-survival Why: Expose Prey (not in the build), Hunter's Mark in a free GCD; survival Why: Counterattack 57, Strider Kick 30 (neither taken), Deadly Aspects 49-53 (50-54) | GUIDES, LG | open |
| H10 | Improved Aspect of the Monkey (Beast-Survival 52-53, Marksmanship 49): no use at 60; Endurance Training 3/5 and 2/5 could take the points at no gate cost | BUILDS | open |
| H11 | leveling/survival 40-60: Lethal Attacks, Careful Aim, Efficiency, Rapid Killing, Mortal Shots on a melee build | BUILDS | open |
| H12 | raid/beast-marks "With a pet" label on an alternative while the headline build has a pet | RM labels | open |
| H13 | raid/beast-marks vs raid/beast-mastery: near duplicates 0.9% apart, both recommended | RM | open |
| H14 | raid/marksmanship: Rapid Killing "comes once in a 3-minute fight" (once either way); only a gate to Rapid Recuperation | GUIDES | open |
| H15 | macros fills keys already in use (Mend Pet, Wing Clip, Hunter's Mark on 1, Rapid Fire on C); "replaces the Auto Shot key" (no such key); presses Intimidation (never pressed) | hand macros | open |
| H16 | macros and leveling README point at keybinds.md (the melee layout) for all specs | hand | open (S12) |
| H17 | drink thresholds disagree within and across pages (a third, 15%, 35%, 60%) | STEPS, LG, GUIDES | open |
| H18 | leveling/marksmanship step "Arcane Shot below a third"; Why "No Arcane Shot" | STEPS/GUIDES | open |
| H19 | leveling/beast-mastery Why describes another build (Efficiency 10-19, Trueshot Aura 25, Bestial Wrath 60, "first 15 points in Marksmanship") | GUIDES | open (known class) |
| H21 | leveling/marksmanship Why: Efficiency, Rapid Recuperation, Barrage, pet points, Unleashed Fury levels all off | GUIDES | open |
| H22 | leveling/beast-survival Why: Resourcefulness, Survivalist's Discipline, Ferocity, Bestial Discipline levels off | GUIDES | open |
| H23 | Aimed Shot "+166", Sniper Shot "+295"; 70753 spells +350 and +590 | GUIDES, hand README | open: check forever-spells |
| H24 | README "Hybrids with their own pages: ... Melee (split)": no such page | hand README | open |
| H25 | Raptor Strike macro on Q vs keybinds (Q for the last 20%); keybinds "if it ends your Auto Shot, that is fine" vs macros' Auto Ranged Combat off | hand | open |
| H27 | "its mana buys more as the sting and the trap" ungrammatical; "slowest of the four" (five specs) | STEPS, LG | open |
| H-lint | the `dead` check's Survivalist's Discipline row is wrong: it also cuts trap cooldowns (fixed by the family rule) | page_lint | fixed |

## mage

| # | Finding | Source | Status |
|---|---|---|---|
| M1 | leveling/arcane-frost (the user's page) signature line: Arcane Blast (not in the build), "Arcane Missiles cast in every fight" (about once every two kills) | signature text | open |
| M2 | leveling/arcane-frost: Frostbolt "more than a fifth" (steps) vs "a tenth" (Why); Fire Blast only for the finish (steps, keybinds Mouse 5) vs also when the mob would reach you / is on you with Frost Nova down (Why) | GUIDES, STEPS, hand keybinds | open |
| M3 | README roles table: 70425/70291 header; Frost "a tie in a full raid ... the clear leveling pick" (-37% raid, second in leveling); Arcane "ties ... one of the two slowest"; Fire "ties" (the single pick) | hand README | open (S10) |
| M4 | README headline: Arcane Blast 15%/15 s/+175% (12%/18 s/+100%), Critical Mass 5 ranks +10% (3 ranks, 6%), Arcane Resilience 2 ranks (3), Elemental Precision (not in the data), Ice Lance +200% (300%), 55 talents (53) | hand README | open |
| M5 | leveling/fire Why: "no talent order yet" while the page has one; "about 33 s, the slowest" vs 38 | GUIDES | open |
| M6 | leveling/fire: "No Scorch: never cast" (steps) vs "Scorch when the mob is on you ... and during the walk-in" (Why); signature counts Scorch and Flamestrike | GUIDES, signature | open |
| M7 | Frost Blast is in no current spell data, yet leveling/frost signature line and keybinds ("trained at 24") name it; the same signature line counts Cone of Cold and Blizzard ("never cast") | signature, hand keybinds | open: verify the spell |
| M8 | leveling/arcane: "Not in this build: Arcane Power" then "Arcane Power too while ..."; Frost Nova step vs "No Frost Nova"; eat two thirds vs 40% | STEPS, GUIDES | open (S2) |
| M9 | leveling/frost: "Ice Barrier before each pull once you have it" and Cold Snap step after "Not in this build: Cold Snap, Ice Barrier"; keybinds Shift+1/Shift+2 for a build not on the page | STEPS, hand | open (S2) |
| M10 | leveling/arcane-frost: Improved Channeling 5 as the Arcane Meditation gate; Arcane Impact 3 (+6% Arcane crit) would gate the same and do something | BUILDS | open: lab check |
| M11 | leveling/arcane-frost: Winter's Chill 1 (58) is no gate and does nothing on one mob: Precision 3 or Improved Frostbolt 4 instead (today's lab check: Improved Frostbolt 4 for Improved Frost Nova 1 read -0.55% time, a tie) | BUILDS | open |
| M12 | leveling/arcane: level-10 point in Arcane Resilience (no gate needs it); a fifth Improved Channeling point gates the same | BUILDS order | open |
| M13 | raid Fire/Arcane/Arcane-Frost: Wand Specialization 2, Arcane Resilience 3, Magic Absorption 2 as Arcane gates; Improved Channeling (pushback) is the utility pick the tie-break should make | BUILDS, filler_audit | open |
| M14 | raid/frost (frost-winters-chill-raid): its own text says Winter's Chill and Frostbite do nothing on a boss: 9 dead points on the page's pick | BUILDS, GUIDES | open |
| M15 | macros "Everything at once" (Arcane Power + Presence of Mind + Arcane Blast: the raid page uses PoM for Arcane Wrath); "Fill it with Cold Snap" (no Arcane build has it) | hand macros | open |
| M16 | macros Combustion macro ends with Fireball (pulls open with Pyroblast); "Instant Pyroblast" needs PoM no Fire/Frostfire build takes | hand macros | open |
| M17 | raid lists "Arcane Blast: keep it on the target" reads like a debuff (it means your stacks) | SR | open |
| M18 | leveling/fire: "Combustion at the pull" from 10 (taken at 59), "hard-cast Pyroblast" before 20 | STEPS | open |
| M19 | leveling/frostfire: 34 s vs README 36; "The leveling queue is re-running this rotation's search as this guide is written (2026-11-04)"; Arcane filler and Accelerant 35-39 doing nothing before Frostfire Bolt at 40 | GUIDES, BUILDS | open |
| M20 | keybinds: "the Keybinds by level tables of the Frost guide": each spec has its own | hand keybinds | open (S12) |
| M22 | macros potion text "every mage holds Cone of Cold on C from 26" (Fire's C becomes Blast Wave) | hand macros | open |
| M23 | arcane-by-level / arcane-frost-by-level: "Arcane-Frost and Frost are the recommended mage leveling specs" (only Arcane-Frost is) | LG | open |
| M24 | raid/frostfire: mana gem from Conjure Mana Citrine; the others say Ruby | specs.json consumables | open |
| M26 | leveling/frost: eat two thirds vs 40% on the other tuned pages | STEPS | open: check the rules file |
| M27 | macros Eureka! paragraph: Q for "Arcane its Arcane Missiles from 8" (Arcane-Frost's Missiles are on 1); a 400-word wall; boosted list omits Arcane Blast and Arcane Wrath | hand macros | open |
| M29 | raid/frost: Winter's Chill "since the 2026-11-02 patch" vs README "client 70425" | GUIDES, README | open |

## Status, 2026-11-08 ~22:35

Done (local, not pushed):
- Hand-kept text, all nine classes (one fixer per class, each finding verified against the data first; several reader findings were
  wrong: M10, M26, R7 in part, WL2 on the working builds): leveling guides rewritten and restamped for every spec, raid guides fixed for
  tooltip facts (shaman and warlock raid guides rewritten: their raid lanes are done), by-level stage texts and keys, the steps, macros,
  keybinds pages and the hand-written README sections (no quoted rankings any more). Potion keys settled in every class.
- Generator: S1 (auras and seals are no cooldowns), S2 (a step led by a talent the build lacks is dropped), S3 (imbues are kept up),
  S4 (pack-only lines leave the one-target list), S5 (emergency buttons go to Advanced with when to press them), S6 (off-GCD lines say
  so), S7 (the most-cast always-ready spell is the filler), S9 (tier tables say their gear differs), S13 (signature lines name the
  spec's core set, no "at least 0%"), R12, R22, H3, H7/WL1 (setup line from the entry's class options), PR12 (race-only spells marked
  in trainer lists), O5 (illegal tier links hidden), O1 note ("Points that do nothing for this spec" on every spec page).
- Builds: Restoration druid repaired (Bloom modelled, +3.3% capacity); its leveling order redone.
- page_lint after the regen: talents 0, links 0, guide 0, keys 0, steps 0, macros 0, names 0; build 15 (raid guides of the lanes'
  classes, rewritten after the lanes; rogue leveling rows to check), dead 11 (free points: build changes).

Open:
- Free points (dead 11 and S8, S14): `heallab/filler_pass.py` running on the five healer picks; `fightlab/fl_filler_pass.py` (new) on
  the Retribution leveling pick, then the other leveling pages with free points.
- Raid guides of warrior, rogue (after their lanes) and hunter, mage, paladin, priest, druid (after the gear redo): rewrite and restamp.
- S16 (no talent list on raid pages), M17 ("Arcane Blast: keep it on the target"), H5 (Explosive Trap line that never fires),
  W27 (Fury stance line), W22 (Protection leveling pick vs the raid-path rule), P13 (Twist of Light in a build name), M24 (Citrine gem).
- A second read of every class after the lanes and the regen (the user's standing request).

## Status, 2026-11-09 ~00:25

The first filler passes (dry runs, nothing written) made wrong moves; both tools fixed before any build changed:
- Healer pass (`heallab/filler_pass.py`): the Restoration druid lost 1.9% capacity in seven moves each under the noise floor (Improved
  Regrowth and Heart of the Wild, one rank at a time); Holy Nova and Holy Binding counted as threat reduction ("cause no threat");
  Totemic Focus went to Natural Grace though the lab charges one totem at the pull (a raid shaman recasts the group's totems all fight).
  Now: every-rank removal next to one rank less, zero in a ten-minute fight too (mana talents read 0 in five minutes when the healer does
  not run dry), utility moves bounded by the capacity the pass started from in both fights, measured moves confirmed on fresh seeds,
  "threat generated by your ... spells" only, a module `KEEP` list (shaman: Totemic Focus), talents that teach a spell the lab casts never
  zero points (Riptide, Swiftmend, Nature's Swiftness). Re-running on the five healer picks.
- Leveling pass on Retribution: wanted Vindication in Improved Seals because the fight lab modelled none of Vindication (hotfix 113554
  left only the target's attack power cut). Modelled (`fightlab/paladin.py _vind_reduction`, `tables.VINDICATION_SCALE`, "mob": the
  level-60 share of a mob's swing, 15%, at every level; how the 204 scales below 60 is unknown): the page build 27.36 -> 27.00 s weighted,
  32.30 -> 31.42 s at 60. The paladin's leveling redo runs in `deep-runs/paladin_vind_1109.sh` (rules from scratch, open search fresh,
  builds, orders, races, guide timings, then the filler pass again).
- A lead from the first healer pass: Discipline `discipline-ml-heal` Litany of Light 1 -> 2 measured +3.6% capacity (200 seeds, 8.6
  standard errors); waiting for the fresh-seed check of the fixed pass.
- Other "not modelled" fight-lab talents read (`grep "not modelled" fightlab/*.py`): none with a leveling effect near Vindication's;
  Lingering Rage (warrior, rage kept between fights) and Spell Warding (priest, -2%/rank spell damage taken) are small, noted here.

## Status, 2026-11-09 ~00:50

Done since 00:25 (regenerated; page_lint: build 16, dead 6, every other check 0):
- W22: healer and tank leveling picks are the raid-path build (user rule 2026-09-30), also where a search build levels faster
  (`render_modes.rank_builds`): Protection warrior (28.1 against 27.6 s) and Discipline priest (46 against 39.5 s) switched; the search
  builds stay under "Other builds". Their guides measured again; the Protection warrior's rotation guide and by-level notes rewritten
  for the raid build (talent values at 60 measured: Shield Specialization 3.1 s, Bastion 2.2, Focused Rage 2.1, Improved Revenge 1.6,
  Cruelty 0.9). The Discipline guide waits for the healer pass (its raid build may change).
- `level_guides.py --check` now fails a guide text that places a talent at levels the order does not ("**Talent** (a-b, c)", 10+):
  it found the Discipline guide (the old build's Shadow talents) and three loose ranges (rogue Relentless Strikes, warlock
  Destruction's group of four, warrior Dual Wield Specialization), fixed.
- Build pages: core and flex entries for talents the allocation no longer holds are not shown (`render_builds.py`), and the 57 builds'
  stale core entries were removed from the JSON with a note (Twist of Light, Lava Burst, Adrenaline Rush, Elemental Precision ...).
- P13: the two Retribution builds renamed (no Twist of Light), their summaries list what they take now, open questions name Unsealed
  Wrath; the paladin README intro too.
- M17: Arcane Blast lines read "keep its buff stacked on you" (`simple_rotation.SELF_STACK`), and the two Arcane guides' apology
  sentences went. W27: warrior raid pages name the entry's starting stance (Berserker for Fury, Defensive for Protection).
- H5: the Survival page's Explosive Trap line is right (9 casts a fight in a full raid, Immolation Trap 1); the guide's "never comes up"
  was the dummy's mana and is corrected. M24: the Frostfire raid rotation really uses Mana Citrine (item 8007); page matches (whether
  the gems share a cooldown in Forever is unverified).
- S13: leveling signature lines name the core spells the build never casts at 60 apart ("this build never casts Devouring Plague").
- S16: raid pages have a "## Talents" table (tree, points, talents and ranks); page_lint ignores the talent tables when it reads uses.
- P16: by-level "New ranks to buy" covers every spell on a key or in the emergency line, not only the pressed ones.
- PR11: priest macros' Discipline intro matches the new leveling page.
- Feral Charge on the feral raid page: "Taken for raid utility" (its interrupt) instead of "does nothing" (`page_lint.raid_utility`);
  page_lint's GENERIC knows "instant cast spells" (Mental Agility was a false dead point).
- Guide stamps: druid leveling restamped (only the Balance rules had moved); a reader is checking the hunter and rogue leveling guides
  against their re-tuned lists before a restamp.

## Status, 2026-11-09 ~01:40

Healer filler pass (fixed tool, 200 runs, five-minute and ten-minute fights) results:
- Discipline `discipline-ml-heal`: Twin Disciplines 1 -> Litany of Light 2, +3.6% capacity (fresh seeds +3.2%, ten-minute fight
  +3.4%). Applied (29/22/0).
- Holy `holy-raid-healer`: Power in Light 2 and Mental Agility 1 -> Silent Resolve 3 (threat; -0.1% capacity, -0.3% in the ten-minute
  fight, inside the start bound). Applied.
- Restoration druid: the pass would move Heart of the Wild 2 -> Nature's Focus 5/5 (pushback) at -0.5% capacity (inside the bound,
  but a loss on every step). Not applied: Heart of the Wild is Intellect, worth more over a raid night than in the lab's fights.
- Restoration shaman: no zero points (Totemic Focus kept by `KEEP`, Riptide as a cast spell).
- Holy paladin: twelve talents read zero (Holy Power, Infusion of Light, Benediction, Boundless Light ...), no move gains and no
  utility destination: the paladin healer model leaves crit size and these talents nearly worthless (heals downranked to the
  deficit overheal on a crit). Open: a lab gap to examine; Consecrated Ground, Improved Judgement and Sanctified Judgement stay free.
- Found on the way: the druid's heal-lab report predated Bloom (2026-11-02): the Restoration pages showed pre-Bloom capacities.
  Re-racing the druid and priest healer reports; then the priest raid-path orders and guide timings, and the Discipline guides.

## Status, 2026-11-09 ~02:00

- Healer reports re-raced (60 runs, the pages' numbers): priest `holy-heal.json` (Holy 0.691, Discipline 0.647 with Litany of Light 2)
  and druid `resto-heal.json` (Restoration 0.686; the report had predated Bloom). Priest raid-path orders redone (Discipline: stats
  model's order 46.2 s; Holy: own tree last 57.0 s), guides measured; the Discipline leveling and raid guides and the Holy guides
  rewritten for the new builds and restamped (Silent Resolve's threat named: the lab models none).
- page_lint: build 6 (mage raid 2 and rogue raid 3 wait for their lanes; paladin Prot-Ret leveling is mid-lane: the Vindication lane's
  fresh ret-dps rules made the page fall back to an optimizer export until its open search and races finish), dead 6, the rest 0.
- Open: Holy paladin healer model (twelve talents at zero), the Affliction leveling free point (Improved Sayaad: a leveling filler
  pass), the rogue raid free points (after the rogue lane), and the raid guides of the lanes' classes.

## Status, 2026-11-09 ~02:20 (warrior lane done 02:07)

- Warrior: the ML final steps confirm arms-battle-raid (+0.22%) and fury-dual-wield-open-raid (+0.00%): no new builds; raid rotations
  re-tuned on 11-08. A reader rewrote the three raid guides (Arms: Bloodrage under 45 rage, Rend about 8; Fury: the page's pick is the
  two-hander fury-open-raid, the guide had been written for dual-wield; Protection: Shield Block is the top line now, 35 a fight, and
  Sunder Armor 45 a fight, the guide said neither was cast); restamped. `page_lint.py warrior`: 0 findings; `--live`: talentsforever
  code 12 (ours 12), the simulator 103 commits past our pin, Blizzard's UI mirror at client 70862 (move after the wrap).
- `simple_rotation`: "time until X is ready > N s" now reads "when **X** is more than N seconds from ready" (the Fury list had
  Whirlwind above Bloodthirst with no condition).
- Research rotation pages (`<class>/research/raid|leveling/rotation.md`) regenerated for every class: the warrior's dated from 11-07.
- Affliction leveling filler pass (dry run, 02:24): zero points Demonic Embrace, Demonic Energies, Demonic Sacrifice, Fel Concentration,
  Improved Drains, Improved Sayaad; the only moves found were tie-breaks of 0.06-0.08% (Improved Drains -> Malevolence, Demonic Energies
  -> Fel Concentration) and nothing for Improved Sayaad (best: under the bar). Not applied: noise-level, and the page already says the
  point opens nothing.

## Status, 2026-11-09 ~04:25

- Holy paladin healer model examined (the "twelve talents at zero" lead). Holy Power works as coded: all five ranks are worth 3.3% of
  capacity, one rank about 0.3%. A crit on a heal downranked to the deficit mostly overheals (27% on critical Holy Light), and the
  paladin runs short of mana, so crit size buys little. No lab bug. Conviction read "not simulated" on the report while the lab applies
  it (+7.3%): added to `heallab/paladin.py` SIMULATED. The scorer's heal model still has Oath of Light and Conviction at 0 (open: the
  paladin heal calibration).
- `holy-ml-heal`: Consecrated Ground -> Holy Power 5/5, Improved Judgement and Sanctified Judgement -> Unyielding Faith 2/2 and Pursuit
  of Justice 2/2, then Holy Conduit (it opened nothing once Consecrated Ground left) -> Purifying Power 1. Healer lab, 200 runs:
  0.6237 -> 0.6242 (five minutes), 0.4823 -> 0.4851 (ten minutes); Infusion of Light 2/2 and Boundless Light 2/2 measured lower.
  Report re-raced with the page build first (0.636; deltas of the page build).
- The Holy raid guide had said "This build takes no **Holy Shock**" and "takes neither **Holy Shock** nor **Light's Vigil**" for a
  build that takes both (the 11-01 deep winner; the guide was of 10-22). Rewritten: Light's Vigil + Holy Shock as the group heal (14%
  of healing), Oath of Light's value, Holy Power at 225%, the utility points.
- page_lint: new reverse build check, a guide that says the build lacks a talent it takes. It found the paladin page, the rogue
  daggers-split page ("It has no **Seal Fate**"; after the rogue lane) and a false positive ("Before 25 you have no **Stormstrike**",
  conditions now excluded).
- popular_builds.CODE_VERSION 7 -> 12: all 45 codes of today's list decode with the site's points (7 under 51 points). The refresh of
  popular-builds.json waits for the rogue search, which reads it.
- `fightlab/fl_filler_pass.py`: a "no loss" fallback (a zero point moves into a live talent when the move costs at most 0.1% on each
  seed). Re-running Affliction with `--write` for Improved Sayaad.
- Open: the Holy paladin leveling guide (raid_path build changed: the Vindication lane's raid_path step re-orders it), the paladin heal
  calibration, rogue subtlety-hemo-raid 25% below the simulator's Subtlety Hemo preset (474 against 356 on the dummy; the rogue open
  search is on it).

## Status, 2026-11-09 ~04:53

- Holy paladin `holy-ml-heal`, one more idle point: Holy held 31 points before Light's Vigil (30 needed), so the fifth Divine Strength
  rank opened nothing: Divine Strength 4, Purifying Power 2 (bit-identical in the lab). Report re-raced (0.636), guide updated; the raid
  page has no idle points now.
- Affliction leveling (`affliction-open-leveling`), filler pass with the new "no loss" fallback, written: Improved Drains -> Malevolence
  5/5 and Demonic Energies -> Fel Concentration 3/3 (tie-breaks), Demonic Sacrifice -> Grim Reach, Demonic Embrace -> Demonic Aegis,
  Improved Sayaad -> Improved Shadow Bolt (no loss; Shadow Bolt is the filler). Level-weighted 36.43 -> 36.36 s on seed 3. Guides
  updated, by-level guide measured. The page's times still come from the open search's race (the old allocation, within 0.2%).
- `open_builds.py` re-applies a written filler pass when the pass's `start_order` is still the search record's order (it rewrites every
  `-open-leveling` build from its record and would have undone the moves); `fl_filler_pass.py` records `start_order` and `written`.
- Beast-Marks hunter raid guide: Frenzy 2 -> 3 points and Improved Tracking 3 -> 2 points (page_lint's new rank check). guides.py's
  vetoed-steps check skips a step that tells the player not to cast the spell (the BM steps' "skipping **Arcane Shot**").
- Stale comments fixed: fightlab/warrior.py eat thresholds (65%, Arms 40% by the 11-03 rules), fightlab/druid.py Genesis (+2%/rank).
- page_lint: build 7 (mage 2 wait for the gear redo, rogue 4 for the rogue lane, paladin Prot-Ret for the Vindication lane), dead 1
  (rogue Subtlety's Dirty Tricks, rogue lane), the rest 0.
