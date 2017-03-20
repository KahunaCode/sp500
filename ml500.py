import numpy as np
import pandas as pd
import pickle
from collections import Counter

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

def extract_featuresets(ticker):
    tickers, df = process_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(bsh,
                                              *[df['{}_{}d'.format(ticker, i)]for i in range(1,8)]))
    vals = df['{}_target'.format(ticker)]
    str_vals = [str(i) for i in vals]
    print('Data spread-', Counter(str_vals))
    
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    
