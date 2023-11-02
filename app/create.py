import json
import random

out_file = open("data/buses/68x3.json", "w")
dt = open("data/buses/68.json", "r")

data = json.load(dt)
start_hour = 16
start_minute = 22
start_sec = 7
interval = 5
i = 0
location = []

bus = {"route": 68,
       "number_plate": "8866",
       "geometry": {
              "type": "Point",
              "location": location,
              },
       }

while i <= 69:
    if start_sec > 60:
        start_sec -= 60
        start_minute += 1
        if start_minute == 60:
            start_minute = 0
            start_hour += 1

    obj = {
        "coordinators": [data[str(i)]["lat"], data[str(i)]["lng"]],
        "timestamp": str(start_hour).zfill(2) + ":" + str(start_minute).zfill(2) + ":" + str(start_sec).zfill(2),
        "velocity": round(random.uniform(0.0, 50.0), 2)
    }
    location.append(obj)
    start_sec += interval

    i += 3

json.dump(bus, out_file, indent=4)
out_file.close()