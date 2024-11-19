import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("/content/drive/MyDrive/lab 8/infy_stock.csv")
data.head(10)
print("\nMissing values in the dataset:")
print(data.isnull().sum())
data_cleaned = data.dropna()
print("\nNumber of rows after dropping missing values:", len(data_cleaned))
# Data Visualization: Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(pd.to_datetime(data_cleaned['Date']), data_cleaned['Close'], label='Closing Price')
plt.title('Stock Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()
import mplfinance as mpf
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'])
data_cleaned.set_index('Date', inplace=True)
data_cleaned_forplot= data_cleaned[['Open', 'High', 'Low', 'Close', 'Volume']]
mpf.plot(data_cleaned_forplot, type='candle', mav=(50, 200), volume=True,title='INFY Stock Prices Candlestick Chart', style='charles')
#stastical Analysis

# 1. Daily Return Percentage
data_cleaned.loc[:, 'Daily_Return %'] = ((data_cleaned['Close'] - data_cleaned['Open']) / data_cleaned['Open']) * 100
# Calculate the average, median, and standard deviation of daily returns
average_return = data_cleaned['Daily_Return %'].mean()
median_return = data_cleaned['Daily_Return %'].median()
std_dev_close = data_cleaned['Close'].std()
print(f"\nAverage Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")
print(f"Standard Deviation of Closing Prices: {std_dev_close:.2f}")
# 4  Moving Averages: Calculate 50-day and 200-day moving averages
data_cleaned['50-day MA'] = data_cleaned['Close'].rolling(window=50).mean()
data_cleaned['200-day MA'] = data_cleaned['Close'].rolling(window=200).mean()


# 5. Volatility (rolling standard deviation with 30-day window)
data_cleaned['Volatility'] = data_cleaned['Close'].rolling(window=30).std()


# Plot the Moving Averages
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned.index, data_cleaned['Close'], label='Close Price', color='blue')
plt.plot(data_cleaned.index, data_cleaned['50-day MA'], label='50-Day MA', color='green')
plt.plot(data_cleaned.index, data_cleaned['200-day MA'], label='200-Day MA', color='red')
plt.title('INFY Stock Price with Moving Averages')
plt.legend()
plt.show()

# Plot the Volatility
plt.figure(figsize=(10, 6))
plt.plot(data_cleaned.index, data_cleaned['Volatility'], label='30-Day Volatility', color='purple')
plt.title('INFY Stock Price Volatility (30-Day Rolling Std)')
plt.legend()
plt.show()

# 6. Trend Analysis (Bullish/Bearish based on 50-day vs. 200-day MA)
# Bullish trend: 50-day MA > 200-day MA, Bearish trend: 50-day MA < 200-day MA
data_cleaned['Trend'] = ['Bullish' if data_cleaned['50-day MA'].iloc[i] > data_cleaned['200-day MA'].iloc[i] else 'Bearish' for i in range(len(data_cleaned))]

