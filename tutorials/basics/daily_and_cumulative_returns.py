"""Compute daily returns."""

import os
import pandas as pd
import matplotlib.pyplot as plt
from utils.utils import *




def test_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')  # one month only
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    cumulative_returns = compute_cumulative_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    plot_data(cumulative_returns, title="Cumulative returns", ylabel="Cumulative returns")


if __name__ == "__main__":
    test_run()
