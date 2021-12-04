from collections import deque
from math import inf


def find_bridges(graph):
    n = len(graph)
    cnt = 0
    parent = [-1 for _ in range(n)]
    time = [inf for _ in range(n)]
    low = [inf for _ in range(n)]
    visited = [False for _ in range(n)]
    bridges = []

    def dfs(u):
        nonlocal cnt, parent, time, low, visited, bridges
        visited[u] = True
        time[u] = cnt
        low[u] = cnt
        cnt += 1
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)

                low[u] = min(low[u], low[v])
                if low[v] > time[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], time[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return bridges


def count_dfs(graph, u, visited, trolls):
    count = 0

    def dfs_visit(x):
        nonlocal count
        visited[x] = True
        count += trolls[x]
        for y in graph[x]:
            if not visited[y]:
                dfs_visit(y)

    dfs_visit(u)
    return count, visited


def destroy_bridge(graph, trolls, s):
    n = len(graph)
    bridges = find_bridges(graph)
    bridge_points = [-1 for _ in range(n)]
    for x, y in bridges:
        bridge_points[x] = y
        bridge_points[y] = x
    visited = [False for _ in range(n)]
    queue = deque()
    queue.append(s)
    max_troll = 0
    best = None

    while queue:
        u = queue.popleft()
        visited[u] = True
        for v in graph[u]:
            if bridge_points[u] == v:  # bridge
                curr_troll, visited = count_dfs(graph, v, visited, trolls)
                if curr_troll > max_troll:
                    max_troll = curr_troll
                    best = (u, v)
            elif not visited[v]:
                queue.append(v)

    return max_troll, best


if __name__ == '__main__':
    test = [[0, 3],
            [0, 3, 2, 4],
            [1, 3, 7],
            [0, 1, 2, 10],
            [1, 5, 6, 7],
            [4, 6],
            [5, 4],
            [2, 8, 9, 4, 10],
            [7, 9],
            [7, 8],
            [3, 12, 11, 13, 7],
            [10, 12, 14],
            [10, 11, 13],
            [12, 10],
            [11]]
    troll = [0, 0, 3, 1, 11, 8, 6, 9, 3, 11, 12, 7, 4, 5, 8]
    print(destroy_bridge(test, troll, 0))
