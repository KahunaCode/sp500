import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web

def sp500_tickers():
    response = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = bs.BeautifulSoup(response.text, "lxml")
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#sp500_tickers()

def get_data(reload=False):
    if reload:
        tickers = sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    if not os.path.exists('stocks'):
        os.makedirs('stocks')

    start = dt.datetime(2010,1,1)
    stop = dt.datetime(2016,12,31)

    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stocks/{}.csv'.format(ticker)):
            df = web.DataReader(ticker, 'yahoo', start, stop)
            df.to_csv('stocks/{}.csv'.format(ticker))
        else:
            print('{} exists'.format(ticker))

get_data()
