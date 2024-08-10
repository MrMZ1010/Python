import pandas as pd  
import numpy as np  
import yfinance as yf  
import datetime  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  
import matplotlib.pyplot as plt  

# Getting today's date and date four years ago
today = datetime.date.today()
four_years_ago = today - datetime.timedelta(days=4 * 365)

# Downloading gold futures data from Yahoo Finance and saving it to a CSV file
data = yf.download("GC=F", start=four_years_ago, end=today)
data.to_csv('gold_futures.csv')

# Shifting Close prices by one day to get the previous day's price and dropping NaN values
data['Previous_Price'] = data['Close'].shift(1)
data = data.dropna()

# Defining features (X) and target variable (y)
X = data[['Previous_Price']]
y = data['Close']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and fitting the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Calculating evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Printing evaluation metrics
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
print(f'R^2 Score: {r2}')

# Plotting the predictions against the actual values
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title('Gold Price Prediction')
plt.xlabel('Previous Price')
plt.ylabel('Price')
plt.show()
