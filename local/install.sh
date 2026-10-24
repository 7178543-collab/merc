#!/usr/bin/env bash
# Sets the Mercatorio bot up on this Linux PC. Run as yourself (not root):
#   curl -fsSL https://raw.githubusercontent.com/7178543-collab/merc/main/local/install.sh | bash
# It asks for two things only you have: a GitHub deploy key (it makes one; you paste it into GitHub) and the game
# API login (kept in ~/.merc_creds, readable only by you; never sent anywhere but the game).
set -euo pipefail
DIR="$HOME/merc"
REPO="git@github.com:7178543-collab/merc.git"
KEY="$HOME/.ssh/merc_deploy"
say() { printf '\n== %s\n' "$*"; }
for c in git python3 curl flock systemctl ssh-keygen; do command -v "$c" >/dev/null || { echo "missing: $c (install it and run again)"; exit 1; }; done
python3 -c 'import venv' 2>/dev/null || { echo "missing: python3-venv (e.g. sudo apt install python3-venv / sudo pacman -S python)"; exit 1; }

say "1/5 GitHub deploy key (lets this PC save the bot's state to the repo)"
mkdir -p "$HOME/.ssh"; chmod 700 "$HOME/.ssh"
[ -f "$KEY" ] || ssh-keygen -q -t ed25519 -N "" -C "merc-bot@$(hostname)" -f "$KEY"
echo "Add this key at https://github.com/7178543-collab/merc/settings/keys -> Add deploy key,"
echo "title 'merc pc', tick 'Allow write access':"
echo; cat "$KEY.pub"; echo
read -r -p "Press Enter once it's added... " _ </dev/tty
export GIT_SSH_COMMAND="ssh -i $KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new"
ssh -T git@github.com 2>&1 | grep -qi "successfully authenticated" || { echo "GitHub didn't accept the key yet - check it was saved with write access, then run again"; exit 1; }

say "2/5 Getting the bot"
if [ -d "$DIR/.git" ]; then git -C "$DIR" fetch -q origin main && git -C "$DIR" reset -q --hard origin/main
else git clone -q --depth 50 "$REPO" "$DIR"; fi
git -C "$DIR" config core.sshCommand "ssh -i $KEY -o IdentitiesOnly=yes"
chmod +x "$DIR/local/run.sh"

say "3/5 Python packages (a private copy in $DIR/.venv)"
python3 -m venv "$DIR/.venv"
"$DIR/.venv/bin/pip" install -q --upgrade pip
"$DIR/.venv/bin/pip" install -q requests numpy scipy

say "4/5 Game login"
if [ -f "$HOME/.merc_creds" ]; then echo "already saved in ~/.merc_creds"; else
  read -r -p "Mercatorio API user: " U </dev/tty
  read -r -s -p "Mercatorio API token (hidden): " T </dev/tty; echo
  umask 077; printf '{"user": "%s", "token": "%s"}\n' "$U" "$T" > "$HOME/.merc_creds"; chmod 600 "$HOME/.merc_creds"
fi

say "5/5 Timers: planner :03, old rules :08 and :38, order queue :15 (every hour, exact minute)"
U="$HOME/.config/systemd/user"; mkdir -p "$U"
cat > "$U/merc@.service" <<UNIT
[Unit]
Description=Mercatorio bot job %i
After=network-online.target
[Service]
Type=oneshot
ExecStart=$DIR/local/run.sh %i
UNIT
mk() { cat > "$U/merc-$1.timer" <<UNIT
[Unit]
Description=Mercatorio bot $1
[Timer]
OnCalendar=$2
Unit=merc@$1.service
AccuracySec=10s
[Install]
WantedBy=timers.target
UNIT
}
mk v2 "*-*-* *:03:00"; mk actor "*-*-* *:08,38:00"; mk queue "*-*-* *:15:00"
systemctl --user daemon-reload
systemctl --user enable --now merc-v2.timer merc-actor.timer merc-queue.timer
loginctl enable-linger "$USER" 2>/dev/null || sudo loginctl enable-linger "$USER" || echo "(could not enable linger: timers run only while you're logged in)"

say "First run (planner) to check it all works"
"$DIR/local/run.sh" v2; tail -5 "$DIR/local/logs/v2.log"
echo
echo "Done. Timers:"; systemctl --user list-timers 'merc-*' --no-pager
echo "Logs: $DIR/local/logs/   Stop everything: systemctl --user disable --now merc-v2.timer merc-actor.timer merc-queue.timer"
echo "Keep the PC awake (no sleep/suspend) - GitHub stays as the backup when it's off."
