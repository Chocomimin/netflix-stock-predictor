# -*- coding: utf-8 -*-
"""stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r9CcxnGS033BXKiDU3sUzhN93WY1HMFA

# Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error, r2_score

"""# Loading Dataset"""

file_path = 'NFLX (3).csv'
df = pd.read_csv(file_path)

df.head()

df.describe()

df.info()

"""# Displaying Dataset Information"""

df.isnull().sum()
df.shape
df.info()
df.describe().T

"""# Splitting the Dataset"""

train, test = train_test_split(df, test_size=0.2, random_state=42)

"""#  Extracting Features and Target"""

x_train = train[['Open', 'High', 'Low', 'Volume']].values
x_test = test[['Open', 'High', 'Low', 'Volume']].values
y_train = train['Close'].values
y_test = test['Close'].values

"""# Creating and Training Linear Regression Model"""

model_lnr = LinearRegression()
model_lnr.fit(x_train, y_train)
y_pred = model_lnr.predict(x_test)

"""# Evaluating the Model"""

print("MSE", round(mean_squared_error(y_test, y_pred), 3))
print("RMSE", round(np.sqrt(mean_squared_error(y_test, y_pred)), 3))
print("MAE", round(mean_absolute_error(y_test, y_pred), 3))
print("MAPE", round(mean_absolute_percentage_error(y_test, y_pred), 3))
print("R2 Score: ", round(r2_score(y_test, y_pred), 3))

"""# Plotting Closing Stock Price"""

plt.figure(facecolor='black', figsize=(15, 10))
ax = plt.axes()
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')
ax.set_facecolor("black")
plt.title('Closing Stock Price', color="white")
plt.plot(df['Date'], df['Close'], color="#94F008")
plt.legend(["Close"], loc="lower right", facecolor='black', labelcolor='white')

"""# Saving Predictions to CSV"""

test_pred = test.copy()
test_pred['Close_Prediction'] = y_pred
test_pred[['Date', 'Close', 'Close_Prediction']].to_csv('Close_Prediction.csv', index=False)

"""# Displaying Predictions"""

test_pred.head()

"""# Function for Predicting Stock Price"""

# Get user inputs for stock prediction
open_input = float(input("Enter the opening stock price: "))
high_input = float(input("Enter the highest stock price: "))
low_input = float(input("Enter the lowest stock price: "))
volume_input = float(input("Enter the stock volume: "))

# Function for Predicting Stock Price
def predict_stock_price(open_val, high_val, low_val, volume_val):
    # Ensure the input values are in the correct format
    input_values = np.array([[open_val, high_val, low_val, volume_val]])

    # Use the trained model to make predictions
    predicted_close = model_lnr.predict(input_values)

    return predicted_close[0]

# Use user inputs in the prediction function
predicted_close_output = predict_stock_price(open_input, high_input, low_input, volume_input)

print(f"Predicted Close Price: {predicted_close_output}")

import pickle

# Save the trained model to a pickle file
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model_lnr, model_file)