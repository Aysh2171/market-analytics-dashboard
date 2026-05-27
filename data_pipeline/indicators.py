def add_indicators(data):

    # 20-period moving average
    data["ma20"] = data["close"].rolling(window=20).mean()

    # Percentage change
    data["pct_change"] = data["close"].pct_change() * 100

    # Rolling volatility
    data["volatility"] = data["close"].rolling(window=20).std()

    return data