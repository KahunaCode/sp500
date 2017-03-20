import numpy as np
import pandas as pd
import pickle
from collections import Counter
from sklearn import svm, cross_validation, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier

def process_labels(ticker):
    hm_days =7
    df = pd.read_csv('sp500_all.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df

def bsh(*args):
    cols = [rec for rec in args]
    req = 0.02
    for col in cols:
        if col > req:
            return 1
        if col < -req:
            return -1
    return 0

def extract_featuresets(ticker):
    tickers, df = process_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(bsh,
                                              *[df['{}_{}d'.format(ticker, i)]for i in range(1,8)]))
    vals = df['{}_target'.format(ticker)].values.tolist()
    str_vals = [str(i) for i in vals]
    print('Data spread-', Counter(str_vals))
    
    df.fillna(0, inplace=True)
    df = df.replace([np.inf, -np.inf], np.nan)
    df.dropna(inplace=True)

    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals.values
    y = df['{}_target'.format(ticker)].values

    #print(X)
    return X,y,df

def mlearn(ticker):
    #X is percent change, y is target classification: 1,-1,0
    X, y, df = extract_featuresets(ticker)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.25)

    clf = neighbors.KNeighborsClassifier()
    #sklearn has flags for linearSVC, KNN, random forest
    clf = VotingClassifier([('lsvc', svm.LinearSVC()),
                            ('knn', neighbors.KNeighborsClassifier()),
                            ('rfor', RandomForestClassifier())])

    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print('Accuracy', confidence)
    predictions = clf.predict(X_test)
    print('Predicted spread:', Counter(predictions))

    return confidence

mlearn('MMM')



