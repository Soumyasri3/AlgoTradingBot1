import plotly.graph_objects as go


def create_backtest_chart(data):

    fig = go.Figure()

    # Close Price
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Close"],
            mode="lines",
            name="Close",
            line=dict(color="#2563EB", width=2)
        )
    )

    # Short SMA
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["SMA_Short"],
            mode="lines",
            name="Short SMA",
            line=dict(color="orange", width=2)
        )
    )

    # Long SMA
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["SMA_Long"],
            mode="lines",
            name="Long SMA",
            line=dict(color="green", width=2)
        )
    )

    # BUY Signals
    buy = data[data["Position"] == 1]

    fig.add_trace(
        go.Scatter(
            x=buy.index,
            y=buy["Close"],
            mode="markers",
            marker=dict(
                color="lime",
                size=12,
                symbol="triangle-up"
            ),
            name="BUY"
        )
    )

    # SELL Signals
    sell = data[data["Position"] == -2]

    fig.add_trace(
        go.Scatter(
            x=sell.index,
            y=sell["Close"],
            mode="markers",
            marker=dict(
                color="red",
                size=12,
                symbol="triangle-down"
            ),
            name="SELL"
        )
    )

    fig.update_layout(

        template="plotly_white",

        height=650,

        title="📈 SMA Backtest",

        xaxis_title="Date",

        yaxis_title="Price",

        xaxis_rangeslider_visible=False
    )

    return fig