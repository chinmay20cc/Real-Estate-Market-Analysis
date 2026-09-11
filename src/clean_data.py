import pandas as pd
import numpy as np
import os

RAW_PATH = "data/raw/house_prices.csv"
OUT_PATH = "data/processed/cleaned_properties.csv"


def main():

    # Load raw data
    df = pd.read_csv(RAW_PATH)

    print(f"Loaded raw data: {df.shape}")

    # Standardize column names
    df = df.rename(columns={
        "Area_SqFt": "area_sqft",
        "Rooms": "bedrooms",
        "Build_Year": "build_year",
        "Location": "city",
        "Street_Type": "street_type",
        "Furnishing": "furnishing",
        "Property_Type": "property_type",
        "Has_Pool": "has_pool",
        "Price": "price"
    })

    # Handle missing values
    before = len(df)

    df = df.dropna(subset=["price", "area_sqft"])

    print(f"Dropped {before - len(df)} rows missing price/area")

    df["bedrooms"] = df["bedrooms"].fillna(df["bedrooms"].median())
    df["furnishing"] = df["furnishing"].fillna("Unknown")

    # Remove duplicates
    before = len(df)

    df = df.drop_duplicates()

    print(f"Removed {before - len(df)} duplicate rows")

    # Type cleanup
    df["bedrooms"] = df["bedrooms"].round().astype(int)
    df["build_year"] = df["build_year"].astype(int)
    df["area_sqft"] = df["area_sqft"].round(2)
    df["price"] = df["price"].round(2)

    # Remove impossible values
    df = df[
        (df["price"] > 0) &
        (df["area_sqft"] > 0) &
        (df["bedrooms"] > 0)
    ]

    # Flag price outliers using IQR
    Q1, Q3 = df["price"].quantile([0.25, 0.75])

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df["is_price_outlier"] = ~df["price"].between(lower, upper)

    print(
        f"Flagged {df['is_price_outlier'].sum()} price outliers"
    )

    # Feature engineering
    df["price_per_sqft"] = (
        df["price"] / df["area_sqft"]
    ).round(2)

    df["property_age"] = (
        2026 - df["build_year"]
    ).clip(lower=0)

    df["area_bucket"] = pd.cut(
        df["area_sqft"],
        bins=[
            0,
            1000,
            1500,
            2000,
            2500,
            3000,
            np.inf
        ],
        labels=[
            "<1000",
            "1000-1500",
            "1500-2000",
            "2000-2500",
            "2500-3000",
            "3000+"
        ]
    )

    # Luxury property definition
    luxury_threshold = (
        df["price"].mean()
        + 2 * df["price"].std()
    )

    df["is_luxury"] = (
        df["price"] > luxury_threshold
    )

    # Create property ID
    df.insert(
        0,
        "property_id",
        range(1, len(df) + 1)
    )

    # Create output directory if required
    os.makedirs(
        "data/processed",
        exist_ok=True
    )

    # Save cleaned dataset
    df.to_csv(
        OUT_PATH,
        index=False
    )

    print(
        f"\nSaved cleaned dataset: "
        f"{df.shape} -> {OUT_PATH}"
    )

    print(
        f"Luxury threshold: "
        f"{luxury_threshold:,.0f} | "
        f"Luxury properties: "
        f"{df['is_luxury'].sum()}"
    )


if __name__ == "__main__":
    main()