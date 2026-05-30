import sqlite3

conn = sqlite3.connect(
    r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Database\uber_eats.db"
)

print("Database Created Successfully")

conn.close()