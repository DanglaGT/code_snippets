
# this snippet of code pulls OHLC & volume information between
# the dates specified from google finance and places it into
# a pandas dataframe

# you can loop through stocklist, but i need to figure out
# how to put them into different dataframes for each stock
# in the list

# i also want to figure out how to pull a list of all stocks
# from online so i can run them each through a screener program
# that i will develop

import pandas_datareader.data as web
import pandas as pd
import datetime as dt

start = dt.date(2016,1,1)
end = dt.date.today()

stocklist = ["HSKA"]

for stock in stocklist:

    print("")
    print("-" * 50)
    print("OHLC & Volume Data for " + stock)
    print("-" * 50 + "\n")

    x = web.DataReader("HSKA", 'google', start, end)
    print(x.tail())
