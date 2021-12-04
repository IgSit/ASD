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


if __name__ == '__main__':
    test = [[1, 8],
            [0, 2],
            [1, 3],
            [1, 2, 4],
            [3, 5],
            [4, 6],
            [4, 5],
            [9, 8],
            [0, 7, 9],
            [7, 8]]
    print(find_bridges(test))
