import pandas as pd
import json
import sqlite3

# Read JSON
with open(
    r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Data\orders.json",
    "r",
    encoding="utf-8"
) as f:
    data = json.load(f)

# Convert to DataFrame
orders_df = pd.DataFrame(data)

# Connect Database
conn = sqlite3.connect(
    r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Database\uber_eats.db"
)

# Load into SQLite
orders_df.to_sql(
    "orders",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Orders Loaded Successfully")