from django.shortcuts import render
from metro.models import Station
from metro.utils.graph import build_graph
from metro.utils.dijkstra import shortest_path

def route_view(request):
    stations = Station.objects.all().order_by("name")
    result = None

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        graph = build_graph()
        path, distance = shortest_path(graph, source, destination)

        result = {
            "source": source,
            "destination": destination,
            "path": path,
            "distance": distance
        }

    return render(request, "metro/route.html", {
        "stations": stations,
        "result": result
    })