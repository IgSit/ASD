# adjacency matrix implementation


# graf rzadki: V wywołań Dijkstry
from math import inf


def get_min(arr, visited, parent):
    i = -1
    dist = inf
    par = -1
    for q in range(len(arr)):
        if not visited[q]:
            if arr[q] < dist:
                dist = arr[q]
                par = parent[q]
                i = q
    return i, par


def dijkstra(graph, x):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    dist = [inf for _ in range(n)]
    dist[x] = 0
    result = inf

    while True:
        i, par = get_min(dist, visited, parent)
        if i == -1:
            break
        visited[i] = True

        for j in range(n):
            if graph[i][j]:
                alter = dist[i] + graph[i][j]
                if j != par:
                    result = min(result, alter + dist[j])
                if alter < dist[j] and not visited[j] and j != par:
                    dist[j] = alter
                    parent[j] = i

    return result


def rare_shortest_cycle(graph):
    n = len(graph)
    min_cycle = inf
    for i in range(n):
        min_cycle = min(min_cycle, dijkstra(graph, i))
    return min_cycle


def floyd_warshall(graph):  # adjacency matrix implementation
    n = len(graph)
    s_arr = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                s_arr[i][j] = graph[i][j]
                parent[i][j] = i

    cycle = inf
    for t in range(n):
        for u in range(n):
            for v in range(n):
                if not v == parent[u][t] and not parent[u][t] == parent[t][v]:
                    cycle = min(cycle, s_arr[u][t] + s_arr[t][v] + s_arr[u][v])
                    if s_arr[u][t] + s_arr[t][v] < s_arr[u][v]:
                        s_arr[u][v] = s_arr[u][t] + s_arr[t][v]
                        parent[u][v] = parent[t][v]

    return cycle


def dense_shortest_cycle(graph):
    return floyd_warshall(graph)


if __name__ == '__main__':
    test = [[0, 1, 5, 0, 0],
            [1, 0, 0, 5, 0],
            [5, 0, 0, 8, 0],
            [0, 5, 8, 0, 5],
            [0, 0, 0, 5, 0]]
    print(dense_shortest_cycle(test))
