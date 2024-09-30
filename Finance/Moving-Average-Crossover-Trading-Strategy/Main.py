import numpy as np


class MovingAverage:
    def __init__(self, window_size):
        self.window_size = window_size
        self.prices = []
        self.sum = 0

    def add_price(self, price):
        self.prices.append(price)
        self.sum += price
        
        
        if len(self.prices) > self.window_size:
            self.sum -= self.prices.pop(0)

    def get_average(self):
        if len(self.prices) == 0:
            return None
        return self.sum / len(self.prices)

class TradingStrategy:
    def __init__(self, short_window, long_window):
        self.short_ma = MovingAverage(short_window)
        self.long_ma = MovingAverage(long_window)
        self.position = 0  # 0 = no position, 1 = long, -1 = short

    def add_price(self, price):
        self.short_ma.add_price(price)
        self.long_ma.add_price(price)
        
        short_avg = self.short_ma.get_average()
        long_avg = self.long_ma.get_average()
        
        if short_avg is None or long_avg is None:
            return "Waiting for data..."
        
        if short_avg > long_avg and self.position <= 0:
            self.position = 1
            return f"Buy signal at {price}"
        elif short_avg < long_avg and self.position >= 0:
            self.position = -1
            return f"Sell signal at {price}"
        else:
            return f"Hold at {price}"

def simulate_trading(prices, short_window=5, long_window=10):
    strategy = TradingStrategy(short_window, long_window)
    signals = []
    
    for price in prices:
        signal = strategy.add_price(price)
        signals.append(signal)
        
    return signals
    
# Example usage
if __name__ == "__main__":
    # Simulating with sample price data
    prices = np.random.uniform(100, 200, 50)  # Randomly generated prices
    signals = simulate_trading(prices)
    
    for i, signal in enumerate(signals):
        print(f"Day {i + 1}: {signal}")
