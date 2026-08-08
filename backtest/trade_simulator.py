import pandas as pd

def simulate_trades(data):

    trades = []

    position = None

    buy_price = 0

    buy_date = None

    for i in range(len(data)):

        signal = data["Signal"].iloc[i]

        if signal == "BUY" and position is None:

            position = "LONG"
            buy_price = data["Close"].iloc[i]
            buy_date = data.index[i]

        elif signal == "SELL" and position == "LONG":

            sell_price = data["Close"].iloc[i]
            sell_date = data.index[i]

            profit = sell_price - buy_price

            trades.append({
                "Buy Date": buy_date,
                "Sell Date": sell_date,
                "Buy Price": buy_price,
                "Sell Price": sell_price,
                "Profit": profit
            })

            position = None

    return pd.DataFrame(trades)