import json
import openrouteservice as ors

client = ors.Client(key='5b3ce3597851110001cf624838be29be4d1e45dc80e1d25adc466814')

buses_file = open("./stations-VN.json", encoding="utf-8")
outp = open("./51.json", "a", encoding="utf-8")
data = json.load(buses_file)


for i in range(len(data)):
    if data[i]["bus_routes"] == "51":

        matrix = client.distance_matrix(
                                        locations=[[data[i]["longitude"], data[i]["latitude"]], [data[i+1]["longitude"], data[i+1]["latitude"]]],
                                        profile='driving-car',
                                        metrics=['distance', 'duration'],
                                        validate=False,
                                        )
        bus = {
            "route"         : data[i]["bus_routes"],
            "stop_id"       : i+1,
            "start_stop"    : str(data[i]['name']),
            "end_stop"      : data[i+1]['name'],
            "start_stop_id" : "39" + str(i+1).zfill(2),
            "end_stop_id"   : "39" + str(i+2).zfill(2),
            "segment_id"    : "39" + str(i+1).zfill(2) + "-" + "39" + str(i+2).zfill(2),
            "geometry"      : {
                "type"          : "LINESTRING",
                "coordinators"  : [[data[i]["longitude"], data[i]["latitude"]], [data[i+1]["longitude"], data[i+1]["latitude"]]]
            },
            "distance(m)"      : matrix["distances"][0][1]
        }
        outp.write(str(bus))
        outp.write(",\n")

