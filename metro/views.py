from django.shortcuts import render
from metro.models import Station

def route_view(request):
    stations = Station.objects.all().order_by("name")
    return render(request, "metro/route.html", {
        "stations": stations
    })

def map_view(request):
    return render(request, "metro/map.html")