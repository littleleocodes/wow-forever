"""Compact, readable JSON formatting for builds files.

Keeps short leaf lists (["Talent", 3]), order steps and string lists on one
line; everything else is indented normally.

Usage:  python _reference/data/fmt_json.py <file.json> [...]
"""
import json
import pathlib
import sys


def _inline(v) -> bool:
    if isinstance(v, list):
        return all(not isinstance(x, (list, dict)) for x in v)
    if isinstance(v, dict):
        return all(not isinstance(x, (list, dict)) for x in v.values()) and len(v) <= 5
    return True


def dumps(v, indent=0) -> str:
    pad = " " * indent
    if isinstance(v, dict):
        if not v:
            return "{}"
        if _inline(v):
            return "{" + ", ".join(f"{json.dumps(k, ensure_ascii=False)}: {json.dumps(x, ensure_ascii=False)}" for k, x in v.items()) + "}"
        items = [f'{pad}  {json.dumps(k, ensure_ascii=False)}: {dumps(x, indent + 2)}' for k, x in v.items()]
        return "{\n" + ",\n".join(items) + f"\n{pad}}}"
    if isinstance(v, list):
        if not v:
            return "[]"
        if _inline(v):
            return json.dumps(v, ensure_ascii=False)
        items = [f"{pad}  {dumps(x, indent + 2)}" for x in v]
        return "[\n" + ",\n".join(items) + f"\n{pad}]"
    return json.dumps(v, ensure_ascii=False)


def format_file(path: pathlib.Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    path.write_text(dumps(data) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        format_file(pathlib.Path(p))
        print("formatted", p)
