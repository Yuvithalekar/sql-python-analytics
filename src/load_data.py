import pandas as pd
from sqlalchemy import create_engine

# Database URL
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"

# Create engine
engine = create_engine(DATABASE_URL)

# Load CSV
df = pd.read_csv("data/sales_data.csv")

# Upload to PostgreSQL
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data uploaded successfully!")