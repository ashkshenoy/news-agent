import requests

def get_crypto():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=inr"
    data = requests.get(url).json()
    btc = data["bitcoin"]["inr"]
    eth = data["ethereum"]["inr"]
    return f"BTC: ₹{btc:,} | ETH: ₹{eth:,}"
