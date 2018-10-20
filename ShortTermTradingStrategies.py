import pandas_datareader as pdr
import pandas as pd
import datetime
import statsmodels.api as sm

tickers = []
aapl=pdr.get_data_yahoo('AAPL')

# Backtest 1 - Buy Stocks Above Their 200-day Moving Average,Not Below
adjClose = pd.DataFrame(aapl['Adj Close'], index=aapl.index)
adjClose['ma'] = adjClose.rolling(window=200).mean()
adjClose['pct_chg'] = adjClose['Adj Close'].pct_change(periods=50)
adjClose['pct_chg']=adjClose['pct_chg'].shift(-50)
#new_df = adjClose.apply(lambda x: x['Adj Close'].pct_change() if  )
#df[(df.x1 > 50)|(df.x2 > 50)
buyUps = adjClose[adjClose['Adj Close']>adjClose['ma']]
#print(buyUps.describe())

buyDowns = adjClose[adjClose['Adj Close']<adjClose['ma']]
#print(buyDowns.describe())


# Backtest 2 - Use the VIX to Your Advantage ... Buy the Fear, Sell the Greed
# %5 VIX Rule: Whenever the VIX has been 5% or more above its 10-day MA,
# the S&F 500 has achieved returns which are better than 2-1 compared to
# the average weekly returns of all weeks.

rule4 = pd.DataFrame(data ={'spy':pdr.get_data_yahoo('SPY')['Adj Close'], 'vix':pdr.get_data_yahoo('^VIX')['Adj Close']})
rule4['spypct_chg'] = rule4.spy.pct_change(periods=7)
rule4['spypct_chg'] = rule4['spypct_chg'].shift(-7)
rule4['vix_ma'] = rule4.vix.rolling(window=10).mean()
buys=rule4[rule4.vix>=1.05*rule4['vix_ma']]
sells=rule4[rule4.vix<=1.05*rule4['vix_ma']]
#print(buys.describe())
#print(sells.describe())

# Backtest 3 - It Pays to Hold Positions Overnight

#print(aapl.head())
spy = pd.DataFrame(data={'spy_open': pdr.get_data_yahoo('SPY')['Open'], 'spy_close': pdr.get_data_yahoo('SPY')['Close']})
spy['DayReturn'] = (spy['spy_close']-spy['spy_open'])/spy['spy_open']
spy['overnight'] = spy['spy_close'].shift(1)

spy['overnight'] = (spy['overnight']-spy['spy_open'])/spy['overnight']
#print(spy['overnight'].describe())
#print(spy['DayReturn'].describe())


# Backtest 4 Trading with Intra-day Drops Making Edges Even Bigger
#1. Stock closes at a IO-period high and is above its 200-day simple moving average (a momentum move in a longer term uptrend).
#2. Average volume over the past 100 days is at least 250,000 shares per day.
#3. Price is greater than $5 per share.
#4. Buy on the close.
#5. Exit on the close 5 trading days later.
#vs
#Test 2 - Buyinginto Further Weakness Intra-day
#1. Stock closes at a 10-period low and is above its 200-day simple moving average (a pullback within a longer term uptrend).
#2. Average volume over the past 100-days is at least 250,000 shares per day.
#3. Price is greater than $5 per share.
#4. Buy on the close.
#5. Exit on the close 5 trading days later.
test4 = pdr.get_data_yahoo('SPY')
test4['ma'] = test4['Adj Close'].rolling(200).mean()
test4['vol_avg'] = test4['Volume'].rolling(200).mean()
test4['pct_chg'] = test4['Adj Close'].pct_change(periods=5)
test4['10dayhigh'] = test4['Adj Close'].rolling(10).max()
test4['10daylow'] = test4['Adj Close'].rolling(10).min()
buys1 = test4[(test4['Adj Close'] > test4.ma) & (test4.vol_avg>250000) & (test4['Adj Close']>5) & (test4['Adj Close']==test4['10dayhigh'])]
#print(buys.head(15))
buys2 = test4[(test4['Adj Close'] > test4.ma) & (test4.vol_avg>250000) & (test4['Adj Close']>5) & (test4['Adj Close']==test4['10daylow'])]

#print(buys1['pct_chg'].describe().mean)
#print(buys2['pct_chg'].describe().mean)

# Backtest 5 The 2-period RSI The Trader's Holy Grail of Indicators?
#1. TheS&P500indexisaboveits200-daymovingaverage.
#2. The 2-period R51ofthe5&P500Indexclosesbelow5.
##3. Buy the 5&1' on the close.
#4. ExitwhentheS&Pclosesaboveits5-periodmovingaverage.
test5 = pdr.get_data_yahoo('SPY')
test4['ma200'] = test4['Adj Close'].rolling(200).mean()
test4['ma5'] = test4['Adj Close'].rolling(5).mean()
test5['diff'] = test4['Adj Close'].diff()
test4['pct_chg'] = test4['Adj Close'].pct_change(periods=5)
#print(test5.head())
def getRSI(d):
    return d[d>0].mean()
    down = d[d < 0].mean()
    return 100-100/(1+up/down)
#print(getRSI(test5['diff']))

test5['rsiscore']=test5['diff'].rolling(2).apply(getRSI)
#print(test5)

# Backtest 6 Double 7s strategy
#1 . The SPY i s above its 200-day moving average
#2. IftheSPYclosesata7-daylow,buy.
#3. If the SPY closes at a 7-day high, sell your long position.
test6 = pdr.get_data_yahoo('SPY')
test6['ma200'] = test6['Adj Close'].rolling(200).mean()
test6['low7'] = test6['Adj Close'].rolling(7).min()
test6['high7'] = test6['Adj Close'].rolling(7).max()
a=['goal']
p=([i for i in a])
