#!/usr/bin/env bash
# Reconstruct the bible-sources corpus from pinned upstream commits.
# Usage: ./fetch.sh [--full-history]
set -euo pipefail
cd "$(dirname "$0")"
DEPTH="--depth 1"
[ "${1:-}" = "--full-history" ] && DEPTH=""
fail=0
while IFS=$'\t' read -r path remote commit; do
  case "$path" in ''|'#'*) continue;; esac
  if [ -d "$path/.git" ] || [ -f "$path/.pinned" ]; then
    echo "skip   $path"; continue
  fi
  echo "fetch  $path  <- $remote @ ${commit:0:8}"
  mkdir -p "$path"
  if ! git clone $DEPTH "$remote" "$path" 2>/dev/null; then
    echo "FAILED $path  ($remote)" >&2; fail=$((fail+1)); continue
  fi
  git -C "$path" fetch --depth 1 origin "$commit" 2>/dev/null && \
    git -C "$path" checkout -q "$commit" 2>/dev/null || \
    echo "  WARN: could not pin to $commit (using default branch tip)" >&2
  echo "$commit" > "$path/.pinned"
done < corpus.lock
if [ "$fail" -gt 0 ]; then echo "FAILED: $fail repo(s) did not clone" >&2; exit 1; fi
echo "OK: corpus reconstructed"
