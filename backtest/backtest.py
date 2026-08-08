def backtest_strategy(data):

    data["Signal"] = "NO SIGNAL"

    for i in range(50, len(data)):

        previous_sma20 = data["SMA_20"].iloc[i - 1]
        previous_sma50 = data["SMA_50"].iloc[i - 1]

        current_sma20 = data["SMA_20"].iloc[i]
        current_sma50 = data["SMA_50"].iloc[i]

        if previous_sma20 <= previous_sma50 and current_sma20 > current_sma50:
            data.loc[data.index[i], "Signal"] = "BUY"

        elif previous_sma20 >= previous_sma50 and current_sma20 < current_sma50:
            data.loc[data.index[i], "Signal"] = "SELL"

    return data