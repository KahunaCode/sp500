import pickle
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

def compile_tickers():
    with open("sp500tickers.pickle", "rb") as f:
        tickers = pickle.load(f)

    df_all = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        df = pd.read_csv('stocks/{}.csv'.format(ticker))
        df.set_index('Date', inplace=True)

        df.rename(columns = {'Adj Close':ticker}, inplace=True)
        df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

        if df_all.empty:
            df_all = df
        else:
            df_all = df_all.join(df, how='outer')

        if count % 10 == 0:
            print(count)

    print(df_all.head())
    df_all.to_csv('sp500_all.csv')

#compile_tickers()

def visualize_data():
    df = pd.read_csv('sp500_all.csv')
##    df['MMM'].plot()
##    plt.show()
    df_corr = df.corr()
    print(df_corr.head())

    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1)
    plt.tight_layout()
    plt.show()

visualize_data()
