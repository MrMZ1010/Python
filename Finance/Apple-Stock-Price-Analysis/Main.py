import yfinance as yf  
import pandas as pd  
import matplotlib.pyplot as plt 
import seaborn as sns  
import datetime  

tickerSymbol = 'AAPL'  # Defining the stock ticker symbol
tickerData = yf.Ticker(tickerSymbol)  # Getting data for the specified ticker symbol
today = datetime.date.today()  # Getting today's date
four_years_ago = today - datetime.timedelta(days=4 * 365)  # Calculating the date four years ago
tickerDf = tickerData.history(period='4y', start=four_years_ago, end=today)  # Getting historical stock data for the past four years

# Calculating moving averages for 20, 50, and 100 days
tickerDf['MA20'] = tickerDf['Close'].rolling(window=20).mean()
tickerDf['MA50'] = tickerDf['Close'].rolling(window=50).mean()
tickerDf['MA100'] = tickerDf['Close'].rolling(window=100).mean()

# Calculating daily returns
tickerDf['Daily_Return'] = tickerDf['Close'].pct_change()

# Calculating cumulative returns
tickerDf['Cumulative_Return'] = (1 + tickerDf['Daily_Return']).cumprod()

# Creating a figure with specified size for plotting multiple graphs
plt.figure(figsize=(12, 10))

# Plot 1: Stock Price Analysis
plt.subplot(3, 1, 1)  # Creating subplot 1 in a 3x1 grid
plt.plot(tickerDf['Close'], label='Close Price')
plt.plot(tickerDf['MA20'], label='20-Day Moving Average')
plt.plot(tickerDf['MA50'], label='50-Day Moving Average')
plt.plot(tickerDf['MA100'], label='100-Day Moving Average')
plt.title('Stock Price Analysis for ' + tickerSymbol)
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Plot 2: Distribution of Daily Returns
plt.subplot(3, 1, 2)  # Creating subplot 2 in a 3x1 grid
sns.histplot(tickerDf['Daily_Return'].dropna(), bins=100, kde=True, color='blue')
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')

# Plot 3: Cumulative Returns
plt.subplot(3, 1, 3)  # Creating subplot 3 in a 3x1 grid
plt.plot(tickerDf['Cumulative_Return'], label='Cumulative Returns', color='green')
plt.title('Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.legend()

plt.tight_layout()  # Adjust layout to prevent overlap of subplots
plt.show()  # Displaying all subplots
