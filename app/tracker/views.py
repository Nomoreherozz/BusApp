from django.shortcuts import render
from .models import Station

def index(request):
    context = {"stops": list(Station.objects.values("number", "stop_id", "name", "latitude", "longitude", "distance")),}
    return render(request, "index.html", context)
