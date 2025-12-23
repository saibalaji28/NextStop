from django.shortcuts import render
from .models import Station
from .utils.graph import build_graph
from .utils.dijkstra import dijkstra

def route_view(request):
    stations = Station.objects.all().order_by("name")
    result = None

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        if source == destination:
            result = {
                "error": "Source and destination cannot be same."
            }
        else:
            graph = build_graph()
            route = dijkstra(graph, source, destination)

            if route:
                result = {
                    "source": source,
                    "destination": destination,
                    "path": [s for s, _ in route["path"]],
                    "time": route["time"]
                }
            else:
                result = {
                    "error": "No route found."
                }

    return render(request, "metro/route.html", {
        "stations": stations,
        "result": result
    })

def map_view(request):
    return render(request, "metro/map.html")