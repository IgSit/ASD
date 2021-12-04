import collections
from math import inf


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


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
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


def max_matching(graph, colours, d):
    n = len(graph)
    new_graph = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    dist = floyd_warshall(graph)
    # indeksy n i n + 1 zarezerwowane dla źródła i ujścia
    for i in range(n):
        for j in range(n):
            new_graph[i][j] = 1 if dist[i][j] >= d else 0

    # indeks n - źródło podłączamy do zielonych
    for i in range(n):
        new_graph[n][i] = 1 if colours[i] == "G" else 0

    # indeks n + 1 dla ujścia
    for i in range(n):
        new_graph[i][n + 1] = 1 if colours[i] == "B" else 0

    return edmonds_karp(new_graph, n, n + 1)
