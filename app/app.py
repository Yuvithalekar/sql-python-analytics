import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


# Page Configuration


st.set_page_config(
    page_title="Business Analytics Dashboard",
    layout="wide"
)


# Dashboard Title

st.title("Business Analytics Dashboard")

st.markdown(
    """
    Interactive sales analytics dashboard using:
    - PostgreSQL
    - Python
    - Pandas
    - Streamlit
    """
)


# PostgreSQL Connection

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"

engine = create_engine(DATABASE_URL)


# Load Dataset

query = "SELECT * FROM sales"

df = pd.read_sql(query, engine)


# Sidebar Filters

st.sidebar.header("Filters")

selected_category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["category"].unique())
)

selected_region = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["region"].unique())
)

selected_channel = st.sidebar.selectbox(
    "Select Sales Channel",
    ["All"] + list(df["sales_channel"].unique())
)

# Apply Filters

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["category"] == selected_category
    ]

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["region"] == selected_region
    ]

if selected_channel != "All":
    filtered_df = filtered_df[
        filtered_df["sales_channel"] == selected_channel
    ]


# KPI Calculations

total_sales = filtered_df["sales_amount"].sum()

average_sales = filtered_df["sales_amount"].mean()

total_transactions = len(filtered_df)

average_discount = filtered_df["discount_pct"].mean()


# KPI Cards

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Sales",
    f"${round(total_sales, 2)}"
)

col2.metric(
    "Average Sales",
    f"${round(average_sales, 2)}"
)

col3.metric(
    "Transactions",
    total_transactions
)

col4.metric(
    "Average Discount",
    f"{round(average_discount, 2)}%"
)


# Category Sales Chart

st.subheader("Category Sales Analysis")

category_sales = (
    filtered_df.groupby("category")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values,
    ax=ax
)

plt.xticks(rotation=45)

plt.xlabel("Category")
plt.ylabel("Total Sales")

st.pyplot(fig)


# Regional Sales Chart

st.subheader("Regional Sales Analysis")

region_sales = (
    filtered_df.groupby("region")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=region_sales.index,
    y=region_sales.values,
    ax=ax
)

plt.xlabel("Region")
plt.ylabel("Total Sales")

st.pyplot(fig)


# Top Products Table

st.subheader("Top 10 Products")

top_products = (
    filtered_df.groupby("product_name")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_products)


# Customer Segment Analysis

st.subheader("Customer Segment Analysis")

segment_sales = (
    filtered_df.groupby("customer_segment")["sales_amount"]
    .mean()
)

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=segment_sales.index,
    y=segment_sales.values,
    ax=ax
)

plt.xlabel("Customer Segment")
plt.ylabel("Average Sales")

st.pyplot(fig)


# Payment Method Analysis

st.subheader("Payment Method Analysis")

payment_analysis = (
    filtered_df.groupby("payment_method")["sales_amount"]
    .sum()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8, 5))

sns.barplot(
    x=payment_analysis.index,
    y=payment_analysis.values,
    ax=ax
)

plt.xticks(rotation=45)

plt.xlabel("Payment Method")
plt.ylabel("Total Sales")

st.pyplot(fig)

# Correlation Heatmap

st.subheader("Correlation Heatmap")

correlation = filtered_df[
    [
        "quantity",
        "unit_price",
        "discount_pct",
        "sales_amount"
    ]
].corr()

fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig)


# Raw Dataset

st.subheader("Raw Dataset")

st.dataframe(filtered_df)


# Footer

st.markdown("---")

st.markdown(
    "Built with PostgreSQL, Python, Pandas, Seaborn, and Streamlit."
)