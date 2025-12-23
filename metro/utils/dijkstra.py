import heapq

def dijkstra(graph, start, end):
    pq = [(0, start, [], None, 0)]  
    visited = set()

    while pq:
        distance, station, path, last_line, time = heapq.heappop(pq)

        if station in visited:
            continue

        visited.add(station)
        path = path + [(station, last_line)]

        if station == end:
            return {
                "path": path,
                "distance": distance,
                "time": time
            }

        for edge in graph.get(station, []):
            if edge["to"] not in visited:
                extra_time = edge["time"]
                extra_distance = edge["distance"]

                # interchange penalty
                if last_line and last_line != edge["line"]:
                    extra_time += 5  # interchange penalty

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