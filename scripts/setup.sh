#!/usr/bin/env bash
set -euo pipefail

# Simple setup script: start DB, generate data, load data, install deps, run validation

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

POSTGRES_USER=${POSTGRES_USER:-sde}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-password}
POSTGRES_DB=${POSTGRES_DB:-data_quality}

echo "--- Starting PostgreSQL ---"
if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
  docker compose up -d
else
  # Fallback: run container directly
  if docker ps -a --format '{{.Names}}' | grep -q '^pg_local$'; then
    echo "pg_local exists, starting container..."
    docker start pg_local || true
  else
    echo "Creating pg_local container..."
    docker run -d --name pg_local -p 5432:5432 \
      -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" \
      -e POSTGRES_DB="$POSTGRES_DB" -v postgres_data:/var/lib/postgresql/data \
      postgres:12.2
  fi
fi

echo "Waiting for PostgreSQL to accept connections..."
for i in {1..30}; do
  if docker exec pg_local pg_isready -U "$POSTGRES_USER" >/dev/null 2>&1; then
    echo "Postgres is ready"
    break
  fi
  sleep 1
done

echo "--- Generating seed data ---"
python3 scripts/generate_data.py

echo "--- Loading schema and seed data ---"
cat sql/setup_db.sql sql/seed_data.sql | docker exec -i pg_local psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"

echo "--- Installing Python dependencies ---"
python3 -m pip install -r requirements.txt

echo "--- Running Great Expectations validation ---"
python3 src/examples/simple_ge_example.py

echo "--- Done ---"
