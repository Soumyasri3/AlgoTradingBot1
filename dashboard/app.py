import streamlit as st
from streamlit_option_menu import option_menu
from components.chart import create_chart
from components.profit_chart import create_profit_chart
from components.pie_chart import create_pie_chart
from components.watchlist import load_watchlist
from datetime import datetime
import pandas as pd
from pathlib import Path
import yfinance as yf
from streamlit_autorefresh import st_autorefresh
from pages.backtesting import show_backtesting


def load_css():
    css_file = Path(__file__).parent / "assets" / "style.css"

    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

st.set_page_config(
    page_title="Algo Trading Terminal",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)
st_autorefresh(
    interval=10000,
    key="refresh"
)

# ---------------- Sidebar ----------------

# ---------------- Sidebar ----------------

with st.sidebar:

    selected = option_menu(
        menu_title="Algo Trading Bot",
        options=[
            "Dashboard",
            "Backtesting",
            "Analytics",
            "Paper Trading",
            "Live Trading",
            "Settings"
        ],
        icons=[
            "speedometer2",
            "graph-up",
            "bar-chart",
            "currency-dollar",
            "activity",
            "gear"
        ],
        default_index=0
    )
if selected == "Backtesting":

    show_backtesting()

    st.stop()
# ---------------- Title ----------------

st.markdown(
    """
    <h1 style='text-align:center;color:#00d4ff;'>
        🤖 ALGO TRADING TERMINAL
    </h1>

    <p style='text-align:center;
              color:#BBBBBB;
              font-size:20px;'>
        Automated US Stock Trading Platform
    </p>
    """,
    unsafe_allow_html=True
)

st.caption(
    f"🕒 Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
)

st.success("🟢 Live Data Connected")

st.divider()



# ---------------- Load Trade History ----------------

BASE_DIR = Path(__file__).resolve().parent.parent

trades = pd.read_csv(BASE_DIR / "data" / "trades.csv")

# ---------------- Download Latest Price ----------------

ticker = st.sidebar.text_input(
    "🔍 Search Stock",
    value="AAPL"
).upper()

data = yf.download(ticker, period="6mo")

if data.columns.nlevels > 1:
    data.columns = data.columns.get_level_values(0)

# ADD THESE TWO LINES
data["SMA_20"] = data["Close"].rolling(20).mean()
data["SMA_50"] = data["Close"].rolling(50).mean()

current_price = float(data["Close"].iloc[-1])
previous_close = float(data["Close"].iloc[-2])

today_change = current_price - previous_close

today_percent = (today_change / previous_close) * 100
# ---------------- Calculate Metrics ----------------

total_trades = len(trades)

winning = len(trades[trades["Profit"] > 0])

win_rate = (winning / total_trades) * 100

net_profit = trades["Profit"].sum()
st.info(f"📌 Currently Viewing: {ticker}")

# ---------------- KPI Cards ----------------

# ---------------- KPI Cards ----------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Current Price",
    f"${current_price:.2f}",
    f"{today_percent:+.2f}%"
)

col2.metric(
    "📈 Net Profit",
    f"${net_profit:.2f}",
    f"{winning}/{total_trades} Wins"
)

col3.metric(
    "🏆 Win Rate",
    f"{win_rate:.2f}%",
    "Strategy"
)

col4.metric(
    "📊 Total Trades",
    total_trades,
    "Executed"
)

st.subheader("📈 Market Chart")

fig = create_chart(data)

st.plotly_chart(fig, use_container_width=True)


st.divider()

st.subheader("📋 Trade History")

st.dataframe(
    trades,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("📈 Profit Curve")

profit_fig = create_profit_chart(trades)

st.plotly_chart(
    profit_fig,
    use_container_width=True
)
st.divider()

st.subheader("📊 Trading Statistics")

col1, col2 = st.columns(2)

with col1:

    pie_fig = create_pie_chart(trades)

    st.plotly_chart(
        pie_fig,
        use_container_width=True
    )
st.divider()

st.subheader("📈 Live Watchlist")

watchlist = load_watchlist()

st.dataframe(
    watchlist,
    use_container_width=True,
    hide_index=True
)

with col2:

    st.metric("Winning Trades", winning)

    st.metric("Losing Trades", total_trades - winning)

    st.metric("Total Profit", f"${net_profit:.2f}")

    st.metric("Win Rate", f"{win_rate:.2f}%")
