# Talent scorer / optimizer

A stats model that turns talent tooltips into numbers, scores every talent for a given spec and use-case, finds
the best legal 51-point build, orders the points level by level, plans respecs, and reports what got buffed or
nerfed between Classic and Forever. It replaces "intuition" with inputs you can read and change: every number is
in a data file, every hand-entered estimate carries its arithmetic.

```
python _reference/data/scorer/effects.py [class ...]                     # (re)parse tooltips -> effects/<game>/<class>.parsed.json
python _reference/data/scorer/run.py hunter --spec bm-leveling --profile leveling-st --compare leveling-beast-mastery --write --export
python _reference/data/scorer/run.py mage --game classic-era --spec frost-raid --profile raid-dps-extwc --compare frost-arcane-power-raid
python _reference/data/scorer/run.py priest --spec holy-heal --profile raid-heal --write --export
python _reference/data/scorer/respec.py mage --write                     # when to respec while leveling
python _reference/data/scorer/compare_effects.py                          # buff/nerf report per class -> changes/
```

`--write` saves a report to `<class>/<leveling|raid|pvp>/optimizer/<spec>-<profile>.md` (the profile's scenario) (or `classic-baseline/optimizer/`
for `--game classic-era`). `--export` (Forever only) inserts the optimized build as `opt-<spec>-<profile>` into the
class's `proposed-builds.json`, where `validate_builds.py` and `render_builds.py` treat it like any other build.
Classic `builds.json` files are never written by the optimizer: they are the calibration reference.

## How a talent becomes a number

1. **Effects** (`effects/<game>/<class>.parsed.json`, generated): regexes read each rank's tooltip and emit
   `(channel, scope, value)` — e.g. Unleashed Fury → `dmg` on `pet` = 0.03/0.06/0.09/0.12/0.15. Ranks stack exactly
   as the tooltips say; nothing is assumed linear unless the text is.
2. **Manual effects** (`effects/<game>/<class>.manual.json`, hand-written): procs, actives and conditionals the
   parser cannot read, and parser results that need a narrower scope (Elemental Fury and Vengeance buff damage
   crits, not healing crits). Each entry states the derivation, e.g. Deadly Aspects: 2%/rank per auto shot × ~4.3
   shots per 12s window → uptime 8/16/23/30/36% × 30% haste → haste EV 2.5%…10.8% on Auto Shot only. Manual entries
   override parsed ones. `modes` restricts an effect to leveling / raid / heal / tank scoring; `requires` makes an
   effect count only when a partner talent is taken (Fingers of Frost needs Shatter; Shadow and Flame needs
   Conflagrate) and the search bundles the pair; `requires_not` drops an effect when a conflicting talent is
   taken (Master Demonologist under Demonic Sacrifice); `disable` / `enable` switch whole sources off and on
   (Demonic Sacrifice removes the pet, Demonic Pact brings it back); `specs` restricts an effect to named spec models
   (the fight-lab calibration writes leveling values for one model without touching the others).
3. **Spec model** (`specs/<class>.json`): where the damage, healing or threat comes from — sources with shares and
   tags (`type:ranged`, `school:frost`, `ability:Frostbolt`, `pet`, `dot`, `hot`, `heal`, `tank`, `threat`,
   `weapon:2h`, `cat`, `mainschool` …), cast times/cooldowns/resource costs, base crit per gear tier, stat
   conversions (agility→dps, intellect→sustain …), mana shares (how much of the mana budget each ability tag
   is), `game_overrides` for abilities that exist in one game only (Holy Strike, Lava Burst), `enabled_by` for
   abilities a talent creates (Ignite, Pyroblast, Bloodthirst, Mortal Strike, Deep Wounds, Stormstrike, Insect Swarm,
   Mind Flay, Holy Shock, Ice Lance, Siphon Life, Riposte, Summon Hawk; Aimed Shot and Consecration in Classic only):
   such a source is off until the talent is allocated, `enabled_ranks` grows its share with the rank, `displaces` names
   the sources that absorb its share while it is off, `scales_with_crit` sizes a burn by the crit chance; the talent's
   own effect is then the net gain over the displaced casts, fitted by the simulators (since 2026-09-26), and the
   fight/downtime/death time split. Shares come from Classic parse experience and are stated so they can be argued with.
4. **Profile** (`profiles.json`): the use-case.
   - `leveling-st`, `leveling-aoe`, `solo-60` (mode *leveling*) score **% of time per kill saved** = fight time ÷ dps
     gain + downtime ÷ sustain gain + death time ÷ survivability gain, plus small utility credits. A spec model may set
     `fight_coupling` per profile: downtime and death time then also shrink with the dps gain to that power (a shorter
     fight means fewer casts and fewer hits taken; the fight lab measured ~1 for the Frost mage), and its own `time`
     split per profile.
   - `raid-dps`, `raid-dps-extwc` (mode *raid*) score **% DPS gain** (+20% weight on mana sustain; per spec model `mana_weight`).
     In Forever these are the training-dummy profiles, and a spec model that runs short of mana there carries a **mana limit**
     (`mana_limit` {game: {profiles, loss, cap}}, written by `raidsim/calibrate.py`, 2026-09-27): the mana-bound damage (every
     source but white attacks and pets) shrinks by min(cap, max(0, loss − (sustain − 1))), and the linear mana term is off there.
     A mana talent is then worth the damage it saves only while the build runs short: nothing once the mana lasts, nothing more
     than the cap (a Frost mage's one Evocation per fight costs about 7% and no more). The sustain unit is the share of the
     mana-bound damage a talent saves (fitted to its removal runs); loss and cap are fitted to what every calibration build gains
     with every mana-only buff on and to the removal runs of the pure mana talents (the same build with less mana).
   - `raid-heal` (mode *heal*) scores **0.6 × healing-throughput gain + 0.5 × mana gain** on `heal` sources — mana
     weighs almost as much as throughput because raid healers are mana-limited.
   - `raid-tank` (mode *tank*) scores **0.5 × threat gain + 0.5 × effective-health gain + 0.1 × sustain** on
     `threat` sources.
5. **Model** (`model.py`): per source, output = share × Π(1+dmg or heal) × (1−miss+hit) × (1 + crit × crit-bonus) ×
   (1+haste) × cast-time factor × cooldown factor × resource-cost factor; `threat_up` multiplies threat sources.
   So crit is worth more where crit bonuses exist, hit is worth exactly the miss it removes, and a cast-time cut is
   worth what it does to that ability's share.

## New spec models

A model added later than the fits (the hunter's `melee-dps`, 2026-09-27: Forever's Survival melee talents with dual wield, Lone Wolf
or the pet) would otherwise see every fitted talent at zero, because fitted effects are tagged with the models that existed at fit
time. `effects_for` falls back to a talent's parsed tooltip effects when none of its effects applies to the model at hand, so a new
model starts from the tooltips and its own fits come later. The melee model's shares are tooltip assumptions until the fight lab's
melee rotation (hunter module, `decide_melee`) calibrates them; `hunter/leveling/fightlab/melee-dps.md` races the leveling
build against the Beast Mastery and Marksmanship builds.

## Scenario and playstyle weights (2026-09-27)

A control, mobility or avoidance talent is worth something only where it is used: a root that lets a frost mage kite is worth
nothing to a warrior, parry is worth nothing to a melee DPS behind a raid boss, a pet talent is worth nothing with Lone Wolf. Until
2026-09-27 every leveling build got the same small "leveling utility" for such talents, whatever its playstyle, and the fight-lab
calibration left those values alone when the lab measured them at zero (its noise rule), so a melee hunter took Improved Wing Clip.

Now each soft effect (utility, surv, sustain) carries a **kind** (`kinds.json`): kite, stun, stick, move, range, stealth, avoid,
resist, escape. The value is multiplied by the **scenario weight** (`profiles.json` `kind_weights`) and the **playstyle weight**
(the spec model's `kind_weights`, per profile in `kind_weights_by_profile`, evidence in `kind_note`):

| Kind | Leveling / solo | Raid DPS, healer | Raid tank | PvP |
|---|---|---|---|---|
| kite, stick, move, stealth | 1 | 0 | 0 (move 1) | explicit PvP values |
| stun | 1 | 0 | 1 | explicit PvP values |
| range | 1 | 1 | 0 | explicit PvP values |
| avoid | 1 | 0 | 1 | explicit PvP values |
| resist | 0.25 | 0 | 0.2 | explicit PvP values |
| escape | 0.2 (AoE, solo-60: 0.3) | 0 | 0 | explicit PvP values |

Playstyles: melee models (warrior, rogue, Retribution and Protection paladin, Enhancement, cat and bear, melee hunter) never kite
and gain nothing from range; the pet-tank hunters and the Voidwalker warlock gain nothing from kiting single-target (the pet holds
the mob: Improved Wing Clip -0.2% +-0.3 in the lab); the cat gains nothing from stuns while leveling (Bash is Bear Form). `needs_pet`
(true or the pet's name) zeroes a talent while that pet is not out. `pet_tank` (melee hunter) multiplies eating time when Lone Wolf
sends the pet away (the lab: downtime x2.0-2.5 at 50-60), which is why the melee leveling build keeps its pet.

The same day the leveling time model split downtime into drinking (divided by mana sustain), eating (divided by survival) and fixed
loot/travel, so avoidance and health talents of melee classes are valued through the eating they save instead of through an
inflated death term; and the calibrations were fixed (one shared `splitfx.split`: 109 duplicate copies merged, lost values restored
for Flurry, Twin Disciplines, Divine Precision, Vigor and Death Wish; simulated talents fitted to what the lab measures, zero
included). `scenario_audit.py --write` lists what is still dead or filler in every build (`_reference/scenario-audit.md`).

## PvP profile

`pvp` scores burst (the damage or healing model) x0.4, survival x0.5, mana x0.05 and PvP utility x1.5: explicit values tagged
`modes: ["pvp"]` for control, escape, crowd-control resistance, burst cooldowns, anti-healing and dispels (tiers high 0.04, medium
0.015, low 0.004 at full rank, from the 2026-09-27 class audits), with every other effect taken as in solo-60 (`effects_as`) and
PvP-worthless talents suppressed per class. The weights were tuned on 2026-09-27 by `pvp_check.py --grid` on the ten Classic
community PvP builds (coarse grid: burst 0.4/0.8, survival 0.2/0.5, utility 0.7/1.5, mana 0.05): the chosen point shares 65% of the
points with the community builds, and the Forever PvP drafts share 57% with the scorer's PvP optimum
(`_reference/pvp-check.md`). No simulator plays PvP: these are assumptions.

Known limits (the low-overlap cases): the damage models are sustained raid or leveling splits, so burst finishers the community
builds around (Seal Fate, Cold Blood, Improved Kidney Shot windows) are undervalued and the rogue optimum drifts to Combat; a healing
model cannot value a hybrid's damage talents (the Shockadin's Retribution points), so its optimum drifts to Protection survival;
talents that only feed a source the model lacks (Thousand Cuts and Hemorrhage for a Hemorrhage rogue) read as zero. Check those
builds by hand, not by the PvP score.

## Raid DPS profile: the training dummy (Forever)

Since 2026-09-27 the Forever `raid-dps` profile scores your own DPS only (`no_utility: ["forever"]`): its raid-mode values are fitted to the community simulator on a boss-level training dummy with only your own buffs (`raidsim/run.py`), so a talent that buffs the raid counts for what it does to you. Classic Era keeps the raid-team view (utility for buffs brought to the raid) so the community raid builds stay the calibration cases. Specs that live on other players' mana buffs run dry on the dummy, so their mana talents are worth more under this profile than in a buffed raid.

## Parse profile

`parse` (profiles.json) scores personal DPS only: no utility term, and the raid supplies every buff and debuff including the ones
the spec could bring itself (Winter's Chill, Improved Scorch, Improved Shadow Bolt, Trueshot Aura, Leader of the Pack, Moonkin
Aura, Sanctity Aura, Improved Battle Shout as profile extras; those talents are suppressed where the buff is shared, which in the
beta excludes the mage and warlock debuffs because they are personal there). `rebuild.py --steps raid` exports `opt-<spec>-parse`
for every DPS spec and `raidsim/run.py --env environments` measures it against the raid build on a training dummy, in the raid and
at the maximum. The raid-dps profile remains the "bring the buff" profile with the measured raid values of the support talents.

## Optimizer (`optimize.py`)

- **Build**: bundle-greedy (a talent's next rank is evaluated together with its unmet prerequisites, synergy
  partners and the cheapest gating filler, ranked by value per point), restarted per tree with a "reach 31 here
  first" constraint; then a re-spend pass (drop each talent, refill) and 1–3 point local moves. `total` can be
  lowered for level-N builds (used by the respec planner). Seed builds (`run.py --seed <ids>`, and the `--compare`
  build) go through the same re-spend and local moves, so the result never scores below a seed's own local optimum;
  `rebuild.py` seeds every export with the hand drafts (the greedy search alone missed the warlock's SM/Ruin raid build,
  which the model scored higher than what it found).
- **Order**: receding-horizon — at every level, each remaining talent's bundle is simulated over the next 6
  levels and only the first point of the best plan is committed. Earlier rows are backfilled whenever they score
  higher; capstones are not delayed by zero-value prerequisites. Every order is legal at every level.

## Respec planner (`respec.py`)

"Best at 60" is not "best at 25". `respec.py` builds one *plan* per (spec model, target level 20/30/40/50/60):
the optimizer's best build for that level, bought in optimizer order, then extended greedily to 60. A dynamic
programme then chooses at which levels to respec between plans, charging the Classic respec price (1g, then +5g
per respec, cap 50g) converted to hours through a gold-per-hour table, and minimising total hours
(hours-per-level × (1 − leveling score)). Output: `<class>/talents/<forever|classic-baseline>/respec-plan.md` with
the recommended schedule (with its point-by-point path), the best never-respec plan, per-model schedules when a
class has several leveling models, and every plan's score curve. The hours/gold tables at the top of `respec.py`
are assumptions — change them and re-run. Finding: in most classes the level-30/40 plan extended greedily beats
playing toward the 60 build from level 10 (the `opt-*-leveling-st` order), so the respec page is the better
leveling path even when it says "never respec".

## Spec loops and the loop audit (`loop_audit.py`, `loops/`)

Numbers alone miss talents whose job is structural (Improved Blizzard makes AoE grinding possible; Improved
Frost Nova keeps the pack off you; Unleashed Fury is the hunter's tank). `loop_audit.py` lists every talent a
Classic community build takes that the model values under 0.4%/point; `loops/<class>.json` records, per spec,
the purpose, the loop, its constraints and — per flagged talent — the role (enabler / control / safety /
throughput / sustain / utility / filler / avoid), the guide's reason and its source, and how the reason was
turned into a number in the manual effect files for **both** games. See `loops/README.md` for the process and
what the first pass changed.

## Buff / nerf report (`compare_effects.py`)

For every Forever talent: rank/row changes, the encoded effects at max rank in both games, the model's value of
the full talent in every spec/profile the class has optimizer output for (Classic → Forever), and a verdict
(buff / nerf / same / reworked / new / removed), plus a "builds that changed" section comparing each `opt-*`
build with the Classic build it was calibrated against. Output: `changes/<class>.md`, index in `changes/README.md`.

## Calibration against Classic (does the model rediscover the known-optimal builds?)

| Case | Community build | Model result | Verdict |
|---|---|---|---|
| Hunter raid (mm-raid / raid-dps) | 20/31/0 BM/MM | 20/31/0 exactly, once Trueshot Aura carries its measured raid value (+2.8% DPS to each of four melee, `raid-buff-values.md`) | pass |
| Hunter leveling (bm-leveling / leveling-st) | 31/20/0 | 31/11/9 — same Beast Mastery core; Survival's Improved Tracking instead of the last Marksmanship fillers (the leveling values are the Forever fight lab's, so this case drifts with Forever's calibration) | pass |
| Mage raid, lone frost mage (frost-raid / raid-dps) | 17/0/34 Winter's Chill | 21/0/30 deep Frost with Winter's Chill — the simulator ranks Arcane Power 4% above it for one mage's own DPS, but Winter's Chill's measured raid value (+7% to each of four other frost mages) puts the lone mage back on the debuff build | pass |
| Mage raid, second frost mage (frost-raid / raid-dps-extwc) | 31/0/20 Arcane Power | 32/0/19 — same score, zero-value fillers differ | pass |
| Mage raid fire (fire-raid / raid-dps) | 17/31/3 | 17/31/3 — same core | pass |
| Mage AoE grinding (frost-aoe / leveling-aoe) | Icy Veins 19/0/32 (no Shatter) and Warcraft Tavern 7/0/44 (Shatter 5) | 7/0/44 — the Warcraft Tavern build exactly, since the fight lab's 4-mob calibration and the talent-created Ice Lance source (2026-09-26) | pass |
| Mage ST leveling (frost-leveling / leveling-st) | deep Frost | 10/0/41 deep Frost | pass |
| Warrior raid Fury (fury-dw-raid / raid-dps) | 17/34/0 | 17/34/0 exactly | pass |
| Warrior raid tank (prot-tank / raid-tank) | 11/5/35 deep Prot | 0/20/31 — Protection core (Defiance, Shield Slam, One-Handed Spec, Imp Shield Block) with Fury rage/crit talents instead of Anticipation/Toughness (which Icy Veins itself calls weaker than they look) | partial (a known Fury/Prot hybrid) |
| Warrior leveling (arms-2h-raid / leveling-st) | Arms 31/20/0 | 2H Fury 20/31/0 scores higher | partial (2H Fury leveling is a recognised alternative) |
| Rogue raid swords (combat-swords-raid / raid-dps) | 19/32/0 | 19/32/0 | pass |
| Rogue raid daggers (combat-daggers-raid / raid-dps) | 15/31/5 | 15/31/5 | pass |
| Priest raid healer (holy-heal / raid-heal) | 21/30/0 Disc/Holy | 21/30/0 | pass |
| Priest leveling (shadow-dps / leveling-st) | deep Shadow | 14/0/37 | pass |
| Paladin raid healer (holy-heal / raid-heal) | 31/11/9 | 32/18/1 — Holy core (Illumination, Divine Favor, Holy Shock, Holy Power) with Prot fillers (Blessing of Kings) | pass |
| Paladin ret (ret-dps / raid-dps) | 11/0/40 | 10/11/30 — same Retribution core (Seal of Command, Vengeance, Two-Handed Spec, Conviction, Sanctity Aura); 11 Protection for Blessing of Kings/Precision instead of deep-Ret fillers | partial |
| Paladin prot (prot-tank / raid-tank) | 11/40/0 | 11/32/8 — same Protection core (Holy Shield, Redoubt, Shield Spec, Imp Righteous Fury, Reckoning); 8 Retribution (Benediction, Deflection) instead of deep-Prot fillers | partial |
| Shaman raid healer (resto-heal / raid-heal) | 0/5/46 | 0/7/44 — same core (Healing Way, Purification, Nature's Swiftness, Mana Tide, Tidal Mastery) | pass |
| Shaman elemental (elemental-dps / raid-dps) | 31/0/20 | 31/0/20 | pass |
| Shaman enhancement (enhancement-dps / raid-dps) | 0/31/20 raid support | 18/31/2 — same Enhancement core (2H, Flurry, Elemental Weapons, Weapon Mastery, Stormstrike); Elemental shock talents instead of Resto support (the raid-support value is only utility here) | partial |
| Shaman leveling (enhancement-dps / leveling-st) | 0/31/20 | 13/31/7 — same Enhancement core, 2H at 20, Stormstrike at 40; Elemental and Survival-side fillers instead of Restoration | pass |
| Warlock raid (sb-raid / raid-dps) | SM/Ruin 30/0/21 and DS/Ruin 7/21/23 | 30/0/21 SM/Ruin exactly (the greedy search alone stopped at a 17/3/31 Ruin build the model scores lower; the search is seeded with the compared build since 2026-09-26); the Classic simulator itself ranks DS/Ruin below SM/Ruin with its succubus preset | pass |
| Warlock leveling (affliction-leveling / leveling-st) | 30/21/0 Aff/Demo | 31/8/12 — same Affliction core; Demonology pet talents rank below Destruction cast-time talents | partial |
| Druid raid healer (resto-heal / raid-heal) | 5/0/46 Swiftmend | 5/0/46 | pass |
| Druid cat (feral-cat-dps / raid-dps) | 14/32/5 | 14/31/6 — same core (Natural Weapons, Omen of Clarity, Furor, HotW, LotP, Blood Frenzy) | pass |
| Druid bear (feral-bear-tank / raid-tank) | 14/32/5 | 14/31/6 | pass |
| Druid moonkin (balance-dps / raid-dps) | 35/0/16 | 35/0/16 exactly | pass |
| Druid leveling (feral-cat-dps / leveling-st) | 14/32/5 | 15/31/5 | pass |

Re-check of 2026-09-26 (`classic_check.py`, after the spec models' shares, time splits and fight coupling were fitted to the Forever
simulators): 21 of 30 optimized builds unchanged; cat leveling (now 14/32/5, the community build exactly), Fury raid (17/34/0 exactly),
BM leveling (32/11/8), Ret leveling (11/11/29), Shadow leveling (11/0/40) and Enhancement leveling (19/31/1) moved toward or onto the
community builds; swords leveling (14/37/0 vs 19/32/0) and the warlock raid (9/21/21 DS/Ruin vs SM/Ruin 30/0/21, scores within 0.5%)
moved away. The Classic pages carry the new results; the verdicts above still hold.

Re-check of 2026-09-26 (evening), after the Classic-era models got their own measured inputs: the raid damage split and the
raid-mode talent values now come from the upstream wowsims/classic simulator (`rebuild.py --steps classic`, reports under
`<class>/talents/classic-baseline/raidsim/`, shares in each source's `game_overrides["classic-era"]`, fits in
`effects/classic-era/`), and the optimizer's search is seeded with the compared build. Six cases changed against the morning
check: moonkin raid (35/0/16, the community build exactly) and the warlock raid (30/0/21 SM/Ruin exactly) moved onto the
community builds; MM raid (22/29/0, no more Survival points) moved toward it; the lone frost mage moved to Arcane Power
(31/1/19: the simulator ranks it 4% above the Winter's Chill build for one mage's own damage once the raid set no longer
supplies Winter's Chill), AoE grinding to 4/0/47 (from the fight lab's 4-mob calibration) and enhancement raid to 18/31/2.
The first Classic pass had measured Winter's Chill, Improved Scorch, Leader of the Pack and Improved Shadow Bolt at zero
because the simulator's full raid set already carried them; those buffs are now switched off for the spec that provides them
(`raidsim/classic_specs.py`, `buffs_off`/`debuffs_off`). Trueshot Aura, Sanctity Aura and Moonkin Aura still measure zero
there: the simulator applies those auras from raid-buff flags and player options rather than from the talent, so their own
value stays a manual (structural) entry. Table updated to these results.

Re-check of 2026-09-26 (night), after talent-created abilities became gated sources (Ignite, Pyroblast, Bloodthirst, Mortal Strike,
Deep Wounds, Stormstrike, Insect Swarm, Mind Flay, Ice Lance, Riposte, Siphon Life, Summon Hawk; Aimed Shot and Consecration in
Classic) and every leveling and raid value was re-fitted: four cases changed. AoE grinding now lands on Warcraft Tavern's 7/0/44
exactly and the priest's leveling build stays deep Shadow (12/0/39); swords leveling moved to 18/33/0 (same core); BM leveling moved
to 17/31/3 because the leveling values are the Forever fight lab's, where the hunter levels fastest with 31 Marksmanship points
(Summon Hawk, Ranged Weapon Specialization): Classic has no fight lab of its own, so this is the cross-game leak the note above
describes, not a Classic finding. Table updated.

Re-check of 2026-09-27 (after the raid-buff values, the tank calibration, the healer lab and the AoE variants): 30 cases, one
moved against the previous pages — the lone frost mage returned to 21/0/30 deep Frost with Winter's Chill once the debuff's
raid value was tagged to the frost model (untagged, the same value had sent it into Fire for Improved Scorch). Exact matches:
moonkin, MM raid, fire, holy priest, both rogues, elemental, the warlock, fury, the resto druid; BM leveling is back at 31/11/9.
Table updated.

Loop audit (2026-09-26 night): every flagged talent without a documented reason (40 across the nine classes) now has a role, a reason
and a source in `loops/<class>.json`; the raid-buff talents carry measured raid values (`_reference/raid-buff-values.md`).

Calibration reports for every row: `<class>/talents/classic-baseline/optimizer/<spec>-<profile>.md`. `classic_check.py` re-runs every
row and reports whether the optimized build moved (the spec models' shares, time splits and fight coupling are shared by both games and
are fitted to the Forever simulators since 2026-09-26, so the scores move with them; the builds are what the table judges).

## Results for WoW: Forever — see `<class>/<scenario>/optimizer/`, the `opt-*` builds and `changes/`

Headlines after the 2026-09-25 refresh (beta client build 1.60.1.70009; all subject to the encodings; scores are vs. a
talentless character of the same model, so compare builds *within* a model, and across models only through
`abs_dps_factor`). The demo-era results are in `_reference/beta-refresh-2026-09-25.md` next to these:

- **Hunter**: pet Marksmanship 9/37/5 (+61%), Lone Wolf 7/39/5 (+98% vs its own petless baseline); Beast Mastery
  leveling 33/16/2 and solo 31/20/0. Multi-Shot and Aimed Shot lost most of their flat damage in the beta, so the
  yellow-shot talents fell and Auto Shot talents rose.
- **Mage**: raid Frost 21/0/30 (+119%; Winter's Chill stacks to 5 again, so the lone-mage build keeps it), with an
  external Winter's Chill 28/0/23 (+119%); Fire 14/32/5 (+91%); Frost leveling 21/2/28 (+44%); AoE grinding 19/0/32
  (+51%). Fire leveling 31/18/2 (+32%) still trails Frost.
- **Warrior**: Fury 18/33/0 (+82%); with a two-hander the model now prefers **Arms 38/13/0 (+87%)** (Bloodthrill doubled
  to 4-20% on main-hand attacks, Slam on an 18s cooldown) over Fury (+82%); Protection 8/5/38 (+87%: Sunder Armor's
  explicit 1013 threat and the stronger Revenge make Focused Rage/Bastion/Shield Slam the core).
- **Rogue**: daggers 21/28/2 (+91%: Mutilate with Combat's Hack and Slash/Flawless Execution) ahead of swords 18/33/0
  (+58%); dagger leveling 21/28/2.
- **Priest**: Holy/Disc healer 22/29/0 (+85% healing score: Improved Power Word: Shield 7/14/20 and Mental Agility
  3/7/10 raised Discipline); Shadow raid 20/0/31 (+111%); Shadow leveling 14/0/37 (+47%).
- **Paladin**: Holy healer 23/0/28 (+44%); Retribution 20/0/31 (+102%: Holy Power's Holy Strike crit and Improved Seals
  pull 20 points into Holy now that Crusade is gone and Vengeance stacks 3); Protection 4/31/16 (+56%); Ret leveling
  20/0/31, solo 16/0/35.
- **Shaman**: Resto 0/10/41 (+73%); Elemental 31/6/14 (+99%: 2.5s Lightning Bolt, Lava Burst, Elemental Alacrity at
  tier 3); Enhancement 1/34/16 (+105%: Mental Dexterity's 100% of Intellect as attack power, Stormstrike, Maelstrom
  Weapon, Water Shield); Enhancement leveling 0/34/17.
- **Warlock**: Shadow Bolt raid 10/11/30 (+147%: Demonic Sacrifice (Imp, +15% Shadow) plus Shadow and Flame; DS/Ruin
  is back in a new shape); Affliction DoT raid 21/0/30 (+110%: Wrack replaced Drain Hope, Improved Drains and Soul
  Siphon reworked); Fire Destruction 9/11/31 (+170% against its own baseline); Affliction leveling 25/24/2 (+36%).
- **Druid**: Resto 11/5/35 (+102%: Swiftmend, Wild Growth, Gift of the Earthmother, Genesis); Cat 9/35/7 (+113%:
  King of the Jungle's 60 Energy, Rend and Tear, Berserk); Bear 9/40/2 (+83%: Primal Bite, Natural Reaction);
  Balance 36/2/13 (+157%: Eclipse, Nature's Grace, Vengeance); Cat leveling 12/31/8, Balance leveling 40/11/0.

Which Classic talents each Forever build drops and which new ones it adds: `changes/<class>.md` ("Builds that
changed"). When to respec while leveling: `<class>/leveling/respec-plan.md`.

## Calibration to the fight lab (first pass 2026-09-26; re-run by `rebuild.py`)

`_reference/data/fightlab/` plays fights out in time with dice (same-level mobs, rolled hits/crits/procs/pushback,
drinking, deaths) and `fightlab/calibrate.py` fits this scorer to it. What the Frost mage sim changed here:

- **The leveling score gained a fight-length coupling** (`fight_coupling` per spec model): downtime and death time
  scale with fight length (measured ~1.0: shorter fights mean fewer casts and fewer hits taken). Without it no set of
  damage effects could reproduce the sim, where Ice Lance, Shatter, Ice Shards and Frostbite are each worth 6-35% of
  time per kill at once.
- **The frost-leveling model** now carries the measured rotation: Ice Lance ~60%, Frostbolt ~20%, Fire Blast ~15%, Cone
  of Cold 4%, Frost Nova 2% (Classic Era keeps the old shares through `game_overrides`), and a 50/45/5 fight/downtime/
  death split; the fire-leveling model was fitted separately with its own playstyle (Fireball/Scorch/Fire Blast, Frost
  Nova, Ice Lance).
- **Fitted leveling values** (relative to the build, mean over levels 30 and 60 and over five builds; original scorer
  value → fitted vs sim): Ice Lance 1% → 30% (sim 36%), Shatter 29% → 20% (20%), Ice Shards 25% → 14% (14%), Frostbite
  3% → 16% (16%), Fingers of Frost 11% → 6% (6%), Ice Barrier 3% → 6.5% (6%), Improved Frostbolt 4% → 2.7% (2.7%),
  Winter's Chill 4% → 0.6% (0%), Arcane Instability 6.7% → 3.4% (3.5%: the scorer has no crit cap and the Frozen Ice
  Lance already crits ~80%), Wake of Fire in the fire model 18% → 0.3% (−5%: Blast Wave breaks the root). Fitted effects
  are tagged `specs` per model, so the fire-leveling model keeps its own numbers.
- **The fit is joint over builds.** Values are in-build marginals: fitted to one build at a time, the optimizer swung
  between an Arcane-heavy 28/0/23 and a deep-Frost 0/5/46 from round to round (each fit pushed the next build
  elsewhere). Calibrating against all candidates at once (`--builds` with the hand draft, the optimizer's build and its
  earlier candidates, saved under `mage/leveling/fightlab/candidates/`) converged in one round.
- **Result:** the optimizer's Frost leveling build is 12/3/36 (Ice Lance at 20, Shatter by 29, Ice Barrier at 40,
  Arcane Concentration last). In the sim it is the fastest build at 20, 40, 50 and 60 (28.3 s per kill at 60 vs 28.9
  for the hand-drafted `leveling-frost`, whose leveling order was itself revised from the sim on 2026-09-26) and 6%
  behind at 30, where its order buys Frost Channeling before Ice Shards. The 28-point Arcane detour the scorer used
  to like (Arcane Mind, Missile Barrage, Improved Counterspell, Magic Absorption) is worth ~0 in the sim; the sim
  then had no caster mobs (added the same day, so Improved Counterspell now measures) and never casts Arcane Missiles, so only Arcane Instability and Arcane Mind were fitted and the
  other manual values stand. The "fire-leveling" model's optimizer produces a Frost/Arcane build too (22/3/26): under
  the beta numbers no Fireball rotation competes with Frost Nova → Ice Lance (the Fire playstyle is 8-10% slower per
  kill with the same talents).
- **The other eight classes** were calibrated the same way on 2026-09-26 (first pass, mob tables from zone rules of thumb; that
  pass found Shadowform and Mind Flay ~40% each for the priest, Mortal Strike 40% for the warrior, Shamanistic Focus 15% and
  Sanctified Judgement 8% for the mana-bound shaman and paladin, King of the Jungle 14% for the cat, the rogue's survival
  talents large, and Wrack, Improved Judgement, Maelstrom Weapon and Vampiric Embrace zero or negative) and are re-calibrated
  by `_reference/data/rebuild.py` whenever the sim changes — on 2026-09-26 the mob tables moved to the Classic 1.12 creature
  database (mobs hit about half as hard as the rule of thumb assumed), caster mobs and Bear Form were added and the leveling
  order gained the deep-talent rush rule. The current fitted values, kill times and talent rankings are in each class's `leveling/README.md`
  "Fight lab" section (generated), `<class>/leveling/fightlab/<spec>-calibration.json` and `_reference/fightlab-summary.md`.
- Full tables: `<class>/leveling/fightlab/<spec>.md`, `sensitivity.md` (the ranking under moved mob health, mob damage,
  root breaks, pushback, gear tier and caster share), `*-calibration.json`; the candidate builds raced in the sim are in
  `fightlab/candidates/` (`run.py --compare <file.json ...>`); `fightlab/last-rebuild.json` says which build won the last race.

## Coverage and limits

- **Encoded classes: all nine** (both games), with healer models for Priest, Paladin, Shaman and Druid and tank
  models for Warrior, Paladin and Druid. Parsed coverage is ~50–60% of talents per class; the rest is hand-entered.
- Cross-model comparisons (pet vs. no pet, Fire vs. Shadow) use the **absolute DPS index** printed in the report
  (`abs_dps_factor`); raw scores are relative to each model's own talent-less baseline. Only Hunter's factors
  have been estimated so far; the ElliotWood/Forever simulator's per-spec results (beta pass) are listed in
  `_reference/beta-refresh-2026-09-25.md` as candidates but not adopted.
- Hand-entered values are the weakest inputs; every talent rank's text is now the beta client's (build 1.60.1.70009,
  level-60 tooltips), so the second-weakest inputs are the spec models' shares and the proc/uptime arithmetic in the
  manual files. The `notes` say which each entry is; `<class>/spells/README.md` holds the beta spellbook numbers.
- Mana-cost effects use the *largest* mana share among the abilities in their scope (not the sum); lists that
  cover a whole spec are encoded as `type:spell` or a group tag (`dmgspell`, `ability:Destruction`) instead.
- Rotations are fixed shares: the model cannot tell that a DS/Ruin warlock skips Corruption or that an
  Enhancement shaman's Lightning Bolt share grows with Maelstrom Weapon (the latter is encoded as a damage bump).
