import json

f = open("./data/stations-EN.json", encoding="utf-8")
data = json.load(f)

buses = dict()

def AllBusesInfo() -> dict():
    buses.clear()
    for bus in data:
        for number in bus['bus_routes'].split(','):
            if number.strip() not in buses:
                
                buses[number.strip()] = list()

            buses[number.strip()].append((bus["name"], bus["latitude"], bus["longitude"]))
    
    return buses
