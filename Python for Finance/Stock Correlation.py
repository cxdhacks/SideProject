import pandas as pd 
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf
from statsmodels import api as sm
from scipy.stats import linregress


stocks =['AAPL','MSFT','FB','GME','TSLA','AMZN']
stock_list = []
for stock in stocks:
  returns = yf.Ticker(stock)
  returns = returns.history(period="1y")
  returns['returns'] =  returns['Close'].pct_change()

  returns.rename(columns={'returns': stock}, inplace=True) # name columns with company's name
  returns = returns[stock] # transform from column of dataframe to Seires
  stock_list.append(returns) # Series 也可以是 list 的成分

all_stock_returns = pd.DataFrame(stock_list).T

#statistics
all_stock_returns.describe()
#calculate correlation
correlation = all_stock_returns.corr()
sm.graphics.plot_corr(correlation,xnames=list(correlation.columns))

all_stock_returns = all_stock_returns.iloc[1:] # 切去 NaN
print(linregress(all_stock_returns['AAPL'],all_stock_returns['MSFT'])) # 如果不切去 NaN 那么这里是 run 不出结果的
print(linregress(all_stock_returns['AAPL'],all_stock_returns['GME']))