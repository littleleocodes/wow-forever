# Fight lab — Monte Carlo fight simulator for leveling and solo play

The scorer (`../scorer/`) is an expected-value model: crit, hit and procs enter as averages. The fight lab plays
fights out in time with dice: a same-level mob walks in, swings, gets rooted and slowed; the player casts, gets pushed
back, follows a priority list, kills or dies; then loots, walks, eats, drinks. Thousands of fights give the
distribution of time to kill, the downtime and death rate they imply, the damage shares the rotation actually
produces, and the value of each talent measured as the change in time per kill when it is removed. It exists to
check and calibrate the scorer's leveling profiles (cast quantization, overkill, proc uptimes, resource dynamics,
variance-driven deaths), not to replace it for level-60 raids, where the ElliotWood/Forever simulator already runs
(`../raidsim/` drives that simulator for our raid builds).

```
python _reference/data/fightlab/run.py mage --spec frost-leveling --build opt-frost-leveling-leveling-st \
    --compare leveling-frost --levels 20,30,40,50,60 --fights 2000 --deltas 30,60 --write
python _reference/data/fightlab/run.py mage --spec frost-leveling --build leveling-frost --levels 30 --fights 5 --log   # print a fight
python _reference/data/rebuild.py --jobs 4                # every class: calibrate <-> optimize, race, report, sensitivity, regenerate pages
python _reference/data/fightlab/summary.py --write        # the cross-class page _reference/fightlab-summary.md
```

Outputs: `<class>/leveling/fightlab/<spec>.md` (+ `.json`), the "Fight lab" section of each class's `leveling/README.md`
(`render_fightlab_sections.py`), `_reference/fightlab-summary.md` and `last-rebuild.json` (what the last `rebuild.py` run found).

## Files

| File | What it is |
|---|---|
| `engine.py` | Class-agnostic combat loop (0.1 s steps), mob model, session loop with loot/travel/eat/drink/death, statistics, paired talent deltas |
| `tables.py` | Every level table and formula the sim assumes (Classic hit/crit/armor formulas, base stats, the gear tiers `GEAR_TIERS` (item-database greens, dungeon blues), wand dps, regen, conjured water/food, downtime, caster-mob constants) plus the mob tables read from `mob_stats.json` |
| `warlock.py` | Warlock: Affliction leveling (`affliction-leveling`) with a Voidwalker that Torments and holds the mob by threat, Corruption / Bane of Agony / Siphon Life / Immolate, Wrack, Shadow Bolt, Drain Life, Life Tap, Fear, Death Coil, Healthstone, Consume Shadows and Health Funnel between fights; Soul Link splits damage to the pet |
| `hunter.py` | Hunter: Beast Mastery leveling (`bm-leveling`) with a cat that Growls, Claws and Bites on focus; Auto Shot from 35 yd (dead zone inside 8 yd), Hunter's Mark, Serpent Sting, Summon Hawk / Arcane Shot, Multi-Shot / Aimed Shot, Bestial Wrath, Intimidation, Rapid Fire, Mend Pet, Feign Death, Wing Clip and Raptor Strike when meleed |
| `warrior.py` | Warrior: two-handed Arms leveling (`arms-2h-raid`): Charge, Bloodrage, Battle Shout, Victory Rush, Mortal Strike, Overpower after dodges / Bloodthrill, Rend, Execute with all the rage, Heroic Strike on the next swing; rage from Classic's formula, Deep Wounds bleeds, Enrage, Flurry; bandages and food between fights |
| `rogue.py` | Rogue: Combat swords leveling (`combat-swords-raid`): Cheap Shot / Garrote opener from stealth, Slice and Dice, Sinister Strike to 5 points, Eviscerate or Kidney Shot, Riposte after a parry, Blade Flurry, Adrenaline Rush, Evasion, Instant / Deadly Poison, Hack and Slash extra attacks; bandages and food between fights |
| `paladin.py` | Paladin: two-handed Retribution leveling (`ret-dps`): Seal of Command / Righteousness, Judgement (doubled on a stunned mob), Holy Strike, Consecration, Hammer of Justice, Hammer of Wrath, Divine Protection, Holy Light / Flash of Light between fights, Lay on Hands |
| `shaman.py` | Shaman: Enhancement leveling (`enhancement-dps`) and Elemental (`elemental-dps`: Lightning Bolts from range, Flame Shock, Earth Shock, Lava Burst, bolts in melee with pushback): Rockbiter / Windfury imbue, Lightning Shield / Water Shield, Searing Totem, Lightning Bolt pull, Stormstrike, Earth Shock, Flame Shock, Maelstrom instant bolts, Stoneclaw Totem, heals, Reincarnation |
| `druid.py` | Druid: Balance (`balance-dps`: Moonfire, Insect Swarm, Wrath, Starfire on Eclipse charges or a rooted mob, Nature's Grace, Moonkin armor from 40) and Feral cat leveling from 20 (`feral-cat-dps`): Ravage / Pounce / Shred opener from prowl, Tiger's Fury, Rake, Claw, Rip / Ferocious Bite, Berserk, shifting out to Regrowth and back into Cat Form at 55% of base mana, Rejuvenation / Regrowth between fights; levels 10-19 (Bear Form) are not simulated |
| `priest.py` | Priest: Shadow leveling (`shadow-dps`): Power Word: Shield / Inner Fire before the pull, Mind Blast, Shadow Word: Pain, Mind Flay channels, Vampiric Embrace, Devouring Plague, Shadow Word: Death, Psychic Scream, Renew between fights; periodic damage that can crit, channels shortened by pushback |
| `hunter.py` (melee) | The hunter module also plays the melee hunter (spec model `melee-dps`: dual-wield under Aspect of the Beast, Raptor Strike, Mongoose Bite on dodges and Expose Prey procs, Strider Kick, Counterattack after a parry via the engine's `on_parry` hook, the Lacerating Strikes bleed, Lone Wolf without a pet); `SHARE_SOURCE_BY_SPEC` maps its damage onto the melee model's sources |
| `mage.py` | Mage (with an AoE grinding priority list for pulls of several mobs: Frost Nova, walk out, Blizzard, Cone of Cold, Arcane Explosion): spell ranks parsed from `_reference/data/forever-spells/mage.json`, talent numbers from the beta tooltips in `forever-talents/mage.json`, talent mechanics (`MECHANICS` lists what is simulated), the `frost-leveling` priority list |
| `run.py` | CLI: builds and their leveling orders from `proposed-builds.json`, per-level runs, build comparison, talent removal values with common random numbers, the expected-value scorer's value of the same removal (same scale), the report |
| `calibrate.py` | Fits the scorer's leveling inputs to the sim: measured damage shares and time split into the spec model, a fight-length coupling, and per-talent effect values for the leveling profiles (`specs`-scoped so other models are untouched) |
| `sensitivity.py` | Re-runs builds with each unverified constant moved (mob health / damage, root breaks, pushback, gear tier, caster share) → `sensitivity.md` per class |
| `mob_stats.py` / `mob_stats.json` | Mob health, melee damage, armor, swing time and caster share by level from the Classic 1.12 creature database (cmangos classic-db z2815; raw CSV under `_reference/data/raw/2026-09-26-cmangos-classic-db-z2815/`) |
| `gear_stats.py` / `gear_stats.json` | Gear by level from the Classic 1.12 item database: per class and tier (greens = fixed-stat green items, mostly quest rewards; blues) the typical good pick per slot 2-7 levels below the character, summed, spell power and healing from the items' on-equip spells (`spell_template` auras 13 / 135), weapon and wand dps by kind |
| `summary.py` | The cross-class page `_reference/fightlab-summary.md` from every class's report JSON |
| `../rebuild.py`, `../render_fightlab_sections.py` | The one-command pipeline (calibrate ↔ optimize to convergence, race, report, sensitivity, regenerate pages; `last-rebuild.json`) and the generator of each class README's "Fight lab" section and hand-draft note |

## Tuned rotations (2026-09-27)

`rotation_opt.py <class> [--spec <model>] --write` (or `--all`) searches rules on top of a module's hand-written priority: spell
vetoes (`BaseModule.veto`, checked in `Fight.can_afford`: never cast a spell, only above a mana share, only while the mob has more /
less than a health share: outside them the priority list falls through to its next choice), the drink / eat thresholds and the
module's `ROTATION_KNOBS`. Common random numbers on the pipeline's build and levels, confirmation on a second seed, score = the
races' level-weighted time per kill. `rotations/<class>-<spec>.json` holds the rules and the search record; `run.make_module`
applies them to every run of that spec model (calibration, races, reports, sensitivity); `WOW_FL_ROTATION=default` switches them
off, and `regression.py` runs that way so the engine check stays about the engine.

## How a class module plugs in

A module subclasses `engine.BaseModule` (every hook has a no-effect default) and gives the engine `make_player(level)`,
`pull_range()`, the spell list by level (`Spell` objects parsed from `forever-spells/`; kinds "spell", "channel", "heal",
"melee", "ranged", "buff", with periodic damage, heals, absorbs, weapon percentages, resource and control fields), the
class flags `melee` / `ranged` / `resource`, and hooks: `cast_time`, `mana_cost`, `final_cost` (Clearcasting),
`hit_bonus`, `crit_bonus`, `crit_damage_bonus`, `damage_multiplier`, `periodic_multiplier`, `heal_multiplier`,
`periodic_can_crit`, `resist_factor`, `chill_duration_bonus`, `chill_extra_slow`, `on_chill` (Frostbite, Fingers of
Frost), `consume_frozen_charge`, `on_hit`, `on_tick` (DoT and channel ticks), `on_swing` (weapon outcomes), `on_miss`,
`after_cast` (cooldowns, step-backs), `pushback_resisted`, `on_hit_taken`, `on_fight_start`, `on_kill`, `on_pet_death`,
`pet_decide` (pet abilities), `pet_threat_bonus`, `mana_regen`, `health_regen`, `swing_speed_factor`, `rage_from_hit`,
`evocation`, `after_fight` (out-of-combat heals, pet care, Life Tap: returns seconds spent) and `decide(fight)` — the
priority list, which returns a `Spell`, `"wand"`, `"retreat"`, `"advance"` (run at the mob), `"shoot"` or `None`.
Module-level constants feed the other scripts: `SHARE_SOURCE` / `NEW_SOURCES` (sim damage keys → scorer sources), `FIT`
(what `calibrate.py` fits and with which template), `KEY_TALENTS` (sensitivity rows), `DESCRIPTION` and `NOT_MODELLED`
(report text) and `PIPELINE` (the scorer model, hand draft, optimizer build, levels, calibration levels and lookahead that
`rebuild.py` uses for the class; `extra_reports` runs other spec models through the same module and a compared
`opt-<spec>-<profile>` build plays under its own model, which also yields the model's `abs_dps_factor`). The engine rolls: spell hit/crit/partial resists, the Forever attack table for weapon swings
(miss, dodge, parry, glancing, crit, dual-wield penalty), rage and energy, combo points, DoT ticks that can crit, channels
shortened by pushback, mob roots/slows/stuns/fears, a pet that holds the mob until the player's threat passes 130% of its own,
pushback on casts, and caster mobs: a share of pulls (the creature database's mage-class share by level, `MOB_CASTER_SHARE`
to override) stands at range and casts a bolt every 3.5 s for 1.6x its melee swing (spell damage, no armor) until an
interrupt, silence or stun lands (`Spell.interrupt` = lockout seconds parsed from the tooltip: Counterspell 10, Kick 5,
Earth Shock 2, Silence 5, Feral Charge 4; the `interrupt_bonus` hook adds Improved Counterspell / Improved Kick), then runs
in and melees until the lockout ends. Mob damage can be reduced flat (`Mob.dmg_reduction`: Demoralizing Roar) and the
druid module switches between Bear Form (10-19, rage: Enrage, Demoralizing Roar, Maul, Bash) and Cat Form (20+, energy).

## Reading the report

- **Time per kill** = fight + loot + travel + eating/drinking + deaths × 90 s. Kills per hour follows from it.
- **Talent values**: positive = removing the talent makes kills slower. "Sim fight time" is the paired difference of
  fight times alone with its standard error (same mobs, same seeds); the time-per-kill column also carries the
  downtime and death effects, which is what the scorer's leveling profiles score.
- **Measured shares** are the rotation's actual damage split; compare with the spec model's `sources` and adjust the
  model when they disagree.
- **Not simulated** lists talents in the build with no mechanic in the module (utility, PvP, or not yet coded).

## Calibrating the scorer

```
python _reference/data/fightlab/calibrate.py mage --spec frost-leveling --profile leveling-st --builds opt-frost-leveling-leveling-st leveling-frost mage/leveling/fightlab/candidates/cand-frost-28-0-23.json [more candidates] --levels 30,60 --fights 2000 --write
```

1. Simulates each build at each level, whole and minus every talent; a talent's sim value is the relative rise in
   time per kill when it is removed (mean over the levels).
2. Rewrites the spec model: damage shares from the rotation the sim actually ran (Ice Lance became a source), the
   fight / downtime / death time split of talent-affected time, and `fight_coupling` — the exponent by which downtime
   and death time move with fight length (measured from the removal experiments; ~1 for a kiting caster: shorter
   fights mean fewer casts and fewer hits taken). Without it a damage talent can only shorten the fight term, and
   the scorer cannot reproduce several 15-25% talents at once.
3. Scales each listed talent's leveling-mode effects (or a template for the talent's real mechanic, e.g. Shatter as
   Frost damage inside the Frozen loop) until the scorer's value of the same removal, on the same relative-to-the-build
   scale ((score_with − score_without) / (1 − score_with)), matches the sim. Fitted effects carry `specs:
   ["frost-leveling"]` so the Fire model keeps its own numbers; effects for raid / AoE modes are not touched.
4. Writes notes into the manual file naming the fit, and `<class>/leveling/fightlab/<spec>-calibration.json`.

Values are in-build marginals, so **fit against several builds at once**: the hand draft, the optimizer's current build
and its earlier candidates (a build id ending in `.json` is read from that file; keep them under
`<class>/leveling/fightlab/candidates/`). Fitted to one build at a time, the mage optimizer swung between an
Arcane-heavy 28/0/23 and a deep-Frost 0/5/46 from round to round; the joint fit over five builds converged in one
round (12/3/36). After a run, race the new build against the candidates with `run.py --compare <files>`: the sim, not
the scorer, decides which build is recommended. The optimizer's leveling order needs a horizon long enough to see
multi-tier paths (`run.py --lookahead 12` for mage: Ice Lance sits 11 points deep).

## Where the numbers come from (2026-09-26)

| Input | Source | Status |
|---|---|---|
| Spell ranks, costs, cast times, cooldowns, coefficients | beta client 1.60.1.70009 (`forever-spells/`) | data |
| Talent numbers | beta client tooltips (`forever-talents/`) | data |
| Conjured water and food per rank | Wowhead Forever item tooltips (raw pull archived) | data |
| Mage base stats at 60 (Int 125, Spirit 120, Stamina 45, health 1,370, mana 1,213), base spell crit 0.91%, 0.0168% crit per Intellect | Forever client PlayerExpectedStat / base stats, via the ElliotWood/Forever simulator | data (level 1-59 interpolated) |
| Spell miss by level difference (4/5/6/17%), white miss 4%, pushback 0.5 s per hit capped at the cast time, armor constant 400 + 85 × level | wowsims Forever combat rules | rules the community simulators use |
| Base stats of every class at 60 (Strength, Agility, Stamina, Intellect, Spirit, health, mana, base crit, crit per Agility / Intellect, attack power per Strength / Agility) | Forever client via the ElliotWood/Forever simulator (`base_stats.go`, `base_stats_auto_gen.go`, class files); levels 1-59 interpolated | data |
| Player attacks vs a same-level mob: 5% miss (+19% dual-wield), 5% dodge, 5% parry from the front, 10% glancing at 95% damage, ranged 5% miss; rage from Classic's formula (the simulator's flat per-hit rule is untested at high levels) | ElliotWood/Forever `target.go` attack table; Classic rage formula | rules / formula |
| Pets: hunter pets and warlock demons inherit nothing from the owner (Classic-era); level-60 pet stats and abilities | ElliotWood/Forever `hunter/pet.go`, `warlock/pets.go` | data |
| Mob health, melee damage, armor, swing time and the caster share by level | Classic 1.12 creature database (cmangos classic-db z2815: 2,262 normal outdoor templates weighted by 43,198 spawns; `mob_stats.py`) — the beta client has no creature stats and the Wowhead Forever tooltips list level and type only | Classic data, Forever assumption: `MOB_HP_MULT`, `MOB_DMG_MULT`, `MOB_CASTER_SHARE` in `sensitivity.md` |
| Gear stats, armor, spell power / healing and weapon dps by level (greens and blues) | Classic 1.12 item database (cmangos classic-db z2815 `item_template`: 2,360 fixed-stat green and 2,128 blue armor pieces and weapons; `gear_stats.py`) with a pick model (typical good pick per slot, items 2-7 levels below the character) | Classic data, Forever assumption: `GEAR_TIER`, `GEAR_STAT_MULT`, `WEAPON_DPS_MULT` in `sensitivity.md` |
| Root-break chance per hit (20%), partial resists (2.5%), travel/loot times, eat/drink thresholds | assumptions in `tables.py` | assumption, see `sensitivity.md` |

`sensitivity.py` re-runs the builds with each unverified constant moved (root break 10/40%, mob health ±20%, mob damage +30%,
pushback 1 s, blue weapons, dungeon blues, gear stats +20%, no caster mobs, 30% caster mobs, 20% runners) and writes `<class>/leveling/fightlab/sensitivity.md`;
`run.py --set KEY=VALUE` does the same by hand and `run.py --gear blues` runs a whole report in the second gear tier.

## Limits

Pulls of `MOBS_PER_PULL` mobs (default 1; the mage's AoE grinding variant runs 4, the other classes' variants 3, the rogue's 2): adds
arrive with the target, stay on the player and are hit by area spells, channels and cleaving attacks (`tables.AOE_SPELLS`: reach,
target cap, chain falloff; Whirlwind / Cleave / Swipe roll the attack table per extra mob, Blade Flurry adds one target to every
melee attack), dots can be spread over the pull (`engine.BaseModule.decide_aoe`, configured by each module's `AOE` dict; the mage
keeps its own AoE priority), no pet on the adds and no runner adds fleeing separately; runners only as a
sensitivity row (`RUNNER_SHARE`: a share of mobs flee at 20% health for 5 s; default 0), one gear tier per report level (item-database
greens; `--gear blues` / `--gear-tiers` for dungeon blues; world-drop greens with random suffixes are not in the pool), no Ice Block / Mana Shield / Arcane Missiles (Missile Barrage measures 0
here and keeps its hand-entered value), no stance dancing, traps, totem buffs left behind between mobs, soul shards, or
levels 1-9. Caster mobs are a single generic caster (one bolt spell, one lockout); Classic-era combat formulas are assumed
(see `tables.py`) and the mob tables are Classic 1.12 data, not Forever measurements. Beta measurements at the same level
(kills per hour, mob health, drink time) should replace the tables, then the sim can be trusted for build-vs-build
differences before absolute numbers.