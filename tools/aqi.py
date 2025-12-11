import requests

def get_aqi(city="Bangalore"):
    try:
        data = requests.get(f"https://api.waqi.info/feed/{city}/?token=demo").json()
        aqi = data["data"]["aqi"]
        return f"AQI: {aqi}"
    except:
        return "AQI data not available"
