from math import inf


def floyd_warshall(graph, s, k):  # adjacency matrix implementation
    n = len(graph)
    s_arr = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                s_arr[i][j] = graph[i][j]
                parent[i][j] = i
            if i == j:
                s_arr[i][j] = 0

    for t in range(n):
        for u in range(n):
            for v in range(n):
                if s_arr[u][t] + s_arr[t][v] < s_arr[u][v]:
                    s_arr[u][v] = s_arr[u][t] + s_arr[t][v]
                    parent[u][v] = parent[t][v]

    return get_path(parent, s, k), s_arr[s][k]


def get_path(parent, s, t):
    res = []
    while parent[s][t] != -1:
        res.append(t)
        t = parent[s][t]
    res.append(t)
    res.reverse()
    return res


if __name__ == '__main__':
    test = [[0, 1, 0, 0, 2],
            [1, 0, 3, 0, 5],
            [0, 3, 0, 5, 1],
            [0, 0, 5, 0, 1],
            [2, 5, 1, 1, 0]]
    print(floyd_warshall(test, 0, 4))
