# Learn Data Quality with Great Expectations

A simple guide to learning data quality validation using Great Expectations, PostgreSQL, and Docker.

## ⚡ Quick Start (2 Minutes)

Copy and paste this:

```bash
# Start database
docker run -d --name pg_local -p 5432:5432 \
  -e POSTGRES_USER=sde -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=data_quality \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:12.2

sleep 5

# Setup data
python3 scripts/generate_data.py
cat sql/setup_db.sql sql/seed_data.sql | docker exec -i pg_local psql -U sde -d data_quality

# Run validation
pip install -r requirements.txt
python3 src/examples/simple_ge_example.py
```

✅ Done! You should see data quality validation results.

## What is this?

- **PostgreSQL Database** - Runs in Docker
- **1000 Sample Rows** - Auto-generated test data
- **Great Expectations** - Data quality validation framework
- **Simple Examples** - Ready-to-run validation script

## What You Need

- Docker ([Install](https://docs.docker.com/get-docker/))
- Python 3.8+ ([Install](https://www.python.org/downloads/))
- 2GB free disk space

## Project Structure

```
scripts/
  ├── generate_data.py      # Create sample data
  └── init_gx.py            # Initialize Great Expectations
sql/
  ├── setup_db.sql          # Create database schema
  └── seed_data.sql         # Insert sample data
src/examples/
  └── simple_ge_example.py  # Run this to validate data
gx/                         # Great Expectations config
docker-compose.yml          # Docker setup
requirements.txt            # Python packages
README.md                   # This file
```

## Main Commands

### Start the database
```bash
docker run -d --name pg_local -p 5432:5432 \
  -e POSTGRES_USER=sde -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=data_quality \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:12.2
```

### Generate fresh data
```bash
python3 scripts/generate_data.py
cat sql/setup_db.sql sql/seed_data.sql | docker exec -i pg_local psql -U sde -d data_quality
```

### Run data validation
```bash
python3 src/examples/simple_ge_example.py
```

### Stop everything
```bash
docker stop pg_local
docker rm pg_local
docker volume rm postgres_data
```

## Database Info

```
User:     sde
Password: password
Database: data_quality
Host:     localhost
Port:     5432
```

## Common Issues

### "Connection refused" error?
Wait longer for PostgreSQL to start:
```bash
sleep 10
python3 src/examples/simple_ge_example.py
```

### Port 5432 already in use?
```bash
docker stop pg_local
docker rm pg_local
```

### Need to reset?
```bash
docker stop pg_local
docker rm pg_local
docker volume rm postgres_data
# Then run Quick Start again
```

### Check if database is running?
```bash
docker ps
```

### See database logs?
```bash
docker logs pg_local
```

## What is Great Expectations?

Great Expectations helps you:
- ✅ Check data quality automatically
- ✅ Validate row counts and data types
- ✅ Catch data issues early
- ✅ Document data characteristics
- ✅ Generate quality reports

## Example Output

When you run the validation, you'll see:

```
Validation Success: True
------------------------------
Expectation: expect_table_row_count_to_equal    | Success: True
Expectation: expect_column_values_to_not_be_null | Success: True
Expectation: expect_column_values_to_be_in_set   | Success: True
```

## Learn More

- [Great Expectations](https://docs.greatexpectations.io/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [Docker](https://docs.docker.com/)

## License

MIT - Use this for learning!
