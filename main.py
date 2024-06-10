import requests


parameters = {
    "lat": 51.318729,
    "lon": 9.494630,
    "appid": "d8271b0eb2a5d90a84e684d6e7d9d3f3",
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
status_code = weather_data["cod"]
weather_next_12_hours = weather_data["list"]

will_rain = False
for weather in weather_next_12_hours:
    if weather["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.")

print(f"Status code: {status_code}")
print(weather_data)
