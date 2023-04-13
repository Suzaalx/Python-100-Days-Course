
import requests
APP_ID= "5d8d9fe8"

APP_KEY= "c289ca348b0d2a2aa4238794f834394f"


exercise_endpoint= "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params={
    "query": input("What exercise did you do?: ")
}

headers={
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response= requests.post(url= exercise_endpoint, json= exercise_params,headers= headers)
print(response.json())
