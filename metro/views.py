from django.shortcuts import render
from .models import Station
from .utils.graph import build_graph
from .utils.dijkstra import dijkstra
from .utils.fare import calculate_fare   # ✅ NEW IMPORT


def route_view(request):
    stations = Station.objects.all().order_by("name")
    result = None

    if request.method == "POST":
        source = request.POST.get("source")
        destination = request.POST.get("destination")

        # ❌ Same source & destination
        if source == destination:
            result = {
                "error": "Source and destination cannot be the same."
            }

        else:
            graph = build_graph()
            route = dijkstra(graph, source, destination)

            if route:
                path_with_lines = route["path"]

                # 🔁 STEP 4: Count interchanges
                interchanges = 0
                last_line = None

                for _, line in path_with_lines:
                    if last_line and line != last_line:
                        interchanges += 1
                    last_line = line

                # 🧮 Stations count
                stations_count = len(path_with_lines)

                # 💰 STEP 5: Fare calculation
                fare = calculate_fare(stations_count)

                # ✅ Final result dictionary
                result = {
                    "source": source,
                    "destination": destination,
                    "path": [s for s, _ in path_with_lines],
                    "time": route["time"],
                    "interchanges": interchanges,
                    "stations_count": stations_count,
                    "fare": fare,
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