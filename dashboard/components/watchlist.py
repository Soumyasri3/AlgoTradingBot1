import pandas as pd
import yfinance as yf


def load_watchlist():

    stocks = [
        "AAPL",
        "MSFT",
        "NVDA",
        "TSLA",
        "AMZN"
    ]

    rows = []

    for stock in stocks:

        data = yf.download(
            stock,
            period="2d",
            progress=False
        )

        if data.empty:
            continue

        if data.columns.nlevels > 1:
            data.columns = data.columns.get_level_values(0)

        latest = float(data["Close"].iloc[-1])
        previous = float(data["Close"].iloc[-2])

        change = ((latest - previous) / previous) * 100

        rows.append({

            "Ticker": stock,

            "Price": round(latest, 2),

            "Change %": round(change, 2)

        })

    return pd.DataFrame(rows)