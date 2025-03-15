import requests
import json
# Function to get live stock data for a symbol


def get_stock_data(ticker):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + {ticker} + "&interval=5min&outputsize=compact&apikey=M0N0LCYG3J1OHGQY"
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        print(data)
        # last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        # price = data["Time Series (5min)"][last_refreshed]["1. open"]
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return data
    else:
        return None


# stock_prices = {}
symbol = "SPY"
latest_price = "Time Series (5min)"
data = get_stock_data(symbol)

if data is not None:
    stock_prices = data[latest_price]


print(f"{symbol}: {data}")
