from utils.utils import *
import matplotlib.pyplot as plt
def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')  # one month only
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    daily_returns.hist(bins=20) #changing # of bins to 20

    #Get mean and standard deviation
    mean=daily_returns['SPY'].mean()
    print("mean=",mean)
    std=daily_returns['SPY'].std()
    print("std=",std)


    #show std and mean in histogram
    plt.axvline(mean,color='w',linestyle='dashed',linewidth=2)
    plt.axvline(std,color='r',linestyle='dashed',linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()

    #Compute kurtosis
    print(daily_returns.kurtosis())

if __name__ == "__main__":
    test_run()