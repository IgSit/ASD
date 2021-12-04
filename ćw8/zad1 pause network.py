def how_to_turn_off(graph):
    n = len(graph)
    visited = [False] * n
    res = []

    def dfs_visit(u):
        nonlocal visited, res

        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs_visit(v)
        res.append(u)

    dfs_visit(0)
    return res


if __name__ == '__main__':
    test = [[3, 2, 1],
            [0, 2, 4],
            [3, 1],
            [0, 2, 7],
            [1, 5],
            [4, 9],
            [10, 7],
            [8, 3, 6],
            [7, 10, 9],
            [8, 10, 5],
            [8, 9, 6]]
    print(how_to_turn_off(test))
