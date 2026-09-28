# Warlock — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

Warlock has the most new talents of any class (22) and 20 removals; every Classic build loses 5–13 points to
removed talents. The Classic *shapes* (7/21/23, 30/0/21) no longer mean anything — the builds below are rebuilt
from the demo tree around the same goals.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Fel Intellect, Fel Stamina, Improved Healthstone, Improved Firestone/Spellstone, Improved Subjugate Demon | **Removed** | 12 of DS/Ruin's 21 Demonology points were these fillers; Demonology tier 2 is now Demonic Aegis / Improved Voidwalker / Fel Vitality / Demonic Energies |
| Demonic Sacrifice | Moved tier 5 → **tier 3** (11 points), effect lasts 2 hours | DS costs half as much |
| Ruin | 1-point tier 5 → **5-rank tier 3** (20% crit damage per rank) | Same effect, 4 more points, but only 10 Destruction points to reach it |
| Devastation, Improved Immolate, Emberstorm, Improved Searing Pain, Improved Firebolt, Improved Lash of Pain | **Removed** | Destruction fillers replaced by Molten Skin, Agonizing Flames, Fire and Brimstone, Shadow and Flame |
| Grim Reach, Dark Pact, Improved Curse of Agony/Weakness/Exhaustion, Improved Drain Life/Soul/Mana | **Removed** | Affliction fillers gone; SM/Ruin's 30 Affliction points must be rebuilt (Malediction, Pandemic, Malevolence, Improved Bane of Agony) |
| Suppression | Affliction hit → **hit with all spells** (1%/rank) + threat reduction (4%/rank) | Now mandatory for every build |
| Improved Life Tap | Moved to Affliction tier 1 | Cheaper |
| Soul Link | Tier 7 → **tier 5**, requires Demonic Sacrifice | Soul Link builds gain 10 points |
| Shadow Mastery | 1%/rank (5% at 5/5; Classic 2%/rank), confirmed by the beta client | Half its Classic value |
| Unholy Power | Moved to Demonology tier 1 | Pet-damage builds start it at level 10 |

## What's new and matters

- **Demonic Pact** (Demonology capstone): keep a different pet while a Demonic Sacrifice buff is active — DS + Imp Blood Pact in one build (needs 31 Demonology; not drafted, worth testing).
- **Wrack** (Affliction capstone: a 6s Shadow channel that buffs your other Shadow DoTs by 10%; replaced Drain Hope in beta build 69893), **Pandemic**, **Malediction**, **Malevolence** — a DoT spec with critting DoTs.
- **Incinerate** (Destruction capstone), **Conflagrate** (16-pt), **Fire and Brimstone**, **Shadow and Flame**, **Agonizing Flames**, **Bane of Havoc** — a fire spec and stronger Shadow Bolt spec.
- **Fel Vitality** (+15% own mana est.) — the Fel Intellect replacement.
- **Demonic Knowledge** (spell damage while a pet is out) and **Decimation** (Soul Fire execute) — pet-keeping DPS options.
- Curses partly renamed **Bane of Agony / Bane of Doom / Bane of Havoc**.

## Decisions made in the proposed builds

1. **DS/Ruin 7/11/33**: cheaper DS and Ruin fund Agonizing Flames, Shadow and Flame and Bane of Havoc.
2. **Affliction DoT 31/0/20** replaces SM/Ruin as the pet-keeping shadow build.
3. **Destruction fire 5/11/35**: a brand-new fire build for when it is tested.
4. **PvP Soul Link 30/21/0**: Soul Link + Shadow Mastery + Siphon Life in one build.

## To verify at launch

- Demonic Sacrifice pairs the Imp with +15% Shadow and the Succubus with +15% Fire in the beta (the reverse of Classic); Ruin 20%/rank confirmed.
- Raid debuff cap (decides Affliction's viability).
- Conflagrate consumes Immolate (tooltip confirmed); Incinerate ranks at 40/50/60.
- Demonic Pact: which pet buffs stack with which sacrifice.
