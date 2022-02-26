import csv
import requests
import wget
import django
django.setup()

from main.models import Help, NeedHelp
from fileinput import filename





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
    
def gpy(address:str):
    




def csv_to_model(filename:str):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for line in reader:
            obj, created = NeedHelp.objects.get_or_create(
                help_type=line[0],
                name=line[1],
                tel=line[2],
                details=line[3],
                # address=line[4]
                )
            obj.save()
            # print(f"tip : {line[0]} | prenume: {line[1]} | nr: {line[2]} | detalii: {line[3]} | raion: {line[4]}")


if __name__ == "__main__":
    # adress_to_points("Moldova, Chisinau")
    # link = "https://docs.google.com/spreadsheets/d/1gnLb9jSxE9XsAKub4UeN0LbdoWYDL4tPLjM1gl-5WYQ/gviz/tq?tqx=out:csv&sheet=Ajutor%20Moldova%20-%20Ucraina%20|%20%D0%94%D0%BE%D0%BF%D0%BE%D0%BC%D0%BE%D0%B3%D0%B0%20%D0%9C%D0%BE%D0%BB%D0%B4%D0%BE%D0%B2%D0%B0%20%E2%80%93%20%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B0"
    # filename = wget.download(link)
    csv_to_model(filename='data.csv')


