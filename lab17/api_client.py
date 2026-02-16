# Lab 17 - Example 1
# Consuming a Public API with Python (CoinGecko)

import requests

api_url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,
    "page": 1,
    "sparkline": "false"
}

try:
    response = requests.get(api_url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    print("Top 5 coins by market cap:")
    for coin in data:
        print(f"{coin['name']}: ${coin['current_price']}")
except requests.RequestException as e:
    print("Failed to retrieve data:", e)
