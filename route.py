import folium
import os
import openrouteservice as ors
from dotenv import load_dotenv

load_dotenv()                               # Locally load all environment variables from .env file

client = ors.Client(key=os.getenv("OPENROUTESERVICE_API"))

# start_point = [106.7716404, 10.8496468]
# dest_point =  [106.7690031, 10.8498116]

start_point = [106.70121875657996, 10.786930772105503]
dest_point =  [106.69645515366152, 10.778204140755804]


# Get route 
route = client.directions(coordinates=[start_point, dest_point],
                         profile="driving-car",
                         format='geojson')

# Create map
map = folium.Map(location=[10.79, 106.675], zoom_start=5)

# Add GeoJson to map
folium.GeoJson(route, name="Route").add_to(map)

# Add a layer control
folium.LayerControl().add_to(map)

map.save("route.html")

