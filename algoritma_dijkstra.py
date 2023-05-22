import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# contoh penggunaan algoritma Dijkstra
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 1, 'E': 6},
    'C': {'B': 1, 'D': 4},
    'D': {'E': 1},
    'E': {}
}
start_node = 'A'
distances = dijkstra(graph, start_node)

print("Jarak terpendek dari node {} ke setiap node lainnya:".format(start_node))
for node, distance in distances.items():
    print("Node {}: {}".format(node, distance))
