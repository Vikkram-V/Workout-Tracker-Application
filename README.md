# Workout-Tracker-Application

## 📌 Project Overview  
Workout Tracker is a Python-based fitness logging tool that automates workout tracking using **Natural Language Processing (NLP)**. It leverages **Nutritionix API** to extract workout details from user input, stores the data in **Google Sheets** via **Sheety API**, and enables **REST API operations** (GET, POST, UPDATE, DELETE) for seamless tracking.  

## 🚀 Features  
✅ Uses **NLP** to extract workout details from user input  
✅ Automatically logs **date, time, activity, duration, and calories burned**  
✅ Stores workout data in **Google Sheets** using Sheety API  
✅ Enables **CRUD operations** (Create, Read, Update, Delete) on workout logs  
✅ Simple and efficient **fitness tracking**  

## 🛠 Tech Stack  
- **Programming Language:** Python  
- **APIs Used:**  
  - **Nutritionix API** – Extracts workout details using NLP  
  - **Sheety API** – Stores workout logs in Google Sheets  
- **Libraries:** requests, json, datetime, dotenv  

## 📌 Installation & Setup  

### 1️⃣ Clone the repository  

    git clone https://github.com/Vikkram-V/workout-tracker.git  
    cd workout-tracker  

### 2️⃣ Set up API keys  
Create a **.env** file and add your API keys:  

# Nutritionix API credentials
NUTRITIONIX_API_ENDPOINT = nutritionix_api_endpoint
NUTRITIONIX_APP_ID = your_nutritionix_app_id
NUTRITIONIX_API_KEY = your_nutritionix_api_key

# Sheety API credentials
SHEETY_API_ENDPOINT = your_google_sheet_endpoint
SHEETY_USERNAME = your_sheety_username
SHEETY_PASSWORD = your_sheety_password 

### 3️⃣ Run the script  

    python main.py    

## 📌 Example Input & Output

### User Input:  
*"I ran for 5 km and swam for 30 minutes"*  

### Stored in Google Sheet: 
| Date       | Time   | Activity | Duration  | Calories Burned |  
|------------|--------|----------|-----------|-----------------|  
| 2025-02-01 | 07:30  |    Run   |   30min   |     350 kcal    |  
| 2025-02-01 | 07:30  |   Swim   |   30min   |     350 kcal    |  

## 📌 Future Enhancements  
🔹 **Add mobile app integration** for easy input  
🔹 **Visual analytics dashboard** for progress tracking  
🔹 **Voice command support** for hands-free workout logging 
