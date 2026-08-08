from ib_insync import *

ib = IB()

try:
    # Connect to IBKR Paper Trading
    ib.connect("127.0.0.1", 7497, clientId=10)

    print("✅ Connected to IBKR")

    # Create Stock Contract
    contract = Stock("AAPL", "SMART", "USD")

    # Verify Contract
    ib.qualifyContracts(contract)

    # Request Live Market Data
    ticker = ib.reqMktData(contract)

    # Wait for data
    ib.sleep(3)

    print("\n========== MARKET DATA ==========")
    print("Symbol :", contract.symbol)
    print("Last   :", ticker.last)
    print("Bid    :", ticker.bid)
    print("Ask    :", ticker.ask)
    print("High   :", ticker.high)
    print("Low    :", ticker.low)
    print("Close  :", ticker.close)
    print("Volume :", ticker.volume)
    print("================================")

except Exception as e:
    print("❌ Error:", e)

finally:
    ib.disconnect()