# Raid sim — level-60 raid builds through the community simulator

The fight lab (`../fightlab/`) covers leveling. For level-60 raid DPS the community has a full simulator for the Forever
beta: the ElliotWood/Forever fork of wowsims (Go, https://github.com/ElliotWood/Forever), with the beta client's spells,
talents, items, buffs and per-spec rotations (APLs) and gear presets. `run.py` pushes our raid builds through it, next to the
simulator's own preset talent builds, with everything but the talents held fixed, and writes one report per spec model.

```
python _reference/data/raidsim/setup.py                       # once: Go + protoc + sparse clone + build (~400 MB under ~/.wow-forever-tools)
python _reference/data/raidsim/run.py mage --spec frost-raid --write
python _reference/data/raidsim/run.py --all --write           # every spec in specs.json (about 10 minutes at 3000 iterations)
python _reference/data/raidsim/run.py druid --spec feral-cat-dps --deltas opt-feral-cat-dps-raid-dps   # talent-by-talent removal values
python _reference/data/raidsim/calibrate.py druid --spec feral-cat-dps --write   # fit the scorer's raid values to those removals
python _reference/data/render_raidsim_sections.py             # the "Raid sim" section of each <class>/raid/README.md + _reference/raidsim-summary.md
python _reference/data/rebuild.py --steps raid,regen          # calibrate <-> optimize <-> race for every raid DPS model, then the pages
python _reference/data/raidsim/setup.py --update              # pull the simulator's master and rebuild
python _reference/data/raidsim/setup.py --game classic        # once: the upstream wowsims/classic simulator (Classic Era) next to it
python _reference/data/raidsim/classic_specs.py               # specs-classic.json from the clone's presets (+ our gear sets copied in)
python _reference/data/raidsim/calibrate.py mage --spec fire-raid --game classic-era --write   # Classic split + fits into the classic-era game
python _reference/data/raidsim/run.py --all --game classic-era --write                         # every Classic spec vs the sim's presets
python _reference/data/rebuild.py --steps classic             # all of the above for every class, then scorer/classic_check.py --write
```

| File | What it is |
|---|---|
| `setup.py` | Downloads Go and protoc into the tools folder (nothing system-wide), sparse-clones the simulator, generates its protobuf code, builds `wowsimcli` and our `foreverbench` |
| `foreverbench/main.go` | A small Go tool compiled inside the simulator: one gear set, rotation, encounter and buff set, N talent strings in, DPS / threat / OOM per build out (JSON lines) |
| `specs.json` | Our scorer spec id → the simulator's spec folder, gear preset, APL, player options, consumables, race, and the build ids raced by default (all from the folder's `presets.ts`). `buffs_off` / `debuffs_off` name fields of the simulator's full buff set that the spec itself provides through a talent (Trueshot Aura, Leader of the Pack, Moonkin Aura; in Classic also Sanctity Aura, Winter's Chill, Improved Scorch, Improved Shadow Bolt): the bench clears them so the talent is measured instead of duplicated by the raid |
| `rebuild.py --steps raid[,adopt]` | Calibrate ↔ optimize (stops when a new build is not 1% better in a quick race) → race with the presets → the best optimizer round is promoted into the `opt-*` build → with `adopt`, a winner over 2% ahead of the best hand raid draft replaces it (old draft kept as `raidsim/candidates/cand-<spec>-hand-<date>.json`, core/flex from the removal values) |
| `calibrate.py` | Fits the scorer's raid-mode values (`modes: ["raid"]`, tagged with the spec) to the simulator's removal deltas over several builds, like `fightlab/calibrate.py` for leveling; writes `<class>/raid/raidsim/<spec>-calibration.json`. A talent the simulator measures whose fitted values are all zero (zeroed by an earlier fit in another setting) is re-seeded from its own values in other modes or its tooltip before the fit ("re-seeded" in the note). A talent the model has no channel for (Shredding Attacks in a cat model without a Shred source) is reported as "capped" and needs a template by hand. `specs.json` entries may name `share_build` (the build whose damage split becomes the model's shares) and `not_measured` ({talent: why}: values the standard target cannot show, kept out of the fit, e.g. Murder's Humanoid/Giant bonus); crit fits stop at +50% per talent (`CHANNEL_MAX`) because the scorer caps crit at 100% |
| tanks | Tank specs (`"tank": true`, profile raid-tank) report damage taken per second next to threat (the bench emits `dtps`, `tmi` and threat per action) and rank by **tank value** = the raid-tank profile's weights on threat per second and on damage avoided, relative to the hand draft; their shares are threat shares and their removal deltas combine threat and mitigation the same way, so `calibrate.py` fits the tank-mode values (`modes: ["tank"]`) and `rebuild.py --steps raid` runs calibrate ↔ optimize ↔ race for the three tank models too |
| `run.py --env environments` | The same builds (ours, the parse build and the presets) on a training dummy (alone, no buffs or consumables, a level-60 target, no execute phase), in the raid setting and at the theoretical maximum (the highest-phase gear preset of the spec's family, every buff and debuff on, consumables and the Classic sim's world buffs, 120 s and 60 s): `<spec>-environments.md`. The scorer's `parse` profile (`scorer/profiles.json`) is the parse build: personal DPS only, the raid brings every buff |
| `apl_opt.py` | The rotation search (2026-09-27): local search over a spec's action priority list (move, drop, show or insert an action from the class's other rotations; drop or loosen a condition; change a threshold; add a mana or fight-time guard; a lower spell rank always or below a mana share; a two-edit lookahead), common random numbers on the spec's main builds, kept only when a second seed confirms it and no tuning build loses more than 0.1%. One search per kind of setting: `apl_opt` (training dummy) and `apl_opt_raid` (fully buffed raid) in specs.json, `apls/<class>/<spec>[-raid].apl.json`, record `<class>/raid/raidsim/<spec>-rotation-search.json`. `run.py apl_path` picks the rotation per setting; nothing found = the simulator's rotation stays. Rotation-only entries (`rotation_only`, `preset_names`) cover talent trees without a scorer model |
| `apl_opt.py` pools (2026-09-28) | Besides the class's other rotations the search inserts explicit casts of each cooldown the builds use (zero-damage actions cast 1-4 times a fight: `use every other cooldown` is all or nothing) and the top rank of every spell the beta spellbook marks new against Classic Era (the simulator's rotations never cast some of them). A search from our tuned rotation adds a pass to the record (`passes`). An entry's `apl` can be our own base rotation (`apls/<class>/<spec>.base.apl.json`, origin in `rotation_note`); `tune_builds` names more builds the search must not cost. A condition on an aura a build does not know vanishes in the simulator (the line then fires always or never): guard such lines with `auraIsKnown` |
| `talent_opt.py` | Talents searched in the simulator itself, for builds no scorer model covers (hybrids, rotation-only trees): local search over legal 51-point allocations (moves of 1, 2, 3 or 5 points), common random numbers, confirmed on a second seed, never dropping a talent the rotation conditions on (`--keep`, `--allow-drop`). Writes a candidate file with its `search` record; tune the rotation and the talents in turns |
| `patches/` | Our additions to the community simulator, copied and inserted by `setup.py` on every build and reset before `--update` (`patches/README.md`): Frostfire Bolt, which the fork ships as a stub. Numbers that depend on a patch are our model |
| potions (2026-09-28) | The simulator builds the potion and conjured-item cooldowns only from the lists its UI sends (`potions`, `conjuredItems`); `foreverbench` now adds the configured `potId` / `conjuredId` to them. Before 2026-09-28 no run used a potion, a Demonic Rune or Thistle Tea |
| `run.py --preset-candidates` | The simulator's presets within 6% of the spec's best build in the last race, saved as `<class>/raid/raidsim/candidates/cand-<spec>-preset-<name>.json` (2026-09-27; `rebuild.py --steps raid` runs it first): `calibrate.py` measures their talents with ours, the optimizer is seeded with them (`scorer/run.py --seed` takes candidate files), the race runs them under their own "sim preset: X" label, and `adopt` can adopt one that beats the best hand draft by over 2% (crediting its `presets.ts`). Reports list them as the simulator's, not ours |
| mana limit | Forever DPS specs on the dummy: `calibrate.py` also runs its builds with every mana-only buff on (`run.py`'s `dummy-surplus` setting: Mana Spring, Mana Tide, Blessing of Wisdom, Innervates, Judgement of Wisdom) and takes the damage gained as each build's mana deficit (5-30% for every mana user on 2026-09-27; out-of-mana seconds miss a Frost mage's Evocation and a warlock's Life Taps). It fits the spec model's `mana_limit` (loss and cap: the mana-bound damage shrinks by min(cap, max(0, loss - (sustain - 1))); the mana talents' sustain comes from their removal runs) to those deficits, alternating with the talent fit (which runs last), takes the model's damage split from the run with every mana buff on (the split before the limit), and writes the table into `<spec>-calibration.json` ("mana") |
| `run.py --deltas` | Removal runs; a talent the rotation *conditions* on (Improved Scorch's stack loop, the Classic mage APL's Combustion gate) is flagged `apl_dependent`: its removal breaks the rotation, `calibrate.py` keeps its manual value ("apl"). Since 2026-09-27 a condition on a proc aura the simulator's spell data names after the talent (`FingersOfFrostTriggered`, `HotStreakTriggered`, `MaelstromWeaponTriggered`, `RedoubtTriggered`) flags it too: those removals had measured +189%, +74.5% and +113.5% |
| `run.py` | **Setting:** Forever DPS specs run on a boss-level training dummy with only your own buffs (the class's self-buffs, `self_buffs` / `self_debuffs` in specs.json, the spec's standard consumables; no raid buffs, no debuffs from others): raw personal DPS ranks the raid DPS builds (2026-09-27). Tanks and the Classic sim use the full raid setting; `--setting raid|dummy` overrides. Converts our allocations to the simulator's talent strings (from `ui/sim/talents/trees/<class>.json`; the names match ours, same beta client), runs the bench, adds the scorer's score, writes `<class>/raid/raidsim/<spec>.md` + `.json` |
| `classic_specs.py`, `specs-classic.json`, `gear_sets/classic/` | The same mapping for the upstream wowsims/classic simulator (Classic Era, `~/.wow-forever-tools/classic-repo`, bench `classicbench`): spec folders are `ui/<spec>/`, talent names map to its camelCase `fieldName`s, the Player carries enum-based `consumes`. The ret sim ships no gear preset, so `gear_sets/classic/retribution_paladin/p1_plate_2h.gear.json` (warrior phase-1 plate + Bonereaver's Edge) is copied in. `run.py`/`calibrate.py --game classic-era` read `<class>/talents/classic-baseline/builds.json`, write `<class>/talents/classic-baseline/raidsim/` and the scorer's classic-era game (shares into each source's `game_overrides`, fits into `effects/classic-era/`) |

## What the numbers mean

- **Fixed:** the simulator's phase-1 (or default) gear preset, its default rotation for the spec, its default consumables and
  options, the full raid/party/individual buffs and debuffs its own tests use, a single level-63 target, 120 s with the
  standard execute phases, 3000 iterations, seed 1. Every build in a table shares all of that, so the table ranks **talents**.
- **Not fair:** a build whose playstyle the rotation does not express (a Fire mage under the Frost APL, a Survival melee hunter
  under the ranged APL). `specs.json` pairs each spec model with the matching APL; hybrids are noted in the report.
- **Not simulated:** healers — the simulator's healer specs are gear planners only ("no healing spells are implemented, so there is no
  simulation for this spec" in its `ui/specs/priest/healer/spec.ts`, checked 2026-09-26), so the four healer models stay expected-value
  scores; PvP and leveling builds (that is the fight lab's job).
- **Provenance:** the simulator is the community's model of the beta; its results are simulations of that model, not
  measurements. The report header records the simulator commit, preset files and settings.
- **Scorer column:** our expected-value model's score of the same allocation for its raid profile, for comparison only
  (relative to a talentless character, comparable within one spec model). `--deltas <build>` adds the sim's value of every
  talent in a build (DPS lost when removed) next to the scorer's, and `calibrate.py` fits the scorer to it.
- **Buff duplication:** with the simulator's full raid buffs, a talent that duplicates a buff someone else brings (Leader of
  the Pack, Trueshot Aura, Moonkin Aura) measures zero; the calibration writes that into raid mode, which is right for a
  buffed raid and wrong for the one player who must bring the buff.
- **Mana limit caveats (2026-09-27):** the limit knows a build's mana only through its talents' sustain, not through how fast its
  rotation spends mana, so builds that spend at different rates leave a fit error (MM hunter about 5 points of deficit, Elemental
  and Balance 3-4; Frost, Destruction, Ret and Enhancement about 1). A talent no calibration build takes keeps its manual raid value:
  a healer's generic mana value (Penance's +3% mana efficiency, untagged) then counts for a DPS model too and can show up as a
  "best next point" in the scenario audit; the optimizer has not taken one, and a race would measure and correct it. The dummy's
  mana pressure also moves builds away from what a buffed raid wants: the MM hunter and Ret drafts adopted on the dummy lose
  6% and 3% to their previous drafts in the raid setting, so those drafts are kept as companions for a fully buffed raid
  (`bm-mm-full-buffs-raid`, `ret-full-buffs-raid`, registered in specs.json so they are raced; user choice 2026-09-27).
- **Shares:** the bench reports damage per action; `run.py` names the actions (the simulator's spell table, our spellbook ids,
  its talent tree) and maps them onto the spec model's sources by `ability:` tags, white attacks and pets; `calibrate.py`
  writes that split into the model's base shares (the raid split), while the fight lab's leveling shares sit in each source's
  `profile_overrides`. Damage that matches no source is reported as unmatched (add a source with the right `ability:` tag).

## Classic Era check

The scorer's Classic-era models were calibrated by hand against community builds. `rebuild.py --steps classic` measures the
Classic raid damage split and the talent removal values in the upstream wowsims/classic simulator (the Classic Era sim, not
a beta model), writes them into the classic-era game of the scorer and re-runs `scorer/classic_check.py --write`: the
optimizer must still land on the community builds. Reports: `<class>/talents/classic-baseline/raidsim/<spec>.md`. Our
builds there are the community builds, so a sim preset ahead of them means the sim's rotation prefers other talents, not
that the community was wrong. Unmatched damage (Ignite, Bloodthirst, Stormstrike, Windfury: talents that create a damage
source the models carry as a talent effect rather than a source) is dropped before the split, the same as for Forever.
The first Classic pass (2026-09-26) measured Winter's Chill, Trueshot Aura, Leader of the Pack, Sanctity Aura and Improved
Scorch at zero because the simulator's full raid buffs already carried them; `buffs_off` / `debuffs_off` in `classic_specs.py`
(and `specs.json` for Forever's party buffs) switch a spec's own buff off in the bench. The optimizer runs of the check are
seeded with the community build (`scorer/run.py --compare` also seeds the search), so a case can no longer fail only because
the greedy search missed a build the model itself scores higher. The switches work for Winter's Chill, Improved Scorch,
Leader of the Pack and Improved Shadow Bolt (measured 6.9%, 37%, 2.8% and 9.7% of DPS afterwards); Trueshot Aura, Sanctity
Aura and Moonkin Aura still measure zero because the simulator applies them from raid-buff flags / player options, not from
the talent — their own value stays a manual entry.

## Adding or changing a spec

Add an entry to `specs.json`: the simulator's `ui/specs/<class>/<spec>/presets.ts` lists the gear sets, APLs, `DefaultOptions`
(translate the TS enums to protojson names, e.g. `MageArmor.MageArmorMageArmor` → `"MageArmorMageArmor"`), `DefaultConsumables`
(the keys are already protojson) and `OtherDefaults` (race, distance, professions). The `spec` fragment is the `Player` oneof
in protojson (`mage`, `hunter`, `warlock`, `rogue`, `dpsWarrior`, `protectionWarrior`, `retributionPaladin`, `protectionPaladin`,
`dpsPriest`, `elementalShaman`, `enhancementShaman`, `balanceDruid`, `feralCatDruid`, `feralBearDruid`). Tanks set `"tank": true`.
