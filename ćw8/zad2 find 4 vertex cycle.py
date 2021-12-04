def find_cycle_of_4(graph):
    n = len(graph)
    paths = [0 for _ in range(n)]

    for v in range(n):  # O(n)

        for i in range(n):  # O(n)
            if graph[v][i]:
                for j in range(n):  # O(n)
                    if graph[i][j] and j != v:
                        paths[j] += 1

        for k in range(n):  # O(n)
            if paths[k] >= 2:
                res = [v]
                i = 2
                for q in range(n):  # O(n)
                    if graph[v][q] == graph[k][q] == 1:
                        res.append(q)
                        if i == 1:
                            res.append(k)
                        i -= 1
                    if i == 0:
                        break
                res.append(v)
                print(res)
                return True

    return False


if __name__ == '__main__':
    test = [[0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0]]
    print(find_cycle_of_4(test))
