def dfs(graph, start):

    visited = [False] * len(graph)

    def rec(u):
        nonlocal visited

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                rec(v)

    rec(start)
