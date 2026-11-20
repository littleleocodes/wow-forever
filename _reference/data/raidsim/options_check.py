"""Our entries' simulator options against the official simulator's own defaults (2026-11-20, the independent audit's check after the
Soul Shards: our warlock entries had never set soulShards, so every fight began with none; the hunter's quiver of 2026-11-04 was the
same kind). spec_check.py lists option names the protos lack; this lists values: per entry of specs.json, every field the simulator's
DefaultOptions for the entry's sim_spec (ui/specs/<sim_spec>/presets.ts) sets that the entry leaves at its zero value, and every field
both set to different values; then the player options the bench sets for every entry (reaction time, channel clip delay, distance,
professions) against the spec's OtherDefaults. Static: no simulator run.

    python _reference/data/raidsim/options_check.py [--repo PATH] [--write]

--write: _reference/options-check.md. A row is a real gap (a value we never chose) or a deliberate difference to write down."""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))


def strip_comments(s):
    s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
    return re.sub(r"(?m)//.*$", "", s)


def balanced(s, i):
    """The text of the bracketed block that opens at s[i] ('{', '(' or '[')."""
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for j in range(i, len(s)):
        c = s[j]
        if c in pairs:
            stack.append(pairs[c])
        elif stack and c == stack[-1]:
            stack.pop()
            if not stack:
                return s[i:j + 1]
    raise ValueError("unbalanced")


TOKEN = re.compile(r"\s*(?:(?P<str>'[^']*'|\"[^\"]*\")|(?P<num>-?\d+(?:\.\d+)?)|(?P<id>[A-Za-z_$][\w$.]*(?:\([^()]*\))?)|(?P<p>[{}\[\]:,]|\.\.\.))")


def parse_ts(src):
    """A TypeScript object literal as a dict: enum references keep their last name (WarlockOptions_Armor.DemonArmor -> DemonArmor),
    X.create({...}) becomes the object, other expressions their text."""
    toks = [m for m in TOKEN.finditer(src)]
    pos = 0

    def peek():
        return toks[pos] if pos < len(toks) else None

    def val():
        nonlocal pos
        t = toks[pos]
        if t.group("p") == "{":
            pos += 1
            out = {}
            while peek() and peek().group("p") != "}":
                k = toks[pos]
                if k.group("p") == "...":
                    pos += 1
                    out.setdefault("...", []).append(toks[pos].group(0).strip())
                    pos += 1
                else:
                    key = (k.group("id") or k.group("str") or k.group("num")).strip("'\"")
                    pos += 1
                    if peek() and peek().group("p") == ":":
                        pos += 1
                        out[key] = val()
                    else:
                        out[key] = key   # shorthand
                if peek() and peek().group("p") == ",":
                    pos += 1
            pos += 1
            return out
        if t.group("p") == "[":
            pos += 1
            out = []
            while peek() and peek().group("p") != "]":
                out.append(val())
                if peek() and peek().group("p") == ",":
                    pos += 1
            pos += 1
            return out
        pos += 1
        if t.group("str"):
            return t.group("str")[1:-1]
        if t.group("num"):
            x = float(t.group("num"))
            return int(x) if x.is_integer() else x
        ident = t.group("id")
        if ident in ("true", "false"):
            return ident == "true"
        if ident.endswith(".create") or ident.endswith(".create()"):
            if ident.endswith("()"):
                return {}
            # X.create({ ... })
            if peek() is not None and peek().group(0).strip() == "{":
                return val()
            return {}
        return ident.split(".")[-1]
    return val()


def defaults(repo, sim_spec):
    p = pathlib.Path(repo) / "ui" / "specs" / sim_spec / "presets.ts"
    if not p.exists():
        return None, None, None
    s = strip_comments(p.read_text(encoding="utf-8"))
    out = {}
    for name in ("DefaultOptions", "OtherDefaults"):
        m = re.search(r"export const " + name + r"\b[^=]*=\s*", s)
        if not m:
            out[name] = None
            continue
        i = m.end()
        m2 = re.match(r"[\w.]+\.create\(", s[i:])
        if m2:
            i = i + m2.end() - 1
            block = balanced(s, i)[1:-1].strip()
        else:
            block = balanced(s, i)
        out[name] = parse_ts(block) if block else {}
    return out["DefaultOptions"], out["OtherDefaults"], p


def snake_enum(v):
    """faster_attack_ii -> FasterAttackII, ancient_sinew_wrapped_lamina -> AncientSinewWrappedLamina."""
    romans = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}
    return "".join(w.upper() if w in romans else w.capitalize() for w in v.split("_"))


def camel(k):
    w = k.split("_")
    return w[0] + "".join(x.capitalize() for x in w[1:])


PLAYER_SIML = {"reaction_time": "reactionTimeMs", "channel_clip_delay": "channelClipDelay", "distance_from_target": "distanceFromTarget",
               "race": "race", "profession1": "profession1", "profession2": "profession2"}


def siml_defaults(repo, sim_spec):
    """The settings block of ui/specs/<sim_spec>/defaults.siml, or of the build file it uses: (class options, player options)."""
    d = pathlib.Path(repo) / "ui" / "specs" / sim_spec
    f = d / "defaults.siml"
    if not f.exists():
        return None, None
    text = f.read_text(encoding="utf-8")
    if "settings:" not in text:
        m = re.search(r'^use "([^"]+)"', text, re.M)
        if m and (d / m.group(1)).exists() and (d / m.group(1)).suffix == ".siml":
            text = (d / m.group(1)).read_text(encoding="utf-8")
    m = re.search(r"^settings:\n((?:[ \t]+.*\n?)+)", text, re.M)
    if not m:
        return {}, {}
    cls, pl = {}, {}
    depth = 0
    for line in m.group(1).splitlines():
        parts = line.split()
        opened = depth > 0 or "(" in line
        depth += line.count("(") - line.count(")")
        if not parts or opened:   # a healing_model(...) or other call, over one line or several: not an option
            continue
        k, vals = parts[0], parts[1:]
        if k == "in_front_of_target":
            pl["inFrontOfTarget"] = True
            continue
        if k in ("tanks",):   # the raid's tank assignment, not an option
            continue
        if k in PLAYER_SIML:
            v = vals[0] if vals else True
            if k in ("reaction_time", "channel_clip_delay"):
                v = "-".join(x.replace("ms", "") for x in vals)
                v = int(v) if v.isdigit() else v
            elif k == "distance_from_target":
                v = float(v) if "." in v else int(v)
            elif k == "race":
                v = "Race" + snake_enum(v)
            else:
                v = snake_enum(v)
            pl[PLAYER_SIML[k]] = v
        elif vals:
            v = vals[0]
            v = int(v) if v.isdigit() else snake_enum(v)
            cls[camel(k)] = v
        else:
            cls[camel(k)] = True
    return cls, pl


def legacy(opts):
    """The bench's translation of the fork's warlock options (foreverbench legacySpec): sacrificeSummon / pactSacrifice ->
    sacrificedDemon."""
    o = json.loads(json.dumps(opts))
    co = o.get("classOptions")
    if isinstance(co, dict):
        if co.pop("sacrificeSummon", False):
            if "summon" in co:
                co["sacrificedDemon"] = co["summon"]
            co["summon"] = "NoSummon"
        if "pactSacrifice" in co:
            co["sacrificedDemon"] = co.pop("pactSacrifice")
    return o


def zero(v):
    return v in (None, 0, 0.0, False, "", [], {}) or (isinstance(v, str) and v.endswith(("None", "Unknown")))


def leaves(d, prefix=""):
    if isinstance(d, dict):
        for k, v in d.items():
            if k == "...":
                continue
            yield from leaves(v, f"{prefix}.{k}" if prefix else k)
    else:
        yield prefix, d


def get(d, path):
    for k in path.split("."):
        if not isinstance(d, dict) or k not in d:
            return None
        d = d[k]
    return d


# What each kind of row is (2026-11-20, the audit's decisions on the first list; full raid, 3,000 fights, seeds 1 / 2): a real gap fixed,
# or a deliberate difference with its measured size. Keys: (class, field) first, then the field.
DECISIONS = {
    "soulShards": "real gap, fixed 2026-11-20: 32 in every warlock entry (Shadowburn spends one; upstream's Destruction package 800 -> 881)",
    ("warlock", "sacrificedDemon"): "deliberate (the audit's step-2 decisions per entry); the Destruction entries sacrifice the Imp: Forever's "
                                    "Imp gives +15% Shadow, and the Succubus is 5.9-10.1% worse on every Destruction build",
    ("warlock", "summon"): "deliberate: the audit's step-2 decisions per entry (one option set per page)",
    "preShadowform": "no gap: the raid rotation casts Shadowform before the pull",
    ("priest", "classOptions.armor"): "no effect: Forever's Inner Fire is armor only (1,395 armor, charges)",
    "startingRage": "deliberate: 0 (at 50: Fury +0.38% / +0.48%, Arms -0.09% / +0.12%)",
    "stanceSnapshot": "deliberate: no effect in our rotations (0.00%)",
    "assumeBleedActive": "real gap, fixed 2026-11-20 in the full raid only (raid_spec): Rend and Tear on a boss a warrior keeps bleeding, "
                         "+0.52% / +0.51% on the Feral pick; the dummies keep it off",
    ("hunter", "petUptime"): "deliberate: Lone Wolf and the melee build have no pet",
    ("hunter", "petAttackSpeed"): "deliberate: the 1.2 s cat (Faster Attack VI, 2026-11-04); upstream's Raptor at II -0.06% to -0.26%",
    "inFrontOfTarget": "real gap, fixed 2026-11-20: the tanks stand in front of the boss (in_front)",
    "reactionTimeMs": "deliberate: 200 ms (at 100 ms: at most +0.2% on six specs)",
    "channelClipDelay": "fixed 2026-11-20: 100 ms, upstream's (run.CLIP_MS; the bench had 50)",
    "distanceFromTarget": "deliberate: melee entries start in melee; a caster's distance moves only travel time (Frost 795.5 at 10 yd, "
                          "792.2 at 20, 792.7 at 28); frost-raid at 10 yd for Cone of Cold",
    "profession1": "deliberate: our professions (no profession bonus in the bench's sets)",
    "profession2": "deliberate: our professions (no profession bonus in the bench's sets)",
    "race": "deliberate: racials are off (WOW_FOREVER_NO_RACIALS=1)",
}


def decision(cls, field):
    short = field.split(".")[-1]
    return DECISIONS.get((cls, field)) or DECISIONS.get((cls, short)) or DECISIONS.get(field) or DECISIONS.get(short) or "open"


# the player options the bench sets for every entry (raidsim/foreverbench/main.go, run.py, apl_opt.py)
BENCH_PLAYER = {"reactionTimeMs": 200, "channelClipDelay": 100}   # run.CLIP_MS since 2026-11-20 (50 before)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo")
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    import run as R
    R.set_game("forever")
    repo = R.repo_path(argparse.Namespace(repo=a.repo))
    specs = json.load(open(HERE / "specs.json", encoding="utf-8"))
    rows_gap, rows_diff, rows_player, notes = [], [], [], []
    cache = {}
    for cls, ents in specs.items():
        if not isinstance(ents, dict):
            continue
        for e, ent in ents.items():
            if not isinstance(ent, dict) or "sim_spec" not in ent:
                continue
            ss = ent["sim_spec"]
            if ss not in cache:
                cache[ss] = defaults(repo, ss)
            dopt, other, src = cache[ss]
            if dopt is None and other is None:
                scls, spl = siml_defaults(repo, ss)
                if scls is None:
                    notes.append(f"{cls}/{e}: no defaults found for {ss}")
                    continue
                dopt, other = {"classOptions": scls}, spl
                notes.append(f"{cls}/{e}: {ss} keeps its defaults in defaults.siml (read: its settings block)")
            frag = R.raid_spec(ent) or {}   # the pages' setting: the full raid, with the entry's raid-only options
            ours = legacy(next(iter(frag.values()), {}).get("options", {}) if frag else {})
            for path, uv in leaves(dopt or {}):
                if zero(uv):
                    continue
                ov = get(ours, path)
                if zero(ov):
                    rows_gap.append((cls, e, ss, path, uv, ov))
                elif ov != uv:
                    rows_diff.append((cls, e, ss, path, uv, ov))
            pl = {"distanceFromTarget": ent.get("distance", 5), "profession1": ent.get("profession1", ""),
                  "profession2": ent.get("profession2", ""), "race": ent.get("race", "RaceHuman"),
                  "inFrontOfTarget": bool(ent.get("in_front", False)), **BENCH_PLAYER}
            for k, uv in (other or {}).items():
                ov = pl.get(k)
                if k in pl and ov != uv:
                    rows_player.append((cls, e, ss, k, uv, ov))
    lines = ["# Simulator options against the official simulator's defaults", "",
             "Generated by `_reference/data/raidsim/options_check.py` (2026-11-20, the independent audit's check after the Soul Shards). "
             "Per entry of `raidsim/specs.json`: the fields the official simulator's `DefaultOptions` for the entry's spec "
             "(`ui/specs/<sim_spec>/presets.ts`) sets that the entry leaves at its zero value, the fields both set differently, and the "
             "player options the bench sets for every entry against the spec's `OtherDefaults`. Static; no simulator run.", ""]

    def table(title, rows, cols):
        lines.extend([f"## {title}", ""])
        if not rows:
            lines.extend(["None.", ""])
            return
        lines.append("| " + " | ".join(cols + ["Decision"]) + " |")
        lines.append("|" + "---|" * (len(cols) + 1))
        for r in rows:
            lines.append("| " + " | ".join(str(x) if x not in (None, "") else "(unset)" for x in r) + " | " + decision(r[0], r[3]) + " |")
        lines.append("")
    table("Fields upstream sets that our entry leaves at zero", rows_gap, ["Class", "Entry", "Sim spec", "Field", "Upstream", "Ours"])
    table("Fields both set, to different values", rows_diff, ["Class", "Entry", "Sim spec", "Field", "Upstream", "Ours"])
    table("Player options (the bench's, for every entry) against OtherDefaults", rows_player, ["Class", "Entry", "Sim spec", "Option", "Upstream", "Ours"])
    if notes:
        lines.extend(["## Notes", ""] + [f"- {n}" for n in notes] + [""])
    srcs = sorted({str(pathlib.Path(v[2]).relative_to(repo)).replace("\\", "/") for v in cache.values() if v[2]})
    lines.append("Sources: " + ", ".join(f"`{s}`" for s in srcs) + f" at the pinned checkout ({repo}).")
    text = "\n".join(lines) + "\n"
    print(text)
    if a.write:
        (ROOT / "_reference" / "options-check.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
