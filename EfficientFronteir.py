import pandas as pd
import quandl
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
table = data[0]
sliced_table = table[1:]
header = table.iloc[0]

corrected_table = sliced_table.rename(columns=header)
tickers = corrected_table['Ticker symbol'].tolist()
#print (tickers)


quandl.ApiConfig.api_key = "4CyWwoB6xqwyTmLtvBRt"
# get adjusted closing prices of 5 selected companies with Quandl
#quandl.ApiConfig.api_key = 'PASTE YOUR API KEY HERE'
selected = ['CNP', 'F', 'WMT', 'GE', 'TSLA']
data = quandl.get_table('WIKI/PRICES', ticker = selected,
                        qopts = { 'columns': ['date', 'ticker', 'adj_close'] },
                        date = { 'gte': '2014-1-1', 'lte': '2016-12-31' }, paginate=True)

clean = data.set_index('date')
print(clean.head())
table = clean.pivot(columns='ticker')