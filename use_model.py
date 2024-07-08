import joblib
import pandas as pd

# Load the trained model
model = joblib.load('stock_price_model.pkl')

# Load the preprocessed data or new data for prediction
df = pd.read_csv('preprocessed_stock_data.csv')

# Prepare features for prediction (example using the same dataset)
X_new = df[['market_cap', 'total_shares', 'investors', 'price_to_market_cap', 'investor_growth']]

# Make predictions
predictions = model.predict(X_new)

# Output predictions
print(predictions)
