import requests

def get_stock_price(symbol):
    api_url = f"https://api.example.com/stocks/{symbol}/price"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()['price']
    else:
        raise Exception(f"Failed to fetch data for {symbol}: {response.status_code}")

if __name__ == "__main__":
    symbol = "AAPL"
    try:
        price = get_stock_price(symbol)
        print(f"The current price of {symbol} is ${price}")
    except Exception as e:
        print(e)
