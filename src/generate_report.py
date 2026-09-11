import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak,
    Table,
    TableStyle
)
import os


# =========================
# PATHS
# =========================

DATA_PATH = "data/processed/cleaned_properties.csv"
CHART_DIR = "reports/charts"
OUTPUT_PATH = "reports/Real_Estate_Market_Report.pdf"


# =========================
# LOAD DATA
# =========================

df = pd.read_csv(DATA_PATH)

os.makedirs("reports", exist_ok=True)


# =========================
# CALCULATE KPIs
# =========================

total_properties = len(df)
average_price = df["price"].mean()
median_price = df["price"].median()
average_area = df["area_sqft"].mean()
average_ppsf = df["price_per_sqft"].mean()
maximum_price = df["price"].max()

highest_price_property = df.loc[df["price"].idxmax()]

city_counts = df["city"].value_counts()
highest_demand_city = city_counts.idxmax()
highest_demand_count = city_counts.max()

city_average_price = df.groupby("city")["price"].mean()
highest_price_city = city_average_price.idxmax()
highest_price_city_avg = city_average_price.max()

luxury_count = (df["is_luxury"] == True).sum()
luxury_percentage = luxury_count / total_properties * 100

area_price_corr = df["area_sqft"].corr(df["price"])
area_ppsf_corr = df["area_sqft"].corr(df["price_per_sqft"])


# =========================
# PROPERTY TYPE ANALYSIS
# =========================

type_average_price = df.groupby("property_type")["price"].mean()

highest_type = type_average_price.idxmax()
highest_type_price = type_average_price.max()

lowest_type = type_average_price.idxmin()
lowest_type_price = type_average_price.min()

type_ppsf = df.groupby("property_type")["price_per_sqft"].mean()

best_value_type = type_ppsf.idxmin()
best_value_ppsf = type_ppsf.min()

premium_type = type_ppsf.idxmax()
premium_ppsf = type_ppsf.max()


# =========================
# FURNISHING & POOL
# =========================

furnishing_avg = df.groupby("furnishing")["price"].mean()

pool_avg = df.groupby("has_pool")["price"].mean()


# =========================
# REPORT STYLES
# =========================

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    fontSize=24,
    leading=30,
    alignment=TA_CENTER,
    spaceAfter=20
)

heading_style = ParagraphStyle(
    "HeadingCustom",
    parent=styles["Heading1"],
    fontSize=18,
    leading=22,
    spaceAfter=12
)

body_style = ParagraphStyle(
    "BodyCustom",
    parent=styles["BodyText"],
    fontSize=11,
    leading=17,
    spaceAfter=10
)


# =========================
# PDF DOCUMENT
# =========================

doc = SimpleDocTemplate(
    OUTPUT_PATH,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=45,
    bottomMargin=45
)

story = []


# =========================
# PAGE 1: TITLE
# =========================

story.append(Spacer(1, 1.5 * inch))

story.append(
    Paragraph(
        "REAL ESTATE PROPERTY<br/>MARKET ANALYSIS",
        title_style
    )
)

story.append(
    Paragraph(
        "Delhi NCR & Selected Indian Cities",
        ParagraphStyle(
            "Subtitle",
            parent=styles["Heading2"],
            alignment=TA_CENTER
        )
    )
)

story.append(Spacer(1, 30))

story.append(
    Paragraph(
        "Data Analytics Project",
        ParagraphStyle(
            "Center",
            parent=body_style,
            alignment=TA_CENTER
        )
    )
)

story.append(PageBreak())


# =========================
# PAGE 2: EXECUTIVE SUMMARY
# =========================

story.append(Paragraph("Executive Summary", heading_style))

summary = f"""
This report analyzes {total_properties:,} residential property listings across
Delhi, Noida, Gurugram, Lucknow, Kanpur, Jaipur, Indore and Prayagraj.

The average property price is ₹{average_price:,.0f}, while the median price is
₹{median_price:,.0f}. The average property area is approximately
{average_area:,.0f} square feet.

{highest_demand_city} has the highest number of listings with
{highest_demand_count} properties, indicating the strongest listing volume
among the analyzed cities.

{highest_price_city} has the highest average property price at approximately
₹{highest_price_city_avg:,.0f}.

The relationship between property area and price is strongly positive, with
a correlation of {area_price_corr:.2f}.
"""

story.append(Paragraph(summary, body_style))
story.append(PageBreak())


# =========================
# PAGE 3: KPI TABLE
# =========================

story.append(Paragraph("Key Market KPIs", heading_style))

kpi_data = [
    ["Metric", "Value"],
    ["Total Properties", f"{total_properties:,}"],
    ["Average Price", f"₹{average_price:,.0f}"],
    ["Median Price", f"₹{median_price:,.0f}"],
    ["Average Area", f"{average_area:,.0f} sqft"],
    ["Average Price / Sq Ft", f"₹{average_ppsf:,.2f}"],
    ["Maximum Price", f"₹{maximum_price:,.0f}"],
    ["Luxury Properties", f"{luxury_count:,}"],
    ["Luxury Percentage", f"{luxury_percentage:.1f}%"],
]

table = Table(kpi_data, colWidths=[3.3 * inch, 2.5 * inch])

table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
        ("ALIGN", (1, 1), (1, -1), "RIGHT"),
        ("PADDING", (0, 0), (-1, -1), 8),
    ])
)

story.append(table)
story.append(PageBreak())


# =========================
# PAGES 4-13: CHARTS
# =========================

charts = [
    ("01_price_distribution.png", "Property Price Distribution"),
    ("02_average_price_by_city.png", "Average Property Price by City"),
    ("03_property_type_distribution.png", "Property Type Distribution"),
    ("04_average_price_by_property_type.png", "Average Price by Property Type"),
    ("05_area_vs_price.png", "Area vs Property Price"),
    ("06_price_per_sqft_by_property_type.png", "Average Price per Sq Ft by Property Type"),
    ("07_bedrooms_vs_price.png", "Average Property Price by Bedrooms"),
    ("08_furnishing_vs_price.png", "Average Price by Furnishing"),
    ("09_pool_vs_price.png", "Average Price by Pool Availability"),
    ("10_build_year_vs_price.png", "Average Price by Build Year"),
]

for filename, title in charts:

    story.append(Paragraph(title, heading_style))
    story.append(Spacer(1, 10))

    chart_path = os.path.join(CHART_DIR, filename)

    if os.path.exists(chart_path):
        img = Image(chart_path)
        img.drawHeight = 5.8 * inch
        img.drawWidth = 7.2 * inch
        story.append(img)
    else:
        story.append(
            Paragraph(
                f"Chart file not found: {filename}",
                body_style
            )
        )

    story.append(PageBreak())


# =========================
# BUSINESS INSIGHTS
# =========================

story.append(Paragraph("Business Insights", heading_style))

insights = [
    f"Property size is a major price driver, with an area-price correlation of {area_price_corr:.2f}.",
    
    f"{highest_demand_city} has the highest listing volume with {highest_demand_count} properties, indicating strong market liquidity.",
    
    f"{highest_price_city} records the highest average property price at approximately ₹{highest_price_city_avg:,.0f}.",
    
    f"{highest_type} properties have the highest average price at approximately ₹{highest_type_price:,.0f}.",
    
    f"{best_value_type} provides the lowest average price per square foot at approximately ₹{best_value_ppsf:,.2f}.",
    
    f"{premium_type} has the highest average price per square foot at approximately ₹{premium_ppsf:,.2f}.",
    
    f"There are {luxury_count} luxury properties, representing approximately {luxury_percentage:.1f}% of the dataset.",
    
    f"Area and price per square foot have a correlation of {area_ppsf_corr:.2f}, suggesting that larger properties tend to have lower price per square foot."
]

for i, insight in enumerate(insights, 1):
    story.append(
        Paragraph(
            f"<b>{i}.</b> {insight}",
            body_style
        )
    )

story.append(PageBreak())


# =========================
# FINAL RECOMMENDATIONS
# =========================

story.append(Paragraph("Final Recommendations", heading_style))

recommendations = f"""
<b>1. Focus on high-demand markets</b><br/>
{highest_demand_city} has the highest listing volume and should be considered
an important market for inventory and transaction activity.

<br/><br/>

<b>2. Consider premium city markets</b><br/>
{highest_price_city} commands the highest average property price, making it
relevant for premium residential positioning.

<br/><br/>

<b>3. Evaluate properties using price per square foot</b><br/>
Price per square foot provides a useful comparison between properties with
different sizes and can help identify relatively better-value opportunities.

<br/><br/>

<b>4. Use property size as a major pricing factor</b><br/>
The strong positive correlation between area and price indicates that property
size should be an important variable in pricing and valuation models.

<br/><br/>

<b>5. Track luxury inventory separately</b><br/>
Luxury properties represent a small portion of the overall market and should
be analyzed as a distinct premium segment.
"""

story.append(Paragraph(recommendations, body_style))


# =========================
# BUILD PDF
# =========================

doc.build(story)

print("PDF report generated successfully!")
print("Saved to:", OUTPUT_PATH)