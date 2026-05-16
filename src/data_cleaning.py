import pandas as pd

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Show first rows
print(df.head())

# Show info
print(df.info())

# Check missing values
print(df.isnull().sum())