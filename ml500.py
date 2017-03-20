import numpy as np
import pandas as pd
import pickle

def process_labels(ticker):
    hm_days =7
    df = pd.read_csv('sp500_all.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker])-df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df

def bsh(*args):
    cols = [rec for rec in args]
    req = 0.02
    for col in cols:
        if col > req:
            return 1
        if col < -reg:
            return -1
    return 0

