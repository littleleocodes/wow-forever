"""Is there a newer WoW: Forever beta client than the one our data comes from?

    python _reference/data/check_beta_build.py

Reads the client build the datamines currently show (talentsforever.com's data.json header, thewowdb.com's talent page
for one class) and compares it with `_reference/data/forever-talents/<class>.json["build"]`. Prints the verdict and, when a
newer build exists, the refresh command to run (`rebuild.py --refresh <date>-beta-<build>` does everything downstream).
Exit code 0 = up to date, 3 = newer build found, 1 = the sources could not be read.
"""
import datetime as dt
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import refresh_forever_talents as R  # noqa: E402

BUILD = re.compile(r"1\.60\.\d+\.(\d{5})")


def main():
    ours = json.load(open(HERE / "forever-talents" / "mage.json", encoding="utf-8")).get("build", "?")
    ours_n = int(BUILD.search(ours).group(1)) if BUILD.search(ours) else 0
    seen = {}
    try:
        tf = R.fetch(R.URL_TF)
        text = tf.decode("utf-8", "replace") if isinstance(tf, bytes) else str(tf)
        head = json.loads(text) if text.lstrip().startswith("{") else {}
        blob = json.dumps({k: v for k, v in head.items() if k in ("generated", "build", "client", "version", "patch")}) + text[:20000]
        m = BUILD.findall(blob)
        seen["talentsforever.com"] = (max(int(x) for x in m) if m else None, head.get("generated"))
    except Exception as e:
        seen["talentsforever.com"] = (None, f"error: {e}")
    try:
        wd = R.fetch(R.URL_WD.format(cls="mage"))
        text = wd.decode("utf-8", "replace") if isinstance(wd, bytes) else str(wd)
        m = BUILD.findall(text)
        seen["thewowdb.com"] = (max(int(x) for x in m) if m else None, None)
    except Exception as e:
        seen["thewowdb.com"] = (None, f"error: {e}")
    print(f"our data: build {ours}")
    newest = 0
    for src, (b, note) in seen.items():
        print(f"  {src}: " + (f"build 1.60.x.{b}" if b else "no build number found") + (f" ({note})" if note else ""))
        newest = max(newest, b or 0)
    if not any(b for b, _ in seen.values()):
        print("could not read the sources")
        return 1
    if newest > ours_n:
        name = f"{dt.date.today().isoformat()}-beta-{newest}"
        print(f"NEWER BUILD {newest} > {ours_n}: run  python _reference/data/rebuild.py --refresh {name} --jobs 5")
        return 3
    print("up to date: the datamines show no newer client build")
    return 0


if __name__ == "__main__":
    sys.exit(main())
