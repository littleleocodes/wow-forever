---
name: wow-forever-raidsim
description: "Level-60 raid builds (DPS and tanks) through the ElliotWood/Forever (wowsims) simulator and, for the Classic-era check, upstream wowsims/classic — toolchain, driver, damage/threat shares, talent calibration, buff switches, raid-buff values, APL flags, adoption loop, results after the 2026-09-26/27 runs"
metadata:
  node_type: memory
  type: project
  originSessionId: 1178b215-3b7e-4e8a-a51c-7bba704c0381
  modified: 2026-09-27T01:41:50.191Z
---

`_reference/data/raidsim/`: `setup.py` (Go 1.27 + protoc 36 into `~/.wow-forever-tools`, sparse clones, protobuf gen,
`wowsimcli.exe` + our `foreverbench.exe` from `foreverbench/main.go`; `--game classic` = upstream wowsims/classic into
`classic-repo` with `classicbench.exe`, main.go transformed; a running bench locks its exe: build to a temp name and swap),
`specs.json` / `classic_specs.py` → `specs-classic.json` (spec id → sim folder, gear, APL, options, consumables, race,
`buffs_off`/`debuffs_off`, `"tank": true` + profile raid-tank; Classic talent names → camelCase `fieldName`, our
`gear_sets/classic/` copied in), `run.py` (talent strings, bench, per-action damage **and threat**, `dps`/`threat`/`dtps`/
`tmi`/`tto` per build; actions → model sources by `ability:` tags with stem matching and rank suffixes stripped, ALIASES for
unnamed proc ids (25505 Windfury); tanks rank by **tank value** = threat_weight × threat/hand's + mit_weight × hand's
dtps/this one's, their shares are threat shares, their removal deltas combine threat and mitigation the same way; `--deltas`
flags talents the APL *conditions* on as `apl_dependent` (Improved Scorch's stack loop, the Classic mage's Combustion
gate) — cast-only references are fine), `calibrate.py` (split into base shares or `game_overrides["classic-era"]`, fits
of raid- or tank-mode values; `apl` rows and `utility`/`enable`/`disable` effects never fitted; `--shares-only`),
`buff_value.py` (each raid buff a talent provides measured on every receiving spec with the buff switched off; × assumed
beneficiaries = the provider talent's raid `utility` for profile raid-dps, tagged with the provider specs so a frost mage
gets nothing for Improved Scorch; page `_reference/raid-buff-values.md`; Forever has no switch for TSA/LotP/Moonkin
(fork no-ops) — Classic measurements or the beta tooltip stand in; Improved Scorch, Sanctity Aura and Improved Battle Shout
are analytic), `render_raidsim_sections.py` (class README sections incl. a Classic Era table + `_reference/raidsim-summary.md`),
`rebuild.py --steps raid[,adopt]` (DPS **and tank** models: calibrate ↔ optimize (seeded with the hand drafts) ↔ race,
promotion of the best round, adoption ≥2%) and `--steps classic` (specs, calibrate + run per Classic spec, then
`scorer/classic_check.py --write`, which exits 0). Toolchain: `C:/Users/leohu/.wow-forever-tools/`.

**Sim facts:** Forever fork 40be98e, wowsims/classic 7779ebb (2026-09-26); full buff sets duplicate the specs' own buff
talents (Classic RaidBuffs: TSA, LotP, Moonkin, Sanctity; Debuffs: WC, Imp Scorch, ISB) — switched off per spec; Trueshot /
Sanctity / Moonkin Aura still measure 0 in wowsims/classic (applied from flags/options, not the talent). Removal deltas of
APL-conditioned talents are artifacts (Improved Scorch 37%, Combustion 100%): flagged and kept manual. The Go sims run
3000 iterations in ~1 s. Git Bash PATH needs `/c/...`; python logs need `-u`; never share a log file between two runs.

**Raid-buff values (2026-09-26, per receiver × beneficiaries):** Classic: Trueshot Aura +2.8% × 4 = 11%, Leader of the
Pack +2.0% × 4 = 8%, Moonkin Aura +2.4% × 4 = 10%, Winter's Chill +7.0% × 4 = 28%, Improved Shadow Bolt +8.7% × 3 = 26%,
Improved Scorch 15% × 4 = 60% (analytic), Sanctity 2.6%, Improved Battle Shout 3.5% × 4 = 14% (analytic). Forever: LotP /
Moonkin from Classic, TSA 30 RAP ≈ 2% × 1; WC / Imp Scorch / ISB are personal in the beta (no raid value).

**Results (Forever, P1 presets, 3000 iterations):** every DPS hand draft stands after the 2026-09-27 loops (opt ≤ 2%
ahead: MM 2.0%, ret 1.9%, enhancement 1.7%, fire 1.6%); earlier adoptions kept (affliction 642, fire-destro 616, DS/Ruin
657, lone wolf 741, arms 378, fury 392, elemental 500, balance 515, cat 388). **Tanks (2026-09-27, tank value vs the
hand draft):** prot warrior adopted the optimizer's 14/5/32 (+9.7%; threat 305/s, 717 dtps; preset 0.934), prot paladin
adopted 8/15/28 (+9.6%; 435 threat/s, 1041 dtps; presets 0.915 / 0.891), bear adopted 13/38/0 (+7.4%; 651 threat/s, 1047
dtps; preset 0.931). Healers: see [[wow-forever-fightlab]] (healer lab): priest adopted 22/29/0 (0.592), shaman 0/10/41
(0.646), paladin hand 31/0/20 (0.649) and druid hand 11/0/40 (0.691) stand.
**Classic Era (wowsims/classic, own buffs switched off):** fury 1843 = preset, swords 1267 vs 1273, daggers 1259 vs 1285,
ret 661 vs 710, elemental 730 vs 699, enhancement 777 = preset, cat 671 vs 691, balance 567 vs 565, frost AP 781 vs WC 748,
fire 1003, SM/Ruin 1092, MM 1049 vs 1051. Classic check after the buff values: MM raid 20/31/0 and moonkin 35/0/16 and
warlock 30/0/21 exact; the lone frost mage takes Winter's Chill deep once its raid value is spec-tagged (verify in
scorer/README.md's table); BM leveling 31/11/9; talent-created sources: unmatched damage is gone for fire (Ignite),
fury (Bloodthirst), enhancement (Windfury), balance (Insect Swarm).
**Parse profile and environments (2026-09-27):** `scorer/profiles.json` `parse` = personal DPS only (`no_utility`, the raid
supplies every buff as game-specific `extra_effects`, own-buff talents suppressed where shared; the beta's WC / Imp Scorch /
ISB stay personal); the raid step exports `opt-<spec>-parse` per DPS spec. `raidsim/run.py --env environments` runs the
builds on a training dummy (bench `targetLevel: 60`, `noExecute` via protoreflect, no buffs/consumables), in the raid
setting and at the maximum (`best_gear`: highest-phase preset of the spec's gear family, everything on, 120 s and 60 s)
→ `<spec>-environments.md`, class README table, summary section. Typical Forever: dummy ≈ 65-75% of raid DPS, maximum ≈
raid (phase-1 is the best preset for most specs; the cat's p2 preset lifts it 388 → 617), 60 s +3-10%. Classic maximum uses
Naxx-phase presets: fury 1843 → 2163 (60 s 2322), elemental 730 → 1051, cat 671 → 1563; dummies run at 30-45% of raid
(no world buffs, no debuffs, level-60 target). The Forever parse builds equal the raid builds except where TSA / LotP / IBS
are suppressed, and the raid build is at least as good in every environment (MM parse 688 vs raid build 701).
`render_raidsim_sections.load()` must skip `-environments.json` and `-calibration.json` files.
**How to apply:** treat sim numbers as the community's model, never measurements; name the sim and commit; after
`setup.py --update` re-run `rebuild.py --steps raid,adopt,classic,heal,regen`; re-run `buff_value.py --write` after a
sim update. Related: [[wow-forever-fightlab]], [[wow-forever-project]].

**Training dummy (2026-09-27, user request: "test against a Testing Dummy like in game ... only our buffs and dps matter"):**
Forever DPS specs' main runs (tables, calibration deltas, races, adopt) use a boss-level (63) dummy with execute phases,
own buffs only (bench `"buffs": "self"` + `buffs_on`/`debuffs_on`; specs.json `self_buffs`/`self_debuffs` for self-cast buffs
the sim only has as raid switches: druid Mark of the Wild, Ret Blessing of Might, hunter Hunter's Mark, shaman Mana Spring) and
the spec's standard consumables. Tanks and Classic stay in the raid setting; `run.py --setting` overrides. Forever `raid-dps`
profile has `no_utility: ["forever"]`. Environments report: dummy, dummy60 (in-game style), raid, max, max60. Finding: hunter
and Enhancement run out of mana ~70 s of 120 on the dummy (their mana comes from Blessing of Wisdom / Mana Spring in raids),
Shadow ~20 s, Moonkin ~13 s; physical DPS roughly halves (no armor debuffs, Windfury, Kings). Reports: <class>/raid/raidsim/.

**Presets compete, stuck zeros, mana limit (2026-09-27, user approved "let the simulator's builds compete and teach the
system, un-stick the zeros, count running out of mana as lost damage"):** `run.py --preset-candidates` saves presets within
6% of the spec's best build as `candidates/cand-<spec>-preset-<slug>.json` ("preset" key; ours=False but measured); the
raid step seeds the optimizer with them (`scorer/run.py --seed` takes .json files), races them under "sim preset: X"
(candidate files are skipped when presets are on), `adopt_raid` can adopt one (credits presets.ts); only `cand-<spec>-rN`
are promoted into opt-*. `splitfx.reseed_zero` (all three calibrations): an all-zero fit with a measured target > noise
restarts from the talent's own other-mode values, else parsed (own first: Arcane Concentration's parse reads 100%).
Mana: `run.py` setting `dummy-surplus` (MANA_SURPLUS buffs) → per-build deficit = 1 - DPS/surplus DPS (every mana user
loses 5-30% on the dummy: Frost 6-7% = one Evocation, warlock 13-17% Life Tap, Ret 19%, hunter 10-25%, Balance 4-30%);
spec model `mana_limit` {forever: {profiles [raid-dps, raid-dps-extwc], loss, cap, rms, points}}: mana-bound damage
(sources not white/pet) x (1 - min(cap, max(0, loss - (sus - 1)))), linear mana_weight off there. Lessons from the fits:
a free slope ran away (hunter builds differ in mana demand) -> slope fixed at 1, talent removals set the sustain unit;
old linear-fit values were ~1/mw too big -> converted once (x mw / bound share) when a spec first gets a limit; pure
mana talents' removal runs are extra curve points (Moonglow's removal costs 27%); mixed talents (Shadowform -50% mana
cost) scale only their damage part; mana talents whose builds sit on the flat part are "held"; the damage split comes
from the surplus run; Bestial Discipline's raid effect is pet damage (was parsed as hunter regen).
Results of the 2026-09-27 rebuild with all three (17 min, `rebuild.py --steps raid,adopt --jobs 4`): every Forever DPS spec's
best build of ours now beats or ties the best preset on the dummy (Frost 565 vs 556, was 539 vs 556; Shadow 524 vs 514, was
510 vs 514; cat 336 vs 336 tie); adopted: frost-fingers-of-frost-raid <- opt (+6.5%), enhancement-raid-dps <- opt (+2.8%);
no preset adopted (none >2% ahead of our hand drafts). Fit error of the mana limit: 0.5-1.2 points (Frost, warlocks, Ret,
Enh), 1.5-2.4 (Fire, Lone Wolf, Shadow), 3.5-4.6 (Balance, Elemental, MM). MM (22/29/0) and Ret (17/0/34) dummy winners
lose 6.4% / 2.6% in the raid setting to their previous drafts: user chose "Both" -> restored as `bm-mm-full-buffs-raid` (raid
687 vs 643) and `ret-full-buffs-raid` (748 vs 729), registered in specs.json builds, pointer notes on the main drafts. Open: Penance's untagged healer sustain leaks into Shadow's mana limit (audit "best next point" +24).

2026-09-28 bench bug fixed: the simulator registers potion / conjured cooldowns only from the `potions` / `conjuredItems` lists
its UI sends; our configs set only potId/conjuredId, so no run before 2026-09-28 used a potion, Demonic Rune or Thistle Tea
(foreverbench/main.go now appends them; hunter dummy +8%, warlock +3-4%, Enh +4%, rogue +2-3%). Every raid number, rotation
search, calibration and race from before that is potion-less; the full re-run started 2026-09-28 13:38.
Also 2026-09-28: `raidsim/talent_opt.py` (talent search in the simulator for model-less builds; keeps talents the rotation
conditions on), `raidsim/patches/forever/` (our Frostfire Bolt, applied by setup.py), an unknown aura in an APL condition
makes the condition vanish (guard with auraIsKnown), new-builds survey (`_reference/data/new-builds.json`,
`render_new_builds.py`). See [[wow-forever-rotations]].
