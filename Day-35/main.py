
import requests
api_key= "117680be52d9c08fdc8b07df7d09df0c"
endpoint="https://api.openweathermap.org/data/2.5/forecast?"


parameters={
    "lat" : 28.26689,
    "lon" : 83.96851,
    "appid": api_key
}

weather=requests.get(endpoint,params=parameters).json()
rain=[]
for n in range(5):
    print(n)
    num=weather['list'][n]['weather'][0]['id']
    if num<700:
        rain.append(n)
print(rain)
for i in rain:    
    print(f"It will rain on {i+1} day")
    
