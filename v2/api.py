"""Bot v2 API client. One place for every game request.

- Credentials from API_USER/API_TOKEN env vars or ~/.merc_creds (same as v1). Never logged.
- Never exits the process: every call returns a value or None, and records the error.
- Retries a turn change ("preparing next game-turn") and transient network errors.
- Read-only unless allow_writes() was called (shadow mode never calls it).
"""
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://play.mercatorio.io/api"
CREDS = os.path.expanduser("~/.merc_creds")

_user, _token = os.environ.get("API_USER"), os.environ.get("API_TOKEN")
if not (_user and _token) and os.path.exists(CREDS):
    try:
        with open(CREDS) as f:
            _d = json.load(f)
        _user, _token = _d.get("user"), _d.get("token")
    except (OSError, ValueError):
        pass

_writes = False
errors = []          # (method, path, status, message) for the run report
calls = {"GET": 0, "write": 0}


def ready():
    return bool(_user and _token)


def allow_writes():
    """Live mode only. Shadow mode never calls this, so no request can change the game."""
    global _writes
    _writes = True


def _request(method, path, body=None, tries=3):
    if not ready():
        errors.append((method, path, None, "no credentials"))
        return False, None, None
    data = json.dumps(body, default=str).encode() if body is not None else None
    headers = {"X-Merc-User": _user, "Authorization": "Bearer " + _token, "Accept": "application/json"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(BASE + path, data=data, method=method, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                text = r.read().decode()
            if "preparing next game-turn" in text:
                last = (None, "turn in progress")
                time.sleep(8)
                continue
            try:
                return True, r.status, json.loads(text) if text else None
            except ValueError:
                return True, r.status, text
        except urllib.error.HTTPError as e:
            msg = e.read().decode()[:300]
            if e.code in (502, 503, 504) or "preparing next game-turn" in msg:
                last = (e.code, msg)
                time.sleep(5 * (attempt + 1))
                continue
            errors.append((method, path, e.code, msg))
            return False, e.code, msg
        except Exception as e:      # network: retry
            last = (None, "%s: %s" % (type(e).__name__, e))
            time.sleep(3 * (attempt + 1))
    errors.append((method, path, last[0] if last else None, last[1] if last else "failed"))
    return False, last[0] if last else None, None


def get(path):
    calls["GET"] += 1
    ok, status, data = _request("GET", path)
    return data if ok else None


def write(method, path, body):
    """PUT/PATCH/POST. Refused (returns False) unless allow_writes() was called."""
    if not _writes:
        errors.append((method, path, None, "refused: shadow mode is read-only"))
        return False, None, "shadow mode"
    calls["write"] += 1
    # PATCH/PUT send the whole wanted state, so a retry after a turn change or a 5xx can't double anything; POST can
    return _request(method, path, body, tries=3 if method in ("PATCH", "PUT") else 1)


def q(item):
    return urllib.parse.quote(item, safe="")
