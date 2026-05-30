import pandas as pd
import sqlite3

df = pd.read_csv(
    r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Data\restaurants_cleaned.csv"
)

conn = sqlite3.connect(
    r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Database\uber_eats.db"
)

df.to_sql(
    "restaurants",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Restaurants Loaded Successfully")