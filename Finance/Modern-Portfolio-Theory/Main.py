import numpy as np

class Asset:
    def __init__(self, name, expected_return, variance):
        self.name = name
        self.expected_return = expected_return
        self.variance = variance

class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def get_expected_returns(self):
        return np.array([asset.expected_return for asset in self.assets])

    def get_variances(self):
        return np.array([asset.variance for asset in self.assets])

    def get_covariance_matrix(self):
        size = len(self.assets)
        cov_matrix = np.zeros((size, size))
        for i in range(size):
            for j in range(size):
                if i == j:
                    cov_matrix[i][j] = self.assets[i].variance
                else:
                    # Placeholder for covariance between assets
                    cov_matrix[i][j] = np.random.uniform(0.01, 0.05)
        return cov_matrix

class PortfolioOptimizer:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def optimize(self, target_return):
        num_assets = len(self.portfolio.assets)
        cov_matrix = self.portfolio.get_covariance_matrix()
        expected_returns = self.portfolio.get_expected_returns()

        # Quadratic Programming setup: Minimize variance for a given return
        ones = np.ones(num_assets)
        inv_cov_matrix = np.linalg.inv(cov_matrix)

        # Calculating weights: Minimize (w.T * cov_matrix * w), subject to constraints
        A = np.dot(ones.T, np.dot(inv_cov_matrix, ones))
        B = np.dot(ones.T, np.dot(inv_cov_matrix, expected_returns))
        C = np.dot(expected_returns.T, np.dot(inv_cov_matrix, expected_returns))
        
        lambda_ = (C - B * target_return) / (A * C - B**2)
        gamma = (A * target_return - B) / (A * C - B**2)

        optimal_weights = lambda_ * np.dot(inv_cov_matrix, ones) + gamma * np.dot(inv_cov_matrix, expected_returns)
        return optimal_weights

# Example usage
if __name__ == "__main__":
    # Create assets with their expected returns and variances
    asset1 = Asset("Stock A", 0.12, 0.02)
    asset2 = Asset("Stock B", 0.08, 0.015)
    asset3 = Asset("Stock C", 0.10, 0.025)

    # Create a portfolio and add assets
    portfolio = Portfolio()
    portfolio.add_asset(asset1)
    portfolio.add_asset(asset2)
    portfolio.add_asset(asset3)

    # Create a Portfolio Optimizer and optimize for a given target return
    optimizer = PortfolioOptimizer(portfolio)
    target_return = 0.10
    optimal_weights = optimizer.optimize(target_return)

    print(f"Optimal Weights for Target Return {target_return}:")
    for i, asset in enumerate(portfolio.assets):
        print(f"{asset.name}: {optimal_weights[i]:.4f}")
