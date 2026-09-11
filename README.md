# Real Estate Market Analysis

An end-to-end Real Estate Property Market Analysis project using Python, MySQL, SQL, Power BI, and automated reporting.

The project analyzes property listings across major Indian cities to identify pricing patterns, property characteristics, city-level demand, and investment-oriented insights.

---

## Project Overview

This project follows a complete data analytics workflow:

**Raw Dataset → Data Cleaning → SQL Analysis → Exploratory Data Analysis → Data Visualization → Automated PDF Report → Power BI Dashboard → Business Insights**

The analysis is based on a real-world property dataset containing information about property area, bedrooms, construction year, city, street type, furnishing, property type, swimming pool availability, and price.

---

## Objectives

- Clean and preprocess the raw real estate dataset.
- Perform SQL-based market analysis using MySQL.
- Conduct exploratory data analysis using Python.
- Identify relationships between property characteristics and prices.
- Analyze city-level property demand and pricing.
- Compare property types and their price performance.
- Analyze price per square foot.
- Identify luxury and price-outlier properties.
- Build an interactive Power BI dashboard.
- Generate an automated PDF market analysis report.
- Extract actionable business and investment insights.

---

## Dataset

The project uses the `dataset_2.csv` real estate dataset.

### Original Dataset

- **Rows:** 1,124
- **Columns:** 9

### Original Columns

| Column | Description |
|---|---|
| Area_SqFt | Property area in square feet |
| Rooms | Number of bedrooms/rooms |
| Build_Year | Year the property was built |
| Location | Property location/city |
| Street_Type | Type of street |
| Furnishing | Furnishing status |
| Property_Type | Type of property |
| Has_Pool | Swimming pool availability |
| Price | Property price |

### Cities Covered

- Delhi
- Noida
- Gurugram
- Lucknow
- Kanpur
- Jaipur
- Indore
- Prayagraj

### Property Types

- Apartment
- Independent House
- Duplex
- Villa

---

## Data Cleaning

The raw dataset was cleaned and standardized using Python.

### Cleaning Results

- **Raw records:** 1,124
- **Cleaned records:** 1,091
- **Rows removed:** 33
- **Duplicate rows:** 0

Rows with missing or invalid values in important fields such as price and area were removed.

### Standardized Columns

The original column names were converted into a consistent naming convention:

```text
Area_SqFt     → area_sqft
Rooms         → bedrooms
Build_Year    → build_year
Location      → city
Street_Type   → street_type
Furnishing    → furnishing
Property_Type → property_type
Has_Pool      → has_pool
Price         → price
