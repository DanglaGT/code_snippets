
import quandl as q
import pandas as pd

q.ApiConfig.api_key = "yVb16ih1yQsv1Xz1MsV_"
q.ApiConfig.api_version = '2015-04-09'

#data = q.get("FRED/GDP",returns="pandas")
#data = q.get_table('ZACKS/FC', ticker='AAPL')
#data = q.get_table('ZACKS/FC')
#data = q.get('YAHOO/INDEX_GSPC')
#data = q.get('GOOG/NASDAQ_AAPL', paginate=True)
#data = q.get('SF0/AGX_EPSDIL_MRY', paginate=True)
#data = q.get('SF0/AGX_DEBTUSD_MRY', paginate=True)
#data = q.get('SF0/AGX_DE_MRY', paginate=True)
#data = q.get_table('ZACKS/FC', paginate=True)
#data = q.get_table('WIKI/PRICES', paginate=True)
data = q.get_table('WIKI/PRICES', ticker="AGX", date='2017-06-7')

print(data.head())
print(data.tail())

#mydata = quandl.get("FRED/GDP")
