#!/usr/bin/env bash
set -euo pipefail
export PATH=$PATH:$(go env GOPATH)/bin

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CODELAB_DIR="$SCRIPT_DIR/content-creation-studio-adk"
DOCS_DIR="$SCRIPT_DIR/docs"

cd "$SCRIPT_DIR"
claat export codelab.md

python3 "$SCRIPT_DIR/scripts/inject_about.py" "$CODELAB_DIR/index.html"

mkdir -p "$DOCS_DIR"
cp -r "$CODELAB_DIR/." "$DOCS_DIR/"

echo "✅ Export complete → $DOCS_DIR"
