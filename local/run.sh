#!/usr/bin/env bash
# One bot job on Taylor's PC (Oct 24, Taylor: "set it up on my pc"): the same steps as the GitHub workflow of
# the same name, on an exact-minute timer (systemd, see install.sh). Usage: run.sh v2 | actor | queue
# State still lives in the GitHub repo: every run starts from origin/main and pushes what it changed, so
# the checks, notes and handoff doc keep working, and GitHub's own workflows can take over at any time.
set -u
JOB="${1:?usage: run.sh v2|actor|queue}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR" || exit 1
PY="$DIR/.venv/bin/python"
LOG="$DIR/local/logs"; mkdir -p "$LOG"
exec >>"$LOG/$JOB.log" 2>&1
echo "=== $(date -u +%FT%TZ) $JOB"
# one job at a time (the workflows' shared concurrency group); wait up to 4 minutes for the one before
exec 9>"$DIR/local/.lock"
flock -w 240 9 || { echo "busy: skipped"; exit 0; }
git fetch -q origin main && git reset -q --hard origin/main || { echo "git fetch failed"; exit 1; }
paused() {   # Taylor's /pause: an open issue labelled merc-paused (public repo: no login needed)
  n=$(curl -s --max-time 15 "https://api.github.com/repos/7178543-collab/merc/issues?labels=merc-paused&state=open" \
      | "$PY" -c 'import json,sys; print(len(json.load(sys.stdin)))' 2>/dev/null || echo 0)
  [ "$n" != "0" ]
}
save() {
  git add -f "$@" 2>/dev/null
  git diff --cached --quiet && return 0
  git -c user.name=merc-bot -c user.email=merc-bot@users.noreply.github.com commit -q -m "$MSG $(date -u +%Y-%m-%dT%H:%MZ) (pc)"
  for i in 1 2 3; do git pull -q --rebase -X theirs origin main && git push -q origin HEAD:main && return 0; git rebase --abort 2>/dev/null; sleep 5; done
  echo "push failed"; return 1
}
case "$JOB" in
  v2)
    timeout 300 "$PY" v2/shadow.py || true
    if paused; then echo "PAUSED - v2 act skipped"; else timeout 240 "$PY" v2/act.py --live || true; fi
    MSG="v2 shadow"; save state/v2 state/order_queue_done.jsonl ;;
  actor)
    if paused; then echo "PAUSED - actor skipped"; else
      timeout 300 "$PY" merc_actor.py --live --quiet || true
      timeout 120 "$PY" chain_balancer.py --live || true
    fi
    timeout 120 "$PY" failsafe.py --live || true
    timeout 120 "$PY" alerts.py --live || true
    timeout 120 "$PY" scorecard.py --live || true
    MSG="history"; save history state ;;
  queue)
    timeout 180 "$PY" order_queue.py --live || true
    timeout 120 "$PY" failsafe.py --live || true
    timeout 120 "$PY" prestige_rules.py --live || true
    timeout 120 "$PY" contracts.py --fill || true
    timeout 60 "$PY" payoff.py || true
    MSG="order queue applied"; save state ;;
  *) echo "unknown job $JOB"; exit 2 ;;
esac
echo "--- done $(date -u +%TZ)"
