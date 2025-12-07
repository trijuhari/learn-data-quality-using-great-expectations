# Learn Data Quality with Great Expectations

This project demonstrates how to set up a Data Quality playground using Docker, PostgreSQL, and Great Expectations.

## Project Structure

```
├── config/              # Configuration files
├── docs/                # Documentation
├── gx/                  # Great Expectations configurations
├── scripts/             # Utility scripts
│   ├── generate_data.py # Generates dummy seed data
│   └── init_gx.py       # Initializes GX data context
├── sql/                 # SQL Scripts
│   ├── setup_db.sql     # Database schema definition
│   └── seed_data.sql    # Generated seed data
├── src/                 # Source Code
│   └── examples/
│       └── simple_ge_example.py # GX validation example
├── docker-compose.yml   # Docker services configuration
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Setup

### 1. Prerequisites
- Docker & Docker Compose
- Python 3.8+

### 2. Start Database
```bash
docker compose up -d
```
This starts a PostgreSQL container named `pg_local` on port 5432.

### 3. Initialize Database
Create schema and seed data (1000 rows):
```bash
# Generate seed data script
python3 scripts/generate_data.py

# Apply schema and seed data
cat sql/setup_db.sql sql/seed_data.sql | docker exec -i pg_local psql -U sde -d data_quality
```

### 4. Install Python Dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Run Data Validation
Run the example script to validate the data in PostgreSQL using Great Expectations:
```bash
python3 src/examples/simple_ge_example.py
```

## Credentials
- **DB User**: `sde`
- **DB Password**: `password`
- **DB Name**: `data_quality`
