from django.shortcuts import render
from .models import Station
from .utils.graph import build_graph
from .utils.dijkstra import dijkstra
from .utils.fare import calculate_fare
from .utils.instructions import build_instructions


def route_view(request):
    stations = Station.objects.all().order_by("name")
    result = None

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        # ❌ Same station edge case
        if source == destination:
            result = {
                "error": "Source and destination cannot be the same."
            }
        else:
            graph = build_graph()
            route = dijkstra(graph, source, destination)

            if route:
                path_with_lines = route["path"]

                # 🔁 Interchanges + stations
                interchanges = 0
                interchange_stations = []
                last_line = None

                for station, line in path_with_lines:
                    if last_line and line != last_line:
                        interchanges += 1
                        interchange_stations.append(station)
                    last_line = line

                stations_count = len(path_with_lines)
                fare = calculate_fare(stations_count)
                instructions = build_instructions(path_with_lines)

                result = {
                    "source": source,
                    "destination": destination,
                    "path": [s for s, _ in path_with_lines],
                    "path_with_lines": path_with_lines,  # ⭐ IMPORTANT
                    "time": route["time"],
                    "distance": route["distance"],
                    "stations_count": stations_count,
                    "interchanges": interchanges,
                    "interchange_stations": interchange_stations,  # ⭐ NEW
                    "fare": fare,
                    "instructions": instructions,
                }
            else:
                result = {
                    "error": "No route found between selected stations."
                }

    return render(request, "metro/route.html", {
        "stations": stations,
        "result": result
    })


def map_view(request):
    """
    Phase 8 Stage 3:
    Receives route data and highlights it on map
    """
    route_path = request.GET.getlist("path")
    interchange_stations = request.GET.getlist("interchanges")

    return render(request, "metro/map.html", {
        "route_path": route_path,
        "interchange_stations": interchange_stations
    })