#!/usr/bin/env bash
set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"
cd "$(dirname "$0")/.."
python3 -m pytest -q
gatekeep suite
echo
echo "UI: run  gatekeep serve --port 8000  then open http://127.0.0.1:8000"
echo "See DEMO.md for the click path."
