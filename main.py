import requests
import datetime
import os


current_datetime= datetime.datetime.now().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%X")

APP_ID=os.environ.get('APP_ID', "yourIDFromAppNutritionix")
API_KEY=os.environ.get('API_KEY', "yourAPIKeyFromNutritionix")
URL= os.environ.get('URL_NUTRI', "yourURLFromNutritionix")

API_SHEETY = os.environ['API_SHEETY']
BEARER_TOKEN_SHEETY = os.environ['BEARER_TOKEN']

header = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}
user_text = input("What exercises you did ?")

info= {
    'query': user_text,
    'gender': 'female',
    'weight_kg': 43,
    'height_cm':164,
    'age': 15

}


response = requests.post(url=URL, json=info, headers=header)
exc_info = response.json()['exercises']



for i in exc_info:
    sheet={
        "workout": {
            "date":current_datetime,
            "time":current_time,
            "activity":i["name"],
            "duration":i["duration_min"],
            "calories":i["nf_calories"]
        }
    }

    header_sheety = {
        "Authorization": BEARER_TOKEN_SHEETY
    }
    response_sheet = requests.post(url=API_SHEETY,json=sheet,headers=header_sheety)









