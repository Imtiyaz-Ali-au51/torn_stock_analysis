import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load the preprocessed data
df = pd.read_csv('preprocessed_stock_data.csv')

# Prepare features and target variable
# Let's assume we want to predict the current_price
X = df[['market_cap', 'total_shares', 'investors', 'price_to_market_cap', 'investor_growth']]
y = df['current_price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)
print(f'Mean Absolute Error: {mae}')

# Save the trained model (optional, for future use)
import joblib
joblib.dump(model, 'stock_price_model.pkl')

print("Model training completed and saved as 'stock_price_model.pkl'")
