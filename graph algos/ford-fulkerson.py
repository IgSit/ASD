from copy import deepcopy
from collections import deque
from math import inf


def BFS(graph, s, t):
    n = len(graph)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    queue = deque()

    visited[s] = True
    queue.append([inf, s])
    while queue:
        cap, v = queue.popleft()
        if v == t:
            path = get_path(parent, t)
            return True, cap, path
        for u in range(n):
            if graph[v][u] != 0 and not visited[u]:
                visited[u] = True
                parent[u] = v
                queue.append([min(cap, graph[v][u]), u])

    return False, 0, []


def get_path(parent, t):
    res = []
    while parent[t] != -1:
        res.append(t)
        t = parent[t]
    res.append(t)
    res.reverse()
    return res


def max_flow(graph, s, t):  # matrix representation
    network = deepcopy(graph)
    flow = 0
    while True:
        is_path, cap, path = BFS(network, s, t)
        if not is_path:
            return flow
        n = len(path)
        flow += cap
        for i in range(0, n - 1):
            v, u = path[i], path[i + 1]
            network[v][u] -= cap
            network[u][v] += cap


if __name__ == '__main__':
    test = [[0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]]
    print(max_flow(test, 0, 5))
