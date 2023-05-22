def bfs(graph, start, goal, parent):
    # implementasi algoritma Breadth-First Search
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    visited[start] = True

    while queue:
        node = queue.pop(0)
        for index, val in enumerate(graph[node]):
            if not visited[index] and val > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = node
                if index == goal:
                    return True

    return False

def ford_fulkerson(graph, source, sink):
    # inisialisasi variabel
    parent = [-1] * len(graph)
    max_flow = 0

    # jalankan algoritma Ford-Fulkerson
    while bfs(graph, source, sink, parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow

# contoh penggunaan algoritma Ford-Fulkerson
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
source = 0
sink = 5
max_flow = ford_fulkerson(graph, source, sink)
print("Aliran maksimum adalah: %d" % max_flow)
