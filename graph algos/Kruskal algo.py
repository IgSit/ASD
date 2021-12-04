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


def Kruskal(graph):  # neighbourhood lists implementation
    n = len(graph)
    points = [Node(i) for i in range(n)]
    edges = []
    for i in range(n):
        for j, weight in graph[i]:
            edges.append([weight, i, j])

    edges.sort()
    res = []
    for _, i, j in edges:
        if find(points[i]) != find(points[j]):
            res.append([i, j])
            union(points[i], points[j])

    return res


if __name__ == '__main__':
    test = [[(1, 3), (4, 7)],
            [(0, 3), (2, 1), (3, 7)],
            [(1, 2), (3, 8)],
            [(1, 7), (2, 8), (4, 12), (5, 2)],
            [(0, 7), (3, 12), (5, 4)],
            [(3, 2), (4, 4), (6, 6), (7, 10)],
            [(5, 6), (7, 5)],
            [(5, 10), (6, 5)]]
    print(Kruskal(test))
