"""Write `specs-classic.json`: our Classic-era raid DPS spec models -> the upstream wowsims/classic simulator's spec folders
(`ui/<spec>/`), gear preset, rotation, player options, consumes and race, read from each folder's presets.ts.

    python _reference/data/raidsim/classic_specs.py

The upstream simulator's Player message uses enum-based `consumes` and per-spec option messages without a classOptions
nesting, so the fragments differ from the Forever ones; TS enum references (`Flask.FlaskOfSupremePower`) become the enum
value name. Builds are our `<class>/talents/classic-baseline/builds.json` raid DPS ids. Edit the SPECS table to add a model.
Gear sets the upstream sim lacks live under `raidsim/gear_sets/classic/<sim folder>/` and are copied into the clone.
"""
import json
import os
import pathlib
import re
import shutil

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REPO = pathlib.Path(os.environ.get("WOW_FOREVER_CLASSIC_SIM", pathlib.Path.home() / ".wow-forever-tools" / "classic-repo"))
OUT = HERE / "specs-classic.json"
OWN_GEAR = HERE / "gear_sets" / "classic"

# our spec model id -> (class, sim folder, Player oneof key, sim class enum, gear keyword, apl keyword, our build ids)
SPECS = {
    "frost-raid": ("mage", "mage", "mage", "ClassMage", "p1.bis", "p1", ["frost-arcane-power-raid", "frost-winters-chill-raid"]),
    "fire-raid": ("mage", "mage", "mage", "ClassMage", "p1.bis", "p1", ["fire-raid"]),
    "sb-raid": ("warlock", "warlock", "warlock", "ClassWarlock", "mc", "rotation", ["ds-ruin-raid", "sm-ruin-raid"]),
    "mm-raid": ("hunter", "hunter", "hunter", "ClassHunter", "p1.bis", "p1", ["bm-mm-raid", "mm-surv-hit-raid"]),
    "fury-dw-raid": ("warrior", "warrior", "warrior", "ClassWarrior", "phase_1", "dps_no_reck", ["fury-dw-raid", "fury-2h-raid"]),
    "combat-swords-raid": ("rogue", "rogue", "rogue", "ClassRogue", "sinister_strike_p1", "combat_sinister_strike.apl", ["combat-swords-raid"]),
    "combat-daggers-raid": ("rogue", "rogue", "rogue", "ClassRogue", "backstab_p1", "combat_backstab.apl", ["combat-daggers-raid"]),
    "ret-dps": ("paladin", "retribution_paladin", "retributionPaladin", "ClassPaladin", "p1_plate_2h", "basic_ret", ["ret-raid-dps"]),
    "elemental-dps": ("shaman", "elemental_shaman", "elementalShaman", "ClassShaman", "phase_1", "default", ["elemental-raid-dps"]),
    "enhancement-dps": ("shaman", "enhancement_shaman", "enhancementShaman", "ClassShaman", "phase_1", "default", ["enhancement-raid-support"]),
    "feral-cat-dps": ("druid", "feral_druid", "feralDruid", "ClassDruid", "p1.bis", "feral", ["feral-cat-dps"]),
    "balance-dps": ("druid", "balance_druid", "balanceDruid", "ClassDruid", "p1.bis", "balance", ["balance-moonkin-raid"]),
}


# the sim's full buff/debuff set (sim/core/test_utils.go) already carries these; a spec that provides one through a talent gets it
# switched off so the talent is measured, not duplicated (proto field names of RaidBuffs/PartyBuffs/IndividualBuffs and Debuffs)
BUFFS_OFF = {"mm-raid": ["trueshot_aura"], "ret-dps": ["sanctity_aura"], "feral-cat-dps": ["leader_of_the_pack"], "balance-dps": ["moonkin_aura"]}
DEBUFFS_OFF = {"frost-raid": ["winters_chill"], "fire-raid": ["improved_scorch"], "sb-raid": ["improved_shadow_bolt"]}


def ts_block(text, name):
    """The body of `export const <name> = X.create({ ... });` (empty for `create({})`), or None when the constant is not a create call."""
    m = re.search(r"export const " + re.escape(name) + r" = \w+\.create\(\{(.*?)\}\);", text, re.S)
    return m.group(1) if m else None


def consumes_block(text):
    """DefaultConsumes when it is a create call, else the first `<Name>Consumes = Consumes.create({...})` (per-phase tables)."""
    b = ts_block(text, "DefaultConsumes")
    if b is not None:
        return b
    m = re.search(r"export const (\w*Consumes) = Consumes\.create\(\{", text)
    return ts_block(text, m.group(1)) if m else ""


def ts_to_json(block):
    """A flat TS object literal (numbers, booleans, Enum.Value, nested {...}) -> dict; comments dropped."""
    out = {}
    for line in (block or "").splitlines():
        line = line.split("//")[0].strip().rstrip(",")
        if not line:
            continue
        m = re.match(r"(\w+):\s*(.+)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if v == "true":
            out[k] = True
        elif v == "false":
            out[k] = False
        elif re.fullmatch(r"-?\d+(\.\d+)?", v):
            out[k] = float(v) if "." in v else int(v)
        elif re.fullmatch(r"\w+\.\w+", v):
            out[k] = v.split(".")[1]
        elif v.startswith("{") and v.endswith("}"):
            out[k] = ts_to_json(v[1:-1].replace(",", "\n"))
        elif v.startswith("'") or v.startswith('"'):
            out[k] = v.strip("'\"")
    return out


def pick(files, keyword):
    files = sorted(files)
    for f in files:
        if keyword and keyword in f.name.lower():
            return f
    return files[0] if files else None


def main():
    if not REPO.exists():
        raise SystemExit(f"no Classic simulator checkout at {REPO} (setup.py --game classic)")
    out = {"_comment": "Classic-era spec models -> upstream wowsims/classic presets (generated by classic_specs.py; edit SPECS there; "
                       "gear sets under raidsim/gear_sets/classic/ are ours, copied into the clone)"}
    for spec, (cls, folder, key, sim_class, gear_kw, apl_kw, builds) in SPECS.items():
        base = REPO / "ui" / folder
        if not base.exists():
            print(f"{spec}: no folder {base}")
            continue
        for own in (OWN_GEAR / folder).glob("*.gear.json"):   # our additions to the sim's gear presets
            shutil.copy(own, base / "gear_sets" / own.name)
        text = (base / "presets.ts").read_text(encoding="utf-8")
        gear = pick(list((base / "gear_sets").glob("*.gear.json")), gear_kw)
        apl = pick(list((base / "apls").glob("*.apl.json")), apl_kw)
        options = ts_to_json(ts_block(text, "DefaultOptions"))
        consumes = ts_to_json(consumes_block(text))
        other = ts_to_json(ts_block(text, "OtherDefaults"))   # a plain object literal in some folders: fall back to a regex on the file
        race_m = re.search(r"race:\s*Race\.(\w+)", text)
        race = other.get("race") or (race_m.group(1) if race_m else "RaceHuman")
        dist_m = re.search(r"distanceFromTarget:\s*(\d+)", text)
        entry = {"class": cls, "sim_class": sim_class, "sim_spec": folder, "profile": "raid-dps", "race": race,
                 "distance": other.get("distanceFromTarget", int(dist_m.group(1)) if dist_m else 5), "profession1": other.get("profession1", "Engineering"),
                 "gear": str(gear.relative_to(REPO)).replace(os.sep, "/") if gear else "", "apl": str(apl.relative_to(REPO)).replace(os.sep, "/") if apl else "",
                 "spec": {key: {"options": options}}, "consumables": consumes, "builds": builds,
                 "buffs_off": BUFFS_OFF.get(spec, []), "debuffs_off": DEBUFFS_OFF.get(spec, [])}
        out.setdefault(cls, {})[spec] = entry
        print(f"{spec}: {folder} gear={gear.name if gear else '-'} apl={apl.name if apl else '-'} race={race} options={json.dumps(options)[:70]} consumes={len(consumes)} keys")
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
