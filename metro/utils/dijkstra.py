import heapq

INTERCHANGE_PENALTY = 6  # minutes

def dijkstra(graph, start, end):
    # (distance, station, path, last_line, time)
    pq = [(0, start, [], None, 0)]
    visited = {}

    while pq:
        distance, station, path, last_line, time = heapq.heappop(pq)

        if station in visited and visited[station] <= time:
            continue
        visited[station] = time

        path = path + [(station, last_line)]

        if station == end:
            interchanges = sum(
                1 for i in range(1, len(path))
                if path[i][1] != path[i-1][1] and path[i][1] is not None
            )

            return {
                "path": path,
                "distance": distance,
                "time": time,
                "interchanges": interchanges
            }

        for edge in graph.get(station, []):
            extra_time = edge["time"]
            extra_distance = edge["distance"]

            if last_line and last_line != edge["line"]:
                extra_time += INTERCHANGE_PENALTY

            heapq.heappush(
                pq,
                (
                    distance + extra_distance,
                    edge["to"],
                    path,
                    edge["line"],
                    time + extra_time
                )
            )

    return None