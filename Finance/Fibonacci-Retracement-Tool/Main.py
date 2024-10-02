import numpy as np
import matplotlib.pyplot as plt

class StockData:
    def __init__(self, prices):
        self.prices = prices
        self.high = max(prices)
        self.low = min(prices)

class FibonacciRetracement:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.levels = self.calculate_levels()

    def calculate_levels(self):
        # Fibonacci levels based on the high and low of the stock prices
        high = self.stock_data.high
        low = self.stock_data.low
        diff = high - low

        levels = {
            "23.6%": high - 0.236 * diff,
            "38.2%": high - 0.382 * diff,
            "50.0%": high - 0.500 * diff,
            "61.8%": high - 0.618 * diff,
            "78.6%": high - 0.786 * diff,
        }
        return levels

    def plot(self):
        # Plot the stock price and Fibonacci levels
        plt.plot(self.stock_data.prices, label="Stock Prices", color='black')

        for level in self.levels:
            plt.axhline(y=self.levels[level], label=f"{level} Retracement", linestyle='--')

        plt.title("Fibonacci Retracement Levels")
        plt.xlabel("Time")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Stock prices for simulation
    prices = [50, 55, 60, 58, 62, 64, 63, 67, 69, 70, 65, 63, 60, 58]

    stock_data = StockData(prices)

    # Calculate and plot Fibonacci retracement levels
    fib_retracement = FibonacciRetracement(stock_data)
    fib_retracement.plot()
