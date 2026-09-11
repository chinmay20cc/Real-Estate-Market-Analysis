import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
DATA_PATH = "data/processed/cleaned_properties.csv"
OUTPUT_DIR = "reports/charts"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

print("Dataset loaded:", df.shape)


# 1. Price Distribution
plt.figure(figsize=(10, 6))
plt.hist(df["price"], bins=30)
plt.title("Property Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Properties")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_price_distribution.png", dpi=300)
plt.close()


# 2. Average Price by City
city_price = df.groupby("city")["price"].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
city_price.plot(kind="bar")
plt.title("Average Property Price by City")
plt.xlabel("City")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_average_price_by_city.png", dpi=300)
plt.close()


# 3. Property Type Distribution
property_counts = df["property_type"].value_counts()

plt.figure(figsize=(8, 6))
property_counts.plot(kind="bar")
plt.title("Property Type Distribution")
plt.xlabel("Property Type")
plt.ylabel("Number of Properties")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_property_type_distribution.png", dpi=300)
plt.close()


# 4. Average Price by Property Type
type_price = df.groupby("property_type")["price"].mean().sort_values(ascending=False)

plt.figure(figsize=(8, 6))
type_price.plot(kind="bar")
plt.title("Average Price by Property Type")
plt.xlabel("Property Type")
plt.ylabel("Average Price")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_average_price_by_property_type.png", dpi=300)
plt.close()


# 5. Area vs Price
plt.figure(figsize=(10, 6))
plt.scatter(df["area_sqft"], df["price"], alpha=0.6)
plt.title("Area vs Property Price")
plt.xlabel("Area (Sq Ft)")
plt.ylabel("Price")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_area_vs_price.png", dpi=300)
plt.close()


# 6. Average Price per Sq Ft by Property Type
price_sqft_type = (
    df.groupby("property_type")["price_per_sqft"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))
price_sqft_type.plot(kind="bar")
plt.title("Average Price per Sq Ft by Property Type")
plt.xlabel("Property Type")
plt.ylabel("Average Price per Sq Ft")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/06_price_per_sqft_by_property_type.png", dpi=300)
plt.close()


# 7. Bedrooms vs Average Price
bedroom_price = df.groupby("bedrooms")["price"].mean().sort_index()

plt.figure(figsize=(10, 6))
bedroom_price.plot(kind="bar")
plt.title("Average Property Price by Number of Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Average Price")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/07_bedrooms_vs_price.png", dpi=300)
plt.close()


# 8. Furnishing vs Average Price
furnishing_price = (
    df.groupby("furnishing")["price"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))
furnishing_price.plot(kind="bar")
plt.title("Average Property Price by Furnishing")
plt.xlabel("Furnishing")
plt.ylabel("Average Price")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/08_furnishing_vs_price.png", dpi=300)
plt.close()


# 9. Pool vs Average Price
pool_price = (
    df.groupby("has_pool")["price"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))
pool_price.plot(kind="bar")
plt.title("Average Property Price by Pool Availability")
plt.xlabel("Has Pool")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/09_pool_vs_price.png", dpi=300)
plt.close()


# 10. Build Year vs Average Price
year_price = df.groupby("build_year")["price"].mean().sort_index()

plt.figure(figsize=(12, 6))
year_price.plot(kind="line", marker="o")
plt.title("Average Property Price by Build Year")
plt.xlabel("Build Year")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/10_build_year_vs_price.png", dpi=300)
plt.close()


print("Successfully generated 10 charts.")
print("Saved to:", OUTPUT_DIR)