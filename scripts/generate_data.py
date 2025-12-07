import os
import random
from datetime import datetime, timedelta

statuses = ['PENDING', 'SHIPPED', 'DELIVERED', 'CANCELLED']

def generate_timestamp():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + timedelta(days=random_number_of_days)
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

os.makedirs('sql', exist_ok=True)
out_path = os.path.join('sql', 'seed_data.sql')

with open(out_path, 'w') as f:
    f.write("INSERT INTO app.order (order_id, customer_order_id, order_status, order_purchase_timestamp) VALUES\n")
    values = []
    for i in range(1000):
        order_id = f"ORD-{1000+i}"
        cust_id = f"CUST-{random.randint(1000, 9999)}"
        status = random.choice(statuses)
        ts = generate_timestamp()
        values.append(f"('{order_id}', '{cust_id}', '{status}', '{ts}')")

    f.write(",\n".join(values))
    f.write(";\n")

print(f"Generated {out_path} with 1000 rows.")
