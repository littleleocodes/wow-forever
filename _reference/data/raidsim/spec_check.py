"""Check every specs.json entry's `spec` fragment against the simulator's proto files (2026-11-04).

The bench reads the fragment with DiscardUnknown, so a field or enum value the official protos do not know is dropped without
a word (the bench prints a `spec:` warning on stderr, which the callers only showed when the bench failed). From the port of
2026-10-18 to 2026-11-04 the hunter entries sent the fork's `petAttackSpeed: "OneTwo"` and `quiverBonus: "Speed15"`: every hunter
raid number of that period ran a 2 s pet with no Faster Attack passive and no quiver haste. This parses the .proto files (messages,
nested messages, enums, oneofs, maps) and lists every key or enum string a fragment carries that the protos lack. Run it after every
re-pin and after editing an entry's `spec`. The fields the bench translates itself (`legacySpec` in foreverbench/main.go) are allowed.

Usage: python spec_check.py [--specs specs.json] [--repo <clone>] [--all-checkouts]
Exit status 1 when a problem is found.
"""
import argparse
import json
import os
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# Fork-era fields the bench maps onto the official protos before the simulator reads them (foreverbench/main.go legacySpec).
LEGACY_OK = {"sacrificeSummon", "pactSacrifice"}

SCALARS = {"double", "float", "int32", "int64", "uint32", "uint64", "sint32", "sint64", "fixed32", "fixed64",
           "sfixed32", "sfixed64", "bool", "string", "bytes"}

_field_re = re.compile(r"^\s*(?:(repeated|optional)\s+)?([A-Za-z_][\w.]*)\s+([a-z_][\w]*)\s*=\s*\d+")
_map_re = re.compile(r"^\s*map<\s*[\w.]+\s*,\s*([\w.]+)\s*>\s+([a-z_][\w]*)\s*=")
_enum_val_re = re.compile(r"^\s*([A-Za-z_][\w]*)\s*=\s*-?\d+")
_block_re = re.compile(r"^\s*(message|enum)\s+([A-Za-z_]\w*)\s*\{")


def camel(name):
    parts = name.split("_")
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


class Protos:
    """The messages (json field name -> type name) and enums (value names) of a proto directory."""

    def __init__(self, proto_dir):
        self.messages = {}
        self.enums = {}
        self.scopes = {}
        for fn in sorted(os.listdir(proto_dir)):
            if fn.endswith(".proto"):
                self._parse(pathlib.Path(proto_dir) / fn)

    def _parse(self, path):
        stack = []   # (kind, full name)
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.split("//")[0].rstrip()
            if not line.strip():
                continue
            m = _block_re.match(line)
            if m:
                kind, name = m.group(1), m.group(2)
                full = ".".join([s[1] for s in stack if s[0] != "oneof"] + [name])
                self.scopes[full] = stack[-1][1] if stack else ""
                (self.messages if kind == "message" else self.enums).setdefault(full, {} if kind == "message" else set())
                if not line.rstrip().endswith("{}"):   # `message Rotation {}` opens and closes on one line
                    stack.append((kind, full))
                continue
            if re.match(r"^\s*oneof\s+\w+\s*\{", line):
                stack.append(("oneof", stack[-1][1]))
                continue
            if line.strip().startswith("}"):
                if stack:
                    stack.pop()
                continue
            if not stack:
                continue
            kind, full = stack[-1]
            if kind == "enum":
                m = _enum_val_re.match(line)
                if m:
                    self.enums[full].add(m.group(1))
            else:
                m = _map_re.match(line)
                if m:
                    self.messages[full][camel(m.group(2))] = "map:" + m.group(1)
                    continue
                m = _field_re.match(line)
                if m and m.group(2) not in ("option", "reserved", "extensions"):
                    self.messages[full][camel(m.group(3))] = m.group(2)

    def resolve(self, type_name, scope):
        """A message or enum by name, looked up from a scope outward (proto nesting rules)."""
        parts = type_name.lstrip(".").split(".")
        if parts[0] == "proto":
            parts = parts[1:]
        cand = ".".join(parts)
        s = scope
        while True:
            full = (s + "." + cand) if s else cand
            if full in self.messages:
                return "message", full
            if full in self.enums:
                return "enum", full
            if not s:
                return None, type_name
            s = self.scopes.get(s, "")

    def check(self, obj, msg, path, problems):
        fields = self.messages[msg]
        if not isinstance(obj, dict):
            problems.append((path, "expected an object for " + msg))
            return
        for key, val in obj.items():
            if key not in fields:
                if key not in LEGACY_OK:
                    problems.append((path + "." + key, "unknown field in " + msg))
                continue
            tname = fields[key]
            if tname.startswith("map:") or tname in SCALARS:
                continue
            kind, full = self.resolve(tname, msg)
            if kind == "enum":
                for v in (val if isinstance(val, list) else [val]):
                    if isinstance(v, str) and v not in self.enums[full]:
                        problems.append((path + "." + key, "unknown value %r for enum %s (known: %s)" % (
                            v, full, ", ".join(sorted(self.enums[full])))))
            elif kind == "message":
                items = val if isinstance(val, list) else [val]
                for i, item in enumerate(items):
                    self.check(item, full, path + "." + key + ("[%d]" % i if isinstance(val, list) else ""), problems)
            else:
                problems.append((path + "." + key, "unresolved type " + tname))


def check_specs(specs, protos):
    """Every entry's spec fragment against proto.Player; returns (entries checked, [(path, problem)])."""
    problems, n = [], 0
    for cls, entries in specs.items():
        if not isinstance(entries, dict):
            continue
        for name, entry in entries.items():
            if isinstance(entry, dict) and isinstance(entry.get("spec"), dict):
                n += 1
                protos.check(entry["spec"], "Player", cls + "/" + name, problems)
    return n, problems


def default_repo():
    try:
        import setup   # noqa: E402  (raidsim/setup.py: the pinned clone, WOW_FOREVER_SIM honoured)
        return pathlib.Path(setup.checkout())
    except Exception:
        return pathlib.Path(os.environ.get("WOW_FOREVER_SIM") or pathlib.Path.home() / ".wow-forever-tools" / "wowsims-forever")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--specs", default=str(HERE / "specs.json"))
    ap.add_argument("--repo", help="a simulator clone (default: setup.checkout())")
    ap.add_argument("--all-checkouts", action="store_true", help="every wowsims-forever* clone under ~/.wow-forever-tools")
    a = ap.parse_args()
    specs = json.load(open(a.specs, encoding="utf-8"))
    if a.all_checkouts:
        tools = pathlib.Path.home() / ".wow-forever-tools"
        repos = sorted(p for p in tools.glob("wowsims-forever*") if (p / "proto").is_dir())
    else:
        repos = [pathlib.Path(a.repo) if a.repo else default_repo()]
    rc = 0
    for repo in repos:
        protos = Protos(repo / "proto")
        n, problems = check_specs(specs, protos)
        print(f"== {repo}: {n} entries against {len(protos.messages)} messages and {len(protos.enums)} enums: "
              + ("no unknown fields or enum values" if not problems else f"{len(problems)} problems"))
        for path, why in problems:
            print("   PROBLEM", path, "->", why)
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
