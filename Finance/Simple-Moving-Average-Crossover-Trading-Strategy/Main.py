import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TradingStrategy:
    def __init__(self, prices, short_window, long_window):
        self.prices = prices
        self.short_window = short_window
        self.long_window = long_window
        self.signals = self.generate_signals()

    def generate_signals(self):
        signals = pd.DataFrame(index=self.prices.index)
        signals['price'] = self.prices
        signals['short_mavg'] = self.prices['Close'].rolling(window=self.short_window, min_periods=1).mean()
        signals['long_mavg'] = self.prices['Close'].rolling(window=self.long_window, min_periods=1).mean()

        # Create signals
        signals['signal'] = 0
        signals['signal'][self.short_window:] = np.where(
            signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1, 0
        )

        # Generate trading orders
        signals['positions'] = signals['signal'].diff()

        return signals

    def plot_signals(self):
        plt.figure(figsize=(14, 7))
        plt.plot(self.prices['Close'], label='Close Price', alpha=0.5, color='blue')
        plt.plot(self.signals['short_mavg'], label='Short Moving Average', alpha=0.75, color='orange')
        plt.plot(self.signals['long_mavg'], label='Long Moving Average', alpha=0.75, color='green')

        # Plot buy signals
        plt.plot(self.signals[self.signals['positions'] == 1].index,
                 self.signals['short_mavg'][self.signals['positions'] == 1],
                 '^', markersize=12, color='lime', label='Buy Signal')

        # Plot sell signals
        plt.plot(self.signals[self.signals['positions'] == -1].index,
                 self.signals['short_mavg'][self.signals['positions'] == -1],
                 'v', markersize=12, color='red', label='Sell Signal')

        plt.title('Trading Strategy - SMA Crossover', fontsize=16)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Price', fontsize=14)
        plt.ylim(bottom=0)  
        plt.xticks(rotation=45)  
        plt.legend()
        plt.grid()
        plt.tight_layout()  
        plt.show()

# Example usage
if __name__ == "__main__":
    # Simulating a more dynamic stock price data using a sine wave and noise
    np.random.seed(42)  # For reproducibility
    dates = pd.date_range(start='2022-01-01', periods=100)
    prices = pd.DataFrame(index=dates)
    prices['Close'] = 100 + (10 * np.sin(np.linspace(0, 3 * np.pi, len(dates)))) + np.random.normal(0, 1, len(dates)).cumsum()

    # Parameters for the SMA strategy
    short_window = 5
    long_window = 20

    # Initialize trading strategy
    trading_strategy = TradingStrategy(prices, short_window, long_window)
    trading_strategy.plot_signals()
