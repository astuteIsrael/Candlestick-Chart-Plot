# Stock Candlestick Chart Visualization

## Overview
This python code provides a tool to visualize historical stock data using candlestick charts. Users can input the stock ticker symbol, and the program will download data from Yahoo Finance for the specified date range. The resulting candlestick chart is displayed using the `mplfinance` library.

## Features
- Fetches historical stock data for any stock using the Yahoo Finance API.
- Visualizes stock data as a candlestick chart.
- Allows users to input stock ticker symbols.
- Customizable date range for data fetching.

## Prerequisites
Before running the project, ensure you have the following libraries installed:

- `yfinance`: For downloading stock data
- `mplfinance`: For generating candlestick charts

You can install them using pip:

cmd:
  pip install yfinance mplfinance

##  Customization
  You can customize the date range by modifying the start and end parameters in the script:
  df = yf.download(ticker, start='2023-08-01', end='2024-09-01')
