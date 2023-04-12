import requests
from datetime import datetime
username= "boksi00"
token= "8888888888"
graph_id= "graph1"
pixela_endpoint= "https://pixe.la/v1/users"
today= datetime(year=2023,month=4,day=11)
date= today.strftime("%Y%m%d")
print(today)


user_params={
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    
}


graph_endpoint= f"{pixela_endpoint}/{username}/graphs"

graph_config={
    "id": "graph1",
    "name": "running",
    "unit": "kilogram",
    "type": "float",
    "color": "ajisai"
}

headers={
    "X-USER-TOKEN": token
}
# response=requests.post(url=graph_endpoint,json= graph_config, headers= headers)
# print(response.text)

pixel_endpoint=f'{pixela_endpoint}/{username}/graphs/{graph_id}'


pixel_config={
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.5",
    
}



# response= requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
# print(response.text)


update_endpoint= f'{pixel_endpoint}/{date}'
update_config={
    "quantity": "89"
}
response= requests.delete(url=update_endpoint,json=update_config,headers=headers)
print(response.text)