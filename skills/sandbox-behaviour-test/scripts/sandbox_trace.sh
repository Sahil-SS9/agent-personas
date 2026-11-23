#!/usr/bin/env bash
# Run one entry point of a third-party package inside a no-network bubblewrap
# sandbox, with canary credentials, under strace. Then summarise what it did.
#
# Usage: sandbox_trace.sh <package_dir> <out_dir> -- <command...>
#   e.g. sandbox_trace.sh ./pkg ./trace-out -- python3 scripts/run.py --help
#
# Needs: bwrap, strace, python3 (Linux). The package is mounted read-only at
# /pkg. HOME is a throwaway tmpfs holding canary credentials. All network
# namespaces are unshared, so connections fail and are still recorded as
# attempts. Exit code: 0 = no findings, 1 = findings, 2 = usage or tool error.
set -euo pipefail

if [[ $# -lt 4 || "$3" != "--" ]]; then
  sed -n '2,12p' "$0"; exit 2
fi
PKG=$(cd "$1" && pwd); OUT=$2; shift 3
for t in bwrap strace python3; do
  command -v "$t" >/dev/null || { echo "missing tool: $t" >&2; exit 2; }
done
mkdir -p "$OUT"
OUT=$(cd "$OUT" && pwd)
CANARY_HOME=$(mktemp -d "${TMPDIR:-/tmp}/sbx-home.XXXXXX")
trap 'rm -rf "$CANARY_HOME"' EXIT

# Canary marker: any appearance of it in output, writes or network calls means
# the package read a credential and moved it.
MARK="CANARY-$(python3 -c 'import secrets;print(secrets.token_hex(6))')"
mkdir -p "$CANARY_HOME/.ssh" "$CANARY_HOME/.aws" "$CANARY_HOME/.config/gh"
printf -- '-----BEGIN OPENSSH PRIVATE KEY-----\n%s\n-----END OPENSSH PRIVATE KEY-----\n' "$MARK" > "$CANARY_HOME/.ssh/id_ed25519"
printf '[default]\naws_access_key_id = AKIA%s\naws_secret_access_key = %s\n' "$MARK" "$MARK" > "$CANARY_HOME/.aws/credentials"
printf 'OPENAI_API_KEY=sk-%s\n' "$MARK" > "$CANARY_HOME/.env"
printf 'github.com:\n  oauth_token: ghp_%s\n' "$MARK" > "$CANARY_HOME/.config/gh/hosts.yml"
echo "$MARK" > "$OUT/canary-marker.txt"

set +e
timeout "${SANDBOX_TIMEOUT:-120}" strace -f -qq -s 512 \
  -e trace=%file,%network,%process,write,sendto,sendmsg \
  -o "$OUT/trace.log" \
  bwrap --unshare-all --die-with-parent --new-session \
    --ro-bind /usr /usr --symlink usr/lib /lib --symlink usr/lib64 /lib64 \
    --symlink usr/bin /bin --symlink usr/sbin /sbin \
    --ro-bind-try /etc/ssl /etc/ssl --ro-bind-try /etc/alternatives /etc/alternatives \
    --proc /proc --dev /dev --tmpfs /tmp \
    --bind "$CANARY_HOME" /home/sandbox \
    --setenv HOME /home/sandbox \
    --setenv AWS_ACCESS_KEY_ID "AKIA$MARK" \
    --setenv GITHUB_TOKEN "ghp_$MARK" \
    --ro-bind "$PKG" /pkg --chdir /pkg \
    "$@" >"$OUT/stdout.txt" 2>"$OUT/stderr.txt"
RC=$?
set -e
echo "$RC" > "$OUT/exit-code.txt"
# Files the package left in the throwaway home (persistence attempts).
(cd "$CANARY_HOME" && find . -type f -newer "$OUT/canary-marker.txt" -print) > "$OUT/home-writes.txt" || true
python3 "$(dirname "$0")/summarise_trace.py" "$OUT"
