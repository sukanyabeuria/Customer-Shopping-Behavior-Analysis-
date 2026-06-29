import sqlalchemy

def connect_database():
    engine = sqlalchemy.create_engine(
    "postgresql://postgres:Niki%40123@localhost:5432/customer_shopping_dp"
)

    connection = engine.connect()
    print("✅ Connected to PostgreSQL successfully!")
    return connection