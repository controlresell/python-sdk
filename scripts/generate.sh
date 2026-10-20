#!/usr/bin/env bash
# Regenerates the client from the OpenAPI document of the ControlResell public API.
#
#   scripts/generate.sh [spec]   # a file or a URL; default: https://api.controlresell.com/api/public/openapi.json
#
# Writes src/controlresell/generated and .spec-sha256. The document itself is not committed.
# Needs uv (https://docs.astral.sh/uv/).
set -euo pipefail

GENERATOR_VERSION=0.29.1
SPEC="${1:-https://api.controlresell.com/api/public/openapi.json}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

case "$SPEC" in
  http://*|https://*) curl -fsSL -o "$WORK/openapi.json" "$SPEC" ;;
  *) cp "$SPEC" "$WORK/openapi.json" ;;
esac

cat > "$WORK/config.yml" <<'YAML'
package_name_override: generated
YAML

uvx --from "openapi-python-client==$GENERATOR_VERSION" openapi-python-client generate \
  --path "$WORK/openapi.json" \
  --config "$WORK/config.yml" \
  --meta none \
  --output-path "$WORK/out" \
  > "$WORK/generate.log"

TARGET="$ROOT/src/controlresell/generated"
rm -rf "$TARGET"
cp -R "$WORK/out" "$TARGET"
rm -rf "$TARGET/.ruff_cache"
find "$TARGET" -name __pycache__ -prune -exec rm -rf {} +

shasum -a 256 "$WORK/openapi.json" | cut -d' ' -f1 > "$ROOT/.spec-sha256"
echo "Generated from $SPEC (sha256 $(cat "$ROOT/.spec-sha256"))"
