import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine, text

# MySQL connection details
username = "root"
password = "root"
host = "localhost"
database = "market_dashboard"

# Create SQLAlchemy engine
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Fetch market data
data = yf.download("^NSEI", period="1d", interval="5m")

# Flatten multi-level columns
data.columns = data.columns.get_level_values(0)

# Convert column names to lowercase
data.columns = [col.lower() for col in data.columns]

# Convert index into normal column
data.reset_index(inplace=True)

# Rename index column
data.rename(columns={"index": "datetime"}, inplace=True)
data["datetime"] = data["datetime"].dt.tz_localize(None)

# Get latest timestamp from database
query = text("SELECT MAX(datetime) FROM nifty_prices")

with engine.connect() as connection:
    latest_timestamp = connection.execute(query).scalar()

print("\nLatest timestamp in database:")
print(latest_timestamp)

# Keep only newer rows
if latest_timestamp is not None:
    data = data[data["datetime"] > latest_timestamp]

print("\nNew rows to insert:")
print(data)

# Insert only new rows
if not data.empty:

    data.to_sql(
        "nifty_prices",
        con=engine,
        if_exists="append",
        index=False
    )

    print("\nNew market data inserted successfully!")

else:
    print("\nNo new rows found.")