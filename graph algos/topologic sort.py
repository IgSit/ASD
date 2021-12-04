def dfs_sort(graph):

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


if __name__ == '__main__':
    test = [[1, 3],
            [2, 4, 5],
            [3],
            [4],
            [],
            [3, 4],
            [0]]
    print(dfs_sort(test))
