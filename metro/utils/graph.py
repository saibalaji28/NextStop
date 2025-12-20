from metro.models import Station, Connection

def build_graph():
    graph = {}

    # Initialize nodes
    for station in Station.objects.all():
        graph[station.name] = {}

    # Add edges
    for conn in Connection.objects.all():
        graph[conn.from_station.name][conn.to_station.name] = conn.distance

    return graph