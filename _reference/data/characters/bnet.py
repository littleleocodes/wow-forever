"""Blizzard's official character API for WoW: Forever characters (2026-11-09, user: "build folders/guides for my specific characters").

    python _reference/data/characters/bnet.py <name>-<surname> [--region us] [--out <folder>]

Credentials: `~/.wow-forever-tools/blizzard.json` ({"client_id", "client_secret"}: the user's Battle.net developer client; never in the
repository) or the environment variables BLIZZARD_CLIENT_ID / BLIZZARD_CLIENT_SECRET. Forever characters have a first name and a surname
instead of a realm, in the namespace profile-forever-<region> (community reports of 2026-11-05/06; the API is not documented for Forever
yet). A character is listed from level 10 and refreshed when it logs out. Writes the profile and its sub-documents (equipment,
professions, specializations, statistics) as JSON into --out (default: printed summary only).
"""
import argparse
import base64
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

CRED = pathlib.Path.home() / ".wow-forever-tools" / "blizzard.json"
PARTS = ["", "/equipment", "/professions", "/specializations", "/statistics", "/quests", "/quests/completed", "/reputations"]


def credentials():
    if os.environ.get("BLIZZARD_CLIENT_ID") and os.environ.get("BLIZZARD_CLIENT_SECRET"):
        return os.environ["BLIZZARD_CLIENT_ID"], os.environ["BLIZZARD_CLIENT_SECRET"]
    c = json.loads(CRED.read_text(encoding="utf-8"))
    return c["client_id"], c["client_secret"]


def token(region):
    cid, sec = credentials()
    req = urllib.request.Request("https://oauth.battle.net/token", data=b"grant_type=client_credentials",
                                 headers={"Authorization": "Basic " + base64.b64encode(f"{cid}:{sec}".encode()).decode(),
                                          "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["access_token"]


def get(region, tok, path, namespace):
    url = f"https://{region}.api.blizzard.com{path}?" + urllib.parse.urlencode({"namespace": namespace, "locale": "en_US"})
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        return e.code, {"error": body[:300]}


def fetch(slug, region="us"):
    """{part: (status, json)} for the character's profile and its sub-documents."""
    tok = token(region)
    ns = f"profile-forever-{region}"
    return {p or "profile": get(region, tok, f"/profile/wow/character/{slug.lower()}{p}", ns) for p in PARTS}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="<name>-<surname>, e.g. arcea-fizzlegan")
    ap.add_argument("--region", default="us")
    ap.add_argument("--out")
    a = ap.parse_args()
    res = fetch(a.slug, a.region)
    for part, (st, js) in res.items():
        keys = list(js.keys())[:12] if isinstance(js, dict) else type(js).__name__
        print(f"{part:16s} {st} {keys}")
    if a.out:
        out = pathlib.Path(a.out)
        out.mkdir(parents=True, exist_ok=True)
        for part, (st, js) in res.items():
            if st == 200:
                (out / f"{part.strip('/')}.json").write_text(json.dumps(js, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {out}")
    sys.exit(0 if res["profile"][0] == 200 else 1)


if __name__ == "__main__":
    main()
