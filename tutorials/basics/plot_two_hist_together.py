from utils.utils import *
import matplotlib.pyplot as plt

def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')  # one month only
    symbols = ['SPY','XOM']
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    daily_returns['SPY'].hist(bins=20,label='SPY')
    daily_returns['XOM'].hist(bins=20,label='XOM')
    plt.legend(loc='upper right')
    plt.show()

    #Compute kurtosis
    print(daily_returns.kurtosis())

if __name__ == "__main__":
    test_run()