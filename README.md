# s&p500 graphing and machine learning 

pricedata.py uses the Pandas / pandas_data reader to query the yahoo api for stock ticker data for a date range. It then computes a moving average and plots all the data with matplotlib.

ohlc.py is Open High Low Close. This takes the data from pricedata.py and computes a candlestick plot, again using pandas and matplotlib, to represent the dataframe.

sp500tickers.py queries Wikipedia for the S&P500 list using Beautiful Soup, and pickles the data. The get_data function then uses Pandas datareader to query for each ticker extracted from the bs4 query, and saves it to a CSV. This query will take 10-20minutes depending on your ISP.

compile_sp500.py takes all of the data you just pulled, reformats it into a nice Pandas df, and outputs it to a csv. The visualize function is using pandas correlation method and matplotlib to display positive and negative correlations

ml500.py uses sklearn machine learning algorithms to predict instances of buy, sell, or holding a stock and calculates an accuracy. process_labels is preparing the data and converting it to percentages, bsh is buy-sell-hold and it labels each ticker, extract_featuresets takes the ticker and creates the dataset labels returning the featuresets and targets, and finally mlearn runs three algorithms against a training dataset and then outputs answers against a test dataset.

thanks to pandas and the pandas data reader for making this much easier, except when having to constantly clean dataframes, and thanks to safari books and python programming for the examples, and of course wikipedia.
