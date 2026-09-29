"""Write `<class>/research/raid/gear.md`, `<class>/research/raid/consumables.md`, `<class>/research/raid/rotation.md` and `<class>/research/leveling/rotation.md` from the ElliotWood/Forever
simulator's presets (generated): the community's gear sets per spec and phase, its standard raid consumables, and its rotations
(APL files) translated into readable priority lists, next to the fight lab's leveling priority.

    python _reference/data/render_sim_presets.py [classes...]

Needs the simulator checkout (`_reference/data/raidsim/setup.py`; WOW_FOREVER_SIM or ~/.wow-forever-tools/forever-repo). Every
name comes from the simulator's database (`assets/database/db.json`): items, enchants, random suffixes, consumables, spells.
These are the simulator maintainers' presets for the beta, not measurements; `rebuild.py --steps regen` runs this after the guides.
"""
import datetime
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE / "scorer"))
sys.path.insert(0, str(HERE / "fightlab"))
sys.path.append(str(HERE))
import paths  # noqa: E402
import readme_sections as rs  # noqa: E402
from run import MODULES  # noqa: E402

REPO = pathlib.Path(os.environ.get("WOW_FOREVER_SIM", pathlib.Path.home() / ".wow-forever-tools" / "forever-repo"))
SLOTS = ["Head", "Neck", "Shoulder", "Back", "Chest", "Wrist", "Hands", "Waist", "Legs", "Feet", "Finger", "Finger", "Trinket", "Trinket", "Main hand", "Off hand", "Ranged"]
QUALITY = {0: "poor", 1: "common", 2: "uncommon", 3: "rare", 4: "epic", 5: "legendary"}
SPEC_FOLDERS = {"druid": ["balance", "feralcat", "feralbear", "restoration"], "hunter": ["dps"], "mage": ["dps"], "paladin": ["holy", "protection", "retribution"],
                "priest": ["dps", "healer"], "rogue": ["dps"], "shaman": ["elemental", "enhancement", "restoration"], "warlock": ["dps"], "warrior": ["dps", "protection"]}
CMP = {"OpEq": "=", "OpNe": "≠", "OpLt": "<", "OpLe": "≤", "OpGt": ">", "OpGe": "≥"}
MATH = {"OpAdd": "+", "OpSub": "−", "OpMul": "×", "OpDiv": "÷"}


class Names:
    def __init__(self, repo):
        db = json.load(open(repo / "assets/database/db.json", encoding="utf-8"))
        self.items = {i["id"]: i for i in db.get("items", [])}
        self.enchants = {e["effectId"]: e for e in db.get("enchants", [])}
        self.suffixes = {s["id"]: s["name"] for s in db.get("randomSuffixes", [])}
        self.consumables = {c["id"]: c["name"] for c in db.get("consumables", [])}
        for i in db.get("itemIcons", []):
            self.consumables.setdefault(i["id"], i["name"])
        self.spells = {s["id"]: s["name"] for s in db.get("spellIcons", [])}
        for book in (ROOT / "_reference/data/forever-spells").glob("*.json"):
            for tab in json.load(open(book, encoding="utf-8")).get("tabs", []):
                for sp in tab.get("spells", []):
                    for r in sp.get("ranks", []):
                        if r.get("id"):
                            self.spells.setdefault(int(r["id"]), sp["name"])
        for tree in (repo / "ui/sim/talents/trees").glob("*.json"):
            for tr in json.load(open(tree, encoding="utf-8")):
                for t in tr["talents"]:
                    if t.get("spellId"):
                        self.spells.setdefault(int(t["spellId"]), t["fancyName"])
        # ids the simulator's database leaves unnamed (Classic 1.12 item ids; 44404 is the simulator's own Missile Barrage aura, talents_arcane.go)
        for iid, name in {8008: "Mana Ruby (mana gem)", 10646: "Goblin Sapper Charge", 18641: "Dense Dynamite"}.items():
            self.consumables.setdefault(iid, name)
        self.spells.setdefault(44404, "Missile Barrage")
        self.unknown = set()

    def spell(self, sid):
        if sid in self.spells:
            return self.spells[sid]
        self.unknown.add(sid)
        return f"spell {sid}"

    def item(self, iid):
        it = self.items.get(iid)
        if it:
            return it["name"]
        return self.consumables.get(iid, f"item {iid}")


# ------------------------------------------------------------------ APL translation
def val(v, N):
    """A value expression of the APL as text."""
    if not isinstance(v, dict) or not v:
        return "?"
    k, x = next(iter(v.items()))
    if k == "const":
        return str(x.get("val", ""))
    if k == "cmp":
        return f"{val(x.get('lhs'), N)} {CMP.get(x.get('op'), x.get('op', '?'))} {val(x.get('rhs'), N)}"
    if k == "math":
        return f"({val(x.get('lhs'), N)} {MATH.get(x.get('op'), x.get('op', '?'))} {val(x.get('rhs'), N)})"
    if k == "and":
        return " and ".join(val(y, N) for y in x.get("vals", []))
    if k == "or":
        return "(" + " or ".join(val(y, N) for y in x.get("vals", [])) + ")"
    if k == "not":
        return "not " + val(x.get("val"), N)
    if k in ("auraIsActive", "auraIsActiveWithReactionTime"):
        return f"{aura(x, N)} is up"
    if k == "auraIsKnown":
        return f"{aura(x, N)} is known"
    if k == "auraRemainingTime":
        return f"time left on {aura(x, N)}"
    if k == "auraNumStacks":
        return f"stacks of {aura(x, N)}"
    if k == "auraInternalCooldown":
        return f"internal cooldown of {aura(x, N)}"
    if k == "auraIcdIsReady":
        return f"{aura(x, N)}'s internal cooldown is ready"
    if k == "auraShouldRefresh":
        return f"{aura(x, N)} should be refreshed"
    if k == "dotIsActive":
        return f"{spell_ref(x.get('spellId'), N)} is on the target"
    if k == "dotRemainingTime":
        return f"time left on {spell_ref(x.get('spellId'), N)}"
    if k == "spellIsReady":
        return f"{spell_ref(x.get('spellId'), N)} is ready"
    if k == "spellCanCast":
        return f"{spell_ref(x.get('spellId'), N)} can be cast"
    if k == "spellTimeToReady":
        return f"time until {spell_ref(x.get('spellId'), N)} is ready"
    if k == "spellCastTime":
        return f"cast time of {spell_ref(x.get('spellId'), N)}"
    if k == "spellChannelTime":
        return f"channel time of {spell_ref(x.get('spellId'), N)}"
    if k == "spellNumCharges":
        return f"charges of {spell_ref(x.get('spellId'), N)}"
    if k == "spellIsKnown":
        return f"{spell_ref(x.get('spellId'), N)} is known"
    if k == "spellCpm":
        return f"casts per minute of {spell_ref(x.get('spellId'), N)}"
    if k == "gcdIsReady":
        return "the global cooldown is ready"
    if k == "gcdTimeToReady":
        return "time until the global cooldown is ready"
    simple = {"currentTime": "time into the fight", "currentTimePercent": "% of the fight elapsed", "remainingTime": "time left in the fight",
              "remainingTimePercent": "% of the fight left", "currentHealth": "health", "currentHealthPercent": "health %", "currentMana": "mana",
              "currentManaPercent": "mana %", "currentRage": "rage", "currentEnergy": "energy", "currentComboPoints": "combo points",
              "currentRunicPower": "runic power", "numberTargets": "number of targets", "isExecutePhase": "execute phase", "targetHealthPercent": "target health %",
              "energyThreshold": "energy threshold", "energyRegenPerSecond": "energy per second", "manaRegenPerSecond": "mana per second",
              "channelClipDelay": "channel clip delay", "frontOfTarget": "in front of the target", "autoTimeToNext": "time to the next auto attack",
              "autoSwingTime": "auto attack swing time", "currentNonDeathRuneCount": "runes", "isExecutePhase20": "execute phase (20%)", "catExcessEnergy": "excess cat energy",
              "catNewSavageRoarDuration": "Savage Roar duration", "totemRemainingTime": "time left on the totem", "warlockShouldRecastDrainSoul": "Drain Soul should be recast",
              "warlockShouldRefreshCorruption": "Corruption should be refreshed", "spellCurrentCost": "current cost", "sequenceIsComplete": "the sequence is complete",
              "sequenceIsReady": "the sequence is ready", "sequenceTimeToReady": "time until the sequence is ready", "boolAnd": "and", "shamanCanSnapshotStrongerFireTotem": "a stronger fire totem could be snapshot"}
    if k in simple:
        label = simple[k]
        if isinstance(x, dict) and x.get("threshold"):
            label += f" ({x['threshold']})"
        if isinstance(x, dict) and x.get("targetUnit"):
            label += " of the target"
        return label
    if k == "runeCooldown" or k == "nextRuneCooldown":
        return "rune cooldown"
    return k


def aura(x, N):
    a = x.get("auraId") or {}
    if "spellId" in a:
        return N.spell(int(a["spellId"]))
    if "itemId" in a:
        return N.item(int(a["itemId"]))
    return "aura"


def spell_ref(s, N):
    s = s or {}
    if "spellId" in s:
        return N.spell(int(s["spellId"]))
    if "itemId" in s:
        return N.item(int(s["itemId"]))
    if "otherId" in s:
        return str(s["otherId"]).replace("OtherAction", "")
    return "?"


def action(a, N, depth=0):
    """One APL action as a line (nested sequences indented)."""
    cond = val(a["condition"], N) if a.get("condition") else ""
    body = {k: v for k, v in a.items() if k != "condition"}
    if not body:
        return "(empty)"
    k, x = next(iter(body.items()))
    if k == "castSpell":
        txt = f"cast {spell_ref(x.get('spellId'), N)}" + (f" on {x['target'].get('type', '').lower()}" if x.get("target") and x["target"].get("type") not in (None, "Target", "Unknown") else "")
    elif k == "channelSpell":   # a channel (Mind Flay, Drain Soul): named like a cast (it printed as "channelSpell" until 2026-09-29)
        txt = f"channel {spell_ref(x.get('spellId'), N)}" + (" (interrupt it when a higher line is ready)" if x.get("interruptIf") else "")
    elif k == "castFriendlySpell":
        txt = f"cast {spell_ref(x.get('spellId'), N)} on a friendly target"
    elif k == "multidot":
        txt = f"keep {spell_ref(x.get('spellId'), N)} on up to {x.get('maxDots', '?')} targets" + (f" (refresh under {x.get('maxOverlap', {}).get('const', {}).get('val', '?')})" if x.get("maxOverlap") else "")
    elif k == "multishield":
        txt = f"shield up to {x.get('maxShields', '?')} targets with {spell_ref(x.get('spellId'), N)}"
    elif k == "autocastOtherCooldowns":
        txt = "use every other cooldown when ready"
    elif k == "wait":
        txt = f"wait {val(x.get('duration'), N)}"
    elif k == "waitUntil":
        txt = f"wait until {val(x.get('condition'), N)}"
    elif k in ("sequence", "strictSequence"):
        inner = "; ".join(action(y, N, depth + 1) for y in x.get("actions", []))
        txt = ("sequence" if k == "sequence" else "strict sequence") + (f" '{x['name']}'" if x.get("name") else "") + f": {inner}"
    elif k == "resetSequence":
        txt = f"reset sequence '{x.get('sequenceName', '')}'"
    elif k == "activateAura":
        txt = f"activate {aura(x, N)}"
    elif k == "cancelAura":
        txt = f"cancel {aura(x, N)}"
    elif k == "triggerIcd":
        txt = f"trigger the internal cooldown of {aura(x, N)}"
    elif k == "changeTarget":
        txt = "change target"
    elif k == "itemSwap":
        txt = f"swap to the {x.get('swapSet', '?')} item set"
    elif k == "move":
        txt = f"move to {val(x.get('rangeFromTarget'), N)} yd"
    elif k == "schedule":
        txt = f"at {x.get('schedule', '?')}: {action(x.get('innerAction', {}), N, depth + 1)}"
    elif k == "castAllStatBuffCooldowns":
        txt = "use every stat cooldown"
    elif k == "customRotation":
        txt = "custom rotation: " + "; ".join(action(y.get("action", y), N, depth + 1) for y in x.get("actions", []))
    else:
        txt = k
    return (f"if {cond}: " if cond else "") + txt


def render_apl(path, N):
    apl = json.load(open(path, encoding="utf-8"))
    o = []
    pre = apl.get("prepullActions") or []
    if pre:
        o.append("Before the pull: " + "; ".join((f"at {p.get('doAtValue', {}).get('const', {}).get('val', '?')}: " if p.get("doAtValue") else "") + action(p.get("action", {}), N) for p in pre))
        o.append("")
    o.append("In priority order, the first line whose condition holds is cast:")
    o.append("")
    for i, item in enumerate(apl.get("priorityList", []), 1):
        if item.get("hide"):
            continue
        o.append(f"{i}. {action(item.get('action', {}), N)}")
    return o


# ------------------------------------------------------------------ pages
def gear_page(cls, N, commit):
    o = [f"# {cls.title()} — gear presets (generated)", "",
         f"> Generated by `_reference/data/render_sim_presets.py` on {datetime.date.today().isoformat()} from the ElliotWood/Forever simulator's gear presets "
         f"(commit {commit}, `ui/specs/{cls}/<spec>/gear_sets/`): the community's launch, pre-raid and phase sets for the beta, named from its item database. "
         "Presets are the maintainers' picks, not measurements; the fight lab levels in Classic quest greens, the raid sim races talents in the phase-1 sets below. Do not hand-edit.", ""]
    for spec in SPEC_FOLDERS.get(cls, []):
        folder = REPO / "ui/specs" / cls / spec / "gear_sets"
        if not folder.exists():
            continue
        for gs in sorted(folder.glob("*.gear.json")):
            g = json.load(open(gs, encoding="utf-8"))
            o += [f"## {spec}: `{gs.name}`", "", "| Slot | Item | Quality | Phase | Enchant |", "|---|---|---|---|---|"]
            for i, it in enumerate(g.get("items", [])):
                if not it or not it.get("id"):
                    continue
                rec = N.items.get(it["id"], {})
                name = rec.get("name", f"item {it['id']}")
                if it.get("randomSuffix"):
                    name += " " + N.suffixes.get(it["randomSuffix"], f"(suffix {it['randomSuffix']})")
                ench = N.enchants.get(it.get("enchant"), {}).get("name", "") if it.get("enchant") else ""
                slot = SLOTS[i] if i < len(SLOTS) else f"slot {i}"
                o.append(f"| {slot} | {name} | {QUALITY.get(rec.get('quality'), '-')} | {rec.get('phase', '-')} | {ench} |")
            o.append("")
    return "\n".join(o) + "\n"


def consumables_page(cls, N, commit):
    o = [f"# {cls.title()} — consumables (generated)", "",
         f"> Generated by `_reference/data/render_sim_presets.py` on {datetime.date.today().isoformat()} from the ElliotWood/Forever simulator's per-spec default consumables "
         f"(commit {commit}, `ui/specs/{cls}/<spec>/presets.ts`): what the community simulates a raider drinking, eating and imbuing in the beta. "
         "Item names from the simulator's database. Not measurements. Do not hand-edit.", ""]
    keys = {"flaskId": "Flask", "battleElixirId": "Battle elixir", "guardianElixirId": "Guardian elixir", "spellPowerElixirId": "Spell power elixir", "schoolElixirId": "School elixir",
            "defenseElixirId": "Defense elixir", "foodId": "Food", "potId": "Potion", "conjuredId": "Conjured item", "strengthBuffId": "Strength buff", "attackPowerBuffId": "Attack power buff",
            "zanzaId": "Zanza / Blasted Lands buff", "alcoholId": "Alcohol", "mhImbueId": "Main-hand imbue", "ohImbueId": "Off-hand imbue", "explosiveId": "Explosive",
            "dragonbreathChili": "Dragonbreath Chili", "goblinSapper": "Goblin Sapper Charge", "boglingRoot": "Bogling Root", "scrollAgi": "Scroll of Agility", "scrollStr": "Scroll of Strength",
            "scrollInt": "Scroll of Intellect", "scrollSpi": "Scroll of Spirit", "scrollArm": "Scroll of Protection"}
    for spec in SPEC_FOLDERS.get(cls, []):
        pt = REPO / "ui/specs" / cls / spec / "presets.ts"
        if not pt.exists():
            continue
        s = pt.read_text(encoding="utf-8")
        for m in re.finditer(r"export const (\w+) = ConsumesSpec\.create\(\{(.*?)\}\);", s, re.S):
            label, body = m.group(1), m.group(2)
            o += [f"## {spec}: `{label}`", "", "| Kind | Item |", "|---|---|"]
            for line in body.splitlines():
                mm = re.match(r"\s*(\w+):\s*(\d+|true),?\s*(?://\s*(.*))?", line)
                if not mm:
                    continue
                key, v, comment = mm.group(1), mm.group(2), (mm.group(3) or "").strip()
                if v == "true":
                    o.append(f"| {keys.get(key, key)} | yes |")
                else:
                    o.append(f"| {keys.get(key, key)} | {comment or N.consumables.get(int(v)) or N.item(int(v))} |")
            o.append("")
    return "\n".join(o) + "\n"


def rotation_page(cls, N, commit):
    cm = __import__(MODULES[cls][0])
    o = [f"# {cls.title()} — raid rotations (generated)", "",
         f"> Generated by `_reference/data/render_sim_presets.py` on {datetime.date.today().isoformat()}. Raid rotations are the ElliotWood/Forever simulator's action priority lists "
         f"(commit {commit}, `ui/specs/{cls}/<spec>/apls/`), translated line by line (spell names from its database; a condition reads left to right, the first line whose condition holds is cast). "
         "The leveling priority the fight lab plays is on the [leveling rotation page](../leveling/rotation.md). Models of the beta, not measurements. Do not hand-edit.", ""]
    for spec in SPEC_FOLDERS.get(cls, []):
        folder = REPO / "ui/specs" / cls / spec / "apls"
        if not folder.exists():
            continue
        for ap in sorted(folder.glob("*.apl.json")):
            o += [f"## {spec}: `{ap.name}`", ""] + render_apl(ap, N) + [""]
    return "\n".join(o) + "\n"


def leveling_rotation_page(cls):
    """The priority list the fight lab plays while leveling (the module's DESCRIPTION)."""
    cm = __import__(MODULES[cls][0])
    o = [f"# {cls.title()} — leveling rotation (generated)", "",
         f"> Generated by `_reference/data/render_sim_presets.py` on {datetime.date.today().isoformat()} from the fight lab's {cls} module "
         f"(`_reference/data/fightlab/{MODULES[cls][0]}.py`): the priority list it plays against same-level mobs. A model of the beta, not a "
         "measurement. Do not hand-edit.", "", cm.DESCRIPTION, ""]
    for er in getattr(cm, "PIPELINE", {}).get("extra_reports", []):
        o.append(f"- Other spec simulated: `{er['spec']}` (see [fightlab/{er['spec']}.md](fightlab/{er['spec']}.md)).")
    return "\n".join(o).rstrip("\n") + "\n"


def main():
    classes = sys.argv[1:] or list(MODULES)
    if not (REPO / "assets/database/db.json").exists():
        print(f"no simulator checkout at {REPO}: run _reference/data/raidsim/setup.py")
        return
    N = Names(REPO)
    import subprocess
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "?"
    for cls in classes:
        for out, fn in ((paths.gear_page(cls), gear_page), (paths.consumables_page(cls), consumables_page)):
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fn(cls, N, commit), encoding="utf-8")   # the rotation pages come from render_rotations.py (per build)
        readme = paths.scenario_readme(cls, "raid")
        rs.splice_ordered(readme, "raid", "## Rotation, gear and consumables", "\n".join([
            "## Rotation, gear and consumables", "",
            "From the ElliotWood/Forever simulator's presets (the community's model of the beta):", "",
            "- [Rotation](rotation.md): what each build casts, ours and the simulator's own: its priority list filtered to the lines that build uses.",
            "- [Gear](gear.md): the launch, pre-raid and phase gear sets.",
            "- [Consumables](consumables.md): the standard raid consumables per spec."]))
        print(f"{cls}: raid gear and consumables written")
    if N.unknown:
        print(f"{len(N.unknown)} spell ids without a name (shown as 'spell <id>'): {sorted(N.unknown)[:12]}")


if __name__ == "__main__":
    main()
