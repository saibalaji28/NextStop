from collections import defaultdict
from metro.models import Connection

def build_graph():
    graph = defaultdict(list)

    connections = Connection.objects.select_related(
        "from_station", "to_station", "line"
    )

    for conn in connections:
        graph[conn.from_station.name].append({
            "to": conn.to_station.name,
            "distance": conn.distance,
            "time": conn.travel_time,
            "line": conn.line.name
        })

        graph[conn.to_station.name].append({
            "to": conn.from_station.name,
            "distance": conn.distance,
            "time": conn.travel_time,
            "line": conn.line.name
        })

    return graph