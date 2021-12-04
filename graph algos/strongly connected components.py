def strongly_connected(graph):
    n = len(graph)
    visited = [False for _ in range(n)]
    times = []  # dodajemy krotki (wierzch, czas)

    def dfs_time(v):
        nonlocal visited, times, time
        visited[v] = True
        for u in graph[v]:
            if not visited[u]:
                dfs_time(u)
        time += 1
        times.append((v, time))

    time = 0
    for q in range(n):
        if not visited[q]:
            dfs_time(q)
    times.reverse()

    new_graph = [[] for _ in range(n)]
    for vert in range(n):
        for neigh in graph[vert]:
            new_graph[neigh].append(vert)

    visited = [False for _ in range(n)]
    components = []

    def normal_dfs(v, cnt):
        nonlocal visited

        visited[v] = True
        components[cnt].append(v)
        for u in new_graph[v]:
            if not visited[u]:
                normal_dfs(u, cnt)

    counter = 0
    for vertex, _ in times:
        if not visited[vertex]:
            components.append([])
            normal_dfs(vertex, counter)
            counter += 1

    return components


if __name__ == '__main__':
    test = [[2],
            [0, 8],
            [1, 3],
            [4, 5],
            [5],
            [6],
            [3],
            [4, 9],
            [7],
            [5, 10],
            [8]]
    print(strongly_connected(test))
