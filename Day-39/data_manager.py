import requests
sheety_api="https://api.sheety.co/82e8dd17b9fcb26b107ec1682b2a61e5/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data={}
    
    def get_data(self):
        self.data=requests.get(url=sheety_api).json()["prices"]
        return self.data
    
    
    # def update_iata(self):
    #     print(self.data)
    #     for city in self.data:
    #         new_data={
    #         "price": {
    #             "iataCode": city["iataCode"]
    #             }
    #         }
    #         response=requests.put(url=f"{sheety_api}/{city['id']}",json=new_data)
    #         print(response.text)