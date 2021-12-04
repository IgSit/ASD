def has_a_cycle(graph, s=0):
    parents = [-1] * len(graph)

    def dfs_visit(u):
        nonlocal graph, parents, check

        for v in graph[u]:
            if parents[v] == -1:
                parents[v] = u
                dfs_visit(v)
            elif parents[u] != v and parents[v] != -2:
                check = True

    check = False
    parents[s] = -2
    dfs_visit(s)
    return check


if __name__ == '__main__':
    test = [[1, 3],
            [0],
            [3],
            [0, 2]]
    print(has_a_cycle(test))
