import csv
import os
from datetime import datetime

def save_signal(close, sma20, sma50, signal):

    filename = "data/signals.csv"

    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Close",
                "SMA20",
                "SMA50",
                "Signal"
            ])

        writer.writerow([
            datetime.now(),
            round(close, 2),
            round(sma20, 2),
            round(sma50, 2),
            signal
        ])