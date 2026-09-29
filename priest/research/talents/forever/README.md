# Priest — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Divine Spirit (Discipline T5) | **Removed** — trained from 30 in the beta (ranks 30/40/50/60, Prayer of Spirit at 60) | The reason every Classic healer put 21 points in Discipline is gone |
| Unbreakable Will, Improved Power Word: Fortitude, Force of Will | **Removed** | Discipline tier 1–2 fillers replaced by Twin Disciplines / Power in Light / Holy Precision |
| Healing Focus (Holy T1) | **Removed** → *Twilight Focus* (3, 23%/rank pushback resistance) | Same job, one more point for full effect |
| Improved Prayer of Healing, Lightwell | **Removed** | Nothing core lost |
| Spiritual Healing | 5 ranks (10%) → **3 ranks (3/7/10%)** | Cheaper, same total |
| Spiritual Guidance | 25% of Spirit → 5/10/15/20/25%, plus 1/3/5/6/8% of Spirit as spell damage | Same |
| Meditation | 5%/rank → **17/33/50%** | Much stronger |
| Inspiration | 25% armor → 8/17/25% | Same |
| Improved Healing | Now also covers Penance and Prayer of Mending | |
| Power Infusion | Requires **Penance** | Power Infusion builds are Penance builds |
| Shadow Weaving | Raid debuff → **self-buff** (33%/rank chance, +2% per stack, 5 stacks) | No debuff slot needed — Shadow raid DPS becomes plausible |
| Improved Psychic Scream | Requires Blackout 5 | Shadow PvP takes Blackout 5/5 |
| Improved Vampiric Embrace | **Removed** | |

## What's new and matters

- **Prayer of Mending** (Holy capstone), **Binding Heal** (Holy 16-pt), **Litany of Light** — raid-healing throughput and mana.
- **Penance** (Disc T5), **Divine Aegis** (T6), **Renewed Hope** (T5), **Soul Warding** (Disc 16-pt) — a shield/crit Discipline healer.
- **Twin Disciplines** (instants +5% est.) — the new tier-1 Discipline pick.
- **Improved Mind Flay**, **Devouring Contagion**, **Early Demise** (Shadow Word: Death is trained at 32/40/48/56) — Shadow gets a kit.
- **Holy Precision** (hit with Holy spells) — only matters if Forever lets heals miss (Classic: no) or for Smite/Holy Fire.

## Decisions made in the proposed builds

1. **Holy 20/31/0**: with Divine Spirit gone, Discipline stops at 20 (Soul Warding) and Holy takes the capstone.
2. **Discipline Penance 31/20/0** replaces the Classic Power Infusion build.
3. **Shadow 7/0/44** for PvP; the same build with Shadow Affinity is the candidate raid Shadow spec.

## To verify at launch

- Divine Spirit is trained (confirmed in the beta spellbook).
- Prayer of Mending / Penance / Binding Heal numbers at 60.
- Whether Shadowform's mana reduction plus self-buff Shadow Weaving makes a raid Shadow priest worth a slot.
