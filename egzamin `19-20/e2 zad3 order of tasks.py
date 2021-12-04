def dfs_sort(graph):

    n = len(graph)
    visited = [False for _ in range(n)]
    top_sort = [-1 for _ in range(n)]
    i = n - 1

    def rec(u):
        nonlocal visited, top_sort, i

        visited[u] = True
        for v in range(n):
            if not visited[v] and graph[u][v]:
                rec(v)
        top_sort[i] = u
        i -= 1

    for q in range(n):
        if not visited[q]:
            rec(q)
    return top_sort


def tasks(matrix):
    n = len(matrix)
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for w in range(n):
        for k in range(n):
            if matrix[w][k] == 1:
                graph[w][k] = 1
            if matrix[w][k] == 2:
                graph[k][w] = 1

    return dfs_sort(graph)
