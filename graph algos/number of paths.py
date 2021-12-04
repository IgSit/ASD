# f(u) - liczba ścieżek idących z u do źródła - żeby zrobić to poprawnie,
# trzeba najpierw sprawdzić wszystkie wierzchołki, na które można przejść z u


def dfs_sort(graph):  # sortowanie topologiczne

    n = len(graph)
    visited = [False for _ in range(n)]
    top_sort = [-1 for _ in range(n)]
    i = n - 1

    def rec(u):
        nonlocal visited, top_sort, i

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                rec(v)
        top_sort[i] = u
        i -= 1

    for q in range(n):
        if not visited[q]:
            rec(q)
    return top_sort


def number_of_paths(graph, a, b):
    n = len(graph)
    sort = dfs_sort(graph)
    dp = [0 for _ in range(n)]
    dp[b] = 1

    for i in range(n - 1, -1, -1):
        for j in range(len(graph[sort[i]])):
            go_through = graph[sort[i]][j]
            dp[sort[i]] += dp[go_through]
    return dp[a]


if __name__ == '__main__':
    test = [[1, 2, 3, 4],
            [],
            [3],
            [4],
            []]
    print(number_of_paths(test, 0, 3))
