from queue import PriorityQueue
from math import inf


def dijkstra(graph, x, y):  # neighbourhood list implementation
    n = len(graph)
    visited = [False for _ in range(n)]
    dist = [inf for _ in range(n)]
    queue = PriorityQueue()
    dist[x] = 0
    for i in range(n):
        queue.put([dist[i], i])

    while not queue.empty():
        _, v = queue.get()
        if visited[v]:
            continue
        visited[v] = True

        for vertex, distance in graph[v]:
            alter = dist[v] + distance
            if alter < dist[vertex] and not visited[vertex]:
                dist[vertex] = alter
                queue.put([dist[vertex], vertex])

    return dist[y]


def has_common_digit(n1, n2):
    dig1 = [False for _ in range(10)]
    dig2 = [False for _ in range(10)]
    while n1 != 0:
        dig1[n1 % 10] = True
        n1 //= 10
    while n2 != 0:
        dig2[n2 % 10] = True
        n2 //= 10
    for q in range(10):
        if dig1[q] == dig2[q] and dig1[q]:
            return True
    return False


def path_min_max(arr):
    s = arr.index(min(arr))
    t = arr.index(max(arr))

    n = len(arr)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if has_common_digit(arr[i], arr[j]):
                graph[i].append([j, abs(arr[i] - arr[j])])
                graph[j].append([i, abs(arr[i] - arr[j])])

    res = dijkstra(graph, s, t)
    return res if res is not inf else -1
