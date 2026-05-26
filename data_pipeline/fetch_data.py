import yfinance as yf

data = yf.download("^NSEI", period="1d", interval="5m")

# Flatten multi-level columns
data.columns = data.columns.get_level_values(0)

# Convert column names to lowercase
data.columns = [col.lower() for col in data.columns]

# Convert index into normal column
data.reset_index(inplace=True)

data.rename(columns={"index": "datetime"}, inplace=True)

print("\nCLEANED DATA:\n")
print(data.head())

print("\nCOLUMN NAMES:\n")
print(data.columns)

print("\nDATA TYPES:\n")
print(data.dtypes)

data.to_csv("nifty_data.csv", index=False)

print("\nCSV file created successfully.")