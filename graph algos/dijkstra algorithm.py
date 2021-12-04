# zrobiony bez kolejki priorytetowej O(V^2)

from math import inf


def get_min(arr, visited):
    i = -1
    dist = inf
    for q in range(len(arr)):
        if not visited[q]:
            if arr[q] < dist:
                dist = arr[q]
                i = q
    return i


def dijkstra(graph, x, y):  # find shortest path from x to y - adjacency matrix implementation
    n = len(graph)
    visited = [False for _ in range(n)]
    dist = [inf for _ in range(n)]
    dist[x] = 0

    while True:
        i = get_min(dist, visited)
        if i == -1:
            break
        visited[i] = True

        for j in range(n):
            if graph[i][j]:
                alter = dist[i] + graph[i][j]
                if not visited[j] and alter < dist[j]:
                    dist[j] = alter

    return dist[y]
