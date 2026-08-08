import plotly.graph_objects as go


def create_pie_chart(trades):

    winning = len(trades[trades["Profit"] > 0])

    losing = len(trades[trades["Profit"] <= 0])

    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Winning", "Losing"],
                values=[winning, losing],
                hole=0.55,
                marker=dict(
                    colors=["#22C55E", "#EF4444"]
                )
            )
        ]
    )

    fig.update_layout(

        title="🏆 Win / Loss Ratio",

        template="plotly_white",

        height=450
    )

    return fig