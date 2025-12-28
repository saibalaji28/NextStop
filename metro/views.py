from django.shortcuts import render
from .models import Station
from .utils.graph import build_graph
from .utils.dijkstra import dijkstra
from .utils.fare import calculate_fare
from .utils.instructions import build_instructions  # ✅ Phase 7


def route_view(request):
    stations = Station.objects.all().order_by("name")
    result = None

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        # ❌ Edge case: same source & destination
        if source == destination:
            result = {
                "error": "Source and destination cannot be the same."
            }
        else:
            graph = build_graph()
            route = dijkstra(graph, source, destination)

            if route:
                path_with_lines = route["path"]

                # 🔁 Count interchanges
                interchanges = 0
                last_line = None
                for _, line in path_with_lines:
                    if last_line and line != last_line:
                        interchanges += 1
                    last_line = line

                # 🧮 Stations count
                stations_count = len(path_with_lines)

                # 💰 Fare calculation
                fare = calculate_fare(stations_count)

                # 🧭 Phase 7: Build user-friendly instructions
                instructions = build_instructions(path_with_lines)

                # ✅ Final result object
                result = {
                    "source": source,
                    "destination": destination,
                    "path": [s for s, _ in path_with_lines],
                    "time": route["time"],
                    "distance": route["distance"],
                    "stations_count": stations_count,
                    "interchanges": interchanges,
                    "fare": fare,
                    "instructions": instructions,  # ⭐ NEW
                }

            else:
                result = {
                    "error": "No route found between selected stations."
                }

    return render(
        request,
        "metro/route.html",
        {
            "stations": stations,
            "result": result
        }
    )


def map_view(request):

    from django.shortcuts import render

def map_view(request):
    # route path can be passed as query param later
    route_path = request.GET.getlist("route")

    return render(
        request,
        "metro/map.html",
        {
            "route_path": route_path
        }
    )