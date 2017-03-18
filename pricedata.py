import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015,1,1)
stop = dt.datetime(2017,2,28)

df = web.DataReader('TNP', 'yahoo', start, stop)


print(df.tail())
