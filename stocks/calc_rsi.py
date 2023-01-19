import pandas as pd
import talib

# Load the stock data into a DataFrame
data = pd.read_csv('TSLA.csv')

# Define the number of days to use in the RSI calculation
period = 14

# Calculate the relative strength index (RSI) using the 'ta-lib' library
data['rsi'] = round(talib.RSI(data['Close'], timeperiod=period), 2)

# Print the RSI values
data.to_csv('TSLA.csv', index=False)
