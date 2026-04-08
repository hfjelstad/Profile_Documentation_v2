#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────
# validate-xml.sh — Local NeTEx XML validation (mirrors CI)
#
# Usage:
#   ./scripts/validate-xml.sh                 # validate all XML
#   ./scripts/validate-xml.sh --changed       # validate only git-changed XML
#   ./scripts/validate-xml.sh file1.xml ...   # validate specific files
# ─────────────────────────────────────────────────────────────
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCHEMA_DIR="$REPO_ROOT/netex-xsd/xsd"
SCHEMA_FILE="$SCHEMA_DIR/NeTEx_publication.xsd"

# ── Check xmllint ──
if ! command -v xmllint &>/dev/null; then
  echo "ERROR: xmllint not found."
  echo "  Install: sudo apt-get install libxml2-utils   (Linux)"
  echo "           brew install libxml2                  (macOS)"
  echo "           choco install xsltproc                (Windows)"
  exit 2
fi

# ── Ensure schema is available ──
if [ ! -f "$SCHEMA_FILE" ]; then
  echo "Schema not found locally. Cloning from official NeTEx repo..."
  (
    cd "$REPO_ROOT"
    git clone --depth=1 https://github.com/NeTEx-CEN/NeTEx.git netex-xsd 2>/dev/null
  )
  if [ ! -f "$SCHEMA_FILE" ]; then
    echo "ERROR: Could not obtain schema at: $SCHEMA_FILE"
    exit 2
  fi
  echo "Schema cloned from https://github.com/NeTEx-CEN/NeTEx"
  echo ""
fi

SCHEMA_ABS="$(realpath "$SCHEMA_FILE")"

# ── Collect files to validate ──
FILES=()

if [ $# -eq 0 ]; then
  # Default: validate all XML under Objects/ and Frames/
  while IFS= read -r -d '' f; do
    FILES+=("$f")
  done < <(find "$REPO_ROOT/Objects" "$REPO_ROOT/Frames" -name '*.xml' -print0 2>/dev/null)

elif [ "$1" = "--changed" ]; then
  # Only git-changed XML files
  cd "$REPO_ROOT"
  BASE="${2:-EnStandardBranch}"
  git fetch origin "$BASE" --depth=1 2>/dev/null || true
  MB=$(git merge-base HEAD "origin/$BASE" 2>/dev/null || echo "")

  if [ -z "$MB" ]; then
    echo "Could not determine merge-base with $BASE. Validating all XML instead."
    while IFS= read -r -d '' f; do
      FILES+=("$f")
    done < <(find "$REPO_ROOT/Objects" "$REPO_ROOT/Frames" -name '*.xml' -print0 2>/dev/null)
  else
    while IFS= read -r -d '' f; do
      [[ "${f,,}" == *.xml ]] || continue
      [[ "$f" == "netex-xsd/"* ]] && continue
      [ -f "$REPO_ROOT/$f" ] || continue
      FILES+=("$REPO_ROOT/$f")
    done < <(git diff --name-only -z "$MB" HEAD)
  fi

else
  # Specific files passed as arguments
  for f in "$@"; do
    if [ -f "$f" ]; then
      FILES+=("$f")
    else
      echo "WARNING: File not found: $f"
    fi
  done
fi

if [ ${#FILES[@]} -eq 0 ]; then
  echo "No XML files to validate."
  exit 0
fi

echo "Validating ${#FILES[@]} XML file(s) against NeTEx schema..."
echo ""

# ── Validate ──
PASS=0
FAIL=0
FAILED_FILES=()

for file in "${FILES[@]}"; do
  REL="${file#"$REPO_ROOT/"}"
  if xmllint --schema "$SCHEMA_ABS" --noout "$file" 2>/dev/null; then
    echo "  ✅ $REL"
    ((PASS++))
  else
    echo "  ❌ $REL"
    # Show error details
    xmllint --schema "$SCHEMA_ABS" --noout "$file" 2>&1 | grep -i 'error' | head -5 | sed 's/^/     /'
    ((FAIL++))
    FAILED_FILES+=("$REL")
  fi
done

echo ""
echo "────────────────────────────────"
echo "  Results: $PASS passed, $FAIL failed"
echo "────────────────────────────────"

if [ $FAIL -gt 0 ]; then
  echo ""
  echo "Failed files:"
  for f in "${FAILED_FILES[@]}"; do
    echo "  - $f"
  done
  exit 1
fi

exit 0
