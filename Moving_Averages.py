import pandas as pd
import matplotlib.pyplot as plt 

################################
#        Moving Averages       #
#   10, 20, 50, 100, 150, 200  #
################################
#    calculates 6 moving averages to evaluate any
#    possible correlation between price movement and the moving average.
#    with code we can customize and use as many iterations of varying moving
#    average time horizons to create a 'net' or 'fan' to assist in visualization
#    of the behavior of the movement

def scan_all_MA(df):
    ma_day = [10, 20, 50, 100, 150, 200]
    for ma in ma_day:
        column_name = "MA for %s days" %(str(ma))
        df[column_name] = df['Adj. Close'].rolling(window = ma, center=False).mean()

    df[['Adj. Close', 'MA for 10 days', 'MA for 20 days',
        'MA for 50 days', 'MA for 100 days', 'MA for 150 days',
        'MA for 200 days']].plot(subplots=False, figsize=(10, 4), lw = 1)
    plt.show()

   temp_df = pd.read_csv('Insert-target-file-path', index_col='Date', parse_dates=True)
   scan_all_MA(temp_df)
