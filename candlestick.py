import yfinance as yf
import mplfinance as mpf

# Fetch stock ticker input
ticker = input("Enter the stock name: ")

# Download stock data for the given date range
df = yf.download(ticker, start='2023-08-01', end='2024-09-01')

# Ensure the title and ylabel are passed in a dictionary (kwargs style)
mpf.plot(df, type='candle', style='charles', 
         title=f'{ticker} Candlestick Chart', ylabel='Price')
