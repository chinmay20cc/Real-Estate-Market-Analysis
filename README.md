# Real Estate Market Analysis

An end-to-end real estate property market analysis project using Python, MySQL, and Power BI.

## Project Overview

This project analyzes residential property data across major cities in India to identify pricing patterns, location-level differences, property-type trends, and factors influencing property prices.

The project follows a complete data analytics workflow:

**Raw Data → Data Cleaning → SQL Analysis → Exploratory Data Analysis → Visualization → Business Insights → Power BI Dashboard**

## Objectives

- Analyze property prices across different cities
- Compare property types and their average prices
- Study the relationship between property area and price
- Analyze price per square foot
- Understand bedroom-wise property distribution
- Identify luxury properties and price outliers
- Analyze the effect of furnishing and swimming pools on property prices
- Identify useful insights for buyers and investors

## Dataset

The project uses a real estate property dataset containing information about:

- Area in square feet
- Number of bedrooms
- Build year
- City
- Street type
- Furnishing status
- Property type
- Swimming pool availability
- Property price

### Dataset Size

| Stage | Rows | Columns |
|---|---:|---:|
| Raw dataset | 1,124 | 9 |
| Cleaned dataset | 1,091 | 15 |

During cleaning:

- 33 records with missing price or area values were removed
- Duplicate records were checked
- 15 price outliers were flagged using the IQR method
- Engineered features were created for analysis

## Technologies Used

- **Python**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - ReportLab

- **MySQL**
  - Data storage
  - SQL analysis
  - Aggregations
  - Ranking
  - Filtering

- **Power BI**
  - Interactive dashboard
  - KPI cards
  - Slicers
  - Charts
  - Property and location analysis

- **Jupyter Notebook**
  - Exploratory Data Analysis

## Project Structure

```text
Real-Estate-Market-Analysis/
│
├── data/
│   ├── raw/
│   │   └── house_prices.csv
│   └── processed/
│       └── cleaned_properties.csv
│
├── notebooks/
│   └── 02_eda.ipynb
│
├── reports/
│   ├── charts/
│   └── Real_Estate_Market_Report.pdf
│
├── sql/
│   ├── 01_create_schema.sql
│   └── 03_analysis_queries.sql
│
├── src/
│   ├── clean_data.py
│   ├── generate_charts.py
│   └── generate_report.py
│
├── docs/
├── .gitignore
└── README.md
