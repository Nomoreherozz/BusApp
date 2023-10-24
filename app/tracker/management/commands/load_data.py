from django.core.management.base import BaseCommand
from tracker.models import Station
import json
import pandas as pd

class Command(BaseCommand):
    help = 'Load Stations'

    def handle(self, *args, **options) -> str | None:
        data = open("data/68.json", encoding="utf-8")
        stations = json.load(data)
        df = pd.DataFrame(stations, columns=["route", "stop_id", "start_stop", "geometry", "distance(m)"])
        lng = df.geometry.apply(lambda x: x['coordinators'][0][0])
        lat = df.geometry.apply(lambda x: x['coordinators'][0][1])
        for NUMBER, ID, NAME, LAT, LNG, DISTANCE in zip(df.route, df.stop_id ,df.start_stop, lat, lng, df["distance(m)"]):
            station = Station(number=int(NUMBER), stop_id=ID, name=NAME, latitude=LAT, longitude=LNG, distance=DISTANCE)
            station.save()

        print(f"{Station.objects.count()} stations in database")


