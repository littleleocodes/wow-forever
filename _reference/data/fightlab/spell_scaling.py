"""Rank damage and healing by character level for the fight lab (audit of 2026-10-18, row 8).

    python _reference/data/fightlab/spell_scaling.py [--store <spells_auto_gen.go>] --write

The client grows a rank's amount with the caster's level, from the spell's own level up to the level its scaling stops at (SpellLevels;
EffectRealPointsPerLevel): amount(L) = floor(base + (min(L, max level) - spell level) x per-level gain). Shadow Bolt rank 4 (1088): base
58, gain 0.8 a level from 20 to 25, so 58 at 20 and 62 from 25 on. Our tooltips are the level-60 text (forever-spells `tooltip_level`),
so the fight lab read every rank's level-60 amount at every level: casters read high where the rank in use is below its cap (median
+4.4% over the effects that scale). This reads, from the raid simulator's spell store (the old fork's export of the client's
SpellEffect and SpellLevels, `sim/core/spelldata/spells_auto_gen.go`; the rule is its `effect.go` Effect.Average), every damage, heal
and absorb effect of each rank in our spellbooks, for the ranks where at least one of them gains per level, sorted into
  direct   (school damage, heal, health leech)          -> the lab's dmg_min/dmg_max, heal_min/heal_max
  periodic (periodic damage/heal/leech auras, persistent area auras, and the effects of a periodically triggered spell: Arcane
            Missiles' missiles, Hurricane's waves)        -> dot, hot, burn
  absorb   (school absorb auras: Power Word: Shield ...) -> absorb
as [base, gain, spell level, max level] rows; `tables.rank_level_factor` turns them into the factor at a level (the amount at L over
the amount at 60) and `engine.scale_rank` applies it in each module's rank_at. Effects of a kind with no gain stay in the rows (Immolate's
periodic part: factor 1). Written per class, name and learn level (our Spell objects carry no id).
"""
import argparse
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
SPELLS = HERE.parent / "forever-spells"
OUT = HERE / "spell_scaling.json"
STORE = pathlib.Path.home() / ".wow-forever-tools/forever-repo/sim/core/spelldata/spells_auto_gen.go"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
DIRECT = {"E_SCHOOL_DAMAGE", "E_HEAL", "E_HEALTH_LEECH"}
PERIODIC_AURA = {"A_PERIODIC_DAMAGE", "A_PERIODIC_HEAL", "A_PERIODIC_LEECH", "A_PERIODIC_DAMAGE_PERCENT"}
TRIGGERS = {"A_PERIODIC_TRIGGER_SPELL"}


def field(line, k, default=None):
    m = re.search(rf"\b{k}: ([^,}}]+)", line)
    return m.group(1).strip() if m else default


def load_store(path):
    """{spell id: [effect dicts]} and {spell id: (name, rank)}."""
    effects, names = {}, {}
    for line in open(path, encoding="utf-8"):
        m = re.search(r'\{ID: (\d+), Name: "([^"]*)"', line)
        if m:
            names[int(m.group(1))] = m.group(2)
            continue
        if "SpellID:" in line and "Type:" in line:
            effects.setdefault(int(field(line, "SpellID")), []).append({
                "type": field(line, "Type").split(".")[-1], "aura": (field(line, "Aura") or "").split(".")[-1],
                "base": float(field(line, "BasePoints", 0)), "ppl": float(field(line, "PPL", 0)),
                "sl": int(field(line, "SpellLevel", 0)), "ml": int(field(line, "MaxLevel", 0)), "trig": int(field(line, "TriggerID", 0))})
    return effects, names


def kinds(sid, effects, depth=0):
    """{kind: [[base, gain, spell level, max level], ...]} for one spell id."""
    out = {"direct": [], "periodic": [], "absorb": []}
    for e in effects.get(sid, []):
        row = [e["base"], round(e["ppl"], 6), e["sl"], e["ml"]]
        if e["type"] in DIRECT:
            out["direct"].append(row)
        elif e["aura"] in PERIODIC_AURA or e["type"] == "E_PERSISTENT_AREA_AURA":
            out["periodic"].append(row)
        elif e["aura"] == "A_SCHOOL_ABSORB":
            out["absorb"].append(row)
        elif e["aura"] in TRIGGERS and e["trig"] and depth == 0:
            sub = kinds(e["trig"], effects, 1)
            out["periodic"] += sub["direct"] + sub["periodic"]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default=str(STORE))
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    effects, _ = load_store(a.store)
    out = {"source": f"EffectBasePoints, EffectRealPointsPerLevel and SpellLevels of the raid simulator's spell store "
                     f"({a.store.replace(str(pathlib.Path.home()), '~')}; rule: effect.go Effect.Average), by our spellbooks' rank ids; "
                     "written by spell_scaling.py (audit of 2026-10-18 row 8)",
           "spellbook_build": json.load(open(SPELLS / "mage.json", encoding="utf-8")).get("build"), "classes": {}}
    n_rank = n_eff = 0
    for cls in CLASSES:
        d = json.load(open(SPELLS / f"{cls}.json", encoding="utf-8"))
        rows = {}
        for tab in d["tabs"]:
            for sp in tab["spells"]:
                for r in sp["ranks"]:
                    sid = r.get("id")
                    if not sid:
                        continue
                    k = kinds(sid, effects)
                    k = {kind: v for kind, v in k.items() if v}
                    if not any(row[1] for v in k.values() for row in v):
                        continue
                    rows.setdefault(sp["name"], {})[str(int(r.get("level") or 1))] = dict(k, id=sid)
                    n_rank += 1
                    n_eff += sum(1 for v in k.values() for row in v if row[1])
        out["classes"][cls] = rows
    print(f"{n_rank} ranks with {n_eff} scaling damage/heal/absorb effects")
    if a.write:
        OUT.write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
