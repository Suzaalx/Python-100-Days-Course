import requests

reps=requests.get(url="http://api.open-notify.org/iss-now.json")
print(reps.status_code)

data=reps.json()['iss_position']['latitude']
print(data)