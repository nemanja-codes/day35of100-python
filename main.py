import requests


parameters = {
    "lat": 44.786568,
    "lon": 20.448921,
    "appid": "d8271b0eb2a5d90a84e684d6e7d9d3f3"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
status_code = data["cod"]

print(f"Status code: {status_code}")
print(data)
