import os

import requests
from twilio.rest import Client

api_key = ""
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

api_parameters = {
    "lat": 45.421532,
    "lon": -75.697189,
    "appid": api_key,
    "exclude": "daily,minutely,current"

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=api_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    day_temperature = hour_data["temp"]
    condition_id = hour_data["weather"][0]["id"]
    if int(condition_id) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")
    print(day_temperature)
    message = client.messages.create(
        body='It will Rain/Snow!, Good luck! Developed By: Fady Shenouda 🌧',
        from_='+14143102193',
        to='+16139813184'
    )

print(condition_id)
