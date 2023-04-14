#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager

from pprint import pprint
data_manager=DataManager()
sheetdata=data_manager.get_data()

print(sheetdata)
# print(sheetdata.data)
if sheetdata[0]["iataCode"]=="":
    from flight_search import FlightSearch
    flight_search=FlightSearch()
    for row in sheetdata:
        # print(sheetdata[i]["iataCode"])
        kk=flight_search.get_code(row["city"])
        print(sheetdata)
        print(kk)
    
    data_manager.get_data=sheetdata
    # data_manager.update_iata()