from django.shortcuts import render
from metro.models import Station

def route_view(request):
    stations = Station.objects.all().order_by("name")
    result = None

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        result = {
            "source": source,
            "destination": destination
        }

    return render(request, "metro/route.html", {
        "stations": stations,
        "result": result
    })


def map_view(request):
    return render(request, "metro/map.html")