from math import sqrt, inf, ceil


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return None
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def dist(a, b, x, y):
    return ceil(sqrt((x - a) ** 2 + (y - b) ** 2))


def mod_kruskal(matrix, graph, n):  # graf jako lista krawędzi już przygotowana
    nodes = [Node(i) for i in range(n)]
    graph.sort()  # O(V^2logV)
    res = []
    for d, i, j in graph:  # O(V^2logV)
        if find(nodes[i]) != find(nodes[j]):
            res.append([i, j])
            union(nodes[i], nodes[j])

    max_d = -inf
    min_d = inf
    for u, v in res:  # O(V)
        max_d = max(max_d, matrix[u][v])
        min_d = min(min_d, matrix[u][v])

    return max_d - min_d


def highways(cities):  # O(V^4logV)
    n = len(cities)
    edges = []
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):  # O(V^2)
        for j in range(n):
            if i == j:
                continue
            a, b = cities[i]
            x, y = cities[j]
            length = dist(a, b, x, y)
            edges.append([length, i, j])
            matrix[i][j] = length

    span = inf
    for edge, u, v in edges:
        relax_graph = [[abs(e - edge), s, t] for e, s, t in edges]  # O(V^2)
        curr_span = mod_kruskal(matrix, relax_graph, n)  # O(V^2logV)
        span = min(span, curr_span)

    return span
