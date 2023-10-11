import openrouteservice as ors
#import webbrowser
from dotenv import load_dotenv
from ipyleaflet import Map, FullScreenControl, LayersControl, Marker, GeoJSON, Icon
import json

f = open("stations-VN.json", encoding="utf-8")
content = json.load(f)

d = dict()
color_l = ['green', 'blue', 'black', 'red', 'black', 'purple']
a = 0

for b in content:
    for n in b['bus_routes'].split(','):
        if n.strip() not in d:
            
            d[n.strip()] = list()

        d[n.strip()].append((b["name"], [b["latitude"], b["longitude"]]))

load_dotenv()                               # Locally load all environment variables from .env file

# client = ors.Client(key=os.getenv("OPENROUTESERVICE_API"))
client = ors.Client("5b3ce3597851110001cf624838be29be4d1e45dc80e1d25adc466814")

m = Map(zoom=15, center=[10.9758774, 106.6705121])
m.layout.height = '1080px'
m.layout.width = '1920px'
icon = Icon(icon_url="E:/ProjectBus2023/VguBusPlan2023-main/Icon/bus.png",icon_size=[30,30])

for bus in d:
    path = list()
    for st, coor in d[bus]:
        marker = Marker(location=coor, title=st, draggable=False, name='Marker', icon=icon)
        path.append(coor[::-1])
        m.add_layer(marker)

    route = client.directions(coordinates=path,
                          profile="driving-car",
                          format='geojson')
    

    st_json = GeoJSON(
        name=str(bus),
        data=route,
        style={
            'opacity': 1, 'fillOpacity': 0.1, 'weight': 5, 'color': color_l[a]
        }
    )
    m.add_layer(st_json)

    a += 1

m.add_control(LayersControl())
m.add_control(FullScreenControl())

m.save("route.html")

from Exec import a
a("route.html")


#webbrowser.open("route.html",new=new)

