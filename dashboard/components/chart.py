import plotly.graph_objects as go


def create_chart(data):

    fig = go.Figure()

    # Candlestick
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name="Candlestick"
        )
    )

    # SMA 20
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["SMA_20"],
            mode="lines",
            name="SMA 20",
            line=dict(color="blue", width=2)
        )
    )

    # SMA 50
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["SMA_50"],
            mode="lines",
            name="SMA 50",
            line=dict(color="orange", width=2)
        )
    )

    fig.update_layout(
        template="plotly_white",
        title="📈 Price Chart",
        height=650,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(color="#111827"),
        xaxis_rangeslider_visible=False,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig