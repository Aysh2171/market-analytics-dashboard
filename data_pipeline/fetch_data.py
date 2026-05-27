import yfinance as yf
from sqlalchemy import create_engine

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

# Save CSV
data.to_csv("nifty_data.csv", index=False)

try:
    data.to_sql(
        "nifty_prices",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("\nData inserted into MySQL successfully!")

except Exception as e:
    print("\nERROR OCCURRED:")
    print(e)