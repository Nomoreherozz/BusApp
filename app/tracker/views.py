from django.shortcuts import render
from .models import Station, Bus

def index(request):
    context = {"stops": list(Station.objects.values("number", "stop_id", "name", "latitude", "longitude", "distance")),
               "bus": list(Bus.objects.values("route", "number_plate", "latitude", "longitude", "velocity", "timestamp"))}

    return render(request, "index.html", context)
