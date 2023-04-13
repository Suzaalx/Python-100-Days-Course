from datetime import datetime
import requests
import os
from dotenv import load_dotenv
load_dotenv("D:/SAT/ss/Documents/docs/EnvironmentVariable/.env")

#nutritionix apis
APP_ID= "5d8d9fe8"
APP_KEY= os.getenv("nutrionix_key")


exercise_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params={
    "query": input("What exercise did you do?: "),
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 180,
    "age": 19
}

headers={
    "x-app-id": APP_ID,
    "x-app-key": f"{APP_KEY}",
}

response= requests.post(url= exercise_endpoint, json= exercise_params,headers= headers).json()
# print(response)


# sheety part
date= datetime.today().strftime("%d/%m/%Y")
time= datetime.now().strftime("%H:%M:%S")
sheety_auth= os.getenv("sheety_auth")
sheety_header={"Authorization": f"{sheety_auth}"}

sheety_endpoint= "https://api.sheety.co/82e8dd17b9fcb26b107ec1682b2a61e5/myWorkouts/workouts"
for n in response["exercises"]:
    sheety_config={
        "workout":{
            "date": date,
            "time": time,
            "exercise": n["name"].title(),
            "duration": n["duration_min"],
            "calories": n["nf_calories"],
        }
    }
    document=requests.post(url=sheety_endpoint,json=sheety_config,headers=sheety_header)
    print(document.status_code)
    print(document.text)

