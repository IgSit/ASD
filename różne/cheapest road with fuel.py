# adjacency matrix implementation
from math import inf


def get_min(visited, cost, d=100):  # O(d*V)
    n = len(visited)
    res = None
    c = inf
    for j in range(d + 1):
        for i in range(n):
            if not visited[i][j] and cost[i][j] < c:
                c = cost[i][j]
                res = (i, j)
    return res


def cheapest_road(graph, prices, s, t, d=100):
    n = len(graph)

    # każdy wierzchołek rozmnażamy na d wierzchołków: [v][f] oznacza, że wjezdzamy do v, mając f paliwa

    visited = [[False for _ in range(d + 1)] for _ in range(n)]
    cost = [[inf for _ in range(d + 1)] for _ in range(n)]
    parent = [[[-1, -1] for _ in range(d + 1)] for _ in range(n)]

    cost[s][0] = 0

    while True:  # O(d*V)
        minimum = get_min(visited, cost, d)  # O(d*V)
        if minimum is None:
            break
        u, fuel = minimum
        visited[u][fuel] = True

        for f in range(fuel + 1, d + 1):  # chcę dotankować w mieście u - O(d)
            rel_c = cost[u][fuel] + (f - fuel) * prices[u]
            if rel_c < cost[u][f]:
                cost[u][f] = rel_c
                parent[u][f] = [u, fuel]

        for v in range(n):  # jadę z u do innych wierzchołków - o(V)
            if graph[u][v] and fuel >= graph[u][v]:  # jest krawędź i nie zabraknie mi paliwa podczas przejazdu
                if not visited[v][fuel - graph[u][v]] and cost[u][fuel] < cost[v][fuel - graph[u][v]]:
                    cost[v][fuel - graph[u][v]] = cost[u][fuel]
                    parent[v][fuel - graph[u][v]] = [u, fuel]

    res = inf
    i = -1
    for q in range(d + 1):
        if cost[t][q] < res:
            res = cost[t][q]
            i = q
    return get_path(parent, t, i), res


def get_path(parent, t, f):
    res = []
    while parent[t][f] != [-1, -1]:
        res.append((t, f))
        t, f = parent[t][f]
    res.append((t, f))
    res.reverse()
    return res


if __name__ == '__main__':
    test = [[0, 90, 0, 200, 0, 0, 80],
            [90, 0, 110, 0, 0, 90, 0],
            [0, 110, 0, 70, 0, 0, 0],
            [200, 0, 0, 70, 110, 40, 0],
            [0, 0, 0, 110, 0, 50, 90],
            [0, 90, 0, 40, 50, 0, 50],
            [80, 0, 0, 0, 90, 50, 0]]
    p = [4, 5, 6, 8, 3, 5, 4]
    print(cheapest_road(test, p, 0, 3))
