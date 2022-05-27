from datetime import datetime
import os

import requests

GENDER = "Male"
WEIGHT_KG = "70"
HEIGHT_CM = "170"
AGE = "20"

APP_ID = os.environ.get("WT_APP_ID")
API_KEY = os.environ.get("WT_API_KEY")

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}
response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=parameters)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
# google sheet NO AUTH
response = requests.post(url=SHEET_ENDPOINT, json=sheet_input)
