from utils.save_signal import save_signal
from utils.plot_chart import plot_chart

def sma_strategy(data):

    data["SMA_20"] = data["Close"].rolling(20).mean()
    data["SMA_50"] = data["Close"].rolling(50).mean()
    
    data["Signal"] = "NO SIGNAL"
    latest_close = data["Close"].iloc[-1]

    latest_sma20 = data["SMA_20"].iloc[-1]
    latest_sma50 = data["SMA_50"].iloc[-1]

    previous_sma20 = data["SMA_20"].iloc[-2]
    previous_sma50 = data["SMA_50"].iloc[-2]

    if previous_sma20 < previous_sma50 and latest_sma20 > latest_sma50:

        signal = "BUY"

    elif previous_sma20 > previous_sma50 and latest_sma20 < latest_sma50:

        signal = "SELL"

    else:

        signal = "NO SIGNAL"


    save_signal(
    latest_close,
    latest_sma20,
    latest_sma50,
    signal
    )

    data.loc[data.index[-1], "Signal"] = signal

    plot_chart(data)

    return signal