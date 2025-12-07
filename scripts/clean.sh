#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "--- Cleaning Docker artifacts ---"
if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
  docker compose down -v
else
  docker stop pg_local 2>/dev/null || true
  docker rm pg_local 2>/dev/null || true
  docker volume rm postgres_data 2>/dev/null || true
fi

echo "--- Clean complete ---"
