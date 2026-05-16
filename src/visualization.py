import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# PostgreSQL Connection
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"
engine = create_engine(DATABASE_URL)


# Load Dataset
query = "SELECT * FROM sales"

df = pd.read_sql(query, engine)

print("\nDataset Loaded Successfully!\n")
print(df.head())


# Set Plot Style
sns.set_style("whitegrid")


# 1. Category Sales Analysis
category_sales = (
    df.groupby("category")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/charts/category_sales.png")

plt.show()

print("Category Sales Chart Saved!")


# 2. Region Sales Analysis
region_sales = (
    df.groupby("region")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("reports/charts/region_sales.png")

plt.show()

print("Region Sales Chart Saved!")


# 3. Top Products Analysis
top_products = (
    df.groupby("product_name")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_products.index,
    y=top_products.values
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("reports/charts/top_products.png")

plt.show()

print("Top Products Chart Saved!")


# 4. Customer Segment Analysis
segment_sales = (
    df.groupby("customer_segment")["sales_amount"]
    .mean()
)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=segment_sales.index,
    y=segment_sales.values
)

plt.title("Average Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Sales")

plt.tight_layout()

plt.savefig("reports/charts/customer_segment.png")

plt.show()

print("Customer Segment Chart Saved!")


# 5. Correlation Heatmap
correlation = df[
    [
        "quantity",
        "unit_price",
        "discount_pct",
        "sales_amount"
    ]
].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("reports/charts/correlation_heatmap.png")

plt.show()

print("Correlation Heatmap Saved!")


# Finished
print("\nAll visualizations generated successfully!")