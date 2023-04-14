import requests
tequila_api_endpoint = "https://api.tequilia.kiwi.com"

tequila_api = "hm-jQEXKstNZq4lp2QBihBYjXyLdXjRZ"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def get_code(self,city):
        
        endpoint=f"{tequila_api_endpoint}/locations/query"
        header={ "apikey": tequila_api}
        query= {"term":city,"location_types":"city"}
        response=requests.get(url=endpoint,headers=header,params=query)
        print(response.json())
        