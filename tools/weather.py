import requests

def get_weather(city="Bangalore"):
    url = f"https://wttr.in/{city}?format=%C+%t"
    res = requests.get(url).text.strip()
    return res
