#import yfinance as yf

#print("Downloading Apple stock data...\n")


#data = yf.download("AAPL")


#print("First 5 rows:")
#print(data.head())

#print("\n--------------------------")


#print("Last 5 rows:")
#print(data.tail())
from backtest.trade_simulator import simulate_trades
from backtest.performance import performance_report
import yfinance as yf

from backtest.backtest import backtest_strategy
from utils.plot_chart import plot_chart

# Download historical data
ticker = input("Enter US Stock Symbol: ").upper()

data = yf.download(ticker, period="5y")
# Fix MultiIndex columns
if data.columns.nlevels > 1:
    data.columns = data.columns.get_level_values(0)

# Calculate Moving Averages
data["SMA_20"] = data["Close"].rolling(20).mean()
data["SMA_50"] = data["Close"].rolling(50).mean()

# Run Backtest
data = backtest_strategy(data)
print(data[["Close", "SMA_20", "SMA_50", "Signal"]].tail(30))
trades = simulate_trades(data)

print("\nTrade History\n")
print(trades)

performance_report(trades)
# Save trades to CSV
trades.to_csv("data/trades.csv", index=False)

print("\nTrade history saved to data/trades.csv")

# Count signals
buy_count = (data["Signal"] == "BUY").sum()
sell_count = (data["Signal"] == "SELL").sum()

print("\nBUY Signals :", buy_count)
print("SELL Signals:", sell_count)

# Plot chart
plot_chart(data)