import great_expectations as gx
from great_expectations.core.expectation_suite import ExpectationSuite

# 1. Get Context
context = gx.get_context(mode="file")

# 2. Add Datasource (Postgres)
datasource_name = "my_postgres_datasource"
connection_string = "postgresql+psycopg2://sde:password@localhost:5432/data_quality"

try:
    datasource = context.data_sources.add_postgres(
        name=datasource_name,
        connection_string=connection_string
    )
except Exception:
    datasource = context.data_sources.get(datasource_name)

# 3. Add Asset (Table)
asset_name = "app_order_asset"
table_name = "order"
schema_name = "app"

try:
    asset = datasource.add_table_asset(name=asset_name, table_name=table_name, schema_name=schema_name)
except Exception:
    asset = datasource.get_asset(asset_name)

# 4. Create Expectation Suite
suite_name = "my_suite"
try:
    suite = context.suites.get(suite_name)
except Exception:
    suite = context.suites.add(ExpectationSuite(name=suite_name))

# 5. Define Expectations
batch_request = asset.build_batch_request()
validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name=suite_name
)

# EXPECTATION 1: Table row count should be exactly 1000
validator.expect_table_row_count_to_equal(1000)

# EXPECTATION 2: order_id should not be null
validator.expect_column_values_to_not_be_null(column="order_id")

# EXPECTATION 3: order_status should be in the known set
known_statuses = ["PENDING", "SHIPPED", "DELIVERED", "CANCELLED"]
validator.expect_column_values_to_be_in_set(column="order_status", value_set=known_statuses)

# 6. Save Suite
# validator.save_expectation_suite() might fail if it exists, so let's force update
try:
    context.suites.delete(suite_name)
except Exception:
    pass
context.suites.add(validator.expectation_suite)

# 7. Run Validation (Directly via Checkpoint or Validator)
# For simplicity in this demo, let's look at the validator's auto-generated result for the last run expectation,
# but to do a full run we can define a checkpoint.

# 7. Run Validation
print("\n--- Running Validation ---")
results = validator.validate()

# 8. Print Results
success = results.success
print(f"\nValidation Success: {success}")
print("-" * 30)

for result in results.results:
    # Handle attribute access safely for different GX versions
    config = result.expectation_config
    exp_type = getattr(config, "expectation_type", getattr(config, "type", "Unknown"))
    success = result.success
    print(f"Expectation: {exp_type:40} | Success: {success}")

