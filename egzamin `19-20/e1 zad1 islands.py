from queue import PriorityQueue
from math import inf


def islands(graph, s, t):
    n = len(graph)
    visited = [[False for _ in range(3)] for _ in range(n)]
    dist = [[inf for _ in range(3)] for _ in range(n)]
    queue = PriorityQueue()

    dist[s][0] = dist[s][1] = dist[s][2] = 0
    queue.put([0, s, -1, 0])
    queue.put([0, s, -1, 1])
    queue.put([0, s, -1, 2])

    # stan 0 - ostatnia krawedz to krawedz 1
    # stan 1 - krawedz 5
    # stan 2- krawedz 8

    while not queue.empty():
        d, u, last, state = queue.get()
        if visited[u][state]:
            continue
        visited[u][state] = True

        for v in range(n):
            if not graph[u][v]:
                continue
            if graph[u][v] == 1 != last:
                rel_d = d + 1
                if not visited[v][0] and rel_d < dist[v][0]:
                    dist[v][0] = rel_d
                    queue.put([dist[v][0], v, 1, 0])
            if graph[u][v] == 5 != last:
                rel_d = d + 5
                if not visited[v][1] and rel_d < dist[v][1]:
                    dist[v][1] = rel_d
                    queue.put([dist[v][1], v, 5, 1])
            if graph[u][v] == 8 != last:
                rel_d = d + 8
                if not visited[v][2] and rel_d < dist[v][2]:
                    dist[v][2] = rel_d
                    queue.put([dist[v][2], v, 8, 2])

    res = min(dist[t])
    return res if res is not inf else None
