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

# response=requests.post(url=pixela_endpoint,json= user_params)
# print(response.text)

graph_endpoint= f"{pixela_endpoint}/{username}/graphs"
