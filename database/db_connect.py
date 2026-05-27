from sqlalchemy import create_engine

username = "root"
password = "root"
host = "localhost"
database = "market_dashboard"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

connection = engine.connect()

print("MySQL connection successful!")