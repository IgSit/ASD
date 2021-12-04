from collections import deque
from math import inf


def bfs(graph, start):  # neighbourhood lists implementation
    n = len(graph)
    visited = [False for _ in range(n)]
    dist = [inf for _ in range(n)]
    queue = deque()

    visited[start] = True
    dist[start] = 0
    queue.append(start)

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            d_rel = dist[u] + 1
            if not visited[v] and d_rel < dist[v]:
                dist[v] = d_rel
                visited[v] = True
                queue.append(v)

    return dist


def best_root(graph):
    n = len(graph)
    rand_dist = bfs(graph, 0)
    s = -1
    d = -1
    for i in range(n):
        if rand_dist[i] > d:
            d = rand_dist[i]
            s = i

    # s to jedna końcówka średnicy drzewa

    s_dist = bfs(graph, s)
    t = -1
    d = -1
    for j in range(n):
        if s_dist[j] > d:
            d = s_dist[j]
            t = j

    # t to drugi koniec średnicy

    # najlepszy root jest w połowie średnicy

    t_dist = bfs(graph, t)
    if d % 2 == 0:
        for k in range(n):
            if s_dist[k] == t_dist[k] == d // 2:
                return k
    else:
        for k in range(n):
            if s_dist[k] == d // 2 and t_dist[k] == d // 2 + 1:
                return k
