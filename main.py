import requests
import datetime
import os
from requests.auth import HTTPBasicAuth

# User input for personal details
GENDER = input("Enter your gender: ")
WEIGHT_KG = input("Enter your weight in kg: ")
HEIGHT_CM = input("Enter your height in cm: ")
AGE = int(input("Enter your age: "))

# API endpoints and credentials from environment variables
NUTRITIONIX_API_ENDPOINT = os.environ.get("NUTRITIONIX_API_ENDPOINT")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")

SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

# Headers for Nutritionix API authentication
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}

# User input for workout activities
user_input = input("Enter your activities: ")

# API request parameters for NLP processing
exercise_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Sending request to Nutritionix API to analyze workout input
response = requests.post(url=NUTRITIONIX_API_ENDPOINT, headers=headers, json=exercise_params)
exercise_data = response.json()

# Get current date and time
current_date = datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# Loop through each exercise and send data to Google Sheets via Sheety API
for exercise in exercise_data["exercises"]:
    workout_entry = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),  # Capitalize first letter
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sending POST request to Sheety API for logging workout data
    auth = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)
    response = requests.post(url=SHEETY_API_ENDPOINT, json=workout_entry, auth=auth)
    
    # Print API response
    print(response.text)
