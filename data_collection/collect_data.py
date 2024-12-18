import requests
import pandas as pd

def get_stock_data():
    api_key = 'YOUR_API_KEY'
    ticker = 'AAPL'
    base_url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={api_key}'
    response = requests.get(base_url)
    data = response.json()
    return pd.DataFrame(data['historical'])
