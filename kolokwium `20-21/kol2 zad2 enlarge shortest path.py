from collections import deque


def BFS(graph, s, t):
    n = len(graph)
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    visited = [False for _ in range(n)]
    visited[s] = True
    parent = [-1 for _ in range(n)]
    queue = deque()
    queue.append(s)

    while queue and not visited[t]:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                queue.append(v)

    while queue:
        u = queue.popleft()
        if dist[u] >= dist[t]:
            break
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                dist[v] = dist[u] + 1
                queue.append(v)

    return dist, parent


def get_path(parent, t):
    res = []
    while parent[t] != -1:
        res.append(t)
        t = parent[t]
    res.append(t)
    res.reverse()
    return res


def enlarge(graph, s, t):
    s_dist, s_par = BFS(graph, s, t)
    if s_dist[t] == -1:
        return None
    t_dist, _ = BFS(graph, t, s)

    n = len(graph)
    length = s_dist[t]
    points = [0 for _ in range(length + 1)]
    for v in range(n):
        if s_dist[v] + t_dist[v] == length:
            points[s_dist[v]] += 1

    for k in range(length):
        if points[k] == points[k + 1] == 1:
            path = get_path(s_par, t)
            return path[k], path[k + 1]
    return None
