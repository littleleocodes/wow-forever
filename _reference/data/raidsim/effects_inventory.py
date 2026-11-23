"""The gear lists' effects inventory (2026-11-23, the user: "let's try and figure out a way to correctly test things like trinkets or rings
or weapons or even armor and gear that has proc chances"; the audit session's item 3a). For each list's pool and each class, every item
with an effect, on the pinned simulator:
  * modelled: the simulator plays its effect (an item effect the generator or a hand implementation registers), so a race measures it;
  * skipped: upstream's generator leaves it for manual implementation ("TODO: Manual implementation required" in
    sim/common/forever/*_auto_gen.go): the race sees the item's stats only. "matters" when its effect moves damage, healing or a combat
    stat (the audit's rule: damage, attack or spell power, healing, haste, crit, the attributes, mana, hit, armor and avoidance, absorbs,
    health, rage, energy, attack or casting speed), not when it is utility (speed, breath, fear, stun, threat, tracking ...);
  * the pool's item sets the simulator gives no bonus, by name (gear_tiers.sim_set_steps).
Each item counts once per class, at the first slot it fits (rings and trinkets have two slots, weapons two hands: the over-count rule of
the counts of 2026-11-23, kept here). Classic's proc rates for skipped items (the Classic simulator's code, the cmangos database) come from
the audit session's research file when it is on this machine (~/.wow-forever-tools/gear-research-1122/proc_rates_local.json).
Scope groups: trinket, weapon, ranged/relic, ring, neck, back (3b's measurement pass races these now) and armor (later).

    python _reference/data/raidsim/effects_inventory.py [--write]   # raidsim/effects-inventory.json, _reference/effects-inventory.md
"""
import argparse
import collections
import datetime
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path[:0] = [str(HERE), str(HERE.parent)]
import gear_tiers as GT  # noqa: E402

G, R = GT.G, GT.R
CLASSES = ["druid", "hunter", "mage", "paladin", "priest", "rogue", "shaman", "warlock", "warrior"]
LISTS = ("dungeon", "prebis", "bis")
SCOPE = ("trinket", "weapon", "ranged/relic", "ring", "neck", "back")
RATES = pathlib.Path.home() / ".wow-forever-tools" / "gear-research-1122" / "proc_rates_local.json"
UTILITY = ("duration of your", "speed of your", "underwater", "breath", "interruption", "run speed", "movement speed", "mount", "fishing",
           "stealth detection", "resurrect", "fear", "silence", "disorient", "knock", "charm", "stun", "threat", "reduce your threat",
           "fall", "swim", "water walking", "tracking", "pickpocket")
# out by rule as utility too (2026-11-23, the audit session's read of 3a): the PvP gloves' interruption lines, Mana Shield's absorb,
# Cleanse and Purify costs, effects tied to a place (Royal Seal's caverns, Arena Grand Master's rings), the Imp's mana, a pet's armor
UTILITY_ALWAYS = ("avoid interruption", "mana shield", "purify and cleanse", "cleanse and purify", "cavernous or underground", "battle ring",
                  "to your imp", "your pet's armor", "from falling", "from falls")
MATTERS = ("damage", "attack power", "spell power", "healing", "haste", "critical", "strength", "agility", "intellect", "stamina",
           "spirit", "mana", "hit", "armor", "dodge", "parry", "block", "absorb", "health", "rage", "energy", "attack speed", "casting speed")


def matters(text):
    t = (text or "").lower()
    if not t or any(u in t for u in UTILITY_ALWAYS):
        return False
    if any(u in t for u in UTILITY) and not any(k in t for k in ("damage", "attack power", "healing", "haste", "critical")):
        return False
    return any(k in t for k in MATTERS)


_CLIENT = {}


def client_rate(item_id, build="1.60.1.71037"):
    """The item's proc rate from Forever's client tables (ItemXItemEffect -> ItemEffect -> SpellAuraOptions, SpellProcsPerMinute;
    ~/.wow-forever-tools/wago/<table>-<build>.csv, outside the repository): "<trigger> <spell>: ppm X" / "chance Y%", or None."""
    import csv
    w = pathlib.Path.home() / ".wow-forever-tools" / "wago"
    if not _CLIENT:
        try:
            rd = lambda n: list(csv.DictReader(open(w / f"{n}-{build}.csv", encoding="utf-8", newline="")))   # noqa: E731
            _CLIENT["x"] = {}
            for r in rd("ItemXItemEffect"):
                _CLIENT["x"].setdefault(int(r["ItemID"]), []).append(int(r["ItemEffectID"]))
            _CLIENT["e"] = {int(r["ID"]): r for r in rd("ItemEffect")}
            _CLIENT["a"] = {}
            for r in rd("SpellAuraOptions"):
                _CLIENT["a"].setdefault(int(r["SpellID"]), r)
            _CLIENT["p"] = {int(r["ID"]): float(r["BaseProcRate"]) for r in rd("SpellProcsPerMinute")}
        except OSError:
            _CLIENT["missing"] = True
    if _CLIENT.get("missing"):
        return None
    out = []
    for eid in _CLIENT["x"].get(item_id, []):
        e = _CLIENT["e"].get(eid)
        if not e:
            continue
        sid, trig = int(e["SpellID"]), {"0": "use", "1": "equip", "2": "chance on hit"}.get(e["TriggerType"], e["TriggerType"])
        ao = _CLIENT["a"].get(sid)
        if ao:
            ppm = _CLIENT["p"].get(int(ao["SpellProcsPerMinuteID"] or 0))
            if ppm:
                out.append(f"{trig} {sid}: ppm {ppm:g}")
            elif ao["ProcChance"] not in ("0", "101", ""):
                out.append(f"{trig} {sid}: chance {ao['ProcChance']}%")
    return "; ".join(out) or None


def skipped_effects(repo):
    """{item id: {"name", "text", "why", "spell", "file"}}: the effects upstream's generator leaves for manual implementation."""
    out = {}
    for fn in ("stat_bonus_procs_auto_gen.go", "stat_bonus_cds_auto_gen.go", "enchants_auto_gen.go"):
        p = pathlib.Path(repo) / "sim" / "common" / "forever" / fn
        if not p.exists():
            continue
        for chunk in p.read_text(encoding="utf-8", errors="replace").split("// TODO: Manual implementation required")[1:]:
            body = chunk.split("\n\n")[0]
            lines = [ln.strip().lstrip("/").strip() for ln in body.splitlines()]
            lines = [ln for ln in lines if ln and not ln.startswith("This can be ignored") and not ln.startswith("With next db run")]
            desc = []
            for ln in lines:
                if ln.startswith(("https://", "unsupported:", "trigger ", "shared.")):
                    break
                desc.append(ln)
            why = next((ln[len("unsupported:"):].strip() for ln in lines if ln.startswith("unsupported:")), "")
            m = re.search(r"spell=(\d+)", next((ln for ln in lines if ln.startswith("https://")), ""))
            for iid, name in re.findall(r"ItemID:\s*(\d+),\s*ItemName:\s*\"([^\"]*)\"", body):
                out[int(iid)] = {"name": name, "text": " ".join(desc), "why": why, "spell": int(m.group(1)) if m else None, "file": fn}
    return out


def effect_kind(it):
    """"proc" or "use" when the item's effect fires in a fight (a chance on hit, an on-use): what a stat weight cannot see and 3b's
    measurement pass races; "other" for an aura the item gives (equip effects the database lists as a buff)."""
    ks = set()
    for e in it.get("itemEffects") or []:
        ks |= {"proc"} if "proc" in e else {"use"} if "onUse" in e else set()
    return "proc" if "proc" in ks else "use" if "use" in ks else "other"


def group_of(slot):
    return ("trinket" if slot in (12, 13) else "weapon" if slot in (14, 15) else "ranged/relic" if slot == 16 else "ring" if slot in (10, 11)
            else "neck" if slot == 1 else "back" if slot == 3 else "armor")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=None))
    db, zones = GT.load_db(repo)
    commit = R.git_commit(repo)
    skipped = skipped_effects(repo)
    rates = {x["item"]: x for x in json.load(open(RATES, encoding="utf-8"))} if RATES.exists() else {}
    steps = GT.sim_set_steps(repo)
    out = {"date": datetime.date.today().isoformat(), "commit": commit, "skipped_total": len(skipped), "lists": {}}
    md = [f"# Gear effects inventory ({out['date']}, simulator {commit})", "",
          "> Generated by `_reference/data/raidsim/effects_inventory.py`. Per list and class: the items with an effect in the list's pool, "
          "each counted once at its first slot; modelled = the simulator plays the effect, skipped = upstream leaves it for manual "
          "implementation (the race sees its stats only), and of those the ones whose effect matters for damage, healing or a combat stat. "
          "Sets: the pool's item sets with no simulated bonus. Do not hand-edit.", ""]
    for lst in LISTS:
        pool = GT.pool_of(lst, zones, repo)
        lrec = {"classes": {}, "sets_without_bonus": []}
        sets_seen = {}
        md += [f"## {GT.GL.LABEL[lst]}", "", "| Class | Modelled, in scope | of them a proc or on-use (raced) | Modelled, armor | Skipped that matter | Skipped, utility |",
               "|---|---|---|---|---|---|"]
        for cls in CLASSES:
            _, _, greedy = G.class_picker(repo, cls, db, pool)
            rows = {"modelled": [], "skipped_matters": [], "skipped_utility": []}
            for it in db.values():
                if not pool(it):
                    continue
                for slot in range(17):
                    if G.SLOT_TYPE[slot] == it.get("type") and greedy.fits(it, slot, it):
                        g = group_of(slot)
                        if it["id"] in skipped:
                            s = skipped[it["id"]]
                            row = {"id": it["id"], "name": it.get("name"), "group": g, "text": s["text"][:200], "why": s["why"][:120]}
                            cr = client_rate(it["id"])
                            if cr:
                                row["client"] = cr
                            rt = rates.get(it["id"])
                            if rt and (rt.get("classic_db") or rt.get("classic_sim")):
                                row["classic"] = [f"{x.get('trigger')} {x.get('spell')} ppm {x.get('ppm')} chance {x.get('procChance')}"
                                                  for x in (rt.get("classic_db") or [])][:3] or ["the Classic simulator implements it"]
                            rows["skipped_matters" if matters(s["text"]) else "skipped_utility"].append(row)
                        elif it.get("itemEffects"):
                            rows["modelled"].append({"id": it["id"], "name": it.get("name"), "group": g, "kind": effect_kind(it)})
                        sid = it.get("setId")
                        if sid and not (steps.get(sid) or {}).get("steps"):   # no simulated step at all (both parser paths)
                            sets_seen.setdefault(it.get("setName") or str(sid), set()).add(cls)
                        break
            cnt = lambda xs, f: collections.Counter(x["group"] for x in xs if f(x["group"]))   # noqa: E731
            fires = [x for x in rows["modelled"] if x["kind"] != "other"]
            lrec["classes"][cls] = {"modelled_scope": dict(cnt(rows["modelled"], lambda g: g in SCOPE)),
                                    "fires_scope": dict(cnt(fires, lambda g: g in SCOPE)),
                                    "fires_scope_items": [x["id"] for x in fires if x["group"] in SCOPE],
                                    "modelled_armor": len([x for x in rows["modelled"] if x["group"] == "armor"]),
                                    "skipped_matters": rows["skipped_matters"], "skipped_utility": len(rows["skipped_utility"]),
                                    "modelled": [x["id"] for x in rows["modelled"]]}
            md.append(f"| {cls} | {sum(lrec['classes'][cls]['modelled_scope'].values())} | {sum(lrec['classes'][cls]['fires_scope'].values())} | "
                      f"{lrec['classes'][cls]['modelled_armor']} | "
                      f"{len(rows['skipped_matters'])} | {len(rows['skipped_utility'])} |")
        lrec["sets_without_bonus"] = [{"set": k, "classes": sorted(v)} for k, v in sorted(sets_seen.items())]
        md += ["", "Item sets in the pool with no simulated bonus: " + (", ".join(x["set"] for x in lrec["sets_without_bonus"]) or "none") + ".", ""]
        allm = {x["id"]: x for c in lrec["classes"].values() for x in c["skipped_matters"]}
        hi = sorted(allm.values(), key=lambda x: (-(db.get(x["id"], {}).get("scalingOptions", {}).get("0", {}).get("ilvl") or 0), x["name"] or ""))
        md += [f"Skipped effects that matter ({len(allm)} items across classes; item level 55 and up):", "",
               "| Item | Item level | Effect (upstream's text) | Forever client rate | Classic rate (where the client has none) |", "|---|---|---|---|---|"]
        for x in hi:
            il = db.get(x["id"], {}).get("scalingOptions", {}).get("0", {}).get("ilvl") or 0
            if il >= 55:
                md.append(f"| {x['name']} ({x['id']}) | {il} | {x['text'][:140]} | {x.get('client') or '-'} | "
                          f"{'-' if x.get('client') else '; '.join(x.get('classic') or ['-'])[:120]} |")
        md.append("")
        out["lists"][lst] = lrec
        print(f"{GT.GL.LABEL[lst]}: " + "; ".join(f"{c} {sum(v['modelled_scope'].values())}({sum(v['fires_scope'].values())})/{v['modelled_armor']}/{len(v['skipped_matters'])}"
                                                    for c, v in lrec["classes"].items()) + f" | sets without a bonus {len(lrec['sets_without_bonus'])}")
    if a.write:
        (HERE / "effects-inventory.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (ROOT / "_reference" / "effects-inventory.md").write_text("\n".join(md) + "\n", encoding="utf-8")
        print("wrote raidsim/effects-inventory.json and _reference/effects-inventory.md")


if __name__ == "__main__":
    main()
