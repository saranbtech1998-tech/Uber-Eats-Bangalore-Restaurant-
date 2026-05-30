import streamlit as st
import pandas as pd
import sqlite3

# Page Config
st.set_page_config(
    page_title="Uber Eats Bangalore Analytics",
    layout="wide"
)

# Database Connection
conn = sqlite3.connect(
    r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Database\uber_eats.db"
)

# Load Data
df = pd.read_sql(
    "SELECT * FROM restaurants",
    conn
)

# Title
st.title("Uber Eats Bangalore Restaurant Analytics")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Restaurants",
    len(df)
)

col2.metric(
    "Average Rating",
    round(df["rate"].mean(), 2)
)

col3.metric(
    "Average Cost",
    round(df["approx_cost(for two people)"].mean(), 0)
)

col4.metric(
    "Locations",
    df["location"].nunique()
)

# Show Data
st.subheader("Restaurant Data")

st.dataframe(df.head(20))

conn.close()