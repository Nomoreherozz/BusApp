import folium
import json

sample = open("./data/buses.json")
data = json.load(sample)
data[0]["geometry"]["location"]
data[0]["properties"]["number"]

m = folium.Map(location=[10, 106], zoom_start=4)

for record in data:
    location = record["geometry"]["location"][1], record["geometry"]["location"][0]
    folium.Marker(location, popup=record["properties"]["number"]).add_to(m)
    
m.save("map.html")