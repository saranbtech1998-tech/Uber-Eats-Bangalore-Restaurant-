import pandas as pd
import numpy as np

# Load Data
df = pd.read_csv(r"D:\DS_Projects\P2_Uber_Eats_Bangalore_Restaurant\Data\Uber_Eats_data.csv")

print("Original Shape:", df.shape)


# 1. Remove Duplicates

df.drop_duplicates(inplace=True)


# 2. Restaurant Name Cleaning

df["restaurant_name"] = (
    df["restaurant_name"]
    .astype(str)
    .str.strip()
)


# 3. Location Cleaning

df["location"] = (
    df["location"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)


# 4. Cuisine Cleaning

df["cuisines"] = (
    df["cuisines"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
)


# 5. Rating Normalization

df["rate"] = (
    df["rate"]
    .astype(str)
    .str.replace("/5", "", regex=False)
)

df["rate"] = df["rate"].replace(
    ["NEW", "-", "nan"],
    np.nan
)

df["rate"] = pd.to_numeric(
    df["rate"],
    errors="coerce"
)

df["rate"] = df["rate"].fillna(
    df["rate"].median()
)


# 6. Cost Standardization

df["approx_cost(for two people)"] = (
    df["approx_cost(for two people)"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["approx_cost(for two people)"] = pd.to_numeric(
    df["approx_cost(for two people)"],
    errors="coerce"
)

df["approx_cost(for two people)"] = (
    df["approx_cost(for two people)"]
    .fillna(df["approx_cost(for two people)"].median())
)


# 7. Online Order Cleaning

df["online_order"] = (
    df["online_order"]
    .astype(str)
    .str.strip()
    .str.title()
)


# 8. Book Table Cleaning

df["book_table"] = (
    df["book_table"]
    .astype(str)
    .str.strip()
    .str.title()
)

# 9. Price Segment Feature

def get_price_segment(cost):
    if cost < 500:
        return "Low"
    elif cost < 1000:
        return "Mid"
    else:
        return "Premium"

df["price_segment"] = (
    df["approx_cost(for two people)"]
    .apply(get_price_segment)
)

# 10. Rating Category Feature

def get_rating_category(rate):
    if rate >= 4.5:
        return "Excellent"
    elif rate >= 4.0:
        return "Good"
    elif rate >= 3.0:
        return "Average"
    else:
        return "Poor"

df["rating_category"] = (
    df["rate"]
    .apply(get_rating_category)
)

# Validation

print("\nFinal Shape:", df.shape)
print("\nMissing Values:")
print(df.isnull().sum())

print("\nPrice Segments:")
print(df["price_segment"].value_counts())

print("\nRating Categories:")
print(df["rating_category"].value_counts())


# Save Clean Data

df.to_csv(
    "data/restaurants_cleaned.csv",
    index=False
)

print("\nCleaned file saved successfully.")