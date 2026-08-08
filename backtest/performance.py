def performance_report(trades):

    total_trades = len(trades)

    winning_trades = len(trades[trades["Profit"] > 0])

    losing_trades = len(trades[trades["Profit"] < 0])

    win_rate = 0

    if total_trades > 0:
        win_rate = (winning_trades / total_trades) * 100

    net_profit = trades["Profit"].sum()

    average_profit = trades["Profit"].mean()

    best_trade = trades["Profit"].max()

    worst_trade = trades["Profit"].min()

    print("\n========== BACKTEST REPORT ==========\n")

    print("Total Trades   :", total_trades)
    print("Winning Trades :", winning_trades)
    print("Losing Trades  :", losing_trades)
    print("Win Rate       :", round(win_rate,2),"%")
    print("Net Profit     :", round(net_profit,2))
    print("Average Profit :", round(average_profit,2))
    print("Best Trade     :", round(best_trade,2))
    print("Worst Trade    :", round(worst_trade,2))