import matplotlib.pyplot as plt


def plot_chart(data):

    plt.figure(figsize=(15,8))

    plt.plot(
        data.index,
        data["Close"],
        label="Close Price"
    )

    plt.plot(
        data.index,
        data["SMA_20"],
        label="20 SMA"
    )

    plt.plot(
        data.index,
        data["SMA_50"],
        label="50 SMA"
    )

    # BUY Signals
    buy = data[data["Signal"] == "BUY"]

    plt.scatter(
        buy.index,
        buy["Close"],
        marker="^",
        s=120,
        label="BUY"
    )

    # SELL Signals
    sell = data[data["Signal"] == "SELL"]

    plt.scatter(
        sell.index,
        sell["Close"],
        marker="v",
        s=120,
        label="SELL"
    )

    plt.title("Apple Trading Strategy")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.grid(True)

    plt.legend()

    plt.show()