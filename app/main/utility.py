import csv
import requests

def adress_to_points(address:str):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address="
    api = "AIzaSyBFPGuCxwr4X5SsgQo6Zf0CQEjobp0SLbQ"
    address_link = address.split(" ")
    address_link_str = ""
    for item in address_link:
        if address_link[-1] == item:
            address_link_str += item+ f"&key={api}"
        else:
            address_link_str += item + "+"
    print(url + address_link_str)
    response = requests.get(url + address_link_str)
    response_json = response.json()
    # print(response_json['results'][0]['geometry']['location'])
    


    print(address_link_str)


if __name__ == "__main__":
    adress_to_points("Moldova, Chisinau")


