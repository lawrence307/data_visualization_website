import pandas as pd
import os
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# Download historical data for a specific stock
ticker = 'SCOM'
data = yf.download(ticker, start='2020-01-01', end='2024-01-01')
print(data.head())
data.to_csv('SCOM_HistoricalPrices.csv')
df = pd.read_csv('SCOM_HistoricalPrices.csv')

# Display the first few rows of the dataset
print(df.tail())
#check the datatypes and missing values
print(df.info())
print(df.isnull().sum())
print(df.columns)
df.columns = df.columns.str.strip()
print("Columns after stripping:", df.columns)
#summary
print(df.describe())
#check for duplicates
print(df.duplicated().sum())
#display hist
df.hist(figsize=(10, 10))
plt.show()

# Standardize date format and string columns
df['Date'] = pd.to_datetime(df['Date'])

# Handle missing data
df = df.dropna()  # or use df['column_name'] = df['column_name'].fillna(df['column_name'].mean())


print(df.head())
print(df.info())



