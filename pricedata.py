import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
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

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100_moving_avg'])
ax2.bar(df.index, df['Volume'])

plt.show()

