"""Battle.net user login for the protected character data (gold), 2026-11-09 (user: "are you able to see the amount of gold on my
character?" ... "Yes" to setting up the login).

    python _reference/data/characters/bnet_login.py [--region us] [--port 8765] [--wait 1800]

Blizzard keeps gold in the protected profile, which needs the player's own authorization (OAuth authorization code, scope wow.profile),
not only the developer key. The developer client must list the redirect URL http://localhost:<port>/callback (develop.battle.net, the
client's settings). The script prints a login link, waits for the browser's redirect on localhost, trades the code for a token (valid
about 24 hours) and stores it in ~/.wow-forever-tools/blizzard-user-token.json (never in the repository). Then it reads the account
profile (/profile/user/wow) and, for each character it lists, the protected character document, and prints what it finds (gold included
when Blizzard serves it for Forever: untested).
"""
import argparse
import base64
import http.server
import json
import pathlib
import secrets
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bnet  # noqa: E402

TOKEN = pathlib.Path.home() / ".wow-forever-tools" / "blizzard-user-token.json"


def exchange(code, redirect):
    cid, sec = bnet.credentials()
    body = urllib.parse.urlencode({"grant_type": "authorization_code", "code": code, "redirect_uri": redirect}).encode()
    req = urllib.request.Request("https://oauth.battle.net/token", data=body,
                                 headers={"Authorization": "Basic " + base64.b64encode(f"{cid}:{sec}".encode()).decode(),
                                          "Content-Type": "application/x-www-form-urlencoded"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def get(region, tok, path, namespace):
    return bnet.get(region, tok, path, namespace)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--region", default="us")
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--wait", type=int, default=1800)
    a = ap.parse_args()
    redirect = f"http://localhost:{a.port}/callback"
    state = secrets.token_urlsafe(16)
    cid, _ = bnet.credentials()
    url = "https://oauth.battle.net/authorize?" + urllib.parse.urlencode(
        {"client_id": cid, "scope": "wow.profile", "redirect_uri": redirect, "response_type": "code", "state": state})
    got = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            ok = q.get("state", [""])[0] == state and "code" in q
            if ok:
                got["code"] = q["code"][0]
            self.send_response(200 if ok else 400)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(("Logged in. You can close this tab." if ok else "Login failed or expired: run the script again.").encode())

        def log_message(self, *args):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", a.port), H)
    srv.timeout = 5
    print(f"Open this link, log in to Battle.net and approve:\n{url}\n(waiting up to {a.wait // 60} minutes for {redirect})", flush=True)
    end = time.time() + a.wait
    while "code" not in got and time.time() < end:
        srv.handle_request()
    srv.server_close()
    if "code" not in got:
        sys.exit("no login within the wait")
    tok = exchange(got["code"], redirect)
    TOKEN.write_text(json.dumps({"access_token": tok["access_token"], "expires_at": time.time() + tok.get("expires_in", 86400) - 60,
                                 "scope": tok.get("scope")}, indent=1), encoding="utf-8")
    print(f"token saved to {TOKEN} (scope {tok.get('scope')})", flush=True)
    ns = f"profile-forever-{a.region}"
    st, acct = get(a.region, tok["access_token"], "/profile/user/wow", ns)
    print("account profile:", st, json.dumps(acct)[:600], flush=True)
    for wa in (acct.get("wow_accounts") or []) if st == 200 else []:
        for ch in wa.get("characters") or []:
            prot = (ch.get("protected_character") or {}).get("href")
            print("character:", ch.get("name"), ch.get("level"), "protected:", prot, flush=True)
            if prot:
                path = urllib.parse.urlparse(prot).path
                st2, js = get(a.region, tok["access_token"], path, ns)
                money = js.get("money") if st2 == 200 else None
                gold = f"{money // 10000}g {money // 100 % 100}s {money % 100}c" if isinstance(money, int) else None
                print("  protected:", st2, "gold:", gold, json.dumps(js)[:300], flush=True)


if __name__ == "__main__":
    main()
