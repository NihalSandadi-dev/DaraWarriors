import requests
import json
# Function to get live stock data for a symbol


def get_stock_data(ticker):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + ticker + "&interval=5min&outputsize=compact&apikey=M0N0LCYG3J1OHGQY"
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        # print(data)
        # last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        # price = data["Time Series (5min)"][last_refreshed]["1. open"]
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return data
    else:
        return None

def get_latest_price(data):
    close_value = 0

    if data is not None:
        first_element_key = list(data["Time Series (5min)"].keys())[0]
        close_value = data["Time Series (5min)"][first_element_key]["4. close"]
    return close_value


# stock_prices = {}
symbol = "SPY"
data = get_stock_data(symbol)


close_value = get_latest_price(data)


print(f"{symbol}: {close_value}")
