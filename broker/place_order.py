from ib_insync import *

ib = IB()

try:
    ib.connect("127.0.0.1", 7497, clientId=20)

    print("✅ Connected to IBKR")

    contract = Stock("AAPL", "SMART", "USD")
    ib.qualifyContracts(contract)

    order = MarketOrder("BUY", 1)

    trade = ib.placeOrder(contract, order)

    # Wait for updates
    for _ in range(10):
        ib.sleep(1)
        print("Status:", trade.orderStatus.status)

    print("\n========== ORDER LOG ==========")
    for log in trade.log:
        print(log)

    print("\n========== ADVANCED ERROR ==========")
    print(trade.advancedError)

except Exception as e:
    print(e)

finally:
    ib.disconnect()