import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#query yahoo api for TNP
##start = dt.datetime(2015,1,1)
##stop = dt.datetime(2017,2,28)
##
##df = web.DataReader('TNP', 'yahoo', start, stop)
##print(df.tail())
##df.to_csv('tnp.csv')

df = pd.read_csv('tnp.csv', parse_dates=True, index_col=0)

#plot closing prices
#print(df['Adj Close'].tail())
#df['Adj Close'].plot()
#plt.show()

df['100_moving_avg'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)#drops NaN's without redoing df
print(df.head())

