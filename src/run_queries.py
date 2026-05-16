import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"

engine = create_engine(DATABASE_URL)

query = """
SELECT category,
       ROUND(SUM(sales_amount)::numeric, 2) AS total_sales
FROM sales
GROUP BY category
ORDER BY total_sales DESC;
"""

df = pd.read_sql(query, engine)

print(df)