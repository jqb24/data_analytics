import quandl
import matplotlib.pyplot as plt
#mydata = quandl.get("FRED/GDP")
#mydata = quandl.get("WIKI/AAPL")

#mydata = quandl.get("EIA/PET_RWTC_D", collapse="monthly")
#quandl.ApiConfig.api_key = "4CyWwoB6xqwyTmLtvBRt"
#mydata = quandl.get_table('ZACKS/FC', ticker='AAPL')
#print(mydata.head())

import pandas_datareader as pdr
import pandas as pd
import datetime
import statsmodels.api as sm
tickers = []
def get(tickers):
    def data(ticker):
        return (pdr.get_data_yahoo(ticker))
    datas = map(data, tickers)
    return (pd.concat(datas, keys=tickers, names=['Ticker'])

aapl = pdr.get_data_yahoo('AAPL')

#Rule 3 - Buy Stocks Above Their 200-day Moving Average,Not Below
adjClose = pd.DataFrame(aapl['Adj Close'], index = aapl.index)
adjClose['ma'] = adjClose.rolling(window=200).mean()



#plt.plot(adjClose, 'blue', Mavg, 'red')
#plt.show()
df=pd.DataFrame(np.random.randn(10,4), index=range(10), columns=list('ABCD'))

#df.sort_index(axis=1, ascending=False)
df['GROUP'].isin([2,5])
df[df>0]=1
df.dropna(how='any')
df.fillna(value=5)
pd.isnull(df)
df2=[df[:3],df[:5]]
pd.concat(df2)
right=pd.DataFrame({'firstname': ['Henry', 'Jones','Indiana'], 'location': [1, 2,3]})
people.groupby('gender').min()
df["grade"].cat.categories = ["very good", "good", "very bad"]
df.groupby("grade").min()
ts.resample('D')
ts.shift(2)
offset.rollforward(now)

###
def get(tickers):
    def data(ticker):
        return (pdf.get_data_yahoo)
datas = map(data, tickers)
return (pd.concat(datas, keys=tickers, names=['Ticker'])