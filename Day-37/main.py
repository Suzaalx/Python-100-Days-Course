import requests

username= "boksi00"
token= "8888888888"

pixela_endpoint= "https://pixe.la/v1/users"

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
response=requests.post(url=graph_endpoint,json= graph_config, headers= headers)
print(response.text)