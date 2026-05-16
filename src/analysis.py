import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM sales"

df = pd.read_sql(query, engine)

print(df.head())
print(df.info())
print(df.describe())

total_sales = df["sales_amount"].sum()
print("Total Sales:", round(total_sales, 2))

average_sales = df["sales_amount"].mean()
print("Average Sales:", round(average_sales, 2))

