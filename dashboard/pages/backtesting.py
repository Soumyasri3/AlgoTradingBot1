import streamlit as st
import yfinance as yf
from datetime import date
from components.backtest_chart import create_backtest_chart


def show_backtesting():

    # ==========================
    # Title
    # ==========================

    st.title("📊 Strategy Backtesting")
    st.write("Configure your backtest.")

    # ==========================
    # Inputs
    # ==========================

    ticker = st.text_input(
        "📈 Stock Symbol",
        value="AAPL"
    ).upper()

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input(
            "📅 Start Date",
            value=date(2024, 1, 1)
        )

    with col2:
        end_date = st.date_input(
            "📅 End Date",
            value=date.today()
        )

    col3, col4 = st.columns(2)

    with col3:
        sma_short = st.number_input(
            "Short SMA",
            min_value=5,
            value=20
        )

    with col4:
        sma_long = st.number_input(
            "Long SMA",
            min_value=10,
            value=50
        )

    # ==========================
    # Run Button
    # ==========================

    run = st.button(
        "▶ Run Backtest",
        use_container_width=True
    )

    # ==========================
    # Run Backtest
    # ==========================

    if run:

        # Download Data
        data = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            progress=False
        )

        if data.empty:
            st.error("❌ No data found.")
            st.stop()

        if data.columns.nlevels > 1:
            data.columns = data.columns.get_level_values(0)

        st.success("✅ Historical data downloaded successfully!")

        # ==========================
        # Calculate SMA
        # ==========================

        data["SMA_Short"] = (
            data["Close"]
            .rolling(window=sma_short)
            .mean()
        )

        data["SMA_Long"] = (
            data["Close"]
            .rolling(window=sma_long)
            .mean()
        )

        # ==========================
        # Generate Signals
        # ==========================

        data["Signal"] = 0

        data.loc[
            data["SMA_Short"] > data["SMA_Long"],
            "Signal"
        ] = 1

        data.loc[
            data["SMA_Short"] < data["SMA_Long"],
            "Signal"
        ] = -1

        # ==========================
        # Buy / Sell Positions
        # ==========================

        data["Position"] = data["Signal"].diff()

        # ==========================
        # Strategy Returns
        # ==========================

        data["Daily Return"] = data["Close"].pct_change()

        data["Strategy Return"] = (
            data["Daily Return"] *
            data["Signal"].shift(1)
        )

        data["Cumulative Return"] = (
            1 + data["Strategy Return"]
        ).cumprod()

        # ==========================
        # Portfolio Value
        # ==========================

        initial_capital = 10000

        final_value = (
            initial_capital *
            data["Cumulative Return"].iloc[-1]
        )

        profit = final_value - initial_capital

        return_percent = (
            profit / initial_capital
        ) * 100

        # ==========================
        # KPI Cards
        # ==========================

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "💰 Initial Capital",
            f"${initial_capital:,.2f}"
        )

        col2.metric(
            "💵 Final Value",
            f"${final_value:,.2f}"
        )

        col3.metric(
            "📈 Profit",
            f"${profit:,.2f}"
        )

        col4.metric(
            "📊 Return %",
            f"{return_percent:.2f}%"
        )

        st.divider()

        # ==========================
        # Strategy Chart
        # ==========================

        st.subheader("📈 Strategy Chart")

        fig = create_backtest_chart(data)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ==========================
        # Strategy Data
        # ==========================

        st.subheader("📋 Strategy Data")

        st.dataframe(
            data.tail(20),
            use_container_width=True
        )