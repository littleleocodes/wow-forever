"""Read and write scorer/kinds.json in its compact layout (one talent per line), for scripts that edit it."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
PATH = HERE / "kinds.json"


def load_kinds_file(path=PATH):
    from collections import OrderedDict
    return json.load(open(path, encoding="utf-8"), object_pairs_hook=OrderedDict)


def dump_kinds(d, path=PATH):
    lines = ["{", '  "_doc": ' + json.dumps(d["_doc"], ensure_ascii=False) + ",", '  "kinds": {']
    ks = list(d["kinds"].items())
    for i, (k, v) in enumerate(ks):
        lines.append(f'    "{k}": ' + json.dumps(v, ensure_ascii=False) + ("," if i < len(ks) - 1 else ""))
    lines += ["  },", '  "talents": {']
    cl = list(d["talents"].items())
    for i, (cls, tal) in enumerate(cl):
        lines.append(f'    "{cls}": {{')
        tl = list(tal.items())
        for j, (name, info) in enumerate(tl):
            lines.append("      " + json.dumps(name, ensure_ascii=False) + ": " + json.dumps(info, ensure_ascii=False) + ("," if j < len(tl) - 1 else ""))
        lines.append("    }" + ("," if i < len(cl) - 1 else ""))
    lines += ["  }", "}"]
    pathlib.Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")
