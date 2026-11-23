"""The pool's item sets the simulator gives no bonus (2026-11-23, the audit session's finding on 3a: "the sets with no simulated bonus are the
bigger gap than the procs"; the user: "fix looking at sets for their bonuses"). For each list's pool, every item set some class can wear
whose id gear_tiers.sim_set_steps does not know, with each bonus step from the client's own tables (ItemSet, ItemSetSpell, Spell's
description, SpellEffect's auras; build 1.60.1.71037, the CSVs in ~/.wow-forever-tools/wago/, outside the repository) and whether the
bonus is plain stats (an aura on a stat, attack or spell power, healing, hit, crit, armor or resistance, health, mp5, avoidance, a rating)
or an effect (a proc, a spell modifier, a script). Read only; the counts decide the second pass (a plain-stat bonus is cheap to model).

    python _reference/data/raidsim/set_bonus_inventory.py [--write]   # raidsim/set-bonus-inventory.json
"""
import argparse
import csv
import datetime
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent)]
import gear_tiers as GT  # noqa: E402

G, R = GT.G, GT.R
WAGO = pathlib.Path.home() / ".wow-forever-tools" / "wago"
BUILD = "1.60.1.71037"
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
APPLY_AURA = {6, 35, 65}   # apply aura, area aura (party), area aura (raid)
PLAIN = {13: "spell damage", 22: "armor or resistance", 29: "a stat", 30: "a skill", 34: "health", 47: "parry", 49: "dodge", 51: "block",
         52: "crit", 54: "hit", 55: "spell hit", 57: "spell crit", 85: "mp5 or regeneration", 99: "attack power", 123: "spell penetration",
         124: "ranged attack power", 135: "healing", 189: "a rating", 158: "block value", 142: "base resistance or armor %",
         137: "a stat %", 71: "spell crit (school)", 290: "crit (all)"}


def table(name):
    return list(csv.DictReader(open(WAGO / f"{name}-{BUILD}.csv", encoding="utf-8", newline="")))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    steps = GT.sim_set_steps(repo)
    names = {int(r["ID"]): r["Name_lang"] for r in table("ItemSet")}
    bonus = {}
    for r in table("ItemSetSpell"):
        bonus.setdefault(int(r["ItemSetID"]), []).append((int(r["Threshold"]), int(r["SpellID"])))
    desc = {int(r["ID"]): r["Description_lang"] for r in table("Spell")}
    effects, points = {}, {}
    for r in table("SpellEffect"):
        effects.setdefault(int(r["SpellID"]), []).append((int(r["Effect"]), int(r["EffectAura"])))
        try:
            points.setdefault(int(r["SpellID"]), {})[int(r["EffectIndex"])] = float(r["EffectBasePointsF"])
        except (KeyError, ValueError):
            pass

    def text_of(sid):
        """The description with $s1.. filled from the effects' base points (the client's own numbers)."""
        import re
        bp = points.get(sid) or {}

        def num(m):
            v = bp.get(int(m.group(1)) - 1)
            return m.group(0) if v is None else (f"{abs(v):g}")
        return re.sub(r"\$s(\d)", num, desc.get(sid) or "")

    def kind(sid):
        es = effects.get(sid) or []
        if not es:
            return "effect", "no effect rows"
        if all(e in APPLY_AURA and au in PLAIN for e, au in es):
            return "plain", ", ".join(sorted({PLAIN[au] for _, au in es}))
        return "effect", ", ".join(sorted({f"effect {e} aura {au}" for e, au in es if not (e in APPLY_AURA and au in PLAIN)}))[:120]
    out = {"date": datetime.date.today().isoformat(), "commit": R.git_commit(repo), "client": BUILD, "lists": {}}
    for lst in ("dungeon", "prebis", "bis"):
        pool = GT.pool_of(lst, zones, repo)
        sets = {}
        for cls in CLASSES:
            _, _, greedy = G.class_picker(repo, cls, db, pool)
            for it in db.values():
                sid = it.get("setId")
                if not sid or not pool(it):
                    continue
                if any(G.SLOT_TYPE[s] == it.get("type") and greedy.fits(it, s, it) for s in range(17)):
                    sets.setdefault(sid, {"pieces": set(), "classes": set()})
                    sets[sid]["pieces"].add(it["id"])
                    sets[sid]["classes"].add(cls)
        rows = []
        for sid, v in sorted(sets.items(), key=lambda kv: names.get(kv[0], "")):
            bs = []
            simulated = set((steps.get(sid) or {}).get("steps") or [])   # step by step (2026-11-23: the generated sets' path)
            for th, sp in sorted(bonus.get(sid) or []):
                if th in simulated:
                    continue
                k, what = kind(sp)
                bs.append({"pieces": th, "spell": sp, "kind": k, "what": what, "text": text_of(sp)[:200]})
            rows.append({"set": names.get(sid, str(sid)), "id": sid, "pieces_in_pool": len(v["pieces"]), "classes": sorted(v["classes"]),
                         "bonuses": bs, "plain": sum(1 for b in bs if b["kind"] == "plain"), "effect": sum(1 for b in bs if b["kind"] == "effect")})
        rows = [r for r in rows if r["bonuses"]]   # a set whose every step the simulator applies is not listed
        reach = [r for r in rows if r["pieces_in_pool"] >= min(b["pieces"] for b in r["bonuses"])]
        out["lists"][lst] = {"sets": rows, "count": len(rows), "reachable": len(reach),
                             "plain_steps": sum(r["plain"] for r in reach), "effect_steps": sum(r["effect"] for r in reach)}
        print(f"{GT.GL.LABEL[lst]}: {len(rows)} sets with an unsimulated step, {len(reach)} with such a step the pool's pieces reach "
              f"({out['lists'][lst]['plain_steps']} plain-stat steps, {out['lists'][lst]['effect_steps']} effect steps)")
        for r in reach[:200]:
            print(f"   {r['set']} ({r['pieces_in_pool']} pieces in the pool; {', '.join(r['classes'])}): "
                  + "; ".join(f"{b['pieces']} pc {b['kind']} ({b['what']}): {b['text'][:90]}" for b in r["bonuses"]))
    if a.write:
        (HERE / "set-bonus-inventory.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("wrote raidsim/set-bonus-inventory.json")


if __name__ == "__main__":
    main()
