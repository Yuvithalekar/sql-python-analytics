from sqlalchemy import create_engine

# PostgreSQL connection
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/sales_analytics"

# Create engine
engine = create_engine(DATABASE_URL)

print("PostgreSQL connection successful!")