import pickle
import pandas as pd

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

compile_tickers()
