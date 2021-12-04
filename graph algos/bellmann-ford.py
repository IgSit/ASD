from math import inf


def bellman_ford(graph, s, t):
    n = len(graph)
    dist = [inf for _ in range(n)]
    dist[s] = 0
    parent = [-1 for _ in range(n)]

    for i in range(n - 1):
        for v in range(n):
            for u, weight in graph[v]:
                if dist[v] + weight < dist[u]:
                    dist[u] = dist[v] + weight
                    parent[u] = v

    for v in range(n):
        for u, weight in graph[v]:
            if not dist[v] <= dist[u] + weight:
                return "Ujemny cykl"

    return get_path(parent, t)


def get_path(parent, t):
    res = []
    while parent[t] != -1:
        res.append(t)
        t = parent[t]
    res.append(t)
    res.reverse()
    return res


if __name__ == '__main__':
    test = [
        [(1, 3), (5, 7)],
        [(3, 2)],
        [],
        [(2, 5), (4, 3)],
        [(2, 1)],
        [(3, 2), (4, 8)]
    ]
    print(bellman_ford(test, 0, 3))
