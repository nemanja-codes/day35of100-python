import requests
from twilio.rest import Client

account_sid = "AC460ce69a64b5a2ba8a8572e00ab9dc44"
auth_token = "aa0386a11b500c78adc7f4ea06448ecc"


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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+13346895033",
        to="+381640250175"
    )

    print(message.status)
