import os
import openrouteservice as ors
from folium import Popup
import pandas as pd

from dotenv                                 import load_dotenv
from .buses_info                            import *

load_dotenv()                               # Locally load all environment variables from .env file

client = ors.Client(key=os.getenv("OPENROUTESERVICE_API"))


def getRoute(number):
    buses = AllBusesInfo()
    path = list()

    for _, lat, lon in buses[number]:
        path.append([lon, lat])

    route = client.directions(coordinates=path, profile="driving-car", format='geojson')

    return route


def addMarkers(Map, number):
    buses = AllBusesInfo()
    points = list()
    names = list()

    for name, lat, lon in buses[number]:
        points.append([lat, lon])
        names.append(name)
    
    for i in range(len(points)):
        html = "<b>" + names[i] + "</b>" + ": " + "<br>"
        popup_html = Popup(html, min_width=100, max_width=200)
        Map.add_marker(location=points[i], popup=popup_html)

# def check(number):
#     buses = AllBusesInfo()

#     df = pd.DataFrame(buses[number], columns=["Trạm", "KĐ", "VĐ"])
#     return df
