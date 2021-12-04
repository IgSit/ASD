from copy import deepcopy


def floyd_warshall(graph):  # adjacency matrix implementation
    n = len(graph)
    s_arr = deepcopy(graph)

    for t in range(n):
        for u in range(n):
            for v in range(n):
                s_arr[u][v] = s_arr[u][v] or (s_arr[u][t] and s_arr[t][v])

    return s_arr


if __name__ == '__main__':
    test = [[0, 1, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0]]
    res = floyd_warshall(test)
    for i in range(len(res)):
        print(res[i])
