import plotly.graph_objects as go


def create_profit_chart(trades):

    equity = trades["Profit"].cumsum()

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=list(range(1, len(equity)+1)),
            y=equity,
            mode="lines+markers",
            name="Equity Curve"
        )
    )

    fig.update_layout(

        title="📈 Profit Curve",

        template="plotly_white",

        height=450,

        xaxis_title="Trades",

        yaxis_title="Profit ($)"
    )

    return fig