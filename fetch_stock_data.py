import requests
import pandas as pd
import json
import time
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('TORN_API_KEY')

def fetch_stock_data(api_key):
    url = f'https://api.torn.com/torn/?selections=stocks&key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

def store_data(data, filename='stock_data.csv'):
    stocks = []
    for stock_id, stock_data in data['stocks'].items():
        flat_data = {
            'stock_id': stock_id,
            'name': stock_data['name'],
            'acronym': stock_data['acronym'],
            'current_price': stock_data['current_price'],
            'market_cap': stock_data['market_cap'],
            'total_shares': stock_data['total_shares'],
            'investors': stock_data['investors'],
            'benefit_type': stock_data['benefit']['type'],
            'benefit_frequency': stock_data['benefit']['frequency'],
            'benefit_requirement': stock_data['benefit']['requirement'],
        }
        stocks.append(flat_data)
    df = pd.DataFrame(stocks)
    df.to_csv(filename, index=False)

# Fetch and store data
data = fetch_stock_data(api_key)
store_data(data)
