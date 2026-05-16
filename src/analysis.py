import os
import pandas as pd
from sqlalchemy import create_engine


# PostgreSQL Connection

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"

engine = create_engine(DATABASE_URL)


# Load Dataset

query = "SELECT * FROM sales"

df = pd.read_sql(query, engine)

print("\nDataset Loaded Successfully!\n")

print(df.head())


# Create Reports Folder

os.makedirs("reports", exist_ok=True)


# KPI Calculations

total_sales = df["sales_amount"].sum()

average_sales = df["sales_amount"].mean()

total_transactions = len(df)

average_discount = df["discount_pct"].mean()


# Print KPIs

print("\n========== KPI SUMMARY ==========\n")

print(f"Total Sales: {round(total_sales, 2)}")

print(f"Average Sales: {round(average_sales, 2)}")

print(f"Total Transactions: {total_transactions}")

print(f"Average Discount: {round(average_discount, 2)}")


# Category Analysis

category_sales = (
    df.groupby("category")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== CATEGORY SALES ==========\n")

print(category_sales)


# Region Analysis

region_sales = (
    df.groupby("region")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REGION SALES ==========\n")

print(region_sales)


# Top Products Analysis

top_products = (
    df.groupby("product_name")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP PRODUCTS ==========\n")

print(top_products)


# Customer Segment Analysis

segment_sales = (
    df.groupby("customer_segment")["sales_amount"]
    .mean()
)

print("\n========== CUSTOMER SEGMENTS ==========\n")

print(segment_sales)


# Payment Method Analysis

payment_analysis = (
    df.groupby("payment_method")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== PAYMENT METHOD ANALYSIS ==========\n")

print(payment_analysis)


# Sales Channel Analysis

channel_analysis = (
    df.groupby("sales_channel")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES CHANNEL ANALYSIS ==========\n")

print(channel_analysis)


# Correlation Analysis

correlation = df[
    [
        "quantity",
        "unit_price",
        "discount_pct",
        "sales_amount"
    ]
].corr()

print("\n========== CORRELATION MATRIX ==========\n")

print(correlation)

#Business Insights Report

report_path = "reports/business_insights.txt"

with open(report_path, "w") as file:

    file.write("BUSINESS SALES ANALYTICS REPORT\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Total Sales: {round(total_sales, 2)}\n")
    file.write(f"Average Sales: {round(average_sales, 2)}\n")
    file.write(f"Total Transactions: {total_transactions}\n")
    file.write(f"Average Discount: {round(average_discount, 2)}\n\n")

    file.write("TOP CATEGORY PERFORMANCE\n")
    file.write("-" * 40 + "\n")
    file.write(str(category_sales))
    file.write("\n\n")

    file.write("REGIONAL SALES PERFORMANCE\n")
    file.write("-" * 40 + "\n")
    file.write(str(region_sales))
    file.write("\n\n")

    file.write("TOP PRODUCTS\n")
    file.write("-" * 40 + "\n")
    file.write(str(top_products))
    file.write("\n\n")

    file.write("CUSTOMER SEGMENT ANALYSIS\n")
    file.write("-" * 40 + "\n")
    file.write(str(segment_sales))
    file.write("\n\n")

    file.write("PAYMENT METHOD ANALYSIS\n")
    file.write("-" * 40 + "\n")
    file.write(str(payment_analysis))
    file.write("\n\n")

    file.write("SALES CHANNEL ANALYSIS\n")
    file.write("-" * 40 + "\n")
    file.write(str(channel_analysis))
    file.write("\n\n")

print("\nBusiness report generated successfully!")

print(f"\nReport saved at: {report_path}")