#!/usr/bin/env bash
#
# publish_wiki.sh -- regenerate the GitHub Wiki mirror from docs/ and push it.
#
# The Wiki is a SEPARATE git repo (TLICA.wiki.git). This script does the git
# plumbing around scripts/build_wiki.py (the pure docs/ -> Wiki transform):
#   * clone the Wiki repo if present, else bootstrap a fresh one (first publish);
#   * regenerate every page from docs/ (build_wiki.py wipes stale *.md first);
#   * commit + push, stamping the source commit it was generated from.
#
# docs/ stays the source of truth (gated by `make validate`, atomic with code).
# Never hand-edit the Wiki: edit docs/ and run `make wiki`.
#
# Usage: publish_wiki.sh <wiki-remote> <build-dir> [--dry-run]
set -euo pipefail

REMOTE="${1:?usage: publish_wiki.sh <wiki-remote> <build-dir> [--dry-run]}"
BUILD="${2:?usage: publish_wiki.sh <wiki-remote> <build-dir> [--dry-run]}"
DRY="${3:-}"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC_SHA="$(git -C "$ROOT" rev-parse --short HEAD)"

# --- obtain a working copy of the Wiki repo (clone, or bootstrap if it does not exist) ---
if [ -d "$BUILD/.git" ]; then
  echo "publish_wiki: updating existing build clone at $BUILD"
  git -C "$BUILD" fetch --quiet origin
  git -C "$BUILD" reset --quiet --hard "origin/$(git -C "$BUILD" rev-parse --abbrev-ref HEAD)" || true
elif git clone --quiet "$REMOTE" "$BUILD" 2>/dev/null; then
  echo "publish_wiki: cloned Wiki repo into $BUILD"
else
  echo "publish_wiki: Wiki repo not found remotely -- bootstrapping a fresh one"
  rm -rf "$BUILD"
  mkdir -p "$BUILD"
  git -C "$BUILD" init --quiet
  git -C "$BUILD" remote add origin "$REMOTE"
fi

# GitHub Wikis use the 'master' branch; normalise to it.
git -C "$BUILD" checkout -q -B master

# --- regenerate the mirror ---
python3 "$ROOT/scripts/build_wiki.py" "$BUILD"

# --- commit + push ---
git -C "$BUILD" add -A
if git -C "$BUILD" diff --cached --quiet; then
  echo "publish_wiki: no changes to publish"
  exit 0
fi
git -C "$BUILD" -c user.name="femboy2112" -c user.email="vandettalm@gmail.com" \
  commit --quiet -m "docs(wiki): regenerate mirror from docs/ @ ${SRC_SHA}"

if [ "$DRY" = "--dry-run" ]; then
  echo "publish_wiki: --dry-run set; committed locally in $BUILD, NOT pushing"
  git -C "$BUILD" --no-pager show --stat HEAD | head -40
  exit 0
fi

git -C "$BUILD" push --quiet -u origin master
echo "publish_wiki: pushed Wiki mirror (generated from ${SRC_SHA})"
