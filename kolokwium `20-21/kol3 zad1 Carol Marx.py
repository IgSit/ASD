from math import inf
from collections import deque


def floyd_warshall(graph):  # adjacency matrix implementation
    n = len(graph)
    s_arr = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                s_arr[i][j] = graph[i][j]
            if i == j:
                s_arr[i][j] = 0

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if s_arr[u][t] + s_arr[t][v] < s_arr[u][v]:
                    s_arr[u][v] = s_arr[u][t] + s_arr[t][v]

    return s_arr


def keep_distance(graph, x, y, d):
    n = len(graph)
    dist = floyd_warshall(graph)
    new_graph = [[[] for _ in range(n)] for _ in range(n)]

    for a in range(n):
        for b in range(n):
            if dist[a][b] >= d:
                for u in range(n):
                    for w in range(n):
                        if dist[u][w] >= d and not (a == w and b == u):
                            # mamy spełnione to, że po przejściu dystans będzie ok
                            # sprawdzamy teraz, czy istnieją krawędzie
                            # 1) obydwaj przechodzą
                            if graph[a][u] and graph[b][w]:
                                new_graph[a][b].append([u, w])

    # 2) gdy jeden z nich stoi w miejscu
    for a in range(n):
        for b in range(n):
            if dist[a][b] >= d:
                for k in range(n):
                    # 1) a zostaje w miejscu
                    if dist[a][k] >= d and graph[b][k]:
                        new_graph[a][b].append([a, k])
                    # 2) b zostaje w miejcu
                    if dist[b][k] >= d and graph[a][k]:
                        new_graph[a][b].append([k, b])

    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        f, g = queue.popleft()
        for r, t in new_graph[f][g]:
            if not visited[r][t]:
                visited[r][t] = True
                parent[r][t] = (f, g)
                queue.append((r, t))

    return get_path(parent, x, y)


def get_path(parent, x, y):
    res = []
    while parent[y][x] is not None:
        res.append((y, x))
        y, x = parent[y][x]
    res.append((y, x))
    res.reverse()
    return res
