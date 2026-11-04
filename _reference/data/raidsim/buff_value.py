"""Measure what a raid buff or debuff that a talent provides is worth to the specs that receive it, in the community simulators:
every receiving spec's hand build runs with the simulator's full buff set and with that one buff switched off, and the DPS
difference is the buff's value to that receiver. Times the number of beneficiaries (a stated assumption) it is the raid-wide
value of the talent, which goes into the provider's manual effect as a `utility` term of the raid-dps profile (the talent
is worth that if you are the one who brings the buff) and into the loops file.

    python _reference/data/raidsim/buff_value.py [--game forever|classic-era|all] [--iterations 3000] [--write]

Improved Scorch cannot be measured this way (the fire mage's own rotation keeps the debuff up, and without the talent the
Classic rotation breaks), so its value is computed from the tooltip: +15% fire damage times the receiver's fire share.
Writes `_reference/data/raidsim/buff-values.json`, the page `_reference/raid-buff-values.md`, and with --write the manual
effect files of both games and `scorer/loops/<class>.json`.
"""
import argparse
import collections
import datetime
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(ROOT / "_reference/data"))
import run as raidrun  # noqa: E402
from fmt_json import dumps  # noqa: E402

OUT = HERE / "buff-values.json"
PAGE = ROOT / "_reference/raid-buff-values.md"

# buff key -> what it is, who brings it, who receives it, how many receive it in a raid (assumption), per-game field names
BUFFS = collections.OrderedDict([
    ("trueshot_aura", {"talent": ("hunter", "Trueshot Aura"), "provider_specs": ["mm-raid", "mm-lonewolf-raid"], "ranks": 1,
                       "fields": {"classic-era": "trueshot_aura"}, "kind": "buffs_off",
                       "forever": {"analytic_value": 0.02, "beneficiaries": 1, "how": "beta tooltip: 30 ranged attack power for the party, about 2% of a raid hunter's ranged attack power; one other hunter in the party (the Forever fork has no party-buff switch)"},
                       "receivers": [("warrior", "fury-dw-raid"), ("warrior", "arms-2h-raid"), ("rogue", "combat-swords-raid"), ("rogue", "combat-daggers-raid"), ("paladin", "ret-dps"), ("shaman", "enhancement-dps"), ("druid", "feral-cat-dps")],
                       "beneficiaries": 4, "why": "a party aura: the hunter sits in a melee group of four others"}),
    ("leader_of_the_pack", {"talent": ("druid", "Leader of the Pack"), "provider_specs": ["feral-cat-dps", "feral-bear-tank"], "ranks": 1,
                            "fields": {"classic-era": "leader_of_the_pack"}, "kind": "buffs_off",
                            "forever": {"from": "classic-era", "how": "the same +3% party crit in the beta tooltip; the Forever fork's party-buff switch is a no-op, so the Classic measurement is used"},
                            "receivers": [("warrior", "fury-dw-raid"), ("warrior", "arms-2h-raid"), ("rogue", "combat-swords-raid"), ("rogue", "combat-daggers-raid"), ("paladin", "ret-dps"), ("shaman", "enhancement-dps"), ("hunter", "mm-raid")],
                            "beneficiaries": 4, "why": "a party aura: the feral druid sits in a melee group of four others"}),
    ("moonkin_aura", {"talent": ("druid", "Moonkin Form"), "provider_specs": ["balance-dps"], "ranks": 1,
                      "fields": {"classic-era": "moonkin_aura"}, "kind": "buffs_off",
                      "forever": {"from": "classic-era", "how": "the same +3% party crit in the beta tooltip; the Forever fork's party-buff switch is a no-op, so the Classic measurement is used"},
                      "receivers": [("mage", "frost-raid"), ("mage", "fire-raid"), ("warlock", "sb-raid"), ("warlock", "affliction-raid"), ("shaman", "elemental-dps"), ("priest", "shadow-dps")],
                      "beneficiaries": 4, "why": "a party aura: the moonkin sits in a caster group of four others"}),
    ("sanctity_aura", {"talent": ("paladin", "Sanctity Aura"), "provider_specs": ["ret-dps"], "ranks": 1,
                       "fields": {}, "kind": "analytic", "analytic": {"school:holy": 0.10}, "games": ["classic-era"],
                       "receivers": [("paladin", "ret-dps")],
                       "beneficiaries": 1, "why": "a party aura (+10% holy damage): one other retribution paladin in the group (Classic raids field few); computed from the tooltip because the simulator's paladin always runs its own aura option"}),
    ("winters_chill", {"talent": ("mage", "Winter's Chill"), "provider_specs": ["frost-raid"], "ranks": 5,
                       "fields": {"classic-era": "winters_chill"}, "kind": "debuffs_off",
                       "receivers": [("mage", "frost-raid")], "receiver_without": "Winter's Chill",
                       "beneficiaries": 4, "why": "a target debuff for frost spells: four other frost mages on the same boss (one mage brings it, the rest take Arcane Power)"}),
    ("improved_shadow_bolt", {"talent": ("warlock", "Improved Shadow Bolt"), "provider_specs": ["sb-raid", "affliction-raid", "fire-destro-raid"], "ranks": 5,
                              "fields": {"classic-era": "improved_shadow_bolt"}, "kind": "debuffs_off",
                              "receivers": [("warlock", "sb-raid")], "receiver_without": "Improved Shadow Bolt",
                              "beneficiaries": 3, "why": "a target debuff (four charges of +20% shadow damage): three other warlocks share the charges, so the simulator's permanent debuff is an upper bound"}),
    ("improved_battle_shout", {"talent": ("warrior", "Improved Battle Shout"), "provider_specs": ["fury-dw-raid", "arms-2h-raid"], "ranks": 5,
                               "fields": {}, "kind": "analytic", "games": ["classic-era"],
                               "classic-era": {"analytic_value": 0.035, "beneficiaries": 4, "how": "+25% Battle Shout attack power (about 58) for the group: roughly 3.5% DPS to each of four melee; the simulator's Battle Shout buff is a tristate the bench cannot half-switch"},
                               "receivers": [], "beneficiaries": 4, "why": "a party shout: four melee in the warrior's group"}),
    ("improved_scorch", {"talent": ("mage", "Improved Scorch"), "provider_specs": ["fire-raid"], "ranks": 3,
                         "fields": {}, "kind": "analytic", "analytic": {"school:fire": 0.15}, "games": ["classic-era"],
                         "receivers": [("mage", "fire-raid")],
                         "beneficiaries": 4, "why": "a target debuff (+15% fire damage): four other fire casters on the boss; computed from the tooltip because the receiver's own rotation keeps the debuff up"}),
])


def hand_build(entry, cls):
    """The spec's first hand build (not an opt-* export)."""
    ids = [b for b in entry["builds"] if not b.startswith("opt-")] or entry["builds"]
    data = json.load(open(ROOT / cls / raidrun.GAMES[raidrun.GAME]["builds"], encoding="utf-8"))
    by_id = {b["id"]: b for b in data["builds"]}
    return ids[0], raidrun.alloc_of(by_id[ids[0]])


def bench(repo, cls, entry, label, talents, off_key, field, on, iterations):
    """One bench run of `talents`: the sim's full set with the spec's own switches, except `field`, which is forced on or off."""
    cfg = {"class": entry["sim_class"], "race": entry.get("race", "RaceHuman"), "gear": entry["gear"], "apl": str(raidrun.apl_path(entry, repo)) if hasattr(raidrun, "apl_path") else entry["apl"], "spec": entry.get("spec", {}),
           "consumables": entry.get("consumables", {}), "buffs": "full", "buffs_off": list(entry.get("buffs_off", [])), "debuffs_off": list(entry.get("debuffs_off", [])),
           "profession1": entry.get("profession1", "Engineering"), "profession2": entry.get("profession2", ""), "distanceFromTarget": entry.get("distance", 5),
           "inFrontOfTarget": entry.get("in_front", False), "reactionTimeMs": 200, "iterations": iterations, "duration": raidrun.FIGHT, "seed": 1, "isTank": entry.get("tank", False),
           "builds": [{"label": label, "talents": talents}]}
    cfg[off_key] = [n for n in cfg[off_key] if n != field]
    if not on:
        cfg[off_key].append(field)
    d = repo / "bench"
    d.mkdir(exist_ok=True)
    p = d / f"buff-{cls}-{label}-{field}-{'on' if on else 'off'}.json"
    p.write_text(json.dumps(cfg, indent=1), encoding="utf-8")
    exe = repo / (f"{raidrun.GAMES[raidrun.GAME]['bench']}.exe" if (repo / f"{raidrun.GAMES[raidrun.GAME]['bench']}.exe").exists() else raidrun.GAMES[raidrun.GAME]["bench"])
    r = subprocess.run([str(exe), "--config", str(p), "--root", str(repo)], capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(repo))
    if r.returncode:
        raise SystemExit(f"bench failed: {r.stderr[-800:]}")
    raidrun.check_bench_stderr(r, f"buff_value {cls} {label}")
    for line in r.stdout.splitlines():
        if line.startswith("{"):
            row = json.loads(line)
            if row.get("error"):
                raise SystemExit(f"bench error for {label}: {row['error']}")
            return row["dps"]
    raise SystemExit("bench printed no result")


def school_share(cls, spec, game, tag):
    """Share of a spec model's damage from sources with `tag` (base shares, or the game's override)."""
    models = json.load(open(ROOT / "_reference/data/scorer/specs" / f"{cls}.json", encoding="utf-8"))["models"]
    tot, part = 0.0, 0.0
    for s in models[spec]["sources"]:
        if s.get("max_level"):
            continue
        sh = s.get("game_overrides", {}).get(game, {}).get("share", s["share"])
        tot += sh
        if tag in s["tags"]:
            part += sh
    return part / tot if tot else 0.0


def measure(game, a, out):
    raidrun.set_game(game)
    repo = raidrun.repo_path(a)
    commit = raidrun.git_commit(repo)
    out["sims"][game] = commit
    for key, B in BUFFS.items():
        if B.get(game) and isinstance(B.get(game), dict):   # no switch for it: another game's measurement or the tooltip stands in
            F = B[game]
            g = out["buffs"][key]["games"].setdefault(game, {"receivers": collections.OrderedDict()})
            if "from" in F:
                src = out["buffs"][key]["games"].get(F["from"])
                if not src:
                    continue
                g["receivers"] = collections.OrderedDict((k, dict(v, how=f"from {F['from']}")) for k, v in src["receivers"].items())
                g["mean_delta"], g["beneficiaries"] = src["mean_delta"], B["beneficiaries"]
            else:
                g["receivers"]["(tooltip)"] = {"build": "-", "delta": F["analytic_value"], "how": F["how"]}
                g["mean_delta"], g["beneficiaries"] = F["analytic_value"], F.get("beneficiaries", B["beneficiaries"])
            g["raid_value"] = g["mean_delta"] * g["beneficiaries"]
            g["how"] = F["how"]
            print(f"  {game} {key}: {F['how'][:70]}... -> mean +{g['mean_delta'] * 100:.1f}% x {g['beneficiaries']} = {g['raid_value'] * 100:.1f}%")
            continue
        if (B["kind"] != "analytic" and game not in B["fields"]) or (B["kind"] == "analytic" and game not in B.get("games", [])):
            continue
        g = out["buffs"][key]["games"].setdefault(game, {"receivers": collections.OrderedDict()})
        g["beneficiaries"] = B["beneficiaries"]
        for cls, spec in B["receivers"]:
            entry = raidrun.SPECS.get(cls, {}).get(spec)
            if not entry:
                continue
            bid, alloc = hand_build(entry, cls)
            if B.get("receiver_without") and B["receiver_without"] in alloc:
                alloc = {k: v for k, v in alloc.items() if k != B["receiver_without"]}
                bid += f" -{B['receiver_without']}"
            if B["kind"] == "analytic":
                tag, v = next(iter(B["analytic"].items()))
                fs = school_share(cls, spec, game, tag)
                delta = v * fs
                g["receivers"][f"{cls}/{spec}"] = {"build": bid, "delta": delta, "how": f"analytic: {v * 100:.0f}% x {tag.split(':')[1]} share {fs * 100:.0f}%"}
                print(f"  {game} {key} -> {cls}/{spec}: +{delta * 100:.1f}% (analytic)")
                continue
            trees = raidrun.load_trees(repo, cls)
            talents = raidrun.talents_string(trees, alloc)
            full = bench(repo, cls, entry, bid, talents, B["kind"], B["fields"][game], True, a.iterations)
            off = bench(repo, cls, entry, bid, talents, B["kind"], B["fields"][game], False, a.iterations)
            delta = (full - off) / off if off else 0.0
            g["receivers"][f"{cls}/{spec}"] = {"build": bid, "dps_full": full, "dps_off": off, "delta": delta, "how": "measured"}
            print(f"  {game} {key} -> {cls}/{spec} ({bid}): {full:.0f} vs {off:.0f} DPS without = +{delta * 100:.1f}%")
        ds = [r["delta"] for r in g["receivers"].values()]
        g["mean_delta"] = sum(ds) / len(ds) if ds else 0.0
        g["raid_value"] = g["mean_delta"] * B["beneficiaries"]
        print(f"  {game} {key}: mean +{g['mean_delta'] * 100:.1f}% per receiver x {B['beneficiaries']} = {g['raid_value'] * 100:.1f}% of one player's DPS")


def write_page(out):
    o = ["# Raid buff values — what a support talent is worth to the raid", "",
         f"> Generated by `_reference/data/raidsim/buff_value.py` on {out['date']}: every receiving spec's hand build ran in the community simulator "
         f"(ElliotWood/Forever {out['sims'].get('forever', '-')} for Forever, wowsims/classic {out['sims'].get('classic-era', '-')} for Classic Era) with the "
         "simulator's full buff set and with the one buff switched off; the difference is the buff's value to that receiver. Times the assumed number of "
         "beneficiaries it is the raid-wide value written into the provider talent's `utility` effect for the raid-dps profile (`effects/<game>/<class>.manual.json`) "
         "and into `scorer/loops/<class>.json`. Simulations of the community's models, not measurements; the beneficiary counts are assumptions. Do not hand-edit.", ""]
    for key, B in BUFFS.items():
        cls, talent = B["talent"]
        o.append(f"## {talent} ({cls}) — `{key}`")
        o.append("")
        o.append(f"Beneficiaries assumed: {B['beneficiaries']} ({B['why']}).")
        o.append("")
        o.append("| Game | Receiver | Build | DPS with | DPS without | Value to the receiver |")
        o.append("|---|---|---|---|---|---|")
        for game, g in out["buffs"][key]["games"].items():
            for rid, r in g["receivers"].items():
                o.append(f"| {game} | `{rid}` | `{r['build']}` | {r.get('dps_full', 0):.0f} | {r.get('dps_off', 0):.0f} | {r['delta'] * 100:+.1f}% ({r['how']}) |" if r["how"] == "measured" else
                         f"| {game} | `{rid}` | `{r['build']}` | - | - | {r['delta'] * 100:+.1f}% ({r['how']}) |")
            o.append(f"| {game} | **mean x {g.get('beneficiaries', B['beneficiaries'])}** | | | | **{g['raid_value'] * 100:+.1f}%** of one player's DPS |")
        if not out["buffs"][key]["games"]:
            o.append("| - | not measurable in either simulator | | | | |")
        o.append("")
    PAGE.write_text("\n".join(o) + "\n", encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT)}")


def write_models(out):
    """The provider talent's raid-dps utility (both games; a value measured in one simulator only serves the other, noted) and the loops entry."""
    for key, B in BUFFS.items():
        cls, talent = B["talent"]
        games = out["buffs"][key]["games"]
        if not games:
            continue
        for game in ("forever", "classic-era"):
            man_p = ROOT / "_reference/data/scorer/effects" / game / f"{cls}.manual.json"
            man = json.load(open(man_p, encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
            if game not in games:
                # Forever's Winter's Chill, Improved Scorch and Improved Shadow Bolt only affect the mage's or warlock's own spells
                # (beta tooltips, build 1.60.1.70009): no raid value there, so any old raid utility goes
                if talent in man and any(x.get("channel") == "utility" for x in man[talent]["effects"]):
                    man[talent]["effects"] = [x for x in man[talent]["effects"] if x.get("channel") != "utility"]
                    man[talent]["note"] = man[talent].get("note", "").split(" Raid buff value")[0].rstrip() + f" Raid buff value ({out['date']}, buff_value.py): none in this game, the effect is personal here."
                    man_p.write_text(dumps(man), encoding="utf-8")
                continue
            g = games[game]
            value = g["raid_value"]
            e = man.get(talent) or collections.OrderedDict([("note", ""), ("effects", [])])
            e["effects"] = [x for x in e["effects"] if x.get("channel") != "utility"]
            vals = [round(value * r / B["ranks"], 4) for r in range(1, B["ranks"] + 1)]
            # only the models that actually bring the buff (a frost mage does not keep Improved Scorch up): tagged with the provider specs
            e["effects"].append(collections.OrderedDict([("channel", "utility"), ("scope", ["profile:raid-dps", "profile:raid-tank"] if key == "leader_of_the_pack" else ["profile:raid-dps"]), ("values", vals), ("modes", ["raid"]), ("specs", list(B["provider_specs"]))]))
            e["note"] = e.get("note", "").split(" Raid buff value")[0].rstrip() + (
                f" Raid buff value ({out['date']}, buff_value.py): worth {g['mean_delta'] * 100:.1f}% DPS to each receiver in the {'ElliotWood/Forever' if game == 'forever' else 'wowsims/classic'} simulator"
                f", x {g.get('beneficiaries', B['beneficiaries'])} beneficiaries = utility {value * 100:.1f}% in the raid-dps profile if you are the one who brings it." + (f" ({g['how']})" if g.get("how") else ""))
            man[talent] = e
            man_p.write_text(dumps(man), encoding="utf-8")
        loops_p = ROOT / "_reference/data/scorer/loops" / f"{cls}.json"
        loops = json.load(open(loops_p, encoding="utf-8"), object_pairs_hook=collections.OrderedDict) if loops_p.exists() else collections.OrderedDict()
        for spec in B["provider_specs"]:
            if spec not in loops:
                continue
            t = loops[spec].setdefault("talents", collections.OrderedDict())
            old = t.get(talent, collections.OrderedDict())
            t[talent] = collections.OrderedDict([
                ("role", "raid-buff"),
                ("why", f"Brings {key.replace('_', ' ')} to {B['beneficiaries']} others ({B['why']}); worth " + ", ".join(f"{gm}: +{gg['mean_delta'] * 100:.1f}% per receiver" for gm, gg in games.items()) + " (buff_value.py)."),
                ("encoded", "utility " + ", ".join(f"{gg['raid_value'] * 100:.1f}% ({gm})" for gm, gg in games.items()) + " in raid-dps (buff_value.py)"),
                ("sources", list(dict.fromkeys(list(old.get("sources", [])) + ["_reference/raid-buff-values.md"]))),
            ])
        loops_p.write_text(dumps(loops), encoding="utf-8")
        print(f"  {cls} {talent}: utility written to both games' manual files and loops")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--game", default="all", choices=["all", "forever", "classic-era"])
    ap.add_argument("--iterations", type=int, default=3000)
    ap.add_argument("--repo")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    out = {"date": datetime.date.today().isoformat(), "sims": {}, "buffs": collections.OrderedDict((k, {"talent": B["talent"], "beneficiaries": B["beneficiaries"], "why": B["why"], "games": collections.OrderedDict()}) for k, B in BUFFS.items())}
    for game in (["classic-era", "forever"] if a.game == "all" else [a.game]):   # Classic first: Forever borrows from it where the fork has no switch
        measure(game, a, out)
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    write_page(out)
    if a.write:
        write_models(out)


if __name__ == "__main__":
    main()
