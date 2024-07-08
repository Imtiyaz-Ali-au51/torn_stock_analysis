import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('stock_data.csv')

# Inspect the data
print(df.head())
print(df.info())
print(df.describe())

# Handle missing values (if any)
# For simplicity, let's forward-fill missing values
df.fillna(method='ffill', inplace=True)

# Ensure correct data types
df['current_price'] = df['current_price'].astype(float)
df['market_cap'] = df['market_cap'].astype(float)
df['total_shares'] = df['total_shares'].astype(int)
df['investors'] = df['investors'].astype(int)

# Feature Engineering: Create new features
df['price_to_market_cap'] = df['current_price'] / df['market_cap']
df['investor_growth'] = df['investors'].pct_change().fillna(0)

# Save the preprocessed data for future use
df.to_csv('preprocessed_stock_data.csv', index=False)

print("Data preprocessing completed and saved to 'preprocessed_stock_data.csv'")
