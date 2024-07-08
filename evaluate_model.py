import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the preprocessed data (ensure this is the same as used for training)
df = pd.read_csv('preprocessed_stock_data.csv')

# Prepare the actual values (assuming you have the actual current prices for evaluation)
y_actual = df['current_price']

# Load the trained model
import joblib
model = joblib.load('stock_price_model.pkl')

# Prepare features for prediction (example using the same dataset)
X_new = df[['market_cap', 'total_shares', 'investors', 'price_to_market_cap', 'investor_growth']]

# Make predictions
predictions = model.predict(X_new)

# Evaluate the model
mae = mean_absolute_error(y_actual, predictions)
mse = mean_squared_error(y_actual, predictions)
r2 = r2_score(y_actual, predictions)

print(f"Mean Absolute Error: {mae}")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Interpretation
evaluation_results = pd.DataFrame({
    'Actual': y_actual,
    'Predicted': predictions,
    'Error': y_actual - predictions
})
print(evaluation_results.head(10))
