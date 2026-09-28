# Paladin — adapting the Classic builds to WoW: Forever

Data: WoW: Forever beta client build 1.60.1.70009, merged 2026-09-25 (`talent-trees.md`; the 2026-09-13 demo snapshot is archived under `_reference/data/raw/`). Spellbook numbers: `../../spells/README.md`. Point-by-point audit of every
Classic build: `baseline-audit.md`. Proposed builds: `proposed-builds.json` → `builds-README.md`.

Paladin has 21 new talents and 13 removals; more importantly the *reasons* behind Classic splits changed:
Blessing of Kings and Consecration are baseline, blessings last an hour, and Holy Strike / Seal of Fury are new
baseline abilities the trees are built around. Undead paladins exist.

## What broke

| Classic talent | Forever | Impact on baselines |
|---|---|---|
| Blessing of Kings (Prot T3), Blessing of Sanctuary (Prot T5) | **Removed** — Kings baseline | The 11-point Protection dip of the Classic healer is pointless |
| Improved Blessing of Might, Improved Blessing of Wisdom | **Removed** | The 9-point Retribution dip and Holy's Improved Wisdom are gone |
| Consecration (Holy T3) | **Removed** — baseline | Ret/Prot no longer dip Holy for it |
| Improved Seal of Righteousness, Improved Lay on Hands, Lasting Judgement | **Removed** | Holy fillers replaced by Improved Seals, Reverence, Voice of Truth, Purifying Power |
| Improved Seal of the Crusader, Sanctity Aura, Improved Retribution Aura | **Removed** | Ret loses its raid-debuff/aura role; Improved Seals (+15% seals/judgements) and Crusade replace the damage |
| Improved Devotion Aura, Improved Concentration Aura | **Removed** | Nothing core lost |
| Holy Shock | Tier 7 → **tier 5** (1 point); Light's Vigil is the new capstone and requires it | Deep Holy is now about Light's Vigil |
| Illumination | Requires **Reverence 3** (new regen talent) | 3 extra points on the way |
| Holy Shield | Requires **Templar's Bulwark** (new 100%-health absorb) | Tank capstone chain |
| Vengeance | +15% after crit → stacking +1%/rank per non-periodic crit (3 stacks since build 70009); requires Sanctified Judgement 3 | Weaker than the demo's 5 stacks |
| Reckoning | 5 ranks reworked (8% on block / 20% on crit per rank read) | |
| Precision | Now hit with **all spells and attacks** (1%/rank) | Ret takes a Protection dip for it |

## What's new and matters

- **Light's Vigil** (Holy capstone): cooldown-free Holy Shock with a party heal. **Infusion of Light**, **Reverence**, **Divine Precision**, **Voice of Truth**.
- **Templar's Bulwark**, **Sacred Duty**, **Iron Creed**, **Swift Judgement**, **Improved Seal of Fury** — a real tank tree.
- **Twist of Light** (Ret capstone, seal twisting, -20% Seal mana), **Sacred Arbiter** (16-pt, +20% Holy Strike), **Champion of the Light**, **Sanctified Judgement**, **Holy Conduit**, **Instrument of Law**; Crusade and Improved Holy Strike were cut in build 70009.
- **Improved Seals** (Holy T2) — the Improved Seal of the Crusader replacement, and better.

## Decisions made in the proposed builds

1. **Holy healer 31/0/20**: the Protection dip is replaced by a Retribution dip for Benediction / Improved Judgement / Sanctified Judgement.
2. **Ret DPS 10/8/33**: Improved Seals + Divine Strength from Holy, Precision from Protection, everything else in Retribution including Champion of the Light and Twist of Light.
3. **Prot tank 13/38/0**: the new Templar's Bulwark → Holy Shield chain with Iron Creed, Sacred Duty, Improved Righteous Fury (Improved Holy Strike's 2 Holy points moved to Divine Strength).
4. **Shockadin 31/0/20**: same Holy core as the healer with Conviction/Seal of Command from Retribution.

## To verify at launch

- Holy Strike (baseline from 6, 8 ranks, 10s cooldown) and Seal of Fury (7 ranks from 10, absorb with a shield): threat values in play.
- Judgement of Fury taunts within 10 yards (dev notes); confirm it holds raid bosses.
- Twist of Light Echo mechanics with Seal of Command.
- Champion of the Light for healers (21/0/30 variant) vs. deep Holy.
