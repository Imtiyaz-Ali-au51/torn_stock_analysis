from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

print("Loading model...")
# Load the trained model
model = joblib.load('stock_price_model.pkl')
print("Model loaded.")

@app.route('/predict', methods=['POST'])
def predict():
    print("Received request for prediction.")
    data = request.get_json()
    # Convert the data into a DataFrame
    input_data = pd.DataFrame(data)
    # Prepare features
    features = input_data[['market_cap', 'total_shares', 'investors', 'price_to_market_cap', 'investor_growth']]
    # Make prediction
    prediction = model.predict(features)
    # Return the prediction as a JSON response
    return jsonify(prediction.tolist())

if __name__ == '__main__':
    print("Running Flask app directly...")
    app.run(debug=True)
