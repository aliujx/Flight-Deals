from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
#print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()







##This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#import requests
#from pprint import pprint
#from flight_search import FlightSearch
#
#flight_search = FlightSearch()
#
#sheety_api = "https://api.sheety.co/f34af4f8a2689c02a3b0a6c031898be8/myFlightDeals/prices"
#
#bearer_headers = {
#    "Authorization": "aegv234jvefnlsfg.slrgmbaqwhqveqwcrh3gr"
#}
#
#responce = requests.get(url=sheety_api, headers=bearer_headers).json()
##pprint(responce)
#sheet_data = responce["prices"]
#pprint(sheet_data)
#for data in sheet_data:
#    if not data["iataCode"] in data:
#        data["iataCode"] = "TESTING"
#        put_data = requests.put(url="https://api.sheety.co/f34af4f8a2689c02a3b0a6c031898be8/myFlightDeals/prices/TESTING")
#pprint(sheet_data)
#print(put_data)