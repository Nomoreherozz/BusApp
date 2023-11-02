from django.core.management.base import BaseCommand
from tracker.models import Station, Bus
import json
import pandas as pd


class Command(BaseCommand):
    # help = 'Load Stations'
    #
    # def handle(self, *args, **options):
    #     data = open("data/routes/68.json", encoding="utf-8")
    #     stations = json.load(data)
    #     df = pd.DataFrame(stations, columns=["route", "stop_id", "start_stop", "geometry", "distance(m)"])
    #     lng = df.geometry.apply(lambda x: x['coordinators'][0][0])
    #     lat = df.geometry.apply(lambda x: x['coordinators'][0][1])
    #     for NUMBER, ID, NAME, LAT, LNG, DISTANCE in zip(df.route, df.stop_id ,df.start_stop, lat, lng, df["distance(m)"]):
    #         station = Station(number=int(NUMBER), stop_id=ID, name=NAME, latitude=LAT, longitude=LNG, distance=DISTANCE)
    #         station.save()
    #
    #     print(f"{Station.objects.count()} stations in database")

    help = 'Load Buses'

    def handle(self, *args, **options):
        data = open("data/buses/39x1.json", encoding="utf-8")
        bus = json.load(data)
        df = pd.DataFrame(bus)

        for i in range(len(bus["geometry"]["location"])):
            busa = Bus(
                  route=df["route"][0],
                  number_plate=df["number_plate"][0],
                  latitude=df["geometry"]["location"][i]["coordinators"][0],
                  longitude=df["geometry"]["location"][i]["coordinators"][1],
                  velocity=df["geometry"]["location"][i]["velocity"],
                  timestamp=df["geometry"]["location"][i]["timestamp"],
            )
            busa.save()

