import heapq

# simple graph (can expand if needed)
city_map = {
    "Delhi": [("Noida", 233), ("Ajmer", 280)],
    "Noida": [("Delhi", 233), ("Ajmer", 240), ("Ujjain", 335)],
    "Ajmer": [("Delhi", 280), ("Noida", 240)],
    "Ujjain": [("Noida", 335)]
}

def shortest_path(graph, start):
    heap = [(0, start)]
    dist = {}
    
    # initialize distances
    for city in graph:
        dist[city] = float('inf')
    dist[start] = 0

    while heap:
        curr_d, curr_city = heapq.heappop(heap)

        for next_city, cost in graph[curr_city]:
            new_d = curr_d + cost

            if new_d < dist[next_city]:
                dist[next_city] = new_d
                heapq.heappush(heap, (new_d, next_city))

    return dist

start = "Delhi"
ans = shortest_path(city_map, start)

print("Shortest distances from", start)
for k in ans:
    print(k, "->", ans[k])
