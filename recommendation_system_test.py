import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd

def download_data(ticker, start_date, end_date):
    asset = yf.Ticker(ticker)
    data = asset.history(start=start_date, end=end_date)
    return data

data = download_data("AAPL", "2010-01-01", "2023-10-31")
print(data.head())

def plot_line(data, title, ylabel):
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"])
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()

plot_line(data, "Apple Inc. Stock Prices", "Closing Price")

def plot_candlestick(data, title):
    mpf.plot(data, type="candle", title=title, ylabel="Price")

plot_candlestick(data, "Apple Inc. Candlestick Chart")

def plot_candlestick(data, title):
    mpf.plot(data, type="candle", title=title, ylabel="Price", mav=(20, 50))

plot_candlestick(data, "Apple Inc. Candlestick Chart with Moving Averages")

class User:
    def __init__(self, name, risk_tolerance, investment_horizon):
        self.name = name
        self.risk_tolerance = risk_tolerance
        self.investment_horizon = investment_horizon

class RecommendationSystem:
    def __init__(self, user, data):
        self.user = user
        self.data = data

    # ...

    def get_recommendation(self):
        filtered_assets = self.data[self.data["Close"].notna()]
        returns = filtered_assets["Close"].pct_change()
        average_returns = returns.mean()
        filtered_assets = pd.DataFrame(average_returns[average_returns <= self.user.risk_tolerance])
        sorted_assets = filtered_assets.sort_values(by=0, ascending=False)
        top_assets = sorted_assets.head(self.user.investment_horizon)
        return top_assets.index.tolist()

user = User("John Doe", 0.02, 5)
recommendation_system = RecommendationSystem(user, data)
recommendation = recommendation_system.get_recommendation()

print(f"Recommended assets for {user.name}: {recommendation}")
