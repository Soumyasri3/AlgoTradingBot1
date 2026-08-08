import yfinance as yf

# Download stock data
data = yf.download("AAPL")

# Flatten columns if needed
if data.columns.nlevels > 1:
    data.columns = data.columns.get_level_values(0)


data["SMA_20"] = data["Close"].rolling(20).mean()
data["SMA_50"] = data["Close"].rolling(50).mean()

latest_sma20 = data["SMA_20"].iloc[-1]
latest_sma50 = data["SMA_50"].iloc[-1]

print("20 SMA :", latest_sma20)
print("50 SMA :", latest_sma50)

# Strategy
if latest_sma20 > latest_sma50:
    print("\nBUY SIGNAL")
else:
    print("\nSELL SIGNAL")