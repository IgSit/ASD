from queue import PriorityQueue
from math import inf


def dijkstra(graph, x, y):  # find shortest path from x to y - neighbourhood list implementation
    n = len(graph)
    visited = [False for _ in range(n)]
    dist = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    queue = PriorityQueue()
    dist[x] = 1
    for i in range(n):
        queue.put([dist[i], i])

    while not queue.empty():
        _, v = queue.get()
        if visited[v]:
            continue
        visited[v] = True

        for vertex, distance in graph[v]:
            alter = dist[v] * distance
            if alter < dist[vertex] and not visited[vertex]:
                dist[vertex] = alter
                parent[vertex] = v
                queue.put([dist[vertex], vertex])

    return get_path(parent, y)


def get_path(parent, y):
    res = []
    while parent[y] != -1:
        res.append(y)
        y = parent[y]
    res.append(y)
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
    print(dijkstra(test, 0, 2))
