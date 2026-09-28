# Healer lab — a Monte Carlo model of one raid healer

The community simulators cover raid DPS and the fight lab covers leveling; healers had nothing behind their models. The
healer lab is a small Monte Carlo model of **one raid healer keeping a five-member group alive for a five-minute boss
fight**: a tank taking boss melee (swings with crushing blows, a periodic spike) and four raid members taking periodic raid
damage. The healer casts from the beta spellbook (`forever-spells/<class>.json`: ranks, costs, cast times, coefficients),
downranks to the deficit, keeps HoTs up, uses group heals when the group is hurt and cooldowns in emergencies; mana follows
spirit regen, the five-second rule, mp5 and potions. Talent numbers come from the beta tooltips
(`scorer/effects/forever/<class>.parsed.json`: healing, mana cost, crit, cast time, regen, stats) plus the mechanics each
class module hand-codes (Illumination, Divine Favor, Inner Focus, Inspiration, Nature's Swiftness, Swiftmend, Mana Tide,
Healing Stream Totem, Prayer of Mending, Penance, Water Shield ...).

```
python _reference/data/heallab/run.py priest --build holy-raid-healer --compare opt-holy-heal-raid-heal --deltas --write
python _reference/data/heallab/calibrate.py druid --write          # shares + heal-mode fits into the scorer
python _reference/data/rebuild.py --steps heal,regen               # calibrate <-> optimize <-> race for the four healers
python _reference/data/heallab/run.py shaman --build resto-raid-healer --set POTIONS=False --set TANK_HP=8000   # sensitivity
```

| File | What it is |
|---|---|
| `tables.py` | Every assumption with a knob: the group, the boss, the raid damage, the healer's phase-1 raid stats per class, buffs, potions, downranking, the emergency and raid-heal thresholds |
| `engine.py` | Spell parsing, the generic talent layer, targets, the encounter, the healer loop, `capacity()` |
| `priest.py`, `paladin.py`, `shaman.py`, `druid.py` | One module per healer: spell roles, talent-taught spells, hand-coded mechanics (`MECHANICS`), which talents the lab measures (`SIMULATED`), spell → scorer source map, `PIPELINE` |
| `run.py` | Capacity, healing split and talent removal values of builds; `<class>/raid/heallab/<spec>.md` + `.json` |
| `calibrate.py` | The lab's healing split into the healer model's shares, the removal values fitted into the heal-mode effects (`modes: ["heal"]`, `specs: [<model>]`) of the simulated talents only |
| `rebuild.py --steps heal[,adopt]` | Calibrate ↔ optimize (the export seeded with the hand draft) ↔ race, promotion of the best round, opt-in adoption over 2% |
| `render_heallab_sections.py` | Class README "Healer lab" sections + `_reference/heallab-summary.md` |

## What the numbers mean

**Capacity** is the multiplier on all incoming damage at which the build keeps the group alive in 90% of runs (per-run
capacities by bisection with common random numbers; the reported value is the mean of the worst fifth). It combines
throughput and mana the way a boss fight does: a healer who runs dry at four minutes fails. A talent's value is the capacity
lost when it is removed, on the same scale as the scorer's raid-heal score, which is what `calibrate.py` fits.

Comparable across classes only under the lab's shared assumptions (same group, boss and gear level); the absolute level of
the encounter is arbitrary, the mix of tank spikes and raid pulses is what makes talents differ. Not simulated: pushback,
threat, dispels, movement, other healers, raid-wide damage beyond the group, Lightwell, Spirit of Redemption, Binding Heal's
self-heal. Talents without mechanics keep their manual values (they are marked * in the reports and never fitted).

## Tuned heal choice (2026-09-27)

`rotation_opt.py <class> --write` (or `--all`) searches the heal-choice settings of `tables.py` (DOWNRANK, HOT_REFRESH_DEFICIT,
EMERGENCY, RAID_HEAL_AT, GROUP_HEAL_MIN, POTION_BELOW, POTION_FIRST) for the class pipeline's hand-draft healer on capacity, common
random numbers, confirmed on other seeds. `rotations/<class>-<spec>.json` holds the settings that differ from the defaults;
`tables.apply_rotation` applies them at the start of `run.py` and `calibrate.py` (`WOW_HL_ROTATION=default` keeps the defaults,
`--set` still overrides).

