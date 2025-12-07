# Learn Data Quality with Great Expectations

A hands-on guide to learning data quality validation using Great Expectations, PostgreSQL, and Docker.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/trijuhari/learn-data-quality-using-great-expectations.git
cd learn-data-quality-using-great-expectations

# Make scripts executable (first time only)
chmod +x scripts/*.sh

# Run automated setup
./scripts/setup.sh
```

**What this does:**
- Starts PostgreSQL in Docker
- Generates 1000 sample rows
- Loads schema and data
- Installs Python dependencies
- Runs Great Expectations validation

**To clean up:**
```bash
./scripts/clean.sh
```

## 📋 What You Need

- **Docker** ([Install](https://docs.docker.com/get-docker/))
- **Python 3.8+** ([Install](https://www.python.org/downloads/))
- **2GB free disk space**

## 📁 Project Structure

```
scripts/
  ├── setup.sh              # Automated setup script
  ├── clean.sh              # Cleanup script
  ├── generate_data.py      # Generate sample data
  └── init_gx.py            # Initialize Great Expectations
sql/
  ├── setup_db.sql          # Database schema
  └── seed_data.sql         # Sample data (auto-generated)
src/examples/
  └── simple_ge_example.py  # Data validation example
gx/                         # Great Expectations config
docker-compose.yml          # Docker configuration
requirements.txt            # Python dependencies
```

## 🔧 Manual Setup (Step-by-Step)

If you prefer to run commands manually:

### 1. Start PostgreSQL
```bash
docker run -d --name pg_local -p 5432:5432 \
  -e POSTGRES_USER=sde \
  -e POSTGRES_PASSWORD=password \
  -e POSTGRES_DB=data_quality \
  -v postgres_data:/var/lib/postgresql/data \
  postgres:12.2

# Wait for PostgreSQL to start
sleep 5
```

### 2. Generate and Load Data
```bash
python3 scripts/generate_data.py
cat sql/setup_db.sql sql/seed_data.sql | docker exec -i pg_local psql -U sde -d data_quality
```

### 3. Run Validation
```bash
pip install -r requirements.txt
python3 src/examples/simple_ge_example.py
```

## 🔑 Database Credentials

```
User:     sde
Password: password
Database: data_quality
Host:     localhost
Port:     5432
```

## ❓ Troubleshooting

### "Connection refused" error?
PostgreSQL may still be starting. Wait and retry:
```bash
sleep 10
python3 src/examples/simple_ge_example.py
```

### Port 5432 already in use?
Stop the conflicting container:
```bash
docker ps
docker stop <container_name>
```

### Need to reset everything?
```bash
./scripts/clean.sh
./scripts/setup.sh
```

### Check if database is running
```bash
docker ps
```

### View database logs
```bash
docker logs pg_local
```

## 💡 What is Great Expectations?

Great Expectations is a data quality framework that helps you:
- ✅ **Validate data automatically** - Check data quality with assertions
- ✅ **Catch issues early** - Detect problems before they reach production
- ✅ **Document data** - Create living documentation of your data
- ✅ **Generate reports** - Get detailed validation results

## 📊 Example Output

When you run the validation, you'll see:

```
Validation Success: True
------------------------------
Expectation: expect_table_row_count_to_equal    | Success: True
Expectation: expect_column_values_to_not_be_null | Success: True
Expectation: expect_column_values_to_be_in_set   | Success: True
```

## 📚 Learn More

- [Great Expectations Documentation](https://docs.greatexpectations.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Docker Documentation](https://docs.docker.com/)

## 📝 License

MIT - Use this for learning!
